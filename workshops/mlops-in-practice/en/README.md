# MLOps in Practice — 4-Day Workshop

**Instructor:** Dr. Yaé Ulrich Gaba
**Duration:** 4 days (24 hours)
**Level:** Intermediate to Advanced
**Language:** English

---

## Overview

This workshop bridges the gap between notebook experiments and production ML systems. Participants learn to package, deploy, monitor, and maintain machine learning models using industry-standard tools. The emphasis is on practical, reproducible workflows that work in resource-constrained environments — including cloud-free and low-infrastructure setups relevant to African contexts.

## Prerequisites

- Python programming (comfortable with functions, classes, packages)
- Machine learning basics (training, evaluation, scikit-learn or equivalent)
- Command line familiarity (terminal, basic shell commands)
- Laptop with Docker Desktop installed ([docker.com](https://www.docker.com/products/docker-desktop/))

## Learning Objectives

By the end of this workshop, participants will be able to:

1. Structure ML projects for reproducibility and collaboration
2. Track experiments systematically with MLflow
3. Version datasets and models with DVC
4. Containerize ML applications with Docker
5. Build CI/CD pipelines for automated testing and deployment
6. Monitor models in production and detect drift

## Software Requirements

- Python 3.10+, pip, virtualenv
- Docker Desktop
- Git
- Libraries: mlflow, dvc, fastapi, uvicorn, pytest, great-expectations
- Optional: GitHub account, cloud provider (free tiers work)

---

## Day-by-Day Program

### Day 1: Project Structure & Experiment Tracking

**Objectives:** Organize ML projects for reproducibility and track experiments systematically.

| Time | Topic |
|------|-------|
| 09:00–10:00 | **The MLOps Problem** — Why notebooks break in production, the ML lifecycle, technical debt in ML systems, MLOps maturity levels |
| 10:00–10:45 | **Project Structure** — Cookiecutter Data Science template, separating config/data/code/models, environment management (virtualenv, conda), requirements files, Makefile patterns |
| 10:45–11:00 | *Break* |
| 11:00–12:30 | **Experiment Tracking with MLflow** — Installing MLflow, logging parameters/metrics/artifacts, comparing runs, the MLflow UI, organizing experiments |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **Data & Model Versioning with DVC** — Git for data, DVC init, adding data files, remote storage (local, S3, GCS), pipelines with dvc.yaml, reproducing experiments |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Configuration Management** — Hydra / OmegaConf for managing hyperparameters, config files vs. command-line overrides, reproducible configurations |

**Lab 1:** Take a messy Jupyter notebook (provided) and refactor it into a clean project: proper directory structure, config files, MLflow tracking, DVC pipeline. Run 5 experiments with different hyperparameters and compare them in the MLflow UI.

**Homework:** Apply the same structure to one of your own ML projects.

---

### Day 2: Containerization & APIs

**Objectives:** Package models as Docker containers and serve them via REST APIs.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Docker Fundamentals** — Images vs. containers, Dockerfile anatomy, building images, running containers, port mapping, volumes, .dockerignore |
| 10:30–10:45 | *Break* |
| 10:45–12:30 | **Dockerizing ML Applications** — Python base images, installing dependencies, copying model artifacts, multi-stage builds for smaller images, GPU support basics |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **Serving Models with FastAPI** — Building a prediction API: endpoints, request/response models (Pydantic), loading model at startup, batch prediction, async endpoints, automatic docs (Swagger) |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Docker Compose** — Multi-container applications: API + database + MLflow server. docker-compose.yml, networking, environment variables, health checks |

**Lab 2:** Build a complete model-serving stack: train a model, save it with MLflow, wrap it in a FastAPI application, containerize with Docker, and orchestrate with Docker Compose (API + MLflow UI). Test the endpoint with curl and Python requests.

**Homework:** Add input validation and error handling to your API.

---

### Day 3: Testing & CI/CD

**Objectives:** Test ML code and automate pipelines with continuous integration.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Testing ML Systems** — Unit tests (pytest), testing data processing functions, testing model predictions, fixtures, parametrize, mocking external services |
| 10:30–10:45 | *Break* |
| 10:45–12:00 | **Data Validation** — Great Expectations: defining expectations, validating datasets, data contracts, catching data quality issues before they reach the model |
| 12:00–12:30 | **Model Validation** — Performance thresholds, regression tests, comparing against baseline, smoke tests for serving endpoints |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **CI/CD with GitHub Actions** — Workflow files, triggers, jobs and steps, running tests on push, building Docker images, environment secrets, artifact caching |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Automated ML Pipelines** — End-to-end: push code → run tests → validate data → train model → evaluate → build container → deploy. Branch-based workflows (dev/staging/prod) |

**Lab 3:** Set up a complete CI/CD pipeline for the model from Day 2: write unit tests, add data validation, create a GitHub Actions workflow that runs tests, trains the model, and builds a Docker image on every push.

**Homework:** Add a model performance gate — the pipeline should fail if accuracy drops below a threshold.

---

### Day 4: Monitoring, Drift Detection & Production

**Objectives:** Monitor deployed models and handle real-world production challenges.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Model Monitoring** — What to monitor: prediction latency, error rates, input distributions, output distributions. Logging and alerting strategies. Prometheus + Grafana basics |
| 10:30–10:45 | *Break* |
| 10:45–12:00 | **Data & Model Drift** — Concept drift, data drift, feature drift. Detection methods: PSI, KS test, Evidently AI. When to retrain, automated retraining triggers |
| 12:00–12:30 | **A/B Testing & Shadow Deployment** — Canary releases, shadow mode, feature flags for ML, comparing model versions in production |
| 12:30–14:00 | *Lunch* |
| 14:00–15:00 | **Production Patterns** — Model registries (MLflow), blue-green deployment, rollback strategies, batch vs. real-time inference, scaling considerations |
| 15:00–15:15 | *Break* |
| 15:15–16:15 | **MLOps in Low-Resource Environments** — Strategies for limited infrastructure: lightweight serving (Flask + systemd), cron-based retraining, local MLflow servers, DVC with local remotes, edge deployment |
| 16:15–17:00 | **Capstone Presentations & Wrap-Up** — Present end-to-end MLOps pipelines, discussion, Q&A, certificates |

**Lab 4 (Capstone):** Add monitoring to the deployed model: implement drift detection using Evidently AI, set up basic alerting, and create a dashboard showing model health metrics. Present the complete pipeline: code → test → build → deploy → monitor.

---

## Assessment

- **Daily labs** (50%) — Working pipelines and infrastructure
- **Capstone pipeline** (30%) — Complete MLOps system demonstrated on Day 4
- **Participation** (20%) — Engagement and homework

## Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [DVC Documentation](https://dvc.org/doc)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Evidently AI](https://www.evidentlyai.com/)
- [Made With ML — MLOps Course](https://madewithml.com/)

## Certificate

Participants who complete all labs and the capstone pipeline receive a certificate of completion.
