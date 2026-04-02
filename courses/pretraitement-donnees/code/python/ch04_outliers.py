"""
Chapter 4: Outlier Detection and Treatment
==========================================
Data Pre-processing with Python — AIRINA Labs

This script demonstrates:
- Visual outlier detection (box plots, scatter plots)
- Z-score and IQR methods
- Mahalanobis distance
- Isolation Forest
- Domain-specific rules
- Treatment strategies (removal, capping, log transform)
"""

import pandas as pd
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# 1. Load dataset
# ============================================================

print("=" * 60)
print("OUTLIER DETECTION — Titanic Dataset")
print("=" * 60)

url = ("https://raw.githubusercontent.com/datasciencedojo/"
       "datasets/master/titanic.csv")
df = pd.read_csv(url)

print(f"Shape: {df.shape}")
print(f"\nFare statistics:")
print(df["Fare"].describe())

# ============================================================
# 2. Z-score method
# ============================================================

print("\n" + "=" * 60)
print("Z-SCORE METHOD")
print("=" * 60)

def detect_zscore_outliers(series, threshold=3):
    """Detect outliers using z-score."""
    z = np.abs(stats.zscore(series.dropna()))
    return z > threshold

for col in ["Age", "Fare", "SibSp", "Parch"]:
    data = df[col].dropna()
    outliers = detect_zscore_outliers(data)
    print(f"{col}: {outliers.sum()} outliers "
          f"({outliers.sum()/len(data)*100:.1f}%)")

# ============================================================
# 3. IQR method
# ============================================================

print("\n" + "=" * 60)
print("IQR METHOD")
print("=" * 60)

def iqr_bounds(series):
    """Return lower and upper IQR bounds."""
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    return Q1 - 1.5 * IQR, Q3 + 1.5 * IQR

def iqr_outlier_report(df, columns):
    """Generate an IQR outlier report."""
    rows = []
    for col in columns:
        data = df[col].dropna()
        lo, hi = iqr_bounds(data)
        n_out = ((data < lo) | (data > hi)).sum()
        rows.append({
            "column": col,
            "lower_bound": round(lo, 2),
            "upper_bound": round(hi, 2),
            "n_outliers": n_out,
            "pct": round(n_out / len(data) * 100, 1),
        })
    return pd.DataFrame(rows)

num_cols = ["Age", "Fare", "SibSp", "Parch"]
report = iqr_outlier_report(df, num_cols)
print(report)

# ============================================================
# 4. Compare z-score vs IQR on skewed data
# ============================================================

print("\n" + "=" * 60)
print("Z-SCORE vs IQR — Fare (skewed)")
print("=" * 60)

fare = df["Fare"].dropna()
print(f"Fare skewness: {fare.skew():.2f}")

z_outliers = detect_zscore_outliers(fare).sum()
lo, hi = iqr_bounds(fare)
iqr_outliers = ((fare < lo) | (fare > hi)).sum()

print(f"Z-score outliers (|z| > 3): {z_outliers}")
print(f"IQR outliers: {iqr_outliers}")
print(f"IQR bounds: [{lo:.2f}, {hi:.2f}]")

# ============================================================
# 5. Multivariate: Mahalanobis distance
# ============================================================

print("\n" + "=" * 60)
print("MAHALANOBIS DISTANCE")
print("=" * 60)

from scipy.spatial.distance import mahalanobis
from numpy.linalg import inv

def mahalanobis_outliers(df, columns, threshold=3):
    """Detect multivariate outliers using Mahalanobis distance."""
    data = df[columns].dropna()
    mean = data.mean().values
    cov_matrix = data.cov().values
    cov_inv = inv(cov_matrix)

    distances = data.apply(
        lambda row: mahalanobis(row.values, mean, cov_inv), axis=1
    )
    return distances, distances > threshold

cols_mv = ["Age", "Fare"]
subset = df[cols_mv].dropna()
distances, mask = mahalanobis_outliers(df, cols_mv)
print(f"Multivariate outliers (Age, Fare): {mask.sum()} "
      f"({mask.sum()/len(mask)*100:.1f}%)")

# ============================================================
# 6. Isolation Forest
# ============================================================

print("\n" + "=" * 60)
print("ISOLATION FOREST")
print("=" * 60)

from sklearn.ensemble import IsolationForest

iso_data = df[["Age", "Fare"]].dropna()
iso = IsolationForest(contamination=0.05, random_state=42)
labels = iso.fit_predict(iso_data)

n_outliers = (labels == -1).sum()
print(f"Isolation Forest outliers: {n_outliers} "
      f"({n_outliers/len(iso_data)*100:.1f}%)")

# ============================================================
# 7. Domain-specific rules
# ============================================================

print("\n" + "=" * 60)
print("DOMAIN-SPECIFIC RULES")
print("=" * 60)

# Titanic domain rules
print(f"Fare == 0: {(df['Fare'] == 0).sum()} passengers (stowaways?)")
print(f"Age > 80: {(df['Age'] > 80).sum()} passengers")
print(f"SibSp > 5: {(df['SibSp'] > 5).sum()} passengers")
print(f"Parch > 5: {(df['Parch'] > 5).sum()} passengers")

# ============================================================
# 8. Treatment strategies
# ============================================================

print("\n" + "=" * 60)
print("TREATMENT STRATEGIES — Fare")
print("=" * 60)

# Strategy 1: Remove
lo, hi = iqr_bounds(df["Fare"].dropna())
df_removed = df[(df["Fare"] >= lo) & (df["Fare"] <= hi)]
print(f"After removal: {len(df_removed)} rows "
      f"(lost {len(df) - len(df_removed)})")

# Strategy 2: Cap (winsorize)
from scipy.stats import mstats
df_capped = df.copy()
df_capped["Fare_capped"] = mstats.winsorize(
    df_capped["Fare"].fillna(0), limits=[0.01, 0.01])
print(f"After capping: max = {df_capped['Fare_capped'].max():.2f} "
      f"(was {df['Fare'].max():.2f})")

# Strategy 3: Log transform
df_log = df.copy()
df_log["Fare_log"] = np.log1p(df_log["Fare"])
print(f"After log: skew = {df_log['Fare_log'].skew():.2f} "
      f"(was {df['Fare'].skew():.2f})")

# Strategy 4: Robust scaling
from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()
df_robust = df.copy()
df_robust["Fare_robust"] = scaler.fit_transform(
    df_robust[["Fare"]].fillna(0))

# ============================================================
# 9. Outlier treatment function
# ============================================================

def treat_outliers(series, method="cap"):
    """Treat outliers using the specified method."""
    if method == "remove":
        lo, hi = iqr_bounds(series)
        return series[(series >= lo) & (series <= hi)]
    elif method == "cap":
        lo, hi = iqr_bounds(series)
        return series.clip(lower=lo, upper=hi)
    elif method == "log":
        return np.log1p(series.clip(lower=0))
    else:
        raise ValueError(f"Unknown method: {method}")

print("\n" + "=" * 60)
print("TREATMENT FUNCTION DEMO")
print("=" * 60)

for method in ["cap", "log"]:
    treated = treat_outliers(df["Fare"].dropna(), method=method)
    print(f"{method}: mean={treated.mean():.2f}, "
          f"std={treated.std():.2f}, "
          f"max={treated.max():.2f}")

print("\nDone! Chapter 4 script completed successfully.")
