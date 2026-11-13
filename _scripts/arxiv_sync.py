"""Sync arXiv author feed into _bibliography/papers.bib.

Fetches https://arxiv.org/a/<author>.atom, finds entries whose eprint ID is not
already in papers.bib, and appends them inside the ARXIV SYNC block (creating
that block if absent). Entries are marked bibtex_show=true (visible on the site)
without a selected flag, so the author keeps full control over curation.

Usage:
    python _scripts/arxiv_sync.py                 # live update
    python _scripts/arxiv_sync.py --dry-run       # print what would change
    python _scripts/arxiv_sync.py --author-id X   # override author id

stdlib only — no pip install needed on CI.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
import unicodedata
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

ATOM_NS = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"

SYNC_MARKER_PREFIX = "% ---- ARXIV SYNC "
SYNC_MARKER_SUFFIX = " (preprints from arxiv.org/a/{author_id}.html not already listed above) ----"

# Minimal LaTeX escape table for diacritics seen in this bib so entries keep
# the same visual style as the hand-authored ones (e.g. Ya{\'e}).
ACCENT_MAP = {
    "á": r"{\'a}", "à": r"{\`a}", "â": r"{\^a}", "ä": r'{\"a}', "ã": r"{\~a}", "å": r"{\aa}",
    "é": r"{\'e}", "è": r"{\`e}", "ê": r"{\^e}", "ë": r'{\"e}',
    "í": r"{\'i}", "ì": r"{\`i}", "î": r"{\^i}", "ï": r'{\"i}',
    "ó": r"{\'o}", "ò": r"{\`o}", "ô": r"{\^o}", "ö": r'{\"o}', "õ": r"{\~o}",
    "ú": r"{\'u}", "ù": r"{\`u}", "û": r"{\^u}", "ü": r'{\"u}',
    "ý": r"{\'y}", "ÿ": r'{\"y}',
    "ñ": r"{\~n}", "ç": r"{\c{c}}",
    "Á": r"{\'A}", "À": r"{\`A}", "Â": r"{\^A}", "Ä": r'{\"A}',
    "É": r"{\'E}", "È": r"{\`E}", "Ê": r"{\^E}", "Ë": r'{\"E}',
    "Í": r"{\'I}", "Ì": r"{\`I}", "Î": r"{\^I}", "Ï": r'{\"I}',
    "Ó": r"{\'O}", "Ò": r"{\`O}", "Ô": r"{\^O}", "Ö": r'{\"O}',
    "Ú": r"{\'U}", "Ù": r"{\`U}", "Û": r"{\^U}", "Ü": r'{\"U}',
    "Ñ": r"{\~N}", "Ç": r"{\c{C}}",
}


@dataclass
class ArxivEntry:
    arxiv_id: str              # bare "YYMM.NNNNN" with no version
    title: str
    authors: list[str]         # as they appear in the feed, e.g. "Yaé U. Gaba"
    year: int
    primary_class: str         # e.g. "cs.LG"


def fetch_atom(author_id: str, timeout: float = 20.0) -> bytes:
    url = f"https://arxiv.org/a/{author_id}.atom"
    req = urllib.request.Request(url, headers={"User-Agent": "gabayae-arxiv-sync/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def parse_atom(raw: bytes) -> list[ArxivEntry]:
    root = ET.fromstring(raw)
    out: list[ArxivEntry] = []
    for entry in root.findall(f"{ATOM_NS}entry"):
        id_el = entry.find(f"{ATOM_NS}id")
        title_el = entry.find(f"{ATOM_NS}title")
        pub_el = entry.find(f"{ATOM_NS}published")
        prim_el = entry.find(f"{ARXIV_NS}primary_category")
        if id_el is None or title_el is None or pub_el is None:
            continue
        raw_id = (id_el.text or "").strip()
        m = re.search(r"abs/([\d\.]+)(?:v\d+)?$", raw_id)
        if not m:
            continue
        arxiv_id = m.group(1)
        title = re.sub(r"\s+", " ", (title_el.text or "").strip())
        year = int((pub_el.text or "")[:4])
        primary = (prim_el.get("term") if prim_el is not None else "") or ""
        authors = [
            re.sub(r"\s+", " ", (a.findtext(f"{ATOM_NS}name") or "").strip())
            for a in entry.findall(f"{ATOM_NS}author")
        ]
        authors = [a for a in authors if a]
        out.append(ArxivEntry(arxiv_id=arxiv_id, title=title, authors=authors, year=year, primary_class=primary))
    return out


def extract_existing_ids(bib_text: str) -> set[str]:
    ids: set[str] = set()
    for field in ("eprint", "arxiv"):
        for m in re.finditer(rf"{field}\s*=\s*\{{([^}}]+)\}}", bib_text, flags=re.IGNORECASE):
            raw = m.group(1).strip()
            raw = re.sub(r"v\d+$", "", raw)   # strip version if present
            if raw:
                ids.add(raw)
    return ids


def latex_escape(s: str) -> str:
    return "".join(ACCENT_MAP.get(ch, ch) for ch in s)


def format_author(name: str) -> str:
    """'Yaé U. Gaba' -> 'Gaba, Ya{\\'e} U.'; 'Christophe D. Hounwanou' -> 'Hounwanou, Christophe D.'."""
    parts = name.strip().split()
    if len(parts) < 2:
        return latex_escape(name)
    last = parts[-1]
    first = " ".join(parts[:-1])
    return f"{latex_escape(last)}, {latex_escape(first)}"


