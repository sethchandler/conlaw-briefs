#!/usr/bin/env python3
r"""Build one converted brief from its fill and apply every acceptance check.

Steps: run fills/src/<stem>.py -> fills/<stem>.json; tools/assemble.py builds
briefs/<stem>.tex from originals/briefs/<stem>.tex (rejecting any moved text
that is not verbatim); quotations are converted to Group A style by
tools/normalize_quotes.py unless the brief is listed in tools/manual_quotes.txt
(then the fill must already build them in Group A style); then the checks below.

Prints one JSON line: {"stem", "pass", "problems", "moved_words", "new_words", "pages"}
usage: check_brief.py STEM [STEM ...]
"""
import json, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A_SECTIONS = ["Memory Jogger", "Detailed Case Facts", "Procedural History", "Judicial Votes",
              "Holding", "Analysis of Opinions", "Examples: Future Applications", "Critique",
              "Key Quotations"]
MANUAL = {s.removesuffix(".tex") for s in open(os.path.join(ROOT, "tools", "manual_quotes.txt")).read().split()}  # informational
NEW_WORD_LIMIT = 1100


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, errors="replace", **kw)


def check(stem):
    probs, info = [], {"stem": stem}
    src_py = os.path.join(ROOT, "fills", "src", stem + ".py")
    if not os.path.exists(src_py):
        return {**info, "pass": False, "problems": ["missing fills/src/%s.py" % stem]}
    r = run([sys.executable, src_py], cwd=ROOT, env={**os.environ, "PYTHONPATH": os.path.join(ROOT, "tools")})
    if r.returncode:
        return {**info, "pass": False, "problems": ["fill script failed: " + r.stderr.strip()[-400:]]}
    out_tex = os.path.join(ROOT, "briefs", stem + ".tex")
    r = run([sys.executable, os.path.join(ROOT, "tools", "assemble.py"),
             os.path.join(ROOT, "originals", "briefs", stem + ".tex"),
             os.path.join(ROOT, "fills", stem + ".json"), out_tex])
    if r.returncode:
        return {**info, "pass": False, "problems": ["assemble failed: " + (r.stderr or r.stdout).strip()[-400:]]}
    rep = json.loads(r.stdout)
    info.update(moved_words=rep["moved_words"], new_words=rep["new_words"])
    # Convert attributions to Group A style. A fill may already build them in
    # Group A style (required for briefs in manual_quotes.txt); that is fine too.
    q = run([sys.executable, os.path.join(ROOT, "tools", "normalize_quotes.py"), out_tex])
    if "converted: 1" not in q.stdout and "already Group A style" not in q.stdout:
        probs.append("quotation conversion failed: " + q.stdout.strip()[:200])
    tex = open(out_tex, encoding="utf-8").read()

    secs = re.findall(r"^\\section\{(.+?)\}", tex, re.M)
    if secs != A_SECTIONS:
        probs.append(f"sections are {secs}")
    ex = re.search(r"\\section\{Examples: Future Applications\}(.*?)\\section\{Critique\}", tex, re.S)
    if ex:
        labels = re.findall(r"\\item\s+\\textbf\{(Same-Side|Opposite-Side|Fence-Sitter)", ex.group(1))
        if sorted(labels) != sorted(["Same-Side"] * 2 + ["Opposite-Side"] * 2 + ["Fence-Sitter"]) \
                or len(re.findall(r"\\item\b", ex.group(1))) != 5:
            probs.append(f"examples must be 5 items labeled 2 Same-Side, 2 Opposite-Side, 1 Fence-Sitter; got {labels}")
    kq = re.search(r"\\section\{Key Quotations\}(.*?)\\end\{document\}", tex, re.S)
    if kq:
        n_q = len(re.findall(r"\\begin\{quote\}", kq.group(1)))
        n_a = len(re.findall(r"\\end\{quote\}\s*\\noindent\s*---", kq.group(1)))
        if n_q == 0 or n_q != n_a:
            probs.append(f"Key Quotations: {n_q} quotes but {n_a} Group A attribution lines")
    mj = re.search(r"\\section\{Memory Jogger\}(.*?)\\section", tex, re.S)
    if mj and len(mj.group(1).split()) > 110:
        probs.append("Memory Jogger longer than ~100 words")
    if rep["new_words"] > NEW_WORD_LIMIT:
        probs.append(f"{rep['new_words']} new words (limit {NEW_WORD_LIMIT})")
    if "Spring 2027" in tex or re.search(r"\bcasebook\b", tex, re.I):
        probs.append("contains 'Spring 2027' or 'casebook'")
    if re.search(r"\\(tfrac|dfrac|mathbb|operatorname)\b|\\text\{", tex):
        probs.append("amsmath-only macro")

    with tempfile.TemporaryDirectory() as d:
        for _ in (1, 2):
            c = run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", out_tex], cwd=d)
        log = open(os.path.join(d, stem + ".log"), errors="replace").read()
        if c.returncode:
            probs.append("pdflatex error: " + " | ".join(re.findall(r"^!.*", log, re.M)[:2]))
        warn = re.findall(r"LaTeX Warning: .*", log)
        if warn:
            probs.append("LaTeX warnings: " + "; ".join(warn[:2]))
        m = re.search(r"\((\d+)\s+pages?", log)
        info["pages"] = int(m.group(1)) if m else 0
    return {**info, "pass": not probs, "problems": probs}


if __name__ == "__main__":
    for s in sys.argv[1:]:
        print(json.dumps(check(os.path.basename(s).removesuffix(".tex").removesuffix(".py"))))
