#!/usr/bin/env python3
r"""
Insert global no-indent settings into every course master TeX file
(both FR cours.tex and EN notes.tex), placed immediately before
\begin{document} so nothing in the preamble can override it (polyglossia
french sets \parindent in the preamble; our setting must come last).

The block inserted:

    % --- Pas d'indentation, espace inter-paragraphe (sweep global) ---
    \setlength{\parindent}{0pt}
    \setlength{\parskip}{0.5\baselineskip plus 0.1\baselineskip minus 0.1\baselineskip}

Idempotent: if the file already contains the marker comment, it is
skipped.

Run:
    python tools/noindent_global.py [--dry-run]
"""
from __future__ import annotations
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
MARKER = "% --- Pas d'indentation, espace inter-paragraphe (sweep global) ---"

BLOCK = (
    f"{MARKER}\n"
    r"\setlength{\parindent}{0pt}"
    "\n"
    r"\setlength{\parskip}{0.5\baselineskip plus 0.1\baselineskip minus 0.1\baselineskip}"
    "\n"
    r"% --- French guillemets fallback (polyglossia french does not define them) ---"
    "\n"
    r"\providecommand{\og}{\guillemotleft\,}"
    "\n"
    r"\providecommand{\fg}{\,\guillemotright}"
    "\n\n"
)

BEGIN_DOC_RE = re.compile(r"^\\begin\{document\}", re.MULTILINE)


def patch(text: str) -> tuple[str, bool]:
    if MARKER in text:
        return text, False
    m = BEGIN_DOC_RE.search(text)
    if m is None:
        return text, False
    pos = m.start()
    new_text = text[:pos] + BLOCK + text[pos:]
    return new_text, True


def main() -> int:
    dry = "--dry-run" in sys.argv
    files = sorted(
        list((REPO_ROOT / "courses").glob("*/fr/cours.tex"))
        + list((REPO_ROOT / "courses").glob("*/en/notes.tex"))
    )
    patched = 0
    skipped = 0
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"  SKIP (encoding) {path.relative_to(REPO_ROOT)}")
            skipped += 1
            continue
        new_text, changed = patch(text)
        rel = path.relative_to(REPO_ROOT)
        if not changed:
            print(f"  ALREADY-SET  {rel}")
            skipped += 1
            continue
        tag = "WOULD WRITE" if dry else "wrote      "
        print(f"  {tag} {rel}")
        if not dry:
            path.write_text(new_text, encoding="utf-8")
        patched += 1

    print(f"\nTotal:")
    print(f"  patched: {patched}")
    print(f"  skipped: {skipped}")
    print(f"  total:   {len(files)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
