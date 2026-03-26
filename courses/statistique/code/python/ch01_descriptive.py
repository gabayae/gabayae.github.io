"""
Chapter 1: Descriptive Statistics — Python Implementation
Statistique Mathematique (L2/L3)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# --- Data ---
salaires = np.array([1800, 1950, 2100, 2100, 2200, 2300, 2350, 2400,
                     2500, 2600, 2650, 2700, 2800, 2900, 3100, 3200,
                     3500, 3800, 4500, 8000])

# --- Measures of central tendency ---
print("=== Mesures de tendance centrale / Central tendency ===")
print(f"Moyenne / Mean     : {np.mean(salaires):.2f}")
print(f"Mediane / Median   : {np.median(salaires):.2f}")
print(f"Mode               : {stats.mode(salaires, keepdims=True).mode[0]}")

# --- Measures of spread ---
print("\n=== Mesures de dispersion / Spread ===")
print(f"Ecart-type / Std   : {np.std(salaires, ddof=1):.2f}")
print(f"Variance           : {np.var(salaires, ddof=1):.2f}")
print(f"Etendue / Range    : {np.ptp(salaires)}")
print(f"IQR                : {stats.iqr(salaires):.2f}")
print(f"CV                 : {np.std(salaires, ddof=1)/np.mean(salaires):.4f}")

# --- Shape ---
print("\n=== Forme / Shape ===")
print(f"Skewness           : {stats.skew(salaires):.4f}")
print(f"Kurtosis (excess)  : {stats.kurtosis(salaires):.4f}")

# --- Visualizations ---
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Histogram
axes[0].hist(salaires, bins=8, edgecolor='black', alpha=0.7, color='steelblue')
axes[0].axvline(np.mean(salaires), color='red', linestyle='--', label=f'Mean={np.mean(salaires):.0f}')
axes[0].axvline(np.median(salaires), color='green', linestyle='-', label=f'Median={np.median(salaires):.0f}')
axes[0].set_title("Histogramme / Histogram")
axes[0].set_xlabel("Salaire (EUR)")
axes[0].legend(fontsize=8)

# Boxplot
bp = axes[1].boxplot(salaires, vert=True, patch_artist=True)
bp['boxes'][0].set_facecolor('lightblue')
axes[1].set_title("Boite a moustaches / Boxplot")

# ECDF
x_sorted = np.sort(salaires)
y_ecdf = np.arange(1, len(x_sorted) + 1) / len(x_sorted)
axes[2].step(x_sorted, y_ecdf, where='post', color='navy', lw=2)
axes[2].set_title("ECDF")
axes[2].set_xlabel("Salaire (EUR)")
axes[2].set_ylabel("F_n(x)")
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("ch01_descriptive.pdf")
plt.show()

# --- Bivariate ---
print("\n=== Donnees bivariees / Bivariate ===")
x = np.array([8, 12, 14, 10, 16, 6, 18, 11])
y = np.array([9, 13, 15, 12, 17, 8, 19, 13])
r, p_val = stats.pearsonr(x, y)
print(f"Correlation r = {r:.4f}, p-value = {p_val:.6f}")
