"""Helpers for writing fills/src/<stem>.py, which emits fills/<stem>.json.

Each Group A section is a list of parts:
  N(text)                  new text (counted and reported for independent review)
  S(text)                  exact substring of the original brief (verified)
  SEC(section, frm=, to=, strip=, lc=)
                           verbatim slice of an original Group B section,
                           from anchor `frm` (inclusive) to before anchor `to`
  ITEMS(section, frm=, to=) like SEC, but "\\item \\textbf{Label:} body" lines
                           become "\\textbf{Label:} body" paragraphs
Any part takes glue=" " to continue the same paragraph (default: blank line)
or glue="\\n" for a plain line break.

At the end of the file call:  emit(__file__, {"sections": {...}, "dropped": [...], "notes": [...]})
"""
import json, os

def _g(d, glue):
    if glue is not None:
        d["glue"] = glue
    return d

def N(t, glue=None): return _g({"new": t}, glue)
def S(t, glue=None): return _g({"src": t}, glue)

def SEC(sec, frm=None, to=None, strip=None, glue=None, lc=False):
    d = {"sec": sec}
    if frm: d["from"] = frm
    if to: d["to"] = to
    if strip: d["strip"] = strip
    if lc: d["lcfirst"] = True
    return _g(d, glue)

def ITEMS(sec, frm=None, to=None, glue=None):
    return _g({"items": sec, "from": frm, "to": to}, glue)

def emit(src_file, fills):
    stem = os.path.splitext(os.path.basename(src_file))[0]
    root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(src_file))))
    out = os.path.join(root, "fills", stem + ".json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(fills, f, indent=1, ensure_ascii=False)
    print("wrote", out)
