"""
Chapter 8: Machine Learning Models
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import (accuracy_score, r2_score,
                             mean_squared_error, classification_report)
from sklearn.preprocessing import StandardScaler

# === Linear Regression: Tips ===
tips = sns.load_dataset('tips')
X_reg = tips[['total_bill', 'size']].values
y_reg = tips['tip'].values

X_tr, X_te, y_tr, y_te = train_test_split(X_reg, y_reg, test_size=0.3, random_state=42)
lr = LinearRegression()
lr.fit(X_tr, y_tr)
y_pred_reg = lr.predict(X_te)

print("=== Linear Regression (Tips) ===")
print(f"Coefficients: {lr.coef_.round(4)}")
print(f"Intercept: {lr.intercept_:.4f}")
print(f"R² (train): {lr.score(X_tr, y_tr):.4f}")
print(f"R² (test):  {lr.score(X_te, y_te):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_te, y_pred_reg)):.4f}")

# === Logistic Regression: Iris (binary) ===
iris = load_iris(as_frame=True)
mask = iris.target != 2
X_log = iris.data[mask]
y_log = iris.target[mask]

X_tr, X_te, y_tr, y_te = train_test_split(X_log, y_log, test_size=0.3, random_state=42)
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_tr, y_tr)
print(f"\n=== Logistic Regression (Iris binary) ===")
print(f"Accuracy: {log_reg.score(X_te, y_te):.3f}")

# === Decision Tree: Iris (multiclass) ===
X_iris = iris.data
y_iris = iris.target
X_tr, X_te, y_tr, y_te = train_test_split(X_iris, y_iris, test_size=0.3, random_state=42)

dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(X_tr, y_tr)
print(f"\n=== Decision Tree (depth=3) ===")
print(f"Train accuracy: {dt.score(X_tr, y_tr):.3f}")
print(f"Test accuracy:  {dt.score(X_te, y_te):.3f}")

# === Random Forest ===
rf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
rf.fit(X_tr, y_tr)
print(f"\n=== Random Forest (100 trees) ===")
print(f"Train accuracy: {rf.score(X_tr, y_tr):.3f}")
print(f"Test accuracy:  {rf.score(X_te, y_te):.3f}")
print(f"Feature importances: {dict(zip(iris.feature_names, rf.feature_importances_.round(3)))}")

# === K-Means Clustering ===
X_km = iris.data.values[:, [2, 3]]  # petal length, petal width
inertias = []
K_range = range(1, 11)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_km)
    inertias.append(km.inertia_)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(K_range, inertias, 'bo-')
axes[0].set_xlabel('k')
axes[0].set_ylabel('Inertia')
axes[0].set_title('Elbow Method')

km3 = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = km3.fit_predict(X_km)
axes[1].scatter(X_km[:, 0], X_km[:, 1], c=labels, cmap='viridis', alpha=0.6)
axes[1].scatter(km3.cluster_centers_[:, 0], km3.cluster_centers_[:, 1],
               c='red', marker='X', s=200, edgecolors='black')
axes[1].set_xlabel('Petal Length')
axes[1].set_ylabel('Petal Width')
axes[1].set_title('K-Means (k=3)')
plt.tight_layout()
plt.savefig('ch08_kmeans.pdf')
plt.show()

print(f"\n=== K-Means (k=3) ===")
print(f"Cluster sizes: {np.bincount(labels)}")
print(f"Inertia: {km3.inertia_:.2f}")
