#!/usr/bin/env python3
"""Rebuild a Group B brief in the Group A (case-briefer) template.

Every output section is a list of parts. A part either copies text verbatim
from the original brief (checked: it must exist in the source) or is flagged
as new text. A provenance report counts moved vs. new words per brief.

Part kinds:
  {"new": "<latex>"}                         new text (counted, reported)
  {"src": "<exact substring of original>"}   verbatim copy
  {"sec": "<B section title>", "from": a, "to": b, "strip": s}
        slice of that section's body, starting at anchor a (inclusive),
        ending before anchor b; optional literal prefix s removed.
  {"items": "<B section title>", "from": a, "to": b}
        like "sec", but each "\\item \\textbf{Label:} body" in the slice is
        turned into a "\\textbf{Label:} body" paragraph (itemize wrappers dropped).

Any part may carry "glue": the separator written after it (default a blank
line; use " " to continue the same paragraph, e.g. after an \\item label).

usage: assemble.py SOURCE.tex FILLS.json OUT.tex
"""
import json, os, re, sys

A_SECTIONS = ["Memory Jogger", "Detailed Case Facts", "Procedural History",
              "Judicial Votes", "Holding", "Analysis of Opinions",
              "Examples: Future Applications", "Critique", "Key Quotations"]

PREAMBLE = r"""\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[margin=1in]{geometry}
\usepackage{setspace}
\usepackage{xcolor}
\usepackage[colorlinks=true, urlcolor=blue!60!black, linkcolor=blue!60!black]{hyperref}
\setlength{\parindent}{2em}
\setlength{\parskip}{1.25em}
\renewcommand{\baselinestretch}{1.0}
\begin{document}
\begin{center}
{\LARGE %s\par}
\vspace{0.8em}
{\large Case Brief\par}
\end{center}
\vspace{1em}
"""


def parse_sections(text):
    body = text.split(r"\begin{document}", 1)[1].rsplit(r"\end{document}", 1)[0]
    parts = re.split(r"^\\section\{(.+?)\}[ \t]*$", body, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


def find_sec(secs, name):
    if name in secs:
        return secs[name]
    hits = [k for k in secs if k.lower().startswith(name.lower())]
    if len(hits) != 1:
        raise SystemExit(f"section {name!r} not found uniquely; have {list(secs)}")
    return secs[hits[0]]


def slice_(body, a, b, what):
    i = 0
    if a:
        i = body.find(a)
        if i < 0:
            raise SystemExit(f"anchor not found in {what}: {a[:60]!r}")
    j = len(body)
    if b:
        j = body.find(b, i)
        if j < 0:
            raise SystemExit(f"end anchor not found in {what}: {b[:60]!r}")
    return body[i:j]


ITEM_RE = re.compile(r"^\s*\\item\s+(\\textbf\{)", re.M)


def items_to_paragraphs(s):
    s = re.sub(r"^\s*\\(begin|end)\{itemize\}\s*$", "", s, flags=re.M)
    s = ITEM_RE.sub(r"\n\1", s)
    return s


def words(s):
    return len(re.findall(r"[A-Za-z]{2,}", re.sub(r"\\href\{[^}]*\}", "", s)))


def build(src_text, fills):
    secs = parse_sections(src_text)
    title = re.search(r"\\title\{(.+)\}\s*$", src_text, re.M).group(1)
    out, stats, new_chunks = [PREAMBLE % title], {"moved": 0, "new": 0}, []
    for name in A_SECTIONS:
        out.append(f"\n\\section{{{name}}}\n")
        for p in fills["sections"][name]:
            if "new" in p:
                t = p["new"]; stats["new"] += words(t); new_chunks.append((name, t))
            elif "src" in p:
                t = p["src"]
                if t not in src_text:
                    raise SystemExit(f"[{name}] src text not in original: {t[:70]!r}")
                stats["moved"] += words(t)
            elif "sec" in p:
                t = slice_(find_sec(secs, p["sec"]), p.get("from"), p.get("to"), p["sec"])
                if p.get("strip"):
                    if not t.lstrip().startswith(p["strip"]):
                        raise SystemExit(f"[{name}] strip prefix missing: {p['strip']!r}")
                    t = t.lstrip()[len(p["strip"]):]
                if p.get("lcfirst"):  # only change allowed to moved text: lowercase first letter after a new subject
                    t = t.lstrip(); t = t[:1].lower() + t[1:]
                stats["moved"] += words(t)
            elif "items" in p:
                t = items_to_paragraphs(slice_(find_sec(secs, p["items"]), p.get("from"), p.get("to"), p["items"]))
                stats["moved"] += words(t)
            else:
                raise SystemExit(f"bad part {p}")
            out.append(t.strip("\n").strip() + p.get("glue", "\n\n"))
    out.append("\\end{document}\n")
    tex = re.sub(r"\n{3,}", "\n\n", "".join(out))
    # Reviewed corrections (fills/corrections/<stem>.json): exact find/replace on the
    # assembled brief, whether the text was moved or new. Each find must occur once.
    for c in fills.get("_corrections", []):
        n = tex.count(c["find"])
        if n != 1:
            raise SystemExit(f"correction {c.get('id')}: find occurs {n} times: {c['find'][:70]!r}")
        tex = tex.replace(c["find"], c["replace"])
        stats["new"] += max(0, words(c["replace"]) - words(c["find"]))
        stats["corrected"] = stats.get("corrected", 0) + 1
    return tex, stats, new_chunks, list(secs)


def main():
    src, fills_p, dst = sys.argv[1:4]
    src_text = open(src, encoding="utf-8").read()
    fills = json.load(open(fills_p, encoding="utf-8"))
    corr_p = os.path.join(os.path.dirname(os.path.abspath(fills_p)), "corrections", os.path.basename(fills_p))
    if os.path.exists(corr_p):
        fills["_corrections"] = [c for c in json.load(open(corr_p, encoding="utf-8")) if c.get("decision", "").startswith("APPLIED")]
    tex, stats, new_chunks, b_secs = build(src_text, fills)
    # sanity: balanced braces / environments, banned strings
    assert tex.count("{") == tex.count("}"), "unbalanced braces"
    for env in set(re.findall(r"\\begin\{(\w+)\}", tex)):
        assert tex.count(f"\\begin{{{env}}}") == tex.count(f"\\end{{{env}}}"), f"unbalanced {env}"
    assert "Spring 2027" not in tex
    open(dst, "w", encoding="utf-8").write(tex)
    # which original sections were never drawn from at all?
    used = {p.get("sec") or p.get("items") for s in fills["sections"].values() for p in s}
    report = {"file": src.split("/")[-1], "moved_words": stats["moved"], "new_words": stats["new"],
              "corrections_applied": stats.get("corrected", 0),
              "dropped": fills.get("dropped", []), "notes": fills.get("notes", []),
              "b_sections_unreferenced_by_slice": [k for k in b_secs if not any(u and k.lower().startswith(u.lower()) for u in used)]}
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
