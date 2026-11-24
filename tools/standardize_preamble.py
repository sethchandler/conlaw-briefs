#!/usr/bin/env python3
r"""Give a standalone brief the main Group A preamble and centered title block.

Replaces everything before the first \section with the canonical preamble and
a centered title built from the brief's \title{...} (or its existing centered
title block). The body from the first \section onward is untouched.
Briefs already in the canonical form are left byte-for-byte unchanged.

usage: standardize_preamble.py FILE.tex ...
"""
import re, sys

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


def title_of(head):
    m = re.search(r"^\\title\{(.+)\}\s*$", head, re.M)
    if m:
        return m.group(1)
    m = re.search(r"\{\\LARGE (.+?)\\par\}", head)
    if m:
        return m.group(1)
    raise SystemExit("no title found")


def main():
    changed = 0
    for f in sys.argv[1:]:
        t = open(f, encoding="utf-8").read()
        i = t.index("\\section{")
        new = PREAMBLE % title_of(t[:i]) + t[i:]
        if new != t:
            open(f, "w", encoding="utf-8").write(new)
            changed += 1
    print(f"standardized {changed} of {len(sys.argv) - 1}")


if __name__ == "__main__":
    main()
