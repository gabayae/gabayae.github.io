# Capstone Project — ML & AI Bootcamp

Two-week, end-to-end ML project that exercises every module of the bootcamp on a problem the participant chooses. Done individually or in a team of 2–3.

The point is not to ship the cleverest model. It's to ship a project that an external reader — a hiring manager, a collaborator, a domain expert — can open, understand, run, and trust in fifteen minutes.

---

## What you ship

By the end of week 10, every participant submits:

1. **A public GitHub repository** with the code, notebooks, lockfile, README, and instructions to reproduce.
2. **A deployed inference endpoint or hosted demo.** REST API on a free cloud tier (Render, Railway, HuggingFace Spaces, Streamlit Cloud), or a Gradio/Streamlit app. The instructor will keep the deployment running for at least three months after the cohort.
3. **A technical writeup (1,500–3,000 words).** Problem framing, data, methodology, results with honest evaluation, deployment notes, what didn't work and why. Markdown in the repo or a published blog post.
4. **A 10-minute live demo + 5-minute Q&A** during week-10 final presentations.

What you do *not* need to ship: a research paper, a novel algorithm, state-of-the-art results, or a polished marketing pitch.

---

## Project tracks

Pick one. Adjust the dataset to your own domain when possible.

### Track A — Tabular ML for high-stakes decisions

