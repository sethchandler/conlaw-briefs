#!/usr/bin/env python3
"""Build Seth J. Chandler's Constitutional Law Briefing Book from standalone .tex briefs.

Reads a master .zip of untouched standalone LaTeX case briefs plus a JSON manifest
and chapters.json, assembles a single combined .tex Briefing Book (organized into
2 parts and 10 chapters, chronologically within each chapter, plus an Alphabetical
Table of Cases), and optionally compiles a 3-pass PDF via pdflatex.

Usage:
    python3 update_briefing_book.py \
        --zip conlaw_briefs_1_247_tex_master.zip \
        --manifest cases_manifest_247.json \
        --chapters chapters.json \
        --out conlaw_briefing_book_247.tex \
        --compile
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from collections import defaultdict


BOOK_PREAMBLE = r"""\documentclass[11pt,openany]{book}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=1in,headheight=14pt]{geometry}
\usepackage{setspace}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage[colorlinks=true,urlcolor=blue!60!black,linkcolor=blue!60!black,citecolor=blue!60!black,bookmarksdepth=2,pdftitle={Constitutional Law: Briefing Book},pdfauthor={Seth J. Chandler}]{hyperref}

\setlength{\parindent}{2em}
\setlength{\parskip}{0.85em}
\renewcommand{\baselinestretch}{1.0}
\setcounter{tocdepth}{1}
\setcounter{secnumdepth}{1}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\small\itshape\nouppercase{\leftmark}}
\fancyhead[RO]{\small\itshape\nouppercase{\rightmark}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}\renewcommand{\headrulewidth}{0pt}}
\raggedbottom

