---
layout: workshop
permalink: /workshops/bayesian-statistics/en/
lang: en
title: "Applied Bayesian Statistics"
tagline: "Probabilistic thinking, PyMC, MCMC diagnostics, and hierarchical modelling — from priors to posterior decisions."
description: "4-day workshop on applied Bayesian statistics: PyMC, MCMC, hierarchical models."

# --- Sidebar metadata ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "4 days (≈ 24 hours)"
level: "Intermediate to Advanced"
format: "On-site, live online, or hybrid"
languages: "English &amp; French"
certificate: "Certificate of completion"

# --- Materials links shown in the sidebar ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/bayesian-statistics

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Workshop inquiry — Applied Bayesian Statistics"
---

## Program Overview

This workshop provides a practical introduction to Bayesian statistics with emphasis on modelling, computation, and real-world applications. Participants learn Bayesian thinking, build probabilistic models with PyMC, and apply hierarchical methods to problems in health, finance, and social science. The workshop bridges mathematical rigour with hands-on implementation.

### Software requirements

- Python 3.10+
- Libraries: pymc (v5+), arviz, numpy, matplotlib, seaborn, pandas, scipy
- Optional: Stan (via cmdstanpy), bambi (formula-based Bayesian models)

### Day 1 — Bayesian thinking & first models

**Objectives:** understand the Bayesian paradigm and build first probabilistic models.

- **Why Bayesian?** — Frequentist vs. Bayesian philosophy, probability as belief, advantages of the Bayesian approach: uncertainty quantification, small data, prior knowledge incorporation.
- **Bayes' theorem in practice** — Prior × Likelihood = Posterior (up to normalization). Conjugate priors, analytical examples: Beta-Binomial, Normal-Normal.
- **Choosing priors** — informative vs. weakly informative vs. non-informative priors. Prior predictive checks: does the prior generate plausible data? Common priors for standard parameters.
- **Introduction to PyMC** — model specification, random variables, observed data, sampling with NUTS, trace plots, ArviZ for diagnostics and visualization.
- **Bayesian linear regression** — normal likelihood, priors on coefficients and variance, posterior interpretation, credible intervals vs. confidence intervals, posterior predictive distribution.

**Lab 1:** build a Bayesian linear regression model in PyMC: predict a health outcome (e.g., blood pressure ~ age + BMI). Explore the effect of different priors, visualize the posterior, and compare with frequentist OLS.

### Day 2 — MCMC, diagnostics & generalized models

**Objectives:** understand how MCMC works and extend Bayesian models beyond linear regression.

- **How MCMC works** — the sampling problem, Metropolis-Hastings (intuition), Hamiltonian Monte Carlo (HMC), NUTS (No U-Turn Sampler). Why NUTS is the default.
- **Diagnosing MCMC** — trace plots, autocorrelation, R-hat (convergence), effective sample size (ESS), divergences in HMC. What to do when sampling fails: reparameterization, non-centered parameterization.
- **Model criticism** — posterior predictive checks: does the model generate data that looks like the real data? Residual analysis, calibration.
- **Bayesian logistic regression** — Bernoulli/Binomial likelihood, logit link, priors for coefficients, interpreting posterior odds ratios, classification with uncertainty.
- **Bayesian GLMs** — Poisson regression for count data, negative binomial for overdispersion, choosing the right likelihood family.

**Lab 2:** build a Bayesian logistic regression for disease diagnosis (e.g., diabetes prediction). Perform full MCMC diagnostics, posterior predictive checks, and compare predicted probabilities with a frequentist logistic regression.

### Day 3 — Hierarchical models

**Objectives:** build multilevel models that share information across groups.

