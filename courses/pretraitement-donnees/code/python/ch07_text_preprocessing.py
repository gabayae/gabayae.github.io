"""
Chapter 7: Text Preprocessing
==============================
Data Pre-processing with Python — AIRINA Labs

This script demonstrates:
- Text cleaning (regex, lowercase, noise removal)
- Tokenization (English + French)
- Stopword removal
- Stemming and lemmatization
- TF-IDF vectorization
- Regular expressions for data extraction
"""

import pandas as pd
import numpy as np
import re
import warnings
warnings.filterwarnings("ignore")

# ============================================================
# 1. Load text dataset
# ============================================================

print("=" * 60)
print("TEXT PREPROCESSING — 20 Newsgroups")
print("=" * 60)

from sklearn.datasets import fetch_20newsgroups

categories = ["sci.space", "rec.sport.baseball", "comp.graphics",
              "talk.politics.mideast", "soc.religion.christian"]
newsgroups = fetch_20newsgroups(subset="train", categories=categories,
                                remove=("headers", "footers", "quotes"))

df = pd.DataFrame({
    "text": newsgroups.data,
    "category": [newsgroups.target_names[i] for i in newsgroups.target]
})

print(f"Documents: {len(df)}")
print(f"Categories:\n{df['category'].value_counts()}")
print(f"\nSample document:\n{df['text'].iloc[0][:200]}...")

# ============================================================
# 2. Text cleaning
# ============================================================

print("\n" + "=" * 60)
print("TEXT CLEANING")
print("=" * 60)

def clean_text(text):
    """Basic text cleaning pipeline."""
    text = text.lower()
    text = re.sub(r'\S+@\S+', '', text)           # emails
    text = re.sub(r'http\S+|www\.\S+', '', text)   # URLs
    text = re.sub(r'\d+', '', text)                 # numbers
    text = re.sub(r'[^a-z\s]', '', text)            # special chars
    text = re.sub(r'\s+', ' ', text).strip()        # whitespace
    return text

df["text_clean"] = df["text"].apply(clean_text)

# Compare before/after
sample_idx = 0
print(f"BEFORE:\n{df['text'].iloc[sample_idx][:200]}")
print(f"\nAFTER:\n{df['text_clean'].iloc[sample_idx][:200]}")

# ============================================================
# 3. Tokenization
# ============================================================

print("\n" + "=" * 60)
print("TOKENIZATION")
print("=" * 60)

import nltk
nltk.download("punkt_tab", quiet=True)
from nltk.tokenize import word_tokenize

# English tokenization
text_en = "Dr. Smith's analysis shows that 42% of patients improved."
tokens_en = word_tokenize(text_en)
print(f"English tokens: {tokens_en}")

# Simple vs NLTK
simple_tokens = text_en.split()
print(f"Simple split:   {simple_tokens}")
print(f"NLTK tokens:    {tokens_en}")

# Apply to dataset
df["tokens"] = df["text_clean"].apply(word_tokenize)
df["n_tokens_raw"] = df["tokens"].apply(len)
print(f"\nAverage tokens per document: {df['n_tokens_raw'].mean():.0f}")

# ============================================================
# 4. Stopword removal
# ============================================================

print("\n" + "=" * 60)
print("STOPWORD REMOVAL")
print("=" * 60)

nltk.download("stopwords", quiet=True)
from nltk.corpus import stopwords

stop_en = set(stopwords.words("english"))
stop_fr = set(stopwords.words("french"))
print(f"English stopwords: {len(stop_en)}")
print(f"French stopwords:  {len(stop_fr)}")

# Remove stopwords
df["tokens_no_stop"] = df["tokens"].apply(
    lambda toks: [t for t in toks if t not in stop_en and len(t) > 2]
)
df["n_tokens_clean"] = df["tokens_no_stop"].apply(len)

print(f"\nBefore stopword removal: {df['n_tokens_raw'].mean():.0f} avg tokens")
print(f"After stopword removal:  {df['n_tokens_clean'].mean():.0f} avg tokens")

# ============================================================
# 5. Stemming and lemmatization
# ============================================================

print("\n" + "=" * 60)
print("STEMMING vs LEMMATIZATION")
print("=" * 60)

from nltk.stem import PorterStemmer, SnowballStemmer
nltk.download("wordnet", quiet=True)
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ["running", "runs", "ran", "studies", "studying",
         "better", "preprocessing", "processed", "computers"]

