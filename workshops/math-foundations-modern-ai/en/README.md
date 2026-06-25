---
layout: workshop
permalink: /workshops/math-foundations-modern-ai/en/
lang: en
title: "Mathematical Foundations of Modern AI"
tagline: "The math behind today's AI systems — in five days, with no advanced math required."
description: "5-day workshop on the mathematical structures behind modern AI: linear algebra, optimization, probability, modelling, evaluation."

# --- Sidebar metadata ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "5 days (≈ 30 hours)"
level: "Intermediate — no advanced math background required"
format: "On-site, live online, or hybrid"
languages: "English &amp; French"
certificate: "Certificate of completion"

# --- Materials links shown in the sidebar ---
syllabus_pdf: /workshops/math-foundations-modern-ai/en/notes.pdf
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/math-foundations-modern-ai/notebooks

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Workshop inquiry — Mathematical Foundations of Modern AI"
---

## Program Overview

Modern AI is moving fast, but the ideas that actually power today's systems are stable and accessible. This workshop builds the mathematical intuition and modelling vocabulary needed to understand what is happening under the hood — across supervised, unsupervised, and generative models.

The goal is not to turn participants into deep-learning specialists. It is to give them the mental structures to evaluate a method, talk to a technical team, frame a business problem as a learning problem, and decide when (and when not) to deploy an AI tool.

The 5 days alternate between morning lectures and afternoon hands-on labs. All labs run on Google Colab (free tier) or any local Python 3.10+ environment with PyTorch.

### Day 1 — Linear algebra and parametric models

**Theme:** representing data and models with vectors, matrices, and transformations.

- **Vector spaces, linear maps, dimensionality** — from feature vectors to latent space; the idea of a learned representation.
- **From the perceptron to the MLP** — layers, non-linear activations, why composing linear functions is not enough.
- **Embeddings and autoencoders** — learning compact representations; geometry of latent space.
- **Lab 1** — visualize layers and feature maps of a pre-trained network.

### Day 2 — Calculus and optimization

**Theme:** loss functions and gradient-based learning.

- **Multivariate derivatives, chain rule** — why the gradient is the right direction.
- **Gradient descent, SGD, Adam** — learning rate, learning curves, hyperparameters.
- **Backpropagation and differentiable programming** — how PyTorch computes a gradient you didn't ask for.
- **Lab 2** — train a neural network end-to-end.

### Day 3 — Probability and generative modelling

**Theme:** randomness as a modelling tool; learning from and sampling distributions.

- **Distributions, densities, likelihood** — the probabilistic language of learning.
- **Generative models: VAEs, diffusion, score-based methods** — how to generate an image (or text) from noise.
- **Noise processes and inversion** — the intuition behind diffusion.
- **Lab 3** — train a simple diffusion model.

### Day 4 — Modelling for AI

**Theme:** turning a messy problem into a structured mathematical one.

- **Constrained and unconstrained optimization, regularization** — when adding a constraint changes everything.
- **Invariance and equivariance** — why a CNN beats an MLP on images, and the generalization of that idea.
- **Specialized architectures: CNNs, GNNs, attention** — inductive bias as a modelling choice.
- **Lab 4** — compare model choices on a graph-learning task.

### Day 5 — Evaluating AI models

**Theme:** generalization, reliability, and informed decisions.

- **Basic statistics, bias–variance, overfitting** — reading a learning curve.
- **Validation, calibration, uncertainty** — beyond mean accuracy.
- **Adversarial examples and out-of-distribution data** — why a model that works in the lab fails in production.
- **Lab 5** — compare models under distribution shift; wrap-up.

### Assessment

- **Daily labs** (60 %) — working implementations and analysis.
- **Final mini-project** (30 %) — frame a real problem as an AI pipeline and defend the modelling choices.
- **Participation** (10 %) — engagement, questions, discussion.

### Reading list

- Goodfellow, Bengio & Courville, *Deep Learning* (MIT Press, free online).
- Bishop & Bishop, *Deep Learning: Foundations and Concepts* (Springer, 2024).
- Murphy, *Probabilistic Machine Learning* (MIT Press, free online).
- Strang, *Linear Algebra and Learning from Data*.
- Ho, Jain & Abbeel, "Denoising Diffusion Probabilistic Models", NeurIPS 2020 ([arXiv:2006.11239](https://arxiv.org/abs/2006.11239)).
- Vaswani et al., "Attention Is All You Need", NeurIPS 2017 ([arXiv:1706.03762](https://arxiv.org/abs/1706.03762)).

## Learning Outcomes

By the end of the workshop, participants will be able to:

1. Understand the core ideas in linear algebra, optimization, and probability that underpin modern AI systems.
2. Describe how common ML / AI models (MLPs, autoencoders, diffusion models) are structured, trained, and evaluated.
3. Frame a real-world problem in the structured language of an AI pipeline.
4. Pick an architecture, a loss function, and an inductive bias suited to the application domain.
5. Assess model reliability through statistical reasoning, validation methods, and awareness of common failure modes.
6. Make technically grounded decisions about deploying AI tools.

## Who Should Attend

Engineers, product managers, analysts, and technical team leads who make decisions about AI. Practitioners who work alongside ML teams and want a real grasp of the foundations. Researchers from other disciplines who want to move from talking about AI to using it.

Comfortable with high-school and first-year undergraduate mathematics (vectors, functions, derivatives, basic probability). Familiarity with Python helps for the hands-on labs but is not required for the lectures themselves. **No advanced prerequisites.**

## Brochure

Lecture notes and lab notebooks are linked in the sidebar.

For a printable one-page brochure suitable for forwarding to a program committee, conference organizer, or corporate L&D team, write to <a href="mailto:gabayae2@gmail.com?subject=Brochure%20request%20%E2%80%94%20Mathematical%20Foundations%20of%20Modern%20AI">gabayae2@gmail.com</a> with the audience size and intended delivery dates.
