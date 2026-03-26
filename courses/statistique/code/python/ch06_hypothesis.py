"""
Chapter 6: Hypothesis Testing — General Framework
"""
import numpy as np
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

# --- One-sample t-test ---
data = np.array([48.2, 47.5, 49.1, 46.8, 50.3, 48.7, 47.9, 49.5,
                 46.2, 48.8, 49.0, 47.3, 48.1, 50.1, 47.0,
                 49.4, 48.6, 46.5, 49.8, 47.2, 48.3, 49.7,
                 47.8, 48.5, 46.9])

t_stat, p_val = stats.ttest_1samp(data, 50)
print(f"H0: mu=50, t={t_stat:.4f}, p={p_val:.6f}")
print("Reject H0" if p_val < 0.05 else "Fail to reject H0")

# --- Power function ---
def power_z(mu, mu0, sigma, n, alpha=0.05):
    z_a = norm.ppf(1 - alpha/2)
    delta = (mu - mu0) / (sigma / np.sqrt(n))
    return 1 - norm.cdf(z_a - delta) + norm.cdf(-z_a - delta)

mu_vals = np.linspace(44, 56, 200)
powers = [power_z(m, 50, 4.5, 25) for m in mu_vals]

plt.figure(figsize=(8, 5))
plt.plot(mu_vals, powers, 'b-', lw=2)
plt.axhline(0.05, color='red', ls='--', label=r'$\alpha=0.05$')
plt.xlabel(r'$\mu$ (true value)')
plt.ylabel('Power')
plt.title('Power function (two-sided z-test)')
plt.legend()
plt.savefig("ch06_power.pdf")
plt.show()

# --- Sample size for target power ---
def sample_size_z(mu_alt, mu0, sigma, alpha=0.05, power=0.8):
    z_a = norm.ppf(1 - alpha/2)
    z_b = norm.ppf(power)
    return int(np.ceil(((z_a + z_b) * sigma / (mu_alt - mu0))**2))

n_needed = sample_size_z(48, 50, 4.5)
print(f"Sample size to detect mu=48 with 80% power: n={n_needed}")
