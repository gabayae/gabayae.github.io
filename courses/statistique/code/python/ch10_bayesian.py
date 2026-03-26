"""
Chapter 10: Introduction to Bayesian Statistics
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# --- Beta-Binomial Model ---
alpha_prior, beta_prior = 2, 2
n, s = 100, 68

alpha_post = alpha_prior + s
beta_post = beta_prior + n - s

p_grid = np.linspace(0, 1, 500)
prior = stats.beta.pdf(p_grid, alpha_prior, beta_prior)
likelihood = stats.binom.pmf(s, n, p_grid)
posterior = stats.beta.pdf(p_grid, alpha_post, beta_post)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(p_grid, prior / prior.max(), 'b--', lw=2, label=f'Prior Beta({alpha_prior},{beta_prior})')
ax.plot(p_grid, likelihood / likelihood.max(), 'g:', lw=2, label='Likelihood (normalized)')
ax.plot(p_grid, posterior / posterior.max(), 'r-', lw=2, label=f'Posterior Beta({alpha_post},{beta_post})')
ax.axvline(s/n, color='gray', linestyle=':', label=f'MLE = {s/n:.2f}')
ax.set_xlabel('p'); ax.set_ylabel('Density (normalized)')
ax.set_title('Bayesian Inference: Beta-Binomial')
ax.legend()
plt.savefig("ch10_beta_binomial.pdf")
plt.show()

# Bayesian estimators
mean_post = alpha_post / (alpha_post + beta_post)
median_post = stats.beta.median(alpha_post, beta_post)
mode_post = (alpha_post - 1) / (alpha_post + beta_post - 2)
ci_bayes = stats.beta.interval(0.95, alpha_post, beta_post)

print(f"Posterior mean  : {mean_post:.4f}")
print(f"Posterior median: {median_post:.4f}")
print(f"MAP (mode)      : {mode_post:.4f}")
print(f"MLE             : {s/n:.4f}")
print(f"95% credible CI : [{ci_bayes[0]:.4f}, {ci_bayes[1]:.4f}]")

# --- Normal-Normal Model ---
sigma2 = 4
mu0, tau2 = 0, 10
n_obs = 20
np.random.seed(42)
x_data = np.random.normal(3, np.sqrt(sigma2), n_obs)
xbar = np.mean(x_data)

prec_prior = 1 / tau2
prec_data = n_obs / sigma2
mu_post = (mu0 * prec_prior + xbar * prec_data) / (prec_prior + prec_data)
tau2_post = 1 / (prec_prior + prec_data)

print(f"\nNormal-Normal Model:")
print(f"Posterior mean : {mu_post:.4f}")
print(f"Posterior var  : {tau2_post:.4f}")
print(f"MLE (xbar)     : {xbar:.4f}")
