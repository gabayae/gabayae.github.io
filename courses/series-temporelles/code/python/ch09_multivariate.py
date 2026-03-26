"""
Chapter 9: Multivariate Time Series — VAR, Cointegration
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import VAR
from statsmodels.tsa.vector_ar.vecm import coint_johansen

# Simulate a VAR(1)
np.random.seed(42)
n = 500
A = np.array([[0.5, 0.3], [-0.2, 0.6]])
Y = np.zeros((n, 2))
for t in range(1, n):
    Y[t] = A @ Y[t-1] + np.random.multivariate_normal([0, 0],
                                      [[1, 0.3], [0.3, 1]])

df = pd.DataFrame(Y, columns=['Y1', 'Y2'])

# Fit VAR
model = VAR(df)
results = model.fit(maxlags=5, ic='bic')
print(results.summary())

# Granger causality
granger = results.test_causality('Y1', 'Y2', kind='f')
print(f"\nGranger Y2 -> Y1: p-value = {granger.pvalue:.4f}")
granger2 = results.test_causality('Y2', 'Y1', kind='f')
print(f"Granger Y1 -> Y2: p-value = {granger2.pvalue:.4f}")

# IRF
irf = results.irf(20)
irf.plot(orth=True)
plt.savefig('ch09_irf.pdf')
plt.show()

# Cointegration test
rw1 = np.cumsum(np.random.normal(0, 1, n))
rw2 = 0.5 * rw1 + np.cumsum(np.random.normal(0, 0.3, n))
data_coint = np.column_stack([rw1, rw2])
joh = coint_johansen(data_coint, det_order=0, k_ar_diff=1)
print("\nJohansen trace statistics:", joh.lr1)
print("Critical values (90%, 95%, 99%):")
print(joh.cvt)
