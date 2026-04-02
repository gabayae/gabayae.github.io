"""
Chapter 3: Missing Data
=======================
Data Pre-processing with Python — AIRINA Labs

This script demonstrates:
- Missing data detection and reporting
- Visualization with missingno
- Simple imputation (mean, median, mode)
- Advanced imputation (KNN, iterative/MICE)
- Missing indicators
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# 1. Load data and detect missing values
# ============================================================

print("=" * 60)
print("MISSING DATA DETECTION")
print("=" * 60)

url = ("https://raw.githubusercontent.com/datasciencedojo/"
       "datasets/master/titanic.csv")
df = pd.read_csv(url)

print(f"Shape: {df.shape}")
print(f"\nMissing values per column:")
print(df.isnull().sum())
print(f"\nTotal missing cells: {df.isnull().sum().sum()}")
print(f"Overall missing rate: {df.isnull().mean().mean()*100:.1f}%")

# ============================================================
# 2. Missing data report
# ============================================================

def missing_report(df):
    """Return a DataFrame summarizing missing data."""
    missing = df.isnull().sum()
    pct = (missing / len(df) * 100).round(1)
    report = pd.DataFrame({"missing": missing, "pct": pct})
    return report[report["missing"] > 0].sort_values("pct", ascending=False)

print("\n" + "=" * 60)
print("MISSING DATA REPORT")
print("=" * 60)
print(missing_report(df))

# ============================================================
# 3. Hidden missing values (Adult Census)
# ============================================================

print("\n" + "=" * 60)
print("HIDDEN MISSING VALUES — Adult Census")
print("=" * 60)

adult_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
             "adult/adult.data")
adult_cols = ["age", "workclass", "fnlwgt", "education", "education_num",
              "marital_status", "occupation", "relationship", "race",
              "sex", "capital_gain", "capital_loss", "hours_per_week",
              "native_country", "income"]

df_adult = pd.read_csv(adult_url, header=None, names=adult_cols,
                        na_values=[" ?"], skipinitialspace=True)
print(f"Adult Census shape: {df_adult.shape}")
print(f"\nMissing values (after replacing ' ?'):")
print(missing_report(df_adult))

# ============================================================
# 4. Visualization with missingno
# ============================================================

print("\n" + "=" * 60)
print("MISSING DATA VISUALIZATION")
print("=" * 60)

try:
    import missingno as msno
    import matplotlib
    matplotlib.use("Agg")  # Non-interactive backend
    import matplotlib.pyplot as plt

    # Matrix plot
    fig, ax = plt.subplots(figsize=(10, 5))
    msno.matrix(df, ax=ax, sparkline=False)
    plt.title("Missing data pattern — Titanic")
    plt.tight_layout()
    plt.savefig("missing_matrix.png", dpi=150)
    plt.close()
    print("Saved: missing_matrix.png")

    # Bar chart
    fig, ax = plt.subplots(figsize=(10, 4))
    msno.bar(df, ax=ax)
    plt.tight_layout()
    plt.savefig("missing_bar.png", dpi=150)
    plt.close()
    print("Saved: missing_bar.png")

except ImportError:
    print("missingno not installed. Run: pip install missingno")

# ============================================================
# 5. Simple imputation
# ============================================================

print("\n" + "=" * 60)
print("SIMPLE IMPUTATION")
print("=" * 60)

df_simple = df.copy()

# Median imputation for Age
from sklearn.impute import SimpleImputer

num_imputer = SimpleImputer(strategy="median")
df_simple["Age"] = num_imputer.fit_transform(df_simple[["Age"]])

# Mode imputation for Embarked
cat_imputer = SimpleImputer(strategy="most_frequent")
df_simple["Embarked"] = cat_imputer.fit_transform(
    df_simple[["Embarked"]]).ravel()

# Constant for Cabin
df_simple["Cabin"] = df_simple["Cabin"].fillna("Unknown")

print("After simple imputation:")
print(df_simple.isnull().sum())

# ============================================================
# 6. KNN imputation
# ============================================================

print("\n" + "=" * 60)
print("KNN IMPUTATION")
print("=" * 60)

from sklearn.impute import KNNImputer

df_knn = df.copy()
num_cols = ["Age", "Fare", "SibSp", "Parch"]

knn_imputer = KNNImputer(n_neighbors=5, weights="distance")
df_knn[num_cols] = knn_imputer.fit_transform(df_knn[num_cols])

print(f"Missing after KNN imputation: {df_knn[num_cols].isnull().sum().sum()}")
print(f"\nAge statistics after KNN imputation:")
print(df_knn["Age"].describe())

# ============================================================
# 7. Iterative imputation (MICE)
# ============================================================

print("\n" + "=" * 60)
print("ITERATIVE IMPUTATION (MICE)")
print("=" * 60)

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

df_mice = df.copy()
iter_imputer = IterativeImputer(max_iter=10, random_state=42)
df_mice[num_cols] = iter_imputer.fit_transform(df_mice[num_cols])

print(f"Missing after iterative imputation: "
      f"{df_mice[num_cols].isnull().sum().sum()}")
print(f"\nAge statistics after MICE:")
print(df_mice["Age"].describe())

# ============================================================
# 8. Compare imputation methods
# ============================================================

print("\n" + "=" * 60)
print("IMPUTATION COMPARISON — Age")
print("=" * 60)

comparison = pd.DataFrame({
    "Original": df["Age"].describe(),
    "Median": df_simple["Age"].describe(),
    "KNN": df_knn["Age"].describe(),
    "MICE": df_mice["Age"].describe(),
})
print(comparison.round(2))

# ============================================================
# 9. Missing indicators
# ============================================================

print("\n" + "=" * 60)
print("MISSING INDICATORS")
print("=" * 60)

df_ind = df.copy()
df_ind["Age_was_missing"] = df_ind["Age"].isnull().astype(int)
df_ind["Cabin_was_missing"] = df_ind["Cabin"].isnull().astype(int)

# Check if missingness correlates with survival
print("Survival rate by Age missingness:")
print(df_ind.groupby("Age_was_missing")["Survived"].mean())
print("\nSurvival rate by Cabin missingness:")
print(df_ind.groupby("Cabin_was_missing")["Survived"].mean())

# ============================================================
# 10. Smart imputation function
# ============================================================

def smart_impute(df, drop_threshold=0.7):
    """
    Smart imputation:
    1. Drop columns with > drop_threshold missing
    2. Add missing indicators
    3. Impute numerical with median
    4. Impute categorical with mode
    """
    df = df.copy()

    # Drop high-missing columns
    high_missing = df.columns[df.isnull().mean() > drop_threshold]
    print(f"Dropping columns (>{drop_threshold*100}% missing): "
          f"{high_missing.tolist()}")
    df = df.drop(columns=high_missing)

    # Add missing indicators
    for col in df.columns[df.isnull().any()]:
        df[f"{col}_missing"] = df[col].isnull().astype(int)

    # Impute numerical
    num_cols = df.select_dtypes(include="number").columns
    for col in num_cols:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].median())

    # Impute categorical
    cat_cols = df.select_dtypes(include="object").columns
    for col in cat_cols:
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].mode()[0])

    return df

df_smart = smart_impute(df)
print(f"\nAfter smart imputation:")
print(f"Shape: {df_smart.shape}")
print(f"Remaining missing: {df_smart.isnull().sum().sum()}")

print("\nDone! Chapter 3 script completed successfully.")
