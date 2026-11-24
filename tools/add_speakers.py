#!/usr/bin/env python3
r"""Add the speaker to Key Quotations attribution lines that give only a cite.

Some originals attributed quotations with a page cite alone, e.g.
"\noindent --- 74 U.S. at 514." For the briefs below, every such quotation was
checked to come from the opinion named (single-opinion or unanimous cases; the
cited pages fall inside the majority opinion; Mahmoud v. Taylor checked against
the slip opinion text on CourtListener). The speaker is prefixed:
"\noindent --- Chief Justice Chase, Opinion of the Court, 74 U.S. at 514."

Only lines with no speaker are touched; running it twice changes nothing.
usage: add_speakers.py FILE.tex ...
"""
import os, re, sys

SPEAKERS = {
    "13_bolling_v_sharpe": "Chief Justice Warren, Opinion of the Court",
    "17_brown_v_board_of_education_ii": "Chief Justice Warren, Opinion of the Court",
    "18_buck_v_bell": "Justice Holmes, Opinion of the Court",
    "166_ex_parte_mccardle": "Chief Justice Chase, Opinion of the Court",
    "167_cooper_v_aaron": "Opinion of the Court (jointly signed by all nine Justices)",
    "168_abbott_laboratories_v_gardner": "Justice Harlan, Opinion of the Court",
    "169_myers_v_united_states": "Chief Justice Taft, Opinion of the Court",
    "191_shelley_v_kraemer": "Chief Justice Vinson, Opinion of the Court",
    "203_cohen_v_california": "Justice Harlan, Opinion of the Court",
    "215_mahmoud_v_taylor": "Justice Alito, Opinion of the Court",
}
HAS_SPEAKER = re.compile(r"Justice|\bJ\.|C\.\s?J\.|[Pp]er [Cc]uriam|Judge|[Oo]pinion|concurr|dissent|"
                         r"[Mm]ajority|plurality|Court|Chase|Marshall|Story|Taney|Washington")


def fix(path):
    stem = os.path.basename(path)[:-4]
    if stem not in SPEAKERS:
        return 0
    head, sep, kq = open(path, encoding="utf-8").read().partition("\\section{Key Quotations}")
    n = 0

    def sub(m):
        nonlocal n
        if HAS_SPEAKER.search(m.group(1)):
            return m.group(0)
        n += 1
        return f"\\noindent --- {SPEAKERS[stem]}, {m.group(1)}"
    kq = re.sub(r"\\noindent --- (.*)", sub, kq)
    if n:
        open(path, "w", encoding="utf-8").write(head + sep + kq)
    return n


if __name__ == "__main__":
    print("speakers added:", sum(fix(p) for p in sys.argv[1:]))
