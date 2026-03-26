"""
Chapter 5: Confidence Intervals
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# --- CI for the mean (unknown variance) ---
data = np.array([12.1, 11.8, 12.5, 12.3, 11.9, 12.7, 12.0, 12.4, 11.7, 12.2])
n = len(data)
xbar, s = np.mean(data), np.std(data, ddof=1)
alpha = 0.05
t_crit = stats.t.ppf(1 - alpha/2, df=n-1)
ci = (xbar - t_crit*s/np.sqrt(n), xbar + t_crit*s/np.sqrt(n))
print(f"95% CI for mu: [{ci[0]:.4f}, {ci[1]:.4f}]")

# --- CI for variance ---
chi2_lo = stats.chi2.ppf(alpha/2, df=n-1)
chi2_hi = stats.chi2.ppf(1-alpha/2, df=n-1)
ci_var = ((n-1)*s**2/chi2_hi, (n-1)*s**2/chi2_lo)
print(f"95% CI for sigma^2: [{ci_var[0]:.4f}, {ci_var[1]:.4f}]")

# --- CI for proportion (Wald and Wilson) ---
n_poll, x_fav = 1000, 520
p_hat = x_fav / n_poll
z = stats.norm.ppf(1-alpha/2)
margin = z * np.sqrt(p_hat*(1-p_hat)/n_poll)
print(f"Wald CI:   [{p_hat-margin:.4f}, {p_hat+margin:.4f}]")

p_tilde = (x_fav + z**2/2) / (n_poll + z**2)
m_w = z * np.sqrt(p_tilde*(1-p_tilde)/(n_poll+z**2))
print(f"Wilson CI: [{p_tilde-m_w:.4f}, {p_tilde+m_w:.4f}]")

# --- Sample size ---
E = 0.03
n_needed = int(np.ceil(z**2 * 0.25 / E**2))
print(f"Min n for margin {E} on proportion: {n_needed}")

# --- Coverage visualization ---
mu_true, sigma_true, n_ci = 12.0, 0.3, 10
np.random.seed(1)
fig, ax = plt.subplots(figsize=(10, 6))
count_miss = 0
for i in range(50):
    sample = np.random.normal(mu_true, sigma_true, n_ci)
    m = np.mean(sample)
    se = np.std(sample, ddof=1) / np.sqrt(n_ci)
    t_c = stats.t.ppf(0.975, df=n_ci-1)
    lo, hi = m - t_c*se, m + t_c*se
    hit = lo <= mu_true <= hi
    color = 'blue' if hit else 'red'
    if not hit:
        count_miss += 1
    ax.plot([lo, hi], [i, i], color=color, lw=1.5)
    ax.plot(m, i, 'o', color=color, markersize=3)
ax.axvline(mu_true, color='green', lw=2, linestyle='--', label=f'mu={mu_true}')
ax.set_title(f'50 CIs at 95% ({count_miss} miss)')
ax.legend()
plt.tight_layout()
plt.savefig("ch05_coverage.pdf")
plt.show()
