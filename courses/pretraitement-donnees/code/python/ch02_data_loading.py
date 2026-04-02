"""
Chapter 2: Data Loading
=======================
Data Pre-processing with Python — AIRINA Labs

This script demonstrates:
- Loading CSV with various options
- Loading JSON and flattening nested structures
- Loading from APIs
- Web scraping HTML tables
- Format comparison (CSV vs Parquet)
"""

import pandas as pd
import numpy as np
import time
import json

# ============================================================
# 1. Loading CSV with options
# ============================================================

print("=" * 60)
print("CSV LOADING")
print("=" * 60)

# Basic load
url = ("https://raw.githubusercontent.com/datasciencedojo/"
       "datasets/master/titanic.csv")
df = pd.read_csv(url)
print(f"Basic load — shape: {df.shape}")
print(f"Memory usage:\n{df.memory_usage(deep=True)}\n")

# Optimized load: specific columns and dtypes
cols = ["PassengerId", "Survived", "Pclass", "Sex", "Age", "Fare"]
dtypes = {"Survived": "int8", "Pclass": "int8", "Sex": "category"}
df_opt = pd.read_csv(url, usecols=cols, dtype=dtypes)
print(f"Optimized load — shape: {df_opt.shape}")
print(f"Memory usage:\n{df_opt.memory_usage(deep=True)}")

# Memory savings
orig_mem = df.memory_usage(deep=True).sum()
opt_mem = df_opt.memory_usage(deep=True).sum()
print(f"\nMemory savings: {orig_mem:,} -> {opt_mem:,} bytes "
      f"({(1 - opt_mem/orig_mem)*100:.1f}% reduction)")

# ============================================================
# 2. Standardizing column names
# ============================================================

print("\n" + "=" * 60)
print("COLUMN NAME STANDARDIZATION")
print("=" * 60)

# Simulate messy column names
messy_df = pd.DataFrame(columns=["Patient ID", " Age ", "Blood Pressure",
                                  "HbA1c (%)", "Diagnosis Code"])
messy_df.columns = (messy_df.columns
                    .str.strip()
                    .str.lower()
                    .str.replace(" ", "_")
                    .str.replace(r"[^a-z0-9_]", "", regex=True))
print(f"Cleaned columns: {messy_df.columns.tolist()}")

# ============================================================
# 3. Loading JSON
# ============================================================

print("\n" + "=" * 60)
print("JSON LOADING")
print("=" * 60)

# Simulate nested JSON (as from an API)
nested_json = {
    "results": [
        {"id": 1, "name": "Station A",
         "measurements": [{"date": "2024-01-01", "temp": 22.5},
                          {"date": "2024-01-02", "temp": 23.1}]},
        {"id": 2, "name": "Station B",
         "measurements": [{"date": "2024-01-01", "temp": 19.8},
                          {"date": "2024-01-02", "temp": 20.3}]},
    ]
}

# Flatten nested JSON
from pandas import json_normalize
df_flat = json_normalize(nested_json["results"],
                         record_path="measurements",
                         meta=["id", "name"])
print("Flattened JSON:")
print(df_flat)

# ============================================================
# 4. Loading from APIs
# ============================================================

print("\n" + "=" * 60)
print("API LOADING")
print("=" * 60)

try:
    import requests
    # World Bank API: population of Benin
    api_url = ("https://api.worldbank.org/v2/country/BEN/"
               "indicator/SP.POP.TOTL?format=json&per_page=10")
    response = requests.get(api_url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        if len(data) > 1 and data[1]:
            df_wb = pd.DataFrame(data[1])
            print(f"World Bank API — Benin population:")
            print(df_wb[["date", "value"]].head(5))
        else:
            print("API returned empty data.")
    else:
        print(f"API returned status {response.status_code}")
except ImportError:
    print("requests library not installed. Skipping API demo.")
except Exception as e:
    print(f"API call failed: {e}")

# ============================================================
# 5. Web scraping HTML tables
# ============================================================

print("\n" + "=" * 60)
print("HTML TABLE SCRAPING")
print("=" * 60)

try:
    tables = pd.read_html(
        "https://en.wikipedia.org/wiki/List_of_African_countries_by_population")
    print(f"Found {len(tables)} tables on the page")
    if tables:
        print(f"First table shape: {tables[0].shape}")
        print(tables[0].head(5))
except Exception as e:
    print(f"HTML scraping failed: {e}")

# ============================================================
# 6. CSV vs Parquet comparison
# ============================================================

print("\n" + "=" * 60)
print("CSV vs PARQUET COMPARISON")
print("=" * 60)

# Create a larger DataFrame for meaningful comparison
np.random.seed(42)
n = 100_000
large_df = pd.DataFrame({
    "id": range(n),
    "category": np.random.choice(["A", "B", "C", "D"], n),
    "value1": np.random.randn(n),
    "value2": np.random.uniform(0, 100, n),
    "date": pd.date_range("2020-01-01", periods=n, freq="min"),
})

# Save as CSV and Parquet
csv_path = "temp_comparison.csv"
pq_path = "temp_comparison.parquet"

large_df.to_csv(csv_path, index=False)
large_df.to_parquet(pq_path, index=False)

# Compare load times
start = time.time()
_ = pd.read_csv(csv_path)
csv_time = time.time() - start

start = time.time()
_ = pd.read_parquet(pq_path)
pq_time = time.time() - start

import os
csv_size = os.path.getsize(csv_path)
pq_size = os.path.getsize(pq_path)

print(f"CSV:     {csv_time:.3f}s, {csv_size / 1024 / 1024:.1f} MB")
print(f"Parquet: {pq_time:.3f}s, {pq_size / 1024 / 1024:.1f} MB")
print(f"Speed:   {csv_time / pq_time:.1f}x faster")
print(f"Size:    {csv_size / pq_size:.1f}x smaller")

# Clean up temp files
os.remove(csv_path)
os.remove(pq_path)

print("\nDone! Chapter 2 script completed successfully.")
