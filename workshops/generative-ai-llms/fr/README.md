---
layout: workshop
permalink: /workshops/generative-ai-llms/fr/
lang: fr
title: "Introduction à l'IA Générative & aux LLMs"
tagline: "Un parcours pratique : prompt engineering, RAG, fine-tuning et déploiement responsable des LLMs modernes."
description: "Atelier de 3 jours : LLMs, prompt engineering, fine-tuning (LoRA), RAG, déploiement."

# --- Métadonnées de la barre latérale ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "3 jours (≈ 18 heures)"
level: "Intermédiaire"
format: "Sur site, en ligne en direct, ou hybride"
languages: "Français &amp; anglais"
certificate: "Certificat de complétion"

# --- Liens des supports ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/generative-ai-llms

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Demande d'atelier — Introduction à l'IA Générative & aux LLMs"
---

## Présentation du programme

Cet atelier offre une introduction pratique à l'IA générative et aux grands modèles de langage (LLMs). Les participants apprennent le prompt engineering, le fine-tuning, la génération augmentée par récupération (RAG) et les stratégies de déploiement. L'atelier équilibre compréhension conceptuelle et implémentation pratique avec les APIs commerciales (OpenAI) et les modèles open-source.

### Logiciels Requis

- Python 3.10+
- Bibliothèques : openai, langchain, transformers, sentence-transformers, chromadb, gradio
- Optionnel : compte HuggingFace, accès GPU (Google Colab gratuit suffit)

### Jour 1 : Comprendre les LLMs & Prompt Engineering

**Objectifs :** Comprendre le fonctionnement des LLMs et maîtriser les techniques de prompt engineering.

- **Le Paysage de l'IA Générative** — De GPT à Claude en passant par l'open-source : chronologie, modèles clés, capacités et limites, tokens et fenêtres de contexte
- **Comment Fonctionnent les LLMs** — Architecture Transformer (intuition, pas de mathématiques lourdes), pré-entraînement, instruction tuning, RLHF, capacités émergentes
- **Fondamentaux du Prompt Engineering** — Zero-shot, few-shot, chaîne de pensée, role prompting, system prompts, sortie structurée (mode JSON), température et top-p
- **Prompting Avancé** — Chaînage de prompts, auto-cohérence, arbre de pensée, méta-prompting, modèles de prompts, gestion des longs contextes
- **API OpenAI** — Authentification, complétions de chat, streaming, appel de fonctions / utilisation d'outils, API vision, gestion des coûts

**TP 1 :** Construire une boîte à outils de prompt engineering : créer un ensemble de modèles de prompts réutilisables pour des tâches courantes (résumé, extraction, classification, génération de code). Tester avec différents modèles et comparer les sorties.

**Devoir :** Utiliser l'API OpenAI pour construire un script qui résume des articles académiques à partir de leurs résumés.

### Jour 2 : Construction d'Applications — RAG & LangChain

**Objectifs :** Construire des applications pratiques alimentées par les LLMs avec RAG et des frameworks d'orchestration.

- **Embeddings & Recherche Vectorielle** — Qu'est-ce qu'un embedding, sentence-transformers, recherche par similarité, bases de données vectorielles (ChromaDB, FAISS), stratégies d'indexation
- **Retrieval-Augmented Generation** — Architecture RAG, chargement de documents (PDF, web, CSV), stratégies de découpage, pipeline récupération + génération, gestion des hallucinations
- **Essentiels de LangChain** — Chaînes, agents, outils, mémoire, parseurs de sortie. Construction d'un agent de raisonnement multi-étapes
- **Construction d'un Système Q&R** — De bout en bout : ingérer les documents, construire l'index vectoriel, créer la chaîne de récupération, ajouter la mémoire conversationnelle, déployer avec Gradio

**TP 2 :** Construire un chatbot Q&R alimenté par RAG qui répond aux questions sur une collection d'articles de recherche (PDFs fournis). Le système doit citer ses sources et gérer le « je ne sais pas » de manière élégante.

