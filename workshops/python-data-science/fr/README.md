---
layout: workshop
permalink: /workshops/python-data-science/fr/
lang: fr
title: "Python pour la Science des Données"
tagline: "De zéro en Python à vos premiers modèles de machine learning — ateliers de code quotidiens sur des jeux de données réels."
description: "Atelier de 5 jours : Pandas, visualisation, ML avec scikit-learn."

# --- Métadonnées de la barre latérale ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "5 jours (≈ 30 heures)"
level: "Débutant à Intermédiaire"
format: "Sur site, en ligne en direct, ou hybride"
languages: "Français &amp; anglais"
certificate: "Certificat de complétion"

# --- Liens des supports ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/python-data-science

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Demande d'atelier — Python pour la Science des Données"
---

## Présentation du programme

Cet atelier pratique accompagne les participants de zéro expérience en Python à la construction de leurs premiers modèles de machine learning. À travers des ateliers de code quotidiens, des jeux de données réels et des projets progressifs, les apprenants développent des compétences pratiques en science des données fondées sur de solides bases en programmation.

### Logiciels requis

- Python 3.10+
- Jupyter Notebook / JupyterLab
- Bibliothèques : NumPy, Pandas, Matplotlib, Seaborn, scikit-learn
- Installation recommandée : [Anaconda Distribution](https://www.anaconda.com/download) (tout inclus).

### Jour 1 — Fondamentaux de Python

**Objectifs :** installer Python, comprendre la syntaxe de base, écrire ses premiers programmes.

- **Installation & premiers pas** — installer Anaconda, lancer Jupyter, cellules & exécution, bases du Markdown.
- **Syntaxe de base** — variables, types (int, float, str, bool), opérateurs, formatage de chaînes, entrées/sorties.
- **Flux de contrôle** — conditions (if/elif/else), boucles (for, while), range(), compréhensions de listes.
- **Fonctions & modules** — définir des fonctions, paramètres, valeurs de retour, importer des modules, `math`, `random`.

**TP 1 :** écrire un programme qui analyse des notes d'étudiants — calculer la moyenne, la médiane, le min/max et attribuer des mentions.

### Jour 2 — Structures de données & NumPy

**Objectifs :** maîtriser les collections Python et le calcul numérique avec NumPy.

- **Structures de données** — listes, tuples, dictionnaires, ensembles, imbrication, méthodes courantes.
- **Fichiers & gestion d'erreurs** — lecture/écriture de fichiers CSV et texte, try/except, instructions with.
- **Fondamentaux de NumPy** — tableaux, formes, dtypes, indexation, slicing, broadcasting.
- **Opérations NumPy** — opérations vectorisées, agrégations, algèbre linéaire de base, génération de nombres aléatoires.

**TP 2 :** charger un fichier CSV de données météo manuellement, puis refaire avec NumPy. Comparer la performance et la lisibilité du code.

### Jour 3 — Pandas & manipulation de données

**Objectifs :** charger, nettoyer, transformer et explorer des jeux de données avec Pandas.

- **Bases de Pandas** — Series, DataFrame, read_csv, head/tail/info/describe, dtypes.
- **Sélection & filtrage** — loc/iloc, indexation booléenne, query(), opérations sur colonnes, tri.
- **Nettoyage de données** — valeurs manquantes (isna, fillna, dropna), doublons, conversion de types, méthodes de chaînes.
- **Agrégation & regroupement** — groupby, agg, pivot_table, merge/join, concat.

**TP 3 :** nettoyer et analyser un jeu de données réel (ex. : indicateurs de développement de la Banque Mondiale pour les pays africains). Gérer les valeurs manquantes, fusionner plusieurs fichiers et produire des statistiques par pays/année.

### Jour 4 — Visualisation de données

**Objectifs :** créer des graphiques de qualité publication et effectuer une analyse exploratoire des données.

- **Fondamentaux de Matplotlib** — modèle figure/axes, plot(), scatter(), bar(), hist(), personnalisation.
- **Seaborn pour la visualisation statistique** — distplot, boxplot, heatmap, pairplot, catplot, styles.
- **Analyse exploratoire des données (EDA)** — approche systématique : distributions, corrélations, valeurs aberrantes, tendances. Checklist EDA.
- **Graphiques avancés & storytelling** — sous-graphiques, annotations, palettes de couleurs, sauvegarde de figures, mises en page type tableau de bord.

**TP 4 :** effectuer une EDA complète sur le jeu de données nettoyé du Jour 3. Répondre à 5 questions analytiques avec des visualisations appropriées. Créer un mini-rapport avec narration et figures.

### Jour 5 — Introduction au machine learning

**Objectifs :** construire, évaluer et interpréter ses premiers modèles ML avec scikit-learn.

- **Concepts ML** — apprentissage supervisé vs. non supervisé, train/test split, surapprentissage, compromis biais-variance.
- **Classification** — régression logistique, arbres de décision, forêts aléatoires. API scikit-learn : fit/predict/score.
- **Régression & évaluation** — régression linéaire, métriques (MSE, R², accuracy, precision, recall, F1), validation croisée.
- **Apprentissage non supervisé** — K-Means, PCA pour la réduction de dimension, visualisation des clusters.
- **Bilan & perspectives** — récapitulatif, ressources pour la suite, questions, certificats.

**TP 5 (projet final) :** mini-projet de bout en bout : charger un jeu de données, le nettoyer, l'explorer, construire un modèle prédictif, l'évaluer et présenter les résultats. Les participants choisissent parmi :
- Prédiction de rendements agricoles à partir de données climatiques.
- Classification du désabonnement client.
- Régression sur les prix immobiliers.

### Évaluation

- **TPs quotidiens** (50 %) — complétion et qualité des exercices pratiques.
- **Projet final** (30 %) — analyse de bout en bout le Jour 5.
- **Participation** (20 %) — engagement dans les discussions et devoirs.

### Ressources

- [Documentation Python](https://docs.python.org/fr/3/)
- [Documentation Pandas](https://pandas.pydata.org/docs/)
- [Guide scikit-learn](https://scikit-learn.org/stable/user_guide.html)
- [Jeux de données Kaggle](https://www.kaggle.com/datasets)
- [The Shape of Data](https://nostarch.com/shapeofdata) — ML géométrique et analyse de données.

## Objectifs pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Écrire des scripts Python et utiliser des notebooks Jupyter pour l'analyse de données.
2. Manipuler et nettoyer des jeux de données avec Pandas.
3. Créer des visualisations informatives avec Matplotlib et Seaborn.
4. Effectuer une analyse exploratoire des données (EDA) sur des jeux de données réels.
5. Construire, évaluer et interpréter des modèles ML de base avec scikit-learn.

## Public visé

Chercheurs, analystes et étudiants de master/doctorat de toutes disciplines qui manipulent des données et veulent une boîte à outils opérationnelle en science des données. Personnes en reconversion vers un premier poste d'analyste ou de data scientist. Spécialistes d'un domaine (économie, biologie, santé publique, éducation) qui veulent lire et écrire leur propre code d'analyse plutôt que dépendre des autres. Le rythme suppose aucune expérience préalable en programmation, donc un débutant complet peut suivre, tandis qu'un utilisateur Excel compétent accélère rapidement.

**Prérequis :**

- Compétences informatiques de base (gestion de fichiers, navigation web).
- Mathématiques de niveau lycée (algèbre, statistiques de base).
- Aucune expérience préalable en programmation requise.
- Ordinateur portable avec accès internet (Python sera installé le Jour 1).

## Plaquette

Les notes de cours et notebooks sont accessibles depuis la barre latérale.

Pour une plaquette d'une page, à transmettre à un comité de programme, un organisateur de conférence ou une équipe formation interne, écrivez à <a href="mailto:gabayae2@gmail.com?subject=Demande%20de%20plaquette%20%E2%80%94%20Python%20pour%20la%20Science%20des%20Donn%C3%A9es">gabayae2@gmail.com</a> en précisant la taille de l'audience et les dates envisagées.
