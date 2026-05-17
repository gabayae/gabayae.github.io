---
layout: page
permalink: /courses/tda/cohort/schedule/
title: "Topological Data Analysis — Schedule"
description: "Week-by-week schedule of Topological Data Analysis."
lang: en
nav: false
---

[← cohort home]({{ '/courses/tda/cohort/' | relative_url }})

The operational schedule for Topological Data Analysis. Per-cohort dates fill in at intake; the structure below is stable across cohorts.

The single source of truth is `_data/tda.yml`. Edits there flow through this page automatically.

---

<table>
  <thead>
    <tr><th>Week</th><th>Title</th><th>Pitch</th><th>Detail</th></tr>
  </thead>
  <tbody>
  {% for week in site.data.tda.weeks %}
    <tr>
      <td><strong>{{ week.number }}</strong></td>
      <td><a href="{{ '/courses/tda/cohort/week-' | append: week.number | append: '/' | relative_url }}"><strong>{{ week.title }}</strong></a></td>
      <td><em>{{ week.pitch }}</em></td>
      <td><a href="{{ '/courses/tda/cohort/week-' | append: week.number | append: '/' | relative_url }}">week {{ week.number }} →</a></td>
    </tr>
  {% endfor %}
  </tbody>
</table>

---

## Operational notes

- Default timezone: **Africa/Lagos (UTC+1)**. Per-cohort timing negotiated at intake.
- Lab notebooks and problem-set repos live in the cohort GitHub organization.
- The [bilingual lecture notes]({{ '/courses/tda/en/notes.pdf' | relative_url }}) remain the reference text.
