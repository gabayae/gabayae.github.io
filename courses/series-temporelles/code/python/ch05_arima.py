"""
Chapter 5: ARIMA Models and Differencing
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
import pmdarima as pm

# Simulate non-stationary series (random walk with drift)
np.random.seed(42)
n = 300
eps = np.random.normal(0, 1, n)
rw_drift = np.cumsum(0.1 + eps)  # I(1) with drift

# ADF test
print("ADF on level:", adfuller(rw_drift)[1])
print("ADF on diff:", adfuller(np.diff(rw_drift))[1])

# ARIMA estimation
model = ARIMA(rw_drift, order=(1, 1, 0))
results = model.fit()
print(results.summary())

# Auto ARIMA
auto_model = pm.auto_arima(rw_drift, stepwise=True, trace=True)
print(auto_model.summary())

# Seasonal example: simulate monthly temperatures
t = np.arange(360)
seasonal = 15 + 0.01*t + 10*np.sin(2*np.pi*t/12) + np.random.normal(0, 2, 360)
idx = pd.date_range('1990-01', periods=360, freq='ME')
ts = pd.Series(seasonal, index=idx)

# SARIMA
model_s = SARIMAX(ts, order=(1,0,1), seasonal_order=(1,1,1,12))
results_s = model_s.fit(disp=False)
print(results_s.summary())

# Forecast
forecast = results_s.get_forecast(steps=24)
pred = forecast.predicted_mean
ci = forecast.conf_int()

fig, ax = plt.subplots(figsize=(12, 5))
ts[-60:].plot(ax=ax, label='Observed')
pred.plot(ax=ax, label='Forecast', color='red')
ax.fill_between(ci.index, ci.iloc[:,0], ci.iloc[:,1],
                alpha=0.2, color='red')
ax.legend()
ax.set_title('SARIMA Forecast')
plt.savefig('ch05_arima.pdf')
plt.show()
