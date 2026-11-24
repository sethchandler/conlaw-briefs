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

For each brief you will see the new Memory Jogger and Judicial Votes text, any new passages of eight or
more words elsewhere, and the COMPLETE Examples section as it now reads. In Examples, some hypotheticals
are new and some reuse the earlier draft's fact patterns under a new Same-Side / Opposite-Side /
Fence-Sitter label; review all five, including whether each label's outcome fits its facts.

Please check each passage for legal accuracy: case names, citations, votes and joins, holdings,
and whether each example's outcome follows from the case's rule.

"""


def main():
    out = [intro]
    files = sorted(sys.argv[1:], key=lambda p: int(os.path.basename(p).split("_")[0]))
    total = 0
    for p in files:
        d = json.load(open(p, encoding="utf-8"))
        stem = os.path.basename(p)[:-5]
        out.append(f"\n---\n\n## {stem}\n")
        brief = open(os.path.join(os.path.dirname(os.path.dirname(p)), "briefs", stem + ".tex"), encoding="utf-8").read()
        for sec, parts in d["sections"].items():
            if sec == "Examples: Future Applications":
                # Show the whole section as it now reads, so each label can be judged against its facts.
                m = re.search(r"\\section\{Examples: Future Applications\}\s*(.*?)\s*\\section\{", brief, re.S)
                text = m.group(1).strip()
                total += sum(len(x["new"].split()) for x in parts if "new" in x)
                out.append(f"\n### {sec} (complete section as it now reads)\n\n```latex\n{text}\n```\n")
                continue
            new = [x["new"] for x in parts if "new" in x and not SCAFFOLD.match(x["new"])]
            # Short lead-ins and labels (e.g. "Justice Kennedy") make no claims on their own.
            new = [n for n in new if len(n.split()) >= 8 or sec in ("Memory Jogger", "Judicial Votes")]
            if not new:
                continue
            text = "\n\n".join(n.strip() for n in new).strip()
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
