"""
Chapter 3: Point Estimation — MLE and Method of Moments
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data = np.array([1200, 1350, 980, 1500, 1100, 1450, 1300, 1050, 1400, 1250])

# --- Method of Moments ---
lambda_mom = 1 / np.mean(data)
print(f"MoM: lambda_hat = {lambda_mom:.6f}")

# --- MLE ---
lambda_mle = 1 / np.mean(data)
print(f"MLE: lambda_hat = {lambda_mle:.6f}")

# --- MLE for Normal ---
mu_mle = np.mean(data)
sigma2_mle = np.var(data, ddof=0)
sigma2_unbiased = np.var(data, ddof=1)
print(f"Normal MLE: mu={mu_mle:.2f}, sigma^2(MLE)={sigma2_mle:.2f}, sigma^2(unbiased)={sigma2_unbiased:.2f}")

# --- Log-likelihood visualization ---
lambdas = np.linspace(0.0005, 0.002, 200)
log_lik = np.array([np.sum(stats.expon.logpdf(data, scale=1/lam)) for lam in lambdas])

plt.figure(figsize=(8, 5))
plt.plot(lambdas, log_lik, 'b-', lw=2)
plt.axvline(lambda_mle, color='r', linestyle='--', label=f'MLE = {lambda_mle:.5f}')
plt.xlabel(r'$\lambda$')
plt.ylabel(r'$\ell(\lambda)$')
plt.title('Exponential Log-Likelihood')
plt.legend()
plt.savefig("ch03_loglik.pdf")
plt.show()

# --- Fisher Information ---
n = len(data)
I_fisher = 1 / lambda_mle**2
var_asymp = 1 / (n * I_fisher)
print(f"\nFisher Information I(lambda) = {I_fisher:.4f}")
print(f"Asymptotic variance: {var_asymp:.8f}")
print(f"95% asymptotic CI: [{lambda_mle - 1.96*np.sqrt(var_asymp):.5f}, "
      f"{lambda_mle + 1.96*np.sqrt(var_asymp):.5f}]")

# --- MLE for Uniform U([0, theta]) ---
data_unif = np.array([0.3, 0.7, 0.5, 0.9, 0.2, 0.8, 0.6, 0.4, 0.95, 0.1])
theta_mle = np.max(data_unif)
print(f"\nMLE for U([0,theta]): theta_hat = X_(n) = {theta_mle}")
