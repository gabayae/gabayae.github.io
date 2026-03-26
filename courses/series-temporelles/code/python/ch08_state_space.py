"""
Chapter 8: State-Space Models and Kalman Filter
"""
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.structural import UnobservedComponents

# Simulate local level model
np.random.seed(42)
n = 200
sigma_w, sigma_v = 0.5, 1.0
x = np.zeros(n)
y = np.zeros(n)
for t in range(1, n):
    x[t] = x[t-1] + sigma_w * np.random.normal()
    y[t] = x[t] + sigma_v * np.random.normal()

# Manual Kalman filter
F, H, Q, R = 1.0, 1.0, sigma_w**2, sigma_v**2
x_filt = np.zeros(n)
P_filt = np.zeros(n)
P_filt[0] = 1.0
for t in range(1, n):
    x_pred = F * x_filt[t-1]
    P_pred = F * P_filt[t-1] * F + Q
    S = H * P_pred * H + R
    K = P_pred * H / S
    x_filt[t] = x_pred + K * (y[t] - H * x_pred)
    P_filt[t] = (1 - K * H) * P_pred

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(y, 'o', ms=2, alpha=0.5, label='Observations')
ax.plot(x, 'g-', lw=1.5, label='True state')
ax.plot(x_filt, 'r--', lw=1.5, label='Kalman filter')
ax.legend()
ax.set_title('Kalman Filter — Local Level Model')
plt.savefig('ch08_kalman.pdf')
plt.show()

# With statsmodels
model = UnobservedComponents(y, 'local level')
results = model.fit(disp=False)
print(results.summary())

# Kalman gain convergence
print(f"\nFinal Kalman gain: {P_filt[-1]*H / (H*P_filt[-1]*H + R):.4f}")
print(f"Steady-state gain (theory): {(-R + np.sqrt(R**2 + 4*Q*R))/(2*R):.4f}")
