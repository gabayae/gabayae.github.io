---
layout: workshop
permalink: /workshops/ml-ai-bootcamp/en/
lang: en
title: "Machine Learning & AI Bootcamp"
tagline: "A 10-week experiential cohort program — ten modules from Python through MLOps, deployed capstone, public portfolio."
description: "AIRINA Labs cohort program. 10 weeks full-time / 20 weeks part-time. Ten modules from Python through MLOps, capstone, portfolio."

# --- Sidebar metadata ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "10 weeks full-time / 20 weeks part-time (≈ 200 course hours)"
level: "Intermediate to Advanced"
format: "On-site, live online, or hybrid"
languages: "English &amp; French"
certificate: "Certificate of completion"

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Workshop inquiry — Machine Learning & AI Bootcamp"
---

## Program Overview

**Operational pages.** [Weekly schedule]({{ '/workshops/ml-ai-bootcamp/en/schedule/' | relative_url }}) | [Capstone brief]({{ '/workshops/ml-ai-bootcamp/CAPSTONE/' | relative_url }})

In January 2023, BioNTech acquired InstaDeep — a machine-learning company founded in Tunis with offices in Lagos, Nairobi, and Paris — for $562 million. The deal made public what recruiters across the continent had been observing for years: global demand for production-ready ML engineers far exceeds trained supply, and the gap is wider in Africa than anywhere else. Most African undergraduate computer-science curricula end before deep learning; the MOOCs that fill the void are calibrated to North-American prerequisites and usually presume a prior software-engineering job. This bootcamp targets that gap directly. It takes quantitatively trained graduates — mathematics, statistics, computer science, quantitative finance, scientific engineering — and brings them in ten weeks to the production-ready level that African and international ML teams now hire for.

### Program at a glance

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

The 200 course hours are split roughly 60 % live (lectures, labs, code-along sessions, capstone reviews) and 40 % structured asynchronous work (reading, lab notebooks, problem sets). The 60+ live sessions include lectures, hands-on labs, industry-speaker sessions, office hours, capstone milestone reviews, and the final showcase.

### Tooling

- **Python 3.11+** as the working language throughout.
- **Jupyter** (notebook + Lab) for labs.
- **NumPy, Pandas, scikit-learn, matplotlib, seaborn** as the analytics stack.
- **PyTorch** (primary) and **TensorFlow/Keras** (secondary) for deep learning.
- **HuggingFace** ecosystem (`transformers`, `datasets`, `peft`, `accelerate`) for NLP and LLMs.
- **LangChain, ChromaDB, FAISS** for RAG.
- **MLflow, DVC, Docker, FastAPI** for the MLOps module.
- **Google Colab** (free tier with GPU) as fallback compute; participants without local GPU will use Colab Pro or Kaggle for the deep-learning weeks.
- **Git / GitHub** for version control across the bootcamp; the final portfolio piece is published on the participant's GitHub.

### The ten modules

Each module below maps to existing course materials in the [course catalogue]({{ '/courses/' | relative_url }}) when a corresponding course exists. The bootcamp condenses, sequences, and adds project work on top of the catalogue, rather than reinventing the content.

#### Module 1 — Python for data work

*One sentence.* Take the Python you already half-know and make it precise enough to ship.

**Topics.** Data types and control flow · functions, scoping, closures · classes and protocols · NumPy arrays, broadcasting, indexing · Pandas Series and DataFrames, joins, group-by, reshape · matplotlib and seaborn for plotting · virtual environments and dependency management · Git basics for code and notebooks.

**Labs.** (1) Refactor a messy 300-line script into a clean module with tests. (2) Wrangle a real public dataset (Kenyan health facility data) end-to-end in Pandas. (3) Publish your project to GitHub with a README, lockfile, and reproducible install.

#### Module 2 — Introduction to machine learning

*One sentence.* What ML actually is, what it isn't, and the workflow that runs underneath every project.

**Topics.** The supervised learning loop · loss functions and risk · empirical risk minimization · bias-variance · cross-validation, train/val/test splits, leakage · evaluation metrics for classification and regression · the "no free lunch" perspective on model choice.

