"""
Chapter 4: Model Identification, Estimation, and Diagnostics (Box-Jenkins)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.graphics.tsaplots import plot_acf
from scipy import stats

# Simulate a known ARMA(1,1)
np.random.seed(42)
true_ar = np.array([1, -0.7])
true_ma = np.array([1, 0.3])
process = ArmaProcess(true_ar, true_ma)
data = process.generate_sample(nsample=500)

# Estimation by MLE
model = ARIMA(data, order=(1, 0, 1))
results = model.fit()
print(results.summary())
print(f"\nphi_1 = {results.arparams[0]:.4f} (true: 0.7)")
print(f"theta_1 = {results.maparams[0]:.4f} (true: 0.3)")

# Diagnostics
residuals = results.resid

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes[0,0].plot(residuals, lw=0.5)
axes[0,0].set_title('Residuals')
plot_acf(residuals, lags=25, ax=axes[0,1], title='ACF of Residuals')
axes[1,0].hist(residuals, bins=30, density=True, alpha=0.7)
axes[1,0].set_title('Residual Distribution')
stats.probplot(residuals, dist='norm', plot=axes[1,1])
axes[1,1].set_title('QQ-plot')
plt.tight_layout()
plt.savefig('ch04_diagnostic.pdf')
plt.show()

# Ljung-Box test
lb_test = acorr_ljungbox(residuals, lags=20, return_df=True)
print("\nLjung-Box test:")
print(lb_test)

# Model selection by AIC/BIC
results_table = []
for p in range(4):
    for q in range(4):
        try:
            m = ARIMA(data, order=(p, 0, q)).fit()
            results_table.append({'p': p, 'q': q,
                                  'AIC': m.aic, 'BIC': m.bic})
        except:
            pass
df = pd.DataFrame(results_table).sort_values('BIC')
print("\nTop 5 models by BIC:")
print(df.head(5))
