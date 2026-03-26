"""
Chapter 11: Non-Parametric Methods
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42)

# --- Wilcoxon Signed-Rank ---
before = np.array([5.2, 4.8, 6.1, 5.5, 4.9, 5.8, 6.3, 5.1, 4.7, 5.4])
after = np.array([4.8, 4.2, 5.5, 5.0, 4.3, 5.1, 5.7, 4.5, 4.1, 4.9])
stat_w, p_w = stats.wilcoxon(before, after, alternative='greater')
print(f"Wilcoxon signed-rank: W={stat_w:.1f}, p={p_w:.4f}")

# --- Mann-Whitney ---
A = np.array([23, 25, 28, 30, 27, 24, 26, 29, 31, 22])
B = np.array([18, 20, 22, 19, 21, 17, 23, 20, 19, 18])
u_stat, p_mw = stats.mannwhitneyu(A, B, alternative='two-sided')
print(f"Mann-Whitney: U={u_stat:.1f}, p={p_mw:.4f}")

# --- Kruskal-Wallis ---
g1 = [6.4, 7.1, 6.8, 7.3, 6.9]
g2 = [8.2, 7.9, 8.5, 8.1, 8.4]
g3 = [5.5, 6.2, 5.8, 6.0, 5.7]
h_stat, p_kw = stats.kruskal(g1, g2, g3)
print(f"Kruskal-Wallis: H={h_stat:.4f}, p={p_kw:.4f}")

# --- Kolmogorov-Smirnov ---
data = np.random.exponential(2, 50)
ks_norm, p_norm = stats.kstest(data, 'norm', args=(np.mean(data), np.std(data)))
ks_exp, p_exp = stats.kstest(data, 'expon', args=(0, np.mean(data)))
print(f"KS (normality):     D={ks_norm:.4f}, p={p_norm:.4f}")
print(f"KS (exponential):   D={ks_exp:.4f}, p={p_exp:.4f}")

# --- KDE ---
data_kde = np.concatenate([np.random.normal(-2, 0.8, 100),
                           np.random.normal(2, 1.2, 150)])
x_grid = np.linspace(-6, 7, 300)

fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(data_kde, bins=30, density=True, alpha=0.3, label='Histogram')
for bw in [0.2, 0.5, 1.0]:
    kde = stats.gaussian_kde(data_kde, bw_method=bw)
    ax.plot(x_grid, kde(x_grid), lw=2, label=f'KDE h={bw}')
ax.set_title("Kernel Density Estimation")
ax.legend()
plt.savefig("ch11_kde.pdf")
plt.show()

# --- Spearman Correlation ---
x = np.arange(1, 11)
y = x**2
r_pearson, _ = stats.pearsonr(x, y)
r_spearman, p_sp = stats.spearmanr(x, y)
print(f"\nPearson:  r = {r_pearson:.4f}")
print(f"Spearman: r_s = {r_spearman:.4f}, p = {p_sp:.4f}")