def ascii_key_token(s: str) -> str:
    """Lowercase, strip diacritics, keep [a-z0-9]."""
    norm = unicodedata.normalize("NFKD", s)
    stripped = "".join(ch for ch in norm if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]", "", stripped.lower())


STOPWORDS = {
    "a", "an", "the", "on", "of", "for", "to", "in", "and", "or", "with",
    "from", "by", "at", "into", "via", "as", "is", "are", "be",
}


def generate_key(entry: ArxivEntry, existing_keys: set[str]) -> str:
    first_author_last = entry.authors[0].split()[-1] if entry.authors else "paper"
    first_token = ascii_key_token(first_author_last) or "paper"
    title_tokens = [ascii_key_token(w) for w in re.split(r"[^A-Za-z0-9]+", entry.title) if w]
    title_tokens = [t for t in title_tokens if t and t not in STOPWORDS]
    short = title_tokens[0] if title_tokens else "paper"
    base = f"{first_token}{entry.year}{short}"
    key = base
    suffix_index = 2
    while key in existing_keys:
        key = f"{base}{suffix_index}"
        suffix_index += 1
    return key


def render_entry(entry: ArxivEntry, key: str) -> str:
    authors = " and ".join(format_author(a) for a in entry.authors) or "Gaba, Ya{\\'e} Ulrich"
    return (
        f"@article{{{key},\n"
        f"  bibtex_show  = {{true}},\n"
        f"  title        = {{{entry.title}}},\n"
        f"  author       = {{{authors}}},\n"
        f"  year         = {{{entry.year}}},\n"
        f"  eprint       = {{{entry.arxiv_id}}},\n"
        f"  archiveprefix = {{arXiv}},\n"
        f"  primaryclass = {{{entry.primary_class}}},\n"
        f"  arxiv        = {{{entry.arxiv_id}}},\n"
        f"  abbr         = {{arXiv}}\n"
        f"}}\n"
    )


def extract_existing_keys(bib_text: str) -> set[str]:
    return {m.group(1) for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib_text)}


def insert_entries(bib_text: str, new_block: str, author_id: str, today: str) -> str:
    """Insert new entries immediately after the ARXIV SYNC header, keeping the
    block contiguous. Also refreshes the header's date to today's.

    If no header exists: place a header + entries before the trailing
    "% Additional publications..." comment (if any), otherwise at EOF.
    """
    header_re = re.compile(
        r"^% ---- ARXIV SYNC \d{4}-\d{2}-\d{2} \(preprints from arxiv\.org/a/[^)]+\.html not already listed above\) ----\s*$",
        flags=re.MULTILINE,
    )
    new_header = f"% ---- ARXIV SYNC {today} (preprints from arxiv.org/a/{author_id}.html not already listed above) ----"

    m = header_re.search(bib_text)
    if m:
        insertion = new_header + "\n\n" + new_block
        return bib_text[: m.start()] + insertion + bib_text[m.end() :]

    trailing_comment_re = re.compile(
        r"^% Additional publications can be exported from:", flags=re.MULTILINE
    )
    header_block = new_header + "\n\n" + new_block + "\n"
    cm = trailing_comment_re.search(bib_text)
    if cm:
        return bib_text[: cm.start()] + header_block + bib_text[cm.start() :]
    tail = "" if bib_text.endswith("\n") else "\n"
    return bib_text + tail + "\n" + header_block


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bib", default="_bibliography/papers.bib")
    parser.add_argument("--author-id", default="gaba_y_1")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    bib_path = Path(args.bib)
    if not bib_path.is_file():
        print(f"error: bib file not found: {bib_path}", file=sys.stderr)
        return 2

    bib_text = bib_path.read_text(encoding="utf-8")
    existing_ids = extract_existing_ids(bib_text)
    existing_keys = extract_existing_keys(bib_text)

    try:
        raw = fetch_atom(args.author_id)
    except Exception as exc:  # noqa: BLE001 — surface any fetch failure in the CI log
        print(f"error: failed to fetch arXiv feed: {exc}", file=sys.stderr)
        return 1

    feed_entries = parse_atom(raw)
    print(f"arxiv feed: {len(feed_entries)} entries; bib: {len(existing_ids)} arxiv IDs already tracked")

    new_entries: list[tuple[str, ArxivEntry]] = []
    for e in feed_entries:
        if e.arxiv_id in existing_ids:
            continue
        key = generate_key(e, existing_keys)
        existing_keys.add(key)
        new_entries.append((key, e))

    if not new_entries:
        print("nothing new — bib is up to date.")
        return 0

    rendered = "\n".join(render_entry(e, key) for key, e in new_entries)
    today = dt.date.today().isoformat()

    print(f"{len(new_entries)} new entry(ies) to add:")
    for key, e in new_entries:
        print(f"  - {key}  ({e.arxiv_id}) {e.title[:60]}...")

    if args.dry_run:
        print("--- dry run, not writing ---")
        print(rendered)
        return 0

    updated = insert_entries(bib_text, rendered, args.author_id, today)
    bib_path.write_text(updated, encoding="utf-8")
    print(f"wrote {bib_path} (+{len(new_entries)} entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
