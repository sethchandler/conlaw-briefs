#!/usr/bin/env python3
r"""Convert Key Quotations attributions to the Group A style.

Group A style:
    \begin{quote}
    ``Quoted text.''
    \end{quote}
    \noindent --- Justice X, Opinion of the Court, 549 U.S.\ at 520 (links).

Handles quote blocks whose attribution sits INSIDE the quote environment, after
the closing '' as either  ``...'' --- Attribution  /  ``...''\\ --- Attribution
or a trailing parenthetical  ``...'' (74 U.S. at 514).  Only whitespace and the
"--- " / parentheses are changed; the quote and attribution text are untouched.

A brief is converted only if EVERY quote block in its Key Quotations section
matches and the section holds nothing but quote blocks; otherwise it is left
alone and reported, so nothing is half-converted.

usage: normalize_quotes.py [--check] FILE.tex ...
  --check   report only, change nothing
"""
import re, sys

SEC_RE = re.compile(r"(\\section\{Key Quotations\}\s*\n)(.*?)(?=\\section\{|\\end\{document\})", re.S)
QUOTE_RE = re.compile(r"\\begin\{quote\}(.*?)\\end\{quote\}", re.S)
DASH_RE = re.compile(r"^(?P<q>.*'')\s*(?:\\\\\s*)?---\s*(?P<a>\S.*?)\s*$", re.S)
PAREN_RE = re.compile(r"^(?P<q>.*'')\s*\((?P<a>[^()]*(?:\([^()]*\)[^()]*)*)\)\s*\.?\s*$", re.S)
ALREADY_A = re.compile(r"\\end\{quote\}\s*\\noindent\s*---")


def convert_block(inner):
    s = inner.strip()
    m = DASH_RE.match(s) or PAREN_RE.match(s)
    if not m:
        return None
    q, a = m.group("q").strip(), m.group("a").strip()
    if not q.startswith("``") or not a or "``" in a:
        return None
    a = a if a.endswith(".") else a + "."
    return f"\\begin{{quote}}\n{q}\n\\end{{quote}}\n\\noindent --- {a}\n"


def convert_section(body):
    """Return (new_body, None) or (None, reason)."""
    if ALREADY_A.search(body):
        return None, "already Group A style"
    blocks = list(QUOTE_RE.finditer(body))
    if not blocks:
        return None, "no quote environments"
    intro = body[:blocks[0].start()].strip()          # a lead-in sentence is kept as is
    leftover = QUOTE_RE.sub("", body[blocks[0].start():]).strip()
    if leftover:
        return None, f"text outside quote blocks: {leftover[:70]!r}"
    out = [intro + "\n"] if intro else []
    for m in blocks:
        c = convert_block(m.group(1))
        if c is None:
            return None, f"unrecognized attribution: {m.group(1).strip()[-80:]!r}"
        out.append(c)
    return "\n".join(out) + "\n", None


def main():
    args = sys.argv[1:]
    check = "--check" in args
    files = [a for a in args if a != "--check"]
    ok = skipped = 0
    for f in files:
        t = open(f, encoding="utf-8").read()
        m = SEC_RE.search(t)
        if not m:
            print(f"SKIP {f}: no Key Quotations section"); skipped += 1; continue
        new, why = convert_section(m.group(2))
        if new is None:
            print(f"SKIP {f}: {why}"); skipped += 1; continue
        ok += 1
        if not check:
            open(f, "w", encoding="utf-8").write(t[:m.start(2)] + new + "\n" + t[m.end(2):])
    print(f"{'would convert' if check else 'converted'}: {ok}   skipped: {skipped}")


if __name__ == "__main__":
    main()
