"""
Chapter 8: Time Series and Temporal Data
========================================
Data Pre-processing with Python — AIRINA Labs

This script demonstrates:
- Datetime parsing and handling mixed formats
- Resampling (downsampling and upsampling)
- Lag features
- Rolling statistics
- Trend and seasonality decomposition
- Comprehensive datetime feature extraction
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# 1. Create a synthetic temporal dataset (for portability)
# ============================================================

print("=" * 60)
print("TEMPORAL DATA — Synthetic Climate Data")
print("=" * 60)

np.random.seed(42)
n_days = 365 * 3  # 3 years of daily data
dates = pd.date_range("2021-01-01", periods=n_days, freq="D")

# Simulate temperature with trend + seasonality + noise
t = np.arange(n_days)
trend = 0.001 * t
seasonal = 10 * np.sin(2 * np.pi * t / 365)
noise = np.random.normal(0, 2, n_days)
temp = 15 + trend + seasonal + noise

df = pd.DataFrame({
    "date": dates,
    "temperature": temp,
    "humidity": 60 + 15 * np.cos(2 * np.pi * t / 365) + np.random.normal(0, 5, n_days),
    "pressure": 1013 + np.random.normal(0, 5, n_days),
})
df = df.set_index("date")

print(f"Shape: {df.shape}")
print(f"Date range: {df.index.min()} to {df.index.max()}")
print(df.head())

# ============================================================
# 2. Datetime parsing
# ============================================================

print("\n" + "=" * 60)
print("DATETIME PARSING")
print("=" * 60)

# Handling mixed date formats
messy_dates = pd.Series(["2024-01-15", "15/01/2024", "Jan 15, 2024",
                         "15-Jan-2024", "20240115"])

def parse_flexible(date_str):
    """Try multiple date formats."""
    formats = ["%Y-%m-%d", "%d/%m/%Y", "%b %d, %Y",
               "%d-%b-%Y", "%Y%m%d"]
    for fmt in formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except (ValueError, TypeError):
            continue
    return pd.NaT

parsed = messy_dates.apply(parse_flexible)
print("Messy dates parsed:")
for orig, p in zip(messy_dates, parsed):
    print(f"  '{orig}' -> {p}")

# ============================================================
# 3. Resampling
# ============================================================

print("\n" + "=" * 60)
print("RESAMPLING")
print("=" * 60)

# Weekly resampling
weekly = df.resample("W").agg({
    "temperature": ["mean", "min", "max"],
    "humidity": "mean",
    "pressure": "mean",
})
weekly.columns = ["temp_mean", "temp_min", "temp_max",
                  "humidity_mean", "pressure_mean"]
print(f"Daily records:  {len(df)}")
print(f"Weekly records: {len(weekly)}")
print(weekly.head())

# Monthly resampling
monthly = df.resample("ME").mean()
print(f"\nMonthly records: {len(monthly)}")
print(monthly.head())

# ============================================================
# 4. Lag features
# ============================================================

print("\n" + "=" * 60)
print("LAG FEATURES")
print("=" * 60)

df["temp_lag1"] = df["temperature"].shift(1)
df["temp_lag7"] = df["temperature"].shift(7)
df["temp_lag30"] = df["temperature"].shift(30)
df["temp_lag365"] = df["temperature"].shift(365)

# Change features
df["temp_change_1d"] = df["temperature"].diff(1)
df["temp_change_7d"] = df["temperature"].diff(7)
df["temp_pct_change"] = df["temperature"].pct_change()

print("Lag features (first valid rows):")
print(df[["temperature", "temp_lag1", "temp_lag7",
          "temp_change_1d"]].iloc[30:35])

# Correlation of lag features with current temperature
print("\nLag feature correlations:")
for col in ["temp_lag1", "temp_lag7", "temp_lag30", "temp_lag365"]:
    corr = df["temperature"].corr(df[col])
    print(f"  {col}: {corr:.4f}")

# ============================================================
# 5. Rolling statistics
# ============================================================

print("\n" + "=" * 60)
print("ROLLING STATISTICS")
print("=" * 60)

df["temp_roll7"] = df["temperature"].rolling(7).mean()
df["temp_roll30"] = df["temperature"].rolling(30).mean()
df["temp_roll_std7"] = df["temperature"].rolling(7).std()
df["temp_ewm7"] = df["temperature"].ewm(span=7).mean()

print("Rolling statistics:")
print(df[["temperature", "temp_roll7", "temp_roll30",
          "temp_roll_std7"]].iloc[30:35])

# ============================================================
# 6. Seasonal decomposition
# ============================================================

print("\n" + "=" * 60)
print("SEASONAL DECOMPOSITION")
print("=" * 60)

from statsmodels.tsa.seasonal import seasonal_decompose

decomposition = seasonal_decompose(monthly["temperature"],
                                    model="additive", period=12)

decomp_df = pd.DataFrame({
    "observed": decomposition.observed,
    "trend": decomposition.trend,
    "seasonal": decomposition.seasonal,
    "residual": decomposition.resid,
})
print(decomp_df.dropna().head(12))
print(f"\nSeasonal amplitude: {decomposition.seasonal.max() - decomposition.seasonal.min():.2f}")

# ============================================================
# 7. Datetime feature extraction
# ============================================================

print("\n" + "=" * 60)
print("DATETIME FEATURE EXTRACTION")
print("=" * 60)

def extract_datetime_features(df):
    """Extract comprehensive datetime features from index."""
    features = pd.DataFrame(index=df.index)
    dt = df.index

    features["year"] = dt.year
    features["month"] = dt.month
    features["day"] = dt.day
    features["dayofweek"] = dt.dayofweek
    features["quarter"] = dt.quarter
    features["is_weekend"] = dt.dayofweek.isin([5, 6]).astype(int)
    features["day_of_year"] = dt.dayofyear
    features["week_of_year"] = dt.isocalendar().week.astype(int)

    # Cyclical encoding
    features["month_sin"] = np.sin(2 * np.pi * dt.month / 12)
    features["month_cos"] = np.cos(2 * np.pi * dt.month / 12)
    features["dow_sin"] = np.sin(2 * np.pi * dt.dayofweek / 7)
    features["dow_cos"] = np.cos(2 * np.pi * dt.dayofweek / 7)

    return features

dt_features = extract_datetime_features(df)
print(f"Datetime features: {dt_features.columns.tolist()}")
print(dt_features.head())

# ============================================================
# 8. Verify cyclical encoding
# ============================================================

print("\n" + "=" * 60)
print("CYCLICAL ENCODING VERIFICATION")
print("=" * 60)

# December and January should be close in cyclical space
dec = dt_features[dt_features["month"] == 12].iloc[0]
jan = dt_features[dt_features["month"] == 1].iloc[0]
jun = dt_features[dt_features["month"] == 6].iloc[0]

dist_dec_jan = np.sqrt((dec["month_sin"] - jan["month_sin"])**2 +
                       (dec["month_cos"] - jan["month_cos"])**2)
dist_dec_jun = np.sqrt((dec["month_sin"] - jun["month_sin"])**2 +
                       (dec["month_cos"] - jun["month_cos"])**2)

print(f"Distance Dec-Jan (cyclical): {dist_dec_jan:.4f}")
print(f"Distance Dec-Jun (cyclical): {dist_dec_jun:.4f}")
print(f"Dec-Jan is {'closer' if dist_dec_jan < dist_dec_jun else 'farther'} "
      f"than Dec-Jun (as expected)")

# ============================================================
# 9. Complete temporal feature set
# ============================================================

print("\n" + "=" * 60)
print("COMPLETE FEATURE SET")
print("=" * 60)

all_features = pd.concat([df, dt_features], axis=1).dropna()
print(f"Total features: {all_features.shape[1]}")
print(f"Total rows (after dropna): {len(all_features)}")
print(f"Columns: {all_features.columns.tolist()}")

print("\nDone! Chapter 8 script completed successfully.")