**Labs.** (1) Predict patient readmission on a real hospital dataset (logistic regression, evaluated with calibration not just accuracy). (2) Diagnose a bad evaluation: spot the leakage in a deliberately broken notebook.

#### Module 3 — Classical machine learning

*One sentence.* The pre-deep-learning toolkit — still the right answer for most tabular problems.

**Topics.** Linear and logistic regression · regularization (ridge, lasso, elastic net) · SVMs and the kernel trick · decision trees, random forests, gradient boosting (XGBoost, LightGBM) · clustering (k-means, hierarchical, DBSCAN, GMM) · dimensionality reduction (PCA, UMAP, t-SNE) · model interpretation (permutation importance, SHAP, partial dependence) · what these methods can and cannot tell you about causation.

**Labs.** (1) Credit-scoring on a Kaggle / African bank dataset — full pipeline with fairness audit. (2) Customer segmentation by mobile-money transaction patterns. (3) SHAP-based interpretation of an XGBoost model, including the failure modes of SHAP itself.

#### Module 4 — Recommender systems

*One sentence.* How Netflix-style systems actually work, and the honest evaluation problem they create.

**Topics.** The recommendation problem · explicit vs implicit feedback · collaborative filtering · matrix factorization (SVD, ALS, NMF) · content-based filtering with embeddings · hybrid models · evaluation: precision@k, recall@k, NDCG, MAP, online vs offline metrics · cold-start, popularity bias, filter bubbles.

**Labs.** (1) MovieLens collaborative filter (SVD then ALS). (2) Build a hybrid recommender on a publicly available e-commerce dataset. (3) Run the same recommender against three evaluation metrics and explain why they rank models differently.

#### Module 5 — Natural language processing

*One sentence.* From the linguistics-aware classical methods to the transformer-era pipeline.

**Topics.** Text preprocessing and tokenization (BPE, WordPiece) · word embeddings (Word2Vec, GloVe, FastText) · sequence models (RNN, LSTM, GRU) · the Transformer architecture · BERT-family models and fine-tuning · NER, sentiment, classification, summarization · multilingual and low-resource NLP · evaluation: BLEU, ROUGE, exact match, human evaluation.

**Labs.** (1) Sentiment classification on customer reviews (logistic regression baseline → fine-tuned DistilBERT). (2) Named entity recognition on a multilingual dataset including at least one African language. (3) Document summarization with a fine-tuned T5/BART.

#### Module 6 — Modern machine learning: ANN, CNN, RNN

*One sentence.* Deep learning end-to-end, with enough theory to know when *not* to use it.

**Topics.** Feed-forward networks, backpropagation, optimization (SGD, Adam, AdamW) · regularization (dropout, batch norm, weight decay, early stopping) · CNNs (LeNet, AlexNet, ResNet, modern architectures) · RNNs, LSTMs, GRUs · attention as a primitive · representation learning · the bitter lessons of deep learning.

**Labs.** (1) Build a 2-layer MLP from scratch in NumPy, then port to PyTorch. (2) Image classification on a public medical imaging dataset. (3) Sequence prediction on a financial time-series dataset with an LSTM.

#### Module 7 — LLMs and generative AI

*One sentence.* What's under the hood of GPT/Claude/LLaMA, what you can actually do with them, and where they fail.

**Topics.** The transformer, attention mechanism, scaling laws · pretraining, fine-tuning, RLHF/DPO at survey level · prompt engineering, structured output, function calling · parameter-efficient fine-tuning (LoRA, QLoRA, PEFT) · RAG: chunking, embedding, retrieval, reranking, generation · diffusion models · evaluation: BLEU, ROUGE, LLM-as-judge, human eval · agentic systems and tool use · safety, alignment, hallucination, bias.

