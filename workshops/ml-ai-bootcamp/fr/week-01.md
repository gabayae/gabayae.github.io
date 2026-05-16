---
layout: page
permalink: /workshops/ml-ai-bootcamp/fr/week-01/
title: "Semaine 01 — Python pour les données"
description: "Module 1 du Bootcamp ML & IA AIRINA Labs. Python idiomatique, NumPy, Pandas, projets reproductibles, discipline Jupyter."
lang: fr
nav: false
---

**Module 1 sur 10.** &nbsp; [← calendrier]({{ '/workshops/ml-ai-bootcamp/fr/schedule/' | relative_url }}) &nbsp;|&nbsp; [semaine suivante →]({{ '/workshops/ml-ai-bootcamp/fr/schedule/' | relative_url }})

> Prenez le Python que vous connaissez à moitié et rendez-le assez précis pour être déployé.

Cette première semaine est en partie un calibrage et en partie une remise à zéro brutale sur l'outillage. Presque tous les participants arrivent avec *un peu* de Python --- quelques notebooks Coursera, deux ou trois tentatives Kaggle, un script de projet de recherche. Presque tous arrivent aussi avec au moins une mauvaise habitude qui les bloquera en semaine 5 si on ne la corrige pas maintenant. Les TP de la semaine sont conçus pour exposer ces habitudes : notebooks brouillons, état caché, fonctions non typées, tests manquants, environnements cassés.

Le vendredi, chaque participant livre un projet Python propre et reproductible, publié sur son GitHub personnel. Cet artefact devient la fondation sur laquelle s'appuieront tous les modules suivants.

---

## Ce que vous livrez cette semaine

| | |
|---|---|
| **Livrable** | Un dépôt GitHub public contenant la version nettoyée du TP 1 (le refactoring de 300 lignes) avec un `README.md`, un `pyproject.toml`, une suite `pytest` qui passe, et un CI vert sur un push. |
| **Échéance** | Vendredi fin de semaine 1, 18h00 Afrique/Lagos. |
| **Soumission** | Déposez l'URL du dépôt dans le canal `#cohort-week-01`. La répartition en binômes pour la revue par les pairs est annoncée le lundi de la semaine 2. |
| **Barème** | Livrable validé ou à reprendre. La validation exige un CI vert, des tests couvrant l'API publique, et un README qu'un inconnu peut suivre pour installer et lancer le code. |

---

## Sessions en direct

