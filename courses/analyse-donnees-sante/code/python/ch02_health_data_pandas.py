"""
Chapter 2: Health data with Pandas
Data Analysis with Python for Health Specialists

Run in Jupyter notebook or Google Colab.
Datasets: Gapminder (life expectancy by country/year)
"""

import pandas as pd
import numpy as np

# ============================================================
# 1. Loading real health data
# ============================================================

# Gapminder dataset: life expectancy, population, GDP per capita
url = "https://raw.githubusercontent.com/datasets/gapminder/main/data/gapminder.csv"
gm = pd.read_csv(url)

print("=== Gapminder dataset ===")
print(f"Shape: {gm.shape}")
print(f"Columns: {gm.columns.tolist()}")
print()
print(gm.head())
print()
print(gm.describe())

# ============================================================
# 2. Exploring the data
# ============================================================

print("\n=== Data types ===")
print(gm.dtypes)

print("\n=== Unique values ===")
print(f"Countries: {gm['country'].nunique()}")
print(f"Continents: {gm['continent'].unique()}")
print(f"Years: {sorted(gm['year'].unique())}")

# ============================================================
# 3. Filtering
# ============================================================

# African countries only
africa = gm[gm["continent"] == "Africa"]
print(f"\n=== Africa ===")
print(f"African countries: {africa['country'].nunique()}")
print(f"Records: {len(africa)}")

# Most recent year
latest = gm[gm["year"] == gm["year"].max()]
print(f"\nLatest year: {gm['year'].max()}")

# Countries with life expectancy below 50 in most recent year
low_le = latest[latest["lifeExp"] < 50]
print(f"Countries with life expectancy < 50: {len(low_le)}")
print(low_le[["country", "continent", "lifeExp"]].sort_values("lifeExp"))

# ============================================================
# 4. Sorting and ranking
# ============================================================

# Top 10 countries by life expectancy (most recent year)
top10 = latest.sort_values("lifeExp", ascending=False).head(10)
print("\n=== Top 10 life expectancy ===")
print(top10[["country", "continent", "lifeExp"]].to_string(index=False))

# Bottom 10
bottom10 = latest.sort_values("lifeExp").head(10)
print("\n=== Bottom 10 life expectancy ===")
print(bottom10[["country", "continent", "lifeExp"]].to_string(index=False))

# ============================================================
# 5. Grouping and aggregation
# ============================================================

print("\n=== Life expectancy by continent (most recent year) ===")
by_continent = latest.groupby("continent")["lifeExp"].agg(
    ["mean", "median", "std", "min", "max", "count"]
).round(1)
print(by_continent.sort_values("mean", ascending=False))

# ============================================================
# 6. Creating new columns
# ============================================================

# Life expectancy category
gm["le_category"] = pd.cut(
    gm["lifeExp"],
    bins=[0, 50, 65, 75, 100],
    labels=["Very low (<50)", "Low (50-65)", "Medium (65-75)", "High (>75)"]
)

# GDP per capita category
gm["income_group"] = pd.cut(
    gm["gdpPercap"],
    bins=[0, 1000, 5000, 20000, 200000],
    labels=["Low", "Lower-middle", "Upper-middle", "High"]
)

# Cross-tabulation
print("\n=== Life expectancy vs income (most recent year) ===")
latest_full = gm[gm["year"] == gm["year"].max()]
ct = pd.crosstab(latest_full["le_category"], latest_full["income_group"])
print(ct)

# ============================================================
# 7. Time trends
# ============================================================

# Average life expectancy over time by continent
trends = gm.groupby(["year", "continent"])["lifeExp"].mean().reset_index()
print("\n=== Life expectancy trends (Africa) ===")
africa_trends = trends[trends["continent"] == "Africa"]
print(africa_trends[["year", "lifeExp"]].to_string(index=False))

# ============================================================
# 8. Saving results
# ============================================================

# Save Africa data
africa_latest = latest[latest["continent"] == "Africa"][
    ["country", "lifeExp", "pop", "gdpPercap"]
].sort_values("lifeExp", ascending=False)

africa_latest.to_csv("africa_health_2007.csv", index=False)
print(f"\nSaved: africa_health_2007.csv ({len(africa_latest)} rows)")
