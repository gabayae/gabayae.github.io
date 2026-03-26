"""
Chapter 6: GARCH and Conditional Volatility
"""
import numpy as np
import matplotlib.pyplot as plt
from arch import arch_model

# Simulate GARCH(1,1)
np.random.seed(42)
n = 1000
omega, alpha, beta = 0.05, 0.10, 0.85
sigma2 = np.zeros(n)
r = np.zeros(n)
sigma2[0] = omega / (1 - alpha - beta)
for t in range(1, n):
    sigma2[t] = omega + alpha * r[t-1]**2 + beta * sigma2[t-1]
    r[t] = np.sqrt(sigma2[t]) * np.random.normal()

fig, axes = plt.subplots(3, 1, figsize=(12, 8))
axes[0].plot(r, lw=0.5)
axes[0].set_title('Simulated returns (GARCH(1,1))')
axes[1].plot(r**2, lw=0.5, color='orange')
axes[1].set_title('Squared returns')
axes[2].plot(np.sqrt(sigma2), lw=0.5, color='red')
axes[2].set_title('Conditional volatility')
plt.tight_layout()
plt.savefig('ch06_garch.pdf')
plt.show()

# Fit GARCH(1,1)
am = arch_model(r, vol='Garch', p=1, q=1, dist='normal')
res = am.fit(disp='off')
print(res.summary())

# Compare GARCH, EGARCH, GJR-GARCH
for vol in ['Garch', 'EGARCH', 'GARCH']:
    try:
        if vol == 'GARCH':
            m = arch_model(r, vol='Garch', p=1, o=1, q=1)  # GJR
        else:
            m = arch_model(r, vol=vol, p=1, q=1)
        res_m = m.fit(disp='off')
        print(f"{vol}: AIC={res_m.aic:.2f}, BIC={res_m.bic:.2f}")
    except:
        pass

# Volatility forecast
forecasts = res.forecast(horizon=10)
print("\nVariance forecast:")
print(forecasts.variance.iloc[-1])
