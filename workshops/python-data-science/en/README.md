---
layout: workshop
permalink: /workshops/python-data-science/en/
lang: en
title: "Python for Data Science"
tagline: "From zero Python to your first machine-learning models — daily coding labs on real datasets."
description: "5-day workshop: Pandas, visualization, ML with scikit-learn."

# --- Sidebar metadata ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "5 days (≈ 30 hours)"
level: "Beginner to Intermediate"
format: "On-site, live online, or hybrid"
languages: "English &amp; French"
certificate: "Certificate of completion"

# --- Materials links shown in the sidebar ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/python-data-science

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Workshop inquiry — Python for Data Science"
---

<p class="workshop-stack-label">Core stack covered</p>

<div class="row row-cols-5 row-cols-md-5 g-2 mb-4 text-center workshop-stack">
  <div class="col"><a href="https://www.python.org/" target="_blank" rel="noopener" class="toolkit-item"><img src="{{ '/assets/img/toolkit/python.svg' | relative_url }}" alt="Python" loading="lazy" width="36" height="36"><div class="toolkit-label">Python</div></a></div>
  <div class="col"><a href="https://jupyter.org/" target="_blank" rel="noopener" class="toolkit-item"><img src="{{ '/assets/img/toolkit/jupyter.svg' | relative_url }}" alt="Jupyter" loading="lazy" width="36" height="36"><div class="toolkit-label">Jupyter</div></a></div>
  <div class="col"><a href="https://numpy.org/" target="_blank" rel="noopener" class="toolkit-item"><img src="{{ '/assets/img/toolkit/numpy.svg' | relative_url }}" alt="NumPy" loading="lazy" width="36" height="36"><div class="toolkit-label">NumPy</div></a></div>
  <div class="col"><a href="https://pandas.pydata.org/" target="_blank" rel="noopener" class="toolkit-item"><img src="{{ '/assets/img/toolkit/pandas.svg' | relative_url }}" alt="pandas" loading="lazy" width="36" height="36"><div class="toolkit-label">pandas</div></a></div>
  <div class="col"><a href="https://scikit-learn.org/" target="_blank" rel="noopener" class="toolkit-item"><img src="{{ '/assets/img/toolkit/scikitlearn.svg' | relative_url }}" alt="scikit-learn" loading="lazy" width="36" height="36"><div class="toolkit-label">scikit-learn</div></a></div>
</div>

<style>
.workshop-stack-label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--global-text-color-light); margin-top: 0; margin-bottom: 0.5rem; font-weight: 600; }
.workshop-stack .toolkit-item { display: block; padding: 0.3rem; color: inherit; text-decoration: none; transition: transform 0.15s ease; }
.workshop-stack .toolkit-item:hover { transform: translateY(-2px); text-decoration: none; }
.workshop-stack img { max-width: 36px; height: auto; }
.workshop-stack .toolkit-label { font-size: 0.72rem; margin-top: 0.3rem; color: var(--global-text-color); font-weight: 500; }
</style>

## Program Overview

This hands-on workshop takes participants from zero Python experience to building their first machine learning models. Through daily coding labs, real-world datasets, and progressive projects, learners develop practical data science skills grounded in solid programming fundamentals.

### Software requirements

