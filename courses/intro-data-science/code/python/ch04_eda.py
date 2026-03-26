"""
Chapter 4: Exploratory Data Analysis (EDA)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === Load Titanic dataset ===
titanic = sns.load_dataset('titanic')
print("Shape:", titanic.shape)
print("\nColumn types:")
print(titanic.dtypes)
print("\nMissing values:")
print(titanic.isnull().sum())
print("\nBasic statistics:")
print(titanic.describe().round(2))

# === Univariate analysis ===
print("\n--- Survival counts ---")
print(titanic['survived'].value_counts())
print(f"\nSurvival rate: {titanic['survived'].mean():.2%}")

print("\n--- Class distribution ---")
print(titanic['class'].value_counts())

# === Bivariate analysis ===
print("\n--- Survival by class ---")
print(titanic.groupby('class')['survived'].mean().round(3))

print("\n--- Survival by sex ---")
print(titanic.groupby('sex')['survived'].mean().round(3))

# === Visualizations ===
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.countplot(data=titanic, x='class', hue='survived', ax=axes[0, 0])
axes[0, 0].set_title('Survival by Class')

sns.countplot(data=titanic, x='sex', hue='survived', ax=axes[0, 1])
axes[0, 1].set_title('Survival by Sex')

sns.histplot(data=titanic, x='age', hue='survived', kde=True,
             bins=30, ax=axes[1, 0])
axes[1, 0].set_title('Age Distribution by Survival')

sns.boxplot(data=titanic, x='class', y='fare', ax=axes[1, 1])
axes[1, 1].set_title('Fare by Class')

plt.tight_layout()
plt.savefig('ch04_titanic_eda.pdf')
plt.show()

# === Correlation heatmap ===
numeric_cols = titanic.select_dtypes(include=[np.number])
corr = numeric_cols.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Titanic Numeric Correlations')
plt.tight_layout()
plt.savefig('ch04_titanic_corr.pdf')
plt.show()

# === Outlier detection (IQR) ===
Q1 = titanic['fare'].quantile(0.25)
Q3 = titanic['fare'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = titanic[(titanic['fare'] < lower) | (titanic['fare'] > upper)]
print(f"\nFare outliers (IQR method): {len(outliers)} out of {len(titanic)}")
print(f"IQR = {IQR:.2f}, bounds = [{lower:.2f}, {upper:.2f}]")
