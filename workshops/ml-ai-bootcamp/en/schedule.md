---
layout: page
permalink: /workshops/ml-ai-bootcamp/en/schedule/
title: "Bootcamp — Weekly schedule"
description: "Week-by-week schedule of the AIRINA Labs Machine Learning & AI Bootcamp."
lang: en
nav: false
---

The operational schedule for one full-time cohort (ten weeks). Part-time cohorts run the same content over twenty weeks at half the weekly load. Per-cohort dates fill in at intake; the structure below is stable across cohorts.

For program rationale, prerequisites, and the ten-module curriculum overview, see the [syllabus]({{ '/workshops/ml-ai-bootcamp/en/' | relative_url }}). For the final project, see the [capstone brief]({{ '/workshops/ml-ai-bootcamp/CAPSTONE/' | relative_url }}).

---

<div class="bootcamp-schedule">

<table>
  <thead>
    <tr><th>Week</th><th>Module</th><th>Title</th><th>Deliverable</th><th>Detail</th></tr>
  </thead>
  <tbody>
  {% for week in site.data.bootcamp.weeks %}
    <tr>
      <td><strong>{{ week.number }}</strong></td>
      <td>{{ week.module }}</td>
      <td><a href="{{ '/workshops/ml-ai-bootcamp/en/week-' | append: week.number | append: '/' | relative_url }}"><strong>{{ week.title }}</strong></a><br><em>{{ week.pitch }}</em></td>
      <td>{{ week.deliverable | markdownify | remove: "<p>" | remove: "</p>" | truncate: 140 }}</td>
      <td><a href="{{ '/workshops/ml-ai-bootcamp/en/week-' | append: week.number | append: '/' | relative_url }}">week {{ week.number }} →</a></td>
    </tr>
  {% endfor %}
  </tbody>
</table>

</div>

## How the week pages work

Every week page is generated from a single source — [`_data/bootcamp.yml`](https://github.com/gabayae/gabayae.github.io/blob/main/_data/bootcamp.yml) — so the data lives in one place. Each week page renders:

1. **What you ship this week** — the deliverable, due date, submission channel, rubric.
2. **Live sessions and labs** — the default weekly cadence (Mon–Thu live + lab blocks, Friday speaker / lab review / retrospective), with per-cohort dates and Zoom links filled in inline.
3. **Learning outcomes and topics covered.**
4. **Labs** — three to four hands-on projects per week, with the dataset link and the task spec.
5. **Readings** — split into mandatory (with the "before X" day specified) and optional deepening.
6. **Catalogue cross-references** — back to the existing [course notes]({{ '/courses/' | relative_url }}) when there is a corresponding course.

## Operational notes

- Sessions run on **Africa/Lagos time (UTC+1)** by default. Part-time cohorts negotiate times at intake.
- Lab notebooks live in a [public GitHub repo](https://github.com/AI-Technipreneurs) that mirrors this schedule. Each week's lab is a tagged release.
- Capstone milestones are interleaved with the regular modules: proposal in week 4, midterm review in week 7, code freeze week 9, final presentations week 10.
- Past-cohort recordings are linked on each week page once the session is complete and retained for at least twelve months.