- Python 3.10+
- Jupyter Notebook / JupyterLab
- Libraries: NumPy, Pandas, Matplotlib, Seaborn, scikit-learn
- Recommended setup: [Anaconda Distribution](https://www.anaconda.com/download) (includes everything).

### Day 1 — Python fundamentals

**Objectives:** install Python, understand core syntax, write first programs.

- **Setup & first steps** — installing Anaconda, launching Jupyter, cells & execution, Markdown basics.
- **Core syntax** — variables, types (int, float, str, bool), operators, string formatting, input/output.
- **Control flow** — conditionals (if/elif/else), loops (for, while), range(), list comprehensions.
- **Functions & modules** — defining functions, parameters, return values, importing modules, `math`, `random`.

**Lab 1:** write a program that analyzes student grades — compute mean, median, min/max, and assign letter grades.

### Day 2 — Data structures & NumPy

**Objectives:** master Python collections and numerical computing with NumPy.

- **Data structures** — lists, tuples, dictionaries, sets, nesting, common methods.
- **File I/O & error handling** — reading/writing CSV and text files, try/except, with statements.
- **NumPy fundamentals** — arrays, shapes, dtypes, indexing, slicing, broadcasting.
- **NumPy operations** — vectorized operations, aggregations, linear algebra basics, random number generation.

**Lab 2:** load a CSV file of weather data manually, then redo it with NumPy. Compare performance and code readability.

### Day 3 — Pandas & data wrangling

**Objectives:** load, clean, transform, and explore datasets with Pandas.

- **Pandas basics** — Series, DataFrame, read_csv, head/tail/info/describe, dtypes.
- **Selection & filtering** — loc/iloc, boolean indexing, query(), column operations, sorting.
- **Data cleaning** — missing values (isna, fillna, dropna), duplicates, type conversion, string methods.
- **Aggregation & grouping** — groupby, agg, pivot_table, merge/join, concat.

**Lab 3:** clean and analyze a messy real-world dataset (e.g., World Bank development indicators for African countries). Handle missing values, merge multiple files, and produce summary statistics by country/year.

### Day 4 — Data visualization

**Objectives:** create publication-quality plots and perform exploratory data analysis.

- **Matplotlib fundamentals** — figure/axes model, plot(), scatter(), bar(), hist(), customization.
- **Seaborn for statistical visualization** — distplot, boxplot, heatmap, pairplot, catplot, styling.
- **Exploratory data analysis (EDA)** — systematic approach: distributions, correlations, outliers, patterns. EDA workflow checklist.
- **Advanced plots & storytelling** — subplots, annotations, color palettes, saving figures, dashboard-style layouts.

**Lab 4:** perform a complete EDA on the cleaned dataset from Day 3. Answer 5 analytical questions with appropriate visualizations. Create a mini-report with narrative and figures.

### Day 5 — Introduction to machine learning

**Objectives:** build, evaluate, and interpret first ML models with scikit-learn.

- **ML concepts** — supervised vs. unsupervised learning, train/test split, overfitting, bias-variance tradeoff.
- **Classification** — logistic regression, decision trees, random forests. scikit-learn API: fit/predict/score.
- **Regression & evaluation** — linear regression, metrics (MSE, R², accuracy, precision, recall, F1), cross-validation.
- **Unsupervised learning** — K-Means clustering, PCA for dimensionality reduction, visualization of clusters.
- **Wrap-up & next steps** — recap, resources for continued learning, Q&A, certificates.

**Lab 5 (capstone):** end-to-end mini-project: load a dataset, clean it, explore it, build a predictive model, evaluate it, and present results. Participants choose from:
- Predicting crop yields from climate data.
- Customer churn classification.
- Housing price regression.

### Assessment

- **Daily labs** (50 %) — completion and quality of hands-on exercises.
- **Capstone project** (30 %) — end-to-end analysis on Day 5.
- **Participation** (20 %) — engagement in discussions and homework.

### Resources

- [Python Documentation](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [The Shape of Data](https://nostarch.com/shapeofdata) — geometry-based ML and data analysis.

## Learning Outcomes

By the end of this workshop, participants will be able to:

1. Write Python scripts and use Jupyter notebooks for data analysis.
2. Manipulate and clean datasets using Pandas.
3. Create informative visualizations with Matplotlib and Seaborn.
4. Perform exploratory data analysis (EDA) on real-world datasets.
5. Build, evaluate, and interpret basic ML models with scikit-learn.

## Who Should Attend

Researchers, analysts, and graduate students in any field who handle data and want a working data-science toolkit. Career-changers preparing for a first analyst or data role. Domain specialists (economics, biology, public health, education) who want to read and write their own analysis code rather than depend on others. The pace assumes no prior programming experience, so a complete beginner can keep up while a competent Excel user accelerates quickly.

**Prerequisites:**

- Basic computer literacy (file management, web browsing).
- High school mathematics (algebra, basic statistics).
- No prior programming experience required.
- Laptop with internet access (Python will be installed on Day 1).

## Brochure

Lecture notes and lab notebooks are linked in the sidebar.

For a printable one-page brochure suitable for forwarding to a program committee, conference organizer, or corporate L&D team, write to <a href="mailto:gabayae2@gmail.com?subject=Brochure%20request%20%E2%80%94%20Python%20for%20Data%20Science">gabayae2@gmail.com</a> with the audience size and intended delivery dates.
