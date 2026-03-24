---
layout: post
title: "Announcing: The Shape of Data"
date: 2025-05-01
description: "Our book on geometry-based machine learning is now available from No Starch Press."
tags: [TDA, data-science, machine-learning, topology]
categories: [research]
giscus_comments: true
related_posts: true
---

I am thrilled to announce that **The Shape of Data: Geometry-Based Machine Learning and Data Analysis in R**, co-authored with [Colleen M. Farrelly](https://scholar.google.com/), is now available from [No Starch Press](https://nostarch.com/shapeofdata).

This book represents several years of work distilling the mathematical ideas I care most about — topology, geometry, metric spaces — into a practical guide that data scientists and ML practitioners can use immediately. It is the book I wish I had when I first started thinking about how topological ideas could improve machine learning.

## What's Inside

The book covers four major themes, each building on the last:

**Topological Data Analysis (TDA).** We introduce persistent homology from the ground up, starting with simplicial complexes and filtrations, and building to persistence diagrams, barcodes, and persistence landscapes. The Mapper algorithm gets its own treatment, with worked examples showing how to use it for exploratory data analysis on real datasets.

**Metric geometry.** Distance-based methods are the backbone of much of ML, but most practitioners never look beyond Euclidean distance. We cover alternative metrics, embeddings into metric spaces, and curvature-based features that capture local and global geometry. For readers familiar with my research on quasi-metric spaces, this chapter connects those abstract ideas to concrete data analysis tasks.

**Network science.** Graph-based representations are everywhere — social networks, molecular structures, citation graphs. We show how topological and geometric tools apply to graph data, including community detection, graph filtrations, and persistent homology on networks.

**Practical R implementations.** Every method in the book comes with runnable R code. We chose R for its strong statistical ecosystem and its excellent TDA packages (the TDA package, GUDHI bindings, and others). Here is a taste of what a TDA pipeline looks like:

```r
library(TDA)

# Generate a noisy circle
n <- 200
theta <- runif(n, 0, 2 * pi)
X <- cbind(cos(theta), sin(theta)) + 0.05 * matrix(rnorm(2*n), ncol=2)

# Compute the Rips filtration and persistent homology
diag <- ripsDiag(X, maxdimension = 1, maxscale = 2)

# Plot the persistence diagram
plot(diag[["diagram"]])
```

## Who It's For

Whether you are a data scientist looking to add geometric tools to your toolkit, a mathematician curious about ML applications, or a graduate student exploring the intersection of topology and data — this book has something for you. We deliberately wrote it at a level accessible to someone with undergraduate mathematics and basic programming experience, while including enough depth to be useful for researchers.

For my students at AIMS and in the Data Science Makers community, this book is also a statement about the kind of mathematics that matters for modern data analysis. The abstract spaces I studied during my PhD — quasi-metrics, generalized metric spaces, asymmetric topologies — are not disconnected from practice. They are the mathematical substrate on which data analysis rests.

## Get the Book

- **Publisher:** [No Starch Press](https://nostarch.com/shapeofdata)
- **Amazon:** [ISBN 9781718503083](https://www.amazon.com/dp/1718503083)
- **ISBN:** 9781718503083

I hope this book helps bridge the gap between the beautiful mathematics of topology and geometry, and the practical challenges of modern data analysis. If you read it and find it useful — or if you have suggestions for a second edition — I would love to hear from you.
