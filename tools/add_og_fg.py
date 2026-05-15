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


def find_all_masters() -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for tex in REPO_ROOT.rglob("*.tex"):
        rel_parts = tex.relative_to(REPO_ROOT).parts
        if rel_parts and rel_parts[0] in {"_site", "node_modules", ".git"}:
            continue
        try:
            head = tex.read_text(encoding="utf-8")[:50000]
        except UnicodeDecodeError:
            continue
        if r"\begin{document}" in head:
            files.append(tex)
    return sorted(files)


def main() -> int:
    files = find_all_masters()
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
