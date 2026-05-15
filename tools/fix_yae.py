#!/usr/bin/env python3
r"""
Sweep all .tex files under courses/ and replace LaTeX accent forms of
"Ya\'e Ulrich Gaba" (which sometimes mis-render as 'Yaë' under
polyglossia french + fontspec) with the literal UTF-8 form "Yaé Ulrich Gaba".

Patterns covered (each can appear with or without surrounding braces):
    Ya\'e            -> Yaé
    Ya\'{e}          -> Yaé
    {Ya\'e}          -> {Yaé}        (braces preserved)
    Ya{\'e}          -> Yaé

Run from repo root:
    python tools/fix_yae.py [--dry-run]
"""
from __future__ import annotations
import re
import sys
import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
COURSES = REPO_ROOT / "courses"

# Match Ya\'e (with optional {} around the e) and Ya{\'e}.
# Capture the trailing context so we keep things like "Ulrich Gaba" untouched.
PAT_BARE = re.compile(r"Ya\\'\{?e\}?")        # Ya\'e or Ya\'{e}
PAT_NEST = re.compile(r"Ya\{\\'e\}")           # Ya{\'e}


def fix(text: str) -> tuple[str, int]:
    n = 0
    def repl(m):
        nonlocal n
        n += 1
        return "Yaé"
    text = PAT_BARE.sub(repl, text)
    text = PAT_NEST.sub(repl, text)
    return text, n


def main() -> int:
    dry = "--dry-run" in sys.argv
    total = 0
    file_count = 0
    for path in sorted(COURSES.rglob("*.tex")):
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"  SKIP (encoding) {path}", file=sys.stderr)
            continue
        new, n = fix(original)
        if n > 0:
            file_count += 1
            total += n
            tag = "WOULD WRITE" if dry else "wrote     "
            print(f"  {tag} {path.relative_to(REPO_ROOT)}  ({n} replacement{'s' if n != 1 else ''})")
            if not dry:
                path.write_text(new, encoding="utf-8")
    print(f"\nTotal: {total} replacements across {file_count} files{' (dry run)' if dry else ''}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
