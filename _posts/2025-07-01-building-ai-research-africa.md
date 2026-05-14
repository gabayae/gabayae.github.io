---
layout: post
title: "Building AI research labs in Africa: lessons from AIRINA Labs"
date: 2025-07-01
description: "Reflections on founding and growing an AI research lab on the continent — what works, what's hard, and why it matters."
tags: [Africa, AI, research, data-science]
categories: [research]
giscus_comments: true
related_posts: true
toc:
  sidebar: left
---

## From the landscape post to actually building one

A few months ago I [wrote about the broader African AI landscape](/en/blog/2025/african-ai-landscape/). Since then, I've been working on the inside of one of the institutions, as Head of R&D at **AIRINA Labs**. This post is what the view looks like from there.

Building an AI lab on the continent isn't a matter of porting a North American playbook. Some of the constraints are different, some of the assets are different, and several of the design choices flip.

## What we work on

Three active lines at AIRINA:

- **Topological and geometric methods**, applied to data problems. We lean on the mathematical training already in place at AIMS, IMSP, and the rest of the network.
- **Data-efficient methods**: what to do when the dataset is smaller, noisier, or more partial than the textbook assumes. This is most of what we see.
- **Responsible AI**: interpretability and fairness audits, with the local-values part not handled as an afterthought.

## Lessons Learned

### 1. Start with the mathematics

The mathematical training across AIMS, CIMPA, and national programs in francophone and anglophone Africa is genuinely strong. We use that. Instead of competing head-on with compute-heavy approaches, we work on theory-driven methods (TDA, geometric deep learning, metric-space methods) where the math earns most of the performance and the compute requirement stays moderate.

### 2. Build local, collaborate globally

A lab on the continent shouldn't be an island. We have active collaborations in Europe, North America, and across Africa. But the research questions come from local needs (healthcare data challenges, agricultural monitoring, financial inclusion) and the deployment target is local. The collaboration imports methods; the problem statement stays anchored here.

### 3. Invest in people, not just papers

The binding constraint isn't funding or compute. It's talent retention. Keeping good people requires several things to work simultaneously: compensation that's competitive against local cost of living (not Silicon Valley), intellectual freedom on fundamental questions, a visible path from research to deployed system, and a community that takes local work seriously rather than treating it as the second-best.

### 4. Infrastructure is a smaller problem than it used to be

Cloud access, open-source tooling, and more efficient algorithms have together made compute less of a bottleneck than it was five years ago. For most of the problems we work on, a TDA pipeline on a workstation will beat brute-force deep learning on a GPU cluster. Asking the right mathematical question does more for performance than renting more GPUs.

### 5. Teach as you build

We don't separate research and teaching. Every project takes on at least one masters or PhD-track student. Workshops and the [ACAS](https://acas-yde.org/) partnership absorb more, and the lab gains future colleagues from inside the same network.

## The bigger picture

Replicating the Silicon Valley model isn't a goal. The combination of strong mathematics and operationally consequential problems sitting in front of you produces a different research style than the one optimized for paper throughput, and I think that style has a real contribution to make.

A diverse problem set produces a diverse method set. Some of what comes out of African labs in the next decade will look unfamiliar to North American reviewers, and that's how the field moves forward rather than in circles.

## What's next

Three lines we're pushing on:

- Topological methods for health data, with regional health organizations as partners.
- Open-source TDA tooling targeting low-resource environments specifically — not "scaled-down" versions, but tooling designed for the constraint from the start.
- Pan-African mailing-list and collaboration infrastructure for mathematical scientists working on AI. Concrete, not symbolic.

If you want to collaborate, my email is on the about page.
