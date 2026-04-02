# Module 7: Regression for health outcomes

**Duration:** 3 hours (1h theory + 1h live coding + 1h exercises)
**Prerequisites:** Modules 2-6 (Pandas, cleaning, descriptive statistics, visualization, hypothesis testing).

---

## Learning objectives

By the end of this module, students will be able to:
1. Fit and interpret a simple linear regression relating a health outcome to one predictor
2. Fit a multiple linear regression adjusting for confounders and interpret "after controlling for"
3. Identify and demonstrate confounding with an adjusted vs. unadjusted analysis
4. Check regression assumptions using residual diagnostic plots
5. Fit a logistic regression for binary health outcomes and interpret odds ratios
6. Evaluate classification performance using the confusion matrix (sensitivity, specificity, PPV, NPV)

---

## Session structure

### Hour 1 — Theory (slides)
- From correlation to prediction: what regression does
- Simple linear regression: slope, intercept, R-squared
- Multiple linear regression: adjusting for confounders
- Confounders: coffee, smoking, and heart disease example
- Checking assumptions: residuals vs. fitted, Q-Q plot, homoscedasticity
- Logistic regression: binary outcomes, log-odds, odds ratios
- Model evaluation: confusion matrix, sensitivity, specificity, PPV, NPV
- Introduction to survival analysis: Kaplan-Meier and Cox proportional hazards

### Hour 2 — Live coding demo
- Simple linear regression: systolic BP vs. age (scipy `linregress`)
- Visualize with scatter plot + regression line
- Multiple regression with statsmodels: SBP ~ age + BMI + smoking
- Interpret coefficients in clinical context
- Confounding demo: unadjusted vs. adjusted coffee-heart disease model
- Residual diagnostic plots (3 panels)
- Logistic regression on Pima diabetes data (statsmodels + sklearn)
- Odds ratios with 95% CI
- Confusion matrix and clinical metrics
- Kaplan-Meier curves and Cox model for treatment vs. control

### Hour 3 — Exercises
- Exercise 1: Simple logistic regression predicting diabetes from glucose alone
- Exercise 2: Multiple logistic regression with age, BMI, glucose, BP, pedigree function
- Exercise 3: Compare model sensitivity/specificity at different thresholds (0.3, 0.5, 0.7)
- Mini-project: Diabetes risk prediction notebook

---

## Reading list

- [statsmodels OLS regression tutorial](https://www.statsmodels.org/stable/regression.html)
- [scikit-learn Logistic Regression documentation](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [lifelines documentation — Cox Proportional Hazards](https://lifelines.readthedocs.io/en/latest/Survival%20Regression.html)

---

## Datasets used

- Simulated clinical data (age, BMI, smoking, systolic BP)
- **Pima Indians Diabetes Dataset**: `https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv`
- Simulated survival data (treatment vs. control)

---

## Mini-project: Diabetes risk prediction

Build a Jupyter notebook that:
1. Loads the Pima Indians Diabetes dataset and replaces biologically impossible zeros with NaN
2. Fits a simple logistic regression (diabetes ~ glucose) and reports the odds ratio
3. Fits a multiple logistic regression (diabetes ~ age + BMI + glucose + BP + pedigree) and reports odds ratios with 95% CIs
4. Splits data 70/30 and compares both models on the test set (sensitivity, specificity, accuracy)
5. Tests confounding: fits glucose-only model, then adds age, and checks if the glucose coefficient changes
6. Tries classification thresholds of 0.3, 0.5, and 0.7 and discusses the sensitivity/specificity tradeoff
7. Visualizes the confusion matrix for the best model

**Deliverable:** A single .ipynb notebook with regression outputs, confusion matrices, and clinical interpretation in markdown cells.
