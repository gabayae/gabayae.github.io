#!/usr/bin/env python3
r"""
One-off: append \og/\fg providecommands after the noindent block in
every master that has the marker but not yet the og/fg fallback.
"""
from __future__ import annotations
import pathlib
import re

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
MARKER = "% --- Pas d'indentation, espace inter-paragraphe (sweep global) ---"
OG_MARKER = "% --- French guillemets fallback (polyglossia french does not define them) ---"
OG_BLOCK = (
    f"{OG_MARKER}\n"
    r"\providecommand{\og}{\guillemotleft\,}"
    "\n"
    r"\providecommand{\fg}{\,\guillemotright}"
    "\n"
)

# Pattern to find the existing noindent block end (the parskip line).
PARSKIP_RE = re.compile(
    r"(\\setlength\{\\parskip\}\{0\.5\\baselineskip plus 0\.1\\baselineskip minus 0\.1\\baselineskip\}\n)"
)


def patch(text: str) -> tuple[str, bool]:
    if MARKER not in text:
        return text, False
    if OG_MARKER in text:
        return text, False
    new_text, n = PARSKIP_RE.subn(lambda m: m.group(1) + OG_BLOCK, text, count=1)
    return new_text, n > 0


def main() -> int:
    files = sorted(
        list((REPO_ROOT / "courses").glob("*/fr/cours.tex"))
        + list((REPO_ROOT / "courses").glob("*/en/notes.tex"))
    )
    patched = 0
    for path in files:
        text = path.read_text(encoding="utf-8")
        new_text, changed = patch(text)
        if changed:
            path.write_text(new_text, encoding="utf-8")
            print(f"  patched  {path.relative_to(REPO_ROOT)}")
            patched += 1
        else:
            print(f"  skip     {path.relative_to(REPO_ROOT)}")
    print(f"\nTotal patched: {patched}/{len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
