---
layout: page
permalink: /workshops/ml-ai-bootcamp/en/week-01/
title: "Week 01 — Python for data work"
description: "Module 1 of the AIRINA Labs ML & AI Bootcamp. Idiomatic Python, NumPy, Pandas, reproducible projects, Jupyter discipline."
lang: en
nav: false
---

**Module 1 of 10.** &nbsp; [← schedule]({{ '/workshops/ml-ai-bootcamp/en/schedule/' | relative_url }}) &nbsp;|&nbsp; [next week →]({{ '/workshops/ml-ai-bootcamp/en/schedule/' | relative_url }})

> Take the Python you already half-know and make it precise enough to ship.

This first week is partly a calibration and partly a hard reset on tooling. Almost every participant arrives with *some* Python --- a few Coursera notebooks, a couple of Kaggle attempts, a research project's script. Almost every participant also arrives with at least one bad habit that will block them in week 5 if we don't fix it now. The week's labs are aggressive about exposing those habits: messy notebooks, hidden state, untyped functions, missing tests, broken environments.

By Friday, every participant ships a clean, reproducible Python project published on their personal GitHub. That artifact becomes the foundation that every later module builds on.

---

## What you ship this week

| | |
|---|---|
| **Deliverable** | A public GitHub repository containing the cleaned-up version of Lab 1 (the 300-line refactor) with a `README.md`, a `pyproject.toml`, a working `pytest` suite, and CI passing on a single push. |
| **Due** | Friday end of week 1, 18:00 Africa/Lagos. |
| **Submission** | Drop the repo URL into the `#cohort-week-01` channel. Peer review pairing is announced Monday of week 2. |
| **Rubric** | The deliverable is pass / revise. Pass requires green CI, tests covering the public API, and a README a stranger can follow to install and run the code. |

---

## Live sessions

| Day | Time | Topic | Link | Recording |
|---|---|---|:---:|:---:|
| Monday | 17:00 | **Kickoff and cohort introductions** | _(filled in at intake)_ | _(pending)_ |
| Tuesday | 17:00 | **Idiomatic Python: comprehensions, generators, decorators** | _(pending)_ | _(pending)_ |
| Wednesday | 17:00 | **NumPy and vectorization, with worked examples on real data** | _(pending)_ | _(pending)_ |
| Thursday | 17:00 | **Pandas in depth: joins, group-by, reshape, the index** | _(pending)_ | _(pending)_ |
| Friday | 17:00 | **Reproducible projects: virtualenv, pyproject, lockfile, pre-commit** | _(pending)_ | _(pending)_ |

Total live time this week: about 7.5 hours (five 90-minute sessions). Office hours add another 90 minutes on Wednesday.

---

## Learning outcomes

By the end of the week, every participant will be able to:

1. **Write idiomatic Python.** Use comprehensions, generators, context managers, and decorators where they pay off and not where they don't. Recognize and refactor non-idiomatic patterns.
2. **Use NumPy and Pandas fluently for vectorized data work.** Without falling back to Python-level loops on arrays of more than a few hundred elements.
3. **Build a reproducible Python project.** Virtual environment, pinned dependencies, `pyproject.toml`, pre-commit hooks, a working `pytest` suite, a CI pipeline that runs on each push.
4. **Read and write Jupyter notebooks without losing reproducibility.** Hidden-state hygiene, output management, conversion to scripts, version control of notebooks.

---

## Readings and prep

**Before Tuesday.** [Hitchhiker's Guide to Python](https://docs.python-guide.org/) chapters on \"Writing great Python code\" (idioms, structuring projects, vendorization). Skim, not deep-read --- we'll work through the same material in the live session.

**Before Wednesday.** Wes McKinney, *Python for Data Analysis* (3rd ed., O'Reilly 2022), chapters 4 (NumPy basics) and 5 (Getting started with Pandas). Available open-access at [wesmckinney.com/book](https://wesmckinney.com/book/).

**Before Thursday.** Same book, chapters 8 and 10 (data wrangling, group-by mechanics).

**Optional deepening.** Luciano Ramalho, *Fluent Python* (2nd ed., O'Reilly 2022) for any participant who already knows Pandas well and wants the language-level deep dive. Especially chapters 17 (concurrency basics), 18 (with/async), 24 (class metaprogramming).

---

## Lab notebooks

### Lab 1 — The 300-line refactor

A deliberately ugly Python script (`messy_data_pipeline.py`) is provided. It loads three CSV files, joins them, computes a handful of metrics, writes outputs to disk. The script works. It is also unreadable, untested, full of hidden state, and indeed has two bugs that don't fire on the example data.

**Your task.** Refactor it into a clean Python package with:

- `src/<your_project>/` module layout
- One pure function per responsibility, typed with `mypy --strict`
- A `pytest` suite that catches both latent bugs
- A `pyproject.toml` that pins all dependencies
- A `README.md` with install + run instructions a stranger can follow
- A passing GitHub Actions workflow (Python 3.11, lint + type-check + test)

**Dataset.** The lab dataset is the public [Kenya Health Facilities Registry](https://kmhfr.health.go.ke/) export from December 2024 (~12,000 facilities). The notebook in the lab repo has the download link.

**Notebook.** [`week-01-lab-01-refactor.ipynb`](https://github.com/AI-Technipreneurs) (link finalized at intake).

### Lab 2 — Pandas wrangling on a real dataset

Starting from raw [Kenya health facility data](https://kmhfr.health.go.ke/), produce a clean analytical DataFrame answering three real questions: (1) what fraction of facilities by county are public vs private? (2) where are the underserved areas (population per facility), and (3) does the picture change if you weight by facility capacity rather than headcount? Hand in a notebook and a short writeup.

**Notebook.** [`week-01-lab-02-pandas.ipynb`](https://github.com/AI-Technipreneurs).

### Lab 3 — Publish your project

Take the refactored Lab 1 package and publish it to a public GitHub repository under your own account, with a release tag, a versioned `pyproject.toml`, and a CI badge in the README. Add it to your bootcamp profile.

This is the artifact you reference every subsequent week --- and the one that recruiters end up looking at first.

---

## Office hours

| When | TA | Topic |
|---|---|---|
| Wednesday 19:00 (Africa/Lagos) | _(announced at intake)_ | Open: bring your refactor, your environment problems, anything blocked. |

Async questions go in the `#cohort-week-01-questions` channel; expected response time is under 24 hours during the week.

---

## Builds on / connects to

This week pulls from two existing course-catalogue volumes:

- [Programmation Scientifique]({{ '/courses/programmation-scientifiques/' | relative_url }}) --- the Python-as-scientific-language perspective.
- [Introduction to Data Science]({{ '/courses/intro-data-science/' | relative_url }}) --- chapters 1-2 of the bilingual notes.

The bootcamp condenses the relevant chapters into the week's reading list rather than re-deriving the material.
