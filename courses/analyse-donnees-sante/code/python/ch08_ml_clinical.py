"""
Chapter 8: Machine learning for clinical prediction
Data Analysis with Python for Health Specialists

Run in Jupyter notebook or Google Colab.
Datasets: UCI Heart Disease (Cleveland)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (classification_report, confusion_matrix,
                             roc_curve, roc_auc_score, RocCurveDisplay)

# ============================================================
# 1. Loading clinical data
# ============================================================

print("=== UCI Heart Disease dataset ===")
url = ("https://raw.githubusercontent.com/raphaelfontenelle/"
       "heart-disease-uci/main/heart.csv")
heart = pd.read_csv(url)
print(f"Shape: {heart.shape}")
print(f"Heart disease prevalence: {heart['target'].mean():.1%}")
print(heart.head())

# Column descriptions
column_info = {
    "age": "Age in years",
    "sex": "1 = male, 0 = female",
    "cp": "Chest pain type (0-3)",
    "trestbps": "Resting blood pressure (mmHg)",
    "chol": "Serum cholesterol (mg/dL)",
    "fbs": "Fasting blood sugar > 120 mg/dL (1 = true)",
    "restecg": "Resting ECG results (0-2)",
    "thalach": "Maximum heart rate achieved",
    "exang": "Exercise-induced angina (1 = yes)",
    "oldpeak": "ST depression induced by exercise",
    "slope": "Slope of peak exercise ST segment",
    "ca": "Number of major vessels colored by fluoroscopy (0-3)",
    "thal": "Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible)",
    "target": "Heart disease (1 = yes, 0 = no)"
}
print("\nColumn descriptions:")
for col, desc in column_info.items():
    print(f"  {col:12s} : {desc}")

# ============================================================
# 2. Train/test split
# ============================================================

print("\n=== Train/test split ===")
feature_cols = ["age", "sex", "cp", "trestbps", "chol", "fbs",
                "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
X = heart[feature_cols]
y = heart["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
print(f"Training set: {X_train.shape[0]} patients")
print(f"Test set:     {X_test.shape[0]} patients")
print(f"Training prevalence: {y_train.mean():.1%}")
print(f"Test prevalence:     {y_test.mean():.1%}")

# ============================================================
# 3. Cross-validation
# ============================================================

print("\n=== Cross-validation ===")
lr = LogisticRegression(max_iter=1000, random_state=42)
cv_scores = cross_val_score(lr, X, y, cv=5, scoring="accuracy")
print(f"CV accuracy: {cv_scores.mean():.3f} +/- {cv_scores.std():.3f}")
print(f"Per-fold: {cv_scores.round(3)}")

# ============================================================
# 4. Decision trees
# ============================================================

print("\n=== Decision tree ===")
dt = DecisionTreeClassifier(max_depth=4, random_state=42)
dt.fit(X_train, y_train)

y_pred_dt = dt.predict(X_test)
print("Decision Tree Results:")
print(classification_report(y_test, y_pred_dt,
                            target_names=["No Disease", "Disease"]))

# Visualize the tree
fig, ax = plt.subplots(figsize=(20, 10))
plot_tree(dt, feature_names=feature_cols,
          class_names=["No Disease", "Disease"],
          filled=True, rounded=True, fontsize=9, ax=ax)
plt.title("Decision tree for heart disease prediction")
plt.tight_layout()
plt.show()

# Overfit tree vs depth-limited tree
print("\n=== Overfitting demonstration ===")
dt_overfit = DecisionTreeClassifier(random_state=42)
dt_overfit.fit(X_train, y_train)

print(f"Training accuracy (overfit): {dt_overfit.score(X_train, y_train):.3f}")
print(f"Test accuracy (overfit):     {dt_overfit.score(X_test, y_test):.3f}")
print(f"Training accuracy (depth=4): {dt.score(X_train, y_train):.3f}")
print(f"Test accuracy (depth=4):     {dt.score(X_test, y_test):.3f}")

# ============================================================
# 5. Random forests
# ============================================================

print("\n=== Random forest ===")
rf = RandomForestClassifier(n_estimators=200, max_depth=6,
                            random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)

y_pred_rf = rf.predict(X_test)
print("Random Forest Results:")
print(classification_report(y_test, y_pred_rf,
                            target_names=["No Disease", "Disease"]))

# Cross-validation comparison
print("\n=== Model comparison (5-fold CV) ===")
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Decision Tree (depth=4)": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=200, max_depth=6,
                                            random_state=42, n_jobs=-1)
}

print("5-fold CV accuracy:")
for name, model in models.items():
    scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
    print(f"  {name:30s}: {scores.mean():.3f} +/- {scores.std():.3f}")

# ============================================================
# 6. ROC curves and AUC
# ============================================================

print("\n=== ROC curves ===")
lr.fit(X_train, y_train)
y_prob_lr = lr.predict_proba(X_test)[:, 1]
y_prob_rf = rf.predict_proba(X_test)[:, 1]

fpr_lr, tpr_lr, _ = roc_curve(y_test, y_prob_lr)
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)
auc_lr = roc_auc_score(y_test, y_prob_lr)
auc_rf = roc_auc_score(y_test, y_prob_rf)

fig, ax = plt.subplots(figsize=(7, 6))
ax.plot(fpr_lr, tpr_lr, label=f"Logistic Regression (AUC = {auc_lr:.3f})",
        linewidth=2)
ax.plot(fpr_rf, tpr_rf, label=f"Random Forest (AUC = {auc_rf:.3f})",
        linewidth=2)
ax.plot([0, 1], [0, 1], "k--", alpha=0.5, label="Random (AUC = 0.500)")
ax.set_xlabel("False Positive Rate (1 - Specificity)")
ax.set_ylabel("True Positive Rate (Sensitivity)")
ax.set_title("ROC curves: Heart disease prediction")
ax.legend(loc="lower right")
plt.tight_layout()
plt.show()

print(f"AUC (Logistic Regression): {auc_lr:.3f}")
print(f"AUC (Random Forest):       {auc_rf:.3f}")

# ============================================================
# 7. Feature importance
# ============================================================

print("\n=== Feature importance ===")
importances = rf.feature_importances_
importance_df = pd.DataFrame({
    "Feature": feature_cols,
    "Importance": importances
}).sort_values("Importance", ascending=True)

fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(importance_df["Feature"], importance_df["Importance"], color="steelblue")
ax.set_xlabel("Feature importance (Gini)")
ax.set_title("Which risk factors predict heart disease?")
plt.tight_layout()
plt.show()

print("Top 5 most important features:")
for _, row in importance_df.tail(5).iloc[::-1].iterrows():
    print(f"  {row['Feature']:12s}: {row['Importance']:.3f}")

# ============================================================
# 8. Calibration
# ============================================================

from sklearn.calibration import calibration_curve

print("\n=== Calibration ===")
prob_true, prob_pred = calibration_curve(y_test, y_prob_rf, n_bins=8)

fig, ax = plt.subplots(figsize=(6, 6))
ax.plot(prob_pred, prob_true, "o-", linewidth=2, label="Random Forest")
ax.plot([0, 1], [0, 1], "k--", label="Perfectly calibrated")
ax.set_xlabel("Mean predicted probability")
ax.set_ylabel("Observed proportion")
ax.set_title("Calibration plot")
ax.legend()
plt.tight_layout()
plt.show()

from sklearn.metrics import brier_score_loss

brier_lr = brier_score_loss(y_test, y_prob_lr)
brier_rf = brier_score_loss(y_test, y_prob_rf)
print(f"Brier score (Logistic Regression): {brier_lr:.4f}")
print(f"Brier score (Random Forest):       {brier_rf:.4f}")

# ============================================================
# 9. Overfitting: learning curve
# ============================================================

print("\n=== Learning curve ===")
train_sizes = [30, 50, 100, 150, 200, len(X_train)]
results = []

for size in train_sizes:
    if size > len(X_train):
        continue
    X_sub = X_train.iloc[:size]
    y_sub = y_train.iloc[:size]

    rf_temp = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_temp.fit(X_sub, y_sub)

    train_acc = rf_temp.score(X_sub, y_sub)
    test_acc = rf_temp.score(X_test, y_test)
    results.append({"n_train": size, "train_acc": train_acc, "test_acc": test_acc})

results_df = pd.DataFrame(results)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(results_df["n_train"], results_df["train_acc"], "o-",
        label="Training accuracy", linewidth=2)
ax.plot(results_df["n_train"], results_df["test_acc"], "s-",
        label="Test accuracy", linewidth=2)
ax.set_xlabel("Number of training patients")
ax.set_ylabel("Accuracy")
ax.set_title("Learning curve: more data reduces overfitting")
ax.legend()
ax.set_ylim(0.5, 1.05)
plt.tight_layout()
plt.show()

# ============================================================
# 10. Complete pipeline
# ============================================================

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

print("\n=== Full pipeline ===")
pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(n_estimators=200, max_depth=6,
                                          random_state=42))
])

cv_scores = cross_val_score(pipeline, X, y, cv=5, scoring="roc_auc")
print(f"Pipeline CV AUC: {cv_scores.mean():.3f} +/- {cv_scores.std():.3f}")

pipeline.fit(X_train, y_train)
y_prob_final = pipeline.predict_proba(X_test)[:, 1]
y_pred_final = pipeline.predict(X_test)

print(f"\nFinal test AUC: {roc_auc_score(y_test, y_prob_final):.3f}")
print(f"\n{classification_report(y_test, y_pred_final, target_names=['No Disease', 'Disease'])}")

# ============================================================
# 11. Fairness audit: performance by sex
# ============================================================

print("=== Fairness audit ===")
for sex_val, sex_label in [(1, "Male"), (0, "Female")]:
    mask = X_test["sex"] == sex_val
    if mask.sum() < 10:
        print(f"{sex_label}: too few samples ({mask.sum()})")
        continue

    auc_sub = roc_auc_score(y_test[mask], y_prob_final[mask])
    sens = (y_pred_final[mask] == 1)[y_test[mask] == 1].mean()
    spec = (y_pred_final[mask] == 0)[y_test[mask] == 0].mean()

    print(f"{sex_label:8s}: AUC = {auc_sub:.3f}, "
          f"Sensitivity = {sens:.3f}, Specificity = {spec:.3f}, "
          f"n = {mask.sum()}")