print(f"{'Word':<18} {'Porter Stem':<18} {'Lemma (verb)':<18}")
print("-" * 54)
for w in words:
    print(f"{w:<18} {stemmer.stem(w):<18} "
          f"{lemmatizer.lemmatize(w, 'v'):<18}")

# French stemming
print("\nFrench stemming:")
stemmer_fr = SnowballStemmer("french")
mots = ["traitements", "traiter", "analyses", "analyser",
        "apprentissage", "apprendre"]
for m in mots:
    print(f"  {m:<20} -> {stemmer_fr.stem(m)}")

# Apply lemmatization to dataset
df["tokens_lemma"] = df["tokens_no_stop"].apply(
    lambda toks: [lemmatizer.lemmatize(t) for t in toks]
)

# ============================================================
# 6. Complete preprocessing pipeline
# ============================================================

print("\n" + "=" * 60)
print("COMPLETE TEXT PIPELINE")
print("=" * 60)

def preprocess_text(text, language="english"):
    """Full text preprocessing pipeline."""
    text = text.lower()
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'http\S+|www\.\S+', '', text)
    text = re.sub(r'[^a-z\s\u00e0-\u00ff]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()

    tokens = word_tokenize(text)
    stop = set(stopwords.words(language))
    tokens = [t for t in tokens if t not in stop and len(t) > 2]

    lem = WordNetLemmatizer()
    tokens = [lem.lemmatize(t) for t in tokens]

    return " ".join(tokens)

df["text_processed"] = df["text"].apply(preprocess_text)
print(f"Sample processed text:\n{df['text_processed'].iloc[0][:200]}...")

# ============================================================
# 7. TF-IDF vectorization
# ============================================================

print("\n" + "=" * 60)
print("TF-IDF VECTORIZATION")
print("=" * 60)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=5000, min_df=5, max_df=0.7,
                         ngram_range=(1, 2))
X_tfidf = tfidf.fit_transform(df["text_processed"])

print(f"TF-IDF shape: {X_tfidf.shape}")
print(f"Vocabulary size: {len(tfidf.vocabulary_)}")

# Top terms per category
feature_names = tfidf.get_feature_names_out()
for cat in df["category"].unique()[:3]:
    mask = df["category"] == cat
    mean_tfidf = X_tfidf[mask].mean(axis=0).A1
    top_idx = mean_tfidf.argsort()[-5:][::-1]
    top_terms = [feature_names[i] for i in top_idx]
    print(f"\n{cat}: {top_terms}")

# ============================================================
# 8. Bag of Words comparison
# ============================================================

print("\n" + "=" * 60)
print("BAG OF WORDS vs TF-IDF")
print("=" * 60)

from sklearn.feature_extraction.text import CountVectorizer

bow = CountVectorizer(max_features=5000, min_df=5, max_df=0.7)
X_bow = bow.fit_transform(df["text_processed"])
print(f"BoW shape:    {X_bow.shape}")
print(f"TF-IDF shape: {X_tfidf.shape}")

# ============================================================
# 9. Regex data extraction
# ============================================================

print("\n" + "=" * 60)
print("REGEX DATA EXTRACTION")
print("=" * 60)

texts = [
    "Patient BP: 120/80 mmHg, HR: 72 bpm",
    "Lab result: glucose 142 mg/dL, HbA1c 7.2%",
    "Contact: dr.smith@hospital.org, Tel: +1-555-0123",
]

# Extract numbers with units
pattern = r'(\d+\.?\d*)\s*(mg/dL|mmHg|bpm|%)'
for t in texts:
    matches = re.findall(pattern, t)
    if matches:
        print(f"Text: {t}")
        for value, unit in matches:
            print(f"  -> {value} {unit}")

# Extract emails
email_pattern = r'\S+@\S+\.\S+'
for t in texts:
    emails = re.findall(email_pattern, t)
    if emails:
        print(f"Emails found: {emails}")

# ============================================================
# 10. Document-level features
# ============================================================

print("\n" + "=" * 60)
print("DOCUMENT-LEVEL FEATURES")
print("=" * 60)

df["doc_length"] = df["text_clean"].str.len()
df["word_count"] = df["text_clean"].str.split().str.len()
df["avg_word_length"] = (df["text_clean"].str.replace(" ", "").str.len() /
                         df["word_count"])
df["vocab_richness"] = (df["text_clean"].str.split().apply(
    lambda x: len(set(x)) / len(x) if len(x) > 0 else 0))

print("Document-level features by category:")
print(df.groupby("category")[["doc_length", "word_count",
                               "avg_word_length", "vocab_richness"]]
        .mean().round(2))

print("\nDone! Chapter 7 script completed successfully.")
