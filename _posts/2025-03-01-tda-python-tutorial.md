---
layout: post
title: "Getting started with TDA in Python"
date: 2025-03-01
description: "A practical introduction to Topological Data Analysis using Python — from point clouds to persistence diagrams."
tags: [TDA, data-science, machine-learning]
categories: [tutorials]
giscus_comments: true
related_posts: true
toc:
  sidebar: left
---

## Setup

The Python ecosystem for TDA has matured significantly. The key libraries you'll need:

```python
pip install ripser persim scikit-tda gudhi matplotlib
```

- **Ripser:** Fast computation of Vietoris-Rips persistence
- **Persim:** Persistence diagram utilities (distances, plotting)
- **GUDHI:** Comprehensive TDA library from INRIA
- **scikit-tda:** Scikit-learn compatible TDA tools

## Your First Persistence Diagram

Let's start with a simple example — computing the persistent homology of a noisy circle:

```python
import numpy as np
from ripser import ripser
from persim import plot_diagrams
import matplotlib.pyplot as plt

# Generate noisy circle
np.random.seed(42)
theta = np.random.uniform(0, 2 * np.pi, 100)
X = np.column_stack([np.cos(theta), np.sin(theta)])
X += 0.1 * np.random.randn(*X.shape)

# Compute persistent homology
result = ripser(X, maxdim=1)

# Plot
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].scatter(X[:, 0], X[:, 1], s=10)
axes[0].set_title("Noisy Circle")
axes[0].set_aspect("equal")

plot_diagrams(result["dgms"], ax=axes[1])
axes[1].set_title("Persistence Diagram")
plt.tight_layout()
plt.show()
```

## Reading the Persistence Diagram

The persistence diagram reveals:
- **$$H_0$$ (connected components):** Many short-lived features (noise), one long-lived feature (the circle is connected)
- **$$H_1$$ (loops):** One prominent point far from the diagonal — this is the loop forming the circle!

Points far from the diagonal represent **persistent** (real) features; points near the diagonal are **noise**.

## Integrating TDA with Machine Learning

TDA features can be fed into standard ML pipelines:

```python
from sklearn.ensemble import RandomForestClassifier
from persim import PersistenceLandscapeExact

# Convert persistence diagrams to feature vectors
landscape = PersistenceLandscapeExact(hom_deg=1)
features = landscape.fit_transform(diagrams)

# Use in a classifier
clf = RandomForestClassifier()
clf.fit(features, labels)
```

## Next Steps

For a comprehensive treatment of geometry-based ML, check out [*The Shape of Data*](https://nostarch.com/shapeofdata) — covering TDA, geometric features, and practical R/Python implementations.
