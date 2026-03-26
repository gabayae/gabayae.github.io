"""
Chapter 11: Applications — Finance, Economics, Meteorology
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from arch import arch_model
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.seasonal import seasonal_decompose
from scipy.stats import t as t_dist

# === FINANCE: VaR with GARCH ===
np.random.seed(42)
n = 2000
omega, alpha, beta = 0.01, 0.08, 0.90
sigma2 = np.zeros(n)
r = np.zeros(n)
sigma2[0] = omega / (1 - alpha - beta)
for t in range(1, n):
    sigma2[t] = omega + alpha * r[t-1]**2 + beta * sigma2[t-1]
    r[t] = np.sqrt(sigma2[t]) * np.random.standard_t(5)

am = arch_model(r * 100, vol='Garch', p=1, q=1, dist='t')
res = am.fit(disp='off')
forecasts = res.forecast(horizon=1)
sigma_next = np.sqrt(forecasts.variance.values[-1, 0])
nu = res.params['nu']
VaR_01 = sigma_next * t_dist.ppf(0.01, nu)
print(f"VaR 1% = {VaR_01:.4f}%")

# === ECONOMICS: VAR Forecast ===
from statsmodels.tsa.api import VAR

np.random.seed(0)
n = 200
gdp = np.cumsum(np.random.normal(0.5, 1, n))
cpi = 0.3 * gdp + np.cumsum(np.random.normal(0, 0.5, n))
df = pd.DataFrame({'GDP_growth': np.diff(gdp), 'Inflation': np.diff(cpi)})

model = VAR(df)
results = model.fit(ic='bic')
print(f"\nVAR order: {results.k_ar}")
forecast = results.forecast(df.values[-results.k_ar:], steps=8)
print("GDP forecast (8 quarters):", forecast[:, 0].round(3))

# === METEOROLOGY: Temperature SARIMA ===
t_idx = np.arange(360)
seasonal = 15 + 0.01*t_idx + 10*np.sin(2*np.pi*t_idx/12) + np.random.normal(0, 2, 360)
ts = pd.Series(seasonal, index=pd.date_range('1990-01', periods=360, freq='ME'))

train = ts.iloc[:-24]
test = ts.iloc[-24:]
model_s = SARIMAX(train, order=(1,0,1), seasonal_order=(1,1,1,12))
results_s = model_s.fit(disp=False)
pred = results_s.forecast(steps=24)
rmse = np.sqrt(np.mean((test - pred.values)**2))
print(f"\nSARIMA temperature RMSE (24 months): {rmse:.2f} degrees")
