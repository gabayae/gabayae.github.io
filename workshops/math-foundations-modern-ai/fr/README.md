---
layout: workshop
permalink: /workshops/math-foundations-modern-ai/fr/
lang: fr
title: "Fondations mathématiques de l'IA moderne"
tagline: "Les mathématiques derrière les systèmes d'IA d'aujourd'hui — en cinq jours, sans prérequis mathématique avancé."
description: "Atelier de 5 jours : les structures mathématiques derrière les modèles modernes — algèbre linéaire, optimisation, probabilités, modélisation, évaluation."

# --- Métadonnées de la barre latérale ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "5 jours (≈ 30 heures)"
level: "Intermédiaire — aucun prérequis mathématique avancé"
format: "Sur site, en ligne en direct, ou hybride"
languages: "Français &amp; anglais"
next_session: "Sur demande"
pricing: "Honoraires pour conférences / institutions académiques ; tarifs entreprise sur demande"
certificate: "Certificat de complétion"

# --- Liens des supports ---
syllabus_pdf: /workshops/math-foundations-modern-ai/fr/cours.pdf
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/math-foundations-modern-ai/notebooks

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Demande d'atelier — Fondations mathématiques de l'IA moderne"
---

## Présentation

L'IA évolue vite, mais les idées qui font tourner les systèmes d'aujourd'hui sont stables et accessibles. Cet atelier construit l'intuition mathématique et le vocabulaire de modélisation nécessaires pour comprendre ce qui se passe sous le capot des modèles modernes — supervisés, non supervisés, génératifs.

L'objectif n'est pas de faire des participants des spécialistes du deep learning. Il est de leur donner les structures mentales pour évaluer une méthode, dialoguer avec une équipe technique, formuler un problème métier en problème d'apprentissage, et décider quand déployer (ou ne pas déployer) un outil d'IA.

## Public visé

Ingénieurs, chefs de produit, analystes, responsables d'équipes techniques qui prennent des décisions sur l'IA. Praticiens qui collaborent avec des équipes ML et veulent une compréhension réelle des fondations. Chercheurs d'autres disciplines qui veulent passer du discours sur l'IA à la pratique.

## Prérequis

À l'aise avec les mathématiques de lycée et de premier cycle universitaire (vecteurs, fonctions, dérivées, probabilités de base). Une familiarité avec Python aide pour les travaux pratiques mais n'est pas requise pour les cours. **Aucun prérequis avancé.**

## Objectifs pédagogiques

À la fin de l'atelier, les participants seront capables de :

1. Comprendre les idées centrales d'algèbre linéaire, d'optimisation et de probabilités qui sous-tendent les systèmes d'IA modernes.
2. Décrire la structure, l'entraînement et l'évaluation des modèles ML / IA courants (MLP, autoencodeurs, modèles de diffusion).
3. Formuler un problème réel dans le langage structuré d'un pipeline d'IA.
4. Choisir une architecture, une fonction de perte et un biais inductif adaptés au domaine d'application.
5. Évaluer la fiabilité d'un modèle par le raisonnement statistique, les méthodes de validation et la conscience des modes d'échec classiques.
6. Prendre des décisions techniquement informées sur le déploiement d'outils d'IA.

## Programme

Les 5 jours alternent cours du matin et travaux pratiques l'après-midi. Tous les TP tournent sur Google Colab (offre gratuite) ou tout environnement Python 3.10+ local avec PyTorch.

### Jour 1 — Algèbre linéaire et modèles paramétriques

**Thème :** représenter données et modèles avec vecteurs, matrices et transformations.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:30 | **Espaces vectoriels, applications linéaires, dimensions** — du vecteur de features à l'espace latent ; notion de représentation. |
| 10:45–12:30 | **Du perceptron au MLP** — couches, activations non-linéaires, pourquoi la composition de fonctions linéaires ne suffit pas. |
| 14:00–15:30 | **Plongements et autoencodeurs** — apprendre une représentation compacte ; géométrie de l'espace latent. |
| 15:45–17:00 | **TP1** — visualiser les couches et cartes de features d'un réseau pré-entraîné. |

