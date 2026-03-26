"""
Chapter 2: Stationarity and Autocovariance
"""
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf, pacf, adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Simulate an AR(1)
np.random.seed(0)
n = 500
phi = 0.7
eps = np.random.normal(0, 1, n)
x = np.zeros(n)
for t in range(1, n):
    x[t] = phi * x[t-1] + eps[t]

# ACF and PACF
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(x, lags=30, ax=axes[0], title='ACF of AR(1)')
plot_pacf(x, lags=30, ax=axes[1], title='PACF of AR(1)')
plt.tight_layout()
plt.savefig('ch02_acf_pacf.pdf')
plt.show()

# ADF test
result = adfuller(x, regression='c')
print(f"AR(1) - ADF statistic: {result[0]:.4f}, p-value: {result[1]:.4f}")
print(f"Stationary: {result[1] < 0.05}")

# Random walk (non-stationary)
rw = np.cumsum(eps)
result_rw = adfuller(rw, regression='c')
print(f"\nRandom Walk - ADF: {result_rw[0]:.4f}, p-value: {result_rw[1]:.4f}")
print(f"Stationary: {result_rw[1] < 0.05}")

# Theoretical vs empirical ACF for AR(1)
lags = np.arange(0, 21)
acf_theo = phi ** lags
acf_emp = acf(x, nlags=20)
print(f"\nACF comparison (lag 5): theoretical={phi**5:.4f}, empirical={acf_emp[5]:.4f}")
