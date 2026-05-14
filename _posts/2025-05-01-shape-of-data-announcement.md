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

**The Shape of Data: Geometry-Based Machine Learning and Data Analysis in R**, co-authored with [Colleen M. Farrelly](https://scholar.google.com/), is out from [No Starch Press](https://nostarch.com/shapeofdata). I've been working on this for a long time and I'm glad it's finally in print.

Several years went into distilling the mathematical ideas I care most about (topology, geometry, metric spaces) into something a working data scientist can use on Monday morning. It's the book I wish I had when I first started thinking about how topological ideas could improve machine learning.

## What's Inside

The book covers four major themes, each building on the last:

**Topological Data Analysis (TDA).** Persistent homology from first principles: simplicial complexes and filtrations, then persistence diagrams, barcodes, and persistence landscapes. Mapper gets its own chapter, with worked examples on real datasets.

**Metric geometry.** Distance-based methods are the backbone of much of ML, but most practitioners never look beyond Euclidean distance. We cover alternative metrics, embeddings into metric spaces, and curvature-based features that capture local and global geometry. For readers familiar with my research on quasi-metric spaces, this chapter connects those abstract ideas to concrete data analysis tasks.

**Network science.** Graph-based representations show up everywhere: social networks, molecular structures, citation graphs. We work through community detection, graph filtrations, and persistent homology on networks.

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

## Who it's for

Three audiences in mind: data scientists who want geometric tools beyond Euclidean distance, mathematicians curious about ML applications, and graduate students working at the intersection of topology and data. The level assumes undergraduate math and basic programming; there's enough depth for working researchers too.

For my students at AIMS and in the Data Science Makers community, the book is also an argument. The abstract spaces I worked on during my PhD (quasi-metrics, generalized metric spaces, asymmetric topologies) aren't disconnected from applied work. They're the substrate the applied work sits on.

## Get the Book

- **Publisher:** [No Starch Press](https://nostarch.com/shapeofdata)
- **Amazon:** [ISBN 9781718503083](https://www.amazon.com/dp/1718503083)
- **ISBN:** 9781718503083

If the book helps connect the topology and geometry side of the math to the data-analysis side for you, that's the goal. If you read it and have suggestions for a second edition, send them — I read everything.
