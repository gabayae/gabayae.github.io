---
layout: workshop
permalink: /workshops/generative-ai-llms/en/
lang: en
title: "Introduction to Generative AI & LLMs"
tagline: "A practical, hands-on path through prompt engineering, RAG, fine-tuning, and responsible deployment of modern LLMs."
description: "3-day workshop: LLMs, prompt engineering, fine-tuning (LoRA), RAG, deployment."

# --- Sidebar metadata ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "3 days (≈ 18 hours)"
level: "Intermediate"
format: "On-site, live online, or hybrid"
languages: "English &amp; French"
certificate: "Certificate of completion"

# --- Materials links shown in the sidebar ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/generative-ai-llms

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Workshop inquiry — Introduction to Generative AI & LLMs"
---

## Program Overview

This workshop provides a practical, hands-on introduction to generative AI and Large Language Models (LLMs). Participants learn prompt engineering, fine-tuning, Retrieval-Augmented Generation (RAG), and deployment strategies. The workshop balances conceptual understanding with practical implementation using both commercial APIs (OpenAI) and open-source models.

### Software Requirements

- Python 3.10+
- Libraries: openai, langchain, transformers, sentence-transformers, chromadb, gradio
- Optional: HuggingFace account, GPU access (Google Colab free tier works)

### Day 1: Understanding LLMs & Prompt Engineering

**Objectives:** Understand how LLMs work and master prompt engineering techniques.

- **The Generative AI Landscape** — From GPT to Claude to open-source: timeline, key models, capabilities and limitations, tokens and context windows
- **How LLMs Work** — Transformer architecture (intuition, not math-heavy), pre-training, instruction tuning, RLHF, emergent capabilities
- **Prompt Engineering Fundamentals** — Zero-shot, few-shot, chain-of-thought, role prompting, system prompts, structured output (JSON mode), temperature and top-p
- **Advanced Prompting** — Prompt chaining, self-consistency, tree-of-thought, meta-prompting, prompt templates, handling long contexts
- **OpenAI API** — Authentication, chat completions, streaming, function calling / tool use, vision API, cost management

**Lab 1:** Build a prompt engineering toolkit: create a set of reusable prompt templates for common tasks (summarization, extraction, classification, code generation). Test each with different models and compare outputs.

**Homework:** Use the OpenAI API to build a script that summarizes academic papers from their abstracts.

### Day 2: Building Applications — RAG & LangChain

**Objectives:** Build practical LLM-powered applications using RAG and orchestration frameworks.

- **Embeddings & Vector Search** — What are embeddings, sentence-transformers, similarity search, vector databases (ChromaDB, FAISS), indexing strategies
- **Retrieval-Augmented Generation** — RAG architecture, document loading (PDF, web, CSV), chunking strategies, retrieval + generation pipeline, handling hallucinations
- **LangChain Essentials** — Chains, agents, tools, memory, output parsers. Building a multi-step reasoning agent
- **Building a Q&A System** — End-to-end: ingest documents, build vector index, create retrieval chain, add conversation memory, deploy with Gradio

**Lab 2:** Build a RAG-powered Q&A chatbot that answers questions about a collection of research papers (PDFs provided). The system should cite its sources and handle "I don't know" gracefully.

**Homework:** Extend the chatbot to handle a new document collection relevant to your research/work.

### Day 3: Fine-Tuning, Evaluation & Deployment

**Objectives:** Fine-tune models, evaluate outputs rigorously, and deploy responsibly.

- **Fine-Tuning Concepts** — When to fine-tune vs. prompt vs. RAG, data preparation, instruction format, LoRA and parameter-efficient methods
- **Hands-On Fine-Tuning** — Fine-tuning a small open-source model (e.g., Mistral 7B / Llama) on a custom dataset using HuggingFace Transformers + PEFT. Using Google Colab for GPU access
- **OpenAI Fine-Tuning API** — Preparing JSONL data, launching fine-tuning jobs, evaluating results, cost considerations
- **Evaluation** — Human evaluation, automated metrics (BLEU, ROUGE, BERTScore), LLM-as-judge, evaluation frameworks, red teaming basics
- **Deployment & Ethics** — API deployment, Gradio/Streamlit interfaces, rate limiting, content filtering, bias detection, responsible AI guidelines, African context considerations
- **Capstone & Wrap-Up** — Present projects, discussion on LLM futures in research and industry, Q&A, certificates

**Lab 3 (Capstone):** Choose one project:
- **Research assistant:** RAG chatbot for a specific research domain with citation support
- **Document analyzer:** Automated extraction of key findings from a corpus of papers
- **Custom classifier:** Fine-tuned model for domain-specific text classification (e.g., medical reports, legal documents)

### Assessment

- **Daily labs** (50%) — Working applications and code quality
- **Capstone project** (30%) — End-to-end application presented on Day 3
- **Participation** (20%) — Engagement and homework

### Resources

- [OpenAI Documentation](https://platform.openai.com/docs)
- [LangChain Documentation](https://python.langchain.com/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [RAG Paper (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401)

## Learning Outcomes

By the end of this workshop, participants will be able to:

1. Understand the architecture and capabilities of modern LLMs
2. Write effective prompts using structured prompt engineering techniques
3. Build applications using the OpenAI API and LangChain
4. Implement Retrieval-Augmented Generation (RAG) pipelines
5. Fine-tune open-source models on custom datasets
6. Evaluate LLM outputs and deploy applications responsibly

## Who Should Attend

Researchers, engineers, and technical practitioners who want to move from talking about generative AI to building working LLM-powered applications. Useful for ML practitioners adding LLMs to their toolkit, software engineers integrating GPT-style APIs into products, and graduate students working with text data.

**Prerequisites:**

- Basic Python programming (variables, functions, loops)
- Familiarity with machine learning concepts (training, inference, evaluation)
- An OpenAI API key (free tier available at [platform.openai.com](https://platform.openai.com))
- Laptop with Python 3.10+ installed

## Brochure

Lecture notes and lab notebooks are linked in the sidebar.

For a printable one-page brochure suitable for forwarding to a program committee, conference organizer, or corporate L&D team, write to <a href="mailto:gabayae2@gmail.com?subject=Brochure%20request%20%E2%80%94%20Introduction%20to%20Generative%20AI%20%26%20LLMs">gabayae2@gmail.com</a> with the audience size and intended delivery dates.
