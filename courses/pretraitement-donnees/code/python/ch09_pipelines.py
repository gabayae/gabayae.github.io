"""
Chapter 9: Pipelines and Automation
====================================
Data Pre-processing with Python — AIRINA Labs

This script demonstrates:
- sklearn Pipeline basics
- ColumnTransformer for mixed types
- Full pipeline with model
- Custom transformers
- Saving and loading pipelines with joblib
- Cross-validation with pipelines
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# 1. Load dataset
# ============================================================

print("=" * 60)
print("PIPELINES — Adult Census Dataset")
print("=" * 60)

url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
       "adult/adult.data")
cols = ["age", "workclass", "fnlwgt", "education", "education_num",
        "marital_status", "occupation", "relationship", "race",
        "sex", "capital_gain", "capital_loss", "hours_per_week",
        "native_country", "income"]
df = pd.read_csv(url, header=None, names=cols, na_values=" ?",
                 skipinitialspace=True)

y = (df["income"] == ">50K").astype(int)
print(f"Shape: {df.shape}")
print(f"Target distribution:\n{y.value_counts()}")

# ============================================================
# 2. Basic Pipeline
# ============================================================

print("\n" + "=" * 60)
print("BASIC NUMERICAL PIPELINE")
print("=" * 60)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

num_cols = ["age", "education_num", "capital_gain",
            "capital_loss", "hours_per_week"]

num_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

X_num = num_pipe.fit_transform(df[num_cols])
print(f"Transformed shape: {X_num.shape}")
print(f"Means (should be ~0): {X_num.mean(axis=0).round(4)}")
print(f"Stds  (should be ~1): {X_num.std(axis=0).round(4)}")

# ============================================================
# 3. ColumnTransformer
# ============================================================

print("\n" + "=" * 60)
print("COLUMN TRANSFORMER")
print("=" * 60)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

num_features = ["age", "education_num", "capital_gain",
                "capital_loss", "hours_per_week"]
cat_features = ["workclass", "marital_status", "occupation",
                "relationship", "race", "sex"]

num_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
])

cat_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore",
                               sparse_output=False)),
])

preprocessor = ColumnTransformer([
    ("num", num_transformer, num_features),
    ("cat", cat_transformer, cat_features),
])

X = preprocessor.fit_transform(df)
print(f"Input shape:  {df[num_features + cat_features].shape}")
print(f"Output shape: {X.shape}")

# ============================================================
# 4. Full pipeline with model
# ============================================================

print("\n" + "=" * 60)
print("FULL PIPELINE WITH MODEL")
print("=" * 60)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

full_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
])

X_train, X_test, y_train, y_test = train_test_split(
    df[num_features + cat_features], y,
    test_size=0.2, random_state=42, stratify=y
)

full_pipeline.fit(X_train, y_train)
y_pred = full_pipeline.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred,
                            target_names=["<=50K", ">50K"]))

# ============================================================
# 5. Cross-validation
# ============================================================

print("\n" + "=" * 60)
print("CROSS-VALIDATION")
print("=" * 60)

from sklearn.model_selection import cross_val_score

scores = cross_val_score(full_pipeline,
                         df[num_features + cat_features], y,
                         cv=5, scoring="accuracy")
print(f"CV Accuracy: {scores.mean():.4f} +/- {scores.std():.4f}")
print(f"Per-fold: {scores.round(4)}")

# ============================================================
# 6. Custom transformers
# ============================================================

print("\n" + "=" * 60)
print("CUSTOM TRANSFORMERS")
print("=" * 60)

from sklearn.base import BaseEstimator, TransformerMixin

class MissingIndicator(BaseEstimator, TransformerMixin):
    """Add binary columns indicating which values were missing."""

    def fit(self, X, y=None):
        if hasattr(X, "columns"):
            self.columns_ = X.columns.tolist()
        else:
            self.columns_ = [f"col_{i}" for i in range(X.shape[1])]
        self.missing_cols_ = [c for c in self.columns_
                              if pd.DataFrame(X, columns=self.columns_)[c]
                              .isnull().any()]
        return self

    def transform(self, X):
        X_df = pd.DataFrame(X, columns=self.columns_)
        for col in self.missing_cols_:
            X_df[f"{col}_missing"] = X_df[col].isnull().astype(int)
        return X_df


class OutlierClipper(BaseEstimator, TransformerMixin):
    """Clip outliers at specified percentiles."""

    def __init__(self, lower_pct=1, upper_pct=99):
        self.lower_pct = lower_pct
        self.upper_pct = upper_pct

    def fit(self, X, y=None):
        X_arr = np.array(X)
        self.lower_ = np.nanpercentile(X_arr, self.lower_pct, axis=0)
        self.upper_ = np.nanpercentile(X_arr, self.upper_pct, axis=0)
        return self

    def transform(self, X):
        X_arr = np.array(X, dtype=float)
        return np.clip(X_arr, self.lower_, self.upper_)


# Test custom transformers
print("OutlierClipper test:")
test_data = np.array([[1, 100], [2, 200], [3, 300],
                       [100, 400], [5, 10000]])
clipper = OutlierClipper(lower_pct=5, upper_pct=95)
clipped = clipper.fit_transform(test_data)
print(f"Before max: {test_data.max(axis=0)}")
print(f"After max:  {clipped.max(axis=0)}")

# ============================================================
# 7. Pipeline with custom transformer
# ============================================================

print("\n" + "=" * 60)
print("PIPELINE WITH CUSTOM TRANSFORMER")
print("=" * 60)

custom_num_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("clipper", OutlierClipper(lower_pct=1, upper_pct=99)),
    ("scaler", StandardScaler()),
])

custom_preprocessor = ColumnTransformer([
    ("num", custom_num_transformer, num_features),
    ("cat", cat_transformer, cat_features),
])

custom_pipeline = Pipeline([
    ("preprocessor", custom_preprocessor),
    ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
])

scores_custom = cross_val_score(custom_pipeline,
                                df[num_features + cat_features], y,
                                cv=5, scoring="accuracy")
print(f"CV Accuracy (with clipping): {scores_custom.mean():.4f} "
      f"+/- {scores_custom.std():.4f}")
print(f"CV Accuracy (without):       {scores.mean():.4f} "
      f"+/- {scores.std():.4f}")

# ============================================================
# 8. Save and load pipeline
# ============================================================

print("\n" + "=" * 60)
print("SAVE AND LOAD PIPELINE")
print("=" * 60)

import joblib

# Save
joblib.dump(full_pipeline, "income_pipeline.joblib")
print("Pipeline saved to income_pipeline.joblib")

# Load
loaded_pipeline = joblib.load("income_pipeline.joblib")

# Predict on new data
new_data = pd.DataFrame({
    "age": [35, 52],
    "education_num": [13, 9],
    "capital_gain": [0, 5000],
    "capital_loss": [0, 0],
    "hours_per_week": [40, 50],
    "workclass": ["Private", "Self-emp-not-inc"],
    "marital_status": ["Married-civ-spouse", "Divorced"],
    "occupation": ["Exec-managerial", "Craft-repair"],
    "relationship": ["Husband", "Not-in-family"],
    "race": ["White", "Black"],
    "sex": ["Male", "Female"],
})

predictions = loaded_pipeline.predict(new_data)
for i, pred in enumerate(predictions):
    label = ">50K" if pred else "<=50K"
    print(f"Person {i+1}: predicted income {label}")

# Clean up
import os
os.remove("income_pipeline.joblib")

# ============================================================
# 9. Pipeline inspection
# ============================================================

print("\n" + "=" * 60)
print("PIPELINE INSPECTION")
print("=" * 60)

print("Pipeline steps:")
for name, step in full_pipeline.named_steps.items():
    print(f"  {name}: {type(step).__name__}")

# Access internal parameters
scaler = (full_pipeline.named_steps["preprocessor"]
          .named_transformers_["num"]
          .named_steps["scaler"])
print(f"\nScaler means: {scaler.mean_.round(2)}")
print(f"Scaler stds:  {scaler.scale_.round(2)}")

encoder = (full_pipeline.named_steps["preprocessor"]
           .named_transformers_["cat"]
           .named_steps["encoder"])
print(f"\nEncoder categories (first 3):")
for i, cats in enumerate(encoder.categories_[:3]):
    print(f"  {cat_features[i]}: {cats[:5]}...")

print("\nDone! Chapter 9 script completed successfully.")
