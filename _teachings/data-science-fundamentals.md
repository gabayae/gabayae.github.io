---
layout: course
title: "Introduction to Topological Data Analysis"
description: "A workshop-style course introducing the foundations of TDA — persistent homology, filtrations, and applications to data science. Designed for graduate students and researchers at AIMS and partner institutions."
instructor: Dr. Yae Ulrich Gaba
year: 2024
term: Workshop
location: AIMS Rwanda / Quantum Leap Africa, Kigali
time: "Self-paced / Workshop sessions"
course_id: intro-tda
schedule:
  - week: 1
    date: "Session 1"
    topic: "What is Topology? From Abstract Spaces to Data"
    description: "Topological spaces, continuous maps, homeomorphisms. Motivation: why shape matters in data."
    materials:
      - name: Slides
        url: https://github.com/gabayae

  - week: 2
    date: "Session 2"
    topic: "Simplicial Complexes and Filtrations"
    description: "Simplices, Vietoris-Rips complexes, Cech complexes. Building filtrations from point clouds."
    materials:
      - name: Notebook
        url: https://github.com/gabayae

  - week: 3
    date: "Session 3"
    topic: "Persistent Homology"
    description: "Homology groups, Betti numbers, persistence diagrams and barcodes. The stability theorem."
    materials:
      - name: Notebook
        url: https://github.com/gabayae

  - week: 4
    date: "Session 4"
    topic: "TDA in Practice: Python Tools"
    description: "Hands-on: Ripser, GUDHI, scikit-tda. Computing persistence from real datasets."
    materials:
      - name: Coding Lab
        url: https://github.com/gabayae

  - week: 5
    date: "Session 5"
    topic: "Applications: TDA Meets Machine Learning"
    description: "Persistence landscapes, vectorization, TDA features in ML pipelines. Case studies."
    materials:
      - name: Notebook
        url: https://github.com/gabayae
---

## Course Overview

This workshop-style course introduces the mathematical foundations of **Topological Data Analysis (TDA)** and demonstrates how topological methods can extract meaningful structure from complex datasets.

Participants will learn:
- The mathematical language of topology relevant to data analysis
- How to compute persistent homology from point clouds and graphs
- Practical Python tools for TDA (Ripser, GUDHI, scikit-tda)
- How to integrate TDA features into machine learning pipelines

## Prerequisites

- Linear algebra fundamentals
- Basic Python programming
- Familiarity with data science concepts (helpful but not required)

## References

- *The Shape of Data* by Farrelly & Gaba (No Starch Press)
- *Computational Topology* by Edelsbrunner & Harer
- *Topological Data Analysis with Applications* by Carlsson & Vejdemo-Johansson
