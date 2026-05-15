# IA Générative : des fondements à la production / Generative AI: from foundations to production

Cours pratique de 30 heures couvrant l'IA générative moderne — grands modèles de langage, modèles de diffusion, prompt engineering, fine-tuning, RAG, agents, et déploiement responsable. Conçu pour étudiants et praticiens connaissant déjà Python et l'apprentissage automatique de base.

A 30-hour practical course covering modern generative AI — large language models, diffusion models, prompt engineering, fine-tuning, RAG, agents, and responsible deployment. Designed for students and practitioners with basic Python and machine learning knowledge.

## Structure

| Chapitre / Chapter | Sujet / Topic | Heures / Hours | Modèles / outils clés |
|---|---|---|---|
| 1 | Fondements des modèles de langage | 3h | GPT-2, tokeniseur BPE, tiktoken |
| 2 | L'architecture Transformer | 3h | DistilBERT, visualisation d'attention |
| 3 | GPT et génération de texte | 3h | GPT-2, TinyLlama, HuggingFace generate() |
| 4 | Prompt engineering | 3h | API Gemini, API Groq, sortie structurée |
| 5 | Fine-tuning des LLM | 3h | LoRA, QLoRA, TinyLlama, HuggingFace Trainer |
| 6 | Génération augmentée par récupération (RAG) | 3h | ChromaDB, FAISS, LangChain, all-MiniLM-L6-v2 |
| 7 | Modèles de diffusion et génération d'images | 3h | Stable Diffusion, diffusers, ControlNet |
| 8 | Évaluation, sûreté et alignement | 3h | BLEU, ROUGE, RLHF, red-teaming |
| 9 | Agents LLM et utilisation d'outils | 3h | LangChain agents, ReAct, LangGraph |
| 10 | Projets de fin de cours | 3h | 5 projets de bout en bout |

## Prérequis / Prerequisites

- Python 3.10+ (à l'aise avec fonctions, classes, pip)
- Bases d'apprentissage automatique (fonction de perte, descente de gradient, division train/test)
- Bases d'algèbre linéaire (vecteurs, matrices, produits scalaires)
- Aucune expérience préalable en TAL ou deep learning requise

## Outils et bibliothèques / Tools and libraries

- **Python 3.10+** avec pip
- **Google Colab** (offre gratuite avec GPU) — recommandé pour tous les exercices
- Écosystème **HuggingFace** : transformers, datasets, peft, diffusers, accelerate
- **LangChain** et **LangGraph** pour RAG et agents
- **ChromaDB** et **FAISS** pour la recherche vectorielle
- API gratuite **Groq** (inférence LLM rapide)
- API gratuite **Google Gemini**

## Ressources gratuites clés / Key free resources

- HuggingFace NLP Course: https://huggingface.co/learn/nlp-course
- Andrej Karpathy, "Let's build GPT": https://www.youtube.com/watch?v=kCc8FmEb1nY
- LangChain documentation: https://python.langchain.com/docs/
- Google Generative AI documentation: https://ai.google.dev/
- Groq Cloud (free API): https://console.groq.com/
- ChromaDB documentation: https://docs.trychroma.com/
- HuggingFace diffusers: https://huggingface.co/docs/diffusers/
- Sebastian Raschka, "Build a Large Language Model From Scratch" (2024)
- Jay Alammar, "The Illustrated Transformer": https://jalammar.github.io/illustrated-transformer/

## Structure du dépôt / Repository structure

- `fr/` — Notes de cours en français (LaTeX + PDF)
- `en/` — English lecture notes (LaTeX + PDF)
- `code/python/` — Scripts Python par chapitre / Python scripts per chapter
- `code/notebooks/` — Notebooks Jupyter par chapitre / Jupyter notebooks per chapter

## Compilation

```bash
# Version française
cd fr && xelatex -shell-escape cours.tex && xelatex -shell-escape cours.tex

# English version
cd en && xelatex -shell-escape notes.tex && xelatex -shell-escape notes.tex
```
