#!/usr/bin/env python3
"""Generate the per-course cohort site shells (landing, schedule, week-NN
pages) for the 6 candidate courses. Reads from _data/<slug>.yml; emits to
courses/<slug>/cohort/.

Idempotent — re-running overwrites the shells but never the data file.
"""
from __future__ import annotations
import pathlib
import sys

import yaml

REPO = pathlib.Path(__file__).resolve().parents[1]

SLUGS = [
    "tda",
    "apprentissage-geometrique",
    "apprentissage-renforcement",
    "mlops",
    "ia-generative",
    "apprentissage-automatique",
]

LANDING_TPL = """---
layout: page
permalink: /courses/{slug}/cohort/
title: "{title} — Cohort site"
description: "{pitch}"
lang: en
nav: false
---

<p style="font-size: 1.15em; line-height: 1.55; color: var(--global-text-color, #333); margin-bottom: 1.6em;">{pitch}</p>

<div style="display: flex; flex-wrap: wrap; gap: 18px; margin: 1.4em 0 2em 0; font-size: 0.95em;">
  <a href="{{{{ '/courses/{slug}/cohort/schedule/' | relative_url }}}}" style="padding: 10px 18px; background: rgba(59,111,212,0.12); border: 1px solid rgba(59,111,212,0.45); border-radius: 6px; text-decoration: none; font-weight: 600;">→ Weekly schedule</a>
  <a href="{{{{ '{notes_pdf}' | relative_url }}}}" style="padding: 10px 18px; background: rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.15); border-radius: 6px; text-decoration: none;">EN notes (PDF)</a>{fr_pdf_button}
</div>

<table style="margin-bottom: 1.8em;">
<tr><th style="text-align:left;">Level</th><td>{level}</td></tr>
<tr><th style="text-align:left;">Instructor</th><td>{instructor}</td></tr>
<tr><th style="text-align:left;">Meeting pattern</th><td>{meeting_pattern}</td></tr>
</table>

## Prerequisites

{prerequisites}

## Grading

{grading}

## Reading

{textbook}

{caveat_block}

## What this site is and isn't

The bilingual notes (linked above) are the reference text. This cohort site is the operational layer: every week page has the lecture topic, the readings to do beforehand, the problem set or code lab, and any paper discussion. The schedule and weeks are generated from a single data file (`_data/{slug}.yml`), so the same source drives the landing, the schedule, and every week page. If you are reading along without being in a cohort, the week pages still work as a self-study guide; the deliverables become optional, but the readings and lecture topics are the same.
"""

SCHEDULE_TPL = """---
layout: page
permalink: /courses/{slug}/cohort/schedule/
title: "{title} — Schedule"
description: "Week-by-week schedule of {title}."
lang: en
nav: false
---

[← cohort home]({{{{ '/courses/{slug}/cohort/' | relative_url }}}})

The operational schedule for {title}. Per-cohort dates fill in at intake; the structure below is stable across cohorts.

The single source of truth is `_data/{slug}.yml`. Edits there flow through this page automatically.

---

<table>
  <thead>
    <tr><th>Week</th><th>Title</th><th>Pitch</th><th>Detail</th></tr>
  </thead>
  <tbody>
  {{% for week in site.data.{slug}.weeks %}}
    <tr>
      <td><strong>{{{{ week.number }}}}</strong></td>
      <td><a href="{{{{ '/courses/{slug}/cohort/week-' | append: week.number | append: '/' | relative_url }}}}"><strong>{{{{ week.title }}}}</strong></a></td>
      <td><em>{{{{ week.pitch }}}}</em></td>
      <td><a href="{{{{ '/courses/{slug}/cohort/week-' | append: week.number | append: '/' | relative_url }}}}">week {{{{ week.number }}}} →</a></td>
    </tr>
  {{% endfor %}}
  </tbody>
</table>

---

## Operational notes

- Default timezone: **Africa/Lagos (UTC+1)**. Per-cohort timing negotiated at intake.
- Lab notebooks and problem-set repos live in the cohort GitHub organization.
- The [bilingual lecture notes]({{{{ '{notes_pdf}' | relative_url }}}}) remain the reference text.
"""

WEEK_TPL = """---
layout: page
permalink: /courses/{slug}/cohort/week-{num}/
title: "Week {num} — {week_title}"
description: "{pitch}"
lang: en
nav: false
---

{{% include course_site_week.liquid data_key="{slug}" week_number="{num}" %}}
"""


def scaffold_one(slug: str) -> None:
    data_path = REPO / "_data" / f"{slug}.yml"
    with data_path.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    course = data["course"]
    weeks = data["weeks"]

    cohort_dir = REPO / "courses" / slug / "cohort"
    cohort_dir.mkdir(parents=True, exist_ok=True)

    caveat_block = ""
    if course.get("caveat"):
        caveat_block = f"## A note on freshness\n\n{course['caveat']}\n"

    fr_pdf_button = ""
    if course.get("notes_pdf_fr"):
        fr_pdf_button = (
            f'\n  <a href="{{{{ \'{course["notes_pdf_fr"]}\' | relative_url }}}}" '
            f'style="padding: 10px 18px; background: rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.15); '
            f'border-radius: 6px; text-decoration: none;">FR notes (PDF)</a>'
        )

    landing = LANDING_TPL.format(
        slug=slug,
        title=course["title"],
        pitch=course["pitch"],
        level=course["level"],
        instructor=course["instructor"],
        meeting_pattern=course["meeting_pattern"],
        prerequisites=course["prerequisites"],
        grading=course["grading"],
        textbook=course.get("textbook", "—"),
        notes_pdf=course["notes_pdf"],
        fr_pdf_button=fr_pdf_button,
        caveat_block=caveat_block,
    )
    (cohort_dir / "index.md").write_text(landing, encoding="utf-8")

    schedule = SCHEDULE_TPL.format(
        slug=slug,
        title=course["title"],
        notes_pdf=course["notes_pdf"],
    )
    (cohort_dir / "schedule.md").write_text(schedule, encoding="utf-8")

    for w in weeks:
        week_md = WEEK_TPL.format(
            slug=slug,
            num=w["number"],
            week_title=w["title"],
            pitch=w["pitch"].replace('"', "'"),
        )
        (cohort_dir / f"week-{w['number']}.md").write_text(week_md, encoding="utf-8")

    print(f"  {slug}: landing + schedule + {len(weeks)} week shells in {cohort_dir.relative_to(REPO)}")


def main() -> int:
    for slug in SLUGS:
        scaffold_one(slug)
    print(f"\nScaffolded {len(SLUGS)} cohort sites. Files emitted under courses/<slug>/cohort/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
