#!/usr/bin/env python3
"""Insert EN story-mode hooks. Same logic as insert_chapter_hooks.py but
walks the EN data file and EN paths.
"""
from __future__ import annotations
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
HOOK_MARKER = "% --- hook ---"

sys.path.insert(0, str(REPO_ROOT / "tools"))
from chapter_hooks_data_en import HOOKS  # type: ignore

SECTION_RE = re.compile(r"^\s*\\section\*?\{")
CHAPTER_RE = re.compile(r"\\chapter\*?\{")


def find_insertion_idx(lines: list[str]) -> int | None:
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
    return section_idx


def insert_hook(text: str, hook: str) -> tuple[str, bool]:
    if HOOK_MARKER in text[:4000]:
        return text, False
    lines = text.splitlines(keepends=True)
    idx = find_insertion_idx(lines)
    if idx is None:
        return text, False
    hook_text = hook.strip()
    block = f"{HOOK_MARKER}\n{hook_text}\n\n"
    lines.insert(idx, block)
    return "".join(lines), True


def main() -> int:
    dry = "--dry-run" in sys.argv
    inserted = 0
    skipped = 0
    missing = 0

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
    return 0


if __name__ == "__main__":
    sys.exit(main())
