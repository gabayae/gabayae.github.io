---
layout: workshop
permalink: /workshops/geometric-deep-learning/en/
lang: en
title: "Geometric Deep Learning"
tagline: "Neural networks on graphs, manifolds, and point clouds — grounded in group theory, differential geometry, and topology."
description: "4-day workshop: GNNs, manifold learning, equivariant architectures."

# --- Sidebar metadata ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "4 days (≈ 24 hours)"
level: "Advanced"
format: "On-site, live online, or hybrid"
languages: "English &amp; French"
certificate: "Certificate of completion"

# --- Materials links shown in the sidebar ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/geometric-deep-learning

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Workshop inquiry — Geometric Deep Learning"
---

## Program Overview

This workshop explores the mathematical foundations and practical applications of geometric deep learning — neural networks that operate on graphs, manifolds, point clouds, and other non-Euclidean domains. Grounded in group theory, differential geometry, and topology, participants learn to build and apply Graph Neural Networks (GNNs), equivariant architectures, and manifold-aware models to problems in molecular science, social networks, and beyond.

### Software Requirements

- Python 3.10+
- PyTorch 2.0+
- PyTorch Geometric (torch-geometric)
- Libraries: networkx, matplotlib, rdkit (for molecular data), open3d (for point clouds)
- Optional: wandb for experiment tracking

### Day 1: Foundations — Graphs, Symmetry & Message Passing

**Objectives:** Understand why geometry matters for deep learning and implement basic GNNs.

- **Why Geometric Deep Learning?** — Limitations of MLPs and CNNs on non-Euclidean data. The GDL blueprint: domains (grids, graphs, groups, manifolds), symmetries, and the 5G's of GDL
- **Group Theory for Deep Learning** — Symmetry groups, invariance vs. equivariance, why CNNs are translation-equivariant, extending equivariance to other symmetries
- **Graph Representations** — Adjacency matrices, edge lists, node/edge features, graph-level features. Building graphs from real data. NetworkX basics
- **Message Passing Neural Networks** — The MPNN framework: message, aggregation, update. Permutation invariance/equivariance. GCN (Kipf & Welling), GraphSAGE, GIN
- **PyTorch Geometric Basics** — Data objects, DataLoader, building a GNN from scratch with MessagePassing base class, Karate Club example

**Lab 1:** Implement a GCN from scratch using the MPNN framework. Then use PyTorch Geometric to build and train a node classification model on the Cora citation network. Visualize learned node embeddings with t-SNE.

**Homework:** Experiment with different GNN architectures (GCN, GAT, GIN) on Cora and compare performance.

### Day 2: Spectral Methods & Advanced Architectures

**Objectives:** Understand the spectral perspective on graph convolutions and advanced GNN designs.

- **Spectral Graph Theory** — Graph Laplacian, eigenvalues and eigenvectors, spectral decomposition, graph Fourier transform, Chebyshev polynomials, spectral vs. spatial convolutions
- **Attention on Graphs** — Graph Attention Networks (GAT): multi-head attention, attention coefficients, comparison with GCN. Transformer-style architectures for graphs
- **Graph-Level Tasks** — Global pooling (mean, sum, max), hierarchical pooling (DiffPool, TopKPool, SAGPool), readout functions, graph classification pipelines
- **Oversmoothing & Expressivity** — The oversmoothing problem in deep GNNs, the WL test and GNN expressivity, skip connections, JumpingKnowledge networks, positional encodings

**Lab 2:** Build a graph classification pipeline using PyTorch Geometric: load a molecular dataset (MUTAG or PROTEINS), implement global and hierarchical pooling, train and evaluate. Experiment with depth and pooling strategies.

**Homework:** Compare GAT vs. GCN vs. GIN on graph classification accuracy and training time.

### Day 3: Manifolds, Point Clouds & Equivariance

**Objectives:** Extend deep learning to manifolds, point clouds, and design equivariant architectures.

