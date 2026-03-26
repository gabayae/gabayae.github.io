"""
Chapter 10: Introduction to Text and Time Series
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# === TEXT: Bag of Words ===
corpus = [
    "Le chat mange le poisson",
    "Le chien mange la viande",
    "Le chat et le chien jouent",
    "Le poisson nage dans l'eau"
]

vec = CountVectorizer()
X_bow = vec.fit_transform(corpus)
print("=== Bag of Words ===")
print(f"Vocabulary: {vec.get_feature_names_out()}")
print(f"Matrix:\n{X_bow.toarray()}")

# === TF-IDF ===
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(corpus)
print(f"\n=== TF-IDF ===")
df_tfidf = pd.DataFrame(X_tfidf.toarray(),
                        columns=tfidf.get_feature_names_out())
print(df_tfidf.round(2))

# === Text classification (20 newsgroups) ===
from sklearn.datasets import fetch_20newsgroups

categories = ['sci.space', 'rec.sport.baseball']
train_data = fetch_20newsgroups(subset='train', categories=categories)
test_data = fetch_20newsgroups(subset='test', categories=categories)

tfidf_vec = TfidfVectorizer(max_features=5000, stop_words='english')
X_train = tfidf_vec.fit_transform(train_data.data)
X_test = tfidf_vec.transform(test_data.data)

nb = MultinomialNB()
nb.fit(X_train, train_data.target)
y_pred = nb.predict(X_test)

print(f"\n=== Text Classification (Naive Bayes) ===")
print(f"Accuracy: {accuracy_score(test_data.target, y_pred):.3f}")
print(classification_report(test_data.target, y_pred,
                            target_names=categories))

# === TIME SERIES ===
# Simulated AirPassengers-like data
np.random.seed(42)
dates = pd.date_range('1949-01', periods=144, freq='ME')
trend = np.linspace(100, 500, 144)
seasonal = 50 * np.sin(2 * np.pi * np.arange(144) / 12)
noise = np.random.normal(0, 15, 144)
passengers = trend + seasonal + noise

ts = pd.Series(passengers, index=dates, name='passengers')
print(f"\n=== Time Series ===")
print(ts.head())
print(f"\nShape: {ts.shape}")

# Visualization
fig, axes = plt.subplots(2, 1, figsize=(12, 8))
axes[0].plot(ts, 'b-', lw=1)
axes[0].set_title('Airline Passengers (simulated)')
axes[0].set_ylabel('Passengers')

# Rolling average
ts.rolling(12).mean().plot(ax=axes[1], label='12-month rolling mean', color='red')
ts.plot(ax=axes[1], alpha=0.5, label='Original')
axes[1].legend()
axes[1].set_title('Rolling Average')
plt.tight_layout()
plt.savefig('ch10_timeseries.pdf')
plt.show()

# Resampling
print("\n=== Yearly resampling ===")
print(ts.resample('YE').mean().round(1))

# Decomposition
from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(ts, model='additive', period=12)
fig = result.plot()
fig.set_size_inches(12, 8)
plt.savefig('ch10_decomposition.pdf')
plt.show()
