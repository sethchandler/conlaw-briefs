#!/usr/bin/env python3
"""Write reports/NEW_TEXT_FOR_REVIEW.md: only the newly written text in each
converted brief, grouped by brief and section, plus what was dropped.

Structural scaffolding (\\begin{itemize}, subsection headings, "Questions
Presented:" labels, quote/attribution wrappers) is omitted so a reviewer sees
only prose that makes claims.

usage: review_export.py fills/*.json > reports/NEW_TEXT_FOR_REVIEW.md
"""
import json, os, re, sys

SCAFFOLD = re.compile(r"^\s*(\\(begin|end)\{(itemize|enumerate|quote)\}|\\subsection\{[^}]*\}|\\textbf\{(Questions Presented|Holding):\}|\\noindent ---|\.)\s*$")

intro = """# New text for independent review

This file contains **only the text newly written** when the Group B briefs were rebuilt in the Group A
(case-briefer) template. Everything else in those briefs was moved verbatim from the original drafts.

Please check each passage for legal accuracy: case names, citations, votes and joins, holdings,
and whether each example's outcome follows from the case's rule. Flag anything wrong with the brief
name, section, and a corrected wording.

"""


def main():
    out = [intro]
    files = sorted(sys.argv[1:], key=lambda p: int(os.path.basename(p).split("_")[0]))
    total = 0
    for p in files:
        d = json.load(open(p, encoding="utf-8"))
        stem = os.path.basename(p)[:-5]
        out.append(f"\n---\n\n## {stem}\n")
        for sec, parts in d["sections"].items():
            new = [x["new"] for x in parts if "new" in x and not SCAFFOLD.match(x["new"])]
            if not new:
                continue
            text = " ".join(new).strip()
            total += len(text.split())
            out.append(f"\n### {sec}\n\n```latex\n{text}\n```\n")
        if d.get("dropped"):
            out.append("\n**Dropped from the original:**\n" + "".join(f"\n- {x}" for x in d["dropped"]) + "\n")
        if d.get("notes"):
            out.append("\n**Notes:**\n" + "".join(f"\n- {x}" for x in d["notes"]) + "\n")
    out.insert(1, f"Briefs: {len(files)}. New words: about {total:,}.\n")
    sys.stdout.write("".join(out))


if __name__ == "__main__":
    main()
