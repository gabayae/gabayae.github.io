#!/usr/bin/env python3
"""
Scan every FR chapter file (ch02+ across all courses) and classify the
opening as 'cold' or 'warm'.

Cold = after the chapter banner, the first non-empty content line is a
       \section{...}, \begin{definition}, \begin{minted}, \begin{quote},
       or some other structural / box environment — i.e. no narrative
       prose paragraph between the chapter title and the first section.

Warm = at least one prose paragraph (or a quote+prose block, as in the
       ia-generative / pretraitement-donnees v2 hooks) sits between the
       chapter banner and the first section.

The scanner reads the first ~25 lines of each file and looks for the
first non-comment, non-empty line after \chapter{...}.

Run:
    python tools/scan_cold_chapters.py
"""
from __future__ import annotations
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
COURSES = REPO_ROOT / "courses"

SKIP_FILENAMES = {
    "preface.tex",
    "appendix_tools.tex",
    "appendix.tex",
    "bibliographie.tex",
    "references.tex",
    "notes.tex",
    "cours.tex",
}

CHAPTER_RE = re.compile(r"\\chapter\*?\{")
SECTION_RE = re.compile(r"\\section\*?\{")
ENV_RE = re.compile(r"\\begin\{(definition|theorem|proposition|lemma|corollary|example|exercise|minted|quote|center|equation|align|figure|tabular|itemize|enumerate|intuition|datatip|warningbox|preprocesstip|remark|note)\}")
HOOK_MARKER = "% --- hook ---"


def classify(path: pathlib.Path) -> tuple[str, str]:
    """Return (status, reason) where status in {'cold','warm','hooked','skip'}."""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ("skip", "encoding")

    if HOOK_MARKER in text[:3000]:
        return ("hooked", "already has hook marker")

    lines = text.splitlines()
    # Find the \chapter line
    chap_idx = None
    for i, line in enumerate(lines):
        if CHAPTER_RE.search(line):
            chap_idx = i
            break
    if chap_idx is None:
        return ("skip", "no \\chapter line")

    # Walk after the chapter line. Skip lines that are part of the chapter
    # banner: comment lines, \label{}, \index{}, \addcontentsline{}, \markboth{}, empty lines.
    banner_skip_re = re.compile(r"^\s*(%|\\label\{|\\index\{|\\addcontentsline\{|\\markboth\{|\\thispagestyle\{|$)")
    for j in range(chap_idx + 1, min(chap_idx + 40, len(lines))):
        line = lines[j]
        if banner_skip_re.match(line):
            continue
        # First substantive line found.
        stripped = line.strip()
        if SECTION_RE.search(stripped):
            return ("cold", f"first content line is a \\section (line {j+1})")
        m = ENV_RE.search(stripped)
        if m:
            env = m.group(1)
            # Environments that can host a warm narrative opening if followed
            # by prose: quote (epigraph), center (epigraph), intuition (idea box).
            if env in ("quote", "center", "intuition"):
                end_tag = f"\\end{{{env}}}"
                env_end_idx = None
                env_body: list[str] = []
                for k in range(j + 1, min(j + 60, len(lines))):
                    if end_tag in lines[k]:
                        env_end_idx = k
                        break
                    env_body.append(lines[k])
                if env_end_idx is None:
                    return ("cold", f"{env} environment unterminated in first 60 lines")
                # Peek after the environment for a prose paragraph before the
                # first \section. Skip blank lines, comments, \bigskip, \medskip,
                # \vspace, \label, \index.
                bench_skip = re.compile(r"^\s*(%|\\bigskip|\\medskip|\\smallskip|\\vspace|\\label\{|\\index\{|$)")
                for m2 in range(env_end_idx + 1, min(env_end_idx + 25, len(lines))):
                    tail = lines[m2].strip()
                    if bench_skip.match(lines[m2]):
                        continue
                    if SECTION_RE.search(tail):
                        # No prose between env and section. For 'intuition',
                        # check if the env body itself is rich enough (>= 3 lines
                        # of prose, mentions a person/year/metaphor) to count as warm.
                        if env == "intuition":
                            body_text = " ".join(env_body)
                            non_blank = [b for b in env_body if b.strip() and not b.strip().startswith("%")]
                            # Heuristic: 4+ non-blank lines OR mention of historical anchor.
                            anchor_re = re.compile(r"\b(en \d{4}|18\d\d|19\d\d|20\d\d|imaginez|imagine|exemple|consid[ée]rons|c[oe]ur|recette|cuisine|comme |selon |dans le)", re.IGNORECASE)
                            if len(non_blank) >= 4 or anchor_re.search(body_text):
                                return ("warm", f"intuition with narrative content ({len(non_blank)} lines)")
                            return ("cold", f"intuition with dry/short content then \\section")
                        return ("cold", f"{env} epigraph then \\section, no prose hook")
                    if ENV_RE.search(tail):
                        return ("cold", f"{env} then another env, no prose hook")
                    # Found prose.
                    return ("warm", f"{env} + prose hook at line {m2+1}")
                return ("cold", f"{env} with no follow-up content in 25 lines")
            return ("cold", f"first content line is \\begin{{{env}}} (line {j+1})")
        # Plain text / prose
        return ("warm", f"prose line at {j+1}: {stripped[:60]}")
    return ("skip", "no content found after banner")


def main() -> int:
    rows: list[tuple[str, pathlib.Path, str]] = []
    for course in sorted(COURSES.iterdir()):
        fr_chap = course / "fr" / "chapitres"
        if not fr_chap.is_dir():
            continue
        for tex in sorted(fr_chap.glob("*.tex")):
            if tex.name in SKIP_FILENAMES:
                continue
            # Skip ch01 — already handled.
            if tex.name.startswith("ch01"):
                continue
            # Skip ch00 — installation/setup chapters get a pass.
            if tex.name.startswith("ch00"):
                continue
            status, reason = classify(tex)
            rel = tex.relative_to(REPO_ROOT)
            rows.append((status, rel, reason))

    cold = [r for r in rows if r[0] == "cold"]
    warm = [r for r in rows if r[0] == "warm"]
    hooked = [r for r in rows if r[0] == "hooked"]
    skipped = [r for r in rows if r[0] == "skip"]

    print(f"\n=== SUMMARY ===")
    print(f"  cold (need a hook):   {len(cold)}")
    print(f"  warm (already telling a story): {len(warm)}")
    print(f"  hooked (has % --- hook --- marker): {len(hooked)}")
    print(f"  skipped:              {len(skipped)}")
    print(f"  total:                {len(rows)}")

    print(f"\n=== COLD CHAPTERS (need hooks) ===")
    for _, p, reason in cold:
        print(f"  {p}  [{reason}]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
