---
layout: page
permalink: /workshops/math-foundations-modern-ai/en/
title: "Mathematical Foundations of Modern AI — 5-day Workshop"
description: "5-day workshop on the mathematical structures behind modern AI: linear algebra, optimization, probability, modelling, evaluation."
lang: en
---

**Instructor:** Dr. Yaé Ulrich Gaba
**Duration:** 5 days
**Level:** Intermediate — no advanced math background required
**Language:** English

---

## Overview

Modern AI is moving fast, but the ideas that actually power today's systems are stable and accessible. This workshop builds the mathematical intuition and modelling vocabulary needed to understand what is happening under the hood — across supervised, unsupervised, and generative models.

The goal is not to turn participants into deep-learning specialists. It is to give them the mental structures to evaluate a method, talk to a technical team, frame a business problem as a learning problem, and decide when (and when not) to deploy an AI tool.

## Audience

Engineers, product managers, analysts, and technical team leads who make decisions about AI. Practitioners who work alongside ML teams and want a real grasp of the foundations. Researchers from other disciplines who want to move from talking about AI to using it.

## Prerequisites

Comfortable with basic mathematics (high-school and first-year undergraduate level) and curious about applied problem-solving. No advanced prerequisites.

## Learning Outcomes

By the end of the workshop, participants will be able to:

1. Understand the core ideas in linear algebra, optimization, and probability that underpin modern AI systems.
2. Describe how common ML/AI models (MLPs, autoencoders, diffusion models) are structured, trained, and evaluated.
3. Frame a real-world problem in the structured language of an AI pipeline.
4. Pick an architecture, a loss function, and an inductive bias suited to the application domain.
5. Assess model reliability through statistical reasoning, validation methods, and awareness of common failure modes.
6. Make technically grounded decisions about deploying AI tools.

## Tools

Python 3.10+, NumPy, PyTorch, matplotlib. Jupyter notebooks runnable locally or on Google Colab.

---

## Schedule

### Day 1 — Linear Algebra and Parametric Models

**Theme:** Representing data and models with vectors, matrices, and transformations.

| Time | Topic |
|------|-------|
| 09:00–10:30 | **Vector spaces, linear maps, dimensionality** — From feature vectors to latent space. The idea of a learned representation. |
| 10:45–12:30 | **From the perceptron to the MLP** — Layers, non-linear activations, why composing linear functions is not enough. |
| 14:00–15:30 | **Embeddings and autoencoders** — Learning compact representations. Geometry of latent space. |
| 15:45–17:00 | **Lab 1 — Visualize layers and feature maps of a pre-trained network.** |

---

### Day 2 — Calculus and Optimization

**Theme:** Loss functions and gradient-based learning.

| Time | Topic |
|------|-------|
| 09:00–10:30 | **Multivariate derivatives, chain rule** — Why the gradient is the right direction. |
| 10:45–12:30 | **Gradient descent, SGD, Adam** — Learning rate, learning curves, hyperparameters. |
| 14:00–15:30 | **Backpropagation and differentiable programming** — How PyTorch computes a gradient you didn't ask for. |
| 15:45–17:00 | **Lab 2 — Train a neural network end-to-end.** |

---

### Day 3 — Probability and Generative Modelling

**Theme:** Randomness as a modelling tool; learning from and sampling distributions.

| Time | Topic |
|------|-------|
| 09:00–10:30 | **Distributions, densities, likelihood** — The probabilistic language of learning. |
| 10:45–12:30 | **Generative models: VAEs, diffusion, score-based methods** — How to generate an image (or text) from noise. |
| 14:00–15:30 | **Noise processes and inversion** — The intuition behind diffusion. |
| 15:45–17:00 | **Lab 3 — Train a simple diffusion model.** |

---

### Day 4 — Modelling for AI

**Theme:** Turning a messy problem into a structured mathematical one.

| Time | Topic |
|------|-------|
| 09:00–10:30 | **Constrained and unconstrained optimization, regularization** — When adding a constraint changes everything. |
| 10:45–12:30 | **Invariance and equivariance** — Why a CNN beats an MLP on images, and the generalization of that idea. |
| 14:00–15:30 | **Specialized architectures: CNNs, GNNs, attention** — Inductive bias as a modelling choice. |
| 15:45–17:00 | **Lab 4 — Compare model choices on a graph-learning task.** |

---

### Day 5 — Evaluating AI Models

**Theme:** Generalization, reliability, and informed decisions.

| Time | Topic |
|------|-------|
| 09:00–10:30 | **Basic statistics, bias–variance, overfitting** — Reading a learning curve. |
| 10:45–12:30 | **Validation, calibration, uncertainty** — Beyond mean accuracy. |
| 14:00–15:30 | **Adversarial examples and out-of-distribution data** — Why a model that works in the lab fails in production. |
| 15:45–17:00 | **Lab 5 — Compare models under distribution shift. Wrap-up.** |

---

## Assessment

- **Daily labs** (60%) — Working implementations and analysis.
- **Final mini-project** (30%) — Frame a real problem as an AI pipeline and defend the modelling choices.
- **Participation** (10%) — Engagement, questions, discussion.

## Resources

- Goodfellow, Bengio, Courville — *Deep Learning* (MIT Press, free online)
- Bishop & Bishop — *Deep Learning: Foundations and Concepts* (Springer, 2024)
- Murphy — *Probabilistic Machine Learning* (MIT Press, free online)
- Strang — *Linear Algebra and Learning from Data*
- Ho et al. — *Denoising Diffusion Probabilistic Models* (NeurIPS 2020, [arXiv:2006.11239](https://arxiv.org/abs/2006.11239))

## Certificate

Participants who complete all labs and the mini-project receive a certificate of completion.
