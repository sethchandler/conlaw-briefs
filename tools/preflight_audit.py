#!/usr/bin/env python3
r"""Pre-flight deterministic audit for standalone LaTeX case briefs in a master .zip.

Checks every .tex brief for:
  1. Disallowed BasicTeX/amsmath-only macros (\tfrac, \dfrac, \mathbb, \operatorname, \text{})
  2. Unwanted 'Spring 2027' strings
  3. Section structure count
  4. Deduplicated list of cited 2024-2026 decisions (for fast cross-model fact-checking)
  5. Optional concurrent HTTP status checks on all \href / \url links (--check-urls)

Usage:
    python3 preflight_audit.py --zip conlaw_briefs_1_247_tex_master.zip
    python3 preflight_audit.py --zip conlaw_briefs_1_247_tex_master.zip --check-urls --out preflight_report.json
"""

import argparse
import concurrent.futures
import json
import re
import urllib.error
import urllib.request
import zipfile
from collections import defaultdict

BAD_MACROS = [r"\\tfrac\b", r"\\dfrac\b", r"\\mathbb\b", r"\\operatorname\b", r"\\text\{"]


def check_url(url: str, timeout: int = 10) -> tuple:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"},
        method="HEAD",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return url, resp.status, ""
    except urllib.error.HTTPError as e:
        if e.code in (403, 405):
            # Retry with GET for sites blocking HEAD
            try:
                req_get = urllib.request.Request(
                    url,
                    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"},
                )
                with urllib.request.urlopen(req_get, timeout=timeout) as resp:
                    return url, resp.status, ""
            except Exception as e2:
                return url, getattr(e2, "code", 0), str(e2)
        return url, e.code, str(e)
    except Exception as e:
        return url, 0, str(e)


def main():
    p = argparse.ArgumentParser(description="Pre-flight LaTeX & URL audit for ConLaw briefs")
    p.add_argument("--zip", required=True, help="Master .zip of standalone .tex briefs")
    p.add_argument("--check-urls", action="store_true", help="Run live HTTP checks on all URLs")
    p.add_argument("--workers", type=int, default=16, help="Concurrent HTTP workers")
    p.add_argument("--out", default="preflight_report.json", help="Output JSON report path")
    args = p.parse_args()

    issues = []
    all_urls = defaultdict(list)
    recent_citations = defaultdict(set)

    with zipfile.ZipFile(args.zip, "r") as zf:
        tex_names = sorted(n for n in zf.namelist() if n.endswith(".tex"))
        print(f"Scanning {len(tex_names)} standalone .tex files in {args.zip}...")
        for name in tex_names:
            text = zf.read(name).decode("utf-8", errors="replace")
            file_issues = []
            if "Spring 2027" in text:
                file_issues.append("Contains disallowed 'Spring 2027'")
            for pat in BAD_MACROS:
                if re.search(pat, text):
                    file_issues.append(f"Unsupported BasicTeX macro matching {pat}")
            sec_count = len(re.findall(r"\\section\*?\{", text))
            if sec_count < 6:
                file_issues.append(f"Low section count ({sec_count})")
            if file_issues:
                issues.append({"file": name, "problems": file_issues})

            for u in set(re.findall(r"\\(?:href|url)\{([^}]+)\}", text)):
                if u.startswith("http"):
                    all_urls[u].append(name)

            # Extract italic case names followed by (2024|2025|2026)
            for m in re.finditer(
                r"\\(?:textit|emph)\{([^{}]{4,80}?\bv\.\s+[^{}]{2,80}?)\}[^(\n]{0,40}\((202[456])\)",
                text,
            ):
                recent_citations[f"{m.group(1)} ({m.group(2)})"].add(name)

    broken_urls = []
    if args.check_urls:
        unique_urls = sorted(all_urls.keys())
        print(f"Checking {len(unique_urls)} unique URLs with {args.workers} workers...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
            for url, status, err in ex.map(check_url, unique_urls):
                if status == 0 or status >= 400:
                    broken_urls.append({
                        "url": url,
                        "status": status,
                        "error": err,
                        "files": all_urls[url],
                    })

    report = {
        "zip": args.zip,
        "total_briefs": len(tex_names),
        "latex_issues_count": len(issues),
        "latex_issues": issues,
        "unique_urls_count": len(all_urls),
        "broken_urls_count": len(broken_urls),
        "broken_urls": broken_urls,
        "recent_2024_2026_cases": {
            k: sorted(v) for k, v in sorted(recent_citations.items())
        },
    }
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"Done! Report written to {args.out}")
    print(f"  LaTeX/hygiene issues: {len(issues)}")
    print(f"  Unique URLs found:    {len(all_urls)}")
    if args.check_urls:
        print(f"  Broken/flagged URLs:  {len(broken_urls)}")
    print(f"  Unique 2024-2026 cases cited: {len(recent_citations)}")


if __name__ == "__main__":
    main()
