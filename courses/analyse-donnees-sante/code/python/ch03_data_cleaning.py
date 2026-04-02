"""
Chapter 3: Data cleaning in health contexts
Data Analysis with Python for Health Specialists

Run in Jupyter notebook or Google Colab.
"""

import pandas as pd
import numpy as np

# ============================================================
# 1. Detecting missing values
# ============================================================

# Create a clinical dataset with missing values
data = {
    "patient_id": ["P001", "P002", "P003", "P004", "P005", "P006"],
    "age": [45, 67, 34, np.nan, 71, 52],
    "sex": ["M", "F", "F", "M", np.nan, "F"],
    "systolic_bp": [128, 158, np.nan, 145, 162, np.nan],
    "hba1c": [5.4, 7.8, 5.1, np.nan, 8.2, 6.3],
    "smoking": ["Never", np.nan, "Current", "Former", np.nan, "Never"]
}
df = pd.DataFrame(data)

# Count missing values per column
print("=== Missing values per column ===")
print(df.isnull().sum())

# Percentage missing per column
print("\n=== Percentage missing ===")
print((df.isnull().sum() / len(df) * 100).round(1))

# Rows with any missing value
print(f"\nRows with missing data: {df.isnull().any(axis=1).sum()} / {len(df)}")

# ============================================================
# 2. Visualizing missingness with msno
# ============================================================

try:
    import missingno as msno
    import matplotlib.pyplot as plt

    # Matrix plot: white bars = missing
    msno.matrix(df)
    plt.title("Missing data pattern")
    plt.tight_layout()
    plt.show()

    # Bar chart: count of non-null values per column
    msno.bar(df)
    plt.tight_layout()
    plt.show()

    # Heatmap: correlations between missingness of different columns
    msno.heatmap(df)
    plt.tight_layout()
    plt.show()
except ImportError:
    print("\nmissingno not installed. Run: pip install missingno")

# ============================================================
# 3. Patterns of co-missingness
# ============================================================

# Check which columns are missing together
missing_pairs = df.isnull().corr()
print("\n=== Co-missingness correlation ===")
print(missing_pairs)

# ============================================================
# 4. Dropping missing data
# ============================================================

# Drop rows with any missing value
df_complete = df.dropna()
print(f"\nRows remaining after dropna(): {len(df_complete)} / {len(df)}")

# Drop rows only if specific columns are missing
df_partial = df.dropna(subset=["age", "systolic_bp"])
print(f"Rows remaining (age & BP required): {len(df_partial)} / {len(df)}")

# ============================================================
# 5. Imputation strategies
# ============================================================

# Reset df for imputation demos
df = pd.DataFrame(data)

# Median imputation for lab values (robust to outliers)
df["systolic_bp"] = df["systolic_bp"].fillna(df["systolic_bp"].median())
df["hba1c"] = df["hba1c"].fillna(df["hba1c"].median())

# Mean imputation for age (approximately symmetric distribution)
df["age"] = df["age"].fillna(df["age"].mean())

print("\n=== After numeric imputation ===")
print(df[["age", "systolic_bp", "hba1c"]])

# Mode imputation for categorical variables
df["sex"] = df["sex"].fillna(df["sex"].mode()[0])
df["smoking"] = df["smoking"].fillna(df["smoking"].mode()[0])

print("\n=== After categorical imputation ===")
print(df[["sex", "smoking"]])

# ============================================================
# 6. Group-specific imputation
# ============================================================

df = pd.DataFrame(data)

# Impute systolic_bp with the median for the patient's age group
df["age"] = df["age"].fillna(df["age"].mean())
df["age_group"] = pd.cut(df["age"], bins=[0, 40, 60, 100],
                         labels=["<40", "40-59", "60+"])
df["systolic_bp"] = df.groupby("age_group")["systolic_bp"].transform(
    lambda x: x.fillna(x.median())
)
print("\n=== Group-specific imputation ===")
print(df[["patient_id", "age_group", "systolic_bp"]])

# ============================================================
# 7. KNN imputation
# ============================================================

from sklearn.impute import KNNImputer

df = pd.DataFrame(data)

# Select numeric columns for KNN imputation
numeric_cols = ["age", "systolic_bp", "hba1c"]
imputer = KNNImputer(n_neighbors=5)
df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

print("\n=== After KNN imputation ===")
print(df[numeric_cols])

# ============================================================
# 8. Missingness indicator
# ============================================================

df = pd.DataFrame(data)

# Before imputing, create a flag
df["bp_was_missing"] = df["systolic_bp"].isnull().astype(int)

# Then impute
df["systolic_bp"] = df["systolic_bp"].fillna(df["systolic_bp"].median())

print("\n=== Missingness indicator ===")
print(df[["patient_id", "systolic_bp", "bp_was_missing"]])