- **Why hierarchical?** — the problem: too many groups, too little data per group. Complete pooling vs. no pooling vs. partial pooling. Shrinkage and the James-Stein phenomenon.
- **Hierarchical linear models** — varying intercepts, varying slopes, group-level predictors. The non-centered parameterization for efficient sampling. Visualizing partial pooling.
- **Hierarchical models for real data** — multi-country health data: estimating country-level effects with partial pooling. Cross-classified and nested structures.
- **Model comparison** — WAIC, LOO-CV (Leave-One-Out Cross-Validation) with ArviZ, comparing models with different structures, information criteria interpretation.

**Lab 3:** build a hierarchical model for educational outcomes across African countries: student test scores nested within schools within countries. Compare complete pooling, no pooling, and hierarchical estimates. Visualize shrinkage.

### Day 4 — Advanced topics & applications

**Objectives:** apply Bayesian methods to domain-specific problems and explore advanced techniques.

- **Bayesian time series** — autoregressive priors, Gaussian processes for time series, structural time series models, changepoint detection.
- **Mixture models & clustering** — Gaussian mixture models, Bayesian nonparametrics (Dirichlet Process intuition), latent variable models.
- **Bayesian A/B testing** — comparing treatments/interventions, posterior probability of superiority, decision-making under uncertainty, advantages over p-values.
- **Domain applications** — case studies: clinical trial analysis, credit risk modelling, epidemiological modelling (SIR with Bayesian inference), survey data analysis.
- **Capstone project work** — complete a Bayesian analysis on a chosen dataset.
- **Presentations & wrap-up** — project presentations, Bayesian workflow summary, resources, certificates.

**Lab 4 (capstone):** choose one project:
- **Health:** Bayesian disease prevalence estimation with hierarchical models across regions.
- **Finance:** credit default modelling with Bayesian logistic regression and uncertainty quantification.
- **Education:** multilevel model of student performance with school and country effects.
- **Custom:** apply Bayesian methods to a problem from your own domain.

### Assessment

- **Daily labs** (40 %) — working models with proper diagnostics.
- **Capstone project** (40 %) — complete Bayesian analysis with interpretation.
- **Participation** (20 %) — engagement, homework, and discussions.

### Resources

- [Bayesian Analysis with Python (3rd ed.) — Osvaldo Martin](https://www.packtpub.com/product/bayesian-analysis-with-python-third-edition/9781805127161)
- [Statistical Rethinking (2nd ed.) — Richard McElreath](https://xcelab.net/rm/statistical-rethinking/)
- [PyMC Documentation](https://www.pymc.io/projects/docs/en/stable/)
- [ArviZ Documentation](https://python.arviz.org/en/stable/)
- [Bayesian Data Analysis (Gelman et al.)](http://www.stat.columbia.edu/~gelman/book/)

## Learning Outcomes

By the end of this workshop, participants will be able to:

1. Think probabilistically and formulate problems in a Bayesian framework.
2. Specify prior distributions and understand their impact on inference.
3. Build and fit Bayesian models with PyMC.
4. Understand and diagnose MCMC sampling (trace plots, R-hat, effective sample size).
5. Construct hierarchical (multilevel) models.
6. Perform model comparison and posterior predictive checks.
7. Apply Bayesian methods to domain-specific problems.

## Who Should Attend

Data scientists, statisticians, and quantitative researchers in health, finance, social science, or public policy who want to move beyond p-values and report uncertainty honestly. Graduate students whose research depends on inference from small or messy samples. Practitioners who already use regression and want a principled way to incorporate prior knowledge and propagate uncertainty into decisions.

**Prerequisites:**

- Probability and statistics basics (distributions, likelihood, conditional probability, Bayes' theorem).
- Python programming (NumPy, Matplotlib).
- Some familiarity with regression (linear/logistic) is helpful.
- No prior Bayesian experience required.

## Brochure

Lecture notes and lab notebooks are linked in the sidebar.

For a printable one-page brochure suitable for forwarding to a program committee, conference organizer, or corporate L&D team, write to <a href="mailto:gabayae2@gmail.com?subject=Brochure%20request%20%E2%80%94%20Applied%20Bayesian%20Statistics">gabayae2@gmail.com</a> with the audience size and intended delivery dates.
