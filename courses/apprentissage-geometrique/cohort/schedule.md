---
layout: page
permalink: /courses/apprentissage-geometrique/cohort/schedule/
title: "Geometric Deep Learning — Schedule"
description: "Week-by-week schedule of Geometric Deep Learning."
lang: en
nav: false
---

[← cohort home]({{ '/courses/apprentissage-geometrique/cohort/' | relative_url }})

The operational schedule for Geometric Deep Learning. Per-cohort dates fill in at intake; the structure below is stable across cohorts.

The single source of truth is `_data/apprentissage-geometrique.yml`. Edits there flow through this page automatically.

---

<table>
  <thead>
    <tr><th>Week</th><th>Title</th><th>Pitch</th><th>Detail</th></tr>
  </thead>
  <tbody>
  {% for week in site.data.apprentissage-geometrique.weeks %}
    <tr>
      <td><strong>{{ week.number }}</strong></td>
      <td><a href="{{ '/courses/apprentissage-geometrique/cohort/week-' | append: week.number | append: '/' | relative_url }}"><strong>{{ week.title }}</strong></a></td>
      <td><em>{{ week.pitch }}</em></td>
      <td><a href="{{ '/courses/apprentissage-geometrique/cohort/week-' | append: week.number | append: '/' | relative_url }}">week {{ week.number }} →</a></td>
    </tr>
  {% endfor %}
  </tbody>
</table>

---

## Operational notes

- Default timezone: **Africa/Lagos (UTC+1)**. Per-cohort timing negotiated at intake.
- Lab notebooks and problem-set repos live in the cohort GitHub organization.
- The [bilingual lecture notes]({{ '/courses/apprentissage-geometrique/en/notes.pdf' | relative_url }}) remain the reference text.
