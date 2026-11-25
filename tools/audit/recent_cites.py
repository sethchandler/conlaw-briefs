#!/usr/bin/env python3
r"""List every 2024-2026 decision cited in the briefs (current text) and in the
original drafts (including passages later dropped), and check Supreme Court
citations against the Court's own slip-opinion lists (terms 2023-2025).

A citation is an italic case name (\textit{A v. B} or \emph{...}) followed within
~160 characters by a year 2024-2026, or a docket number "No. 24-123".

usage: recent_cites.py BRIEFS_DIR ORIGINALS_DIR OUT.json
"""
import glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fetch_sources as fs

fs.SLIP_TERMS = ["23", "24", "25"]
CITE = re.compile(r"\\(?:textit|emph)\{((?:[^{}]|\{[^{}]*\})*?\bv\.(?:[^{}]|\{[^{}]*\})*?)\}(.{0,160}?)\((?:[^()]*?)(202[4-6])\)", re.S)
LOWER = re.compile(r"(\d+(?:st|nd|rd|th) Cir\.|D\.C\. Cir\.|Fed\. Cir\.|[A-Z]\.D\. [A-Z][a-z]+\.|Cal\.|Tex\.|Colo\.)")


def clean(name):
    name = re.sub(r"\\[a-z]+\s*", "", name).replace("{", "").replace("}", "").replace("~", " ")
    return re.sub(r"\s+", " ", name).strip(" ,")


def main():
    briefs_dir, orig_dir, out_p = sys.argv[1:4]
    idx = fs.slip_index()
    cites = {}
    for label, d in (("current", briefs_dir), ("original", orig_dir)):
        for path in glob.glob(os.path.join(d, "*.tex")):
            stem = os.path.basename(path)[:-4]
            t = open(path, encoding="utf-8").read()
            for m in CITE.finditer(t):
                name, between, year = clean(m.group(1)), m.group(2), m.group(3)
                court = "lower" if LOWER.search(between) else "scotus?"
                key = (fs.norm(name), year)
                c = cites.setdefault(key, {"name": name, "year": year, "court": court, "current": set(), "original": set()})
                c[label].add(stem)
                if court == "lower":
                    c["court"] = "lower"
    out = []
    for (key, year), c in sorted(cites.items(), key=lambda kv: kv[1]["name"]):
        hit = next((u for n, u in idx["name"].items() if n == key or (len(key) > 10 and (n.startswith(key) or key.startswith(n)))), None)
        c["scotus_slip"] = hit
        c["verified"] = bool(hit)
        c["current"], c["original"] = sorted(c["current"]), sorted(c["original"])
        c["dropped_only"] = bool(c["original"]) and not c["current"]
        out.append(c)
    json.dump(out, open(out_p, "w"), indent=1)
    v = sum(c["verified"] for c in out)
    print(f"{len(out)} distinct 2024-26 citations; {v} matched to a Supreme Court slip opinion; "
          f"{sum(c['court']=='lower' for c in out)} marked as lower-court; "
          f"{sum(c['dropped_only'] for c in out)} appear only in original drafts (dropped)")


if __name__ == "__main__":
    main()