# ============================================================
# 9. Handling duplicates
# ============================================================

patients = pd.DataFrame({
    "patient_id": ["P001", "P002", "P003", "P002", "P004", "P003"],
    "visit_date": ["2023-01-15", "2023-01-16", "2023-01-17",
                   "2023-01-16", "2023-01-18", "2023-02-20"],
    "systolic_bp": [128, 158, 112, 158, 145, 118],
    "diagnosis": ["HTN", "T2DM", "None", "T2DM", "HTN", "None"]
})

# Exact duplicates (all columns identical)
print(f"\n=== Duplicates ===")
print(f"Exact duplicates: {patients.duplicated().sum()}")
print(patients[patients.duplicated(keep=False)])

# Duplicates based on patient_id only
print(f"\nDuplicate patient IDs: {patients.duplicated(subset='patient_id').sum()}")

# Remove exact duplicates
patients_clean = patients.drop_duplicates()
print(f"After removing exact duplicates: {len(patients_clean)} rows")

# Keep only the first visit per patient
first_visits = patients.drop_duplicates(subset="patient_id", keep="first")
print(f"First visits only: {len(first_visits)} rows")

# Keep only the last visit per patient
last_visits = patients.drop_duplicates(subset="patient_id", keep="last")

# ============================================================
# 10. Inconsistent data: ICD codes
# ============================================================

diagnoses = pd.Series(["E11.9", "e11.9", "E119", "E11.9 ", " e11.9"])

# Standardize: uppercase, strip whitespace, ensure dot format
cleaned = (diagnoses
           .str.strip()
           .str.upper()
           .str.replace(r"^([A-Z]\d{2})(\d+)$", r"\1.\2", regex=True))
print("\n=== Standardized ICD codes ===")
print(cleaned)

# ============================================================
# 11. Inconsistent data: dates
# ============================================================

dates = pd.Series(["2023-01-15", "01/15/2023", "15-Jan-2023",
                   "Jan 15, 2023", "20230115"])

# pd.to_datetime handles multiple formats automatically
parsed = pd.to_datetime(dates, format="mixed", dayfirst=False)
print("\n=== Parsed dates ===")
print(parsed)

# Standardize to ISO format
print(parsed.dt.strftime("%Y-%m-%d"))

# ============================================================
# 12. Unit conversions
# ============================================================

def standardize_glucose(value, unit=None):
    """Convert glucose to mmol/L. Infer unit if not provided."""
    if unit == "mg/dL" or (unit is None and value > 30):
        return value / 18.018
    return value  # already in mmol/L

# Test
test_values = [95, 7.2, 110, 180, 5.5]
for v in test_values:
    converted = standardize_glucose(v)
    print(f"  {v:6.1f} -> {converted:.2f} mmol/L")

# ============================================================
# 13. Standardizing text fields
# ============================================================

sex_col = pd.Series(["Male", "male", "M", "m", "MALE", "Female",
                     "female", "F", "f", "FEMALE"])

# Map to standard values
sex_mapping = {"male": "M", "m": "M", "female": "F", "f": "F"}
sex_clean = sex_col.str.strip().str.lower().map(sex_mapping)
print("\n=== Standardized sex field ===")
print(sex_clean)

# ============================================================
# 14. Data validation: range checks
# ============================================================

ranges = {
    "age": (0, 120),
    "systolic_bp": (60, 300),
    "diastolic_bp": (30, 200),
    "heart_rate": (20, 300),
    "hba1c": (2.0, 20.0),
    "glucose_mgdl": (10, 1500),
    "bmi": (8, 80),
    "temperature_c": (25, 45),
}

def validate_range(df, column, low, high):
    """Flag values outside the plausible range."""
    out_of_range = df[(df[column] < low) | (df[column] > high)]
    if len(out_of_range) > 0:
        print(f"WARNING: {len(out_of_range)} values in '{column}' "
              f"outside [{low}, {high}]")
        print(out_of_range[["patient_id", column]])
    return out_of_range

# ============================================================
# 15. Automated data quality report
# ============================================================

def data_quality_report(df):
    """Generate a summary of data quality issues."""
    report = []
    for col in df.columns:
        n_missing = df[col].isnull().sum()
        pct_missing = n_missing / len(df) * 100
        n_unique = df[col].nunique()

        row = {
            "column": col,
            "dtype": str(df[col].dtype),
            "n_missing": n_missing,
            "pct_missing": round(pct_missing, 1),
            "n_unique": n_unique,
        }

        if df[col].dtype in ["float64", "int64"]:
            row["min"] = df[col].min()
            row["max"] = df[col].max()
            row["mean"] = round(df[col].mean(), 2)

        report.append(row)

    return pd.DataFrame(report)

