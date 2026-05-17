---
layout: page
permalink: /courses/apprentissage-geometrique/cohort/
title: "Geometric Deep Learning — Cohort site"
description: "Neural networks that respect the symmetries of their input domain — translation, rotation, permutation, graph structure. The mathematical thesis that ties GNNs, equivariant networks, and AlphaFold together."
lang: en
nav: false
---

<p style="font-size: 1.15em; line-height: 1.55; color: var(--global-text-color, #333); margin-bottom: 1.6em;">Neural networks that respect the symmetries of their input domain — translation, rotation, permutation, graph structure. The mathematical thesis that ties GNNs, equivariant networks, and AlphaFold together.</p>

<div style="display: flex; flex-wrap: wrap; gap: 18px; margin: 1.4em 0 2em 0; font-size: 0.95em;">
  <a href="{{ '/courses/apprentissage-geometrique/cohort/schedule/' | relative_url }}" style="padding: 10px 18px; background: rgba(59,111,212,0.12); border: 1px solid rgba(59,111,212,0.45); border-radius: 6px; text-decoration: none; font-weight: 600;">→ Weekly schedule</a>
  <a href="{{ '/courses/apprentissage-geometrique/en/notes.pdf' | relative_url }}" style="padding: 10px 18px; background: rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.15); border-radius: 6px; text-decoration: none;">EN notes (PDF)</a>
  <a href="{{ '/courses/apprentissage-geometrique/fr/cours.pdf' | relative_url }}" style="padding: 10px 18px; background: rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.15); border-radius: 6px; text-decoration: none;">FR notes (PDF)</a>
</div>

<table style="margin-bottom: 1.8em;">
<tr><th style="text-align:left;">Level</th><td>Graduate</td></tr>
<tr><th style="text-align:left;">Instructor</th><td>Dr. Yaé Ulrich Gaba</td></tr>
<tr><th style="text-align:left;">Meeting pattern</th><td>Tuesdays 14:00–16:00 lecture · Thursdays 14:00–15:00 paper discussion (Africa/Lagos UTC+1)</td></tr>
</table>

## Prerequisites

Linear algebra and multivariable calculus. Basic deep learning (forward pass, backprop). Familiarity with PyTorch. No prior group theory required — week 2 builds it from scratch.

## Grading

Four problem sets (40%) · three code labs (25%) · paper-discussion recitations (10%) · final project (25%).

## Reading

Bronstein, Bruna, Cohen, Veličković, *Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges* (2021) — recommended companion.



## What this site is and isn't

The bilingual notes (linked above) are the reference text. This cohort site is the operational layer: every week page has the lecture topic, the readings to do beforehand, the problem set or code lab, and any paper discussion. The schedule and weeks are generated from a single data file (`_data/apprentissage-geometrique.yml`), so the same source drives the landing, the schedule, and every week page. If you are reading along without being in a cohort, the week pages still work as a self-study guide; the deliverables become optional, but the readings and lecture topics are the same.