**Devoir :** Étendre le chatbot pour gérer une nouvelle collection de documents pertinente pour votre recherche/travail.

### Jour 3 : Fine-Tuning, Évaluation & Déploiement

**Objectifs :** Fine-tuner des modèles, évaluer les sorties rigoureusement et déployer de manière responsable.

- **Concepts du Fine-Tuning** — Quand fine-tuner vs. prompter vs. RAG, préparation des données, format d'instructions, LoRA et méthodes à paramètres efficaces
- **Fine-Tuning Pratique** — Fine-tuner un petit modèle open-source (ex. : Mistral 7B / Llama) sur un jeu de données personnalisé avec HuggingFace Transformers + PEFT. Utilisation de Google Colab pour l'accès GPU
- **API de Fine-Tuning OpenAI** — Préparation des données JSONL, lancement des tâches, évaluation des résultats, considérations de coût
- **Évaluation** — Évaluation humaine, métriques automatisées (BLEU, ROUGE, BERTScore), LLM-as-judge, frameworks d'évaluation, bases du red teaming
- **Déploiement & Éthique** — Déploiement par API, interfaces Gradio/Streamlit, limitation de débit, filtrage de contenu, détection de biais, lignes directrices IA responsable, considérations du contexte africain
- **Projet Final & Bilan** — Présentations des projets, discussion sur l'avenir des LLMs en recherche et industrie, questions, certificats

**TP 3 (Projet Final) :** Choisir un projet :
- **Assistant de recherche :** chatbot RAG pour un domaine de recherche spécifique avec support de citations
- **Analyseur de documents :** extraction automatisée des résultats clés d'un corpus d'articles
- **Classificateur personnalisé :** modèle fine-tuné pour la classification de texte spécifique à un domaine (ex. : rapports médicaux, documents juridiques)

### Évaluation

- **TPs quotidiens** (50 %) — Applications fonctionnelles et qualité du code
- **Projet final** (30 %) — Application de bout en bout présentée le Jour 3
- **Participation** (20 %) — Engagement et devoirs

### Ressources

- [Documentation OpenAI](https://platform.openai.com/docs)
- [Documentation LangChain](https://python.langchain.com/)
- [HuggingFace Transformers](https://huggingface.co/docs/transformers)
- [Guide de Prompt Engineering](https://www.promptingguide.ai/)
- [Article RAG (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401)

## Objectifs pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Comprendre l'architecture et les capacités des LLMs modernes
2. Rédiger des prompts efficaces avec des techniques structurées
3. Construire des applications avec l'API OpenAI et LangChain
4. Implémenter des pipelines de Retrieval-Augmented Generation (RAG)
5. Fine-tuner des modèles open-source sur des jeux de données personnalisés
6. Évaluer les sorties des LLMs et déployer des applications de manière responsable

## Public visé

Chercheurs, ingénieurs et praticiens techniques qui veulent passer du discours sur l'IA générative à la construction d'applications LLM fonctionnelles. Utile pour les praticiens ML qui ajoutent les LLMs à leur boîte à outils, les développeurs qui intègrent des APIs de type GPT à des produits, et les doctorants qui travaillent avec des données textuelles.

**Prérequis :**

- Programmation Python de base (variables, fonctions, boucles)
- Familiarité avec les concepts de machine learning (entraînement, inférence, évaluation)
- Une clé API OpenAI (niveau gratuit disponible sur [platform.openai.com](https://platform.openai.com))
- Ordinateur portable avec Python 3.10+

## Plaquette

Les notes de cours et notebooks sont accessibles depuis la barre latérale.

Pour une plaquette d'une page, à transmettre à un comité de programme, un organisateur de conférence ou une équipe formation interne, écrivez à <a href="mailto:gabayae2@gmail.com?subject=Demande%20de%20plaquette%20%E2%80%94%20Introduction%20%C3%A0%20l%27IA%20G%C3%A9n%C3%A9rative%20%26%20aux%20LLMs">gabayae2@gmail.com</a> en précisant la taille de l'audience et les dates envisagées.
