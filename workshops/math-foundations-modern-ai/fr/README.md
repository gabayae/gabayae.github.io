---
layout: page
permalink: /workshops/math-foundations-modern-ai/fr/
title: "Fondations mathématiques de l'IA moderne — Atelier de 5 jours"
description: "Atelier de 5 jours : les structures mathématiques derrière les modèles modernes — algèbre linéaire, optimisation, probabilités, modélisation, évaluation."
lang: fr
---

**Formateur :** Dr. Yaé Ulrich Gaba
**Durée :** 5 jours
**Niveau :** Intermédiaire — aucun prérequis mathématique avancé
**Langue :** Français

---

## Présentation

L'IA évolue vite, mais les idées qui font tourner les systèmes d'aujourd'hui sont stables et accessibles. Cet atelier construit l'intuition mathématique et le vocabulaire de modélisation nécessaires pour comprendre ce qui se passe sous le capot des modèles modernes — supervisés, non supervisés, génératifs.

L'objectif n'est pas de faire des participants des spécialistes du deep learning. Il est de leur donner les structures mentales pour évaluer une méthode, dialoguer avec une équipe technique, formuler un problème métier en problème d'apprentissage, et décider quand déployer (ou ne pas déployer) un outil d'IA.

## Public

Ingénieurs, chefs de produit, analystes, responsables d'équipes techniques qui prennent des décisions sur l'IA. Praticiens qui collaborent avec des équipes ML et veulent une compréhension réelle des fondations. Chercheurs d'autres disciplines qui veulent passer du discours sur l'IA à la pratique.

## Prérequis

Familiarité avec les mathématiques de base (lycée + premier cycle universitaire) et un intérêt pour la résolution de problèmes appliqués. Aucun prérequis avancé.

## Objectifs

À la fin de l'atelier, les participants seront capables de :

1. Comprendre les idées centrales d'algèbre linéaire, d'optimisation et de probabilités qui sous-tendent les systèmes d'IA modernes.
2. Décrire la structure, l'entraînement et l'évaluation des modèles ML/IA courants (MLP, autoencodeurs, modèles de diffusion).
3. Formuler un problème réel dans le langage structuré d'un pipeline d'IA.
4. Choisir une architecture, une fonction de perte et un biais inductif adaptés au domaine d'application.
5. Évaluer la fiabilité d'un modèle par le raisonnement statistique, les méthodes de validation et la conscience des modes d'échec classiques.
6. Prendre des décisions techniquement informées sur le déploiement d'outils d'IA.

## Outils

Python 3.10+, NumPy, PyTorch, matplotlib. Notebooks Jupyter exécutables localement ou sur Google Colab.

---

## Programme

### Jour 1 — Algèbre linéaire et modèles paramétriques

**Thème :** Représenter données et modèles avec vecteurs, matrices et transformations.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:30 | **Espaces vectoriels, applications linéaires, dimensions** — Du vecteur de features à l'espace latent. Notion de représentation. |
| 10:45–12:30 | **Du perceptron au MLP** — Couches, activations non-linéaires, pourquoi la composition de fonctions linéaires ne suffit pas. |
| 14:00–15:30 | **Plongements et autoencodeurs** — Apprendre une représentation compacte. Géométrie de l'espace latent. |
| 15:45–17:00 | **TP1 — Visualiser les couches et les cartes de features d'un réseau pré-entraîné.** |

---

### Jour 2 — Calcul différentiel et optimisation

**Thème :** Fonctions de perte et apprentissage par gradient.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:30 | **Dérivées multivariées, règle de la chaîne** — Pourquoi le gradient est la bonne direction. |
| 10:45–12:30 | **Descente de gradient, SGD, Adam** — Taux d'apprentissage, courbes d'apprentissage, hyperparamètres. |
| 14:00–15:30 | **Rétropropagation et programmation différentiable** — Comment PyTorch calcule un gradient sans qu'on lui demande. |
| 15:45–17:00 | **TP2 — Entraîner un réseau de neurones de bout en bout.** |

---

### Jour 3 — Probabilités et modélisation générative

**Thème :** Le hasard comme outil de modélisation ; apprendre et échantillonner depuis des distributions.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:30 | **Distributions, densités, vraisemblance** — Le langage probabiliste de l'apprentissage. |
| 10:45–12:30 | **Modèles génératifs : VAE, modèles de diffusion, méthodes basées sur le score** — Comment générer une image (ou un texte) à partir du bruit. |
| 14:00–15:30 | **Processus de bruit et inversion** — L'intuition derrière la diffusion. |
| 15:45–17:00 | **TP3 — Entraîner un modèle de diffusion simple.** |

---

### Jour 4 — Modélisation pour l'IA

**Thème :** Transformer un problème désordonné en problème mathématique structuré.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:30 | **Optimisation contrainte et non contrainte, régularisation** — Quand ajouter une contrainte change tout. |
| 10:45–12:30 | **Invariance et équivariance** — Pourquoi un CNN est meilleur qu'un MLP pour les images, et la généralisation de cette idée. |
| 14:00–15:30 | **Architectures spécialisées : CNN, GNN, attention** — Le biais inductif comme choix de modélisation. |
| 15:45–17:00 | **TP4 — Comparer plusieurs choix de modèle sur une tâche d'apprentissage sur graphes.** |

---

### Jour 5 — Évaluer les modèles d'IA

**Thème :** Généralisation, fiabilité, prendre des décisions informées.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:30 | **Statistiques de base, biais–variance, sur-apprentissage** — Diagnostiquer une courbe d'apprentissage. |
| 10:45–12:30 | **Validation, calibration, incertitude** — Au-delà de la précision moyenne. |
| 14:00–15:30 | **Exemples adversariaux, données hors distribution** — Pourquoi un modèle qui marche en lab échoue en production. |
| 15:45–17:00 | **TP5 — Comparer des modèles sous décalage de distribution. Bilan.** |

---

## Évaluation

- **TPs quotidiens** (60 %) — Implémentations fonctionnelles et analyse.
- **Mini-projet final** (30 %) — Formuler un problème métier en pipeline d'IA et défendre les choix.
- **Participation** (10 %) — Engagement, questions, discussions.

## Ressources

- Goodfellow, Bengio, Courville — *Deep Learning* (MIT Press, accès libre)
- Bishop & Bishop — *Deep Learning: Foundations and Concepts* (Springer, 2024)
- Murphy — *Probabilistic Machine Learning* (MIT Press, accès libre)
- Strang — *Linear Algebra and Learning from Data*
- Ho et al. — *Denoising Diffusion Probabilistic Models* (NeurIPS 2020, [arXiv:2006.11239](https://arxiv.org/abs/2006.11239))

## Certificat

Les participants ayant complété tous les TPs et le mini-projet reçoivent un certificat de complétion.
