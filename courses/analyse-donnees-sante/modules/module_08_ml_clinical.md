# Module 8: Machine learning for clinical prediction

**Duration:** 3 hours (1h theory + 1h live coding + 1h exercises)
**Prerequisites:** Modules 2-7 (Pandas through regression). Understanding of logistic regression and model evaluation.

---

## Learning objectives

By the end of this module, students will be able to:
1. Explain when to use ML vs. traditional statistics (prediction vs. inference)
2. Implement a proper train/test split and 5-fold cross-validation
3. Train and evaluate decision trees, random forests, and logistic regression for clinical classification
4. Plot and interpret ROC curves and compare models using AUC
5. Extract and interpret feature importance from a random forest
6. Assess model calibration and detect overfitting using learning curves

---

## Session structure

### Hour 1 — Theory (slides)
- ML vs. traditional statistics: prediction vs. inference
- When NOT to use ML (small data, regulatory, simple rules work)
- Train/test split and why you must never evaluate on training data
- Cross-validation: rotating the test set for robust estimates
- Decision trees: interpretable flowcharts for clinical rules
- Random forests: ensemble of trees, majority vote
- ROC curves and AUC: comparing discriminative ability
- Feature importance: which risk factors drive predictions (not causation)
- Calibration: do predicted probabilities match reality?
- Overfitting: the danger of small clinical datasets
- Ethics: fairness in clinical prediction models

### Hour 2 — Live coding demo
- Load UCI Heart Disease dataset
- Train/test split (70/30, stratified)
- 5-fold cross-validation with logistic regression
- Fit a decision tree (max_depth=4), visualize it
- Demonstrate overfitting with an unlimited-depth tree
- Fit a random forest (200 trees)
- Compare all three models via cross-validation
- Plot ROC curves on a single figure
- Feature importance bar chart
- Calibration plot and Brier score
- Learning curve: accuracy vs. training set size
- Fairness audit: AUC by sex

### Hour 3 — Exercises
- Exercise 1: Fit all three models and compare CV accuracy and AUC
- Exercise 2: Visualize decision tree and discuss clinical interpretability
- Exercise 3: Train random forest with only top 5 features, compare performance
- Exercise 4: Plot sensitivity and specificity vs. threshold for the random forest
- Mini-project: Heart disease prediction pipeline

---

## Reading list

- [scikit-learn User Guide — Classification](https://scikit-learn.org/stable/supervised_learning.html)
- [Rajkomar et al. (2019) "Machine Learning in Medicine"](https://doi.org/10.1056/NEJMra1814259) (NEJM review)
- [Obermeyer et al. (2019) "Dissecting racial bias in an algorithm"](https://doi.org/10.1126/science.aax2342) (Science)

---

## Datasets used

- **UCI Heart Disease Dataset**: `https://raw.githubusercontent.com/raphaelfontenelle/heart-disease-uci/main/heart.csv` (303 patients, 13 features, binary target)

---

## Mini-project: Heart disease prediction pipeline

Build a Jupyter notebook that:
1. Loads the UCI Heart Disease dataset and explores it
2. Splits data 70/30 (stratified)
3. Trains 3 models: logistic regression, decision tree (depth=4), random forest (200 trees)
4. Reports 5-fold CV accuracy and AUC for each model
5. Plots ROC curves for all 3 models on one figure
6. Generates a feature importance bar chart from the random forest
7. Creates a calibration plot for the best model
8. Performs a fairness audit: compares AUC, sensitivity, and specificity between male and female patients
9. Writes a paragraph discussing which model to choose for screening vs. confirmation

**Deliverable:** A single .ipynb notebook with model comparison table, ROC figure, feature importance chart, and clinical interpretation.
