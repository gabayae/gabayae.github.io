---
layout: page
permalink: /courses/ia-generative/cohort/
title: "Generative AI — Cohort site"
description: "Transformers, GPT-class language models, prompt engineering, LoRA fine-tuning, RAG, diffusion models, agents, and the evaluation problem none of this has solved."
lang: en
nav: false
---

<p style="font-size: 1.15em; line-height: 1.55; color: var(--global-text-color, #333); margin-bottom: 1.6em;">Transformers, GPT-class language models, prompt engineering, LoRA fine-tuning, RAG, diffusion models, agents, and the evaluation problem none of this has solved.</p>

<div style="display: flex; flex-wrap: wrap; gap: 18px; margin: 1.4em 0 2em 0; font-size: 0.95em;">
  <a href="{{ '/courses/ia-generative/cohort/schedule/' | relative_url }}" style="padding: 10px 18px; background: rgba(59,111,212,0.12); border: 1px solid rgba(59,111,212,0.45); border-radius: 6px; text-decoration: none; font-weight: 600;">→ Weekly schedule</a>
  <a href="{{ '/courses/ia-generative/en/notes.pdf' | relative_url }}" style="padding: 10px 18px; background: rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.15); border-radius: 6px; text-decoration: none;">EN notes (PDF)</a>
  <a href="{{ '/courses/ia-generative/fr/cours.pdf' | relative_url }}" style="padding: 10px 18px; background: rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.15); border-radius: 6px; text-decoration: none;">FR notes (PDF)</a>
</div>

<table style="margin-bottom: 1.8em;">
<tr><th style="text-align:left;">Level</th><td>Graduate</td></tr>
<tr><th style="text-align:left;">Instructor</th><td>Dr. Yaé Ulrich Gaba</td></tr>
<tr><th style="text-align:left;">Meeting pattern</th><td>Mondays + Wednesdays, 14:00–16:00 lecture · Fridays 14:00–15:00 paper discussion (Africa/Lagos UTC+1)</td></tr>
</table>

## Prerequisites

Deep learning at the level of one prior course. PyTorch fluency. Comfortable reading recent NeurIPS / ICLR papers. Familiarity with the transformer architecture is a plus but not required — week 2 builds it.

## Grading

Four labs (40%) · two paper-discussion reviews (15%) · final deployed agent or RAG system (45%).

## Reading

No standard textbook — the field moves too fast. Reading list is curated weekly from arXiv.

## A note on freshness

Generative AI moves fast enough that the reading list, lab tooling, and code lab versions are reviewed and updated at the start of every cohort. The structure below is stable; the specific models, frameworks, and benchmarks are not.


## What this site is and isn't

The bilingual notes (linked above) are the reference text. This cohort site is the operational layer: every week page has the lecture topic, the readings to do beforehand, the problem set or code lab, and any paper discussion. The schedule and weeks are generated from a single data file (`_data/ia-generative.yml`), so the same source drives the landing, the schedule, and every week page. If you are reading along without being in a cohort, the week pages still work as a self-study guide; the deliverables become optional, but the readings and lecture topics are the same.
