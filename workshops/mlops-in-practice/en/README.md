---
layout: workshop
permalink: /workshops/mlops-in-practice/en/
lang: en
title: "MLOps in Practice"
tagline: "From notebook to production: package, deploy, monitor, and maintain ML systems with industry-standard tooling."
description: "4-day workshop: Docker, CI/CD, monitoring, MLflow, DVC — from notebook to production."

# --- Sidebar metadata ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "4 days (≈ 24 hours)"
level: "Intermediate to Advanced"
format: "On-site, live online, or hybrid"
languages: "English &amp; French"
certificate: "Certificate of completion"

# --- Materials links shown in the sidebar ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/mlops-in-practice

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Workshop inquiry — MLOps in Practice"
---

## Program Overview

This workshop bridges the gap between notebook experiments and production ML systems. Participants learn to package, deploy, monitor, and maintain machine learning models using industry-standard tools. The emphasis is on practical, reproducible workflows that work in resource-constrained environments — including cloud-free and low-infrastructure setups relevant to African contexts.

### Software Requirements

- Python 3.10+, pip, virtualenv
- Docker Desktop
- Git
- Libraries: mlflow, dvc, fastapi, uvicorn, pytest, great-expectations
- Optional: GitHub account, cloud provider (free tiers work)

### Day 1: Project Structure & Experiment Tracking

**Objectives:** Organize ML projects for reproducibility and track experiments systematically.

- **The MLOps Problem** — Why notebooks break in production, the ML lifecycle, technical debt in ML systems, MLOps maturity levels
- **Project Structure** — Cookiecutter Data Science template, separating config/data/code/models, environment management (virtualenv, conda), requirements files, Makefile patterns
- **Experiment Tracking with MLflow** — Installing MLflow, logging parameters/metrics/artifacts, comparing runs, the MLflow UI, organizing experiments
- **Data & Model Versioning with DVC** — Git for data, DVC init, adding data files, remote storage (local, S3, GCS), pipelines with dvc.yaml, reproducing experiments
- **Configuration Management** — Hydra / OmegaConf for managing hyperparameters, config files vs. command-line overrides, reproducible configurations

**Lab 1:** Take a messy Jupyter notebook (provided) and refactor it into a clean project: proper directory structure, config files, MLflow tracking, DVC pipeline. Run 5 experiments with different hyperparameters and compare them in the MLflow UI.

**Homework:** Apply the same structure to one of your own ML projects.

### Day 2: Containerization & APIs

**Objectives:** Package models as Docker containers and serve them via REST APIs.

- **Docker Fundamentals** — Images vs. containers, Dockerfile anatomy, building images, running containers, port mapping, volumes, .dockerignore
- **Dockerizing ML Applications** — Python base images, installing dependencies, copying model artifacts, multi-stage builds for smaller images, GPU support basics
- **Serving Models with FastAPI** — Building a prediction API: endpoints, request/response models (Pydantic), loading model at startup, batch prediction, async endpoints, automatic docs (Swagger)
- **Docker Compose** — Multi-container applications: API + database + MLflow server. docker-compose.yml, networking, environment variables, health checks

**Lab 2:** Build a complete model-serving stack: train a model, save it with MLflow, wrap it in a FastAPI application, containerize with Docker, and orchestrate with Docker Compose (API + MLflow UI). Test the endpoint with curl and Python requests.

**Homework:** Add input validation and error handling to your API.

### Day 3: Testing & CI/CD

**Objectives:** Test ML code and automate pipelines with continuous integration.

- **Testing ML Systems** — Unit tests (pytest), testing data processing functions, testing model predictions, fixtures, parametrize, mocking external services
- **Data Validation** — Great Expectations: defining expectations, validating datasets, data contracts, catching data quality issues before they reach the model
- **Model Validation** — Performance thresholds, regression tests, comparing against baseline, smoke tests for serving endpoints
- **CI/CD with GitHub Actions** — Workflow files, triggers, jobs and steps, running tests on push, building Docker images, environment secrets, artifact caching
- **Automated ML Pipelines** — End-to-end: push code → run tests → validate data → train model → evaluate → build container → deploy. Branch-based workflows (dev/staging/prod)

**Lab 3:** Set up a complete CI/CD pipeline for the model from Day 2: write unit tests, add data validation, create a GitHub Actions workflow that runs tests, trains the model, and builds a Docker image on every push.

**Homework:** Add a model performance gate — the pipeline should fail if accuracy drops below a threshold.

### Day 4: Monitoring, Drift Detection & Production

**Objectives:** Monitor deployed models and handle real-world production challenges.

- **Model Monitoring** — What to monitor: prediction latency, error rates, input distributions, output distributions. Logging and alerting strategies. Prometheus + Grafana basics
- **Data & Model Drift** — Concept drift, data drift, feature drift. Detection methods: PSI, KS test, Evidently AI. When to retrain, automated retraining triggers
- **A/B Testing & Shadow Deployment** — Canary releases, shadow mode, feature flags for ML, comparing model versions in production
- **Production Patterns** — Model registries (MLflow), blue-green deployment, rollback strategies, batch vs. real-time inference, scaling considerations
- **MLOps in Low-Resource Environments** — Strategies for limited infrastructure: lightweight serving (Flask + systemd), cron-based retraining, local MLflow servers, DVC with local remotes, edge deployment
- **Capstone Presentations & Wrap-Up** — Present end-to-end MLOps pipelines, discussion, Q&A, certificates

**Lab 4 (Capstone):** Add monitoring to the deployed model: implement drift detection using Evidently AI, set up basic alerting, and create a dashboard showing model health metrics. Present the complete pipeline: code → test → build → deploy → monitor.

### Assessment

- **Daily labs** (50%) — Working pipelines and infrastructure
- **Capstone pipeline** (30%) — Complete MLOps system demonstrated on Day 4
- **Participation** (20%) — Engagement and homework

### Resources

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [DVC Documentation](https://dvc.org/doc)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Evidently AI](https://www.evidentlyai.com/)
- [Made With ML — MLOps Course](https://madewithml.com/)

## Learning Outcomes

By the end of this workshop, participants will be able to:

1. Structure ML projects for reproducibility and collaboration
2. Track experiments systematically with MLflow
3. Version datasets and models with DVC
4. Containerize ML applications with Docker
5. Build CI/CD pipelines for automated testing and deployment
6. Monitor models in production and detect drift

## Who Should Attend

Data scientists and ML practitioners who have trained models in notebooks but never shipped one. Software engineers moving into ML infrastructure. Research engineers responsible for reproducibility and deployment. DevOps engineers who need to support ML workloads.

**Prerequisites:**

- Python programming (comfortable with functions, classes, packages)
- Machine learning basics (training, evaluation, scikit-learn or equivalent)
- Command line familiarity (terminal, basic shell commands)
- Laptop with Docker Desktop installed ([docker.com](https://www.docker.com/products/docker-desktop/))

## Brochure

Lecture notes and lab notebooks are linked in the sidebar.

For a printable one-page brochure suitable for forwarding to a program committee, conference organizer, or corporate L&D team, write to <a href="mailto:gabayae2@gmail.com?subject=Brochure%20request%20%E2%80%94%20MLOps%20in%20Practice">gabayae2@gmail.com</a> with the audience size and intended delivery dates.
