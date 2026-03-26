"""
Chapter 3: Data Visualization
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# === Matplotlib basics ===
x = np.linspace(0, 2 * np.pi, 100)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(x, np.sin(x), 'b-', lw=2, label='sin(x)')
axes[0, 0].plot(x, np.cos(x), 'r--', lw=2, label='cos(x)')
axes[0, 0].set_title('Line Plot')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

np.random.seed(42)
axes[0, 1].scatter(np.random.normal(0, 1, 100), np.random.normal(0, 1, 100),
                   c=np.random.rand(100), cmap='viridis', alpha=0.6)
axes[0, 1].set_title('Scatter Plot')

axes[1, 0].hist(np.random.normal(0, 1, 500), bins=30, edgecolor='black',
                alpha=0.7, color='steelblue')
axes[1, 0].set_title('Histogram')

categories = ['A', 'B', 'C', 'D']
values = [23, 45, 12, 37]
axes[1, 1].bar(categories, values, color=['#e74c3c', '#3498db', '#2ecc71', '#f39c12'])
axes[1, 1].set_title('Bar Chart')

plt.tight_layout()
plt.savefig('ch03_matplotlib_basics.pdf')
plt.show()

# === Seaborn with Tips ===
tips = sns.load_dataset('tips')

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.histplot(data=tips, x='total_bill', hue='time', kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Distribution of Total Bill')

sns.boxplot(data=tips, x='day', y='total_bill', hue='sex', ax=axes[0, 1])
axes[0, 1].set_title('Bill by Day and Sex')

sns.scatterplot(data=tips, x='total_bill', y='tip', hue='smoker',
                style='time', ax=axes[1, 0])
axes[1, 0].set_title('Tip vs Total Bill')

sns.violinplot(data=tips, x='day', y='tip', ax=axes[1, 1])
axes[1, 1].set_title('Tip Distribution by Day')

plt.tight_layout()
plt.savefig('ch03_seaborn_tips.pdf')
plt.show()

# === Heatmap ===
iris = load_iris(as_frame=True)
corr = iris.frame.iloc[:, :4].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Iris Correlation Heatmap')
plt.tight_layout()
plt.savefig('ch03_heatmap.pdf')
plt.show()

# === Pairplot ===
g = sns.pairplot(iris.frame, hue='target', diag_kind='kde')
g.fig.suptitle('Iris Pairplot', y=1.02)
plt.savefig('ch03_pairplot.pdf')
plt.show()