\begin{document}
\frontmatter
\begin{titlepage}
\centering
\vspace*{2.2in}
{\Huge\bfseries Constitutional Law\par}
\vspace{0.6em}
{\Large\itshape Briefing Book (NUM_CASES Decisions)\par}
\vspace{1.8em}
\rule{0.45\textwidth}{0.6pt}\par
\vspace{1.8em}
{\large Seth J. Chandler\par}
\vspace{0.4em}
{\normalsize University of Houston Law Center\par}
\vfill
{\small Organized by Constitutional Area and Chronologically Within Each Chapter\par}
\end{titlepage}
\tableofcontents
\clearpage
\mainmatter
"""


def tex_escape(text: str) -> str:
    """Escape unescaped & and % for LaTeX headings/entries."""
    text = re.sub(r"(?<!\\)&", r"\\&", text)
    text = re.sub(r"(?<!\\)%", r"\\%", text)
    return text


def shorten_toc_title(title: str, max_len: int = 44) -> str:
    if len(title) <= max_len:
        return title
    return title[: max_len - 3].rstrip() + "..."


def transform_brief_body(raw_tex: str, filename: str = "") -> str:
    """Strip standalone preamble/document wrappers and demote section headings."""
    m = re.search(r"\\begin\{document\}(.*)\\end\{document\}", raw_tex, re.DOTALL)
    body = m.group(1) if m else raw_tex
    body = re.sub(r"\\maketitle\b", "", body)
    # Demote top-level headings so each case sits cleanly under \section[...]
    body = re.sub(r"\\subsubsection\*?\{", r"\\paragraph{", body)
    body = re.sub(r"\\subsection\*?\{", r"\\subsubsection*{", body)
    body = re.sub(r"\\section\*?\{", r"\\subsection*{", body)
    return body.strip()


def load_zip_by_case_num(zip_path: str) -> dict:
    """Map integer case number -> (filename, utf8 text) from a master .zip."""
    mapping = {}
    with zipfile.ZipFile(zip_path, "r") as zf:
        for name in zf.namelist():
            if not name.endswith(".tex"):
                continue
            base = os.path.basename(name)
            m = re.match(r"^(\d+)_", base)
            if not m:
                continue
            num = int(m.group(1))
            mapping[num] = (base, zf.read(name).decode("utf-8", errors="replace"))
    return mapping


def build_briefing_book(zip_path: str, manifest: list, chapters_cfg: dict, out_tex: str) -> None:
    briefs_by_num = load_zip_by_case_num(zip_path)

    topic_to_chap = {}
    chap_by_num = {}
    for ch in chapters_cfg["chapters"]:
        chap_by_num[ch["number"]] = ch
        for t in ch.get("topics", []):
            topic_to_chap[t] = ch["number"]

    cases_by_chap = defaultdict(list)
    for entry in manifest:
        num = int(entry["num"])
        if num not in briefs_by_num:
            raise FileNotFoundError(f"Case #{num} ({entry['title']}) missing from {zip_path}")
        ch_num = entry.get("chapter") or topic_to_chap.get(entry.get("topic", ""))
        if not ch_num:
            raise ValueError(f"No chapter mapping for case #{num} ({entry['title']})")
        cases_by_chap[int(ch_num)].append(entry)

    out_lines = [BOOK_PREAMBLE.replace("NUM_CASES", str(len(manifest)))]

    for part in chapters_cfg["parts"]:
        out_lines.append(f"\n\\part{{{tex_escape(part['title'])}}}\n")
        for ch_num in part["chapters"]:
            ch = chap_by_num[ch_num]
            ch_cases = sorted(
                cases_by_chap[ch_num],
                key=lambda c: (int(c["year"]), c["title"].lower()),
            )
            out_lines.append(f"\\chapter{{{tex_escape(ch['title'])}}}\n")
            out_lines.append("\\noindent\\textbf{Cases in This Chapter (Chronological Order):}\n")
            out_lines.append("\\begin{enumerate}\\setlength{\\itemsep}{2pt}\\setlength{\\parskip}{0pt}\n")
            for c in ch_cases:
                cid = f"case:{int(c['num']):03d}"
                t_esc = tex_escape(c["title"])
                c_esc = tex_escape(c["citation"])
                out_lines.append(
                    f"\\item \\hyperref[{cid}]{{\\textit{{{t_esc}}}}}, {c_esc} \\dotfill\\ \\pageref{{{cid}}}\n"
                )
            out_lines.append("\\end{enumerate}\n")

            for c in ch_cases:
                num = int(c["num"])
                cid = f"case:{num:03d}"
                fname, raw_tex = briefs_by_num[num]
                body = transform_brief_body(raw_tex, fname)
                if "Spring 2027" in body:
                    raise ValueError(f"Found disallowed 'Spring 2027' in {fname}")
                t_esc = tex_escape(c["title"])
                c_esc = tex_escape(c["citation"])
                toc_t = tex_escape(shorten_toc_title(c["title"]))
                topic_esc = tex_escape(c.get("topic", ""))
                url = c.get("url", "")
                url_label = tex_escape(c.get("url_label", "Primary Opinion"))
                link_part = f" \\quad$\\cdot$\\quad \\href{{{url}}}{{{url_label}}}" if url else ""

                out_lines.append(f"\n% --- Case #{num:03d} ({c['year']}): {c['title']} [{fname}] ---\n")
                out_lines.append("\\clearpage\n")
                out_lines.append(
                    f"\\section[{toc_t} ({c['year']})]{{\\textit{{{t_esc}}}, {c_esc}}}\n"
                )
                out_lines.append(f"\\label{{{cid}}}\n")
                out_lines.append(
                    f"\\noindent{{\\small\\textit{{Course Unit:}} {topic_esc}{link_part}}}\\par\\vspace{{0.4em}}\n"
                )
                out_lines.append(body + "\n")

    # Alphabetical Table of Cases
    out_lines.append("\n\\clearpage\n\\chapter{Alphabetical Table of Cases}\n{\\small\n")
    all_sorted = sorted(manifest, key=lambda c: c["title"].lower())
    for c in all_sorted:
        num = int(c["num"])
        cid = f"case:{num:03d}"
        ch_num = c.get("chapter") or topic_to_chap[c["topic"]]
        t_esc = tex_escape(c["title"])
        c_esc = tex_escape(c["citation"])
        out_lines.append(
            f"\\noindent\\hangindent=1.5em \\hyperref[{cid}]{{\\textit{{{t_esc}}}}}, "
            f"{c_esc} (Ch.\\ {ch_num}) \\dotfill\\ \\pageref{{{cid}}}\\par\n"
        )
    out_lines.append("}\n\\end{document}\n")

    full_book = "".join(out_lines)
    with open(out_tex, "w", encoding="utf-8") as f:
        f.write(full_book)
    print(f"Wrote {out_tex} ({len(full_book):,} chars, {len(manifest)} cases)")


def compile_pdf(tex_path: str) -> None:
    pdflatex = shutil.which("pdflatex") or "/Library/TeX/texbin/pdflatex"
    if not os.path.exists(pdflatex):
        raise RuntimeError("pdflatex not found in PATH or /Library/TeX/texbin/pdflatex")
    workdir = os.path.dirname(os.path.abspath(tex_path)) or "."
    tex_name = os.path.basename(tex_path)
    for i in (1, 2, 3):
        print(f"Running pdflatex pass {i}/3...")
        res = subprocess.run(
            [pdflatex, "-interaction=nonstopmode", "-halt-on-error", tex_name],
            cwd=workdir,
            capture_output=True,
            text=True,
            errors="replace",
        )
        if res.returncode != 0:
            print("pdflatex failed! Last 2500 chars of output:")
            print(res.stdout[-2500:])
            sys.exit(1)
    log_path = os.path.splitext(tex_path)[0] + ".log"
    with open(log_path, "r", encoding="utf-8", errors="replace") as f:
        log_txt = f.read()
    undef = re.findall(r"LaTeX Warning:.*(?:undefined|Reference|Citation).*", log_txt)
    pages_m = re.search(r"Output written on .*?\.pdf \((\d+) pages", log_txt)
    pages = pages_m.group(1) if pages_m else "unknown"
    print(f"PDF compiled cleanly: {pages} pages, {len(undef)} undefined ref/citation warnings.")


def main():
    p = argparse.ArgumentParser(description="Build Constitutional Law Briefing Book .tex / .pdf")
    p.add_argument("--zip", required=True, help="Path to master .zip of standalone .tex briefs")
    p.add_argument("--manifest", required=True, help="Path to cases_manifest_*.json")
    p.add_argument("--chapters", default="chapters.json", help="Path to chapters.json")
    p.add_argument("--out", required=True, help="Output combined .tex path")
    p.add_argument("--compile", action="store_true", help="Compile 3-pass PDF via pdflatex")
    args = p.parse_args()

    with open(args.manifest, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    with open(args.chapters, "r", encoding="utf-8") as f:
        chapters_cfg = json.load(f)

    build_briefing_book(args.zip, manifest, chapters_cfg, args.out)
    if args.compile:
        compile_pdf(args.out)


if __name__ == "__main__":
    main()
