#!/usr/bin/env python3
"""
Awesome List lint (strict on resources, permissive on TOC)

Errors:
- README.md missing
- Missing "Contribute"/"Contributing" heading (accepts contribut* variants)
- Missing "License" heading
- TAB characters in README.md
- Trailing whitespace on list lines that start with "- [" or "* ["
- External resource entries must be in the format:
    - [Name](https://example.com) — Short, neutral description.
  (also allows '-' instead of '—')

Allows:
- TOC / internal anchor bullets:
    - [Section](#section)
  (no description required)

Notes:
- Ignores code blocks.
- Duplicate headings are warnings, not failures.
"""
from __future__ import annotations

import re
from pathlib import Path
from collections import Counter

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
CODE_FENCE_RE = re.compile(r"^\s*```")

# Basic markdown bullet + link capture
BULLET_LINK_RE = re.compile(r"^[-*]\s+\[[^\]]+\]\(([^)]+)\)\s*$")

# External resource entry with description
RESOURCE_WITH_DESC_RE = re.compile(
    r"^[-*]\s+\[[^\]]+\]\((https?://[^\s)]+)\)\s*(—|-)\s+.+"
)

def strip_code_blocks(lines: list[str]) -> list[tuple[int, str]]:
    in_code = False
    out: list[tuple[int, str]] = []
    for i, line in enumerate(lines, start=1):
        if CODE_FENCE_RE.match(line):
            in_code = not in_code
            continue
        if not in_code:
            out.append((i, line))
    return out

def main() -> int:
    readme = Path("README.md")
    if not readme.exists():
        print("ERROR: README.md not found.")
        return 1

    text = readme.read_text(encoding="utf-8", errors="ignore")
    if "\t" in text:
        print("ERROR: README.md contains TAB characters. Replace tabs with spaces.")
        return 1

    lines = text.splitlines()
    noncode = strip_code_blocks(lines)

    # headings
    headings: list[str] = []
    for _ln, line in noncode:
        m = HEADING_RE.match(line)
        if m:
            headings.append(m.group(2).strip())

    lower = [h.lower().strip() for h in headings]

    if not any(h in ("contribute", "contributing") or "contribut" in h for h in lower):
        print("ERROR: Missing a 'Contribute'/'Contributing' section heading in README.md.")
        return 1

    if not any("license" in h for h in lower):
        print("ERROR: Missing a 'License' section heading in README.md.")
        return 1

    # Duplicate heading warning (non-fatal)
    c = Counter(lower)
    dups = [h for h, n in c.items() if n > 1]
    if dups:
        print("WARNING: Duplicate section headings detected:")
        for h in sorted(dups):
            print(f"  - {h}")
        print()

    errors = 0

    for ln, line in noncode:
        s = line.rstrip("\n")

        # Only lint bullets that look like markdown-link bullets
        if not (s.startswith("- [") or s.startswith("* [")):
            continue

        # Trailing whitespace (fail)
        if s != s.rstrip():
            print(f"ERROR: Trailing whitespace on list line {ln}.")
            errors += 1

        # If it's exactly a TOC-style bullet like "- [Section](#section)", allow it.
        m = BULLET_LINK_RE.match(s.strip())
        if m:
            url = m.group(1).strip()
            if url.startswith("#"):
                continue  # TOC anchor bullet is valid

        # For external resources, require description format
        if s.find("(http://") != -1 or s.find("(https://") != -1:
            if RESOURCE_WITH_DESC_RE.match(s):
                continue

            print(f"ERROR: Resource entry bullet malformed on line {ln}. Expected:")
            print("  - [Name](https://example.com) — Short, neutral description.")
            print("or")
            print("  - [Name](https://example.com) - Short, neutral description.")
            print(f"  {s}")
            errors += 1

    if errors:
        print(f"Found {errors} lint error(s).")
        return 1

    print("Awesome list lint: OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
