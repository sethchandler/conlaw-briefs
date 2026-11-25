#!/usr/bin/env python3
"""Search a case's official opinion text (fetched by fetch_sources.py) for a phrase.

Matching ignores case, punctuation, line breaks, and PDF hyphenation, like
check_quotes.py. Prints each hit with its U.S. Reports page (official PDFs) or
PDF page (slip opinions) and the surrounding text as printed.

usage: grep_source.py SOURCES_DIR CASE_NUM "phrase to find" [--context 400]
       grep_source.py SOURCES_DIR CASE_NUM --page N      (print one U.S./PDF page)
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_quotes as cq


def main():
    src_dir, num = sys.argv[1], sys.argv[2]
    src = json.load(open(os.path.join(src_dir, f"{num}.json")))
    first = src.get("first_page") if src["kind"] != "slip" else None
    label = (lambda i: f"{first + i} U.S. page") if first else (lambda i: f"PDF page {i + 1}")
    print(f"# {src['title']} | {src['citation']} | {src['kind']} | {src['source_url']}")
    if sys.argv[3] == "--page":
        n = int(sys.argv[4]); i = n - first if first else n - 1
        print(f"## {label(i)}\n{src['pages'][i]}"); return
    ctx = int(sys.argv[sys.argv.index("--context") + 1]) if "--context" in sys.argv else 400
    want = cq.tokens(sys.argv[3])
    hay, page_of = cq.source_tokens(src)
    hits = [p for p in range(len(hay) - len(want) + 1) if hay[p:p + len(want)] == want]
    if not hits:
        r, p = cq.best_fuzzy(hay, {tuple(hay[i:i+3]): [i] for i in range(len(hay) - 2)} if False else _idx(hay), want)
        print(f"no exact hit; best fuzzy similarity {r:.2f}" + (f" at {label(page_of[p])}:" if p is not None else ""))
        if p is not None:
            print(" ".join(hay[max(0, p - 30):p + len(want) + 30]))
        return
    for p in hits[:10]:
        print(f"## hit at {label(page_of[p])}")
        print(" ".join(hay[max(0, p - ctx // 8):p + len(want) + ctx // 8]))


def _idx(hay):
    idx = {}
    for i in range(len(hay) - 2):
        idx.setdefault((hay[i], hay[i + 1], hay[i + 2]), []).append(i)
    return idx


if __name__ == "__main__":
    main()
