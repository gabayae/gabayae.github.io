"""
Chapter 4: Estimator Properties — Bias, Consistency, Efficiency
"""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mu_true, sigma2_true = 0, 4
n = 10
n_sim = 50000

biased = np.array([np.var(np.random.normal(mu_true, 2, n), ddof=0) for _ in range(n_sim)])
unbiased = np.array([np.var(np.random.normal(mu_true, 2, n), ddof=1) for _ in range(n_sim)])

print("=== MLE (divisor n) ===")
print(f"  E[hat_sigma^2] = {np.mean(biased):.4f}, Bias = {np.mean(biased)-sigma2_true:.4f}")
print(f"  Var = {np.var(biased):.4f}, MSE = {np.mean((biased-sigma2_true)**2):.4f}")

print("\n=== S^2 (divisor n-1) ===")
print(f"  E[S^2] = {np.mean(unbiased):.4f}, Bias = {np.mean(unbiased)-sigma2_true:.4f}")
print(f"  Var = {np.var(unbiased):.4f}, MSE = {np.mean((unbiased-sigma2_true)**2):.4f}")

print(f"\nCramer-Rao bound for mu: {sigma2_true/n:.4f}")

fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(biased, bins=50, alpha=0.5, density=True, label='MLE (n)')
ax.hist(unbiased, bins=50, alpha=0.5, density=True, label='$S^2$ (n-1)')
ax.axvline(sigma2_true, color='red', lw=2, label=f'True $\\sigma^2$={sigma2_true}')
ax.legend()
ax.set_title(f'Distribution of variance estimators (n={n})')
plt.savefig("ch04_bias_variance.pdf")
plt.show()
