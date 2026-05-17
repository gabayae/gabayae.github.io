---
layout: page
permalink: /courses/mlops/cohort/
title: "MLOps — From Notebook to Production — Cohort site"
description: "What it takes for a machine-learning model to keep working after the notebook is closed: containerization, deployment, monitoring, reproducibility, and the engineering discipline that distinguishes a prototype from a production system."
lang: en
nav: false
---

<p style="font-size: 1.15em; line-height: 1.55; color: var(--global-text-color, #333); margin-bottom: 1.6em;">What it takes for a machine-learning model to keep working after the notebook is closed: containerization, deployment, monitoring, reproducibility, and the engineering discipline that distinguishes a prototype from a production system.</p>

<div style="display: flex; flex-wrap: wrap; gap: 18px; margin: 1.4em 0 2em 0; font-size: 0.95em;">
  <a href="{{ '/courses/mlops/cohort/schedule/' | relative_url }}" style="padding: 10px 18px; background: rgba(59,111,212,0.12); border: 1px solid rgba(59,111,212,0.45); border-radius: 6px; text-decoration: none; font-weight: 600;">→ Weekly schedule</a>
  <a href="{{ '/courses/mlops/en/notes.pdf' | relative_url }}" style="padding: 10px 18px; background: rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.15); border-radius: 6px; text-decoration: none;">EN notes (PDF)</a>
  <a href="{{ '/courses/mlops/fr/cours.pdf' | relative_url }}" style="padding: 10px 18px; background: rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.15); border-radius: 6px; text-decoration: none;">FR notes (PDF)</a>
</div>

<table style="margin-bottom: 1.8em;">
<tr><th style="text-align:left;">Level</th><td>Graduate / professional</td></tr>
<tr><th style="text-align:left;">Instructor</th><td>Dr. Yaé Ulrich Gaba</td></tr>
<tr><th style="text-align:left;">Meeting pattern</th><td>Tuesdays + Thursdays, 14:00–16:00 lecture · Fridays 14:00–15:00 systems review (Africa/Lagos UTC+1)</td></tr>
</table>

## Prerequisites

Comfortable Python (functions, classes, virtual environments). At least one prior ML project (any course in the catalogue). Basic command-line proficiency. Familiarity with Git.

## Grading

Five labs (50%) · two systems-design memos (20%) · final deployed capstone (30%).

## Reading

Chip Huyen, *Designing Machine Learning Systems* (O'Reilly 2022) — recommended companion.



## What this site is and isn't

The bilingual notes (linked above) are the reference text. This cohort site is the operational layer: every week page has the lecture topic, the readings to do beforehand, the problem set or code lab, and any paper discussion. The schedule and weeks are generated from a single data file (`_data/mlops.yml`), so the same source drives the landing, the schedule, and every week page. If you are reading along without being in a cohort, the week pages still work as a self-study guide; the deliverables become optional, but the readings and lecture topics are the same.
