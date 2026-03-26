"""
Chapter 6: Applied Statistics
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# === Descriptive statistics ===
tips = sns.load_dataset('tips')
print("=== Descriptive Statistics ===")
print(f"Mean bill:   {tips['total_bill'].mean():.2f}")
print(f"Median bill: {tips['total_bill'].median():.2f}")
print(f"Std bill:    {tips['total_bill'].std():.2f}")
print(f"Q1, Q3:      {tips['total_bill'].quantile(0.25):.2f}, "
      f"{tips['total_bill'].quantile(0.75):.2f}")

# === Normal distribution ===
x = np.linspace(-4, 4, 200)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, stats.norm.pdf(x), 'b-', lw=2, label='N(0,1)')
ax.fill_between(x, stats.norm.pdf(x), where=(x >= -1.96) & (x <= 1.96),
                alpha=0.3, color='blue', label='95% CI')
ax.legend()
ax.set_title('Standard Normal Distribution')
plt.savefig('ch06_normal.pdf')
plt.show()

# === Confidence interval ===
sample = tips['total_bill']
n = len(sample)
mean = sample.mean()
se = sample.std() / np.sqrt(n)
ci_95 = stats.t.interval(0.95, df=n-1, loc=mean, scale=se)
print(f"\n=== Confidence Interval ===")
print(f"Mean: {mean:.2f}, SE: {se:.2f}")
print(f"95% CI: [{ci_95[0]:.2f}, {ci_95[1]:.2f}]")

# === t-test: male vs female tips ===
male_tips = tips[tips['sex'] == 'Male']['tip']
female_tips = tips[tips['sex'] == 'Female']['tip']
t_stat, p_value = stats.ttest_ind(male_tips, female_tips)
print(f"\n=== t-test: Male vs Female tips ===")
print(f"Male mean:   {male_tips.mean():.3f}")
print(f"Female mean: {female_tips.mean():.3f}")
print(f"t = {t_stat:.4f}, p = {p_value:.4f}")

# === Chi-squared test ===
titanic = sns.load_dataset('titanic')
ct = pd.crosstab(titanic['sex'], titanic['survived'])
chi2, p, dof, expected = stats.chi2_contingency(ct)
print(f"\n=== Chi-squared test: sex vs survival ===")
print(f"Contingency table:\n{ct}")
print(f"chi2 = {chi2:.2f}, p = {p:.2e}, dof = {dof}")

# === Correlation ===
r, p_corr = stats.pearsonr(tips['total_bill'], tips['tip'])
rho, p_spear = stats.spearmanr(tips['total_bill'], tips['tip'])
print(f"\n=== Correlation (bill vs tip) ===")
print(f"Pearson:  r = {r:.4f}, p = {p_corr:.2e}")
print(f"Spearman: rho = {rho:.4f}, p = {p_spear:.2e}")

# === ANOVA ===
thur = tips[tips['day'] == 'Thur']['tip']
fri = tips[tips['day'] == 'Fri']['tip']
sat = tips[tips['day'] == 'Sat']['tip']
sun = tips[tips['day'] == 'Sun']['tip']
F_stat, p_anova = stats.f_oneway(thur, fri, sat, sun)
print(f"\n=== ANOVA: tip by day ===")
print(f"F = {F_stat:.4f}, p = {p_anova:.4f}")
