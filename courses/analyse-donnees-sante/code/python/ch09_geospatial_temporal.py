"""
Chapter 9: Geospatial and temporal health data
Data Analysis with Python for Health Specialists

Run in Jupyter notebook or Google Colab.
Datasets: JHU CSSE COVID-19, Natural Earth (geopandas built-in)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. Time series: date parsing and indexing
# ============================================================

print("=== Time series: malaria cases ===")
dates = pd.date_range("2023-01-01", periods=365, freq="D")
np.random.seed(42)
# Simulate seasonal pattern: peak during rainy season (June-September)
day_of_year = dates.dayofyear
seasonal = 50 + 40 * np.sin(2 * np.pi * (day_of_year - 90) / 365)
cases = np.maximum(0, seasonal + np.random.normal(0, 12, 365)).astype(int)

df = pd.DataFrame({"date": dates, "cases": cases})
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")
print(df.head())

# ============================================================
# 2. Rolling averages
# ============================================================

df["cases_7d"] = df["cases"].rolling(window=7).mean()
df["cases_14d"] = df["cases"].rolling(window=14).mean()

fig, ax = plt.subplots(figsize=(12, 5))
ax.bar(df.index, df["cases"], alpha=0.3, label="Daily cases", color="steelblue")
ax.plot(df.index, df["cases_7d"], color="red", linewidth=2, label="7-day average")
ax.plot(df.index, df["cases_14d"], color="darkgreen", linewidth=2, label="14-day average")
ax.set_xlabel("Date")
ax.set_ylabel("Malaria cases")
ax.set_title("Daily malaria cases with rolling averages")
ax.legend()
plt.tight_layout()
plt.show()

# ============================================================
# 3. Trend decomposition
# ============================================================

from statsmodels.tsa.seasonal import seasonal_decompose

result = seasonal_decompose(df["cases"], model="additive", period=30)

fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)
result.observed.plot(ax=axes[0], title="Observed")
result.trend.plot(ax=axes[1], title="Trend")
result.seasonal.plot(ax=axes[2], title="Seasonal")
result.resid.plot(ax=axes[3], title="Residual")
plt.tight_layout()
plt.show()

# ============================================================
# 4. COVID-19 case curves (JHU data)
# ============================================================

print("\n=== COVID-19 data ===")
url = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/"
       "master/csse_covid_19_data/csse_covid_19_time_series/"
       "time_series_covid19_confirmed_global.csv")
confirmed = pd.read_csv(url)
print(f"Shape: {confirmed.shape}")
print(confirmed.head())

# ============================================================
# 5. Reshaping wide to long format
# ============================================================

countries = ["South Africa", "Nigeria", "Kenya", "Egypt", "Morocco"]
africa = confirmed[confirmed["Country/Region"].isin(countries)]

# Group by country
africa = africa.groupby("Country/Region").sum(numeric_only=True)
africa = africa.drop(columns=["Lat", "Long"], errors="ignore")

# Reshape: wide -> long
africa_long = africa.T
africa_long.index = pd.to_datetime(africa_long.index)
africa_long.index.name = "date"
print(africa_long.head())

# ============================================================
# 6. Daily cases and 7-day averages
# ============================================================

# Cumulative -> daily new cases
daily = africa_long.diff().clip(lower=0)

# 7-day rolling average
daily_7d = daily.rolling(7).mean()

fig, ax = plt.subplots(figsize=(14, 6))
for country in countries:
    ax.plot(daily_7d.index, daily_7d[country], linewidth=2, label=country)
ax.set_xlabel("Date")
ax.set_ylabel("Daily new cases (7-day average)")
ax.set_title("COVID-19 daily cases in 5 African countries")
ax.legend()
plt.tight_layout()
plt.show()

# ============================================================
# 7. Introduction to geopandas
# ============================================================

try:
    import geopandas as gpd

    print("\n=== Geospatial data ===")
    # Natural Earth dataset (built into geopandas)
    world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    print(f"Columns: {world.columns.tolist()}")
    print(f"CRS: {world.crs}")
    print(world.head())

    # ============================================================
    # 8. Choropleth map: Africa population
    # ============================================================

    africa_map = world[world["continent"] == "Africa"].copy()

    fig, ax = plt.subplots(figsize=(10, 10))
    africa_map.plot(column="pop_est", cmap="YlOrRd", legend=True,
                    legend_kwds={"label": "Population", "shrink": 0.6},
                    edgecolor="black", linewidth=0.5, ax=ax)
    ax.set_title("Population estimates in African countries")
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()

    # ============================================================
    # 9. Mapping malaria prevalence (simulated merge)
    # ============================================================

    # Simulated malaria incidence data for demonstration
    np.random.seed(42)
    malaria_data = pd.DataFrame({
        "country": africa_map["name"].values,
        "incidence_per_1000": np.random.exponential(100, len(africa_map)).clip(0, 500)
    })

    africa_malaria = africa_map.merge(malaria_data, left_on="name",
                                       right_on="country", how="left")

    fig, ax = plt.subplots(figsize=(10, 10))
    africa_malaria.plot(column="incidence_per_1000", cmap="YlOrRd",
                         legend=True, missing_kwds={"color": "lightgrey"},
                         legend_kwds={"label": "Incidence per 1,000",
                                      "shrink": 0.6},
                         edgecolor="black", linewidth=0.5, ax=ax)
    ax.set_title("Malaria incidence in Africa (simulated)")
    ax.set_axis_off()
    plt.tight_layout()
    plt.show()

    # ============================================================
    # 10. Small multiples: one map per time period
    # ============================================================

    # Example with simulated data at 3 time points
    fig, axes = plt.subplots(1, 3, figsize=(18, 7))
    time_labels = ["2020", "2021", "2022"]

    for ax, year_label in zip(axes, time_labels):
        np.random.seed(int(year_label))
        temp = africa_map.copy()
        temp["cases"] = np.random.exponential(50000, len(temp)).astype(int)

        temp.plot(column="cases", cmap="Reds", legend=True,
                  edgecolor="black", linewidth=0.5, ax=ax,
                  missing_kwds={"color": "lightgrey"})
        ax.set_title(year_label)
        ax.set_axis_off()

    plt.suptitle("Simulated COVID-19 cumulative cases in Africa", fontsize=14)
    plt.tight_layout()
    plt.show()

except ImportError:
    print("\ngeopandas not installed. Run: pip install geopandas mapclassify")

# ============================================================
# 11. Animated maps (skeleton)
# ============================================================

# Animation code (commented out -- requires full data pipeline)
# import matplotlib.animation as animation
#
# fig, ax = plt.subplots(figsize=(10, 10))
#
# def update(frame_date):
#     ax.clear()
#     temp = africa_map.copy()
#     # ... merge case data for this date ...
#     temp.plot(column="cases", cmap="Reds", ax=ax, edgecolor="black",
#               linewidth=0.5, missing_kwds={"color": "lightgrey"},
#               vmin=0, vmax=max_cases)
#     ax.set_title(f"COVID-19 cases - {frame_date}")
#     ax.set_axis_off()
#
# ani = animation.FuncAnimation(fig, update, frames=monthly_dates,
#                                interval=500)
# ani.save("covid_africa.gif", writer="pillow")

print("\nAnimation code is provided as a skeleton -- see source for details.")

# ============================================================
# 12. Practical: COVID-19 dashboard layout
# ============================================================

print("\n=== Dashboard layout ===")
print("Use the following layout for a 4-panel COVID-19 dashboard:")
print("  axes[0, 0] -> Panel 1: Confirmed cases over time")
print("  axes[0, 1] -> Panel 2: Deaths over time")
print("  axes[1, 0] -> Panel 3: Vaccination progress")
print("  axes[1, 1] -> Panel 4: Choropleth map")
print()
print("Data sources:")
print("  Cases:  https://raw.githubusercontent.com/CSSEGISandData/COVID-19/...")
print("  Deaths: time_series_covid19_deaths_global.csv")
print("  Vaccination: https://raw.githubusercontent.com/owid/covid-19-data/...")
print("  Map:    geopandas naturalearth_lowres")
