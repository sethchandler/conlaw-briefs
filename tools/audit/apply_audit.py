#!/usr/bin/env python3
"""Validate and apply audit results (results/*.json written by the audit agents).

For every proposed correction:
  - `find` must occur exactly once in the current briefs/<stem>.tex
  - it may not touch a \\section heading or change the start of an example label
  - the replacement may not introduce "Spring 2027" or "casebook"
Rejected corrections are reported with the reason; nothing is half-applied.

Applying:
  - original Group A briefs (case number < 166): edited in place in briefs/
  - converted Group B briefs: appended to fills/corrections/<stem>.json with
    "stage": "post", so tools/check_brief.py re-applies them on every rebuild
All decisions are logged to reports/audit/decisions.json.

usage: apply_audit.py RESULTS_DIR [--dry-run]
"""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LABEL = re.compile(r"\\textbf\{(Same-Side|Opposite-Side|Fence-Sitter) \(")


def problems(c, tex):
    f, r = c.get("find", ""), c.get("replace", "")
    if len(f) < 20:
        return "find shorter than 20 characters"
    n = tex.count(f)
    if n != 1:
        return f"find occurs {n} times"
    if "\\section{" in f or "\\section{" in r:
        return "touches a section heading"
    if LABEL.findall(f) != LABEL.findall(r):
        return "changes an example label's Same/Opposite/Fence prefix"
    if re.search(r"Spring 2027|\bcasebook\b", r, re.I):
        return "introduces a banned phrase"
    if r.count("{") != r.count("}") or f.count("{") - f.count("}") != r.count("{") - r.count("}"):
        return "unbalanced braces in replacement"
    return None


def main():
    res_dir = sys.argv[1]
    dry = "--dry-run" in sys.argv
    log = []
    for rp in sorted(glob.glob(os.path.join(res_dir, "group*.json"))):
        for entry in json.load(open(rp, encoding="utf-8")):
            stem = entry["brief"]
            path = os.path.join(ROOT, "briefs", stem + ".tex")
            tex = open(path, encoding="utf-8").read()
            group_b = int(stem.split("_")[0]) >= 166
            post = []
            for i, c in enumerate(entry.get("corrections", [])):
                why = problems(c, tex)
                rec = {"brief": stem, "id": f"audit.{i + 1}", **{k: c.get(k) for k in
                       ("category", "severity", "find", "replace", "reason", "source")}}
                if why:
                    rec["decision"] = f"REJECTED: {why}"
                else:
                    rec["decision"] = "APPLIED"
                    tex = tex.replace(c["find"], c["replace"])     # later finds see earlier edits
                    if group_b:
                        post.append({**rec, "stage": "post"})
                log.append(rec)
            for r in entry.get("restore", []):
                log.append({"brief": stem, "id": "restore", "decision": "PROPOSED RESTORE", **r})
            for note in entry.get("unresolved", []):
                log.append({"brief": stem, "id": "unresolved", "decision": "UNRESOLVED", "reason": note})
            log.append({"brief": stem, "id": "ok", "decision": "VERIFIED OK", "count": len(entry.get("resolved_ok", [])),
                        "notes": entry.get("resolved_ok", [])})
            if dry:
                continue
            if group_b:
                if post:
                    cp = os.path.join(ROOT, "fills", "corrections", stem + ".json")
                    existing = json.load(open(cp, encoding="utf-8")) if os.path.exists(cp) else []
                    existing = [c for c in existing if not str(c.get("id", "")).startswith("audit.")]
                    json.dump(existing + post, open(cp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
            else:
                open(path, "w", encoding="utf-8").write(tex)
    os.makedirs(os.path.join(ROOT, "reports", "audit"), exist_ok=True)
    if not dry:
        json.dump(log, open(os.path.join(ROOT, "reports", "audit", "decisions.json"), "w", encoding="utf-8"),
                  indent=1, ensure_ascii=False)
    from collections import Counter
    print(Counter(r["decision"].split(":")[0] for r in log if r["id"].startswith("audit")))
    for r in log:
        if r["decision"].startswith("REJECTED"):
            print("  ", r["brief"], r["id"], r["decision"])


if __name__ == "__main__":
    main()
