"""
Chapter 5: Visualization for health data
Data Analysis with Python for Health Specialists

Run in Jupyter notebook or Google Colab.
Datasets: Gapminder (life expectancy by country/year)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# 1. Setup: matplotlib and seaborn
# ============================================================

# Set a clean style for all plots
sns.set_theme(style="whitegrid", font_scale=1.1)
plt.rcParams["figure.figsize"] = (8, 5)
plt.rcParams["figure.dpi"] = 100

# Colorblind-friendly palette
cb_palette = ["#0072B2", "#D55E00", "#009E73",
              "#CC79A7", "#F0E442", "#56B4E9"]
sns.set_palette(cb_palette)

# ============================================================
# 2. Histograms and density plots
# ============================================================

# Load Gapminder data
url = ("https://raw.githubusercontent.com/datasets/"
       "gapminder/main/data/gapminder.csv")
gapminder = pd.read_csv(url)
recent = gapminder[gapminder["year"] == 2007]

# Histogram of life expectancy
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: histogram
axes[0].hist(recent["lifeExp"], bins=20, edgecolor="white", alpha=0.8)
axes[0].set_xlabel("Life expectancy (years)")
axes[0].set_ylabel("Number of countries")
axes[0].set_title("Distribution of life expectancy, 2007")
axes[0].axvline(recent["lifeExp"].median(), color="red",
                linestyle="--", label=f'Median: {recent["lifeExp"].median():.1f}')
axes[0].legend()

# Right: kernel density estimate (smooth version)
sns.kdeplot(data=recent, x="lifeExp", hue="continent",
            fill=True, alpha=0.3, ax=axes[1])
axes[1].set_xlabel("Life expectancy (years)")
axes[1].set_title("Life expectancy by continent, 2007")

plt.tight_layout()
plt.show()

# Clinical example: distribution of fasting glucose
np.random.seed(42)
normal_glucose = np.random.normal(95, 10, 800)
prediabetic = np.random.normal(115, 8, 150)
diabetic = np.random.normal(180, 40, 50)
all_glucose = np.concatenate([normal_glucose, prediabetic, diabetic])

fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(all_glucose, bins=40, edgecolor="white", alpha=0.7)
ax.axvline(100, color="orange", linestyle="--", linewidth=2,
           label="Normal threshold (100 mg/dL)")
ax.axvline(126, color="red", linestyle="--", linewidth=2,
           label="Diabetic threshold (126 mg/dL)")
ax.set_xlabel("Fasting glucose (mg/dL)")
ax.set_ylabel("Number of patients")
ax.set_title("Distribution of fasting glucose (n=1,000)")
ax.legend()
plt.tight_layout()
plt.show()

# ============================================================
# 3. Box plots
# ============================================================

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=recent, x="continent", y="lifeExp", ax=ax)
ax.set_xlabel("Continent")
ax.set_ylabel("Life expectancy (years)")
ax.set_title("Life expectancy by continent, 2007 (n={})".format(len(recent)))
plt.tight_layout()
plt.show()

# Clinical example: BMI by sex and age group
np.random.seed(42)
n = 500
clinical = pd.DataFrame({
    "sex": np.random.choice(["Male", "Female"], n),
    "age_group": np.random.choice(["18-39", "40-59", "60+"], n,
                                  p=[0.3, 0.4, 0.3]),
    "bmi": np.random.normal(27, 5, n).clip(15, 50)
})

fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=clinical, x="age_group", y="bmi", hue="sex",
            order=["18-39", "40-59", "60+"], ax=ax)
ax.axhline(25, color="orange", linestyle="--", alpha=0.7,
           label="Overweight threshold")
ax.axhline(30, color="red", linestyle="--", alpha=0.7,
           label="Obese threshold")
ax.set_xlabel("Age group")
ax.set_ylabel("BMI (kg/m²)")
ax.set_title(f"BMI by sex and age group (n={n})")
ax.legend()
plt.tight_layout()
plt.show()

# ============================================================
# 4. Bar charts
# ============================================================

# Bottom 15 countries by life expectancy
bottom15 = recent.nsmallest(15, "lifeExp")

fig, ax = plt.subplots(figsize=(10, 7))
ax.barh(bottom15["country"], bottom15["lifeExp"], color="#D55E00")
ax.set_xlabel("Life expectancy (years)")
ax.set_title("15 countries with lowest life expectancy, 2007")
ax.invert_yaxis()
for i, v in enumerate(bottom15["lifeExp"]):
    ax.text(v + 0.5, i, f"{v:.1f}", va="center", fontsize=9)
plt.tight_layout()
plt.show()

# Disease prevalence comparison by country (simulated)
diseases = pd.DataFrame({
    "country": ["Nigeria", "DRC", "Tanzania", "Kenya", "Ghana",
                "South Africa", "Ethiopia", "Uganda"],
    "malaria_prev": [27.3, 31.2, 7.5, 5.8, 15.2, 0.5, 1.2, 9.7],
    "hiv_prev": [1.3, 0.7, 4.7, 4.9, 1.7, 19.0, 1.0, 5.4],
})

fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(len(diseases))
width = 0.35
ax.bar(x - width/2, diseases["malaria_prev"], width,
       label="Malaria", color="#0072B2")
ax.bar(x + width/2, diseases["hiv_prev"], width,
       label="HIV", color="#D55E00")
ax.set_xticks(x)
ax.set_xticklabels(diseases["country"], rotation=45, ha="right")
ax.set_ylabel("Prevalence (%)")
ax.set_title("Malaria vs HIV prevalence by country")
ax.legend()
plt.tight_layout()
plt.show()

# ============================================================
# 5. Line plots: time trends
# ============================================================

continent_trend = gapminder.groupby(
    ["year", "continent"])["lifeExp"].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
for continent in continent_trend["continent"].unique():
    subset = continent_trend[continent_trend["continent"] == continent]
    ax.plot(subset["year"], subset["lifeExp"],
            marker="o", markersize=4, label=continent)

ax.set_xlabel("Year")
ax.set_ylabel("Mean life expectancy (years)")
ax.set_title("Life expectancy trends by continent, 1952-2007")
ax.legend(title="Continent")
plt.tight_layout()
plt.show()

# ============================================================
# 6. Epidemic curves
# ============================================================

np.random.seed(42)
days = pd.date_range("2023-01-01", periods=120, freq="D")
t = np.arange(120)
peak = 45
cases = np.maximum(0, 200 * np.exp(-0.5 * ((t - peak) / 15) ** 2)
                   + np.random.normal(0, 10, 120)).astype(int)

epi = pd.DataFrame({"date": days, "new_cases": cases})
epi["rolling_7d"] = epi["new_cases"].rolling(7).mean()
epi["cumulative"] = epi["new_cases"].cumsum()

fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Top: daily cases + 7-day average
axes[0].bar(epi["date"], epi["new_cases"], alpha=0.4,
            color="#0072B2", label="Daily cases")
axes[0].plot(epi["date"], epi["rolling_7d"], color="#D55E00",
             linewidth=2, label="7-day average")
axes[0].set_ylabel("New cases per day")
axes[0].set_title("Epidemic curve: daily new cases")
axes[0].legend()

# Bottom: cumulative cases
axes[1].plot(epi["date"], epi["cumulative"], color="#009E73",
             linewidth=2)
axes[1].set_xlabel("Date")
axes[1].set_ylabel("Cumulative cases")
axes[1].set_title("Cumulative case count")

plt.tight_layout()
plt.show()

# ============================================================
# 7. Scatter plots
# ============================================================

# GDP per capita vs life expectancy (the classic Gapminder plot)
fig, ax = plt.subplots(figsize=(10, 7))
for continent in recent["continent"].unique():
    subset = recent[recent["continent"] == continent]
    ax.scatter(subset["gdpPercap"], subset["lifeExp"],
               s=subset["pop"] / 1e6,  # bubble size = population
               alpha=0.6, label=continent)

ax.set_xscale("log")
ax.set_xlabel("GDP per capita (log scale, USD)")
ax.set_ylabel("Life expectancy (years)")
ax.set_title("Wealth vs Health, 2007 (bubble size = population)")
ax.legend(title="Continent")
plt.tight_layout()
plt.show()

# Clinical scatter: BMI vs systolic BP with regression line
np.random.seed(42)
n = 200
bmi = np.random.normal(28, 5, n).clip(18, 45)
sbp = 80 + 1.8 * bmi + np.random.normal(0, 12, n)

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(bmi, sbp, alpha=0.5, s=30, color="#0072B2")

# Add regression line
from numpy.polynomial.polynomial import polyfit
b, m = polyfit(bmi, sbp, 1)
x_line = np.linspace(bmi.min(), bmi.max(), 100)
ax.plot(x_line, b + m * x_line, color="#D55E00", linewidth=2,
        label=f"y = {m:.1f}x + {b:.1f}")

# Correlation coefficient
from scipy.stats import pearsonr
r, p = pearsonr(bmi, sbp)
ax.set_xlabel("BMI (kg/m²)")
ax.set_ylabel("Systolic BP (mmHg)")
ax.set_title(f"BMI vs Systolic BP (r={r:.2f}, p<0.001, n={n})")
ax.legend()
plt.tight_layout()
plt.show()

# ============================================================
# 8. Kaplan-Meier survival curves
# ============================================================

try:
    from lifelines import KaplanMeierFitter

    np.random.seed(42)
    n_per_group = 100

    # Treatment group: longer survival
    treatment_time = np.random.exponential(24, n_per_group).clip(0, 60)
    treatment_event = np.random.binomial(1, 0.7, n_per_group)

    # Control group: shorter survival
    control_time = np.random.exponential(15, n_per_group).clip(0, 60)
    control_event = np.random.binomial(1, 0.8, n_per_group)

    fig, ax = plt.subplots(figsize=(10, 6))

    kmf_treatment = KaplanMeierFitter()
    kmf_treatment.fit(treatment_time, event_observed=treatment_event,
                      label="Treatment (n=100)")
    kmf_treatment.plot_survival_function(ax=ax, ci_show=True)

    kmf_control = KaplanMeierFitter()
    kmf_control.fit(control_time, event_observed=control_event,
                    label="Control (n=100)")
    kmf_control.plot_survival_function(ax=ax, ci_show=True)

    ax.set_xlabel("Time (months)")
    ax.set_ylabel("Survival probability")
    ax.set_title("Kaplan-Meier survival curves by treatment group")
    ax.set_ylim(0, 1.05)

    for kmf, color in [(kmf_treatment, "#0072B2"), (kmf_control, "#D55E00")]:
        median = kmf.median_survival_time_
        if not np.isinf(median):
            ax.axhline(0.5, color="gray", linestyle=":", alpha=0.5)
            ax.axvline(median, color=color, linestyle=":", alpha=0.5)

    plt.tight_layout()
    plt.show()

    print(f"Median survival (treatment): "
          f"{kmf_treatment.median_survival_time_:.1f} months")
    print(f"Median survival (control): "
          f"{kmf_control.median_survival_time_:.1f} months")
except ImportError:
    print("lifelines not installed. Run: pip install lifelines")

# ============================================================
# 9. Heatmaps: correlation matrix
# ============================================================

np.random.seed(42)
n = 300
health = pd.DataFrame({
    "BMI": np.random.normal(27, 5, n),
    "Systolic_BP": np.random.normal(130, 18, n),
    "Diastolic_BP": np.random.normal(82, 10, n),
    "Glucose": np.random.normal(105, 25, n),
    "Cholesterol": np.random.normal(200, 40, n),
    "HbA1c": np.random.normal(5.8, 1.2, n),
    "Heart_Rate": np.random.normal(72, 12, n),
    "Age": np.random.normal(55, 15, n).clip(18, 90)
})

# Add realistic correlations
health["Systolic_BP"] += 0.8 * health["BMI"]
health["Glucose"] += 15 * health["HbA1c"]
health["Diastolic_BP"] += 0.4 * health["Systolic_BP"]
health["Cholesterol"] += 0.5 * health["BMI"]

corr = health.corr()

fig, ax = plt.subplots(figsize=(9, 8))
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt=".2f",
            cmap="RdBu_r", center=0, vmin=-1, vmax=1,
            square=True, ax=ax)
ax.set_title("Correlation matrix of health indicators")
plt.tight_layout()
plt.show()

# ============================================================
# 10. Heatmap: disease co-occurrence
# ============================================================

conditions = ["Hypertension", "Diabetes", "COPD",
              "Heart Failure", "CKD", "Obesity"]
np.random.seed(42)
cooccurrence = np.random.randint(5, 60, (6, 6))
cooccurrence = (cooccurrence + cooccurrence.T) // 2
np.fill_diagonal(cooccurrence, [320, 180, 95, 75, 110, 210])

co_df = pd.DataFrame(cooccurrence,
                     index=conditions, columns=conditions)

fig, ax = plt.subplots(figsize=(9, 8))
sns.heatmap(co_df, annot=True, fmt="d", cmap="YlOrRd",
            square=True, ax=ax)
ax.set_title("Disease co-occurrence matrix\n"
             "(diagonal = total cases, off-diagonal = co-occurring)")
plt.tight_layout()
plt.show()

# ============================================================
# 11. Practical: 4-panel health dashboard
# ============================================================

sns.set_theme(style="whitegrid", font_scale=1.0)

url = ("https://raw.githubusercontent.com/datasets/"
       "gapminder/main/data/gapminder.csv")
df = pd.read_csv(url)
recent = df[df["year"] == 2007].copy()

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Global Health Dashboard, 2007",
             fontsize=16, fontweight="bold", y=1.02)

# Panel A: Life expectancy by continent
ax = axes[0, 0]
sns.boxplot(data=recent, x="continent", y="lifeExp", ax=ax,
            palette="Set2")
ax.set_xlabel("")
ax.set_ylabel("Life expectancy (years)")
ax.set_title("A. Life expectancy by continent")
ax.tick_params(axis="x", rotation=30)

# Panel B: GDP vs Life expectancy scatter
ax = axes[0, 1]
for continent in recent["continent"].unique():
    subset = recent[recent["continent"] == continent]
    ax.scatter(subset["gdpPercap"], subset["lifeExp"],
               s=subset["pop"] / 2e6, alpha=0.6,
               label=continent)
ax.set_xscale("log")
ax.set_xlabel("GDP per capita (USD, log scale)")
ax.set_ylabel("Life expectancy (years)")
ax.set_title("B. Wealth vs health")
ax.legend(fontsize=8, title="Continent", title_fontsize=8)

# Panel C: Life expectancy trends
ax = axes[1, 0]
trend = df.groupby(["year", "continent"])["lifeExp"].mean().reset_index()
for continent in trend["continent"].unique():
    subset = trend[trend["continent"] == continent]
    ax.plot(subset["year"], subset["lifeExp"],
            marker="o", markersize=3, label=continent)
ax.set_xlabel("Year")
ax.set_ylabel("Mean life expectancy (years)")
ax.set_title("C. Life expectancy trends, 1952-2007")
ax.legend(fontsize=8, title="Continent", title_fontsize=8)

# Panel D: Bottom 10 countries
ax = axes[1, 1]
bottom10 = recent.nsmallest(10, "lifeExp")
ax.barh(bottom10["country"], bottom10["lifeExp"], color="#D55E00")
ax.set_xlabel("Life expectancy (years)")
ax.set_title("D. 10 lowest life expectancy countries")
ax.invert_yaxis()
for i, v in enumerate(bottom10["lifeExp"]):
    ax.text(v + 0.3, i, f"{v:.1f}", va="center", fontsize=8)

plt.tight_layout()
plt.savefig("health_dashboard_2007.png", dpi=150, bbox_inches="tight")
plt.show()
print("Dashboard saved as health_dashboard_2007.png")
