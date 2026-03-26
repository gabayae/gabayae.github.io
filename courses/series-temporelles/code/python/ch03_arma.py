"""
Chapter 3: AR, MA, ARMA Models
"""
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.regression.linear_model import yule_walker

np.random.seed(42)

# AR(2)
ar_params = np.array([1, -0.75, 0.25])
ma_params = np.array([1])
ar2 = ArmaProcess(ar_params, ma_params)
x = ar2.generate_sample(nsample=500)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].plot(x, lw=0.7)
axes[0].set_title('AR(2): phi1=0.75, phi2=-0.25')
plot_acf(x, lags=25, ax=axes[1], title='ACF')
plot_pacf(x, lags=25, ax=axes[2], title='PACF')
plt.tight_layout()
plt.savefig('ch03_arma.pdf')
plt.show()

# MA(2)
ma2 = ArmaProcess(np.array([1]), np.array([1, 0.6, -0.3]))
y = ma2.generate_sample(nsample=500)

# ARMA(1,1)
arma11 = ArmaProcess(np.array([1, -0.8]), np.array([1, 0.4]))
z = arma11.generate_sample(nsample=500)

# Yule-Walker estimation
rho, sigma = yule_walker(x, order=2)
print(f"Yule-Walker estimates: phi = {rho}")
print(f"True values: phi = [0.75, -0.25]")

# MA(1) ACF
theta = 0.5
acf_ma1_h1 = theta / (1 + theta**2)
print(f"\nMA(1) theoretical ACF(1) = {acf_ma1_h1:.4f}")