**Labs.** (1) Build a RAG system over a domain-specific corpus (e.g., WHO/AFRO health reports) using ChromaDB and a local or API LLM. (2) Fine-tune a 1-7B-parameter open model with LoRA on a domain task. (3) Build a multi-step agent with tool use (search, calculator, code execution) using LangChain or LangGraph.

#### Module 8 — MLOps and deployment

*One sentence.* What it takes for the model to keep working after the notebook is closed.

**Topics.** Reproducibility (Git, DVC, MLflow) · experiment tracking and model registry (MLflow, Weights & Biases) · containerization (Docker, docker-compose) · serving (FastAPI, BentoML, model registries) · monitoring (data drift, prediction drift, performance drift, latency, cost) · CI/CD for ML pipelines.

**Labs.** (1) Wrap a trained model in a FastAPI service, containerize, deploy to a free-tier cloud, call it from a notebook. (2) Set up MLflow tracking for a model retraining loop. (3) Simulate data drift on a deployed model and detect it from the monitoring dashboard.

#### Module 9 — Capstone project

*One sentence.* Take a real problem from idea to deployed system in two weeks.

This module runs in parallel with Modules 8 and 10, occupying the last two weeks of the program. Each participant (or small team of 2-3) ships a complete project: real dataset, real model, deployed endpoint, written report, public repository, live demo.

See [`CAPSTONE.md`]({{ '/workshops/ml-ai-bootcamp/CAPSTONE/' | relative_url }}) for the full project specification, milestones, evaluation rubric, and example project tracks.

#### Module 10 — Portfolio

*One sentence.* The capstone, the labs, and a clear public profile that says *"I can actually do this."*

**Topics.** Portfolio curation (less is more) · README discipline · technical writing for ML projects · publishing notebooks (nbviewer, Colab, GitHub Pages, Jupyter Book) · hosting model demos (Gradio, Streamlit, HuggingFace Spaces) · using your portfolio to ask better technical interview questions.

### Schedule (10-week full-time cohort)

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

Part-time cohorts run the same content over 20 weeks at half the weekly intensity. Industry-speaker sessions are distributed across weeks 2-9.

### Pedagogy

The "experiential approach" is not marketing — it's a deliberate choice with two concrete consequences:

1. **Every module has a real dataset and a deployable artifact.** Not a tutorial dataset chosen for pedagogical neatness, but data that participants will plausibly encounter in their own work: African banking records, health facility data, telecom CDRs, satellite imagery, multilingual text. The artifact at the end of the module is something a participant could put on GitHub.

2. **Mistakes are part of the curriculum.** Several labs are deliberately seeded with leakage, bad evaluation choices, or training pathologies. The exercise is to find them. The point is that *spotting a broken ML pipeline is more valuable than building a working one in a vacuum*.

### Assessment and certificate

- **Weekly lab deliverables** (40 %) — each module's labs are graded on correctness, code quality, and a short written interpretation.
- **Capstone project** (40 %) — deployed system + technical writeup + live demo.
- **Participation** (20 %) — engagement in live sessions, peer code review, capstone milestone presentations.

Participants who complete all module deliverables and pass the capstone (rubric in `CAPSTONE.md`) receive a **Certificate of Completion** signed by the lead instructor and AIRINA Labs. The certificate is a record of completion, not an accredited degree.

### Industry-speaker series

The 8 industry speakers across the cohort are drawn from the AIRINA Labs and AIMS networks: ML/AI practitioners at African banks, telecoms, fintechs, and the regional offices of global tech firms; one or two senior researchers at international labs. Each speaker session is one hour: 30 minutes of *"what we actually build and why"*, 30 minutes of cohort Q&A. Speakers do not pitch products and do not recruit.

### Post-program

For three months after the cohort ends, participants retain access to:

- The cohort Slack workspace (peer network + alumni channel).
- One 30-minute 1-on-1 with the lead instructor for career or technical follow-up.
- The hosted version of their capstone (instructor will keep the deployment up for at least 3 months on a free-tier cloud).

This isn't a job-placement service. The goal is to leave participants with a working portfolio, a peer network, and the technical foundation to take their own next step.

### Resources

