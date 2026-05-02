#!/usr/bin/env python3
"""README Link Checker (stdlib-only)

Checks the online status of links in a README.md (or any Markdown file).

Usage:
  python3 check_readme_links.py README.md
  python3 check_readme_links.py path/to/file.md --timeout 20

Notes:
- Uses HEAD first, then falls back to GET for servers that block HEAD.
- Prints a simple report and exits non-zero if any links appear broken.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path

URL_RE = re.compile(r"\[[^\]]*\]\((https?://[^\s\)]+)\)")

def http_check(url: str, timeout: int) -> int:
    headers = {
        "User-Agent": "awesome-list-link-checker/1.0 (+https://github.com)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    def request(method: str) -> int:
        req = urllib.request.Request(url, headers=headers, method=method)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return getattr(resp, "status", 200)

    # HEAD first
    try:
        return request("HEAD")
    except urllib.error.HTTPError as e:
        # Some sites reject HEAD; fall back to GET on common cases
        if e.code in (403, 405):
            try:
                return request("GET")
            except urllib.error.HTTPError as e2:
                return e2.code
        return e.code
    except Exception:
        # fallback GET
        try:
            return request("GET")
        except urllib.error.HTTPError as e:
            return e.code
        except Exception:
            return 0

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Path to README.md (or any .md file)")
    ap.add_argument("--timeout", type=int, default=20, help="Request timeout in seconds")
    args = ap.parse_args()

    md = Path(args.path)
    if not md.exists():
        print(f"File not found: {md}", file=sys.stderr)
        return 2

    text = md.read_text(encoding="utf-8", errors="ignore")
    urls = [u.rstrip(".,;:!?)\"'") for u in URL_RE.findall(text)]

    if not urls:
        print("No links found.")
        return 0

    bad = 0
    for url in urls:
        code = http_check(url, timeout=args.timeout)
        if 200 <= code < 400 or code == 429:
            print(f"OK   [{code}] {url}")
        else:
            bad += 1
            print(f"BAD  [{code}] {url}")

    print(f"\nChecked {len(urls)} links. Bad: {bad}")
    return 1 if bad else 0

if __name__ == "__main__":
    raise SystemExit(main())
