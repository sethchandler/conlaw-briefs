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
LINE_DASH_RE = re.compile(r"^(?P<q>.*?)\s*(?:\\\\)?\s*\n\s*---\s*(?P<a>[^\n]+?)\s*$", re.S)   # attribution on its own last line
PAREN_RE = re.compile(r"^(?P<q>.*'')\s*\((?P<a>[^()]*(?:\([^()]*\)[^()]*)*)\)\s*\.?\s*$", re.S)
ATTR_AFTER = re.compile(r"\s*\\noindent --- ")
# A Group A attribution line: "\noindent --- ..." running to the next blank line
ATTR_LINE = re.compile(r"\\noindent --- .*?(?=\n\s*\n|\n\\begin|\Z)", re.S)


def _unwrap(s):
    """Turn in-quote attribution wrappers into a final '--- attribution' line."""
    s = re.sub(r"\\begin\{flushright\}\s*(?:---\s*)?(.*?)\s*\\end\{flushright\}", r"\n--- \1", s, flags=re.S)
    s = re.sub(r"(?:\\par\s*)?\\noindent\s*---\s*", "\n--- ", s)
    s = re.sub(r"\s*\\hfill\s*", " ", s)
    return s.strip()


def convert_block(inner):
    s = _unwrap(inner)
    m = DASH_RE.match(s) or LINE_DASH_RE.match(s) or PAREN_RE.match(s)
    if not m:
        return None
    q, a = m.group("q").strip(), m.group("a").strip()
    if not q or not a or "``" in a or q.endswith("\\\\") and not q[:-2].strip():
        return None
    q = re.sub(r"\s*\\\\$", "", q)
    a = a if a.endswith(".") else a + "."
    return f"\\begin{{quote}}\n{q}\n\\end{{quote}}\n\\noindent --- {a}\n"


def convert_section(body):
    """Return (new_body, None) or (None, reason)."""
    orig = body
    # Attribution already after the quote but without \noindent (or without a space): standardize it.
    body = re.sub(r"\\end\{quote\}\s*\n\s*---\s*", "\\\\end{quote}\n\\\\noindent --- ", body)
    body = re.sub(r"\\end\{quote\}\s*\\noindent\s*---\s*", "\\\\end{quote}\n\\\\noindent --- ", body)
    blocks = list(QUOTE_RE.finditer(body))
    if not blocks:
        return None, "no quote environments"
    intro = body[:blocks[0].start()].strip()          # a lead-in sentence is kept as is
    rest = body[blocks[0].start():]
    leftover = ATTR_LINE.sub("", QUOTE_RE.sub("", rest)).strip()
    if leftover:
        return None, f"text outside quote blocks: {leftover[:70]!r}"
    out = [intro + "\n"] if intro else []
    for m in blocks:
        if ATTR_AFTER.match(body, m.end()):
            tail = ATTR_LINE.match(body, body.index("\\noindent", m.end()))
            out.append(m.group(0) + "\n" + tail.group(0).strip() + "\n")
            continue
        c = convert_block(m.group(1))
        if c is None:
            return None, f"unrecognized attribution: {m.group(1).strip()[-80:]!r}"
        out.append(c)
    new = "\n".join(out) + "\n"
    if re.sub(r"\s+", "", new) == re.sub(r"\s+", "", orig):
        return None, "already Group A style"
    return new, None


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
