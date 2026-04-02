"""
Chapter 4: Descriptive statistics and epidemiological measures
Data Analysis with Python for Health Specialists

Run in Jupyter notebook or Google Colab.
Datasets: Gapminder (life expectancy by country/year)
"""

import pandas as pd
import numpy as np
import math

# ============================================================
# 1. Central tendency: mean, median, mode
# ============================================================

# Fasting blood glucose for 10 patients (mg/dL)
glucose = pd.Series([92, 98, 104, 95, 88, 110, 97, 340, 101, 93])

print("=== Central tendency ===")
print(f"Mean:   {glucose.mean():.1f} mg/dL")
print(f"Median: {glucose.median():.1f} mg/dL")

# Mode for categorical data
diagnoses = pd.Series(["HTN", "T2DM", "HTN", "None", "HTN",
                       "T2DM", "None", "HTN", "COPD", "HTN"])
print(f"\nMost common diagnosis: {diagnoses.mode()[0]}")
print(f"Frequency: {diagnoses.value_counts().iloc[0]}/{len(diagnoses)}")

# ============================================================
# 2. Spread: standard deviation, IQR
# ============================================================

# Blood pressure readings from two clinics
clinic_a = pd.Series([120, 122, 118, 125, 121, 119, 123, 120])
clinic_b = pd.Series([98, 145, 110, 155, 102, 160, 115, 135])

print("\n=== Spread ===")
print(f"Clinic A: mean={clinic_a.mean():.1f}, SD={clinic_a.std():.1f}")
print(f"Clinic B: mean={clinic_b.mean():.1f}, SD={clinic_b.std():.1f}")

# IQR and percentiles
los = pd.Series([2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 12, 28, 45])

q25 = los.quantile(0.25)
q75 = los.quantile(0.75)
iqr = q75 - q25

print(f"\nMedian LOS: {los.median():.0f} days")
print(f"IQR: {q25:.0f}--{q75:.0f} days (range: {iqr:.0f})")
print(f"Mean LOS: {los.mean():.1f} days")  # inflated by 28 and 45

# ============================================================
# 3. Coefficient of variation
# ============================================================

glucose = pd.Series([95, 102, 88, 110, 97, 105, 92, 98])
hemoglobin = pd.Series([13.2, 14.1, 12.8, 13.5, 14.0, 13.8, 12.5, 13.9])

cv_glucose = (glucose.std() / glucose.mean()) * 100
cv_hb = (hemoglobin.std() / hemoglobin.mean()) * 100

print(f"\n=== Coefficient of variation ===")
print(f"CV glucose: {cv_glucose:.1f}%")
print(f"CV hemoglobin: {cv_hb:.1f}%")

# ============================================================
# 4. Frequency tables and cross-tabulations
# ============================================================

# Load Gapminder data
url = ("https://raw.githubusercontent.com/datasets/"
       "gapminder/main/data/gapminder.csv")
gapminder = pd.read_csv(url)
recent = gapminder[gapminder["year"] == 2007]

# Create life expectancy categories
recent = recent.copy()
recent["le_cat"] = pd.cut(recent["lifeExp"],
                          bins=[0, 55, 70, 85],
                          labels=["Low (<55)", "Medium (55-70)",
                                  "High (>70)"])

# Frequency table
freq = recent["le_cat"].value_counts().sort_index()
print("\n=== Frequency table ===")
print(freq)

# With proportions
freq_table = pd.DataFrame({
    "n": freq,
    "pct": (freq / freq.sum() * 100).round(1),
    "cum_pct": (freq.cumsum() / freq.sum() * 100).round(1)
})
print(freq_table)

# Cross-tabulate life expectancy category by continent
ct = pd.crosstab(recent["continent"], recent["le_cat"], margins=True)
print("\n=== Cross-tabulation ===")
print(ct)

# With row percentages
ct_pct = pd.crosstab(recent["continent"], recent["le_cat"],
                     normalize="index").round(3) * 100
print("\n=== Row percentages ===")
print(ct_pct)

# ============================================================
# 5. Prevalence
# ============================================================

from scipy import stats

n_total = 5000
n_diabetic = 625

prevalence = n_diabetic / n_total * 100
print(f"\n=== Prevalence ===")
print(f"Diabetes prevalence: {prevalence:.1f}%")

