"""
Chapter 10: Capstone Project — Titanic Survival
================================================
Data Pre-processing with Python — AIRINA Labs

This script demonstrates a complete end-to-end preprocessing
project using the Titanic dataset (Project 2 from the chapter).
It integrates all techniques from Chapters 1-9.
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# STEP 1: Load and inspect
# ============================================================

print("=" * 60)
print("CAPSTONE: Titanic Survival — End-to-End Preprocessing")
print("=" * 60)

url = ("https://raw.githubusercontent.com/datasciencedojo/"
       "datasets/master/titanic.csv")
df = pd.read_csv(url)

print(f"Shape: {df.shape}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nMissing values:\n{df.isnull().sum()}")
print(f"\nSurvival rate: {df['Survived'].mean():.2%}")

# ============================================================
# STEP 2: Data quality report (Chapter 1)
# ============================================================

print("\n" + "=" * 60)
print("STEP 2: Data Quality Report")
print("=" * 60)

def data_quality_report(df):
    report = pd.DataFrame({
        "dtype": df.dtypes,
        "null_pct": (df.isnull().mean() * 100).round(1),
        "n_unique": df.nunique(),
    })
    return report.sort_values("null_pct", ascending=False)

print(data_quality_report(df))

# ============================================================
# STEP 3: Investigate missing data mechanism (Chapter 3)
# ============================================================

print("\n" + "=" * 60)
print("STEP 3: Missing Data Analysis")
print("=" * 60)

# Is Age MCAR? Compare missingness across groups
df["age_missing"] = df["Age"].isnull().astype(int)

print("Age missingness by Pclass:")
print(df.groupby("Pclass")["age_missing"].mean().round(3))
print("\nAge missingness by Sex:")
print(df.groupby("Sex")["age_missing"].mean().round(3))
print("\nAge missingness by Survived:")
print(df.groupby("Survived")["age_missing"].mean().round(3))

print("\nConclusion: Age missingness varies by Pclass -> likely MAR, not MCAR")

# ============================================================
# STEP 4: Feature engineering (Chapters 6 & 7)
# ============================================================

print("\n" + "=" * 60)
print("STEP 4: Feature Engineering")
print("=" * 60)

# Extract title from name
df["Title"] = df["Name"].str.extract(r',\s*([^\.]+)\.', expand=False)
title_map = {
    "Mr": "Mr", "Miss": "Miss", "Mrs": "Mrs", "Master": "Master",
    "Dr": "Rare", "Rev": "Rare", "Col": "Rare", "Major": "Rare",
    "Mlle": "Miss", "Ms": "Miss", "Mme": "Mrs",
}
df["Title"] = df["Title"].map(title_map).fillna("Rare")

# Family features
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)
df["FarePerPerson"] = df["Fare"] / df["FamilySize"]

# Cabin features
df["HasCabin"] = df["Cabin"].notnull().astype(int)
df["CabinDeck"] = df["Cabin"].str[0].fillna("U")

# Name length
df["NameLength"] = df["Name"].str.len()

# Log fare
df["LogFare"] = np.log1p(df["Fare"])

new_features = ["Title", "FamilySize", "IsAlone", "FarePerPerson",
                "HasCabin", "CabinDeck", "NameLength", "LogFare"]
print(f"New features created: {new_features}")
print(df[new_features].head())

# ============================================================
# STEP 5: Build sklearn Pipeline (Chapter 9)
# ============================================================

print("\n" + "=" * 60)
print("STEP 5: Build Pipeline")
print("=" * 60)

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer, KNNImputer

num_features = ["Age", "Fare", "FamilySize", "FarePerPerson",
                "NameLength", "LogFare", "SibSp", "Parch"]
cat_features = ["Sex", "Embarked", "Title", "CabinDeck"]
binary_features = ["IsAlone", "HasCabin"]

num_transformer = Pipeline([
    ("imputer", KNNImputer(n_neighbors=5)),
    ("scaler", StandardScaler()),
])

cat_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore",
                               sparse_output=False, drop="first")),
])

binary_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
])

preprocessor = ColumnTransformer([
    ("num", num_transformer, num_features),
    ("cat", cat_transformer, cat_features),
    ("bin", binary_transformer, binary_features),
])

print("Preprocessor built:")
print(f"  Numerical features:  {num_features}")
print(f"  Categorical features: {cat_features}")
print(f"  Binary features:     {binary_features}")

# ============================================================
# STEP 6: Train and evaluate (Chapter 9)
# ============================================================

print("\n" + "=" * 60)
print("STEP 6: Train and Evaluate")
print("=" * 60)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import classification_report

X = df[num_features + cat_features + binary_features]
y = df["Survived"]

# Compare multiple models
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42),
    "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
}

for name, model in models.items():
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("classifier", model),
    ])
    scores = cross_val_score(pipeline, X, y, cv=5, scoring="accuracy")
    print(f"{name}: {scores.mean():.4f} +/- {scores.std():.4f}")

# Best model: detailed evaluation
best_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(n_estimators=100, random_state=42)),
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

best_pipeline.fit(X_train, y_train)
y_pred = best_pipeline.predict(X_test)

print(f"\nDetailed Report (RandomForest):")
print(classification_report(y_test, y_pred,
                            target_names=["Died", "Survived"]))

# ============================================================
# STEP 7: Feature importance
# ============================================================

print("=" * 60)
print("STEP 7: Feature Importance")
print("=" * 60)

# Get feature names after transformation
feature_names = (
    num_features +
    best_pipeline.named_steps["preprocessor"]
    .named_transformers_["cat"]
    .named_steps["encoder"]
    .get_feature_names_out(cat_features).tolist() +
    binary_features
)

importances = best_pipeline.named_steps["classifier"].feature_importances_
importance_df = (pd.DataFrame({"feature": feature_names,
                               "importance": importances})
                 .sort_values("importance", ascending=False))

print("Top 10 features:")
for _, row in importance_df.head(10).iterrows():
    bar = "#" * int(row["importance"] * 100)
    print(f"  {row['feature']:<25} {row['importance']:.4f} {bar}")

# ============================================================
# STEP 8: Save pipeline
# ============================================================

print("\n" + "=" * 60)
print("STEP 8: Save Pipeline")
print("=" * 60)

import joblib

joblib.dump(best_pipeline, "titanic_pipeline.joblib")
print("Pipeline saved to titanic_pipeline.joblib")

# Verify loading
loaded = joblib.load("titanic_pipeline.joblib")
verify_pred = loaded.predict(X_test)
assert (verify_pred == y_pred).all(), "Loaded pipeline gives different results!"
print("Pipeline verified: loaded model produces identical predictions.")

# Clean up
import os
os.remove("titanic_pipeline.joblib")

# ============================================================
# STEP 9: Deliverables checklist
# ============================================================

print("\n" + "=" * 60)
print("DELIVERABLES CHECKLIST")
print("=" * 60)

deliverables = {
    "Data quality report": True,
    "Missing data analysis (MCAR/MAR)": True,
    "Feature engineering (8 features)": True,
    "Pipeline built (ColumnTransformer)": True,
    "KNN imputation used": True,
    "Cross-validation (no leakage)": True,
    "Model comparison": True,
    "Feature importance analysis": True,
    "Pipeline saved with joblib": True,
}

for item, done in deliverables.items():
    status = "DONE" if done else "TODO"
    print(f"  [{status}] {item}")

print(f"\nFinal accuracy: {best_pipeline.score(X_test, y_test):.4f}")
print("\nDone! Capstone project completed successfully.")
