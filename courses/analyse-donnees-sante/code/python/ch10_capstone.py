"""
Chapter 10: Capstone project
Data Analysis with Python for Health Specialists

Run in Jupyter notebook or Google Colab.
This script demonstrates the starter code for each of the 5 suggested
capstone projects. Students should choose one and expand it into a
full analysis with report and presentation.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# Project 1: Diabetes risk factor analysis
# ============================================================

print("=" * 60)
print("PROJECT 1: Diabetes risk factor analysis")
print("=" * 60)

# Load Pima Indians Diabetes dataset
url = ("https://raw.githubusercontent.com/jbrownlee/Datasets/"
       "master/pima-indians-diabetes.data.csv")
columns = ["pregnancies", "glucose", "blood_pressure", "skin_thickness",
           "insulin", "bmi", "diabetes_pedigree", "age", "outcome"]
pima = pd.read_csv(url, names=columns)

print(f"Shape: {pima.shape}")
print(f"Diabetes prevalence: {pima['outcome'].mean():.1%}")

# Handle zeros in glucose, blood pressure, BMI (missing values coded as 0)
zero_cols = ["glucose", "blood_pressure", "bmi", "skin_thickness", "insulin"]
pima[zero_cols] = pima[zero_cols].replace(0, np.nan)
print(f"\nMissing after replacing zeros:")
print(pima.isnull().sum())

# Drop rows with missing values
pima_clean = pima.dropna()
print(f"\nClean dataset: {pima_clean.shape[0]} patients")

# Exploratory: distributions by diabetes status
print(pima_clean.groupby("outcome")[["glucose", "bmi", "age"]].mean().round(1))

# Correlation heatmap
fig, ax = plt.subplots(figsize=(8, 7))
sns.heatmap(pima_clean.corr(), annot=True, fmt=".2f", cmap="RdBu_r",
            center=0, ax=ax)
ax.set_title("Correlation heatmap: Pima diabetes features")
plt.tight_layout()
plt.show()

# Logistic regression
import statsmodels.api as sm

X = sm.add_constant(pima_clean[["glucose", "bmi", "age", "diabetes_pedigree"]])
y = pima_clean["outcome"]
logit = sm.Logit(y, X).fit()

# Odds ratios
or_df = pd.DataFrame({
    "OR": np.exp(logit.params),
    "95% CI low": np.exp(logit.conf_int()[0]),
    "95% CI high": np.exp(logit.conf_int()[1]),
    "p-value": logit.pvalues
}).round(4)
print("\nOdds ratios:")
print(or_df)

# Model comparison: logistic regression vs random forest
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, classification_report

features = ["glucose", "bmi", "age", "diabetes_pedigree",
            "pregnancies", "blood_pressure"]
X = pima_clean[features]
y = pima_clean["outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

lr = LogisticRegression(max_iter=1000, random_state=42)
rf = RandomForestClassifier(n_estimators=200, max_depth=6, random_state=42)

for name, model in [("Logistic Regression", lr), ("Random Forest", rf)]:
    model.fit(X_train, y_train)
    y_prob = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, y_prob)
    cv = cross_val_score(model, X, y, cv=5, scoring="roc_auc")
    print(f"\n{name}: AUC={auc:.3f}, CV AUC={cv.mean():.3f} +/- {cv.std():.3f}")

# ============================================================
# Project 2: COVID-19 impact analysis (starter)
# ============================================================

print("\n" + "=" * 60)
print("PROJECT 2: COVID-19 impact analysis across African countries")
print("=" * 60)

# Load JHU CSSE COVID-19 data
jhu_url = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/"
           "master/csse_covid_19_data/csse_covid_19_time_series/"
           "time_series_covid19_confirmed_global.csv")
confirmed = pd.read_csv(jhu_url)
print(f"JHU confirmed cases shape: {confirmed.shape}")

# Select African countries
african_countries = ["South Africa", "Nigeria", "Kenya", "Egypt", "Morocco",
                     "Ethiopia", "Ghana", "Senegal", "Rwanda", "Tanzania"]
africa_covid = confirmed[confirmed["Country/Region"].isin(african_countries)]
africa_covid = africa_covid.groupby("Country/Region").sum(numeric_only=True)
africa_covid = africa_covid.drop(columns=["Lat", "Long"], errors="ignore")

# Reshape and compute daily cases
africa_long = africa_covid.T
africa_long.index = pd.to_datetime(africa_long.index)

daily = africa_long.diff().clip(lower=0)
daily_7d = daily.rolling(7).mean()

# Total cases per country
totals = africa_long.iloc[-1].sort_values(ascending=False)
print("\nTotal confirmed cases:")
print(totals)

# OWID comprehensive dataset
owid_url = ("https://raw.githubusercontent.com/owid/covid-19-data/"
            "master/public/data/owid-covid-data.csv")
print(f"\nOWID data URL: {owid_url}")
print("Load with: pd.read_csv(owid_url)")

# ============================================================
# Project 3: Maternal mortality determinants (starter)
# ============================================================

print("\n" + "=" * 60)
print("PROJECT 3: Maternal mortality determinants")
print("=" * 60)

print("Datasets:")
print("  WHO GHO - Maternal mortality ratio:")
print("    https://apps.who.int/gho/athena/api/GHO/MDG_0000000026?format=csv")
print("  WHO GHO - Skilled birth attendance:")
print("    https://apps.who.int/gho/athena/api/GHO/MDG_0000000025?format=csv")
print("  WHO GHO - Antenatal care coverage:")
print("    https://apps.who.int/gho/athena/api/GHO/WHS4_154?format=csv")
print("  World Bank - GDP, health expenditure:")
print("    https://data.worldbank.org/")

# Simulated demonstration
np.random.seed(42)
n_countries = 50
mmr_data = pd.DataFrame({
    "country": [f"Country_{i}" for i in range(n_countries)],
    "mmr": np.random.exponential(200, n_countries).clip(10, 1500),
    "skilled_birth_pct": np.random.uniform(20, 99, n_countries),
    "anc4_coverage": np.random.uniform(15, 95, n_countries),
    "health_exp_pc": np.random.exponential(200, n_countries),
    "gdp_pc": np.random.exponential(5000, n_countries),
})

# Correlations
print(f"\nSimulated MMR data ({n_countries} countries):")
print(mmr_data[["mmr", "skilled_birth_pct", "health_exp_pc"]].describe().round(1))

from scipy.stats import pearsonr, spearmanr
r_sba, p_sba = spearmanr(mmr_data["mmr"], mmr_data["skilled_birth_pct"])
r_exp, p_exp = spearmanr(mmr_data["mmr"], mmr_data["health_exp_pc"])
print(f"\nSpearman correlations with MMR:")
print(f"  Skilled birth attendance: r={r_sba:.3f} (p={p_sba:.4f})")
print(f"  Health expenditure:       r={r_exp:.3f} (p={p_exp:.4f})")

# ============================================================
# Project 4: Heart disease prediction (starter)
# ============================================================

print("\n" + "=" * 60)
print("PROJECT 4: Heart disease prediction model comparison")
print("=" * 60)

heart_url = ("https://raw.githubusercontent.com/raphaelfontenelle/"
             "heart-disease-uci/main/heart.csv")
heart = pd.read_csv(heart_url)
print(f"Shape: {heart.shape}")
print(f"Heart disease prevalence: {heart['target'].mean():.1%}")

feature_cols = ["age", "sex", "cp", "trestbps", "chol", "fbs",
                "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
X = heart[feature_cols]
y = heart["target"]

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

models_to_compare = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Decision Tree": DecisionTreeClassifier(max_depth=4, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=200, max_depth=6,
                                             random_state=42),
    "KNN": KNeighborsClassifier(n_neighbors=7),
}

print("\n5-fold CV comparison:")
for name, model in models_to_compare.items():
    acc = cross_val_score(model, X, y, cv=5, scoring="accuracy")
    auc = cross_val_score(model, X, y, cv=5, scoring="roc_auc")
    print(f"  {name:25s}: Accuracy={acc.mean():.3f}, AUC={auc.mean():.3f}")

# ============================================================
# Project 5: Malaria burden and interventions (starter)
# ============================================================

print("\n" + "=" * 60)
print("PROJECT 5: Malaria burden and intervention effectiveness")
print("=" * 60)

print("Datasets:")
print("  WHO GHO - Malaria incidence:")
print("    https://apps.who.int/gho/athena/api/GHO/MALARIA_INCIDENCE?format=csv")
print("  WHO GHO - Malaria mortality:")
print("    https://apps.who.int/gho/athena/api/GHO/MALARIA_DEATHS_PER100000?format=csv")
print("  Malaria Atlas Project: https://malariaatlas.org/")

# Simulated malaria trend data
np.random.seed(42)
years = list(range(2000, 2023))
countries_mal = ["Nigeria", "DRC", "Mozambique", "Uganda", "Ghana",
                 "Tanzania", "Mali", "Burkina Faso", "Niger", "Cameroon"]

rows = []
for country in countries_mal:
    baseline = np.random.uniform(200, 500)
    for i, year in enumerate(years):
        # Simulated declining trend with noise
        incidence = baseline * (0.97 ** i) + np.random.normal(0, 20)
        rows.append({"country": country, "year": year,
                      "incidence_per_1000": max(0, incidence)})

malaria_trend = pd.DataFrame(rows)

# Plot trends for all countries
fig, ax = plt.subplots(figsize=(12, 6))
for country in countries_mal:
    subset = malaria_trend[malaria_trend["country"] == country]
    ax.plot(subset["year"], subset["incidence_per_1000"],
            marker=".", label=country)
ax.set_xlabel("Year")
ax.set_ylabel("Incidence per 1,000 population at risk")
ax.set_title("Malaria incidence trends (simulated), 2000-2022")
ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left", fontsize=8)
plt.tight_layout()
plt.show()

# Summary
recent_malaria = malaria_trend[malaria_trend["year"] == 2022]
print("\nMalaria incidence in 2022 (simulated):")
print(recent_malaria.sort_values("incidence_per_1000", ascending=False)
      [["country", "incidence_per_1000"]].to_string(index=False))

# ============================================================
# Getting started checklist
# ============================================================

print("\n" + "=" * 60)
print("GETTING STARTED CHECKLIST")
print("=" * 60)
print("""
1. Choose your project (1-5 or custom proposal)
2. Download your primary dataset and run .head(), .shape, .info(), .describe()
3. Write your research question in one sentence
4. List 3 visualizations you plan to create
5. List 1 statistical test or model you plan to use
6. Identify potential problems: missing data, messy columns, multiple files
7. Create a project folder:

   capstone_project/
       data/
           raw/          # original downloaded files
           cleaned/      # processed data
       notebooks/
           01_exploration.ipynb
           02_analysis.ipynb
       figures/
       report.pdf

8. Submit your project choice and research question to the instructor
""")

# Save figures as high-resolution PNGs for slides
# fig.savefig("figure1.png", dpi=300, bbox_inches="tight")
