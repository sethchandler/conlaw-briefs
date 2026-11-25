#!/usr/bin/env python3
"""Apply audit corrections marked "stage": "post" in fills/corrections/<stem>.json
to a converted brief, after quotation normalization and speaker names.
Each find must occur exactly once. usage: apply_post_corrections.py BRIEF.tex"""
import json, os, sys

path = sys.argv[1]
stem = os.path.basename(path)[:-4]
root = os.path.dirname(os.path.dirname(os.path.abspath(path)))
cp = os.path.join(root, "fills", "corrections", stem + ".json")
if not os.path.exists(cp):
    sys.exit(0)
tex = open(path, encoding="utf-8").read()
n = 0
for c in json.load(open(cp, encoding="utf-8")):
    if c.get("stage") != "post" or not c.get("decision", "").startswith("APPLIED"):
        continue
    k = tex.count(c["find"])
    if k != 1:
        sys.exit(f"correction {c.get('id')}: find occurs {k} times: {c['find'][:70]!r}")
    tex = tex.replace(c["find"], c["replace"]); n += 1
open(path, "w", encoding="utf-8").write(tex)
print("post corrections applied:", n)
