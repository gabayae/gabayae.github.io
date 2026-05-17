---
layout: page
permalink: /courses/mlops/cohort/schedule/
title: "MLOps — From Notebook to Production — Schedule"
description: "Week-by-week schedule of MLOps — From Notebook to Production."
lang: en
nav: false
---

[← cohort home]({{ '/courses/mlops/cohort/' | relative_url }})

The operational schedule for MLOps — From Notebook to Production. Per-cohort dates fill in at intake; the structure below is stable across cohorts.

The single source of truth is `_data/mlops.yml`. Edits there flow through this page automatically.

---

<table>
  <thead>
    <tr><th>Week</th><th>Title</th><th>Pitch</th><th>Detail</th></tr>
  </thead>
  <tbody>
  {% for week in site.data.mlops.weeks %}
    <tr>
      <td><strong>{{ week.number }}</strong></td>
      <td><a href="{{ '/courses/mlops/cohort/week-' | append: week.number | append: '/' | relative_url }}"><strong>{{ week.title }}</strong></a></td>
      <td><em>{{ week.pitch }}</em></td>
      <td><a href="{{ '/courses/mlops/cohort/week-' | append: week.number | append: '/' | relative_url }}">week {{ week.number }} →</a></td>
    </tr>
  {% endfor %}
  </tbody>
</table>

---

## Operational notes

- Default timezone: **Africa/Lagos (UTC+1)**. Per-cohort timing negotiated at intake.
- Lab notebooks and problem-set repos live in the cohort GitHub organization.
- The [bilingual lecture notes]({{ '/courses/mlops/en/notes.pdf' | relative_url }}) remain the reference text.
