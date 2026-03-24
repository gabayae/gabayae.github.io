# Python pour la Science des Données — Atelier de 5 jours

**Formateur :** Dr. Yaé Ulrich Gaba
**Durée :** 5 jours (30 heures)
**Niveau :** Débutant à Intermédiaire
**Langue :** Français

---

## Présentation

Cet atelier pratique accompagne les participants de zéro expérience en Python à la construction de leurs premiers modèles de machine learning. À travers des ateliers de code quotidiens, des jeux de données réels et des projets progressifs, les apprenants développent des compétences pratiques en science des données fondées sur de solides bases en programmation.

## Prérequis

- Compétences informatiques de base (gestion de fichiers, navigation web)
- Mathématiques de niveau lycée (algèbre, statistiques de base)
- Aucune expérience préalable en programmation requise
- Ordinateur portable avec accès internet (Python sera installé le Jour 1)

## Objectifs Pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Écrire des scripts Python et utiliser des notebooks Jupyter pour l'analyse de données
2. Manipuler et nettoyer des jeux de données avec Pandas
3. Créer des visualisations informatives avec Matplotlib et Seaborn
4. Effectuer une analyse exploratoire des données (EDA) sur des jeux de données réels
5. Construire, évaluer et interpréter des modèles ML de base avec scikit-learn

## Logiciels Requis

- Python 3.10+
- Jupyter Notebook / JupyterLab
- Bibliothèques : NumPy, Pandas, Matplotlib, Seaborn, scikit-learn

**Installation recommandée :** [Anaconda Distribution](https://www.anaconda.com/download) (tout inclus)

---

## Programme Jour par Jour

### Jour 1 : Fondamentaux de Python

**Objectifs :** Installer Python, comprendre la syntaxe de base, écrire ses premiers programmes.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:30 | **Installation & Premiers Pas** — Installer Anaconda, lancer Jupyter, cellules & exécution, bases du Markdown |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Syntaxe de Base** — Variables, types (int, float, str, bool), opérateurs, formatage de chaînes, entrées/sorties |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Flux de Contrôle** — Conditions (if/elif/else), boucles (for, while), range(), compréhensions de listes |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Fonctions & Modules** — Définir des fonctions, paramètres, valeurs de retour, importer des modules, `math`, `random` |

**TP 1 :** Écrire un programme qui analyse des notes d'étudiants — calculer la moyenne, la médiane, le min/max et attribuer des mentions.

**Devoir :** Créer un jeu de devinette de nombres utilisant les boucles et conditions.

---

### Jour 2 : Structures de Données & NumPy

**Objectifs :** Maîtriser les collections Python et le calcul numérique avec NumPy.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** — Discussion et questions |
| 09:30–10:30 | **Structures de Données** — Listes, tuples, dictionnaires, ensembles, imbrication, méthodes courantes |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Fichiers & Gestion d'Erreurs** — Lecture/écriture de fichiers CSV et texte, try/except, instructions with |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Fondamentaux de NumPy** — Tableaux, formes, dtypes, indexation, slicing, broadcasting |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Opérations NumPy** — Opérations vectorisées, agrégations, algèbre linéaire de base, génération de nombres aléatoires |

**TP 2 :** Charger un fichier CSV de données météo manuellement, puis refaire avec NumPy. Comparer la performance et la lisibilité du code.

**Devoir :** Utiliser NumPy pour simuler 10 000 lancers de dés et tracer la distribution des sommes.

---

### Jour 3 : Pandas — Manipulation de Données

**Objectifs :** Charger, nettoyer, transformer et explorer des jeux de données avec Pandas.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Bases de Pandas** — Series, DataFrame, read_csv, head/tail/info/describe, dtypes |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Sélection & Filtrage** — loc/iloc, indexation booléenne, query(), opérations sur colonnes, tri |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Nettoyage de Données** — Valeurs manquantes (isna, fillna, dropna), doublons, conversion de types, méthodes de chaînes |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Agrégation & Regroupement** — groupby, agg, pivot_table, merge/join, concat |

**TP 3 :** Nettoyer et analyser un jeu de données réel (ex. : indicateurs de développement de la Banque Mondiale pour les pays africains). Gérer les valeurs manquantes, fusionner plusieurs fichiers et produire des statistiques par pays/année.

**Devoir :** Préparer un jeu de données nettoyé et formuler 5 questions analytiques à répondre par la visualisation.

---

### Jour 4 : Visualisation de Données

**Objectifs :** Créer des graphiques de qualité publication et effectuer une analyse exploratoire des données.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Fondamentaux de Matplotlib** — modèle figure/axes, plot(), scatter(), bar(), hist(), personnalisation |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Seaborn pour la Visualisation Statistique** — distplot, boxplot, heatmap, pairplot, catplot, styles |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Analyse Exploratoire des Données (EDA)** — Approche systématique : distributions, corrélations, valeurs aberrantes, tendances. Checklist EDA |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Graphiques Avancés & Storytelling** — Sous-graphiques, annotations, palettes de couleurs, sauvegarde de figures, mises en page type tableau de bord |

**TP 4 :** Effectuer une EDA complète sur le jeu de données nettoyé du Jour 3. Répondre aux 5 questions avec des visualisations appropriées. Créer un mini-rapport avec narration et figures.

**Devoir :** Trouver un jeu de données pertinent pour votre travail/intérêts et le préparer pour la session ML du Jour 5.

---

### Jour 5 : Introduction au Machine Learning

**Objectifs :** Construire, évaluer et interpréter ses premiers modèles ML avec scikit-learn.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Présentations des devoirs** — Partage des résultats EDA |
| 09:30–10:30 | **Concepts ML** — Apprentissage supervisé vs. non supervisé, train/test split, surapprentissage, compromis biais-variance |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Classification** — Régression logistique, arbres de décision, forêts aléatoires. API scikit-learn : fit/predict/score |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Régression & Évaluation** — Régression linéaire, métriques (MSE, R², accuracy, precision, recall, F1), validation croisée |
| 15:30–15:45 | *Pause* |
| 15:45–16:30 | **Apprentissage Non Supervisé** — K-Means, PCA pour la réduction de dimension, visualisation des clusters |
| 16:30–17:00 | **Bilan & Perspectives** — Récapitulatif, ressources pour la suite, questions, certificats |

**TP 5 (Projet Final) :** Mini-projet de bout en bout : charger un jeu de données, le nettoyer, l'explorer, construire un modèle prédictif, l'évaluer et présenter les résultats. Les participants choisissent parmi :
- Prédiction de rendements agricoles à partir de données climatiques
- Classification du désabonnement client
- Régression sur les prix immobiliers

---

## Évaluation

- **TPs quotidiens** (50 %) — Complétion et qualité des exercices pratiques
- **Projet final** (30 %) — Analyse de bout en bout le Jour 5
- **Participation** (20 %) — Engagement dans les discussions et devoirs

## Ressources

- [Documentation Python](https://docs.python.org/fr/3/)
- [Documentation Pandas](https://pandas.pydata.org/docs/)
- [Guide scikit-learn](https://scikit-learn.org/stable/user_guide.html)
- [Jeux de données Kaggle](https://www.kaggle.com/datasets)
- [The Shape of Data](https://nostarch.com/shapeofdata) — ML géométrique et analyse de données

## Certificat

Les participants ayant complété tous les TPs et le projet final reçoivent un certificat de complétion délivré par le formateur.
