# Generative AI: From Foundations to Production

A 30-hour practical course covering modern generative AI --- large language models, diffusion models, prompt engineering, fine-tuning, RAG, agents, and responsible deployment. Designed for students and practitioners with basic Python and machine learning knowledge.

## Structure

| Chapter | Topic | Hours | Key models / tools |
|---------|-------|-------|--------------------|
| 1 | Foundations of language models | 3h | GPT-2, BPE tokenizer, tiktoken |
| 2 | The Transformer architecture | 3h | DistilBERT, attention visualization |
| 3 | GPT and text generation | 3h | GPT-2, TinyLlama, HuggingFace generate() |
| 4 | Prompt engineering | 3h | Gemini API, Groq API, structured output |
| 5 | Fine-tuning LLMs | 3h | LoRA, QLoRA, TinyLlama, HuggingFace Trainer |
| 6 | Retrieval-augmented generation (RAG) | 3h | ChromaDB, FAISS, LangChain, all-MiniLM-L6-v2 |
| 7 | Diffusion models and image generation | 3h | Stable Diffusion, diffusers, ControlNet |
| 8 | Evaluation, safety, and alignment | 3h | BLEU, ROUGE, RLHF, red-teaming |
| 9 | LLM agents and tool use | 3h | LangChain agents, ReAct, LangGraph |
| 10 | Capstone projects | 3h | 5 end-to-end projects |

## Prerequisites

- Python 3.10+ (comfortable with functions, classes, pip)
- Basic machine learning (what is a loss function, gradient descent, train/test split)
- Linear algebra basics (vectors, matrices, dot products)
- No prior NLP or deep learning experience required

## Tools and libraries

- **Python 3.10+** with pip
- **Google Colab** (free tier with GPU) --- recommended for all exercises
- **HuggingFace** ecosystem: transformers, datasets, peft, diffusers, accelerate
- **LangChain** and **LangGraph** for RAG and agents
- **ChromaDB** and **FAISS** for vector search
- **Groq** free API (fast LLM inference)
- **Google Gemini** free API

## Key free resources

- HuggingFace NLP Course: https://huggingface.co/learn/nlp-course
- Andrej Karpathy, "Let's build GPT": https://www.youtube.com/watch?v=kCc8FmEb1nY
- LangChain documentation: https://python.langchain.com/docs/
- Google Generative AI documentation: https://ai.google.dev/
- Groq Cloud (free API): https://console.groq.com/
- ChromaDB documentation: https://docs.trychroma.com/
- HuggingFace diffusers: https://huggingface.co/docs/diffusers/
- Sebastian Raschka, "Build a Large Language Model From Scratch" (2024)
- Jay Alammar, "The Illustrated Transformer": https://jalammar.github.io/illustrated-transformer/

## Languages

- `en/` --- English lecture notes (LaTeX + PDF)
- `code/python/` --- Python scripts per chapter
- `code/notebooks/` --- Jupyter notebooks per chapter
