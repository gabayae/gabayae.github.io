---
layout: post
title: "Why topology matters for machine learning"
date: 2025-01-15
description: "What persistent homology and geometric deep learning bring to machine learning, written from the perspective of a working topologist."
tags: [topology, TDA, machine-learning]
categories: [research]
giscus_comments: true
related_posts: true
toc:
  sidebar: left
---

## The Shape of Data

Machine learning algorithms work with data, but data has **shape**. Sensor readings, images, molecular structures, social networks — none of these are just bags of feature vectors. They sit on manifolds, in graphs, with topology that standard ML pipelines flatten before they ever see it.

**Topological Data Analysis (TDA)** is the mathematical framework for detecting and using that structure. TDA borrows from algebraic topology to identify features like connected components, loops, and voids in data, at multiple scales simultaneously.

I have spent most of my career thinking about the geometry and topology of spaces, first in pure mathematics (quasi-metric spaces, fixed-point theory) and now in data. The transition is less dramatic than it sounds: the same mathematical structures that govern convergence in generalized metric spaces also govern the behavior of learning algorithms.

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

## Why these features earn their place

Topological features have four properties that make them useful as ML inputs. They're coordinate-free (invariant under rotations, translations, and continuous deformations). They're multi-scale, capturing structure across resolutions in one pass. They're stable under small data perturbations — this is what the stability theorem buys you, and it's why moderate noise doesn't destroy the signal. And they provide information that's largely orthogonal to standard geometric features, so they compose with PCA, kernels, and the rest of the usual pipeline rather than competing with it.

In *The Shape of Data*, Colleen Farrelly and I show how persistence landscapes plug in as feature vectors, how Mapper supports exploratory data analysis, and where each method earns its keep against the standard baselines.

## Beyond persistence: geometric deep learning

TDA is part of a wider shift toward geometry-aware ML. Graph neural networks, equivariant networks, and manifold-learning methods all use the geometric structure of their input domains rather than treating inputs as opaque vectors. Bronstein et al.'s geometric deep learning program organizes these approaches into a single framework, with topology sitting at the bottom of the stack.

Watching this happen from a pure-topology background is satisfying. The quasi-metrics, asymmetric distances, and generalized fixed-point theorems I worked on during my PhD at UCT now have concrete uses: understanding when learning algorithms converge, and what shape the representations they learn actually have.

## What's coming in the next posts

I'll work through fixed-point theory and reinforcement-learning convergence, practical TDA workflows in Python (Ripser, GUDHI), geometric deep learning on graphs and manifolds, and what asymmetric topology contributes to modeling irreversible processes.

The pure-math / applied-ML boundary is real but porous, and topology happens to be one of the places where the two sides share vocabulary. That's the through-line of the series.