### Jour 2 — Calcul différentiel et optimisation

**Thème :** fonctions de perte et apprentissage par gradient.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:30 | **Dérivées multivariées, règle de la chaîne** — pourquoi le gradient est la bonne direction. |
| 10:45–12:30 | **Descente de gradient, SGD, Adam** — taux d'apprentissage, courbes d'apprentissage, hyperparamètres. |
| 14:00–15:30 | **Rétropropagation et programmation différentiable** — comment PyTorch calcule un gradient sans qu'on lui demande. |
| 15:45–17:00 | **TP2** — entraîner un réseau de neurones de bout en bout. |

### Jour 3 — Probabilités et modélisation générative

**Thème :** le hasard comme outil de modélisation ; apprendre et échantillonner depuis des distributions.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:30 | **Distributions, densités, vraisemblance** — le langage probabiliste de l'apprentissage. |
| 10:45–12:30 | **Modèles génératifs : VAE, modèles de diffusion, méthodes basées sur le score** — comment générer une image (ou un texte) à partir du bruit. |
| 14:00–15:30 | **Processus de bruit et inversion** — l'intuition derrière la diffusion. |
| 15:45–17:00 | **TP3** — entraîner un modèle de diffusion simple. |

### Jour 4 — Modélisation pour l'IA

**Thème :** transformer un problème désordonné en problème mathématique structuré.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:30 | **Optimisation contrainte et non contrainte, régularisation** — quand ajouter une contrainte change tout. |
| 10:45–12:30 | **Invariance et équivariance** — pourquoi un CNN est meilleur qu'un MLP pour les images, et la généralisation de cette idée. |
| 14:00–15:30 | **Architectures spécialisées : CNN, GNN, attention** — le biais inductif comme choix de modélisation. |
| 15:45–17:00 | **TP4** — comparer plusieurs choix de modèle sur une tâche d'apprentissage sur graphes. |

### Jour 5 — Évaluer les modèles d'IA

**Thème :** généralisation, fiabilité, prendre des décisions informées.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:30 | **Statistiques de base, biais–variance, sur-apprentissage** — diagnostiquer une courbe d'apprentissage. |
| 10:45–12:30 | **Validation, calibration, incertitude** — au-delà de la précision moyenne. |
| 14:00–15:30 | **Exemples adversariaux, données hors distribution** — pourquoi un modèle qui marche en lab échoue en production. |
| 15:45–17:00 | **TP5** — comparer des modèles sous décalage de distribution ; bilan. |

## Évaluation

- **TPs quotidiens** (60 %) — implémentations fonctionnelles et analyse.
- **Mini-projet final** (30 %) — formuler un problème métier en pipeline d'IA et défendre les choix.
- **Participation** (10 %) — engagement, questions, discussions.

## Lectures recommandées

- Goodfellow, Bengio & Courville, *Deep Learning* (MIT Press, accès libre).
- Bishop & Bishop, *Deep Learning: Foundations and Concepts* (Springer, 2024).
- Murphy, *Probabilistic Machine Learning* (MIT Press, accès libre).
- Strang, *Linear Algebra and Learning from Data*.
- Ho, Jain & Abbeel, « Denoising Diffusion Probabilistic Models », NeurIPS 2020 ([arXiv:2006.11239](https://arxiv.org/abs/2006.11239)).
- Vaswani et al., « Attention Is All You Need », NeurIPS 2017 ([arXiv:1706.03762](https://arxiv.org/abs/1706.03762)).

## Inviter cet atelier

Organisateurs de conférence, départements universitaires, équipes d'entreprise : écrivez à <a href="mailto:gabayae2@gmail.com?subject=Demande%20d%27atelier%20%E2%80%94%20Fondations%20math%C3%A9matiques%20de%20l%27IA%20moderne">gabayae2@gmail.com</a> pour discuter dates, format (sur site, en ligne, hybride) et adaptation au public. L'atelier a déjà été donné en contexte académique, secteur public et entreprise ; les supports peuvent être adaptés au domaine de pratique de l'audience.
