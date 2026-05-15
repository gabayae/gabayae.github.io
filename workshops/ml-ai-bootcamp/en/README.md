---
layout: page
permalink: /workshops/ml-ai-bootcamp/en/
title: "Machine Learning & AI Bootcamp — Syllabus"
description: "AIRINA Labs cohort program. 10 weeks full-time / 20 weeks part-time. Ten modules from Python through MLOps, capstone, portfolio."
lang: en
---

**Program:** Machine Learning &amp; AI Bootcamp — *An experiential approach*
**Delivered by:** [AIRINA Labs](https://github.com/AI-Technipreneurs)
**Lead instructor:** Dr. Yaé Ulrich Gaba
**Format:** 100% online, synchronous, cohort-based
**Language:** English (FR cohort available on request)
**Cadence:** 10 weeks full-time or 20 weeks part-time
**Cohort size:** 12–24 participants per intake

---

## Program at a glance

| | |
|---|---|
| **Live sessions** | 60+ |
| **Capstone project** | 1 (team or individual) |
| **Industry speakers** | 8 |
| **Course hours** | 200 |
| **Self-study (FT)** | 20 hours / week |
| **Self-study (PT)** | 10 hours / week |
| **Office hours** | Weekly, with teaching assistants |
| **Final deliverable** | Deployed capstone + portfolio piece |
| **Certificate** | Yes, on completion of all modules + capstone |

The 200 course hours are split roughly 60% live (lectures, labs, code-along sessions, capstone reviews) and 40% structured asynchronous work (reading, lab notebooks, problem sets). The 60+ live sessions include lectures, hands-on labs, industry-speaker sessions, office hours, capstone milestone reviews, and the final showcase.

---

## Who this is for

- **Working professionals** moving into ML/AI roles from adjacent fields — software engineering, data analysis, quantitative finance, actuarial work, scientific computing.
- **Upper-undergraduate and masters students** in mathematics, computer science, statistics, engineering, or quantitative social science who want an intensive route rather than a semester-paced course.
- **Corporate cohorts** running an internal upskilling program — banks, telecoms, insurers, fintechs, public-sector data teams.

You will get more out of this if you arrive with comfortable Python syntax (functions, classes, comprehensions), familiarity with the command line, and undergraduate-level mathematics (linear algebra, calculus, probability). No prior machine-learning experience is required, but it helps.

## Prerequisites

- **Required.** Python proficiency at the level of *"can read and modify a 200-line script without getting lost"*. Comfortable with functions, classes, imports, dictionaries, list comprehensions. Familiar with `pip` and virtual environments.
- **Required.** Linear algebra (vectors, matrices, eigenvalues), calculus (derivatives, gradients, integrals), probability (random variables, expectation, conditional probability) at undergraduate level.
- **Strongly recommended.** Some exposure to NumPy / Pandas, even at the *"I've used it once or twice"* level.
- **Helpful but not required.** Prior ML exposure (a Coursera course, a Kaggle competition, a university intro course), familiarity with Git/GitHub, basic Linux command line.

If you are not sure whether you have the prerequisites, the application includes a short technical screen. Honest self-assessment up front is better than scrambling in week 1.

## Tooling

- **Python 3.11+** as the working language throughout
- **Jupyter** (notebook + Lab) for labs
- **NumPy, Pandas, scikit-learn, matplotlib, seaborn** as the analytics stack
- **PyTorch** (primary) and **TensorFlow/Keras** (secondary) for deep learning
- **HuggingFace** ecosystem (`transformers`, `datasets`, `peft`, `accelerate`) for NLP and LLMs
- **LangChain, ChromaDB, FAISS** for RAG
- **MLflow, DVC, Docker, FastAPI** for the MLOps module
- **Google Colab** (free tier with GPU) as fallback compute; participants without local GPU will use Colab Pro or Kaggle for the deep-learning weeks
- **Git / GitHub** for version control across the bootcamp; the final portfolio piece is published on the participant's GitHub

---

## The ten modules

Each module below maps to existing course materials in the [course catalogue](../../../courses/) when a corresponding course exists. The bootcamp condenses, sequences, and adds project work on top of the catalogue, rather than reinventing the content.

### Module 1 — Python for data work

**One sentence.** Take the Python you already half-know and make it precise enough to ship.

**Learning outcomes.** By the end of the module, participants will be able to:

1. Write idiomatic Python — list/dict/set comprehensions, generators, context managers, decorators
2. Use NumPy and Pandas fluently for vectorized data manipulation
3. Build a reproducible Python project (virtualenv, `pyproject.toml`, pre-commit, basic testing)
4. Read, modify, and write Jupyter notebooks without losing reproducibility

**Topics.** Data types and control flow · functions, scoping, closures · classes and protocols · NumPy arrays, broadcasting, indexing · Pandas Series and DataFrames, joins, group-by, reshape · matplotlib and seaborn for plotting · virtual environments and dependency management · Git basics for code and notebooks.

**Labs.** (1) Refactor a messy 300-line script into a clean module with tests. (2) Wrangle a real public dataset (Kenyan health facility data) end-to-end in Pandas. (3) Publish your project to GitHub with a README, lockfile, and reproducible install.

**Builds on / connects to.** Catalogue: [Programmation pour Scientifiques](../../../courses/programmation-scientifiques/) and [Introduction to Data Science](../../../courses/intro-data-science/).

---

### Module 2 — Introduction to machine learning

**One sentence.** What ML actually is, what it isn't, and the workflow that runs underneath every project.

**Learning outcomes.**

1. Frame a problem as supervised, unsupervised, or reinforcement learning, and recognize when none of these is the right framing
2. Build a clean train/validation/test pipeline that avoids leakage
3. Choose, fit, and evaluate a simple model on a real dataset
4. Read a learning curve and a confusion matrix without confusing yourself

**Topics.** The supervised learning loop · loss functions and risk · empirical risk minimization · bias-variance · cross-validation, train/val/test splits, leakage · evaluation metrics for classification and regression · the "no free lunch" perspective on model choice.

**Labs.** (1) Predict patient readmission on a real hospital dataset (logistic regression, evaluated with calibration not just accuracy). (2) Diagnose a bad evaluation: spot the leakage in a deliberately broken notebook.

**Builds on.** Catalogue: [Fondements de l'Apprentissage Automatique](../../../courses/apprentissage-automatique/) (intro chapters).

---

### Module 3 — Classical machine learning: classification, regression, clustering

**One sentence.** The pre-deep-learning toolkit — still the right answer for most tabular problems.

**Learning outcomes.**

1. Fit and tune linear and regularized regression (ridge, lasso, elastic net)
2. Build and interpret tree-based ensembles (random forests, gradient boosting)
3. Apply unsupervised methods (k-means, hierarchical, DBSCAN, GMMs, PCA, UMAP)
4. Diagnose feature-importance and partial-dependence honestly, without overclaiming causality

**Topics.** Linear and logistic regression · regularization (ridge, lasso, elastic net) · SVMs and the kernel trick · decision trees, random forests, gradient boosting (XGBoost, LightGBM) · clustering (k-means, hierarchical, DBSCAN, GMM) · dimensionality reduction (PCA, UMAP, t-SNE) · model interpretation (permutation importance, SHAP, partial dependence) · what these methods can and cannot tell you about causation.

**Labs.** (1) Credit-scoring on a Kaggle/African bank dataset — full pipeline from EDA to deployable scoring function, with fairness audit. (2) Customer segmentation by mobile-money transaction patterns. (3) SHAP-based interpretation of an XGBoost model, including the failure modes of SHAP itself.

**Builds on.** Catalogue: [Fondements de l'Apprentissage Automatique](../../../courses/apprentissage-automatique/) (main body).

---

### Module 4 — Recommender systems

**One sentence.** How Netflix-style systems actually work, and the honest evaluation problem they create.

**Learning outcomes.**

1. Implement collaborative filtering (user-based, item-based, matrix factorization)
2. Implement content-based filtering with embeddings
3. Build a hybrid recommender and evaluate it with offline metrics (precision@k, NDCG, MAP)
4. Understand why offline metrics often disagree with online A/B results

**Topics.** The recommendation problem · explicit vs implicit feedback · collaborative filtering · matrix factorization (SVD, ALS, NMF) · content-based filtering with embeddings · hybrid models · evaluation: precision@k, recall@k, NDCG, MAP, online vs offline metrics · cold-start, popularity bias, filter bubbles · the "you'll never know until you A/B test" problem.

**Labs.** (1) MovieLens collaborative filter (SVD then ALS). (2) Build a hybrid recommender on a publicly available e-commerce dataset. (3) Run the same recommender against three evaluation metrics and explain why they rank models differently.

**Builds on.** No direct catalogue equivalent — this module is new content built specifically for the bootcamp.

---

### Module 5 — Natural language processing

**One sentence.** From the linguistics-aware classical methods to the transformer-era pipeline.

**Learning outcomes.**

1. Build a working text classification pipeline (cleaning, tokenization, vectorization, training, evaluation)
2. Fine-tune a pretrained transformer on a domain-specific task
3. Apply NLP to a multilingual or low-resource setting (with attention to African languages)
4. Understand the limitations: hallucination, bias, evaluation difficulty

**Topics.** Text preprocessing and tokenization (BPE, WordPiece) · word embeddings (Word2Vec, GloVe, FastText) · sequence models (RNN, LSTM, GRU) · the Transformer architecture · BERT-family models and fine-tuning · NER, sentiment, classification, summarization · multilingual and low-resource NLP · evaluation: BLEU, ROUGE, exact match, human evaluation.

**Labs.** (1) Sentiment classification on customer reviews (logistic regression baseline → fine-tuned DistilBERT). (2) Named entity recognition on a multilingual dataset including at least one African language. (3) Document summarization with a fine-tuned T5/BART.

**Builds on.** Catalogue: [Traitement Automatique du Langage](../../../courses/tal-nlp/).

---

### Module 6 — Modern machine learning: ANN, CNN, RNN

**One sentence.** Deep learning end-to-end, with enough theory to know when *not* to use it.

**Learning outcomes.**

1. Train a feed-forward neural network from scratch, in NumPy and then in PyTorch
2. Build, train, and evaluate CNNs on image classification tasks
3. Build, train, and evaluate RNNs/LSTMs on sequence tasks
4. Diagnose training pathologies: vanishing gradients, overfitting, dead neurons, distribution shift

**Topics.** Feed-forward networks, backpropagation, optimization (SGD, Adam, AdamW) · regularization (dropout, batch norm, weight decay, early stopping) · CNNs (LeNet, AlexNet, ResNet, modern architectures) · RNNs, LSTMs, GRUs · attention as a primitive · representation learning · the bitter lessons of deep learning (compute scaling, what doesn't transfer).

**Labs.** (1) Build a 2-layer MLP from scratch in NumPy, then port to PyTorch. (2) Image classification on a public medical imaging dataset (e.g., chest X-ray, with discussion of dataset bias). (3) Sequence prediction on a financial time-series dataset with an LSTM.

**Builds on.** Catalogue: [Apprentissage Profond](../../../courses/apprentissage-profond/).

---

### Module 7 — LLMs and generative AI

**One sentence.** What's under the hood of GPT/Claude/LLaMA, what you can actually do with them, and where they fail.

**Learning outcomes.**

1. Understand the transformer architecture as it appears in modern LLMs
2. Apply prompt engineering and structured output techniques effectively
3. Fine-tune a small open-source LLM with LoRA/QLoRA on a domain dataset
4. Build a retrieval-augmented generation (RAG) system
5. Evaluate generation honestly: when an LLM is genuinely useful, and when it's confabulating

**Topics.** The transformer, attention mechanism, scaling laws · pretraining, fine-tuning, RLHF/DPO at survey level · prompt engineering, structured output, function calling · parameter-efficient fine-tuning (LoRA, QLoRA, PEFT) · RAG: chunking, embedding, retrieval, reranking, generation · diffusion models (intuition + practical use) · evaluation: BLEU, ROUGE, LLM-as-judge, human eval, why all of these are partial · agentic systems and tool use · safety, alignment, hallucination, bias.

**Labs.** (1) Build a RAG system over a domain-specific corpus (e.g., a set of WHO/AFRO health reports) using ChromaDB and a local or API LLM. (2) Fine-tune a 1-7B-parameter open model with LoRA on a domain task. (3) Build a multi-step agent with tool use (search, calculator, code execution) using LangChain or LangGraph.

**Builds on.** Catalogue: [IA Générative](../../../courses/ia-generative/).

---

### Module 8 — MLOps and deployment

**One sentence.** What it takes for the model to keep working after the notebook is closed.

**Learning outcomes.**

1. Version code, data, and models in a way that supports reproducibility
2. Containerize a model and deploy it as a REST API
3. Set up experiment tracking, model registry, and monitoring
4. Build a basic CI/CD pipeline for an ML system

**Topics.** Reproducibility (Git, DVC, MLflow) · experiment tracking and model registry (MLflow, Weights &amp; Biases) · containerization (Docker, docker-compose) · serving (FastAPI, BentoML, model registries) · monitoring (data drift, prediction drift, performance drift, latency, cost) · CI/CD for ML pipelines · the difference between "the model works on my laptop" and "the model works in production for six months."

**Labs.** (1) Wrap a trained model in a FastAPI service, containerize, deploy to a free-tier cloud (Render or Railway), call it from a notebook. (2) Set up MLflow tracking for a model retraining loop. (3) Simulate data drift on a deployed model and detect it from the monitoring dashboard.

**Builds on.** Catalogue: [MLOps](../../../courses/mlops/).

---

### Module 9 — Capstone project

**One sentence.** Take a real problem from idea to deployed system in two weeks.

This module runs in parallel with Modules 8 and 10, occupying the last two weeks of the program. Each participant (or small team of 2-3) ships a complete project: real dataset, real model, deployed endpoint, written report, public repository, live demo.

See [`CAPSTONE.md`](../CAPSTONE.md) for the full project specification, milestones, evaluation rubric, and example project tracks.

---

### Module 10 — Portfolio

**One sentence.** The capstone, the labs, and a clear public profile that says *"I can actually do this."*

**Learning outcomes.**

1. Curate three to five projects from the bootcamp into a coherent portfolio
2. Write a project README that an external reader can follow in five minutes
3. Publish the capstone as a hosted demo + technical writeup
4. Build a public profile (GitHub, LinkedIn, personal site if applicable) that points to the portfolio

**Topics.** Portfolio curation (less is more) · README discipline · technical writing for ML projects · publishing notebooks (nbviewer, Colab, GitHub Pages, Jupyter Book) · hosting model demos (Gradio, Streamlit, HuggingFace Spaces) · using your portfolio to ask better technical interview questions.

**Reference.** The lead instructor's own [data-science portfolio](https://gabayae.github.io/data-portfolio/) is one model. Module 10 doesn't prescribe a single template — it teaches the discipline of *making your work findable and legible to non-cohort readers*.

---

## Schedule (10-week full-time cohort)

| Week | Focus | Modules |
|------|-------|---------|
| 1 | Python toolkit for data work | M1 |
| 2 | Introduction to ML + start of classical ML | M2 + M3 (part 1) |
| 3 | Classical ML in depth, credit-scoring lab | M3 |
| 4 | Recommender systems | M4 |
| 5 | Natural language processing | M5 |
| 6 | Deep learning (ANN, CNN, RNN) | M6 |
| 7 | LLMs and generative AI | M7 |
| 8 | MLOps and deployment | M8 |
| 9 | Capstone work-week + portfolio sessions | M9 + M10 |
| 10 | Capstone wrap-up, final presentations, portfolio launch | M9 + M10 |

Part-time cohorts run the same content over 20 weeks at half the weekly intensity. Industry-speaker sessions are distributed across weeks 2-9 (roughly one per week, sometimes paired).

A typical full-time week:

- **Mon-Thu mornings (3 hrs each).** Live instruction, code-along, lab work
- **Mon-Thu afternoons (2 hrs each).** Independent lab work, with teaching-assistant office hours
- **Friday.** Industry speaker (1 hr) + lab review (1 hr) + cohort retrospective (1 hr)
- **Self-study (20 hrs over the week).** Reading, pre-work for next week, lab completion

## Pedagogy

The "experiential approach" is not marketing — it's a deliberate choice with two concrete consequences:

1. **Every module has a real dataset and a deployable artifact.** Not a tutorial dataset chosen for pedagogical neatness, but data that participants will plausibly encounter in their own work: African banking records, health facility data, telecom CDRs, satellite imagery, multilingual text. The artifact at the end of the module is something a participant could put on GitHub.

2. **Mistakes are part of the curriculum.** Several labs are deliberately seeded with leakage, bad evaluation choices, or training pathologies. The exercise is to find them. The point is that *spotting a broken ML pipeline is more valuable than building a working one in a vacuum*.

The "case-based" framing in the syllabus translates to: each week opens with a real-world case (a deployed system, a published failure, an audit report), and the technical content is motivated by what the case needed.

## Assessment and certificate

- **Weekly lab deliverables** (40%) — each module's labs are graded on correctness, code quality, and a short written interpretation
- **Capstone project** (40%) — deployed system + technical writeup + live demo
- **Participation** (20%) — engagement in live sessions, peer code review, capstone milestone presentations

Participants who complete all module deliverables and pass the capstone (rubric in `CAPSTONE.md`) receive a **Certificate of Completion** signed by the lead instructor and AIRINA Labs.

The certificate is a record of completion, not an accredited degree. It's most useful as a portfolio anchor in conversations with employers, not as a credential in its own right.

## Industry-speaker series

The 8 industry speakers across the cohort are drawn from the AIRINA Labs and AIMS networks: ML/AI practitioners at African banks, telecoms, fintechs, and the regional offices of global tech firms; one or two senior researchers at international labs. Each speaker session is one hour: 30 minutes of *"what we actually build and why"*, 30 minutes of cohort Q&amp;A. Names and affiliations are confirmed per cohort and shared once registration closes.

Speakers do not pitch products and do not recruit. They show up to tell the cohort what the work looks like outside the bootcamp.

## Post-program

For three months after the cohort ends, participants retain access to:

- The cohort Slack workspace (peer network + alumni channel)
- One 30-minute 1-on-1 with the lead instructor for career or technical follow-up
- The hosted version of their capstone (instructor will keep the deployment up for at least 3 months on a free-tier cloud)

This isn't a job-placement service. The goal is to leave participants with a working portfolio, a peer network, and the technical foundation to take their own next step.

## Resources

Recommended reading and reference, organized by module:

- **Module 1-3 (Python, ML foundations).** Aurélien Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed., O'Reilly).
- **Module 3 (Classical ML).** Trevor Hastie, Robert Tibshirani, Jerome Friedman, *The Elements of Statistical Learning* (Springer, 2nd ed.). Free PDF on Hastie's site.
- **Module 4 (Recommender systems).** Charu Aggarwal, *Recommender Systems: The Textbook* (Springer, 2016).
- **Module 5 (NLP).** Dan Jurafsky and James Martin, *Speech and Language Processing* (3rd ed. draft). Free on the authors' site.
- **Module 6 (Deep learning).** Ian Goodfellow, Yoshua Bengio, Aaron Courville, *Deep Learning* (MIT Press, 2016). Free online.
- **Module 7 (LLMs / GenAI).** Sebastian Raschka, *Build a Large Language Model From Scratch* (Manning, 2024). The HuggingFace NLP course (free, online).
- **Module 8 (MLOps).** Chip Huyen, *Designing Machine Learning Systems* (O'Reilly, 2022). Eugene Yan's MLOps blog.
- **Topology / geometry-aware ML companion (optional).** Colleen M. Farrelly and Yaé Ulrich Gaba, [*The Shape of Data*](https://nostarch.com/shapeofdata) (No Starch Press) — for cohort members who want to bring topological and geometric tools to bear on the same problems.

---

## Apply

Cohorts are run several times per year. To express interest in a future cohort, or to discuss a private corporate cohort for your organization:

📧 [gabayae2@gmail.com](mailto:gabayae2@gmail.com?subject=ML%20%26%20AI%20Bootcamp%20%E2%80%94%20cohort%20inquiry)

Please include in your inquiry: your background, your goal for the bootcamp, and whether you're asking about an open cohort (individual) or a private corporate cohort (team). For corporate cohorts, also include the team size and the time window you're targeting.
