"""
Chapter 2: Statistical Model and Sampling — Python Implementation
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(42)

# --- CLT Illustration ---
n_values = [1, 2, 5, 30]
fig, axes = plt.subplots(1, 4, figsize=(16, 3.5))
for ax, n in zip(axes, n_values):
    means = [np.mean(np.random.exponential(1, n)) for _ in range(10000)]
    ax.hist(means, bins=40, density=True, alpha=0.7, edgecolor='black')
    ax.set_title(f"n = {n}")
    if n >= 5:
        x = np.linspace(min(means), max(means), 100)
        ax.plot(x, stats.norm.pdf(x, 1, 1/np.sqrt(n)), 'r-', lw=2)
plt.suptitle("CLT: sample means from Exp(1)", fontsize=13)
plt.tight_layout()
plt.savefig("ch02_clt.pdf")
plt.show()

# --- Glivenko-Cantelli ---
X = np.random.normal(0, 1, 50)
x_sorted = np.sort(X)
ecdf = np.arange(1, len(X)+1) / len(X)
x_grid = np.linspace(-3, 3, 200)

plt.figure(figsize=(8, 5))
plt.step(x_sorted, ecdf, where='post', label=r'$\hat{F}_{50}(x)$', lw=2)
plt.plot(x_grid, stats.norm.cdf(x_grid), 'r-', label=r'$\Phi(x)$', lw=2)
plt.legend()
plt.title("Glivenko-Cantelli: ECDF vs Normal CDF")
plt.savefig("ch02_glivenko.pdf")
plt.show()

# --- Sufficient statistic: Bernoulli ---
n, p_true = 100, 0.68
sample = np.random.binomial(1, p_true, n)
T = sample.sum()
print(f"Sufficient statistic T = sum(Xi) = {T}")
print(f"Natural estimate p_hat = T/n = {T/n:.2f}")
