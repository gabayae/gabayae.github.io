"""
Chapter 11: Case Studies and Projects
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, r2_score, mean_squared_error)

# ============================================================
# PROJECT 1: Titanic Survival Prediction
# ============================================================
print("=" * 60)
print("PROJECT 1: TITANIC SURVIVAL PREDICTION")
print("=" * 60)

# 1. Load
titanic = sns.load_dataset('titanic')
print(f"Shape: {titanic.shape}")
print(f"\nMissing:\n{titanic.isnull().sum()}")

# 2. Clean
df = titanic[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']].copy()
df['age'] = df['age'].fillna(df['age'].median())
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])
df['sex'] = LabelEncoder().fit_transform(df['sex'])
df = pd.get_dummies(df, columns=['embarked'], dtype=int)
df['family_size'] = df['sibsp'] + df['parch'] + 1

print(f"\nCleaned shape: {df.shape}")
print(df.head())

# 3. Split
X = df.drop('survived', axis=1)
y = df['survived']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 4. Model
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# 5. Evaluate
print(f"\n=== Results ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(classification_report(y_test, y_pred, target_names=['Died', 'Survived']))

# Feature importance
feat_imp = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
print("Feature Importances:")
print(feat_imp.round(3))

# Cross-validation
cv_scores = cross_val_score(rf, X, y, cv=5, scoring='accuracy')
print(f"\n5-Fold CV: {cv_scores.mean():.3f} (+/- {cv_scores.std():.3f})")

# ============================================================
# PROJECT 2: California Housing Price Prediction
# ============================================================
print("\n" + "=" * 60)
print("PROJECT 2: CALIFORNIA HOUSING PRICE PREDICTION")
print("=" * 60)

from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing(as_frame=True)
df_h = housing.frame
print(f"Shape: {df_h.shape}")
print(df_h.describe().round(2))

# Features and target
X = df_h.drop('MedHouseVal', axis=1)
y = df_h['MedHouseVal']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.transform(X_test)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train_sc, y_train)
y_pred_lr = lr.predict(X_test_sc)
print(f"\n=== Linear Regression ===")
print(f"R²:   {r2_score(y_test, y_pred_lr):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_lr)):.4f}")

# Random Forest
rf_reg = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
rf_reg.fit(X_train_sc, y_train)
y_pred_rf = rf_reg.predict(X_test_sc)
print(f"\n=== Random Forest ===")
print(f"R²:   {r2_score(y_test, y_pred_rf):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_rf)):.4f}")

# Feature importance
feat_imp = pd.Series(rf_reg.feature_importances_, index=X.columns).sort_values(ascending=False)
print(f"\nFeature Importances:\n{feat_imp.round(3)}")

# Plot predictions vs actual
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].scatter(y_test, y_pred_lr, alpha=0.3, s=5)
axes[0].plot([0, 5], [0, 5], 'r--')
axes[0].set_xlabel('Actual')
axes[0].set_ylabel('Predicted')
axes[0].set_title('Linear Regression')

axes[1].scatter(y_test, y_pred_rf, alpha=0.3, s=5)
axes[1].plot([0, 5], [0, 5], 'r--')
axes[1].set_xlabel('Actual')
axes[1].set_ylabel('Predicted')
axes[1].set_title('Random Forest')

plt.tight_layout()
plt.savefig('ch11_predictions.pdf')
plt.show()
