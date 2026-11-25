#!/usr/bin/env python3
r"""Check every quotation in the briefs against the text of the case's own opinion.

For each brief, quotations are taken from (a) Key Quotations blocks, with their
attribution line, and (b) inline ``...'' quotations of at least MIN_WORDS words.
Each quotation is normalized (LaTeX removed, case and punctuation ignored, PDF
line-break hyphens rejoined), split at ellipses and bracketed alterations, and
every segment is searched for in the opinion text fetched by fetch_sources.py.

Results per quotation:
  status  EXACT   every segment found, in order
          CLOSE   best match >= 0.85 similarity (likely a small wording slip)
          NOTFOUND
  page    U.S. Reports page where the match starts/ends (official PDFs only)
  pin     for Key Quotations: the pin cite in the attribution and whether the
          matched page falls inside it (OK / OFF_BY_1 / WRONG / NONE)

usage: check_quotes.py SOURCES_DIR MANIFEST.json BRIEFS_DIR OUT.json
"""
import difflib, glob, json, os, re, sys, unicodedata

MIN_WORDS = 8


def latex_to_text(s):
    s = re.sub(r"\\href\{[^}]*\}\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\(?:textit|emph|textbf|textsc|underline|mbox|text)\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\(?:textit|emph|textbf)\{([^{}]*)\}", r"\1", s)
    s = s.replace("\\S", "§").replace("\\&", "&").replace("\\%", "%").replace("\\$", "$").replace("\\_", "_")
    s = re.sub(r"\\(?:dots|ldots)\b\s*", " … ", s)
    s = re.sub(r"\.\s?\.\s?\.(\s?\.)?", " … ", s)
    s = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", s)
    s = s.replace("~", " ").replace("\\,", "").replace("\\ ", " ").replace("{", "").replace("}", "")
    return s


def tokens(s):
    s = unicodedata.normalize("NFKC", s)               # ligatures: \ufb01 -> fi, etc.
    s = s.replace("\u00ad", "").replace("\u2010", "-").replace("\u2011", "-")
    s = s.lower().replace("’", "'").replace("‘", "'")
    s = re.sub(r"---|--|[—–]", " ", s)                 # dashes separate words
    s = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s)      # PDF line-break hyphenation
    s = s.replace("-", "")
    toks = re.findall(r"[a-z0-9§]+", s)
    return [t for t in toks if not (t.isdigit() and len(t) <= 3)]   # drop footnote markers / page numbers


def segments(quote):
    """Split at ellipses and [bracketed insertions]; keep segments of >= 4 tokens."""
    q = re.sub(r"\[([a-zA-Z])\]", r"\1", quote)            # [e]ven -> even
    parts = re.split(r"…|\[[^\]]{2,}\]", q)
    segs = [tokens(p) for p in parts]
    return [s for s in segs if len(s) >= 4]


HEADER = re.compile(r"(cite as|opinion of the court|october term|syllabus|dissenting|concurring|^\s*\d+\s*$|u\.\s?s\.)", re.I)


def source_tokens(src):
    """Token list for the whole opinion plus, for each token, the PDF page it came from."""
    toks, page_of = [], []
    for i, page in enumerate(src["pages"]):
        lines = page.split("\n")
        body = [l for k, l in enumerate(lines) if not (k < 4 and (len(l.strip()) < 50 or HEADER.search(l)) and len(l.strip()) < 90)]
        t = tokens("\n".join(body))
        toks += t; page_of += [i] * len(t)
    return toks, page_of


def find_seq(hay, idx, seg):
    """Exact positions of token list seg in hay, via a 3-gram index."""
    key = tuple(seg[:3])
    for p in idx.get(key, []):
        if hay[p:p + len(seg)] == seg:
            return p
    return None


