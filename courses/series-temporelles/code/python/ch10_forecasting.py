"""
Chapter 10: Forecasting and Confidence Intervals
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.arima_process import ArmaProcess
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Simulate ARMA(1,1)
np.random.seed(42)
ar = np.array([1, -0.7])
ma = np.array([1, 0.3])
data = ArmaProcess(ar, ma).generate_sample(nsample=300)

# Train/test split
train, test = data[:250], data[250:]

# Fit and forecast
model = ARIMA(train, order=(1, 0, 1))
results = model.fit()

forecast = results.get_forecast(steps=50)
pred = forecast.predicted_mean
ci = forecast.conf_int(alpha=0.05)

# Metrics
mae = mean_absolute_error(test, pred)
rmse = np.sqrt(mean_squared_error(test, pred))
print(f"MAE  = {mae:.4f}")
print(f"RMSE = {rmse:.4f}")

# Plot
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(range(250), train, 'b-', lw=0.7, label='Train')
ax.plot(range(250, 300), test, 'g-', lw=1, label='Test')
ax.plot(range(250, 300), pred, 'r--', lw=1.5, label='Forecast')
ax.fill_between(range(250, 300), ci[:, 0], ci[:, 1],
                alpha=0.2, color='red')
ax.legend()
ax.set_title('ARMA(1,1) Forecast')
plt.savefig('ch10_forecast.pdf')
plt.show()

# Rolling forecast
rolling_preds = []
for i in range(len(test)):
    train_i = data[:250+i]
    model_i = ARIMA(train_i, order=(1, 0, 1)).fit()
    rolling_preds.append(model_i.forecast(steps=1)[0])
rmse_roll = np.sqrt(mean_squared_error(test, rolling_preds))
print(f"RMSE (rolling): {rmse_roll:.4f}")

# AR(1) forecast variance
phi = 0.8
sigma2 = 1.0
for h in [1, 2, 5, 10, 20]:
    var_h = sigma2 * (1 - phi**(2*h)) / (1 - phi**2)
    print(f"AR(1) forecast variance at h={h}: {var_h:.4f}")
