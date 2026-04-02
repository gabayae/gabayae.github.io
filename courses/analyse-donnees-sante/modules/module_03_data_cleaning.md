# Module 3: Data cleaning in health contexts

**Duration:** 3 hours (1h theory + 1h live coding + 1h exercises)
**Prerequisites:** Module 2 (Health data with Pandas). Ability to load, filter, and group DataFrames.

---

## Learning objectives

By the end of this module, students will be able to:
1. Distinguish the three missing-data mechanisms (MCAR, MAR, MNAR) and their clinical implications
2. Detect and visualize missing values using pandas and the `missingno` library
3. Apply appropriate imputation strategies (mean, median, mode, KNN) depending on context
4. Identify and remove duplicate patient records while distinguishing true duplicates from repeated visits
5. Standardize inconsistent data: ICD codes, date formats, units, and text fields
6. Build and run a data validation pipeline with range checks and cross-field rules

---

## Session structure

### Hour 1 — Theory (slides)
- Why data cleaning matters in health (wrong units, duplicate IDs, ambiguous dates)
- Missing data mechanisms: MCAR, MAR, MNAR with clinical examples
- Imputation strategies: drop, mean/median, mode, group-specific, KNN
- Duplicates in health data: true duplicates vs. repeated measures
- Inconsistent data: ICD codes, date formats, unit conversions, text standardization
- Data validation: range checks, cross-field rules, automated quality reports

### Hour 2 — Live coding demo
- Create a messy clinical dataset with deliberate errors
- Detect missing values with `.isnull().sum()` and `missingno` plots
- Impute continuous variables (median) and categorical variables (mode)
- Remove exact duplicates and keep first visit per patient
- Standardize ICD codes, date formats, and glucose units
- Run range checks and cross-field validation
- Generate before/after data quality reports

### Hour 3 — Exercises
- Exercise 1: Generate a data quality report for a messy clinical dataset
- Exercise 2: Fix sex column standardization and validate age/BP ranges
- Exercise 3: Convert mixed glucose units (mg/dL and mmol/L) and HbA1c (IFCC to NGSP)
- Mini-project: Complete cleaning pipeline on a messy dataset

---

## Reading list

- [Pandas User Guide — Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [missingno library documentation](https://github.com/ResidentMario/missingno)
- [Sterne et al. (2009) "Multiple imputation for missing data in epidemiological studies"](https://doi.org/10.1136/bmj.b2393) (BMJ, free access)

---

## Datasets used

- Manually created messy clinical dataset with deliberate errors (missing values, duplicates, mixed units, inconsistent ICD codes, ambiguous dates)
- **Gapminder** for the complete cleaning pipeline demo

---

## Mini-project: Cleaning a messy clinical dataset

Build a Jupyter notebook that takes a deliberately messy clinical dataset (provided in the exercise) and applies a complete cleaning pipeline:
1. Generate an initial data quality report (missing counts, data types, ranges)
2. Remove exact duplicate rows
3. Standardize the `sex` column to "M"/"F"
4. Set impossible `age` values (-3, 200) to NaN
5. Set impossible `systolic_bp` (450) to NaN and validate diastolic < systolic
6. Convert glucose values in mmol/L to mg/dL (values < 30 are likely mmol/L)
7. Convert HbA1c value of 55 from mmol/mol (IFCC) to % (NGSP)
8. Standardize all dates to ISO format and all ICD codes to uppercase with dot separator
9. Impute remaining missing values (median for continuous, mode for categorical)
10. Generate a final data quality report and compare with the initial one
11. Save the cleaned dataset to CSV

**Deliverable:** A single .ipynb notebook with before/after quality reports and all cleaning steps documented.
