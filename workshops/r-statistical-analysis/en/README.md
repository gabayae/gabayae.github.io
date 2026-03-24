# R for Statistical Analysis — 4-Day Workshop

**Instructor:** Dr. Yaé Ulrich Gaba
**Duration:** 4 days (24 hours)
**Level:** Beginner to Intermediate
**Language:** English

---

## Overview

This workshop provides a comprehensive introduction to R for data analysis and statistical modelling. Participants learn the Tidyverse ecosystem, create publication-quality visualizations with ggplot2, and build reproducible reports with R Markdown. The workshop serves as a practical companion to *The Shape of Data* (No Starch Press).

## Prerequisites

- Basic statistics (mean, variance, hypothesis testing concepts)
- No prior R experience required
- Laptop with internet access

## Learning Objectives

By the end of this workshop, participants will be able to:

1. Navigate RStudio and write clean, readable R code
2. Wrangle data efficiently with dplyr and tidyr
3. Create compelling statistical visualizations with ggplot2
4. Perform common statistical analyses (t-tests, ANOVA, regression)
5. Produce reproducible reports with R Markdown

## Software Requirements

- R 4.3+ ([CRAN](https://cran.r-project.org/))
- RStudio Desktop ([posit.co](https://posit.co/download/rstudio-desktop/))
- Packages: tidyverse, rmarkdown, knitr, broom, palmerpenguins

---

## Day-by-Day Program

### Day 1: R Fundamentals & RStudio

**Objectives:** Set up the environment, learn R syntax, understand data types and structures.

| Time | Topic |
|------|-------|
| 09:00–10:30 | **Setup & RStudio Tour** — Installing R & RStudio, console, scripts, projects, environment pane, help system |
| 10:30–10:45 | *Break* |
| 10:45–12:30 | **R Basics** — Variables, vectors, types (numeric, character, logical, factor), indexing, vectorized operations |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **Data Structures** — Matrices, lists, data frames, tibbles. Creating, subsetting, modifying |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Control Flow & Functions** — if/else, for loops, apply family, writing custom functions, pipes (`|>` and `%>%`) |

**Lab 1:** Load the built-in `iris` dataset, compute summary statistics per species, and write a function that classifies a flower based on petal measurements.

**Homework:** Explore the `mtcars` dataset — compute grouped statistics and answer 3 questions about the data.

---

### Day 2: Data Wrangling with the Tidyverse

**Objectives:** Master data manipulation with dplyr and tidyr.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Reading Data** — read_csv, read_excel, read_delim, readr options, handling encodings and messy files |
| 10:30–10:45 | *Break* |
| 10:45–12:30 | **dplyr Core Verbs** — filter(), select(), mutate(), arrange(), summarise(), group_by(), across() |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **tidyr & Reshaping** — pivot_longer(), pivot_wider(), separate(), unite(), handling NAs (drop_na, replace_na) |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Joining & Combining** — left_join, inner_join, anti_join, bind_rows, bind_cols. Relational data patterns |

**Lab 2:** Work with a multi-file dataset (e.g., WHO health statistics for African countries): read multiple CSVs, join them, reshape from wide to long, clean missing values, and produce a tidy analysis-ready dataset.

**Homework:** Using the cleaned dataset, compute 5 summary tables using dplyr pipelines.

---

### Day 3: Visualization with ggplot2

**Objectives:** Build a complete visualization toolkit using the grammar of graphics.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Grammar of Graphics** — Aesthetics, geoms, scales, coordinate systems, the layered approach |
| 10:30–10:45 | *Break* |
| 10:45–12:30 | **Core Geoms** — geom_point, geom_line, geom_bar, geom_histogram, geom_boxplot, geom_violin, geom_density |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **Customization** — Themes (theme_minimal, theme_classic, custom themes), color palettes (viridis, brewer), labels, annotations, legends |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Advanced Techniques** — Faceting (facet_wrap, facet_grid), stat layers, coordinate transformations, combining plots (patchwork), saving with ggsave |

**Lab 3:** Create a visual report with 6+ publication-quality figures exploring the health dataset. Include: distribution plots, trend lines, faceted comparisons, and a correlation heatmap.

**Homework:** Reproduce a figure from a published paper (provided) using ggplot2.

---

### Day 4: Statistical Modelling & Reproducible Reports

**Objectives:** Perform common statistical analyses and produce reproducible reports.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Descriptive & Inferential Statistics** — Summary statistics, t-tests, chi-squared tests, confidence intervals, p-values and their interpretation |
| 10:30–10:45 | *Break* |
| 10:45–12:30 | **Linear Models** — lm(), interpreting coefficients, R², residual diagnostics, multiple regression, ANOVA with aov() |
| 12:30–14:00 | *Lunch* |
| 14:00–15:00 | **Model Diagnostics & Beyond** — Residual plots, Q-Q plots, influence measures, logistic regression with glm(), broom for tidy model output |
| 15:00–15:15 | *Break* |
| 15:15–16:15 | **R Markdown** — YAML header, code chunks, inline code, tables (kable), figure options, output formats (HTML, PDF, Word) |
| 16:15–17:00 | **Capstone & Wrap-Up** — Mini-project presentations, resources, Q&A, certificates |

**Lab 4 (Capstone):** Produce a complete reproducible R Markdown report: load data, perform EDA with ggplot2, fit a linear model, diagnose it, and present findings with narrative, tables, and figures. Topics:
- Health outcome modelling (life expectancy ~ GDP, education, etc.)
- Agricultural yield analysis
- Financial indicator analysis

---

## Assessment

- **Daily labs** (50%) — Completion and quality of exercises
- **Capstone report** (30%) — R Markdown document produced on Day 4
- **Participation** (20%) — Engagement and homework

## Resources

- [R for Data Science (2e)](https://r4ds.hadley.nz/) — Hadley Wickham & Garrett Grolemund
- [ggplot2 Book](https://ggplot2-book.org/)
- [The Shape of Data](https://nostarch.com/shapeofdata) — Companion book with R implementations
- [RStudio Cheat Sheets](https://posit.co/resources/cheatsheets/)
- [CRAN Task Views](https://cran.r-project.org/web/views/)

## Certificate

Participants who complete all labs and the capstone report receive a certificate of completion.