- **Examples.** Credit scoring for underbanked populations, hospital readmission risk, agricultural insurance pricing, telecom churn, fraud detection in mobile money transactions.
- **Required pieces.** Cleaning pipeline, baseline + improved model, calibration analysis, fairness audit across at least two demographic slices, deployed scoring endpoint, monitoring plan.
- **Stretch.** Causal sensitivity analysis (what would change in a target metric if a feature you don't have were available?), counterfactual explanations.

### Track B — Computer vision

- **Examples.** Medical imaging classification (with bias discussion), satellite-image crop yield, document OCR for a low-resource script, defect detection on a manufacturing line.
- **Required pieces.** Preprocessing pipeline, fine-tuned model (transfer learning), evaluation with confusion matrices and per-class breakdowns, deployed inference (image upload → prediction), monitoring for distribution shift.
- **Stretch.** Grad-CAM / saliency analysis, adversarial robustness probe, model compression for edge deployment.

### Track C — NLP / multilingual

- **Examples.** Sentiment or topic classification on multilingual customer reviews, NER on a low-resource African language, document summarization for a domain corpus, semantic search over a knowledge base.
- **Required pieces.** Tokenization choice justified, pretrained model + fine-tuned model, evaluation including human spot-checks, deployed text endpoint or hosted demo.
- **Stretch.** Cross-lingual transfer experiment, error analysis by topic / dialect, comparison with a zero-shot LLM baseline.

### Track D — LLM application / RAG

- **Examples.** RAG over a specific domain corpus (legal, medical, scientific, regulatory), a multi-step agent for a real workflow, a fine-tuned domain LLM with LoRA.
- **Required pieces.** Retrieval pipeline with reranking, generation pipeline, hallucination-detection or grounding evaluation, deployed chat UI or API, latency + cost measurements per query.
- **Stretch.** Evaluation harness with LLM-as-judge + human eval, multi-tenant deployment, response-cache strategy.

### Track E — Time series / forecasting

- **Examples.** Hospital supply chain forecasting, energy demand prediction, river-flow forecasting (Lake Kariba style), seasonal disease incidence prediction.
- **Required pieces.** EDA with seasonal decomposition, baseline (naive, SARIMA) + advanced model (Prophet, gradient boosting, LSTM), prediction intervals not just point forecasts, deployed forecasting endpoint, backtesting protocol.
- **Stretch.** Hierarchical reconciliation, exogenous-variable ablation, monitoring for forecast drift.

### Track F — Bring your own problem

If you have a problem from your work or research and a dataset to support it, propose it. Approved in week 7 by the instructor. Must hit the same required-pieces bar as the tracks above.

---

## Milestones

| Week | Milestone | Deliverable |
|------|-----------|-------------|
| 7 | Track + dataset locked, scope sketched | One-page project brief: problem, data, target metric, plan, risks |
| 8 | Baseline shipped | Working baseline model + initial evaluation, in a public repo with a README |
| 9 | Iteration + first deploy | Improved model, basic deployment, draft writeup outline |
| 10 (mid) | Code freeze + writeup draft | Complete repo, deployed endpoint live, writeup in good shape |
| 10 (end) | Final presentation | 10-min demo + 5-min Q&A, polished writeup, working deployed system |

Milestones aren't optional. Missing one without a flagged reason is grounds for an incomplete capstone (and no certificate).

---

## Evaluation rubric

The capstone is graded on five dimensions, each out of 10.

### 1. Problem framing (10)

- Is the problem stated clearly enough that an outsider can repeat it?
- Is the target metric the right metric for the actual decision being supported?
- Is the dataset appropriate for the problem (or are its limitations named honestly)?

### 2. Methodology (10)

- Was the choice of method justified, or just defaulted to?
- Is the train/validation/test discipline correct? No leakage?
- Are baselines sensible and reported alongside the main model?
- Is hyperparameter tuning done in a way that doesn't contaminate the test set?

### 3. Evaluation honesty (10)

- Are the right metrics used, with confidence intervals where appropriate?
- Are failure modes investigated, not just headline accuracy?
- Is fairness / subgroup performance examined where the problem warrants it?
- Are known limitations stated up front?

### 4. Reproducibility and deployment (10)

- Can a reader clone the repo and reproduce the main result from scratch?
- Is the deployment actually working, with reasonable latency?
- Is the deployment documented (how to call it, what it returns, what could go wrong)?
- Is there a monitoring plan, even if minimal?

### 5. Writeup and communication (10)

- Is the README enough to orient an external reader in 5 minutes?
- Is the writeup honest about what worked, what didn't, and why?
- Is the demo coherent and well-paced?
- Are visualizations chosen for the reader, not for the author?

**Passing the capstone requires at least 6/10 on every dimension and 35/50 overall.** Falling below on one dimension may be recoverable with a revision before the certificate is issued; falling below on two or more is not.

A capstone that scores 45+/50 typically becomes a strong portfolio anchor and is the kind of project that opens doors in technical interviews.

---

## What good looks like

A successful capstone usually has these properties:

- **A specific, narrow problem.** "Predict X for population Y in context Z" beats "Build an ML system for [broad domain]."
- **A real dataset.** Synthetic or contest data is acceptable only if there's a defensible reason. A real, messy dataset that participants had to clean is usually a stronger story than a polished benchmark.
- **A baseline that works.** A linear-regression or random-forest baseline that ships and is honestly evaluated beats a deep-learning model that doesn't quite work.
- **A deployed thing the reader can poke.** Even a small Gradio demo that runs is worth more than a notebook claiming production-grade performance.
- **A writeup that names trade-offs.** Every real ML system has trade-offs. The writeup that says *"we chose X over Y because of Z, and here's what we'd watch for"* reads as competent. The writeup that pretends there were no trade-offs reads as a tutorial.

---

## What to avoid

- **Mismatch between metric and decision.** Optimizing accuracy when the actual cost structure is asymmetric (e.g., false negatives much costlier than false positives in medical screening).
- **Toy datasets dressed up as case studies.** MNIST and Iris are pedagogically useful; they're not capstone material.
- **Deploying something that wasn't actually evaluated.** A live endpoint serving a model with known data leakage is worse than no deployment.
- **Overclaiming.** "Our model achieves state-of-the-art on..." is almost never true and is easy to verify against. Honest framing earns more credit than ambitious framing.
- **Skipping the writeup.** A capstone without a clear writeup is invisible. Hiring managers don't run unfamiliar code; they read READMEs.

---

## Reuse and credit

Code, datasets, and ideas from the bootcamp labs are fair game in the capstone. So is open-source code, with attribution. Pre-existing personal projects can serve as a starting point, but the capstone must include substantive new work and be clearly delimited from prior contributions in the writeup.

If you use external help — an LLM coding assistant, a collaborator, a Stack Overflow answer — say so. The expectation is not that you did everything alone. The expectation is that you understand what you shipped and can defend it in the Q&A.
