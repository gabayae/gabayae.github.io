# Applied Bayesian Statistics — 4-Day Workshop

**Instructor:** Dr. Yaé Ulrich Gaba
**Duration:** 4 days (24 hours)
**Level:** Intermediate to Advanced
**Language:** English

---

## Overview

This workshop provides a practical introduction to Bayesian statistics with emphasis on modelling, computation, and real-world applications. Participants learn Bayesian thinking, build probabilistic models with PyMC, and apply hierarchical methods to problems in health, finance, and social science. The workshop bridges mathematical rigour with hands-on implementation.

## Prerequisites

- Probability and statistics basics (distributions, likelihood, conditional probability, Bayes' theorem)
- Python programming (NumPy, Matplotlib)
- Some familiarity with regression (linear/logistic) is helpful
- No prior Bayesian experience required

## Learning Objectives

By the end of this workshop, participants will be able to:

1. Think probabilistically and formulate problems in a Bayesian framework
2. Specify prior distributions and understand their impact on inference
3. Build and fit Bayesian models with PyMC
4. Understand and diagnose MCMC sampling (trace plots, R-hat, effective sample size)
5. Construct hierarchical (multilevel) models
6. Perform model comparison and posterior predictive checks
7. Apply Bayesian methods to domain-specific problems

## Software Requirements

- Python 3.10+
- Libraries: pymc (v5+), arviz, numpy, matplotlib, seaborn, pandas, scipy
- Optional: Stan (via cmdstanpy), bambi (formula-based Bayesian models)

---

## Day-by-Day Program

### Day 1: Bayesian Thinking & First Models

**Objectives:** Understand the Bayesian paradigm and build first probabilistic models.

| Time | Topic |
|------|-------|
| 09:00–10:00 | **Why Bayesian?** — Frequentist vs. Bayesian philosophy, probability as belief, advantages of the Bayesian approach: uncertainty quantification, small data, prior knowledge incorporation |
| 10:00–10:45 | **Bayes' Theorem in Practice** — Prior × Likelihood = Posterior (up to normalization). Conjugate priors, analytical examples: Beta-Binomial, Normal-Normal |
| 10:45–11:00 | *Break* |
| 11:00–12:30 | **Choosing Priors** — Informative vs. weakly informative vs. non-informative priors. Prior predictive checks: does the prior generate plausible data? Common priors for standard parameters |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **Introduction to PyMC** — Model specification, random variables, observed data, sampling with NUTS, trace plots, ArviZ for diagnostics and visualization |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Bayesian Linear Regression** — Normal likelihood, priors on coefficients and variance, posterior interpretation, credible intervals vs. confidence intervals, posterior predictive distribution |

**Lab 1:** Build a Bayesian linear regression model in PyMC: predict a health outcome (e.g., blood pressure ~ age + BMI). Explore the effect of different priors, visualize the posterior, and compare with frequentist OLS.

**Homework:** Fit a Bayesian regression on a dataset of your choice. Experiment with prior sensitivity.

---

### Day 2: MCMC, Diagnostics & Generalized Models

**Objectives:** Understand how MCMC works and extend Bayesian models beyond linear regression.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **How MCMC Works** — The sampling problem, Metropolis-Hastings (intuition), Hamiltonian Monte Carlo (HMC), NUTS (No U-Turn Sampler). Why NUTS is the default |
| 10:30–10:45 | *Break* |
| 10:45–12:00 | **Diagnosing MCMC** — Trace plots, autocorrelation, R-hat (convergence), effective sample size (ESS), divergences in HMC. What to do when sampling fails: reparameterization, non-centered parameterization |
| 12:00–12:30 | **Model Criticism** — Posterior predictive checks: does the model generate data that looks like the real data? Residual analysis, calibration |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **Bayesian Logistic Regression** — Bernoulli/Binomial likelihood, logit link, priors for coefficients, interpreting posterior odds ratios, classification with uncertainty |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Bayesian GLMs** — Poisson regression for count data, negative binomial for overdispersion, choosing the right likelihood family |

**Lab 2:** Build a Bayesian logistic regression for disease diagnosis (e.g., diabetes prediction). Perform full MCMC diagnostics, posterior predictive checks, and compare predicted probabilities with a frequentist logistic regression.

**Homework:** Fit a Poisson model to count data (e.g., number of doctor visits) and check for overdispersion.

---

### Day 3: Hierarchical Models

**Objectives:** Build multilevel models that share information across groups.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Why Hierarchical?** — The problem: too many groups, too little data per group. Complete pooling vs. no pooling vs. partial pooling. Shrinkage and the James-Stein phenomenon |
| 10:30–10:45 | *Break* |
| 10:45–12:30 | **Hierarchical Linear Models** — Varying intercepts, varying slopes, group-level predictors. The non-centered parameterization for efficient sampling. Visualizing partial pooling |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **Hierarchical Models for Real Data** — Multi-country health data: estimating country-level effects with partial pooling. Cross-classified and nested structures |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Model Comparison** — WAIC, LOO-CV (Leave-One-Out Cross-Validation) with ArviZ, comparing models with different structures, information criteria interpretation |

**Lab 3:** Build a hierarchical model for educational outcomes across African countries: student test scores nested within schools within countries. Compare complete pooling, no pooling, and hierarchical estimates. Visualize shrinkage.

**Homework:** Extend the hierarchical model with a group-level predictor (e.g., school funding level).

---

### Day 4: Advanced Topics & Applications

**Objectives:** Apply Bayesian methods to domain-specific problems and explore advanced techniques.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Bayesian Time Series** — Autoregressive priors, Gaussian processes for time series, structural time series models, changepoint detection |
| 10:30–10:45 | *Break* |
| 10:45–12:00 | **Mixture Models & Clustering** — Gaussian mixture models, Bayesian nonparametrics (Dirichlet Process intuition), latent variable models |
| 12:00–12:30 | **Bayesian A/B Testing** — Comparing treatments/interventions, posterior probability of superiority, decision-making under uncertainty, advantages over p-values |
| 12:30–14:00 | *Lunch* |
| 14:00–15:00 | **Domain Applications** — Case studies: clinical trial analysis, credit risk modelling, epidemiological modelling (SIR with Bayesian inference), survey data analysis |
| 15:00–15:15 | *Break* |
| 15:15–16:15 | **Capstone Project Work** — Complete a Bayesian analysis on a chosen dataset |
| 16:15–17:00 | **Presentations & Wrap-Up** — Project presentations, Bayesian workflow summary, resources, certificates |

**Lab 4 (Capstone):** Choose one project:
- **Health:** Bayesian disease prevalence estimation with hierarchical models across regions
- **Finance:** Credit default modelling with Bayesian logistic regression and uncertainty quantification
- **Education:** Multilevel model of student performance with school and country effects
- **Custom:** Apply Bayesian methods to a problem from your own domain

---

## Assessment

- **Daily labs** (40%) — Working models with proper diagnostics
- **Capstone project** (40%) — Complete Bayesian analysis with interpretation
- **Participation** (20%) — Engagement, homework, and discussions

## Resources

- [Bayesian Analysis with Python (3rd ed.) — Osvaldo Martin](https://www.packtpub.com/product/bayesian-analysis-with-python-third-edition/9781805127161)
- [Statistical Rethinking (2nd ed.) — Richard McElreath](https://xcelab.net/rm/statistical-rethinking/)
- [PyMC Documentation](https://www.pymc.io/projects/docs/en/stable/)
- [ArviZ Documentation](https://python.arviz.org/en/stable/)
- [Bayesian Data Analysis (Gelman et al.)](http://www.stat.columbia.edu/~gelman/book/)

## Certificate

Participants who complete all labs and the capstone project receive a certificate of completion.
