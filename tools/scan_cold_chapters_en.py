#!/usr/bin/env python3
"""Scan every EN chapter file (ch01+) for cold openings.

Cold = first non-banner content line is a \\section, \\begin{definition},
       \\begin{intuition}, \\begin{minted}, \\begin{quote}, or
       \\begin{center} epigraph followed directly by a \\section.
Warm = a prose paragraph sits between the chapter banner and the first
       \\section.

The classifier mirrors tools/scan_cold_chapters.py but walks
courses/*/en/chapters/*.tex.

Run:
    python tools/scan_cold_chapters_en.py
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
    "bibliography.tex",
    "references.tex",
    "notes.tex",
    "cours.tex",
}

CHAPTER_RE = re.compile(r"\\chapter\*?\{")
SECTION_RE = re.compile(r"\\section\*?\{")
ENV_RE = re.compile(
    r"\\begin\{(definition|theorem|proposition|lemma|corollary|example|exercise|minted|quote|center|equation|align|figure|tabular|itemize|enumerate|intuition|datatip|warningbox|preprocesstip|remark|note)\}"
)
HOOK_MARKER = "% --- hook ---"


def classify(path: pathlib.Path) -> tuple[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ("skip", "encoding")
    if HOOK_MARKER in text[:3000]:
        return ("hooked", "already has hook marker")
    lines = text.splitlines()
    chap_idx = None
    for i, line in enumerate(lines):
        if CHAPTER_RE.search(line):
            chap_idx = i
            break
    if chap_idx is None:
        return ("skip", "no \\chapter line")
    banner_skip_re = re.compile(
        r"^\s*(%|\\label\{|\\index\{|\\addcontentsline\{|\\markboth\{|\\thispagestyle\{|$)"
    )
    for j in range(chap_idx + 1, min(chap_idx + 40, len(lines))):
        line = lines[j]
        if banner_skip_re.match(line):
            continue
        stripped = line.strip()
        if SECTION_RE.search(stripped):
            return ("cold", f"first content line is a \\section (line {j+1})")
        m = ENV_RE.search(stripped)
        if m:
            env = m.group(1)
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
                    return ("cold", f"{env} unterminated")
                bench_skip = re.compile(
                    r"^\s*(%|\\bigskip|\\medskip|\\smallskip|\\vspace|\\label\{|\\index\{|$)"
                )
                for m2 in range(env_end_idx + 1, min(env_end_idx + 25, len(lines))):
                    tail = lines[m2].strip()
                    if bench_skip.match(lines[m2]):
                        continue
                    if SECTION_RE.search(tail):
                        if env == "intuition":
                            body_text = " ".join(env_body)
                            non_blank = [b for b in env_body if b.strip() and not b.strip().startswith("%")]
                            anchor_re = re.compile(
                                r"\b(in \d{4}|18\d\d|19\d\d|20\d\d|imagine|consider|example|recipe|kitchen|as |according to)",
                                re.IGNORECASE,
                            )
                            if len(non_blank) >= 4 or anchor_re.search(body_text):
                                return ("warm", f"intuition with narrative content ({len(non_blank)} lines)")
                            return ("cold", f"intuition with dry/short content then \\section")
                        return ("cold", f"{env} epigraph then \\section, no prose hook")
                    if ENV_RE.search(tail):
                        return ("cold", f"{env} then another env, no prose hook")
                    return ("warm", f"{env} + prose hook at line {m2+1}")
                return ("cold", f"{env} with no follow-up content")
            return ("cold", f"first content line is \\begin{{{env}}} (line {j+1})")
        return ("warm", f"prose line at {j+1}: {stripped[:60]}")
    return ("skip", "no content after banner")


def main() -> int:
    rows: list[tuple[str, pathlib.Path, str]] = []
    for course in sorted(COURSES.iterdir()):
        en_chap = course / "en" / "chapters"
        if not en_chap.is_dir():
            # Some nested courses (algebre-abstraite/I etc.) have chapters one level deeper.
            for sub in course.glob("*/en/chapters"):
                if sub.is_dir():
                    rows.extend(_classify_dir(sub))
            continue
        rows.extend(_classify_dir(en_chap))

    cold = [r for r in rows if r[0] == "cold"]
    warm = [r for r in rows if r[0] == "warm"]
    hooked = [r for r in rows if r[0] == "hooked"]
    skipped = [r for r in rows if r[0] == "skip"]

    print("=== SUMMARY ===")
    print(f"  cold:    {len(cold)}")
    print(f"  warm:    {len(warm)}")
    print(f"  hooked:  {len(hooked)}")
    print(f"  skipped: {len(skipped)}")
    print(f"  total:   {len(rows)}")

    print("\n=== COLD ===")
    for _, p, reason in cold:
        print(f"  {p}  [{reason}]")

    return 0


def _classify_dir(d: pathlib.Path) -> list[tuple[str, pathlib.Path, str]]:
    out: list[tuple[str, pathlib.Path, str]] = []
    for tex in sorted(d.glob("*.tex")):
        if tex.name in SKIP_FILENAMES:
            continue
        if tex.name.startswith("ch00"):
            continue
        status, reason = classify(tex)
        out.append((status, tex.relative_to(REPO_ROOT), reason))
    return out


if __name__ == "__main__":
    sys.exit(main())
