"""
Chapter 9: Multiple Regression and ANOVA
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import matplotlib.pyplot as plt

np.random.seed(42)

# --- Multiple regression ---
n = 50
df = pd.DataFrame({
    'area': np.random.uniform(25, 120, n),
    'rooms': np.random.randint(1, 6, n),
    'floor': np.random.randint(0, 10, n)
})
df['price'] = 30 + 2.5*df['area'] + 15*df['rooms'] + 3*df['floor'] + np.random.normal(0, 15, n)

X = sm.add_constant(df[['area', 'rooms', 'floor']])
model = sm.OLS(df['price'], X).fit()
print(model.summary())
print(f"\nR^2 = {model.rsquared:.4f}, R^2_adj = {model.rsquared_adj:.4f}")

# --- ANOVA ---
A = [20.1, 21.5, 19.8, 22.0, 20.5, 21.2]
B = [23.4, 24.1, 22.8, 23.9, 24.5, 23.2]
C = [19.5, 20.2, 18.9, 20.8, 19.1, 20.5]

f_stat, p_val = stats.f_oneway(A, B, C)
print(f"\nANOVA: F={f_stat:.4f}, p={p_val:.6f}")

df_anova = pd.DataFrame({
    'yield': A + B + C,
    'fertilizer': ['A']*6 + ['B']*6 + ['C']*6
})
model_anova = ols('Q("yield") ~ C(fertilizer)', data=df_anova).fit()
print(sm.stats.anova_lm(model_anova, typ=2))

# Tukey HSD
tukey = pairwise_tukeyhsd(df_anova['yield'], df_anova['fertilizer'], alpha=0.05)
print("\nTukey HSD:")
print(tukey)
