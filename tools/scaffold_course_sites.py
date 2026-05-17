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

**Course:** {title}
**Level:** {level}
**Instructor:** {instructor}
**Meeting pattern:** {meeting_pattern}

**Operational pages.** &nbsp; [Weekly schedule]({{{{ '/courses/{slug}/cohort/schedule/' | relative_url }}}}) &nbsp;|&nbsp; [Course notes (PDF)]({{{{ '{notes_pdf}' | relative_url }}}})

---

{pitch}

---

## Prerequisites

{prerequisites}

## Grading

{grading}

## Reading

{textbook}

{caveat_block}

## How this site works

- The bilingual lecture notes ([EN PDF]({{{{ '{notes_pdf}' | relative_url }}}}){fr_pdf_link}) remain the reference text.
- This **cohort site** is the operational layer for participants enrolled in a live cohort: weekly pages with the lecture topic, readings, problem sets, code labs, and paper discussions.
- The single source of truth for the schedule is `_data/{slug}.yml` in the site repository. Editing one YAML entry updates every place the week appears.
- Past-cohort recordings are linked on each week page once the session is complete.

## Going to the weekly material

Use the [schedule]({{{{ '/courses/{slug}/cohort/schedule/' | relative_url }}}}) page to navigate to any week, or jump directly:

{week_links}
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

    week_links = "\n".join(
        f"- [Week {w['number']} — {w['title']}]({{{{ '/courses/{slug}/cohort/week-{w['number']}/' | relative_url }}}})"
        for w in weeks
    )

    caveat_block = ""
    if course.get("caveat"):
        caveat_block = f"## A note on freshness\n\n{course['caveat']}\n"

    fr_pdf_link = ""
    if course.get("notes_pdf_fr"):
        fr_pdf_link = f" · [FR PDF]({{{{ '{course['notes_pdf_fr']}' | relative_url }}}})"

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
        fr_pdf_link=fr_pdf_link,
        caveat_block=caveat_block,
        week_links=week_links,
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
