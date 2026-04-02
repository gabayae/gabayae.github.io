"""
Chapter 6: Feature Engineering
==============================
Data Pre-processing with Python — AIRINA Labs

This script demonstrates:
- Polynomial and interaction features
- Mathematical transformations (ratios, logs)
- Date/time feature extraction
- Aggregation features
- Text-derived features
- Domain knowledge features
- Feature selection with mutual information
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# 1. Load dataset
# ============================================================

print("=" * 60)
print("FEATURE ENGINEERING — Titanic")
print("=" * 60)

url = ("https://raw.githubusercontent.com/datasciencedojo/"
       "datasets/master/titanic.csv")
df = pd.read_csv(url)
print(f"Original shape: {df.shape}")
print(f"Original columns: {df.columns.tolist()}")

# ============================================================
# 2. Polynomial features
# ============================================================

print("\n" + "=" * 60)
print("POLYNOMIAL FEATURES")
print("=" * 60)

from sklearn.preprocessing import PolynomialFeatures

features = df[["Age", "Fare"]].dropna()
poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(features)
poly_names = poly.get_feature_names_out(["Age", "Fare"])

print(f"Original: {features.shape[1]} features")
print(f"Polynomial (degree 2): {len(poly_names)} features")
print(f"Names: {poly_names}")

# ============================================================
# 3. Ratio and mathematical features
# ============================================================

print("\n" + "=" * 60)
print("RATIO FEATURES")
print("=" * 60)

df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)
df["FarePerPerson"] = df["Fare"] / df["FamilySize"]
df["Fare_log"] = np.log1p(df["Fare"])

print(df[["Fare", "FamilySize", "FarePerPerson",
          "Fare_log", "IsAlone"]].head(10))

# Survival rate by family size
print(f"\nSurvival rate by FamilySize:")
print(df.groupby("FamilySize")["Survived"].mean().round(3))

# ============================================================
# 4. Text-derived features from Name
# ============================================================

print("\n" + "=" * 60)
print("TEXT-DERIVED FEATURES — Name")
print("=" * 60)

# Extract title from name
df["Title"] = df["Name"].str.extract(r',\s*([^\.]+)\.', expand=False)
print(f"Titles found:\n{df['Title'].value_counts()}")

# Consolidate rare titles
title_map = {
    "Mr": "Mr", "Miss": "Miss", "Mrs": "Mrs", "Master": "Master",
    "Dr": "Rare", "Rev": "Rare", "Col": "Rare", "Major": "Rare",
    "Mlle": "Miss", "Ms": "Miss", "Mme": "Mrs", "Don": "Rare",
    "Dona": "Rare", "Lady": "Rare", "the Countess": "Rare",
    "Sir": "Rare", "Capt": "Rare", "Jonkheer": "Rare",
}
df["Title_clean"] = df["Title"].map(title_map).fillna("Rare")

print(f"\nCleaned titles:\n{df['Title_clean'].value_counts()}")
print(f"\nSurvival by title:")
print(df.groupby("Title_clean")["Survived"].mean().sort_values(ascending=False))

# Name length
df["NameLength"] = df["Name"].str.len()

# ============================================================
# 5. Cabin-derived features
# ============================================================

print("\n" + "=" * 60)
print("CABIN FEATURES")
print("=" * 60)

df["HasCabin"] = df["Cabin"].notnull().astype(int)
df["CabinDeck"] = df["Cabin"].str[0].fillna("Unknown")

print(f"Has cabin: {df['HasCabin'].sum()} / {len(df)}")
print(f"\nSurvival by cabin deck:")
print(df.groupby("CabinDeck")["Survived"].mean().sort_values(ascending=False))

# ============================================================
# 6. Aggregation features
# ============================================================

print("\n" + "=" * 60)
print("AGGREGATION FEATURES")
print("=" * 60)

# Average fare by Pclass
class_stats = df.groupby("Pclass")["Fare"].agg(
    class_mean_fare="mean",
    class_median_fare="median",
).reset_index()
df = df.merge(class_stats, on="Pclass", how="left")

# How does this passenger's fare compare to class average?
df["FareVsClass"] = df["Fare"] / df["class_mean_fare"]

print(df[["Pclass", "Fare", "class_mean_fare",
          "FareVsClass"]].head(10))

# ============================================================
# 7. Interaction features
# ============================================================

print("\n" + "=" * 60)
print("INTERACTION FEATURES")
print("=" * 60)

df["Sex_Pclass"] = df["Sex"] + "_" + df["Pclass"].astype(str)
print(f"Survival by Sex x Pclass:")
print(df.groupby("Sex_Pclass")["Survived"].mean()
        .sort_values(ascending=False))

# Numerical interaction
df["Age_x_Pclass"] = df["Age"] * df["Pclass"]
df["Fare_x_IsAlone"] = df["Fare"] * df["IsAlone"]

# ============================================================
# 8. Feature selection with mutual information
# ============================================================

print("\n" + "=" * 60)
print("FEATURE SELECTION — Mutual Information")
print("=" * 60)

from sklearn.feature_selection import mutual_info_classif

feature_cols = ["Age", "Fare", "FamilySize", "IsAlone",
                "FarePerPerson", "HasCabin", "NameLength",
                "Fare_log", "FareVsClass", "Age_x_Pclass"]

subset = df[feature_cols + ["Survived"]].dropna()
X = subset[feature_cols]
y = subset["Survived"]

mi = mutual_info_classif(X, y, random_state=42)
mi_series = pd.Series(mi, index=feature_cols).sort_values(ascending=False)

print("Mutual information with Survived:")
for feat, score in mi_series.items():
    bar = "#" * int(score * 50)
    print(f"  {feat:<20} {score:.4f} {bar}")

# ============================================================
# 9. Summary of all engineered features
# ============================================================

print("\n" + "=" * 60)
print("FEATURE ENGINEERING SUMMARY")
print("=" * 60)

original_cols = ["PassengerId", "Survived", "Pclass", "Name", "Sex",
                 "Age", "SibSp", "Parch", "Ticket", "Fare",
                 "Cabin", "Embarked"]
new_cols = [c for c in df.columns if c not in original_cols]
print(f"Original columns: {len(original_cols)}")
print(f"New engineered columns: {len(new_cols)}")
print(f"New columns: {new_cols}")

print("\nDone! Chapter 6 script completed successfully.")
