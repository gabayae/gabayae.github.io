---
layout: workshop
permalink: /workshops/r-statistical-analysis/en/
lang: en
title: "R for Statistical Analysis"
tagline: "The Tidyverse, ggplot2, statistical modelling and reproducible reports — a practical companion to The Shape of Data."
description: "4-day workshop: Tidyverse, ggplot2, statistical modelling, R Markdown."

# --- Sidebar metadata ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "4 days (≈ 24 hours)"
level: "Beginner to Intermediate"
format: "On-site, live online, or hybrid"
languages: "English &amp; French"
certificate: "Certificate of completion"

# --- Materials links shown in the sidebar ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/r-statistical-analysis

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Workshop inquiry — R for Statistical Analysis"
---

## Program Overview

This workshop provides a comprehensive introduction to R for data analysis and statistical modelling. Participants learn the Tidyverse ecosystem, create publication-quality visualizations with ggplot2, and build reproducible reports with R Markdown. The workshop serves as a practical companion to *The Shape of Data* (No Starch Press).

### Software requirements

- R 4.3+ ([CRAN](https://cran.r-project.org/))
- RStudio Desktop ([posit.co](https://posit.co/download/rstudio-desktop/))
- Packages: tidyverse, rmarkdown, knitr, broom, palmerpenguins

### Day 1 — R fundamentals & RStudio

**Objectives:** set up the environment, learn R syntax, understand data types and structures.

- **Setup & RStudio tour** — installing R & RStudio, console, scripts, projects, environment pane, help system.
- **R basics** — variables, vectors, types (numeric, character, logical, factor), indexing, vectorized operations.
- **Data structures** — matrices, lists, data frames, tibbles. Creating, subsetting, modifying.
- **Control flow & functions** — if/else, for loops, apply family, writing custom functions, pipes (`|>` and `%>%`).

**Lab 1:** load the built-in `iris` dataset, compute summary statistics per species, and write a function that classifies a flower based on petal measurements.

### Day 2 — Data wrangling with the Tidyverse

**Objectives:** master data manipulation with dplyr and tidyr.

- **Reading data** — read_csv, read_excel, read_delim, readr options, handling encodings and messy files.
- **dplyr core verbs** — filter(), select(), mutate(), arrange(), summarise(), group_by(), across().
- **tidyr & reshaping** — pivot_longer(), pivot_wider(), separate(), unite(), handling NAs (drop_na, replace_na).
- **Joining & combining** — left_join, inner_join, anti_join, bind_rows, bind_cols. Relational data patterns.

**Lab 2:** work with a multi-file dataset (e.g., WHO health statistics for African countries): read multiple CSVs, join them, reshape from wide to long, clean missing values, and produce a tidy analysis-ready dataset.

### Day 3 — Visualization with ggplot2

**Objectives:** build a complete visualization toolkit using the grammar of graphics.

- **Grammar of graphics** — aesthetics, geoms, scales, coordinate systems, the layered approach.
- **Core geoms** — geom_point, geom_line, geom_bar, geom_histogram, geom_boxplot, geom_violin, geom_density.
- **Customization** — themes (theme_minimal, theme_classic, custom themes), color palettes (viridis, brewer), labels, annotations, legends.
- **Advanced techniques** — faceting (facet_wrap, facet_grid), stat layers, coordinate transformations, combining plots (patchwork), saving with ggsave.

**Lab 3:** create a visual report with 6+ publication-quality figures exploring the health dataset. Include: distribution plots, trend lines, faceted comparisons, and a correlation heatmap.

### Day 4 — Statistical modelling & reproducible reports

**Objectives:** perform common statistical analyses and produce reproducible reports.

- **Descriptive & inferential statistics** — summary statistics, t-tests, chi-squared tests, confidence intervals, p-values and their interpretation.
- **Linear models** — lm(), interpreting coefficients, R², residual diagnostics, multiple regression, ANOVA with aov().
- **Model diagnostics & beyond** — residual plots, Q-Q plots, influence measures, logistic regression with glm(), broom for tidy model output.
- **R Markdown** — YAML header, code chunks, inline code, tables (kable), figure options, output formats (HTML, PDF, Word).
- **Capstone & wrap-up** — mini-project presentations, resources, Q&A, certificates.

**Lab 4 (capstone):** produce a complete reproducible R Markdown report: load data, perform EDA with ggplot2, fit a linear model, diagnose it, and present findings with narrative, tables, and figures. Topics:
- Health outcome modelling (life expectancy ~ GDP, education, etc.).
- Agricultural yield analysis.
- Financial indicator analysis.

### Assessment

- **Daily labs** (50 %) — completion and quality of exercises.
- **Capstone report** (30 %) — R Markdown document produced on Day 4.
- **Participation** (20 %) — engagement and homework.

### Resources

- [R for Data Science (2e)](https://r4ds.hadley.nz/) — Hadley Wickham & Garrett Grolemund
- [ggplot2 Book](https://ggplot2-book.org/)
- [The Shape of Data](https://nostarch.com/shapeofdata) — companion book with R implementations
- [RStudio Cheat Sheets](https://posit.co/resources/cheatsheets/)
- [CRAN Task Views](https://cran.r-project.org/web/views/)

## Learning Outcomes

By the end of this workshop, participants will be able to:

1. Navigate RStudio and write clean, readable R code.
2. Wrangle data efficiently with dplyr and tidyr.
3. Create compelling statistical visualizations with ggplot2.
4. Perform common statistical analyses (t-tests, ANOVA, regression).
5. Produce reproducible reports with R Markdown.

## Who Should Attend

Graduate students, researchers, and analysts in social science, public health, economics, biology, agriculture, or any domain whose work involves statistical analysis on real datasets and where reproducibility matters. The workshop is also a good fit for academics who use SAS, SPSS, or Stata and want to migrate to an open-source workflow without losing rigour.

**Prerequisites:**

- Basic statistics (mean, variance, hypothesis testing concepts).
- No prior R experience required.
- Laptop with internet access.

## Brochure

Lecture notes and lab notebooks are linked in the sidebar.

For a printable one-page brochure suitable for forwarding to a program committee, conference organizer, or corporate L&D team, write to <a href="mailto:gabayae2@gmail.com?subject=Brochure%20request%20%E2%80%94%20R%20for%20Statistical%20Analysis">gabayae2@gmail.com</a> with the audience size and intended delivery dates.