- **Modules 1-3 (Python, ML foundations).** Aurélien Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed., O'Reilly).
- **Module 3 (Classical ML).** Trevor Hastie, Robert Tibshirani, Jerome Friedman, *The Elements of Statistical Learning* (Springer, 2nd ed.).
- **Module 4 (Recommender systems).** Charu Aggarwal, *Recommender Systems: The Textbook* (Springer, 2016).
- **Module 5 (NLP).** Dan Jurafsky and James Martin, *Speech and Language Processing* (3rd ed. draft).
- **Module 6 (Deep learning).** Ian Goodfellow, Yoshua Bengio, Aaron Courville, *Deep Learning* (MIT Press, 2016).
- **Module 7 (LLMs / GenAI).** Sebastian Raschka, *Build a Large Language Model From Scratch* (Manning, 2024). HuggingFace NLP course.
- **Module 8 (MLOps).** Chip Huyen, *Designing Machine Learning Systems* (O'Reilly, 2022).
- **Topology / geometry-aware ML companion.** Colleen M. Farrelly and Yaé Ulrich Gaba, [*The Shape of Data*](https://nostarch.com/shapeofdata) (No Starch Press).

## Learning Outcomes

By the end of the bootcamp, participants will be able to:

1. Build, evaluate, and deploy a complete ML system end-to-end — from raw data to a working hosted demo.
2. Choose the right model family for a problem and defend the choice against simpler baselines.
3. Diagnose the standard failure modes (data leakage, miscalibration, distribution shift, dead training) before they ship.
4. Apply the modern LLM toolkit (prompt engineering, fine-tuning with LoRA, RAG, agents) to real domain problems.
5. Set up the MLOps machinery (versioning, containerization, monitoring, CI/CD) needed to keep a deployed model alive.
6. Curate a public portfolio that demonstrates working production-grade ML to a technical interviewer.

## Who Should Attend

- **Working professionals** moving into ML/AI roles from adjacent fields — software engineering, data analysis, quantitative finance, actuarial work, scientific computing.
- **Upper-undergraduate and masters students** in mathematics, computer science, statistics, engineering, or quantitative social science who want an intensive route rather than a semester-paced course.
- **Corporate cohorts** running an internal upskilling program — banks, telecoms, insurers, fintechs, public-sector data teams.

You will get more out of this if you arrive with comfortable Python syntax (functions, classes, comprehensions), familiarity with the command line, and undergraduate-level mathematics (linear algebra, calculus, probability). No prior machine-learning experience is required, but it helps.

**Prerequisites:**

- **Required.** Python proficiency at the level of *"can read and modify a 200-line script without getting lost"*. Comfortable with functions, classes, imports, dictionaries, list comprehensions. Familiar with `pip` and virtual environments.
- **Required.** Linear algebra (vectors, matrices, eigenvalues), calculus (derivatives, gradients, integrals), probability (random variables, expectation, conditional probability) at undergraduate level.
- **Strongly recommended.** Some exposure to NumPy / Pandas.
- **Helpful but not required.** Prior ML exposure, familiarity with Git/GitHub, basic Linux command line.

If you are not sure whether you have the prerequisites, the application includes a short technical screen. Honest self-assessment up front is better than scrambling in week 1.

## Brochure

For a printable one-page brochure suitable for forwarding to a corporate L&D team, university department, or admissions committee, write to <a href="mailto:gabayae2@gmail.com?subject=Brochure%20request%20%E2%80%94%20ML%20%26%20AI%20Bootcamp">gabayae2@gmail.com</a> with the audience size and intended cohort window.

To apply directly for a future open cohort, or to discuss a private corporate cohort for your organization, write to <a href="mailto:gabayae2@gmail.com?subject=ML%20%26%20AI%20Bootcamp%20%E2%80%94%20cohort%20inquiry">gabayae2@gmail.com</a>. Please include your background, your goal for the bootcamp, and whether you're asking about an open cohort (individual) or a private corporate cohort (team). For corporate cohorts, also include the team size and the time window you're targeting.
