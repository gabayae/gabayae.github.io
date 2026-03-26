"""
Chapter 2: Data Manipulation with Pandas
"""
import pandas as pd
import numpy as np
import seaborn as sns

# === Create DataFrame ===
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Salary': [45000, 55000, 70000, 52000],
    'City': ['Paris', 'Lyon', 'Paris', 'Marseille']
}
df = pd.DataFrame(data)
print(df)
print(f"\nShape: {df.shape}")
print(f"Types:\n{df.dtypes}")

# === Load Tips dataset ===
tips = sns.load_dataset('tips')
print(f"\nTips shape: {tips.shape}")
print(tips.head(3))

# === Selection and filtering ===
print("\n--- Column selection ---")
print(tips['total_bill'].head(3))

big_tips = tips[tips['tip'] > 5]
print(f"\n--- Tips > $5: {len(big_tips)} rows ---")
print(big_tips.head(3))

mask = (tips['sex'] == 'Female') & (tips['day'] == 'Sun')
print("\n--- loc: females, Sunday ---")
print(tips.loc[mask, ['total_bill', 'tip']].head(3))

# === New columns ===
tips['tip_pct'] = (tips['tip'] / tips['total_bill'] * 100).round(1)
print(tips[['total_bill', 'tip', 'tip_pct']].head(5))

tips['bill_category'] = tips['total_bill'].apply(
    lambda x: 'High' if x > 30 else ('Medium' if x > 15 else 'Low'))
print(tips['bill_category'].value_counts())

# === GroupBy ===
print("\n--- Mean by day ---")
print(tips.groupby('day')[['total_bill', 'tip']].mean().round(2))

agg = tips.groupby(['day', 'time']).agg(
    n_meals=('total_bill', 'count'),
    avg_bill=('total_bill', 'mean'),
    avg_tip=('tip', 'mean')
).round(2)
print("\n--- Multiple aggregations ---")
print(agg)

# === Pivot table ===
pivot = tips.pivot_table(values='tip', index='day', columns='sex',
                         aggfunc='mean').round(2)
print("\n--- Pivot table ---")
print(pivot)

# === Merge ===
clients = pd.DataFrame({
    'client_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana']
})
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104],
    'client_id': [1, 2, 2, 5],
    'amount': [150, 200, 80, 300]
})

inner = pd.merge(clients, orders, on='client_id', how='inner')
print("\n--- Inner join ---")
print(inner)

left = pd.merge(clients, orders, on='client_id', how='left')
print("\n--- Left join ---")
print(left)
