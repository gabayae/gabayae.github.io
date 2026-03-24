# Introduction to Generative AI & LLMs — 3-Day Workshop

**Instructor:** Dr. Yaé Ulrich Gaba
**Duration:** 3 days (18 hours)
**Level:** Intermediate
**Language:** English

---

## Overview

This workshop provides a practical, hands-on introduction to generative AI and Large Language Models (LLMs). Participants learn prompt engineering, fine-tuning, Retrieval-Augmented Generation (RAG), and deployment strategies. The workshop balances conceptual understanding with practical implementation using both commercial APIs (OpenAI) and open-source models.

## Prerequisites

- Basic Python programming (variables, functions, loops)
- Familiarity with machine learning concepts (training, inference, evaluation)
- An OpenAI API key (free tier available at [platform.openai.com](https://platform.openai.com))
- Laptop with Python 3.10+ installed

## Learning Objectives

By the end of this workshop, participants will be able to:

1. Understand the architecture and capabilities of modern LLMs
2. Write effective prompts using structured prompt engineering techniques
3. Build applications using the OpenAI API and LangChain
4. Implement Retrieval-Augmented Generation (RAG) pipelines
5. Fine-tune open-source models on custom datasets
6. Evaluate LLM outputs and deploy applications responsibly

## Software Requirements

- Python 3.10+
- Libraries: openai, langchain, transformers, sentence-transformers, chromadb, gradio
- Optional: HuggingFace account, GPU access (Google Colab free tier works)

---

## Day-by-Day Program

### Day 1: Understanding LLMs & Prompt Engineering

**Objectives:** Understand how LLMs work and master prompt engineering techniques.

| Time | Topic |
|------|-------|
| 09:00–10:00 | **The Generative AI Landscape** — From GPT to Claude to open-source: timeline, key models, capabilities and limitations, tokens and context windows |
| 10:00–10:45 | **How LLMs Work** — Transformer architecture (intuition, not math-heavy), pre-training, instruction tuning, RLHF, emergent capabilities |
| 10:45–11:00 | *Break* |
| 11:00–12:30 | **Prompt Engineering Fundamentals** — Zero-shot, few-shot, chain-of-thought, role prompting, system prompts, structured output (JSON mode), temperature and top-p |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **Advanced Prompting** — Prompt chaining, self-consistency, tree-of-thought, meta-prompting, prompt templates, handling long contexts |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **OpenAI API** — Authentication, chat completions, streaming, function calling / tool use, vision API, cost management |

**Lab 1:** Build a prompt engineering toolkit: create a set of reusable prompt templates for common tasks (summarization, extraction, classification, code generation). Test each with different models and compare outputs.

**Homework:** Use the OpenAI API to build a script that summarizes academic papers from their abstracts.

---

### Day 2: Building Applications — RAG & LangChain

**Objectives:** Build practical LLM-powered applications using RAG and orchestration frameworks.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Embeddings & Vector Search** — What are embeddings, sentence-transformers, similarity search, vector databases (ChromaDB, FAISS), indexing strategies |
| 10:30–10:45 | *Break* |
| 10:45–12:30 | **Retrieval-Augmented Generation** — RAG architecture, document loading (PDF, web, CSV), chunking strategies, retrieval + generation pipeline, handling hallucinations |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **LangChain Essentials** — Chains, agents, tools, memory, output parsers. Building a multi-step reasoning agent |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Building a Q&A System** — End-to-end: ingest documents, build vector index, create retrieval chain, add conversation memory, deploy with Gradio |

**Lab 2:** Build a RAG-powered Q&A chatbot that answers questions about a collection of research papers (PDFs provided). The system should cite its sources and handle "I don't know" gracefully.

**Homework:** Extend the chatbot to handle a new document collection relevant to your research/work.

---

### Day 3: Fine-Tuning, Evaluation & Deployment

**Objectives:** Fine-tune models, evaluate outputs rigorously, and deploy responsibly.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Fine-Tuning Concepts** — When to fine-tune vs. prompt vs. RAG, data preparation, instruction format, LoRA and parameter-efficient methods |
| 10:30–10:45 | *Break* |
| 10:45–12:00 | **Hands-On Fine-Tuning** — Fine-tuning a small open-source model (e.g., Mistral 7B / Llama) on a custom dataset using HuggingFace Transformers + PEFT. Using Google Colab for GPU access |
| 12:00–12:30 | **OpenAI Fine-Tuning API** — Preparing JSONL data, launching fine-tuning jobs, evaluating results, cost considerations |
| 12:30–14:00 | *Lunch* |
| 14:00–15:00 | **Evaluation** — Human evaluation, automated metrics (BLEU, ROUGE, BERTScore), LLM-as-judge, evaluation frameworks, red teaming basics |
| 15:00–15:15 | *Break* |
| 15:15–16:00 | **Deployment & Ethics** — API deployment, Gradio/Streamlit interfaces, rate limiting, content filtering, bias detection, responsible AI guidelines, African context considerations |
| 16:00–17:00 | **Capstone & Wrap-Up** — Present projects, discussion on LLM futures in research and industry, Q&A, certificates |

**Lab 3 (Capstone):** Choose one project:
- **Research assistant:** RAG chatbot for a specific research domain with citation support
- **Document analyzer:** Automated extraction of key findings from a corpus of papers
- **Custom classifier:** Fine-tuned model for domain-specific text classification (e.g., medical reports, legal documents)

---

## Assessment

- **Daily labs** (50%) — Working applications and code quality
- **Capstone project** (30%) — End-to-end application presented on Day 3
- **Participation** (20%) — Engagement and homework

## Resources

- [OpenAI Documentation](https://platform.openai.com/docs)
- [LangChain Documentation](https://python.langchain.com/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [RAG Paper (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401)

## Certificate

Participants who complete all labs and the capstone project receive a certificate of completion.
