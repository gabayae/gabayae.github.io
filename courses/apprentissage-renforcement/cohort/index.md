---
layout: page
permalink: /courses/apprentissage-renforcement/cohort/
title: "Reinforcement Learning — Cohort site"
description: "MDPs, dynamic programming, Q-learning, policy gradients, actor-critic, modern algorithms (PPO, SAC), and the new RLHF pipeline behind ChatGPT-class systems."
lang: en
nav: false
---

<div style="margin-bottom: 1em;"><span style="display: inline-block; padding: 4px 12px; background: rgba(120,120,120,0.12); border: 1px solid rgba(120,120,120,0.5); border-radius: 14px; font-size: 0.82em; font-family: monospace; letter-spacing: 0.04em; text-transform: uppercase;">self-study</span> <span style="color: var(--global-text-color-light, #777); font-size: 0.9em; margin-left: 6px;">Self-study reference — no active cohort</span></div>

<p style="font-size: 1.15em; line-height: 1.55; color: var(--global-text-color, #333); margin-bottom: 1.6em;">MDPs, dynamic programming, Q-learning, policy gradients, actor-critic, modern algorithms (PPO, SAC), and the new RLHF pipeline behind ChatGPT-class systems.</p>

<div style="display: flex; flex-wrap: wrap; gap: 18px; margin: 1.4em 0 2em 0; font-size: 0.95em;">
  <a href="{{ '/courses/apprentissage-renforcement/cohort/schedule/' | relative_url }}" style="padding: 10px 18px; background: rgba(59,111,212,0.12); border: 1px solid rgba(59,111,212,0.45); border-radius: 6px; text-decoration: none; font-weight: 600;">→ Weekly schedule</a>
  <a href="{{ '/courses/apprentissage-renforcement/en/notes.pdf' | relative_url }}" style="padding: 10px 18px; background: rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.15); border-radius: 6px; text-decoration: none;">EN notes (PDF)</a>
  <a href="{{ '/courses/apprentissage-renforcement/fr/cours.pdf' | relative_url }}" style="padding: 10px 18px; background: rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.15); border-radius: 6px; text-decoration: none;">FR notes (PDF)</a>
</div>

<table style="margin-bottom: 1.8em;">
<tr><th style="text-align:left;">Level</th><td>Graduate</td></tr>
<tr><th style="text-align:left;">Instructor</th><td>Dr. Yaé Ulrich Gaba</td></tr>
<tr><th style="text-align:left;">Meeting pattern</th><td>Mondays + Wednesdays, 14:00–16:00 lecture · Fridays 14:00–15:00 paper discussion (Africa/Lagos UTC+1)</td></tr>
</table>

## Prerequisites

Probability and statistics at the level of expectation, variance, and conditional probability. Linear algebra. Comfortable Python and PyTorch. No prior RL required.

## Grading

Five problem sets (35%) · three code labs (25%) · paper-discussion recitations (10%) · final project (30%).

## Reading

Sutton and Barto, *Reinforcement Learning: An Introduction* (2nd ed., MIT Press 2018) — required reference.



## What this site is and isn't

The bilingual notes (linked above) are the reference text. This cohort site is the operational layer: every week page has the lecture topic, the readings to do beforehand, the problem set or code lab, and any paper discussion. The schedule and weeks are generated from a single data file (`_data/apprentissage-renforcement.yml`), so the same source drives the landing, the schedule, and every week page. If you are reading along without being in a cohort, the week pages still work as a self-study guide; the deliverables become optional, but the readings and lecture topics are the same.
