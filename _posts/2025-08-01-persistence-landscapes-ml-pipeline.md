---
layout: post
title: "Persistence Landscapes as ML Features: A Complete Pipeline"
date: 2025-08-01
description: "A step-by-step guide to computing persistence landscapes and using them as features in machine learning pipelines."
tags: [TDA, topology, machine-learning, Python, tutorial]
categories: [research]
giscus_comments: true
related_posts: true
toc:
  sidebar: left
---

## Beyond Persistence Diagrams

In the [TDA Python tutorial](/en/blog/2025/tda-python-tutorial/), we computed persistence diagrams and used basic summary statistics as ML features. But persistence diagrams live in an awkward mathematical space — they are multisets of points, not vectors — which makes them difficult to use directly with standard ML algorithms.

**Persistence landscapes**, introduced by Peter Bubenik, solve this problem elegantly. They transform persistence diagrams into functions in a Banach space, giving us a vector representation that is:
- **Stable:** small changes in data produce small changes in the landscape
- **Statistical:** we can compute means, variances, and perform hypothesis tests
- **Compatible:** the output plugs directly into any ML pipeline expecting feature vectors

## The Mathematics

Given a persistence diagram $$D = \{(b_i, d_i)\}$$, we first define **tent functions** for each point:

$$\Lambda_i(t) = \max\left(0, \min(t - b_i, d_i - t)\right)$$

Each tent function is a triangle centered at $$\frac{b_i + d_i}{2}$$ with height $$\frac{d_i - b_i}{2}$$.

The **$$k$$-th persistence landscape** is the $$k$$-th largest value of these tent functions at each point:

$$\lambda_k(t) = k\text{-th largest value of } \{\Lambda_i(t)\}_i$$

The first landscape $$\lambda_1$$ captures the most persistent features, $$\lambda_2$$ the second most persistent, and so on.

## Implementation

Let's build a complete pipeline. First, install the dependencies:

```bash
pip install ripser persim scikit-learn matplotlib
```

### Step 1: Compute Persistence Diagrams

```python
import numpy as np
from ripser import ripser

def compute_persistence(X, maxdim=1):
    """Compute persistence diagrams up to dimension maxdim."""
    result = ripser(X, maxdim=maxdim)
    return result['dgms']
```

### Step 2: Compute Persistence Landscapes

```python
def persistence_landscape(dgm, num_landscapes=5, resolution=100):
    """
    Compute persistence landscapes from a persistence diagram.

    Parameters
    ----------
    dgm : np.ndarray
        Persistence diagram (n x 2 array of birth-death pairs).
    num_landscapes : int
        Number of landscape functions to compute.
    resolution : int
        Number of sample points for discretization.

    Returns
    -------
    landscapes : np.ndarray
        Array of shape (num_landscapes, resolution).
    """
    # Remove infinite death times
    finite = dgm[np.isfinite(dgm[:, 1])]
    if len(finite) == 0:
        return np.zeros((num_landscapes, resolution))

    # Define the grid
    birth_min = finite[:, 0].min()
    death_max = finite[:, 1].max()
    grid = np.linspace(birth_min, death_max, resolution)

    # Compute tent functions for each point
    tents = np.zeros((len(finite), resolution))
    for i, (b, d) in enumerate(finite):
        tents[i] = np.maximum(0, np.minimum(grid - b, d - grid))

    # Sort at each grid point to get landscapes
    sorted_tents = np.sort(tents, axis=0)[::-1]

    # Take top-k landscapes
    k = min(num_landscapes, len(finite))
    landscapes = np.zeros((num_landscapes, resolution))
    landscapes[:k] = sorted_tents[:k]

    return landscapes
```

### Step 3: Build the Feature Vector

```python
def landscape_features(X, maxdim=1, num_landscapes=5, resolution=100):
    """
    Full pipeline: point cloud -> persistence -> landscapes -> feature vector.
    """
    dgms = compute_persistence(X, maxdim=maxdim)

    features = []
    for dim in range(maxdim + 1):
        ls = persistence_landscape(dgms[dim], num_landscapes, resolution)
        # Flatten into a single feature vector
        features.append(ls.flatten())

    return np.concatenate(features)
```

### Step 4: Classification Pipeline

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def tda_classification(datasets, labels):
    """
    Classify point clouds using persistence landscape features.

    Parameters
    ----------
    datasets : list of np.ndarray
        List of point clouds.
    labels : np.ndarray
        Class labels.
    """
    # Compute features for all datasets
    X = np.array([landscape_features(data) for data in datasets])

    # Build pipeline
    clf = Pipeline([
        ('scaler', StandardScaler()),
        ('rf', RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    # Cross-validate
    scores = cross_val_score(clf, X, labels, cv=5, scoring='accuracy')
    print(f"Accuracy: {scores.mean():.3f} (+/- {scores.std():.3f})")

    return clf.fit(X, labels)
```

## Example: Classifying Shapes

Let's test this on a synthetic dataset — distinguishing circles from figure-eights:

```python
from sklearn.datasets import make_circles

def make_figure_eight(n_points=100, noise=0.05):
    """Generate points on a figure-eight curve."""
    t = np.linspace(0, 2 * np.pi, n_points)
    x = np.sin(t) + np.random.normal(0, noise, n_points)
    y = np.sin(2 * t) / 2 + np.random.normal(0, noise, n_points)
    return np.column_stack([x, y])

# Generate datasets
n_samples = 50
datasets = []
labels = []

for _ in range(n_samples):
    X_circle, _ = make_circles(n_samples=100, noise=0.05, factor=0.5)
    datasets.append(X_circle)
    labels.append(0)

    X_eight = make_figure_eight(100, noise=0.05)
    datasets.append(X_eight)
    labels.append(1)

labels = np.array(labels)

# Classify
model = tda_classification(datasets, labels)
```

A circle has one $$H_1$$ feature (one loop), while a figure-eight has two. Persistence landscapes capture this distinction naturally, typically achieving **95%+ accuracy** on this task.

## Tips for Real-World Use

1. **Normalize your data** before computing persistence. TDA is scale-sensitive — the persistence values depend on the metric.

2. **Choose resolution and num_landscapes carefully.** Start with `resolution=100` and `num_landscapes=5`. Increase if your diagrams have many points.

3. **Combine with standard features.** Landscape features are complementary — concatenating them with traditional features (PCA components, statistical summaries) often improves performance.

4. **Consider persistence images** as an alternative vectorization. They use a Gaussian kernel density estimate instead of tent functions and can work better for certain datasets.

5. **For large datasets**, use approximate persistence (e.g., subsampling or landmark-based methods) to keep computation tractable.

## Further Reading

- Bubenik, P. (2015). *Statistical Topological Data Analysis using Persistence Landscapes.* JMLR.
- For a comprehensive treatment of these methods, see [*The Shape of Data*](https://nostarch.com/shapeofdata).
- The [scikit-tda](https://scikit-tda.org/) ecosystem provides production-ready implementations.
