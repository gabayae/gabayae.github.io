"""
Chapter 5: Data Cleaning and Preparation
"""
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

# === Load Titanic ===
titanic = sns.load_dataset('titanic')
print("Original shape:", titanic.shape)
print("\nMissing values:")
print(titanic.isnull().sum())
print(f"\nMissing percentage:\n{(titanic.isnull().mean() * 100).round(1)}")

# === Handle missing values ===
df = titanic.copy()

# Fill age with median
median_age = df['age'].median()
df['age'] = df['age'].fillna(median_age)
print(f"\nAge filled with median: {median_age}")

# Fill embarked with mode
mode_embarked = df['embarked'].mode()[0]
df['embarked'] = df['embarked'].fillna(mode_embarked)
print(f"Embarked filled with mode: {mode_embarked}")

# Drop deck (too many missing)
df = df.drop(columns=['deck'])
print(f"\nAfter cleaning, missing values:\n{df.isnull().sum().sum()}")

# === Duplicates ===
print(f"\nDuplicates: {df.duplicated().sum()}")
df = df.drop_duplicates()

# === Type conversion ===
df['pclass'] = df['pclass'].astype('category')
print(f"\npclass type: {df['pclass'].dtype}")

# === Encoding categorical variables ===
# One-hot encoding
embarked_dummies = pd.get_dummies(df['embarked'], prefix='embarked', dtype=int)
print("\nOne-hot encoding (embarked):")
print(embarked_dummies.head(3))

# Label encoding
le = LabelEncoder()
df['sex_encoded'] = le.fit_transform(df['sex'])
print(f"\nLabel encoding (sex): {dict(zip(le.classes_, le.transform(le.classes_)))}")

# === Feature engineering ===
df['family_size'] = df['sibsp'] + df['parch'] + 1
df['is_alone'] = (df['family_size'] == 1).astype(int)
print(f"\nFamily size stats:\n{df['family_size'].describe().round(2)}")
print(f"Alone passengers: {df['is_alone'].sum()} ({df['is_alone'].mean():.1%})")

# === Scaling ===
from sklearn.preprocessing import StandardScaler, MinMaxScaler

scaler_std = StandardScaler()
scaler_mm = MinMaxScaler()

age_std = scaler_std.fit_transform(df[['age']])
age_mm = scaler_mm.fit_transform(df[['age']])

print(f"\nAge - Original: mean={df['age'].mean():.2f}, std={df['age'].std():.2f}")
print(f"Age - StandardScaler: mean={age_std.mean():.4f}, std={age_std.std():.4f}")
print(f"Age - MinMaxScaler: min={age_mm.min():.4f}, max={age_mm.max():.4f}")