# With 95% confidence interval (normal approximation)
p = n_diabetic / n_total
se = np.sqrt(p * (1 - p) / n_total)
ci_low = (p - 1.96 * se) * 100
ci_high = (p + 1.96 * se) * 100
print(f"95% CI: [{ci_low:.1f}%, {ci_high:.1f}%]")

# ============================================================
# 6. Incidence rate
# ============================================================

new_tb_cases = 18
total_person_years = 850

incidence_rate = new_tb_cases / total_person_years
print(f"\n=== Incidence rate ===")
print(f"TB incidence rate: {incidence_rate:.4f} per person-year")
print(f"                 = {incidence_rate * 1000:.1f} per 1,000 person-years")

# 95% CI for incidence rate (Poisson approximation)
ir_se = np.sqrt(new_tb_cases) / total_person_years
ci_low = (incidence_rate - 1.96 * ir_se) * 1000
ci_high = (incidence_rate + 1.96 * ir_se) * 1000
print(f"95% CI: [{ci_low:.1f}, {ci_high:.1f}] per 1,000 person-years")

# ============================================================
# 7. Mortality rates
# ============================================================

# Crude mortality rate
deaths = 1250
population = 500_000
mortality_rate = deaths / population * 100_000
print(f"\n=== Mortality rates ===")
print(f"Crude mortality rate: {mortality_rate:.1f} per 100,000")

# Case fatality rate (CFR)
total_cases = 3200
deaths_among_cases = 128
cfr = deaths_among_cases / total_cases * 100
print(f"Case fatality rate: {cfr:.1f}%")

# ============================================================
# 8. Risk ratio (relative risk)
# ============================================================

# Smoking and lung cancer (hypothetical cohort)
a, b, c, d = 80, 920, 10, 990

risk_exposed = a / (a + b)
risk_unexposed = c / (c + d)
rr = risk_exposed / risk_unexposed

print(f"\n=== Risk ratio ===")
print(f"Risk in smokers:     {risk_exposed:.3f} ({risk_exposed*100:.1f}%)")
print(f"Risk in non-smokers: {risk_unexposed:.3f} ({risk_unexposed*100:.1f}%)")
print(f"Risk Ratio: {rr:.2f}")

# 95% CI for log(RR)
se_ln_rr = math.sqrt(1/a - 1/(a+b) + 1/c - 1/(c+d))
ln_rr = math.log(rr)
ci_low = math.exp(ln_rr - 1.96 * se_ln_rr)
ci_high = math.exp(ln_rr + 1.96 * se_ln_rr)
print(f"95% CI: [{ci_low:.2f}, {ci_high:.2f}]")

# ============================================================
# 9. Odds ratio
# ============================================================

# Case-control study: obesity and knee osteoarthritis
a, b, c, d = 120, 60, 80, 140

odds_ratio = (a * d) / (b * c)
print(f"\n=== Odds ratio ===")
print(f"Odds Ratio: {odds_ratio:.2f}")

se_ln_or = math.sqrt(1/a + 1/b + 1/c + 1/d)
ln_or = math.log(odds_ratio)
ci_low = math.exp(ln_or - 1.96 * se_ln_or)
ci_high = math.exp(ln_or + 1.96 * se_ln_or)
print(f"95% CI: [{ci_low:.2f}, {ci_high:.2f}]")

# ============================================================
# 10. Reusable functions
# ============================================================

def risk_ratio(a, b, c, d, alpha=0.05):
    """Compute risk ratio with confidence interval.

    a = exposed with disease
    b = exposed without disease
    c = unexposed with disease
    d = unexposed without disease
    """
    from scipy.stats import norm
    z = norm.ppf(1 - alpha / 2)

    rr = (a / (a + b)) / (c / (c + d))
    se = math.sqrt(1/a - 1/(a+b) + 1/c - 1/(c+d))
    ci = (math.exp(math.log(rr) - z * se),
          math.exp(math.log(rr) + z * se))

    return {"RR": round(rr, 3), "CI_low": round(ci[0], 3),
            "CI_high": round(ci[1], 3)}


def odds_ratio_fn(a, b, c, d, alpha=0.05):
    """Compute odds ratio with confidence interval."""
    from scipy.stats import norm
    z = norm.ppf(1 - alpha / 2)

    o_r = (a * d) / (b * c)
    se = math.sqrt(1/a + 1/b + 1/c + 1/d)
    ci = (math.exp(math.log(o_r) - z * se),
          math.exp(math.log(o_r) + z * se))

    return {"OR": round(o_r, 3), "CI_low": round(ci[0], 3),
            "CI_high": round(ci[1], 3)}


