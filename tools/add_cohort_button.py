#!/usr/bin/env python3
"""Add a 'Cohort site / Site cohorte' button to the flip-card front face
of the 6 courses that have a cohort site. Adds matching CSS for the new
button style. Idempotent — running twice does not double-insert.

Run:
    python tools/add_cohort_button.py
"""
from __future__ import annotations
import pathlib
import re
import sys

SLUGS = [
    "tda",
    "apprentissage-geometrique",
    "apprentissage-renforcement",
    "mlops",
    "ia-generative",
    "apprentissage-automatique",
]

REPO = pathlib.Path(__file__).resolve().parents[1]

# The CSS rule to add for the new button style. Goes inside <style>...</style>.
CSS_MARKER = ".btn-cohort{"
CSS_RULE = (
    ".btn-cohort{background:var(--gold);color:#000;border:1px solid var(--gold);font-weight:600}"
    ".btn-cohort:hover{background:#f4d144;color:#000;transform:translateY(-1px)}"
)

# The HTML button to add. Goes inside <div class="downloads">...</div>, after
# the existing PDF buttons.
HTML_MARKER = 'class="btn btn-cohort"'
HTML_BUTTON = '<a href="cohort/" class="btn btn-cohort">Site cohorte &middot; Cohort</a>'


def patch_one(slug: str) -> str:
    path = REPO / "courses" / slug / "index.html"
    if not path.exists():
        return f"  MISSING {path.relative_to(REPO)}"
    text = path.read_text(encoding="utf-8")

    css_added = False
    html_added = False

    if CSS_MARKER not in text:
        # Insert CSS rule after the .btn-outline:hover line if it exists,
        # else after the first .btn definition.
        anchor = re.search(r"\.btn-outline:hover\{[^}]*\}", text)
        if anchor:
            insert_at = anchor.end()
            text = text[:insert_at] + "\n" + CSS_RULE + text[insert_at:]
            css_added = True

    if HTML_MARKER not in text:
        # Insert button into the .downloads div. Locate the closing </div>
        # of the .downloads block by finding the first occurrence of
        # 'class="downloads"' and then the matching </div>.
        m = re.search(r'(<div class="downloads">)([^<]*(?:<a[^>]*>[^<]*</a>[^<]*)+)(</div>)', text)
        if m:
            buttons = m.group(2).rstrip()
            new_block = m.group(1) + buttons + "\n    " + HTML_BUTTON + m.group(3)
            text = text[: m.start()] + new_block + text[m.end():]
            html_added = True

    if css_added or html_added:
        path.write_text(text, encoding="utf-8")
    flag = ("css" if css_added else "  ") + " " + ("html" if html_added else "    ")
    return f"  [{flag}] {path.relative_to(REPO)}"


def main() -> int:
    for slug in SLUGS:
        print(patch_one(slug))
    return 0


if __name__ == "__main__":
    sys.exit(main())
