# Module 6: Hypothesis testing for health data

**Duration:** 3 hours (1h theory + 1h live coding + 1h exercises)
**Prerequisites:** Modules 2-5 (Pandas, cleaning, descriptive statistics, visualization).

---

## Learning objectives

By the end of this module, students will be able to:
1. Formulate null and alternative hypotheses for clinical research questions
2. Interpret p-values correctly and explain what they do NOT mean
3. Apply one-sample, two-sample, and paired t-tests to clinical data
4. Use the chi-square test for association between categorical variables
5. Apply Mann-Whitney U as a non-parametric alternative for skewed data
6. Correct for multiple testing (Bonferroni, FDR) and compute Cohen's d effect size

---

## Session structure

### Hour 1 — Theory (slides)
- Logic of hypothesis testing: H0, H1, test statistic, p-value, decision
- What a p-value IS and IS NOT
- Type I error (false positive) and Type II error (false negative)
- One-sample t-test: sample mean vs. reference value
- Two-sample t-test: comparing two groups (checking assumptions)
- Paired t-test: before/after intervention
- Chi-square test of independence for categorical data
- Mann-Whitney U: non-parametric alternative
- Multiple testing correction: Bonferroni and Benjamini-Hochberg FDR
- Effect size: Cohen's d and clinical vs. statistical significance

### Hour 2 — Live coding demo
- One-sample t-test: clinic cholesterol vs. national average (200 mg/dL)
- Two-sample t-test: BP in treatment vs. control groups
- Check assumptions: Shapiro-Wilk normality, Levene's equal variance
- Paired t-test: BP before/after exercise intervention with visualization
- Chi-square test: obesity category vs. diabetes status
- Mann-Whitney U: hospital length of stay (surgical vs. medical)
- Multiple testing simulation: 1000 tests under H0, Bonferroni and FDR correction
- Cohen's d: large sample + tiny effect = significant but meaningless

### Hour 3 — Exercises
- Exercise 1: One-sample t-test on Framingham cholesterol data
- Exercise 2: Two-sample t-test comparing systolic BP between CHD and non-CHD groups
- Exercise 3: Chi-square test of smoking vs. CHD risk
- Exercise 4: Multiple testing correction across all continuous variables
- Mini-project: Comprehensive hypothesis testing on Framingham data

---

## Reading list

- [SciPy stats documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [statsmodels multipletests](https://www.statsmodels.org/dev/generated/statsmodels.stats.multitest.multipletests.html)
- [Greenland et al. (2016) "Statistical tests, P values, confidence intervals, and power"](https://doi.org/10.1007/s10654-016-0149-3) (European Journal of Epidemiology, open access)

---

## Datasets used

- Simulated clinical trial data (treatment vs. control blood pressure)
- Simulated before/after intervention data
- **Framingham Heart Study dataset**: `https://raw.githubusercontent.com/dsrscientist/dataset-for-machine-learning/master/framingham.csv`

---

## Mini-project: Hypothesis testing on Framingham data

Build a Jupyter notebook that:
1. Loads the Framingham cardiovascular dataset and drops rows with missing values
2. Performs a one-sample t-test: is mean total cholesterol different from 200 mg/dL?
3. Performs a two-sample t-test: systolic BP in CHD vs. non-CHD groups, reports p-value, mean difference, and Cohen's d
4. Performs a chi-square test: is smoking associated with 10-year CHD risk?
5. Performs Mann-Whitney U: compares cigarettes per day between CHD and non-CHD
6. Runs t-tests on all continuous variables (age, totChol, sysBP, diaBP, BMI, heartRate, glucose) with Bonferroni and FDR correction
7. Identifies the variable with the largest effect size and discusses clinical meaningfulness

**Deliverable:** A single .ipynb notebook with test results, interpretations in markdown cells, and at least one visualization (e.g., before/after or group comparison).
