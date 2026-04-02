# Module 4: Descriptive statistics and epidemiological measures

**Duration:** 3 hours (1h theory + 1h live coding + 1h exercises)
**Prerequisites:** Modules 2-3 (Pandas, data cleaning). Ability to load, clean, and group DataFrames.

---

## Learning objectives

By the end of this module, students will be able to:
1. Compute and interpret measures of central tendency (mean, median, mode) and choose the appropriate one for health data
2. Compute measures of spread (SD, IQR, coefficient of variation) and explain their clinical relevance
3. Build frequency tables and cross-tabulations for epidemiological reporting
4. Calculate prevalence, incidence rate, and mortality rate with confidence intervals
5. Compute and interpret risk ratios and odds ratios from 2x2 tables
6. Perform direct age standardization to compare mortality rates across populations

---

## Session structure

### Hour 1 — Theory (slides)
- Central tendency: mean vs. median for skewed health data
- Spread: SD, IQR, coefficient of variation
- Frequency tables and cross-tabulations (the "Table 1" of clinical papers)
- Prevalence vs. incidence: burden vs. risk
- Mortality rate and case fatality rate
- Measures of association: risk ratio and odds ratio with 2x2 tables
- Age-standardized rates: why crude rates mislead

### Hour 2 — Live coding demo
- Compute mean, median, SD, IQR for fasting glucose data
- Show how one outlier distorts the mean but not the median
- Build a frequency table for life expectancy categories by continent
- Compute diabetes prevalence with 95% confidence interval
- Calculate TB incidence rate from person-years at risk
- Compute risk ratio for smoking and lung cancer (with CI)
- Compute odds ratio for a case-control study
- Perform direct age standardization comparing two regions

### Hour 3 — Exercises
- Exercise 1: Compute summary statistics by continent for Gapminder 2007 data
- Exercise 2: Build a 2x2 table and compute OR with 95% CI
- Exercise 3: Compute age-standardized mortality rates for two populations
- Mini-project: Epidemiological profile of a disease using real WHO data

---

## Reading list

- [Python Data Science Handbook, Ch. 3 — Aggregation and Grouping](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [CDC Principles of Epidemiology, Lesson 3 — Measures of Risk](https://www.cdc.gov/csels/dsepd/ss1978/lesson3/index.html)
- [WHO Global Health Observatory — Data and statistics](https://www.who.int/data/gho)

---

## Datasets used

- **Gapminder** (life expectancy, GDP, population): `https://raw.githubusercontent.com/datasets/gapminder/main/data/gapminder.csv`
- Manually created clinical data for prevalence, incidence, and association computations

---

## Mini-project: Epidemiological profile report

Build a Jupyter notebook that:
1. Loads the Gapminder dataset for 2007
2. Computes summary statistics (mean, median, SD, IQR) for life expectancy, GDP per capita, and population by continent
3. Creates a cross-tabulation of continent vs. life expectancy category with row percentages
4. Computes cumulative incidence and incidence rate from a provided cohort scenario (10,000 people, 450 cases, 4.5 avg person-years)
5. Computes an odds ratio with 95% CI from a case-control study (200 cases, 200 controls)
6. Writes a reusable `prevalence_ci(cases, total)` function and tests it
7. Performs age standardization comparing two regions

**Deliverable:** A single .ipynb notebook with all computations, interpretations in markdown cells, and at least one summary table.