df = pd.DataFrame(data)
quality = data_quality_report(df)
print("\n=== Data quality report ===")
print(quality.to_string(index=False))

# ============================================================
# 16. Complete cleaning pipeline
# ============================================================

from sklearn.impute import KNNImputer

# Step 1: Load data
url = ("https://raw.githubusercontent.com/datasets/"
       "gapminder/main/data/gapminder.csv")
df = pd.read_csv(url)
print(f"\n=== Complete pipeline ===")
print(f"Raw data: {df.shape}")

# Step 2: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 3: Remove exact duplicates
n_before = len(df)
df = df.drop_duplicates()
print(f"Duplicates removed: {n_before - len(df)}")

# Step 4: Assess missing data
missing_pct = (df.isnull().sum() / len(df) * 100).round(1)
print("Missing percentages:")
print(missing_pct[missing_pct > 0])

# Step 5: Validate ranges
outliers = df[(df["lifeexp"] < 20) | (df["lifeexp"] > 90)]
print(f"Life expectancy outliers: {len(outliers)}")

# Step 6: Save cleaned data
df.to_csv("gapminder_cleaned.csv", index=False)
print(f"Cleaned data saved: {df.shape}")

# ============================================================
# 17. Practical: cleaning a messy clinical dataset
# ============================================================

print("\n=== Messy clinical dataset ===")

messy = pd.DataFrame({
    "patient_id": ["P001", "P002", "P003", "P004", "P002",
                   "P005", "P006", "P007", "P008", "P009"],
    "age": [45, 67, -3, 52, 67, 200, 38, np.nan, 71, 44],
    "sex": ["M", "F", "Female", "m", "F",
            "Male", np.nan, "F", "X", "M"],
    "systolic_bp": [128, 158, 112, 450, 158,
                    135, 122, np.nan, 162, 118],
    "diastolic_bp": [82, 160, 74, 92, 160,
                     88, 78, np.nan, 98, 76],
    "glucose_mgdl": [95, 7.2, 110, 180, 95,
                     88, 102, 6.8, 220, 5.5],
    "hba1c": [5.4, 7.8, 5.1, 6.3, 7.8,
              np.nan, 5.8, 6.1, 55, 5.2],
    "visit_date": ["2023-01-15", "01/16/2023", "2023-01-17",
                   "2023/01/18", "2023-01-16",
                   "15-Jan-2023", "2023-01-20", "2023-01-21",
                   "2023-01-22", "Jan 23, 2023"],
    "icd_code": ["I10", "E119", "e11.9", "I10 ", " i10",
                 "E11.9", "I10", "e119", "I10", "E11.9"]
})

print(f"Initial shape: {messy.shape}")
print(data_quality_report(messy).to_string(index=False))

# Remove exact duplicates
messy = messy.drop_duplicates()
print(f"\nAfter dedup: {len(messy)} rows")

# Standardize sex
sex_map = {"male": "M", "m": "M", "female": "F", "f": "F", "x": np.nan}
messy["sex"] = messy["sex"].str.strip().str.lower().map(sex_map)

# Fix impossible ages
messy.loc[(messy["age"] < 0) | (messy["age"] > 120), "age"] = np.nan

# Fix impossible systolic BP
messy.loc[messy["systolic_bp"] > 300, "systolic_bp"] = np.nan

# Flag diastolic >= systolic
bp_errors = messy[messy["diastolic_bp"] >= messy["systolic_bp"]]
print(f"Diastolic >= systolic errors: {len(bp_errors)}")

# Fix glucose: values < 30 are likely mmol/L
messy["glucose_mgdl"] = messy["glucose_mgdl"].apply(
    lambda x: x * 18.018 if x < 30 else x
)

# Fix HbA1c: value 55 is likely IFCC (mmol/mol)
messy["hba1c"] = messy["hba1c"].apply(
    lambda x: 0.0915 * x + 2.15 if x > 20 else x
)

# Standardize dates
messy["visit_date"] = pd.to_datetime(messy["visit_date"], format="mixed",
                                      dayfirst=False)

# Standardize ICD codes
messy["icd_code"] = (messy["icd_code"]
                     .str.strip()
                     .str.upper()
                     .str.replace(r"^([A-Z]\d{2})(\d+)$", r"\1.\2", regex=True))

# Impute remaining missing values
for col in ["age", "systolic_bp", "hba1c", "diastolic_bp"]:
    messy[col] = messy[col].fillna(messy[col].median())
messy["sex"] = messy["sex"].fillna(messy["sex"].mode()[0])

print("\n=== Final quality report ===")
print(data_quality_report(messy).to_string(index=False))

messy.to_csv("cleaned_clinical_data.csv", index=False)
print(f"\nSaved: cleaned_clinical_data.csv ({len(messy)} rows)")
