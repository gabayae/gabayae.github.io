"""
Chapter 7: Regression for health outcomes
Data Analysis with Python for Health Specialists

Run in Jupyter notebook or Google Colab.
Datasets: Pima Indians Diabetes (UCI), simulated clinical data
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ============================================================
# 1. Simple linear regression
# ============================================================

print("=== Simple linear regression ===")
np.random.seed(42)
n = 200
age = np.random.uniform(25, 80, n)
# True relationship: SBP = 90 + 0.7 * age + noise
sbp = 90 + 0.7 * age + np.random.normal(0, 12, n)

df = pd.DataFrame({"age": age, "systolic_bp": sbp})

# Fit with scipy
slope, intercept, r_value, p_value, std_err = stats.linregress(
    df["age"], df["systolic_bp"])
print(f"Intercept: {intercept:.2f}")
print(f"Slope: {slope:.2f} mmHg per year of age")
print(f"R-squared: {r_value**2:.3f}")
print(f"p-value: {p_value:.2e}")

# Visualize
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(df["age"], df["systolic_bp"], alpha=0.5, s=20, color="steelblue")
x_line = np.linspace(25, 80, 100)
ax.plot(x_line, intercept + slope * x_line, color="red", linewidth=2,
        label=f"SBP = {intercept:.1f} + {slope:.2f} x Age")
ax.set_xlabel("Age (years)")
ax.set_ylabel("Systolic BP (mmHg)")
ax.set_title("Simple linear regression: SBP vs Age")
ax.legend()
plt.tight_layout()
plt.show()

# ============================================================
# 2. Multiple linear regression
# ============================================================

import statsmodels.api as sm

print("\n=== Multiple linear regression ===")
np.random.seed(42)
n = 300
age = np.random.uniform(25, 80, n)
bmi = np.random.normal(27, 5, n)
smoking = np.random.binomial(1, 0.25, n)
# True model: SBP = 70 + 0.6*age + 0.8*BMI + 5*smoking + noise
sbp = 70 + 0.6 * age + 0.8 * bmi + 5 * smoking + np.random.normal(0, 10, n)

df = pd.DataFrame({
    "age": age, "bmi": bmi, "smoking": smoking, "systolic_bp": sbp
})

# Fit multiple regression with statsmodels
X = sm.add_constant(df[["age", "bmi", "smoking"]])
model = sm.OLS(df["systolic_bp"], X).fit()
print(model.summary())

# ============================================================
# 3. Interpreting coefficients
# ============================================================

print("\n=== Coefficients ===")
coef_df = pd.DataFrame({
    "Coefficient": model.params,
    "95% CI lower": model.conf_int()[0],
    "95% CI upper": model.conf_int()[1],
    "p-value": model.pvalues
}).round(4)
print(coef_df)

# ============================================================
# 4. Confounders
# ============================================================

print("\n=== Confounders: coffee and heart disease ===")
np.random.seed(42)
n = 500
smoking = np.random.binomial(1, 0.3, n)
coffee = 1.5 + 2 * smoking + np.random.normal(0, 1.5, n)
heart_disease_risk = 0.5 * smoking + np.random.normal(0, 0.3, n)

# Unadjusted
r_unadjusted, p_unadjusted = stats.pearsonr(coffee, heart_disease_risk)
print(f"Unadjusted correlation (coffee vs HD risk): r = {r_unadjusted:.3f}, p = {p_unadjusted:.4f}")

# Adjusted regression
df_conf = pd.DataFrame({"coffee": coffee, "smoking": smoking,
                         "hd_risk": heart_disease_risk})
X = sm.add_constant(df_conf[["coffee", "smoking"]])
model_adj = sm.OLS(df_conf["hd_risk"], X).fit()
print(f"\nAdjusted model:")
print(f"  Coffee coefficient: {model_adj.params['coffee']:.4f} "
      f"(p = {model_adj.pvalues['coffee']:.4f})")
print(f"  Smoking coefficient: {model_adj.params['smoking']:.4f} "
      f"(p = {model_adj.pvalues['smoking']:.4f})")

# ============================================================
# 5. Checking regression assumptions
# ============================================================

print("\n=== Residual diagnostics ===")
# Refit SBP model for diagnostics
X = sm.add_constant(df[["age", "bmi", "smoking"]])
model = sm.OLS(df["systolic_bp"], X).fit()
residuals = model.resid
fitted = model.fittedvalues

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Residuals vs fitted
axes[0].scatter(fitted, residuals, alpha=0.4, s=15)
axes[0].axhline(0, color="red", linestyle="--")
axes[0].set_xlabel("Fitted values")
axes[0].set_ylabel("Residuals")
axes[0].set_title("Residuals vs Fitted")

# Histogram of residuals
axes[1].hist(residuals, bins=25, edgecolor="black", alpha=0.7)
axes[1].set_xlabel("Residuals")
axes[1].set_title("Distribution of residuals")

# Q-Q plot
stats.probplot(residuals, dist="norm", plot=axes[2])
axes[2].set_title("Q-Q plot")

plt.tight_layout()
plt.show()

# ============================================================
# 6. Logistic regression
# ============================================================

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

print("\n=== Logistic regression: Pima diabetes ===")
url = ("https://raw.githubusercontent.com/jbrownlee/Datasets/"
       "master/pima-indians-diabetes.data.csv")
columns = ["pregnancies", "glucose", "blood_pressure", "skin_thickness",
           "insulin", "bmi", "diabetes_pedigree", "age", "outcome"]
pima = pd.read_csv(url, names=columns)
print(f"Shape: {pima.shape}")
print(f"Diabetes prevalence: {pima['outcome'].mean():.1%}")
print(pima.head())

# Fit logistic regression with statsmodels
X = sm.add_constant(pima[["age", "bmi", "glucose"]])
y = pima["outcome"]

logit_model = sm.Logit(y, X).fit()
print(logit_model.summary())

# ============================================================
# 7. Odds ratios from logistic regression
# ============================================================

print("\n=== Odds ratios ===")
odds_ratios = np.exp(logit_model.params)
ci = np.exp(logit_model.conf_int())

or_df = pd.DataFrame({
    "Odds Ratio": odds_ratios,
    "95% CI lower": ci[0],
    "95% CI upper": ci[1],
    "p-value": logit_model.pvalues
}).round(4)
print(or_df)

# ============================================================
# 8. Model evaluation: confusion matrix
# ============================================================

print("\n=== Model evaluation ===")
features = ["age", "bmi", "glucose"]
X = pima[features]
y = pima["outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

clf = LogisticRegression(max_iter=1000, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
print()

print(classification_report(y_test, y_pred,
                            target_names=["No Diabetes", "Diabetes"]))

# ============================================================
# 9. Sensitivity, specificity, PPV, NPV
# ============================================================

print("=== Diagnostic metrics ===")
tn, fp, fn, tp = cm.ravel()
sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)
ppv = tp / (tp + fp)
npv = tn / (tn + fn)

print(f"Sensitivity (recall): {sensitivity:.3f}")
print(f"  -> Of those WITH diabetes, {sensitivity:.1%} were correctly identified")
print(f"Specificity:          {specificity:.3f}")
print(f"  -> Of those WITHOUT diabetes, {specificity:.1%} were correctly identified")
print(f"PPV (precision):      {ppv:.3f}")
print(f"  -> Of those PREDICTED positive, {ppv:.1%} actually have diabetes")
print(f"NPV:                  {npv:.3f}")
print(f"  -> Of those PREDICTED negative, {npv:.1%} are truly disease-free")

# Visualize confusion matrix
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["No Diabetes", "Diabetes"],
            yticklabels=["No Diabetes", "Diabetes"], ax=ax)
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
ax.set_title("Confusion Matrix")
plt.tight_layout()
plt.show()

# ============================================================
# 10. Survival analysis: Kaplan-Meier and Cox model
# ============================================================

try:
    from lifelines import KaplanMeierFitter, CoxPHFitter

    print("\n=== Survival analysis ===")
    np.random.seed(42)
    n = 200
    treatment = np.random.binomial(1, 0.5, n)
    time = np.where(treatment == 1,
                    np.random.exponential(24, n),
                    np.random.exponential(16, n))
    event = np.random.binomial(1, 0.75, n)

    surv_df = pd.DataFrame({
        "time": time, "event": event, "treatment": treatment
    })

    # Kaplan-Meier curves
    fig, ax = plt.subplots(figsize=(8, 5))

    for label, group_df in surv_df.groupby("treatment"):
        kmf = KaplanMeierFitter()
        kmf.fit(group_df["time"], event_observed=group_df["event"],
                label="Treatment" if label == 1 else "Control")
        kmf.plot_survival_function(ax=ax)

    ax.set_xlabel("Time (months)")
    ax.set_ylabel("Survival probability")
    ax.set_title("Kaplan-Meier survival curves")
    plt.tight_layout()
    plt.show()

    # Cox proportional hazards
    cph = CoxPHFitter()
    cph.fit(surv_df, duration_col="time", event_col="event",
            formula="treatment")
    cph.print_summary()

    # Hazard ratio
    hr = np.exp(cph.params_["treatment"])
    print(f"\nHazard ratio for treatment: {hr:.3f}")
    if hr < 1:
        print(f"Treatment reduces hazard by {(1-hr)*100:.1f}%")
    else:
        print(f"Treatment increases hazard by {(hr-1)*100:.1f}%")
except ImportError:
    print("\nlifelines not installed. Run: pip install lifelines")
