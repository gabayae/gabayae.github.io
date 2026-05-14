---
layout: post
title: "LLMs meet topology: can TDA improve language model interpretability?"
date: 2025-06-15
description: "Exploring how topological data analysis can shed light on the inner workings of large language models — from attention geometry to representation topology."
tags: [topology, TDA, LLMs, interpretability, machine-learning]
categories: [research]
giscus_comments: true
related_posts: true
toc:
  sidebar: left
---

## The interpretability problem

Most LLM interpretability work uses linear probes, attention visualization, or the mechanistic interpretability toolkit. Each treats hidden states as roughly linear, or focuses on individual circuits. The nonlinear, multi-scale structure of representation space (the part TDA was designed for) usually goes unstudied.

## Topology of representations

Each layer of a network maps inputs into a different high-dimensional space. The points live on a manifold of unknown shape. TDA characterizes that shape without assuming linearity.

Consider the hidden states $$\mathbf{h}_1, \ldots, \mathbf{h}_n \in \mathbb{R}^d$$ at a given layer. Using persistent homology, we can compute:

- **$$H_0$$ (connected components):** How many distinct clusters of representations exist? Do semantically similar tokens cluster together?
- **$$H_1$$ (loops):** Are there circular structures in representation space? These can indicate periodic or cyclical relationships the model has learned.
- **$$H_2$$ (voids):** Higher-dimensional cavities may reveal complex organizational principles.

## Attention as a geometric object

Build a simplicial complex from attention by connecting tokens with strong mutual attention. The resulting object has topology, and several 2024–25 preprints argue that this topology tracks linguistic structure: persistent 1-cycles correspond to syntactic dependencies, persistent connected components across layers correspond to coreference chains, and the topological complexity of attention patterns rises with model capability. The evidence is still thin enough that I'd treat these as testable hypotheses rather than established results.

## Detecting distribution shift

One practical application: persistence diagrams as an OOD detector. The topological signature of in-distribution representations sits in a characteristic region of diagram space. Anomalous text moves it. The signal is coordinate-free and scale-invariant, so it composes with standard uncertainty estimation rather than competing with it.

## Open questions

Four directions I think are worth pursuing:

1. **Can TDA features predict hallucination?** If the topological structure of internal representations differs when a model confabulates vs. retrieves factual information, persistence-based features could serve as a hallucination detector.

2. **Layer-wise topology.** How does the topological complexity of representations evolve across layers? Does the model "simplify" the topology as it approaches the output?

3. **Topological fine-tuning.** Can we add a topological regularization term to the loss function, encouraging representations with desirable geometric properties?

4. **Cross-model comparison.** Do models with similar capabilities share topological signatures, even if trained differently?

## Why I think this matters

TDA gives interpretability research a coordinate-free vocabulary. That matters because most current methods are bound to the geometry of a specific model: linear probes are linear in this model's basis, attention patterns are this model's attention patterns. Persistent homology talks about shape in a way that survives a basis change. If a topological feature shows up in GPT-4, LLaMA, and Claude at the same point in the network, that's an architectural fact about transformers, not an artifact of one training run.

The tools (persistent homology, Mapper, persistence landscapes) are in place. The application work on real models is the bottleneck.
