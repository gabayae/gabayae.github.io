#!/usr/bin/env python3
r"""
Insert a story-mode hook paragraph into each cold chapter, between the
chapter banner (and any leading environment like an epigraph or intuition
box) and the first \section command.

The hook payloads live in tools/chapter_hooks_data.py as a dict mapping
the chapter file path (relative to repo root, POSIX-style) to the hook
prose. The hook is wrapped with the marker:

    % --- hook ---
    <hook prose>

    \section{...} <-- left untouched

Insertion rule per pattern (auto-detected):

    A) \section directly after the chapter banner --> insert just before
       the \section.

    B) \begin{quote}...\end{quote} epigraph then \section --> insert
       after \end{quote}, before \section.

    C) \begin{intuition}...\end{intuition} then \section --> insert
       after \end{intuition}, before \section.

    D) \begin{center}...\end{center} epigraph then \section --> insert
       after \end{center} (and an optional \bigskip/\medskip), before
       \section.

Idempotent: skips files that already contain '% --- hook ---' near the
top.

Run:
    python tools/insert_chapter_hooks.py [--dry-run]
"""
from __future__ import annotations
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
HOOK_MARKER = "% --- hook ---"

# Import the data file
sys.path.insert(0, str(REPO_ROOT / "tools"))
from chapter_hooks_data import HOOKS  # type: ignore

SECTION_RE = re.compile(r"^\s*\\section\*?\{")
CHAPTER_RE = re.compile(r"\\chapter\*?\{")
END_QUOTE_RE = re.compile(r"\\end\{quote\}")
END_INTUITION_RE = re.compile(r"\\end\{intuition\}")
END_CENTER_RE = re.compile(r"\\end\{center\}")
SKIP_AFTER_END_RE = re.compile(r"^\s*(\\bigskip|\\medskip|\\smallskip|\\vspace\{|%|$)")


def find_first_section_idx(lines: list[str], start_idx: int) -> int | None:
    for i in range(start_idx, len(lines)):
        if SECTION_RE.match(lines[i]):
            return i
    return None


def find_insertion_idx(lines: list[str]) -> int | None:
    """Return the line index *before* which the hook block should be inserted."""
    section_idx = None
    chapter_idx = None
    for i, line in enumerate(lines):
        if CHAPTER_RE.search(line) and chapter_idx is None:
            chapter_idx = i
        if SECTION_RE.match(line):
            section_idx = i
            break
    if section_idx is None or chapter_idx is None:
        return None

    # Walk backwards from section_idx and find the latest \end{quote},
    # \end{intuition}, or \end{center} that sits *after* the chapter banner.
    last_end = chapter_idx
    for i in range(chapter_idx + 1, section_idx):
        if END_QUOTE_RE.search(lines[i]) or END_INTUITION_RE.search(lines[i]) or END_CENTER_RE.search(lines[i]):
            last_end = i

    # Insert *just before* the \section, but the hook prose should be
    # immediately after the epigraph/intuition block (with one blank line
    # separating). We return section_idx as the line *before* which we
    # insert. The blank line bookkeeping happens in the caller.
    return section_idx


def insert_hook(text: str, hook: str) -> tuple[str, bool]:
    if HOOK_MARKER in text[:4000]:
        return text, False
    lines = text.splitlines(keepends=True)
    idx = find_insertion_idx(lines)
    if idx is None:
        return text, False
    # Build hook block. Ensure exactly one blank line before \section.
    # Strip trailing whitespace from hook prose, then wrap.
    hook_text = hook.strip()
    block = f"{HOOK_MARKER}\n{hook_text}\n\n"
    # If the line immediately preceding the section is non-blank, we want
    # a blank line between the hook block end and the section anchor — the
    # trailing \n\n in block handles that. If it is blank, we still get
    # correct spacing.
    lines.insert(idx, block)
    return "".join(lines), True


def main() -> int:
    dry = "--dry-run" in sys.argv
    inserted = 0
    skipped = 0
    missing = 0
    failed = 0

    for rel_path, hook in sorted(HOOKS.items()):
        path = REPO_ROOT / rel_path
        if not path.exists():
            print(f"  MISSING {rel_path}")
            missing += 1
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"  SKIP (encoding) {rel_path}")
            skipped += 1
            continue
        new_text, changed = insert_hook(text, hook)
        if not changed:
            print(f"  ALREADY-HOOKED  {rel_path}")
            skipped += 1
            continue
        tag = "WOULD WRITE" if dry else "wrote      "
        print(f"  {tag} {rel_path}")
        if not dry:
            path.write_text(new_text, encoding="utf-8")
        inserted += 1

    print(f"\nTotal:")
    print(f"  inserted: {inserted}")
    print(f"  skipped:  {skipped}")
    print(f"  missing:  {missing}")
    print(f"  failed:   {failed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
