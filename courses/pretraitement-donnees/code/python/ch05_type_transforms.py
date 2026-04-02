"""
Chapter 5: Data Type Transformations
====================================
Data Pre-processing with Python — AIRINA Labs

This script demonstrates:
- Label (ordinal) encoding
- One-hot encoding
- Target encoding
- StandardScaler, MinMaxScaler, RobustScaler
- Discretization (binning)
- Power transforms
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# 1. Load Adult Census dataset
# ============================================================

print("=" * 60)
print("ADULT CENSUS DATASET")
print("=" * 60)

url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
       "adult/adult.data")
cols = ["age", "workclass", "fnlwgt", "education", "education_num",
        "marital_status", "occupation", "relationship", "race",
        "sex", "capital_gain", "capital_loss", "hours_per_week",
        "native_country", "income"]
df = pd.read_csv(url, header=None, names=cols, na_values=" ?",
                 skipinitialspace=True)

print(f"Shape: {df.shape}")
print(f"Target distribution:\n{df['income'].value_counts()}")

# ============================================================
# 2. Ordinal encoding
# ============================================================

print("\n" + "=" * 60)
print("ORDINAL ENCODING — Education")
print("=" * 60)

from sklearn.preprocessing import OrdinalEncoder

edu_order = [["Preschool", "1st-4th", "5th-6th", "7th-8th", "9th",
              "10th", "11th", "12th", "HS-grad", "Some-college",
              "Assoc-voc", "Assoc-acdm", "Bachelors", "Masters",
              "Prof-school", "Doctorate"]]

enc = OrdinalEncoder(categories=edu_order,
                     handle_unknown="use_encoded_value",
                     unknown_value=-1)
df["education_ord"] = enc.fit_transform(df[["education"]])
print(df[["education", "education_ord"]].drop_duplicates()
        .sort_values("education_ord"))

# ============================================================
# 3. One-hot encoding
# ============================================================

print("\n" + "=" * 60)
print("ONE-HOT ENCODING — Sex, Race")
print("=" * 60)

from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(sparse_output=False, drop="first",
                    handle_unknown="ignore")
encoded = ohe.fit_transform(df[["sex", "race"]].fillna("Unknown"))
encoded_df = pd.DataFrame(encoded, columns=ohe.get_feature_names_out())
print(f"One-hot columns: {encoded_df.columns.tolist()}")
print(encoded_df.head())

# pandas alternative
df_dummies = pd.get_dummies(df[["sex", "race"]], drop_first=True, dtype=int)
print(f"\npd.get_dummies columns: {df_dummies.columns.tolist()}")

# ============================================================
# 4. Target encoding
# ============================================================

print("\n" + "=" * 60)
print("TARGET ENCODING — Occupation")
print("=" * 60)

df["income_binary"] = (df["income"] == ">50K").astype(int)
target_means = df.groupby("occupation")["income_binary"].mean().to_dict()
df["occupation_target"] = df["occupation"].map(target_means)

print("Occupation -> target encoding:")
print(df[["occupation", "occupation_target"]]
        .drop_duplicates()
        .sort_values("occupation_target", ascending=False)
        .head(10))

# ============================================================
# 5. Frequency encoding
# ============================================================

print("\n" + "=" * 60)
print("FREQUENCY ENCODING — Native country")
print("=" * 60)

freq = df["native_country"].value_counts(normalize=True)
df["country_freq"] = df["native_country"].map(freq)
print(df[["native_country", "country_freq"]].drop_duplicates()
        .sort_values("country_freq", ascending=False).head(10))

# ============================================================
# 6. Numerical scaling
# ============================================================

print("\n" + "=" * 60)
print("SCALING COMPARISON")
print("=" * 60)

from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

num_features = ["age", "hours_per_week", "capital_gain"]
data = df[num_features].fillna(0)

scalers = {
    "Original": None,
    "StandardScaler": StandardScaler(),
    "MinMaxScaler": MinMaxScaler(),
    "RobustScaler": RobustScaler(),
}

for name, scaler in scalers.items():
    if scaler is None:
        scaled = data
    else:
        scaled = pd.DataFrame(scaler.fit_transform(data),
                              columns=num_features)
    print(f"\n{name}:")
    print(scaled.describe().loc[["mean", "std", "min", "max"]].round(3))

# ============================================================
# 7. Discretization (binning)
# ============================================================

print("\n" + "=" * 60)
print("DISCRETIZATION — Age")
print("=" * 60)

# Equal-width
df["age_bin_width"] = pd.cut(df["age"], bins=5)
print("Equal-width bins:")
print(df["age_bin_width"].value_counts().sort_index())

# Quantile
df["age_bin_quantile"] = pd.qcut(df["age"], q=5,
                                  labels=["Q1", "Q2", "Q3", "Q4", "Q5"])
print(f"\nQuantile bins:")
print(df["age_bin_quantile"].value_counts().sort_index())

# Domain-based
df["age_group"] = pd.cut(df["age"],
                          bins=[0, 25, 35, 50, 65, 100],
                          labels=["<25", "25-34", "35-49", "50-64", "65+"])
print(f"\nDomain bins:")
print(df["age_group"].value_counts().sort_index())

# Income rate by age group
print(f"\nIncome >50K rate by age group:")
print(df.groupby("age_group")["income_binary"].mean().round(3))

# ============================================================
# 8. Power transforms
# ============================================================

print("\n" + "=" * 60)
print("POWER TRANSFORMS — Capital Gain")
print("=" * 60)

from sklearn.preprocessing import PowerTransformer

# Yeo-Johnson
pt = PowerTransformer(method="yeo-johnson")
df["cg_yeojohnson"] = pt.fit_transform(df[["capital_gain"]])

# Log
df["cg_log"] = np.log1p(df["capital_gain"])

print(f"Original skew:     {df['capital_gain'].skew():.2f}")
print(f"Yeo-Johnson skew:  {df['cg_yeojohnson'].skew():.2f}")
print(f"Log1p skew:        {df['cg_log'].skew():.2f}")

print("\nDone! Chapter 5 script completed successfully.")