def best_fuzzy(hay, idx, seg):
    best = (0.0, None)
    cands = set()
    for k in range(0, max(1, len(seg) - 2), max(1, len(seg) // 6)):
        for p in idx.get(tuple(seg[k:k + 3]), [])[:50]:
            cands.add(max(0, p - k))
    for p in cands:
        r = difflib.SequenceMatcher(None, seg, hay[p:p + len(seg) + 3], autojunk=False).ratio()
        if r > best[0]:
            best = (r, p)
    return best


def check_one(text, hay, idx, page_of):
    segs = segments(latex_to_text(text))
    if not segs:
        return None
    positions, worst, diffs = [], 1.0, []
    for s in segs:
        p = find_seq(hay, idx, s)
        if p is None:
            r, p = best_fuzzy(hay, idx, s)
            worst = min(worst, r)
            if p is None or r < 0.85:
                return {"status": "NOTFOUND", "similarity": round(r, 2)}
            diffs += char_diffs(s, hay[p:p + len(s) + 3])
        positions.append((p, p + len(s) - 1))
    start, end = positions[0][0], positions[-1][1]
    # OCR noise (split/joined words, a stray character) vs. real wording differences (words added/dropped/changed)
    real = [d for d in diffs if d[2] > 3]
    status = "EXACT" if not diffs else ("OCR_NOISE" if not real else "WORDING")
    out = {"status": status, "similarity": round(worst, 2),
           "pdf_pages": [page_of[start], page_of[min(end, len(page_of) - 1)]]}
    if real:
        out["differences"] = [f"{op}: brief '{a}' / opinion '{b}'" for op, a, n, b in real][:6]
    return out


def char_diffs(seg, window):
    """Character-level differences between a quote segment and the opinion, spaces ignored.
    Returns (op, quote_text, size, opinion_text); trailing extra opinion text is ignored."""
    a = "".join(seg)
    b_full = "".join(window)
    sm = difflib.SequenceMatcher(None, a, b_full, autojunk=False)
    ops = sm.get_opcodes()
    while ops and ops[-1][0] == "insert":      # opinion continues past the quote
        ops.pop()
    out = []
    for op, i1, i2, j1, j2 in ops:
        if op != "equal":
            out.append((op, a[i1:i2], max(i2 - i1, j2 - j1), b_full[j1:j2]))
    return out


PIN = re.compile(r"(?:U\.\s?S\.\s*,?\s*)?at\s+(\d+)(?:\s*(?:--|–|-)\s*(\d+))?")


def pin_status(attr, us_pages):
    m = PIN.search(latex_to_text(attr))
    if not m or not us_pages:
        return ("NONE" if not m else "UNCHECKED"), (m.group(0) if m else None)
    a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
    if b < a and len(m.group(2)) < len(m.group(1)):          # 512--13 style
        b = int(m.group(1)[: len(m.group(1)) - len(m.group(2))] + m.group(2))
    lo, hi = us_pages
    if a <= hi and b >= lo:
        return "OK", m.group(0)
    if a - 1 <= hi and b + 1 >= lo:
        return "OFF_BY_1", m.group(0)
    return "WRONG", m.group(0)


def main():
    src_dir, man_p, briefs_dir, out_p = sys.argv[1:5]
    by_num = {e["num"]: e for e in json.load(open(man_p))}
    results = []
    for path in sorted(glob.glob(os.path.join(briefs_dir, "*.tex")), key=lambda p: int(os.path.basename(p).split("_")[0])):
        stem = os.path.basename(path)[:-4]
        num = int(stem.split("_")[0])
        sp = os.path.join(src_dir, f"{num}.json")
        if not os.path.exists(sp):
            results.append({"brief": stem, "error": "no source text"}); continue
        src = json.load(open(sp))
        hay, page_of = source_tokens(src)
        idx = {}
        for i in range(len(hay) - 2):
            idx.setdefault((hay[i], hay[i + 1], hay[i + 2]), []).append(i)
        first = src.get("first_page")
        tex = open(path, encoding="utf-8").read()
        body, _, kq = tex.partition("\\section{Key Quotations}")
        items = []
        for q, a in re.findall(r"\\begin\{quote\}\s*(.*?)\s*\\end\{quote\}\s*\\noindent --- (.*?)\n", kq, re.S):
            items.append(("key", q, a))
        for q in re.findall(r"``(.+?)''", re.sub(r"\\begin\{quote\}.*?\\end\{quote\}", " ", body, flags=re.S), re.S):
            if len(latex_to_text(q).split()) >= MIN_WORDS:
                items.append(("inline", q, None))
        for kind, q, a in items:
            r = check_one(q, hay, idx, page_of)
            if r is None:
                continue
            rec = {"brief": stem, "kind": kind, "quote": latex_to_text(q).strip()[:400], **r, "source": src["kind"]}
            if r.get("pdf_pages") and first and src["kind"] in ("loc", "govinfo", "prelim_print"):
                rec["us_pages"] = [first + r["pdf_pages"][0], first + r["pdf_pages"][1]]
            if kind == "key":
                rec["attribution"] = latex_to_text(a).strip()[:200]
                rec["pin"], rec["pin_cited"] = pin_status(a, rec.get("us_pages"))
            results.append(rec)
    json.dump(results, open(out_p, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
