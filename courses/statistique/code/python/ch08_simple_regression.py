"""
Chapter 8: Simple Linear Regression
"""
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

area = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100, 120])
price = np.array([95, 110, 125, 140, 148, 160, 175, 185, 195, 210, 220, 240, 260, 290, 350])

# --- scipy ---
slope, intercept, r, p, se = stats.linregress(area, price)
print(f"beta_1={slope:.4f} (SE={se:.4f}, p={p:.6f})")
print(f"beta_0={intercept:.4f}")
print(f"R^2={r**2:.4f}")

# --- statsmodels ---
X = sm.add_constant(area)
model = sm.OLS(price, X).fit()
print(model.summary())

# --- Diagnostics ---
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].scatter(area, price, color='blue')
axes[0, 0].plot(area, model.fittedvalues, 'r-', lw=2)
axes[0, 0].set_xlabel('Area (m^2)'); axes[0, 0].set_ylabel('Price (kEUR)')
axes[0, 0].set_title('Regression Line')

axes[0, 1].scatter(model.fittedvalues, model.resid)
axes[0, 1].axhline(0, color='red', ls='--')
axes[0, 1].set_title('Residuals vs Fitted')

stats.probplot(model.resid, plot=axes[1, 0])
axes[1, 0].set_title('QQ-plot')

axes[1, 1].hist(model.resid, bins=6, edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Residual Distribution')

plt.tight_layout()
plt.savefig("ch08_regression.pdf")
plt.show()

# --- Prediction ---
x_new = 85
pred = model.get_prediction(sm.add_constant([x_new]))
print(f"\nPrediction for {x_new} m^2:")
print(pred.summary_frame(alpha=0.05))
