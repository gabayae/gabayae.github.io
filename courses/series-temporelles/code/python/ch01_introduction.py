"""
Chapter 1: Introduction to Time Series
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simulate a random walk
np.random.seed(42)
n = 500
eps = np.random.normal(0, 1, n)
rw = np.cumsum(eps)

# Simulate an AR(1)
phi = 0.8
ar1 = np.zeros(n)
for t in range(1, n):
    ar1[t] = phi * ar1[t-1] + eps[t]

# Simulate a seasonal series
t = np.arange(1, 121)
seasonal = 15 + 0.05*t + 10*np.sin(2*np.pi*t/12) + np.random.normal(0, 2, 120)

fig, axes = plt.subplots(3, 1, figsize=(12, 9))
axes[0].plot(rw, lw=0.8)
axes[0].set_title('Random Walk')
axes[0].set_xlabel('t')

axes[1].plot(ar1, lw=0.8, color='red')
axes[1].set_title(f'AR(1) with phi={phi}')
axes[1].set_xlabel('t')

axes[2].plot(t, seasonal, lw=0.8, color='green')
axes[2].set_title('Seasonal Series (period=12)')
axes[2].set_xlabel('t')

plt.tight_layout()
plt.savefig('ch01_intro.pdf')
plt.show()

# Random walk variance
print(f"Var(X_200) theoretical: {200*1.0:.1f}")
rw_samples = np.cumsum(np.random.normal(0, 1, (1000, 200)), axis=1)
print(f"Var(X_200) empirical: {np.var(rw_samples[:, -1]):.1f}")
