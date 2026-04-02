"""
Chapter 1: Data Landscape and Pipelines
========================================
Data Pre-processing with Python — AIRINA Labs

This script demonstrates:
- Loading and inspecting real datasets
- Data quality reports
- Variable type detection
- The preprocessing workflow overview
"""

import pandas as pd
import numpy as np

# ============================================================
# 1. Loading a real dataset
# ============================================================

# Titanic dataset (readily available online)
url = ("https://raw.githubusercontent.com/datasciencedojo/"
       "datasets/master/titanic.csv")
df = pd.read_csv(url)

print("=" * 60)
print("TITANIC DATASET — FIRST LOOK")
print("=" * 60)
print(f"Shape: {df.shape}")
print(f"\nColumn types:\n{df.dtypes}")
print(f"\nFirst 5 rows:\n{df.head()}")

# ============================================================
# 2. Data quality report
# ============================================================

def data_quality_report(df):
    """Generate a comprehensive quality report for any DataFrame."""
    report = pd.DataFrame({
        "dtype": df.dtypes,
        "non_null": df.notnull().sum(),
        "null_count": df.isnull().sum(),
        "null_pct": (df.isnull().sum() / len(df) * 100).round(1),
        "n_unique": df.nunique(),
        "sample_value": df.iloc[0],
    })
    return report.sort_values("null_pct", ascending=False)

print("\n" + "=" * 60)
print("DATA QUALITY REPORT")
print("=" * 60)
print(data_quality_report(df))

# ============================================================
# 3. Identifying variable types
# ============================================================

numerical = df.select_dtypes(include="number").columns.tolist()
categorical = df.select_dtypes(include="object").columns.tolist()

print(f"\nNumerical columns ({len(numerical)}): {numerical}")
print(f"Categorical columns ({len(categorical)}): {categorical}")

# ============================================================
# 4. Summary statistics
# ============================================================

print("\n" + "=" * 60)
print("SUMMARY STATISTICS — NUMERICAL")
print("=" * 60)
print(df.describe())

print("\n" + "=" * 60)
print("SUMMARY STATISTICS — CATEGORICAL")
print("=" * 60)
print(df.describe(include="object"))

# ============================================================
# 5. Missing values overview
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(1)
missing_report = pd.DataFrame({"count": missing, "pct": missing_pct})
print(missing_report[missing_report["count"] > 0].sort_values(
    "pct", ascending=False))

# ============================================================
# 6. Detecting mixed types
# ============================================================

def detect_mixed_types(df):
    """Check each column for mixed Python types."""
    mixed = []
    for col in df.columns:
        types = df[col].dropna().apply(type).unique()
        if len(types) > 1:
            mixed.append((col, [t.__name__ for t in types]))
    return mixed

mixed = detect_mixed_types(df)
if mixed:
    print(f"\nColumns with mixed types: {mixed}")
else:
    print("\nNo columns with mixed types detected.")

# ============================================================
# 7. Minimal preprocessing workflow
# ============================================================

print("\n" + "=" * 60)
print("MINIMAL PREPROCESSING WORKFLOW")
print("=" * 60)

# Step 1: Drop duplicates
n_before = len(df)
df = df.drop_duplicates()
print(f"Duplicates removed: {n_before - len(df)}")

# Step 2: Handle missing values (simple for demo)
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Step 3: Encode categorical
df["Sex_encoded"] = df["Sex"].map({"male": 0, "female": 1})

# Step 4: Validate
print(f"Remaining missing: {df.isnull().sum().sum()}")
print(f"Final shape: {df.shape}")

print("\nDone! Chapter 1 script completed successfully.")
