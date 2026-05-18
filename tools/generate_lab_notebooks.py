#!/usr/bin/env python3
"""Generate one starter .ipynb per lab referenced in any cohort data file.

Each notebook is a functional starting point — real imports, real dataset
loading, structured exercise cells with clear deliverable spec. Not a
worked solution; the participant fills in the marked sections.

Layout: courses/<slug>/cohort/labs/<notebook_name>

Run:
    python tools/generate_lab_notebooks.py
"""
from __future__ import annotations
import json
import pathlib
import sys

import yaml

REPO = pathlib.Path(__file__).resolve().parents[1]
SLUGS = [
    "tda",
    "apprentissage-geometrique",
    "apprentissage-renforcement",
    "mlops",
    "ia-generative",
    "apprentissage-automatique",
]


def md(source: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source.splitlines(keepends=True),
    }


def code(source: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source.splitlines(keepends=True),
    }


def notebook(cells: list[dict]) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


# -----------------------------------------------------------------------------
# Per-lab specs — keyed by (slug, week_number)
# -----------------------------------------------------------------------------

LABS = {

  # TDA ----------------------------------------------------------------------
  ("tda", "01"): {
    "title": "Lab 1 — First persistence diagrams",
    "goal": "Compute persistence diagrams of three point clouds (noisy circle, torus, two interlocked circles), plot them, and interpret which features survive across scales.",
    "deliverable": "Notebook with three persistence diagrams plus a 200-word interpretation in markdown explaining what the H_0 and H_1 bars tell you about each shape.",
    "install": "ripser persim matplotlib numpy",
    "imports": (
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "from ripser import ripser\n"
        "from persim import plot_diagrams\n"
        "\n"
        "rng = np.random.default_rng(42)"
    ),
    "data_section": (
        "## Datasets — three synthetic point clouds\n\n"
        "We build the data inline so the lab is reproducible without external downloads."
    ),
    "data_code": (
        "def noisy_circle(n=200, r=1.0, noise=0.05):\n"
        "    theta = rng.uniform(0, 2*np.pi, n)\n"
        "    pts = np.column_stack([r*np.cos(theta), r*np.sin(theta)])\n"
        "    pts += noise * rng.normal(size=pts.shape)\n"
        "    return pts\n"
        "\n"
        "def noisy_torus(n=400, R=1.5, r=0.5, noise=0.03):\n"
        "    u = rng.uniform(0, 2*np.pi, n)\n"
        "    v = rng.uniform(0, 2*np.pi, n)\n"
        "    x = (R + r*np.cos(v)) * np.cos(u)\n"
        "    y = (R + r*np.cos(v)) * np.sin(u)\n"
        "    z = r * np.sin(v)\n"
        "    pts = np.column_stack([x, y, z])\n"
        "    return pts + noise * rng.normal(size=pts.shape)\n"
        "\n"
        "def two_circles(n=300, sep=2.5, noise=0.05):\n"
        "    c1 = noisy_circle(n//2)\n"
        "    c2 = noisy_circle(n//2) + np.array([sep, 0.0])\n"
        "    return np.vstack([c1, c2])\n"
        "\n"
        "X_circle = noisy_circle()\n"
        "X_torus  = noisy_torus()\n"
        "X_two    = two_circles()\n"
        "print('circle:', X_circle.shape, 'torus:', X_torus.shape, 'two:', X_two.shape)"
    ),
    "exercises": [
      ("Exercise 1 — Compute and plot the three diagrams",
       "for name, X in [('circle', X_circle), ('torus', X_torus), ('two_circles', X_two)]:\n"
       "    result = ripser(X, maxdim=1)\n"
       "    fig, ax = plt.subplots(figsize=(5,5))\n"
       "    plot_diagrams(result['dgms'], ax=ax)\n"
       "    ax.set_title(f'{name}')\n"
       "    plt.show()\n"),
      ("Exercise 2 — Interpret",
       "# YOUR TURN\n"
       "# Write a short markdown cell below each plot that answers:\n"
       "# - How many H_0 bars are long-lived in each diagram? Why?\n"
       "# - How many H_1 bars survive to high persistence? Why?\n"
       "# - Where are the noisy features sitting in the diagram?\n"),
      ("Exercise 3 — Stretch goal",
       "# YOUR TURN\n"
       "# Increase the noise parameter on the circle. At what level does the\n"
       "# H_1 feature stop being clearly separated from the diagonal?\n"
       "# Document the noise level you found and explain in 2-3 sentences.\n"),
    ],
  },

  ("tda", "04"): {
    "title": "Lab 2 — Vectorizing persistence diagrams",
    "goal": "Take diagrams from Lab 1, compute persistence landscapes and persistence images, and use them as features for a sklearn classifier that distinguishes the three point-cloud types.",
    "deliverable": "Notebook with two classifiers (one on landscapes, one on images) and a confusion matrix for each. Plus a 200-word memo on which vectorization works best on this dataset and why.",
    "install": "ripser persim scikit-learn matplotlib numpy",
    "imports": (
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "from ripser import ripser\n"
        "from persim import PersistenceImager, plot_diagrams\n"
        "from persim.landscapes import PersLandscapeApprox, plot_landscape_simple\n"
        "from sklearn.linear_model import LogisticRegression\n"
        "from sklearn.model_selection import train_test_split\n"
        "from sklearn.metrics import classification_report, confusion_matrix\n"
        "\n"
        "rng = np.random.default_rng(42)"
    ),
    "data_section": "## Datasets — 90 point clouds, three classes (30 each)",
    "data_code": (
        "def noisy_circle(n=200, r=1.0, noise=0.05, seed=None):\n"
        "    r_rng = np.random.default_rng(seed)\n"
        "    theta = r_rng.uniform(0, 2*np.pi, n)\n"
        "    pts = np.column_stack([r*np.cos(theta), r*np.sin(theta)])\n"
        "    return pts + noise * r_rng.normal(size=pts.shape)\n"
        "\n"
        "def two_circles(n=300, sep=2.5, noise=0.05, seed=None):\n"
        "    r_rng = np.random.default_rng(seed)\n"
        "    c1 = noisy_circle(n//2, noise=noise, seed=seed)\n"
        "    c2 = noisy_circle(n//2, noise=noise, seed=seed+1 if seed else None) + np.array([sep, 0.0])\n"
        "    return np.vstack([c1, c2])\n"
        "\n"
        "def random_blob(n=200, noise=0.4, seed=None):\n"
        "    r_rng = np.random.default_rng(seed)\n"
        "    return r_rng.normal(scale=noise, size=(n, 2))\n"
        "\n"
        "X_data, y_data = [], []\n"
        "for i in range(30):\n"
        "    X_data.append(noisy_circle(seed=i));      y_data.append(0)\n"
        "    X_data.append(two_circles(seed=100+i));   y_data.append(1)\n"
        "    X_data.append(random_blob(seed=200+i));   y_data.append(2)\n"
        "y_data = np.array(y_data)\n"
        "print('dataset:', len(X_data), 'point clouds,', np.bincount(y_data), 'per class')"
    ),
    "exercises": [
      ("Exercise 1 — Compute persistence diagrams for all 90 clouds",
       "diagrams = []\n"
       "for X in X_data:\n"
       "    res = ripser(X, maxdim=1)\n"
       "    diagrams.append(res['dgms'])\n"
       "print(f'{len(diagrams)} diagrams computed')\n"),
      ("Exercise 2 — Vectorize using persistence images",
       "# YOUR TURN\n"
       "# Use persim.PersistenceImager to vectorize the H_1 diagrams.\n"
       "# Stack the resulting flat vectors into an (N, D) feature matrix X_img.\n"),
      ("Exercise 3 — Train a logistic-regression classifier on each",
       "# YOUR TURN\n"
       "# 1. Train/test split (75/25)\n"
       "# 2. Fit logistic regression on the persistence-image features.\n"
       "# 3. Print the classification_report and the confusion matrix.\n"),
      ("Exercise 4 — Repeat for persistence landscapes and compare",
       "# YOUR TURN\n"
       "# Vectorize via PersLandscapeApprox, train the same classifier,\n"
       "# and report which vectorization performs better on this dataset.\n"),
    ],
  },

  ("tda", "06"): {
    "title": "Lab 3 — Comparing simplicial-complex constructions",
    "goal": "On the same point cloud, compute persistence with Vietoris-Rips, Čech (via alpha approximation), and alpha complexes. Compare diagrams and compute time.",
    "deliverable": "Notebook with three diagrams overlaid, plus a table of computation times and a 200-word discussion of when the differences matter.",
    "install": "ripser gudhi persim matplotlib numpy",
    "imports": (
        "import time\n"
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "from ripser import ripser\n"
        "import gudhi\n"
        "from persim import plot_diagrams\n"
        "\n"
        "rng = np.random.default_rng(42)"
    ),
    "data_section": "## A point cloud with one prominent H_1 feature",
    "data_code": (
        "n = 400\n"
        "theta = rng.uniform(0, 2*np.pi, n)\n"
        "X = np.column_stack([np.cos(theta), np.sin(theta)])\n"
        "X += 0.07 * rng.normal(size=X.shape)\n"
        "print('cloud:', X.shape)"
    ),
    "exercises": [
      ("Exercise 1 — Vietoris-Rips via ripser",
       "t0 = time.time()\n"
       "rips = ripser(X, maxdim=1)\n"
       "t_rips = time.time() - t0\n"
       "print(f'Rips: {t_rips:.2f}s')\n"),
      ("Exercise 2 — Alpha complex via GUDHI",
       "# YOUR TURN\n"
       "# Use gudhi.AlphaComplex(points=X) and compute persistence with maxdim=1.\n"
       "# Record the time.\n"),
      ("Exercise 3 — Čech approximation",
       "# YOUR TURN\n"
       "# Use gudhi.CechComplex (approximate) or a witness complex.\n"
       "# Compare the resulting diagram to Rips and Alpha.\n"),
      ("Exercise 4 — Time comparison",
       "# YOUR TURN\n"
       "# Print a table of complex name, computation time, number of simplices,\n"
       "# and number of H_1 features above persistence 0.1.\n"),
    ],
  },

  ("tda", "08"): {
    "title": "Lab 4 — Statistical tests on persistence diagrams",
    "goal": "Two-sample test on diagrams: simulate two populations differing in H_1 noise level, test for a difference using a sliced-Wasserstein kernel and a permutation test.",
    "deliverable": "Notebook reporting a p-value, a power curve as the noise difference shrinks, and a 200-word memo on what the test does and does not tell you.",
    "install": "ripser persim scikit-learn matplotlib numpy",
    "imports": (
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "from ripser import ripser\n"
        "from persim import sliced_wasserstein\n"
        "from scipy.stats import permutation_test\n"
        "\n"
        "rng = np.random.default_rng(42)"
    ),
    "data_section": "## Two populations of 50 noisy circles each",
    "data_code": (
        "def population(n_clouds=50, n_points=200, noise=0.05, seed_base=0):\n"
        "    diagrams = []\n"
        "    for i in range(n_clouds):\n"
        "        r = np.random.default_rng(seed_base + i)\n"
        "        theta = r.uniform(0, 2*np.pi, n_points)\n"
        "        X = np.column_stack([np.cos(theta), np.sin(theta)])\n"
        "        X += noise * r.normal(size=X.shape)\n"
        "        diagrams.append(ripser(X, maxdim=1)['dgms'][1])\n"
        "    return diagrams\n"
        "\n"
        "pop_A = population(noise=0.05, seed_base=0)\n"
        "pop_B = population(noise=0.10, seed_base=1000)\n"
        "print('populations built:', len(pop_A), len(pop_B))"
    ),
    "exercises": [
      ("Exercise 1 — Compute pairwise sliced-Wasserstein distance matrix",
       "# YOUR TURN\n"
       "# Compute the (100, 100) pairwise distance matrix using persim.sliced_wasserstein.\n"),
      ("Exercise 2 — Permutation test",
       "# YOUR TURN\n"
       "# Test whether the mean within-A distance differs from the mean between-AB distance.\n"
       "# Use scipy.stats.permutation_test with n_resamples=1000.\n"),
      ("Exercise 3 — Power curve",
       "# YOUR TURN\n"
       "# For noise difference in {0.02, 0.04, 0.06, 0.08, 0.10}, estimate the power\n"
       "# of the test at alpha=0.05 over 50 replications each.\n"),
    ],
  },

  # Geom DL ------------------------------------------------------------------
  ("apprentissage-geometrique", "03"): {
    "title": "Lab 1 — Your first GNN: GCN on Cora",
    "goal": "Train a 2-layer GCN on the Cora citation network and compare against a logistic-regression baseline on the same features.",
    "deliverable": "Notebook with training curves, final test accuracy for both models, and a 200-word memo on what the GCN gains over the bag-of-features baseline.",
    "install": "torch torch_geometric scikit-learn matplotlib",
    "imports": (
        "import torch\n"
        "import torch.nn.functional as F\n"
        "from torch_geometric.datasets import Planetoid\n"
        "from torch_geometric.nn import GCNConv\n"
        "from sklearn.linear_model import LogisticRegression\n"
        "from sklearn.metrics import accuracy_score\n"
        "import numpy as np\n"
        "\n"
        "torch.manual_seed(42)\n"
        "np.random.seed(42)"
    ),
    "data_section": "## The Cora citation network",
    "data_code": (
        "dataset = Planetoid(root='/tmp/Cora', name='Cora')\n"
        "data = dataset[0]\n"
        "print('Nodes:', data.num_nodes, 'Edges:', data.num_edges, 'Features:', data.num_features, 'Classes:', dataset.num_classes)"
    ),
    "exercises": [
      ("Exercise 1 — Logistic-regression baseline on node features",
       "X = data.x.numpy()\n"
       "y = data.y.numpy()\n"
       "train_mask = data.train_mask.numpy()\n"
       "test_mask = data.test_mask.numpy()\n"
       "\n"
       "clf = LogisticRegression(max_iter=2000)\n"
       "clf.fit(X[train_mask], y[train_mask])\n"
       "preds = clf.predict(X[test_mask])\n"
       "print('Logistic baseline accuracy:', accuracy_score(y[test_mask], preds))\n"),
      ("Exercise 2 — Implement a 2-layer GCN",
       "# YOUR TURN\n"
       "# Define a GCN with two GCNConv layers, a ReLU between them, and dropout.\n"
       "# class GCN(torch.nn.Module): ...\n"),
      ("Exercise 3 — Train and report test accuracy",
       "# YOUR TURN\n"
       "# Train for 200 epochs with Adam(lr=0.01). Track val accuracy.\n"
       "# Report final test accuracy. Compare to the logistic baseline.\n"),
      ("Exercise 4 — Inspect failure cases",
       "# YOUR TURN\n"
       "# Find 5 test-set nodes the GCN gets wrong. Look at their neighborhoods.\n"
       "# Hypothesize why and write a short note.\n"),
    ],
  },

  ("apprentissage-geometrique", "06"): {
    "title": "Lab 2 — Hyperbolic embedding of a taxonomy",
    "goal": "Embed WordNet's mammal subtree in 2-D Euclidean and 2-D Poincaré-ball space. Compare nearest-neighbor structure.",
    "deliverable": "Two scatter plots (Euclidean vs Poincaré), a precision@10 table for retrieving parent nodes, and a 200-word memo on when hyperbolic helps and when it doesn't.",
    "install": "torch nltk matplotlib scikit-learn",
    "imports": (
        "import torch\n"
        "import torch.nn.functional as F\n"
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "import nltk\n"
        "from nltk.corpus import wordnet as wn\n"
        "\n"
        "nltk.download('wordnet', quiet=True)\n"
        "torch.manual_seed(42)"
    ),
    "data_section": "## WordNet mammal subtree",
    "data_code": (
        "root = wn.synset('mammal.n.01')\n"
        "def descendants(s, depth=4):\n"
        "    out = {s.name(): 0}\n"
        "    frontier = [(s, 0)]\n"
        "    while frontier:\n"
        "        node, d = frontier.pop()\n"
        "        if d >= depth: continue\n"
        "        for child in node.hyponyms():\n"
        "            if child.name() not in out:\n"
        "                out[child.name()] = d + 1\n"
        "                frontier.append((child, d+1))\n"
        "    return out\n"
        "\n"
        "nodes = descendants(root)\n"
        "name_to_idx = {n: i for i, n in enumerate(nodes)}\n"
        "edges = []\n"
        "for name in nodes:\n"
        "    for child in wn.synset(name).hyponyms():\n"
        "        if child.name() in name_to_idx:\n"
        "            edges.append((name_to_idx[name], name_to_idx[child.name()]))\n"
        "print(f'{len(nodes)} synsets, {len(edges)} hyponymy edges')"
    ),
    "exercises": [
      ("Exercise 1 — Euclidean baseline (random init + edge attraction)",
       "# YOUR TURN\n"
       "# Initialize 2-D embeddings, optimize so connected pairs are close and\n"
       "# non-connected pairs are far (use a simple contrastive or InfoNCE loss).\n"),
      ("Exercise 2 — Poincaré embedding",
       "# YOUR TURN\n"
       "# Implement Nickel-Kiela Poincaré embedding using the hyperbolic distance:\n"
       "# d(u,v) = arccosh(1 + 2 * |u-v|^2 / ((1 - |u|^2)(1 - |v|^2)))\n"
       "# Train with Riemannian SGD on the same edges.\n"),
      ("Exercise 3 — Compare visually and quantitatively",
       "# YOUR TURN\n"
       "# Plot both embeddings. For each non-root node, retrieve the 10 nearest\n"
       "# neighbors and compute precision@10 against true ancestors. Print both\n"
       "# numbers in a table.\n"),
    ],
  },

  ("apprentissage-geometrique", "08"): {
    "title": "Lab 3 — PointNet on ModelNet10",
    "goal": "Train a PointNet for 3D shape classification on ModelNet10. Evaluate the model's equivariance breakage by rotating test inputs.",
    "deliverable": "Notebook with a trained PointNet, a confusion matrix on ModelNet10 test, and a rotation-robustness curve showing accuracy as a function of test-time rotation angle.",
    "install": "torch torch_geometric matplotlib scikit-learn",
    "imports": (
        "import torch\n"
        "import torch.nn as nn\n"
        "import torch.nn.functional as F\n"
        "from torch_geometric.datasets import ModelNet\n"
        "from torch_geometric.loader import DataLoader\n"
        "import torch_geometric.transforms as T\n"
        "from sklearn.metrics import classification_report, confusion_matrix\n"
        "import numpy as np\n"
        "\n"
        "torch.manual_seed(42)\n"
        "device = 'cuda' if torch.cuda.is_available() else 'cpu'"
    ),
    "data_section": (
        "## ModelNet10\n"
        "\n"
        "The first run downloads ~50 MB."
    ),
    "data_code": (
        "transform = T.Compose([T.SamplePoints(1024), T.NormalizeScale()])\n"
        "train_ds = ModelNet(root='/tmp/ModelNet10', name='10', train=True,  transform=transform)\n"
        "test_ds  = ModelNet(root='/tmp/ModelNet10', name='10', train=False, transform=transform)\n"
        "print('classes:', train_ds.num_classes, 'train:', len(train_ds), 'test:', len(test_ds))"
    ),
    "exercises": [
      ("Exercise 1 — Implement a minimal PointNet",
       "# YOUR TURN\n"
       "# Define a PointNet with: per-point MLP -> global max-pool -> classifier MLP.\n"
       "# 3 input dims (xyz), 10 output classes.\n"),
      ("Exercise 2 — Train and report test accuracy",
       "# YOUR TURN\n"
       "# Train for 30 epochs with Adam(lr=1e-3). Report test accuracy and confusion matrix.\n"),
      ("Exercise 3 — Rotation-robustness curve",
       "# YOUR TURN\n"
       "# For theta in {0, 30, 60, 90, 120, 150, 180} degrees, rotate every test\n"
       "# point cloud about a random axis and report classification accuracy.\n"
       "# Plot the resulting curve.\n"),
    ],
  },

  # RL -----------------------------------------------------------------------
  ("apprentissage-renforcement", "02"): {
    "title": "Lab 1 — Value iteration on a 50-state inventory MDP",
    "goal": "Solve a 50-state inventory-management MDP by value iteration. Compare with a hand-designed heuristic policy.",
    "deliverable": "Notebook with the optimal value function, the optimal policy, and a comparison against a 'order-up-to-S' heuristic across 1000 simulated rollouts.",
    "install": "numpy matplotlib",
    "imports": (
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "\n"
        "rng = np.random.default_rng(42)"
    ),
    "data_section": "## Inventory MDP setup",
    "data_code": (
        "# State: current stock in {0, ..., 49}. Action: order quantity in {0, ..., 49-s}.\n"
        "# Demand: Poisson(lambda=3). Holding cost 0.5/unit/period. Stockout cost 5/unit.\n"
        "# Selling price 4/unit. Ordering cost 2/unit + fixed 10 if order > 0.\n"
        "\n"
        "S = 50\n"
        "GAMMA = 0.95\n"
        "DEMAND_LAMBDA = 3\n"
        "HOLD = 0.5\n"
        "STOCKOUT = 5.0\n"
        "PRICE = 4.0\n"
        "ORDER_VAR = 2.0\n"
        "ORDER_FIX = 10.0\n"
        "\n"
        "from scipy.stats import poisson\n"
        "demand_pmf = poisson.pmf(np.arange(S+1), DEMAND_LAMBDA)\n"
        "demand_pmf[-1] = 1.0 - demand_pmf[:-1].sum()\n"
        "print('demand pmf sum:', demand_pmf.sum())"
    ),
    "exercises": [
      ("Exercise 1 — Build the reward and transition tables",
       "# YOUR TURN\n"
       "# For each (state s, action a), compute:\n"
       "# - expected immediate reward r(s, a)\n"
       "# - transition probabilities P(s' | s, a)\n"),
      ("Exercise 2 — Value iteration",
       "# YOUR TURN\n"
       "# Initialize V = 0. Iterate V_{k+1}(s) = max_a [r(s, a) + gamma * sum_{s'} P(s'|s,a) V_k(s')]\n"
       "# until ||V_{k+1} - V_k||_inf < 1e-6. Plot V and the policy.\n"),
      ("Exercise 3 — Compare against (s, S) heuristic",
       "# YOUR TURN\n"
       "# Simulate both the optimal policy and an order-up-to-S heuristic for 1000 episodes.\n"
       "# Report mean total reward, standard error, and the gap.\n"),
    ],
  },

  ("apprentissage-renforcement", "04"): {
    "title": "Lab 2 — Tabular Q-learning on FrozenLake and Taxi",
    "goal": "Train a tabular Q-learning agent on FrozenLake-v1 and Taxi-v3. Report learning curves and final reward.",
    "deliverable": "Notebook with two trained Q-tables, learning curves, and a 200-word note on which hyperparameter mattered most.",
    "install": "gymnasium numpy matplotlib",
    "imports": (
        "import gymnasium as gym\n"
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "\n"
        "rng = np.random.default_rng(42)"
    ),
    "data_section": "## Environments",
    "data_code": (
        "env_lake = gym.make('FrozenLake-v1', is_slippery=True)\n"
        "env_taxi = gym.make('Taxi-v3')\n"
        "print('FrozenLake states/actions:', env_lake.observation_space.n, env_lake.action_space.n)\n"
        "print('Taxi states/actions:', env_taxi.observation_space.n, env_taxi.action_space.n)"
    ),
    "exercises": [
      ("Exercise 1 — Implement tabular Q-learning",
       "# YOUR TURN\n"
       "# Function q_learn(env, episodes, alpha, gamma, eps_start, eps_end, eps_decay)\n"
       "# returning Q-table and per-episode reward.\n"),
      ("Exercise 2 — Train on FrozenLake and plot the learning curve",
       "# YOUR TURN\n"
       "# Train for 20_000 episodes. Plot 100-episode rolling mean of reward.\n"
       "# Print the final greedy-policy success rate over 1000 evaluation episodes.\n"),
      ("Exercise 3 — Train on Taxi and tune",
       "# YOUR TURN\n"
       "# Train for 30_000 episodes. Tune alpha and eps_decay. Report final\n"
       "# average return over 1000 evaluation episodes.\n"),
    ],
  },

  ("apprentissage-renforcement", "07"): {
    "title": "Lab 3 — PPO on CartPole and BipedalWalker",
    "goal": "Train PPO with Stable-Baselines3 on CartPole-v1 (easy) and BipedalWalker-v3 (hard). Tune learning rate, clip range, entropy coefficient.",
    "deliverable": "Notebook with two trained agents, training curves, evaluation videos (or screenshots), and a 200-word memo on which hyperparameter mattered most for the harder task.",
    "install": "gymnasium stable-baselines3 numpy matplotlib",
    "imports": (
        "import gymnasium as gym\n"
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "from stable_baselines3 import PPO\n"
        "from stable_baselines3.common.evaluation import evaluate_policy\n"
        "\n"
        "np.random.seed(42)"
    ),
    "data_section": "## Environments",
    "data_code": (
        "env_cart = gym.make('CartPole-v1')\n"
        "env_walk = gym.make('BipedalWalker-v3')\n"
        "print('CartPole obs/act dims:', env_cart.observation_space.shape, env_cart.action_space.n)\n"
        "print('BipedalWalker obs/act dims:', env_walk.observation_space.shape, env_walk.action_space.shape)"
    ),
    "exercises": [
      ("Exercise 1 — PPO on CartPole",
       "model = PPO('MlpPolicy', env_cart, verbose=0)\n"
       "model.learn(total_timesteps=50_000)\n"
       "mean, std = evaluate_policy(model, env_cart, n_eval_episodes=20)\n"
       "print(f'CartPole: {mean:.1f} +/- {std:.1f}')\n"),
      ("Exercise 2 — PPO on BipedalWalker",
       "# YOUR TURN\n"
       "# Train PPO on BipedalWalker for 500_000 steps. Tune lr, n_steps, ent_coef.\n"
       "# Report mean reward over 20 eval episodes.\n"),
      ("Exercise 3 — Hyperparameter sensitivity",
       "# YOUR TURN\n"
       "# On BipedalWalker, sweep ent_coef in {0.0, 0.01, 0.1}. Plot learning curves.\n"
       "# Write a 200-word memo on which mattered most and why.\n"),
    ],
  },

  # MLOps --------------------------------------------------------------------
  ("mlops", "02"): {
    "title": "Lab 1 — Reproducible Python environment",
    "goal": "Set up a project with uv + pyproject.toml + lockfile + pre-commit hooks. Add a Dockerfile that reproduces the same environment.",
    "deliverable": "Public GitHub repo with the artifacts. CI passing on a single push. README that a stranger can follow in five minutes.",
    "install": "uv",
    "imports": "import subprocess, pathlib\n",
    "data_section": (
        "## What you build outside this notebook\n\n"
        "Most of this lab happens at the shell. The notebook is a structured walkthrough\n"
        "with shell commands you run yourself (uncomment and run as you go)."
    ),
    "data_code": "# Working directory for the lab\nLAB = pathlib.Path('mlops-lab01')\nLAB.mkdir(exist_ok=True)\nprint('working in:', LAB.resolve())\n",
    "exercises": [
      ("Exercise 1 — Initialize the project",
       "# !uv init mlops-lab01\n"
       "# !cd mlops-lab01 && uv add numpy pandas scikit-learn\n"
       "# !cd mlops-lab01 && uv add --dev pytest ruff mypy pre-commit\n"
       "#\n"
       "# Verify pyproject.toml and uv.lock both exist.\n"),
      ("Exercise 2 — Add pre-commit hooks",
       "# YOUR TURN\n"
       "# Create .pre-commit-config.yaml with ruff and mypy hooks. Run pre-commit install.\n"),
      ("Exercise 3 — Containerize with the same dependencies",
       "# YOUR TURN\n"
       "# Write a multi-stage Dockerfile that copies the lockfile and produces a slim\n"
       "# runtime image. Verify identical behavior on host and container.\n"),
      ("Exercise 4 — CI passing on a single push",
       "# YOUR TURN\n"
       "# Add .github/workflows/ci.yml that runs ruff + mypy + pytest on push.\n"
       "# Push to GitHub. Confirm green.\n"),
    ],
  },

  ("mlops", "03"): {
    "title": "Lab 2 — Versioning the full ML project",
    "goal": "Take an existing ML notebook. Version code in Git, dataset in DVC, trained model artifact in MLflow Model Registry. Tag a v1.0 release that reproduces from scratch.",
    "deliverable": "Public repo with code + DVC remote pointer + MLflow registry pointer. README documenting the reproduction steps.",
    "install": "dvc mlflow scikit-learn",
    "imports": (
        "import subprocess, pathlib\n"
        "import mlflow\n"
        "import mlflow.sklearn"
    ),
    "data_section": "## Pick a model from a prior lab and version it end-to-end",
    "data_code": "# Set the MLflow tracking URI (local for the lab, S3 / Databricks for production)\nimport os\nos.environ.setdefault('MLFLOW_TRACKING_URI', 'sqlite:///mlflow.db')\nprint('MLflow URI:', os.environ['MLFLOW_TRACKING_URI'])\n",
    "exercises": [
      ("Exercise 1 — Version the data with DVC",
       "# !pip install dvc dvc-s3\n"
       "# !dvc init\n"
       "# !dvc add data/training.csv\n"
       "# git add data/training.csv.dvc .gitignore\n"
       "#\n"
       "# YOUR TURN — point a DVC remote at the storage of your choice (S3, GCS, Azure, local).\n"),
      ("Exercise 2 — Log model training with MLflow",
       "# YOUR TURN\n"
       "# Wrap your training script in mlflow.start_run(). Log params, metrics, and\n"
       "# the trained model with mlflow.sklearn.log_model.\n"),
      ("Exercise 3 — Promote to Model Registry",
       "# YOUR TURN\n"
       "# Register the model. Transition stage from None -> Staging -> Production.\n"
       "# Tag a v1.0 release in Git.\n"),
    ],
  },

  ("mlops", "04"): {
    "title": "Lab 3 — Instrumented training loop",
    "goal": "Take any training script from a prior course. Add MLflow tracking. Run a hyperparameter sweep. Promote the best model to the registry.",
    "deliverable": "MLflow run history (screenshot or exported HTML), the best model in the registry tagged Production, and a 200-word note on what surprised you in the sweep.",
    "install": "mlflow scikit-learn pandas",
    "imports": (
        "import mlflow\n"
        "import mlflow.sklearn\n"
        "from sklearn.ensemble import RandomForestClassifier\n"
        "from sklearn.datasets import load_breast_cancer\n"
        "from sklearn.model_selection import train_test_split\n"
        "from sklearn.metrics import accuracy_score, roc_auc_score\n"
        "import numpy as np\n"
        "import os\n"
        "\n"
        "os.environ.setdefault('MLFLOW_TRACKING_URI', 'sqlite:///mlflow.db')"
    ),
    "data_section": "## A small but real dataset to sweep over",
    "data_code": (
        "data = load_breast_cancer()\n"
        "X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)\n"
        "print('train/test shapes:', X_train.shape, X_test.shape)"
    ),
    "exercises": [
      ("Exercise 1 — Instrument a single training run",
       "with mlflow.start_run():\n"
       "    mlflow.log_param('n_estimators', 100)\n"
       "    clf = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_train, y_train)\n"
       "    p = clf.predict_proba(X_test)[:, 1]\n"
       "    mlflow.log_metric('auc', roc_auc_score(y_test, p))\n"
       "    mlflow.sklearn.log_model(clf, 'model')\n"),
      ("Exercise 2 — Hyperparameter sweep",
       "# YOUR TURN\n"
       "# Sweep n_estimators in {50, 100, 200, 500} and max_depth in {3, 5, 10, None}.\n"
       "# Log each run to MLflow.\n"),
      ("Exercise 3 — Promote the best run",
       "# YOUR TURN\n"
       "# Identify the best run by AUC. Register it. Transition to Production.\n"),
    ],
  },

  ("mlops", "07"): {
    "title": "Lab 4 — Minimal ML inference image",
    "goal": "Build a Docker image for a single-model inference service. Target image size under 500 MB. Push to a registry.",
    "deliverable": "Docker image on a public registry, runnable in one docker run command. README with image size and build time.",
    "install": "(none — Docker is the focus)",
    "imports": "import subprocess, pathlib\n",
    "data_section": "## What you build at the shell, structured as a walkthrough",
    "data_code": "# Lab directory\nLAB = pathlib.Path('mlops-lab04')\nLAB.mkdir(exist_ok=True)\nprint('working in:', LAB.resolve())\n",
    "exercises": [
      ("Exercise 1 — Write a multi-stage Dockerfile",
       "# YOUR TURN\n"
       "# Stage 1 (builder): install Python + dependencies into a virtualenv\n"
       "# Stage 2 (runtime): COPY the virtualenv from builder, drop build tooling\n"),
      ("Exercise 2 — Build, tag, and check size",
       "# !docker build -t yourname/ml-inference:0.1 .\n"
       "# !docker images yourname/ml-inference:0.1\n"
       "# Target: under 500 MB.\n"),
      ("Exercise 3 — Push to a public registry",
       "# !docker login\n"
       "# !docker push yourname/ml-inference:0.1\n"),
    ],
  },

  ("mlops", "08"): {
    "title": "Lab 5 — Deploy a model end-to-end",
    "goal": "Wrap a model in FastAPI. Containerize. Deploy to Render or Railway free tier. Verify the endpoint from a fresh notebook.",
    "deliverable": "Public deployed endpoint that someone unfamiliar with the project can call. README with the curl example.",
    "install": "fastapi uvicorn pydantic scikit-learn requests",
    "imports": (
        "import requests\n"
        "import json\n"
        "from sklearn.datasets import load_iris\n"
        "from sklearn.ensemble import RandomForestClassifier"
    ),
    "data_section": "## What the notebook does vs what you do at the shell",
    "data_code": (
        "# This notebook runs end-to-end against a *deployed* endpoint at the end.\n"
        "# The middle steps (writing the FastAPI app, containerizing, deploying)\n"
        "# happen outside the notebook.\n"
        "ENDPOINT = 'https://your-service.onrender.com'  # set after deployment\n"
        "print('targeting:', ENDPOINT)"
    ),
    "exercises": [
      ("Exercise 1 — Train and save a model locally",
       "data = load_iris()\n"
       "clf = RandomForestClassifier().fit(data.data, data.target)\n"
       "import joblib\n"
       "joblib.dump(clf, 'iris.joblib')\n"
       "print('saved iris.joblib')\n"),
      ("Exercise 2 — Write the FastAPI service",
       "# YOUR TURN\n"
       "# In app/main.py:\n"
       "# - load iris.joblib at startup\n"
       "# - POST /predict expects a 4-vector, returns class index + probabilities\n"
       "# - GET /health returns {'status': 'ok'}\n"),
      ("Exercise 3 — Containerize and deploy",
       "# YOUR TURN\n"
       "# Dockerfile + render.yaml (or railway.toml). Push to GitHub, connect repo,\n"
       "# deploy. Update ENDPOINT above and run cells below.\n"),
      ("Exercise 4 — Call the deployed endpoint",
       "# After deployment, run this against the live URL:\n"
       "r = requests.get(f'{ENDPOINT}/health')\n"
       "print('health:', r.json())\n"
       "r = requests.post(f'{ENDPOINT}/predict', json={'features': [5.1, 3.5, 1.4, 0.2]})\n"
       "print('predict:', r.json())\n"),
    ],
  },

  # GenAI --------------------------------------------------------------------
  ("ia-generative", "02"): {
    "title": "Lab 1 — Mini transformer from scratch",
    "goal": "Implement a 4-layer decoder-only transformer in pure PyTorch. Train on TinyShakespeare or TinyStories. Generate samples.",
    "deliverable": "Notebook with a trained model (max 25M parameters), training and validation loss curves, and 5 sample generations across temperature {0.5, 0.8, 1.0}.",
    "install": "torch numpy matplotlib",
    "imports": (
        "import torch\n"
        "import torch.nn as nn\n"
        "import torch.nn.functional as F\n"
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "\n"
        "torch.manual_seed(42)\n"
        "device = 'cuda' if torch.cuda.is_available() else 'cpu'\n"
        "print('device:', device)"
    ),
    "data_section": "## TinyShakespeare",
    "data_code": (
        "import urllib.request\n"
        "url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'\n"
        "urllib.request.urlretrieve(url, 'tinyshakespeare.txt')\n"
        "text = open('tinyshakespeare.txt').read()\n"
        "print(f'corpus: {len(text)} chars, {len(set(text))} unique')"
    ),
    "exercises": [
      ("Exercise 1 — Character-level tokenizer",
       "chars = sorted(set(text))\n"
       "stoi = {c: i for i, c in enumerate(chars)}\n"
       "itos = {i: c for c, i in stoi.items()}\n"
       "data = torch.tensor([stoi[c] for c in text], dtype=torch.long)\n"
       "n = int(0.9 * len(data))\n"
       "train_data, val_data = data[:n], data[n:]\n"
       "print('vocab:', len(chars), 'train:', len(train_data), 'val:', len(val_data))\n"),
      ("Exercise 2 — Implement the transformer block",
       "# YOUR TURN\n"
       "# class MultiHeadAttention(nn.Module): ...\n"
       "# class TransformerBlock(nn.Module): ...\n"
       "# class MiniTransformer(nn.Module): ...\n"
       "# 4 layers, 4 heads, d_model=256, context length=128. ~12M parameters.\n"),
      ("Exercise 3 — Training loop with eval",
       "# YOUR TURN\n"
       "# AdamW, lr=3e-4. Train for ~5000 iterations. Log train/val loss every 200 iter.\n"),
      ("Exercise 4 — Generate samples at three temperatures",
       "# YOUR TURN\n"
       "# After training, generate 200 chars starting from 'ROMEO:' at\n"
       "# temperature in {0.5, 0.8, 1.0}. Compare diversity vs coherence.\n"),
    ],
  },

  ("ia-generative", "03"): {
    "title": "Lab 2 — Sampling-strategy analysis",
    "goal": "On a 1B-parameter open model, generate the same prompt with five sampling strategies. Quantify diversity, coherence, factuality with simple metrics.",
    "deliverable": "Notebook with 5 sampling strategies × 10 samples each, plus a small evaluation table on three metrics.",
    "install": "torch transformers accelerate matplotlib",
    "imports": (
        "import torch\n"
        "from transformers import AutoModelForCausalLM, AutoTokenizer\n"
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "\n"
        "torch.manual_seed(42)\n"
        "device = 'cuda' if torch.cuda.is_available() else 'cpu'"
    ),
    "data_section": "## Load a small open model",
    "data_code": (
        "MODEL = 'EleutherAI/pythia-1b'\n"
        "tokenizer = AutoTokenizer.from_pretrained(MODEL)\n"
        "model = AutoModelForCausalLM.from_pretrained(MODEL).to(device).eval()\n"
        "print('parameters:', sum(p.numel() for p in model.parameters()) / 1e9, 'B')"
    ),
    "exercises": [
      ("Exercise 1 — Generate under each sampling strategy",
       "PROMPT = 'The capital of Cameroon is'\n"
       "STRATEGIES = {\n"
       "  'greedy':    {'do_sample': False},\n"
       "  'temp_0.5':  {'do_sample': True, 'temperature': 0.5},\n"
       "  'temp_1.0':  {'do_sample': True, 'temperature': 1.0},\n"
       "  'top_k_50':  {'do_sample': True, 'top_k': 50},\n"
       "  'top_p_0.9': {'do_sample': True, 'top_p': 0.9},\n"
       "}\n"
       "\n"
       "# YOUR TURN — generate 10 continuations per strategy at max_new_tokens=80.\n"),
      ("Exercise 2 — Quantify diversity",
       "# YOUR TURN\n"
       "# For each strategy, compute distinct-2 (fraction of unique bigrams across samples).\n"),
      ("Exercise 3 — Quantify coherence and factuality",
       "# YOUR TURN\n"
       "# Coherence: average per-token perplexity of each sample under the same model.\n"
       "# Factuality: did the sample correctly say 'Yaoundé'? Manual or string match.\n"),
    ],
  },

  ("ia-generative", "05"): {
    "title": "Lab 3 — LoRA fine-tune of a small open model",
    "goal": "Fine-tune Mistral-7B or Llama-3.1-8B with LoRA on a domain dataset. Compare zero-shot vs fine-tuned on a 50-example task-specific eval.",
    "deliverable": "Notebook with LoRA adapter weights, training loss curve, and a side-by-side eval table on a held-out 50-example test set.",
    "install": "torch transformers peft accelerate bitsandbytes datasets",
    "imports": (
        "import torch\n"
        "from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments\n"
        "from peft import LoraConfig, get_peft_model, TaskType\n"
        "from datasets import load_dataset\n"
        "from trl import SFTTrainer\n"
        "\n"
        "torch.manual_seed(42)"
    ),
    "data_section": (
        "## Pick a domain dataset\n\n"
        "The default below is a small medical-Q&A dataset; substitute your own if you have one."
    ),
    "data_code": (
        "DATASET = 'medalpaca/medical_meadow_medqa'\n"
        "BASE_MODEL = 'mistralai/Mistral-7B-Instruct-v0.2'\n"
        "ds = load_dataset(DATASET, split='train').select(range(1000))\n"
        "test = load_dataset(DATASET, split='train').select(range(1000, 1050))\n"
        "print('train:', len(ds), 'test:', len(test))"
    ),
    "exercises": [
      ("Exercise 1 — Zero-shot baseline",
       "# YOUR TURN\n"
       "# Load BASE_MODEL in 4-bit. Run zero-shot on the 50-example test set.\n"
       "# Record exact-match accuracy.\n"),
      ("Exercise 2 — LoRA fine-tune",
       "# YOUR TURN\n"
       "# Configure LoraConfig(r=16, lora_alpha=32, target_modules=['q_proj','v_proj']).\n"
       "# Train with SFTTrainer for 200-500 steps on the 1000-example train set.\n"),
      ("Exercise 3 — Side-by-side eval",
       "# YOUR TURN\n"
       "# Re-run on the same 50-example test set with the fine-tuned model.\n"
       "# Print a table: base accuracy vs fine-tuned accuracy.\n"),
    ],
  },

  ("ia-generative", "06"): {
    "title": "Lab 4 — RAG over a domain corpus",
    "goal": "Index a public-domain corpus in Chroma. Build retrieval + reranking + grounded generation. Evaluate on 30 questions.",
    "deliverable": "Notebook with the indexed corpus, retrieval pipeline, and an eval table for faithfulness, context relevance, answer correctness on 30 questions.",
    "install": "langchain chromadb sentence-transformers transformers torch pypdf",
    "imports": (
        "from langchain_chroma import Chroma\n"
        "from langchain_huggingface import HuggingFaceEmbeddings\n"
        "from langchain.text_splitter import RecursiveCharacterTextSplitter\n"
        "from langchain_community.document_loaders import PyPDFLoader\n"
        "import pathlib\n"
        "import urllib.request"
    ),
    "data_section": (
        "## Build a small corpus from open-access PDFs\n\n"
        "Replace these with your domain corpus. The defaults below are 3 WHO/AFRO PDFs."
    ),
    "data_code": (
        "URLS = [\n"
        "  # Replace with your real WHO/AFRO URLs — placeholders below.\n"
        "  'https://example.org/who-afro-1.pdf',\n"
        "  'https://example.org/who-afro-2.pdf',\n"
        "  'https://example.org/who-afro-3.pdf',\n"
        "]\n"
        "pathlib.Path('corpus').mkdir(exist_ok=True)\n"
        "for u in URLS:\n"
        "    fn = pathlib.Path('corpus') / u.rsplit('/', 1)[-1]\n"
        "    if not fn.exists():\n"
        "        print('skip (placeholder URL):', u)\n"
        "print('corpus dir:', list(pathlib.Path('corpus').glob('*.pdf')))"
    ),
    "exercises": [
      ("Exercise 1 — Load, chunk, and embed",
       "# YOUR TURN\n"
       "# Load each PDF with PyPDFLoader. Split with RecursiveCharacterTextSplitter\n"
       "# (chunk_size=600, chunk_overlap=80). Embed with sentence-transformers (all-MiniLM-L6-v2).\n"
       "# Persist to Chroma.\n"),
      ("Exercise 2 — Retrieval + grounded generation",
       "# YOUR TURN\n"
       "# Build a chain: query -> top-k=5 retrieval -> prompt with context -> LLM.\n"
       "# Use any open LLM (Mistral, Llama, Gemma) or an API.\n"),
      ("Exercise 3 — Evaluate on 30 held-out questions",
       "# YOUR TURN\n"
       "# Write 30 questions where you know the answer is in the corpus.\n"
       "# Evaluate by LLM-as-judge on three axes: faithfulness, context relevance, answer correctness.\n"),
    ],
  },

  # ML foundations -----------------------------------------------------------
  ("apprentissage-automatique", "03"): {
    "title": "Lab 1 — Classification on a clinical dataset",
    "goal": "Predict 30-day hospital readmission. Compare logistic regression, k-NN, Naive Bayes, plus a calibration-aware variant.",
    "deliverable": "Notebook with four models, accuracy + AUC + Brier calibration for each, and a 200-word memo on why calibration matters in clinical ML.",
    "install": "scikit-learn pandas matplotlib numpy",
    "imports": (
        "import numpy as np\n"
        "import pandas as pd\n"
        "import matplotlib.pyplot as plt\n"
        "from sklearn.linear_model import LogisticRegression\n"
        "from sklearn.neighbors import KNeighborsClassifier\n"
        "from sklearn.naive_bayes import GaussianNB\n"
        "from sklearn.calibration import CalibratedClassifierCV, calibration_curve\n"
        "from sklearn.model_selection import train_test_split\n"
        "from sklearn.metrics import accuracy_score, roc_auc_score, brier_score_loss\n"
        "from sklearn.datasets import fetch_openml\n"
        "\n"
        "np.random.seed(42)"
    ),
    "data_section": (
        "## A diabetes-readmission dataset\n\n"
        "Public alternative to MIMIC-IV demo (which requires PhysioNet credentialing). The actual cohort uses MIMIC-IV."
    ),
    "data_code": (
        "X, y = fetch_openml('diabetes', version=1, as_frame=True, return_X_y=True)\n"
        "y = (y == 'tested_positive').astype(int)\n"
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)\n"
        "print('train/test:', X_train.shape, X_test.shape)"
    ),
    "exercises": [
      ("Exercise 1 — Three baselines",
       "# YOUR TURN — fit logistic, k-NN, and Naive Bayes. Report accuracy and AUC.\n"),
      ("Exercise 2 — Calibration",
       "# YOUR TURN — compute Brier scores. Plot reliability diagrams for each.\n"),
      ("Exercise 3 — Calibrated variant",
       "# YOUR TURN — Wrap the best uncalibrated model in CalibratedClassifierCV.\n"
       "# Recompute Brier score and AUC.\n"),
    ],
  },

  ("apprentissage-automatique", "05"): {
    "title": "Lab 2 — SVM with a kernel sweep",
    "goal": "Train SVMs with linear, polynomial, and RBF kernels. Tune C and gamma. Compare against logistic regression baseline. Discuss the kernel-trick trade-off.",
    "deliverable": "Notebook with 3 kernels × tuned hyperparameters, a comparison table, and a 200-word note on the computational cost.",
    "install": "scikit-learn pandas matplotlib numpy",
    "imports": (
        "import numpy as np\n"
        "import pandas as pd\n"
        "import matplotlib.pyplot as plt\n"
        "from sklearn.svm import SVC\n"
        "from sklearn.linear_model import LogisticRegression\n"
        "from sklearn.preprocessing import StandardScaler\n"
        "from sklearn.compose import ColumnTransformer\n"
        "from sklearn.pipeline import Pipeline\n"
        "from sklearn.model_selection import GridSearchCV, train_test_split\n"
        "from sklearn.metrics import classification_report, roc_auc_score\n"
        "from sklearn.datasets import fetch_openml\n"
        "import time"
    ),
    "data_section": "## Adult Census Income (UCI, public)",
    "data_code": (
        "adult = fetch_openml('adult', version=2, as_frame=True)\n"
        "X = adult.data\n"
        "y = (adult.target == '>50K').astype(int)\n"
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)\n"
        "print('train/test:', X_train.shape, X_test.shape)"
    ),
    "exercises": [
      ("Exercise 1 — Logistic regression baseline",
       "# YOUR TURN\n"
       "# Build a preprocessing pipeline (one-hot for categoricals, scale for numerics).\n"
       "# Fit logistic regression. Report accuracy and AUC.\n"),
      ("Exercise 2 — SVM with three kernels",
       "# YOUR TURN\n"
       "# For each kernel in {linear, poly, rbf}, grid-search over C and gamma.\n"
       "# Train on a 20k random subsample of the train set (SVM scales poorly).\n"),
      ("Exercise 3 — Compare time and accuracy",
       "# YOUR TURN\n"
       "# Print: model, training time, AUC. Discuss the trade-off in 200 words.\n"),
    ],
  },

  ("apprentissage-automatique", "07"): {
    "title": "Lab 3 — Gradient boosting in production",
    "goal": "Train XGBoost, LightGBM, and CatBoost on the same dataset. Tune hyperparameters. Compare training time, inference time, accuracy. Audit feature importance with SHAP.",
    "deliverable": "Notebook with 3 trained gradient-boosting models, performance comparison, and SHAP plots for the best one.",
    "install": "xgboost lightgbm catboost shap scikit-learn pandas matplotlib numpy",
    "imports": (
        "import numpy as np\n"
        "import pandas as pd\n"
        "import matplotlib.pyplot as plt\n"
        "import xgboost as xgb\n"
        "import lightgbm as lgb\n"
        "from catboost import CatBoostClassifier\n"
        "import shap\n"
        "from sklearn.model_selection import train_test_split\n"
        "from sklearn.metrics import roc_auc_score\n"
        "from sklearn.datasets import fetch_openml\n"
        "import time\n"
        "\n"
        "np.random.seed(42)"
    ),
    "data_section": "## A real-but-public tabular dataset (substitute the Cameroon bank-loan when available)",
    "data_code": (
        "data = fetch_openml('credit-g', version=1, as_frame=True)\n"
        "X = data.data\n"
        "y = (data.target == 'good').astype(int)\n"
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)\n"
        "print('train/test:', X_train.shape, X_test.shape)"
    ),
    "exercises": [
      ("Exercise 1 — Train all three boosters",
       "# YOUR TURN\n"
       "# Train XGBoost, LightGBM, CatBoost with default hyperparameters.\n"
       "# Time each fit. Report test AUC.\n"),
      ("Exercise 2 — Tune the best one",
       "# YOUR TURN\n"
       "# For the best baseline, do a grid search over n_estimators, learning_rate, max_depth.\n"
       "# Report tuned AUC and how much the gain was.\n"),
      ("Exercise 3 — SHAP interpretation",
       "# YOUR TURN\n"
       "# Compute SHAP values for the tuned model on the test set.\n"
       "# Plot the global feature-importance summary. Identify one feature whose effect\n"
       "# is monotonic and one whose effect is non-monotonic.\n"),
    ],
  },

  ("apprentissage-automatique", "09"): {
    "title": "Lab 4 — Visualizing single-cell genomic data",
    "goal": "Apply PCA, t-SNE, and UMAP to a public single-cell RNA-seq dataset. Compare what each method preserves. Discuss the cost of nonlinear methods for downstream interpretation.",
    "deliverable": "Notebook with three 2-D embeddings of the same data, side-by-side, with a 200-word memo on when each is the right tool.",
    "install": "scanpy umap-learn scikit-learn matplotlib",
    "imports": (
        "import numpy as np\n"
        "import matplotlib.pyplot as plt\n"
        "import scanpy as sc\n"
        "from sklearn.decomposition import PCA\n"
        "from sklearn.manifold import TSNE\n"
        "import umap\n"
        "\n"
        "np.random.seed(42)"
    ),
    "data_section": "## 10x Genomics PBMC 3K (a canonical single-cell dataset)",
    "data_code": (
        "adata = sc.datasets.pbmc3k()\n"
        "sc.pp.normalize_total(adata, target_sum=1e4)\n"
        "sc.pp.log1p(adata)\n"
        "sc.pp.highly_variable_genes(adata, n_top_genes=2000)\n"
        "adata = adata[:, adata.var.highly_variable]\n"
        "X = adata.X.toarray()\n"
        "print('X shape:', X.shape)"
    ),
    "exercises": [
      ("Exercise 1 — PCA",
       "# YOUR TURN\n"
       "# Compute first 50 PCs. Plot PC1 vs PC2.\n"),
      ("Exercise 2 — t-SNE on PCA features",
       "# YOUR TURN\n"
       "# Run t-SNE (perplexity=30) on the first 50 PCs.\n"),
      ("Exercise 3 — UMAP on PCA features",
       "# YOUR TURN\n"
       "# Run UMAP (n_neighbors=15, min_dist=0.1) on the first 50 PCs.\n"),
      ("Exercise 4 — Compare visually",
       "# YOUR TURN\n"
       "# Plot all three side by side. Color by Louvain cluster (sc.tl.louvain).\n"
       "# Write 200 words on which is best for which downstream task.\n"),
    ],
  },

}


