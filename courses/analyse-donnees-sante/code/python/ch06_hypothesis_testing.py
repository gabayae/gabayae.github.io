"""
Chapter 6: Hypothesis testing
Data Analysis with Python for Health Specialists

Run in Jupyter notebook or Google Colab.
Datasets: Framingham Heart Study (cardiovascular risk factors)
"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# 1. Visualizing the logic of hypothesis testing
# ============================================================

np.random.seed(42)
null_distribution = np.random.normal(loc=0, scale=1, size=10000)

fig, ax = plt.subplots(figsize=(9, 4))
ax.hist(null_distribution, bins=60, density=True, alpha=0.7, color="steelblue")
ax.axvline(1.96, color="red", linestyle="--", label="Critical value (alpha=0.05)")
ax.axvline(-1.96, color="red", linestyle="--")
ax.fill_betweenx([0, 0.45], 1.96, 3.5, alpha=0.3, color="red", label="Rejection region")
ax.fill_betweenx([0, 0.45], -3.5, -1.96, alpha=0.3, color="red")
ax.set_xlabel("Test statistic (z)")
ax.set_ylabel("Density")
ax.set_title("Two-tailed test: rejection regions under H0")
ax.legend()
plt.tight_layout()
plt.show()

# ============================================================
# 2. One-sample t-test
# ============================================================

print("=== One-sample t-test ===")
np.random.seed(42)
cholesterol = np.random.normal(loc=212, scale=35, size=80)

# Is the mean different from 200?
t_stat, p_value = stats.ttest_1samp(cholesterol, popmean=200)
print(f"Sample mean: {cholesterol.mean():.1f} mg/dL")
print(f"t-statistic: {t_stat:.3f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Reject H0: mean cholesterol differs from 200 mg/dL")
else:
    print("Fail to reject H0: no evidence mean differs from 200 mg/dL")

# ============================================================
# 3. Two-sample t-test
# ============================================================

print("\n=== Two-sample t-test ===")
np.random.seed(42)
treatment = np.random.normal(loc=128, scale=15, size=60)
control = np.random.normal(loc=138, scale=16, size=55)

t_stat, p_value = stats.ttest_ind(treatment, control)
print(f"Treatment mean: {treatment.mean():.1f} mmHg")
print(f"Control mean:   {control.mean():.1f} mmHg")
print(f"Difference:     {control.mean() - treatment.mean():.1f} mmHg")
print(f"t-statistic:    {t_stat:.3f}")
print(f"p-value:        {p_value:.4f}")

# ============================================================
# 4. Checking assumptions
# ============================================================

print("\n=== Checking assumptions ===")

# Normality: Shapiro-Wilk test
_, p_treat = stats.shapiro(treatment)
_, p_ctrl = stats.shapiro(control)
print(f"Shapiro-Wilk p (treatment): {p_treat:.4f}")
print(f"Shapiro-Wilk p (control):   {p_ctrl:.4f}")

# Equal variances: Levene's test
_, p_levene = stats.levene(treatment, control)
print(f"Levene's test p: {p_levene:.4f}")

# Welch's t-test (does not assume equal variances)
t_stat, p_value = stats.ttest_ind(treatment, control, equal_var=False)
print(f"Welch's t-test p-value: {p_value:.4f}")

# ============================================================
# 5. Paired t-test
# ============================================================

print("\n=== Paired t-test ===")
np.random.seed(42)
n_patients = 45
bp_before = np.random.normal(loc=142, scale=12, size=n_patients)
bp_after = bp_before - np.random.normal(loc=8, scale=6, size=n_patients)

t_stat, p_value = stats.ttest_rel(bp_before, bp_after)
differences = bp_before - bp_after
print(f"Mean BP before:     {bp_before.mean():.1f} mmHg")
print(f"Mean BP after:      {bp_after.mean():.1f} mmHg")
print(f"Mean reduction:     {differences.mean():.1f} mmHg")
print(f"t-statistic:        {t_stat:.3f}")
print(f"p-value:            {p_value:.6f}")

# Visualize before/after
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for i in range(n_patients):
    axes[0].plot([0, 1], [bp_before[i], bp_after[i]],
                 color="gray", alpha=0.4)
axes[0].plot([0, 1], [bp_before.mean(), bp_after.mean()],
             color="red", linewidth=3, marker="o", markersize=8)
axes[0].set_xticks([0, 1])
axes[0].set_xticklabels(["Before", "After"])
axes[0].set_ylabel("Systolic BP (mmHg)")
axes[0].set_title("Individual patient trajectories")

axes[1].hist(differences, bins=15, edgecolor="black", alpha=0.7, color="steelblue")
axes[1].axvline(0, color="red", linestyle="--", label="No change")
axes[1].axvline(differences.mean(), color="green", linestyle="--",
                label=f"Mean = {differences.mean():.1f}")
axes[1].set_xlabel("BP reduction (mmHg)")
axes[1].set_ylabel("Frequency")
axes[1].set_title("Distribution of BP changes")
axes[1].legend()

plt.tight_layout()
plt.show()

# ============================================================
# 6. Chi-square test of independence
# ============================================================

print("\n=== Chi-square test ===")
np.random.seed(42)
n = 500
bmi_cat = np.random.choice(["Normal", "Overweight", "Obese"],
                           size=n, p=[0.3, 0.4, 0.3])
diabetes_prob = {"Normal": 0.08, "Overweight": 0.18, "Obese": 0.35}
diabetes = [np.random.binomial(1, diabetes_prob[b]) for b in bmi_cat]

df_chi = pd.DataFrame({"bmi_category": bmi_cat, "diabetes": diabetes})
df_chi["diabetes_label"] = df_chi["diabetes"].map({0: "No", 1: "Yes"})

contingency = pd.crosstab(df_chi["bmi_category"], df_chi["diabetes_label"])
print(contingency)
print()

chi2, p_value, dof, expected = stats.chi2_contingency(contingency)
print(f"Chi-square statistic: {chi2:.2f}")
print(f"Degrees of freedom:   {dof}")
print(f"p-value:              {p_value:.4f}")
print(f"\nExpected frequencies (if independent):")
print(pd.DataFrame(expected, index=contingency.index,
                   columns=contingency.columns).round(1))

# ============================================================
# 7. Mann-Whitney U test
# ============================================================

print("\n=== Mann-Whitney U test ===")
np.random.seed(42)
los_surgical = np.random.exponential(scale=7, size=40)
los_medical = np.random.exponential(scale=4.5, size=45)

u_stat, p_value = stats.mannwhitneyu(los_surgical, los_medical,
                                      alternative="two-sided")
print(f"Median LOS (surgical): {np.median(los_surgical):.1f} days")
print(f"Median LOS (medical):  {np.median(los_medical):.1f} days")
print(f"U statistic:           {u_stat:.0f}")
print(f"p-value:               {p_value:.4f}")

fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(los_surgical, bins=15, alpha=0.6, label="Surgical", color="coral")
ax.hist(los_medical, bins=15, alpha=0.6, label="Medical", color="steelblue")
ax.set_xlabel("Length of stay (days)")
ax.set_ylabel("Frequency")
ax.set_title("Hospital length of stay by department")
ax.legend()
plt.tight_layout()
plt.show()

# ============================================================
# 8. Multiple testing correction
# ============================================================

print("\n=== Multiple testing ===")
np.random.seed(42)
n_tests = 1000
p_values = []
for _ in range(n_tests):
    a = np.random.normal(0, 1, 30)
    b = np.random.normal(0, 1, 30)
    _, p = stats.ttest_ind(a, b)
    p_values.append(p)

p_values = np.array(p_values)
false_positives = (p_values < 0.05).sum()
print(f"Tests performed: {n_tests}")
print(f"False positives (p < 0.05): {false_positives}")
print(f"False positive rate: {false_positives/n_tests:.1%}")

from statsmodels.stats.multitest import multipletests

# Bonferroni correction
rejected_bonf, pvals_corrected_bonf, _, _ = multipletests(
    p_values, alpha=0.05, method="bonferroni"
)
print(f"Bonferroni: {rejected_bonf.sum()} significant results")

# Benjamini-Hochberg FDR correction
rejected_fdr, pvals_corrected_fdr, _, _ = multipletests(
    p_values, alpha=0.05, method="fdr_bh"
)
print(f"FDR (BH): {rejected_fdr.sum()} significant results")

# ============================================================
# 9. Effect size: Cohen's d
# ============================================================

print("\n=== Effect size ===")

def cohens_d(group1, group2):
    """Compute Cohen's d for two independent groups."""
    n1, n2 = len(group1), len(group2)
    var1, var2 = group1.var(ddof=1), group2.var(ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    return (group1.mean() - group2.mean()) / pooled_std

d = cohens_d(treatment, control)
print(f"Cohen's d: {d:.2f}")
print(f"Interpretation: {'large' if abs(d) >= 0.8 else 'medium' if abs(d) >= 0.5 else 'small' if abs(d) >= 0.2 else 'negligible'} effect")

# Large sample + tiny effect = significant p-value
np.random.seed(42)
huge_group1 = np.random.normal(120.0, 15, size=50000)
huge_group2 = np.random.normal(120.5, 15, size=50000)

t, p = stats.ttest_ind(huge_group1, huge_group2)
d = cohens_d(huge_group1, huge_group2)
print(f"\nMean difference: {huge_group2.mean() - huge_group1.mean():.2f} mmHg")
print(f"p-value: {p:.6f}")
print(f"Cohen's d: {d:.3f}")
print("Statistically significant? Yes. Clinically meaningful? No.")

# ============================================================
# 10. Practical: Framingham-style data
# ============================================================

print("\n=== Framingham dataset ===")
url = ("https://raw.githubusercontent.com/dsrscientist/"
       "dataset-for-machine-learning/master/framingham.csv")
fram = pd.read_csv(url)
print(f"Shape: {fram.shape}")
print(f"Columns: {fram.columns.tolist()}")
print(fram.head())
print(fram.describe())

# Drop rows with missing values for simplicity
fram_clean = fram.dropna()
print(f"\nClean dataset: {fram_clean.shape[0]} patients")