print("\n=== Reusable functions ===")
print(risk_ratio(80, 920, 10, 990))
print(odds_ratio_fn(120, 60, 80, 140))

# ============================================================
# 11. Age-standardized rates
# ============================================================

data_a = pd.DataFrame({
    "age_group": ["0-14", "15-44", "45-64", "65+"],
    "population": [50000, 80000, 40000, 10000],
    "deaths": [50, 80, 200, 300]
})
data_a["rate"] = data_a["deaths"] / data_a["population"] * 100000

data_b = pd.DataFrame({
    "age_group": ["0-14", "15-44", "45-64", "65+"],
    "population": [15000, 40000, 50000, 45000],
    "deaths": [20, 50, 280, 1500]
})
data_b["rate"] = data_b["deaths"] / data_b["population"] * 100000

# Standard population (WHO World Standard)
standard_pop = pd.DataFrame({
    "age_group": ["0-14", "15-44", "45-64", "65+"],
    "std_weight": [0.26, 0.42, 0.22, 0.10]
})

# Crude rates
crude_a = data_a["deaths"].sum() / data_a["population"].sum() * 100000
crude_b = data_b["deaths"].sum() / data_b["population"].sum() * 100000
print(f"\n=== Age standardization ===")
print(f"Crude rate Region A: {crude_a:.1f} per 100,000")
print(f"Crude rate Region B: {crude_b:.1f} per 100,000")

# Age-standardized rates
asr_a = (data_a["rate"] * standard_pop["std_weight"]).sum()
asr_b = (data_b["rate"] * standard_pop["std_weight"]).sum()
print(f"Age-standardized rate Region A: {asr_a:.1f} per 100,000")
print(f"Age-standardized rate Region B: {asr_b:.1f} per 100,000")

# ============================================================
# 12. Practical: descriptive stats on Gapminder
# ============================================================

from scipy import stats

url = ("https://raw.githubusercontent.com/datasets/"
       "gapminder/main/data/gapminder.csv")
df = pd.read_csv(url)

# Summary statistics by continent (2007)
recent = df[df["year"] == 2007].copy()
summary = recent.groupby("continent")["lifeExp"].agg(
    ["count", "mean", "median", "std",
     lambda x: x.quantile(0.25),
     lambda x: x.quantile(0.75)]
)
summary.columns = ["n", "mean", "median", "sd", "Q1", "Q3"]
print("\n=== Summary by continent (2007) ===")
print(summary.round(1))

# ============================================================
# 13. Malaria prevalence by region (simulated)
# ============================================================

np.random.seed(42)
countries = (["Nigeria", "DRC", "Mozambique", "Uganda", "Ghana"] * 3 +
             ["India", "Indonesia", "Myanmar", "Pakistan", "Ethiopia"] * 3)

malaria = pd.DataFrame({
    "country": countries,
    "region": ["West Africa", "Central Africa", "East Africa",
               "East Africa", "West Africa"] * 6,
    "year": [2018]*5 + [2019]*5 + [2020]*5 +
            [2018]*5 + [2019]*5 + [2020]*5,
    "population_at_risk": np.random.randint(10_000_000, 200_000_000, 30),
    "estimated_cases": np.random.randint(500_000, 50_000_000, 30)
})

# Compute prevalence per 1,000 population at risk
malaria["prevalence_per_1000"] = (
    malaria["estimated_cases"] / malaria["population_at_risk"] * 1000
)

# Summary by region
region_summary = malaria.groupby("region").agg(
    total_cases=("estimated_cases", "sum"),
    total_pop=("population_at_risk", "sum"),
    n_countries=("country", "nunique")
)
region_summary["prevalence_per_1000"] = (
    region_summary["total_cases"] / region_summary["total_pop"] * 1000
)
print("\n=== Malaria by region ===")
print(region_summary.round(1))

# Trend by year
year_trend = malaria.groupby("year").agg(
    total_cases=("estimated_cases", "sum"),
    total_pop=("population_at_risk", "sum")
)
year_trend["prevalence_per_1000"] = (
    year_trend["total_cases"] / year_trend["total_pop"] * 1000
)
print("\n=== Malaria trend by year ===")
print(year_trend.round(1))