def build_notebook(spec: dict) -> dict:
    cells = [
        md(f"# {spec['title']}\n"
           f"\n"
           f"**Goal.** {spec['goal']}\n"
           f"\n"
           f"**What you ship.** {spec['deliverable']}\n"),
        md(f"## Setup\n"
           f"\n"
           f"Install the dependencies (one-time)."),
        code(f"# !pip install {spec['install']}"),
        code(spec["imports"]),
        md(spec["data_section"]),
        code(spec["data_code"]),
    ]
    for i, (title, body) in enumerate(spec["exercises"], start=1):
        cells.append(md(f"## {title}"))
        cells.append(code(body))
    cells.append(md(
        "## Done?\n"
        "\n"
        "Submit per the cohort schedule. Peer review pairing announced the following Monday."
    ))
    return notebook(cells)


def main() -> int:
    written = 0
    for (slug, week_num), spec in LABS.items():
        labs_dir = REPO / "courses" / slug / "cohort" / "labs"
        labs_dir.mkdir(parents=True, exist_ok=True)
        # Read the notebook filename from the data file
        data = yaml.safe_load((REPO / "_data" / f"{slug}.yml").read_text(encoding="utf-8"))
        week = next(w for w in data["weeks"] if w["number"] == week_num)
        nb_name = week.get("code_lab", {}).get("notebook")
        if not nb_name:
            print(f"  skip {slug} w{week_num}: no notebook name in data file")
            continue
        nb_path = labs_dir / nb_name
        nb_path.write_text(json.dumps(build_notebook(spec), indent=1) + "\n", encoding="utf-8")
        print(f"  wrote {nb_path.relative_to(REPO)}")
        written += 1
    print(f"\n{written} notebooks generated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
