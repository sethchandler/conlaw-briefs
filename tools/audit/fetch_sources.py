#!/usr/bin/env python3
"""Download the official text of every case in the manifest, page by page.

Sources, in order of preference:
  - Library of Congress U.S. Reports PDFs (tile.loc.gov), volumes 1-573
  - GovInfo U.S. Reports PDFs (govinfo.gov), volumes 570 and later
  - Supreme Court slip opinions (supremecourt.gov), located by docket number

Writes <cache>/<num>.json: {"num", "title", "citation", "source_url", "kind",
"first_page" (U.S. Reports page of PDF page 1, or null for slip opinions),
"pages": [text of each PDF page]}. Already-fetched cases are skipped.

usage: fetch_sources.py MANIFEST.json CACHE_DIR [--only NUM ...]
"""
import concurrent.futures as cf, json, os, re, subprocess, sys, tempfile, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (case-brief citation audit)"}
SLIP_TERMS = ["17", "18", "19", "20", "21", "22", "23", "24", "25"]


def get(url, timeout=90):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def pdf_pages(data):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "x.pdf")
        open(p, "wb").write(data)
        out = subprocess.run(["pdftotext", "-layout", p, "-"], capture_output=True, text=True, errors="replace").stdout
    return out.split("\f")[:-1] if out.endswith("\f") else out.split("\f")


_slip_index = None
ROW = re.compile(r"<td[^>]*>\s*([0-9]{2}[-Aa][0-9A-Za-z]+)\s*</td>\s*<td>\s*<a href=['\"](/opinions/(?:\d+pdf|preliminaryprint)/[^'\"]+\.pdf(?:#page=\d+)?)['\"][^>]*>([^<]+)</a>")


def norm(t):
    t = re.sub(r"[^a-z ]", " ", t.lower().replace("&", " and "))
    return " ".join(w for w in t.split() if w not in {"v", "inc", "et", "al", "the", "of", "co", "corp", "llc"})


def slip_index():
    """docket -> url and normalized case name -> url, from the Court's slip-opinion lists."""
    global _slip_index
    if _slip_index is None:
        _slip_index = {"docket": {}, "name": {}}
        for t in SLIP_TERMS:
            html = get(f"https://www.supremecourt.gov/opinions/slipopinion/{t}").decode("utf-8", "replace")
            for dk, path, name in ROW.findall(html):
                url = "https://www.supremecourt.gov" + path
                _slip_index["docket"].setdefault(dk.upper(), url)
                _slip_index["name"].setdefault(norm(name), url)
    return _slip_index


_prints = {}
def print_pages(url, title):
    base, start = url.split("#page=")
    if base not in _prints:
        _prints[base] = pdf_pages(get(base, timeout=300))
    allp, i = _prints[base], int(start) - 1
    key = re.sub(r"[^A-Z]", "", title.split(" v. ")[0].split(",")[0].upper())[:8]
    out, misses = [], 0
    while i < len(allp) and misses < 2:
        head = re.sub(r"[^A-Z]", "", "".join(allp[i].strip().split("\n")[:3]).upper())
        misses = 0 if (key and key in head) or not out else misses + 1
        out.append(allp[i]); i += 1
    return out[:-misses] if misses else out


def candidates(e):
    c = e["citation"]
    m = re.match(r"(\d+)\s+U\.\s?S\.\s+(?:\([^)]*\)\s+)?(\d+)", c)
    out = []
    if m:
        v, p = int(m.group(1)), int(m.group(2))
        if v <= 573:
            base = f"https://tile.loc.gov/storage-services/service/ll/usrep/usrep{v:03d}/usrep{v:03d}{p:03d}"
            out += [(f"{base}/usrep{v:03d}{p:03d}.pdf", "loc", p), (f"{base}a/usrep{v:03d}{p:03d}a.pdf", "loc", p)]
        if v >= 502:
            out.append((f"https://www.govinfo.gov/content/pkg/USREPORTS-{v}/pdf/USREPORTS-{v}-{p}.pdf", "govinfo", p))
    idx = slip_index()
    for dk in re.findall(r"\b(\d{2}-\d+|\d{2}A\d+)\b", c + " " + e.get("docket", "")):
        if dk.upper() in idx["docket"]:
            out.append((idx["docket"][dk.upper()], "slip", None))
    if not m or int(m.group(1)) >= 584:   # name lookup for recent cases without a docket in the manifest
        key = norm(e["title"].split("/")[0])
        hits = [u for n, u in idx["name"].items() if n == key or (len(key) > 8 and (n.startswith(key) or key.startswith(n)))]
        out += [(u, "slip", None) for u in hits[:1]]
    return out


def fetch(e, cache):
    path = os.path.join(cache, f"{e['num']}.json")
    if os.path.exists(path):
        return e["num"], "cached"
    tried = []
    cm = re.match(r"(\d+)\s+U\.\s?S\.\s+(?:\([^)]*\)\s+)?(\d+)", e["citation"])
    for url, kind, first in candidates(e):
        if "#page=" in url and cm:      # preliminary prints carry official U.S. Reports pages
            first = int(cm.group(2))
        try:
            if "#page=" in url:   # a preliminary print (whole volume part): keep this case's pages only
                pages = print_pages(url, e["title"])
                json.dump({"num": e["num"], "title": e["title"], "citation": e["citation"], "source_url": url,
                           "kind": "prelim_print", "first_page": first, "pages": pages}, open(path, "w"))
                return e["num"], f"prelim_print {len(pages)}pp"
            data = get(url)
            if not data.startswith(b"%PDF"):
                tried.append(f"{url} (not a PDF)"); continue
            pages = pdf_pages(data)
            json.dump({"num": e["num"], "title": e["title"], "citation": e["citation"], "source_url": url,
                       "kind": kind, "first_page": first, "pages": pages}, open(path, "w"))
            return e["num"], f"{kind} {len(pages)}pp"
        except Exception as ex:
            tried.append(f"{url} ({getattr(ex, 'code', ex)})")
    return e["num"], "FAILED: " + "; ".join(tried) if tried else "FAILED: no source for " + e["citation"]


def main():
    man, cache = sys.argv[1], sys.argv[2]
    only = set(int(x) for x in sys.argv[sys.argv.index("--only") + 1:]) if "--only" in sys.argv else None
    os.makedirs(cache, exist_ok=True)
    entries = [e for e in json.load(open(man)) if not only or e["num"] in only]
    slip_index()   # build once before threads start (avoids a race on the shared index)
    with cf.ThreadPoolExecutor(3) as ex:
        for num, status in ex.map(lambda e: fetch(e, cache), entries):
            if status != "cached":
                print(num, status, flush=True)


if __name__ == "__main__":
    main()
