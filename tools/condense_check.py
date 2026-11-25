#!/usr/bin/env python3
r"""Check the three condensed editions of one brief.

For STEM, expects:
  condensed/4page/STEM.tex, condensed/2page/STEM.tex, condensed/1page/STEM.tex
  condensed/signature/STEM.json   (quotation ranking; see condensed/CONDENSE_GUIDE.md)

Checks: each edition compiles with no errors, no LaTeX warnings, no overfull boxes;
exact page count (4 / 2 / 1) with a reasonably full last page; required headings;
every quotation of three or more words is verbatim in the full brief (or is the
verified nominated passage in the signature file); the top-ranked quotation appears
in all three editions and the top three in the 4-page edition; no banned phrases.

Prints one JSON line: {"stem", "pass", "problems", "pages"}.
usage: condense_check.py STEM [STEM ...]
"""
import json, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTIONS = ["Memory Jogger", "Detailed Case Facts", "Procedural History", "Judicial Votes", "Holding",
            "Analysis of Opinions", "Examples: Future Applications", "Critique", "Key Quotations"]
LABELS_1 = ["Memory Jogger.", "Facts.", "Procedural History.", "Votes.", "Holding.", "Reasoning.",
            "Examples.", "Critique.", "Key Quotation."]
TARGET = {"4page": 4, "2page": 2, "1page": 1}
MIN_LAST_LINES = {"4page": 12, "2page": 15, "1page": 26}
SUBTITLE = {"4page": "Four-Page Edition", "2page": "Two-Page Edition", "1page": "One-Page Edition"}


def norm(s):
    s = re.sub(r"\\[a-zA-Z]+\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+\s*", " ", s)
    s = s.replace("[", "").replace("]", "")
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def key(text, n=12):
    """First n words of a quotation, normalized: enough to identify it."""
    return " ".join(norm(text).split()[:n])


def check(stem):
    probs, pages = [], {}
    full_p = os.path.join(ROOT, "briefs", stem + ".tex")
    sig_p = os.path.join(ROOT, "condensed", "signature", stem + ".json")
    if not os.path.exists(sig_p):
        return {"stem": stem, "pass": False, "problems": ["missing condensed/signature/%s.json" % stem]}
    sig = json.load(open(sig_p, encoding="utf-8"))
    cands = sorted(sig.get("candidates", []), key=lambda c: c.get("rank", 99))
    allowed = norm(open(full_p, encoding="utf-8").read())
    nominated = [norm(c["text"]) for c in cands if c.get("source") == "nominated" and c.get("verified_in")]
    if not cands:
        probs.append("signature file has no candidates")
    for ed in ("4page", "2page", "1page"):
        p = os.path.join(ROOT, "condensed", ed, stem + ".tex")
        if not os.path.exists(p):
            probs.append(f"{ed}: missing"); continue
        tex = open(p, encoding="utf-8").read()
        if SUBTITLE[ed] not in tex:
            probs.append(f"{ed}: subtitle '{SUBTITLE[ed]}' missing")
        if ed == "1page":
            missing = [l for l in LABELS_1 if f"\\textbf{{{l}}}" not in tex]
            if missing: probs.append(f"1page: missing labels {missing}")
        else:
            secs = re.findall(r"^\\section\{(.+?)\}", tex, re.M)
            if secs != SECTIONS: probs.append(f"{ed}: sections are {secs}")
        if re.search(r"Spring 2027|\bcasebook\b", tex, re.I):
            probs.append(f"{ed}: banned phrase")
        for q in re.findall(r"``(.+?)''", tex, re.S):
            if len(q.split()) >= 3:
                nq = norm(q)
                if nq not in allowed and not any(nq in n for n in nominated):
                    probs.append(f"{ed}: quotation not verbatim in full brief: {q[:70]!r}")
        need = cands[:3] if ed == "4page" else cands[:1]
        body = norm(tex)
        for c in need:
            if key(c["text"]) not in body:
                probs.append(f"{ed}: ranked quotation #{c.get('rank')} missing: {c['text'][:60]!r}")
        with tempfile.TemporaryDirectory() as d:
            r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", p], cwd=d,
                               capture_output=True, text=True, errors="replace")
            log = open(os.path.join(d, stem + ".log"), errors="replace").read()
            if r.returncode:
                probs.append(f"{ed}: pdflatex error " + " | ".join(re.findall(r"^!.*", log, re.M)[:2])); continue
            m = re.search(r"\((\d+)\s+pages?", log)
            n = int(m.group(1)) if m else 0
            pages[ed] = n
            if n != TARGET[ed]:
                probs.append(f"{ed}: {n} pages (target {TARGET[ed]})")
            if re.search(r"Overfull|LaTeX Warning", log):
                probs.append(f"{ed}: " + "; ".join(re.findall(r"(Overfull[^\n]*|LaTeX Warning[^\n]*)", log)[:2]))
            if n == TARGET[ed]:
                last = subprocess.run(["pdftotext", "-f", str(n), "-l", str(n), "-layout",
                                       os.path.join(d, stem + ".pdf"), "-"], capture_output=True, text=True).stdout
                lines = len([l for l in last.split("\n") if l.strip()])
                if lines < MIN_LAST_LINES[ed]:
                    probs.append(f"{ed}: last page too empty ({lines} lines; want >= {MIN_LAST_LINES[ed]})")
    return {"stem": stem, "pass": not probs, "problems": probs, "pages": pages}


if __name__ == "__main__":
    for s in sys.argv[1:]:
        print(json.dumps(check(os.path.basename(s).removesuffix(".tex").removesuffix(".json"))))