| Jour | Heure | Sujet | Lien | Enreg. |
|---|---|---|:---:|:---:|
| Lundi | 17h00 | **Kickoff et présentations de cohorte** | _(rempli à l'inscription)_ | _(à venir)_ |
| Mardi | 17h00 | **Python idiomatique : compréhensions, générateurs, décorateurs** | _(à venir)_ | _(à venir)_ |
| Mercredi | 17h00 | **NumPy et vectorisation, avec exemples sur des données réelles** | _(à venir)_ | _(à venir)_ |
| Jeudi | 17h00 | **Pandas en profondeur : jointures, group-by, reshape, l'index** | _(à venir)_ | _(à venir)_ |
| Vendredi | 17h00 | **Projets reproductibles : virtualenv, pyproject, lockfile, pre-commit** | _(à venir)_ | _(à venir)_ |

Temps total en direct cette semaine : environ 7h30 (cinq sessions de 90 minutes). Les permanences ajoutent 90 minutes le mercredi.

---

## Objectifs d'apprentissage

À la fin de la semaine, chaque participant saura :

1. **Écrire du Python idiomatique.** Utiliser compréhensions, générateurs, gestionnaires de contexte, décorateurs là où ils paient et pas là où ils ne paient pas. Reconnaître et refactoriser les motifs non idiomatiques.
2. **Utiliser NumPy et Pandas couramment pour le travail vectorisé sur données.** Sans retomber dans des boucles Python sur des tableaux de plus de quelques centaines d'éléments.
3. **Construire un projet Python reproductible.** Environnement virtuel, dépendances figées, `pyproject.toml`, hooks pre-commit, suite `pytest` opérationnelle, pipeline CI qui s'exécute à chaque push.
4. **Lire et écrire des notebooks Jupyter sans perdre la reproductibilité.** Hygiène d'état caché, gestion des sorties, conversion vers scripts, versionnage des notebooks.

---

## Lectures et préparation

**Avant mardi.** [Hitchhiker's Guide to Python](https://docs.python-guide.org/) chapitres sur \og Writing great Python code \fg{} (idiomes, structuration des projets, vendorisation). En lecture rapide --- on parcourra le même contenu en session.

**Avant mercredi.** Wes McKinney, *Python for Data Analysis* (3\\textsuperscript{e} éd., O'Reilly 2022), chapitres 4 (bases NumPy) et 5 (bases Pandas). Disponible en accès libre sur [wesmckinney.com/book](https://wesmckinney.com/book/).

**Avant jeudi.** Même livre, chapitres 8 et 10 (manipulation de données, mécanique de group-by).

**Approfondissement optionnel.** Luciano Ramalho, *Fluent Python* (2\\textsuperscript{e} éd., O'Reilly 2022) pour tout participant qui connaît déjà bien Pandas et veut l'approfondissement au niveau du langage. Surtout les chapitres 17 (bases de concurrence), 18 (with/async), 24 (métaprogrammation de classes).

---

## Notebooks de TP

### TP 1 — Le refactoring de 300 lignes

Un script Python délibérément moche (`messy_data_pipeline.py`) est fourni. Il charge trois fichiers CSV, les joint, calcule quelques métriques, écrit les sorties sur disque. Le script fonctionne. Il est aussi illisible, sans tests, plein d'état caché, et il contient deux bugs qui ne se déclenchent pas sur les données d'exemple.

**Votre tâche.** Le refactoriser en un package Python propre avec :

- une structure de module `src/<votre_projet>/`
- une fonction pure par responsabilité, typée avec `mypy --strict`
- une suite `pytest` qui détecte les deux bugs latents
- un `pyproject.toml` qui fige toutes les dépendances
- un `README.md` avec instructions d'installation et d'exécution qu'un inconnu peut suivre
- un workflow GitHub Actions vert (Python 3.11, lint + type-check + tests)

**Jeu de données.** Le jeu de données du TP est l'export public du [registre kényan des formations sanitaires](https://kmhfr.health.go.ke/) de décembre 2024 (~12\\,000 formations). Le notebook du dépôt de TP contient le lien de téléchargement.

**Notebook.** [`week-01-lab-01-refactor.ipynb`](https://github.com/AI-Technipreneurs) (lien finalisé à l'inscription).

### TP 2 — Manipulation Pandas sur données réelles

À partir des données brutes des [formations sanitaires kényanes](https://kmhfr.health.go.ke/), produire un DataFrame analytique propre répondant à trois questions concrètes : (1) quelle fraction des formations par comté est publique vs privée ? (2) où sont les zones sous-desservies (population par formation) ? et (3) le tableau change-t-il si l'on pondère par capacité plutôt que par effectif ? Livrer un notebook et un court compte rendu.

**Notebook.** [`week-01-lab-02-pandas.ipynb`](https://github.com/AI-Technipreneurs).

### TP 3 — Publier votre projet

Reprenez le package refactorisé du TP 1 et publiez-le dans un dépôt GitHub public sous votre propre compte, avec un tag de release, un `pyproject.toml` versionné, et un badge CI dans le README. Ajoutez-le à votre profil bootcamp.

C'est l'artefact que vous référencerez chaque semaine suivante --- et celui que les recruteurs regarderont en premier.

---

## Permanences

| Quand | Assistant | Sujet |
|---|---|---|
| Mercredi 19h00 (Afrique/Lagos) | _(annoncé à l'inscription)_ | Ouvert : amenez votre refactoring, vos problèmes d'environnement, tout blocage. |

Les questions asynchrones vont dans le canal `#cohort-week-01-questions` ; temps de réponse attendu sous 24 heures en semaine.

---

## S'appuie sur / fait le lien avec

Cette semaine puise dans deux volumes existants du catalogue de cours :

- [Programmation Scientifique]({{ '/courses/programmation-scientifiques/' | relative_url }}) --- la perspective Python comme langage scientifique.
- [Introduction à la Data Science]({{ '/courses/intro-data-science/' | relative_url }}) --- chapitres 1 et 2 des notes bilingues.

Le bootcamp condense les chapitres pertinents dans la liste de lectures de la semaine plutôt que de re-dériver le contenu.
