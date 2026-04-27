---
layout: page
title: "Data-Science Portfolio"
description: "13 end-to-end data-science projects on real public data, with 5 long-form bilingual case studies. Bilingual EN/FR."
img: assets/img/publication_preview/shape-of-data.svg
importance: 1
category: teaching & outreach
---

A bilingual portfolio of **13 end-to-end data-science projects** on real public data (Kaggle, NASA POWER, USAID PEPFAR), each with a business question, executable Jupyter notebook, methodology write-up, and validation metrics. Five projects have **long-form case studies** with results tables, model comparisons, and honest trade-off analysis.

**Live site:** [gabayae.github.io/data-portfolio](https://gabayae.github.io/data-portfolio/) · [Version française](https://gabayae.github.io/data-portfolio/fr/)

**Source code:** [github.com/gabayae/data-portfolio](https://github.com/gabayae/data-portfolio)

### Methodology coverage

- **Time-series forecasting:** SARIMA, UnobservedComponents (state-space + Kalman), gradient-boosted regressors with weather exogenous covariates
- **GLMs / actuarial pricing:** Poisson + Gamma, Tweedie compound-Poisson, monotonic-constrained boosting
- **Survival analysis:** Kaplan-Meier, Cox proportional hazards, Weibull AFT
- **Stochastic optimization / RL:** Markov decision processes, Q-learning, capped linear programming
- **Hierarchical reconciliation:** MinT-OLS across SKU × store × week
- **Experimental design:** ANOVA, Welch t-tests with Bonferroni correction, Bayesian A/B

### Featured case studies

- **Hourly load forecasting (PJM East):** GBM 6.2% MAPE, UC PI coverage 99% — the right model depends on whether procurement or risk is reading
- **Lake Kariba river flow:** GBM 7 cm RMSE on a 7 m operational band — turns "will we breach turbine safety in 30 days" from guess into calibrated probability
- **Solar irradiance (Nairobi, NASA POWER):** monthly climatology beats SARIMA at this latitude — the seasonal envelope is most of the predictability
- **freMTPL2 pricing:** Tweedie wins on Gini, Poisson + Gamma wins on top-decile lift — the choice is actuarial, not technical
- **Kenya mobile clinics:** Q-learning vs capped LP — the constraint formulation matters more than the algorithm
