"""
Chapter 7: Classical Tests z, t, chi2, F
"""
import numpy as np
from scipy import stats

# --- One-sample t-test ---
data = np.array([50.2, 49.8, 51.1, 48.9, 50.5, 49.3, 50.8, 49.1,
                 50.0, 49.7, 50.3, 49.5, 50.6, 49.2, 50.4])
t_stat, p_val = stats.ttest_1samp(data, 50)
print(f"One-sample t: t={t_stat:.4f}, p={p_val:.4f}")

# --- Two-sample t-test ---
np.random.seed(42)
A = np.random.normal(50, 1.5, 20)
B = np.random.normal(49.5, 2.1, 25)

t_eq, p_eq = stats.ttest_ind(A, B, equal_var=True)
print(f"Equal var t: t={t_eq:.4f}, p={p_eq:.4f}")

t_w, p_w = stats.ttest_ind(A, B, equal_var=False)
print(f"Welch t:     t={t_w:.4f}, p={p_w:.4f}")

# --- F-test ---
f_stat = np.var(A, ddof=1) / np.var(B, ddof=1)
df1, df2 = len(A)-1, len(B)-1
p_f = 2 * min(stats.f.cdf(f_stat, df1, df2), 1-stats.f.cdf(f_stat, df1, df2))
print(f"F-test: F={f_stat:.4f}, p={p_f:.4f}")

# --- Paired t-test ---
before = np.array([140, 135, 150, 145, 138, 142, 155, 148, 137, 143])
after = np.array([132, 130, 142, 138, 135, 136, 148, 140, 133, 138])
t_p, p_p = stats.ttest_rel(before, after)
print(f"Paired t: t={t_p:.4f}, p={p_p:.4f}")

# --- Chi-squared goodness of fit ---
obs = np.array([25, 17, 22, 18, 19, 19])
chi2, p_chi = stats.chisquare(obs)
print(f"Chi2 GoF: chi2={chi2:.4f}, p={p_chi:.4f}")

# --- Chi-squared independence ---
table = np.array([[30, 20, 10], [25, 30, 15], [15, 20, 35]])
chi2_ind, p_ind, dof, expected = stats.chi2_contingency(table)
print(f"Chi2 independence: chi2={chi2_ind:.4f}, p={p_ind:.4f}, dof={dof}")

# --- Proportion z-test ---
from statsmodels.stats.proportion import proportions_ztest
z_prop, p_prop = proportions_ztest(520, 1000, value=0.5)
print(f"Proportion z: z={z_prop:.4f}, p={p_prop:.4f}")
