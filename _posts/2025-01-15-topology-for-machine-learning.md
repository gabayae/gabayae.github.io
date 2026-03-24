---
layout: post
title: "Why Topology Matters for Machine Learning"
date: 2025-01-15
description: "An introduction to how topological ideas are reshaping modern machine learning — from persistent homology to geometric deep learning."
tags: [topology, TDA, machine-learning]
categories: [research]
giscus_comments: true
related_posts: true
toc:
  sidebar: left
---

## The Shape of Data

Machine learning algorithms work with data, but data has **shape**. When we collect measurements from the real world — sensor readings, images, molecular structures, social networks — the resulting datasets often possess rich geometric and topological structure that standard ML methods ignore.

**Topological Data Analysis (TDA)** provides a mathematical framework for detecting and leveraging this structure. At its core, TDA uses tools from algebraic topology to identify features like connected components, loops, and voids in data at multiple scales.

I have spent much of my career thinking about the geometry and topology of spaces — first in the context of pure mathematics (quasi-metric spaces, fixed point theory), and now increasingly in the context of data. The transition is less dramatic than it sounds: the same mathematical structures that govern convergence in generalized metric spaces also govern the behavior of learning algorithms.

## Persistent Homology

The foundational tool of TDA is **persistent homology**. Given a dataset $$X = \{x_1, \ldots, x_n\} \subset \mathbb{R}^d$$, we construct a filtration of simplicial complexes:

$$K_0 \subseteq K_1 \subseteq \cdots \subseteq K_m$$

by growing balls of radius $$\epsilon$$ around each point and tracking when topological features appear (are "born") and disappear ("die").

The construction typically uses the **Vietoris-Rips complex**: at scale $$\epsilon$$, we add a $$k$$-simplex $$[x_{i_0}, \ldots, x_{i_k}]$$ whenever all pairwise distances satisfy $$d(x_{i_j}, x_{i_l}) \leq \epsilon$$. As $$\epsilon$$ increases from zero, we sweep through all scales and record the evolution of topological features.

The result is a **persistence diagram** — a multiset of points $$(b_i, d_i)$$ in the plane, where each point represents a topological feature with birth time $$b_i$$ and death time $$d_i$$. Features that persist across a wide range of scales (far from the diagonal) are considered genuine structural features of the data; those that appear and vanish quickly are noise.

## A Quick Example in Python

Here is a minimal example computing persistence on a noisy circle:

```python
import numpy as np
from ripser import ripser
from persim import plot_diagrams

# Generate a noisy circle
np.random.seed(42)
theta = np.random.uniform(0, 2 * np.pi, 200)
X = np.column_stack([np.cos(theta), np.sin(theta)])
X += 0.05 * np.random.randn(*X.shape)

# Compute persistent homology up to dimension 1
result = ripser(X, maxdim=1)

# The H_0 diagram shows one long-lived component (the circle is connected).
# The H_1 diagram shows one prominent point far from the diagonal — the loop.
plot_diagrams(result['dgms'], show=True)
```

The single persistent $$H_1$$ feature captures the fact that our data lies on a circle, regardless of the coordinate system or the noise level. This coordinate-free, multi-scale summary is exactly what makes TDA compelling for machine learning.

## Why It Matters

Topological features are:
- **Coordinate-free:** invariant under rotations, translations, and continuous deformations
- **Multi-scale:** capture structure at all resolutions simultaneously
- **Robust:** stable under small perturbations of the data (stability theorem)
- **Complementary:** provide information orthogonal to standard geometric features

These properties make TDA particularly powerful for applications where the intrinsic shape of data carries meaningful information. In my own work with Colleen Farrelly on [*The Shape of Data*](https://nostarch.com/shapeofdata), we explored how these topological summaries can be integrated into standard ML pipelines — from persistence landscapes as feature vectors to the Mapper algorithm for exploratory data analysis.

## Beyond Persistence: Geometric Deep Learning

TDA is part of a broader movement toward **geometry-aware machine learning**. Graph neural networks, equivariant networks, and manifold learning methods all exploit the geometric structure of their input domains. The emerging field of geometric deep learning, as articulated by Bronstein et al., unifies these approaches under a common mathematical umbrella — one in which topology plays a foundational role.

From my perspective as a topologist, this convergence is deeply satisfying. The abstract structures I studied during my PhD at UCT — quasi-metrics, asymmetric distances, generalized fixed point theorems — are finding concrete applications in understanding when and why learning algorithms converge, and what shape the learned representations take.

## Looking Ahead

In upcoming posts, I will explore:
- How fixed point theory connects to reinforcement learning convergence
- Practical TDA workflows in Python using Ripser and GUDHI
- Geometric deep learning on graphs and manifolds
- The role of asymmetric topology in modeling irreversible processes

The boundary between pure mathematics and applied machine learning is thinner than most people realize. Topology provides a language for describing that boundary — and for crossing it productively.