- **Learning on Manifolds** — Meshes, surfaces, intrinsic vs. extrinsic geometry. Geodesic distances, heat kernels, Laplace-Beltrami operator. MeshCNN and DiffusionNet
- **Point Cloud Processing** — PointNet and PointNet++: symmetric functions for permutation invariance, local feature aggregation, hierarchical processing. Dynamic graph CNNs (DGCNN)
- **Equivariant Neural Networks** — SE(3)-equivariance, Tensor Field Networks, EGNN (E(n) Equivariant GNNs), SchNet for molecular dynamics. Why equivariance improves data efficiency
- **Topological Features for GDL** — Persistent homology as node/graph features, filtration learning, TopologyLayer, combining TDA with GNNs

**Lab 3:** Implement a point cloud classifier using PointNet (from scratch in PyTorch) on ModelNet10 or ShapeNet. Then augment a GNN with topological features (Betti numbers, persistence statistics) and measure the improvement.

**Homework:** Apply EGNN to a molecular property prediction task and compare with standard GNN.

### Day 4: Applications & Capstone

**Objectives:** Apply GDL to real-world domains and complete a capstone project.

- **Molecular Property Prediction** — Molecular graphs, SMILES to graph conversion, QM9 dataset, SchNet, DimeNet, SphereNet. Drug discovery applications
- **Social Network Analysis** — Community detection with GNNs, link prediction, node influence, temporal graphs, heterogeneous graphs
- **Other Applications** — Protein structure prediction (AlphaFold context), traffic prediction, recommendation systems, physics simulation, weather forecasting
- **Capstone Project Work** — Implement a complete GDL pipeline on a chosen application
- **Presentations & Wrap-Up** — Project demos, discussion on GDL frontiers, resources, certificates

**Lab 4 (Capstone):** Choose one project:
- **Molecular:** Predict molecular properties (solubility, toxicity) using GNNs on MoleculeNet
- **Social:** Community detection or link prediction on a real social network dataset
- **3D:** Point cloud classification or segmentation on ModelNet/ShapeNet
- **Custom:** Apply GDL to a problem from your research with appropriate graph construction

### Assessment

- **Daily labs** (40%) — Working implementations and analysis
- **Capstone project** (40%) — Complete GDL application with evaluation
- **Participation** (20%) — Engagement, homework, and discussions

### Resources

- [Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, Gauges (Bronstein et al.)](https://geometricdeeplearning.com/)
- [PyTorch Geometric Documentation](https://pytorch-geometric.readthedocs.io/)
- [Graph Representation Learning Book (Hamilton)](https://www.cs.mcgill.ca/~wlh/grl_book/)
- [The Shape of Data](https://nostarch.com/shapeofdata)
- [Stanford CS224W: Machine Learning with Graphs](http://web.stanford.edu/class/cs224w/)

## Learning Outcomes

By the end of this workshop, participants will be able to:

1. Understand the mathematical principles behind geometric deep learning (symmetry, invariance, equivariance)
2. Implement message-passing neural networks and GNN variants
3. Work with PyTorch Geometric for graph-level and node-level tasks
4. Apply spectral and spatial methods for graph convolutions
5. Understand manifold learning and equivariant architectures
6. Apply GDL to real-world problems (molecular property prediction, social network analysis, point cloud classification)

## Who Should Attend

Advanced ML practitioners and researchers working on non-Euclidean data: molecular graphs, social networks, 3D shapes, meshes, point clouds. Graduate students in computational chemistry, drug discovery, computer vision, or network science. Engineers building recommendation systems or systems that reason over relational data. Researchers in physics, biology, or chemistry who want to apply equivariant architectures.

**Prerequisites:**

- Python programming with PyTorch (tensors, autograd, nn.Module)
- Linear algebra (eigenvalues, spectral decomposition)
- Machine learning basics (training loops, loss functions, optimization)
- Basic graph theory (nodes, edges, adjacency matrices) is helpful but not required

## Brochure

Lecture notes and lab notebooks are linked in the sidebar.

For a printable one-page brochure suitable for forwarding to a program committee, conference organizer, or corporate L&D team, write to <a href="mailto:gabayae2@gmail.com?subject=Brochure%20request%20%E2%80%94%20Geometric%20Deep%20Learning">gabayae2@gmail.com</a> with the audience size and intended delivery dates.
