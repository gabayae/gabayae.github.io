"""
Chapter 8: Pandas — Data Analysis
"""
import pandas as pd
import seaborn as sns

# === Load dataset ===
tips = sns.load_dataset('tips')
print(f"Shape: {tips.shape}")
print(tips.head())
print(tips.describe().round(2))

# === Selection ===
print("\n--- Column ---")
print(tips['total_bill'].head())

print("\n--- Filtering ---")
big = tips[tips['tip'] > 5]
print(f"Tips > $5: {len(big)} rows")

# === GroupBy ===
print("\n--- Mean by day ---")
print(tips.groupby('day')[['total_bill', 'tip']].mean().round(2))

# === Pivot table ===
pivot = tips.pivot_table(values='tip', index='day', columns='sex', aggfunc='mean')
print("\n--- Pivot ---")
print(pivot.round(2))
