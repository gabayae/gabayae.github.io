"""
Chapter 7: Introduction to Machine Learning
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# === Load data ===
iris = load_iris(as_frame=True)
X = iris.data
y = iris.target
print(f"Features: {X.shape}, Target: {y.shape}")

# === Train/test split ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")

# === KNN with different k ===
print("\n=== KNN: varying k ===")
k_values = [1, 3, 5, 7, 9, 11, 15]
train_scores = []
test_scores = []
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    tr_acc = knn.score(X_train, y_train)
    te_acc = knn.score(X_test, y_test)
    train_scores.append(tr_acc)
    test_scores.append(te_acc)
    print(f"  k={k:2d}: train={tr_acc:.3f}, test={te_acc:.3f}")

# Plot bias-variance
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(k_values, train_scores, 'bo-', label='Train')
ax.plot(k_values, test_scores, 'rs-', label='Test')
ax.set_xlabel('k (number of neighbors)')
ax.set_ylabel('Accuracy')
ax.set_title('Bias-Variance Tradeoff (KNN)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('ch07_bias_variance.pdf')
plt.show()

# === Cross-validation ===
knn5 = KNeighborsClassifier(n_neighbors=5)
cv_scores = cross_val_score(knn5, X, y, cv=5, scoring='accuracy')
print(f"\n=== 5-Fold Cross-Validation ===")
print(f"Scores: {cv_scores.round(3)}")
print(f"Mean: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")
