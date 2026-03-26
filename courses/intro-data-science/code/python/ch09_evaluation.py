"""
Chapter 9: Model Evaluation
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import (train_test_split, cross_val_score,
                                     StratifiedKFold, GridSearchCV,
                                     learning_curve)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, classification_report, confusion_matrix,
                             ConfusionMatrixDisplay, roc_curve, auc)
from sklearn.preprocessing import label_binarize

# === Load data ===
titanic = sns.load_dataset('titanic').dropna(subset=['age'])
X = titanic[['pclass', 'age', 'sibsp', 'parch', 'fare']].values
y = titanic['survived'].values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

# === Logistic Regression ===
lr = LogisticRegression(max_iter=200, random_state=42)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

print("=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=['Died', 'Survived']))

# === Confusion Matrix ===
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

fig, ax = plt.subplots(figsize=(6, 5))
ConfusionMatrixDisplay(cm, display_labels=['Died', 'Survived']).plot(ax=ax)
plt.title('Confusion Matrix')
plt.savefig('ch09_confusion_matrix.pdf')
plt.show()

# === ROC Curve ===
y_prob = lr.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(fpr, tpr, 'b-', lw=2, label=f'ROC (AUC = {roc_auc:.3f})')
ax.plot([0, 1], [0, 1], 'r--', lw=1, label='Random')
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
ax.set_title('ROC Curve')
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('ch09_roc_curve.pdf')
plt.show()

print(f"\nAUC = {roc_auc:.4f}")

# === Cross-Validation ===
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(lr, X, y, cv=cv, scoring='accuracy')
print(f"\n=== 5-Fold Stratified CV ===")
print(f"Scores: {cv_scores.round(3)}")
print(f"Mean: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")

# === GridSearchCV ===
param_grid = {
    'n_neighbors': [3, 5, 7, 9, 11],
    'weights': ['uniform', 'distance']
}
grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)
print(f"\n=== GridSearchCV (KNN) ===")
print(f"Best params: {grid.best_params_}")
print(f"Best CV score: {grid.best_score_:.3f}")
print(f"Test score: {grid.score(X_test, y_test):.3f}")

# === Learning Curve ===
train_sizes, train_scores, val_scores = learning_curve(
    lr, X, y, cv=5, train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='accuracy')

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(train_sizes, train_scores.mean(axis=1), 'bo-', label='Train')
ax.plot(train_sizes, val_scores.mean(axis=1), 'rs-', label='Validation')
ax.fill_between(train_sizes,
                train_scores.mean(axis=1) - train_scores.std(axis=1),
                train_scores.mean(axis=1) + train_scores.std(axis=1), alpha=0.1)
ax.fill_between(train_sizes,
                val_scores.mean(axis=1) - val_scores.std(axis=1),
                val_scores.mean(axis=1) + val_scores.std(axis=1), alpha=0.1)
ax.set_xlabel('Training Set Size')
ax.set_ylabel('Accuracy')
ax.set_title('Learning Curve')
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('ch09_learning_curve.pdf')
plt.show()
