---
layout: workshop
permalink: /workshops/r-statistical-analysis/fr/
lang: fr
title: "R pour l'Analyse Statistique"
tagline: "Tidyverse, ggplot2, modélisation statistique et rapports reproductibles — un compagnon pratique de The Shape of Data."
description: "Atelier de 4 jours : Tidyverse, ggplot2, modélisation statistique, R Markdown."

# --- Métadonnées de la barre latérale ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "4 jours (≈ 24 heures)"
level: "Débutant à Intermédiaire"
format: "Sur site, en ligne en direct, ou hybride"
languages: "Français &amp; anglais"
certificate: "Certificat de complétion"

# --- Liens des supports ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/r-statistical-analysis

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Demande d'atelier — R pour l'Analyse Statistique"
---

## Présentation du programme

Cet atelier propose une introduction complète à R pour l'analyse de données et la modélisation statistique. Les participants apprennent l'écosystème Tidyverse, créent des visualisations de qualité publication avec ggplot2 et produisent des rapports reproductibles avec R Markdown. L'atelier sert de compagnon pratique à *The Shape of Data* (No Starch Press).

### Logiciels requis

- R 4.3+ ([CRAN](https://cran.r-project.org/))
- RStudio Desktop ([posit.co](https://posit.co/download/rstudio-desktop/))
- Packages : tidyverse, rmarkdown, knitr, broom, palmerpenguins

### Jour 1 — Fondamentaux de R & RStudio

**Objectifs :** configurer l'environnement, apprendre la syntaxe R, comprendre les types et structures de données.

- **Installation & visite de RStudio** — installer R & RStudio, console, scripts, projets, panneau environnement, système d'aide.
- **Bases de R** — variables, vecteurs, types (numeric, character, logical, factor), indexation, opérations vectorisées.
- **Structures de données** — matrices, listes, data frames, tibbles. Création, sous-ensembles, modification.
- **Flux de contrôle & fonctions** — if/else, boucles for, famille apply, écriture de fonctions personnalisées, pipes (`|>` et `%>%`).

**TP 1 :** charger le jeu de données `iris`, calculer les statistiques descriptives par espèce, et écrire une fonction qui classifie une fleur selon les mesures des pétales.

### Jour 2 — Manipulation de données avec le Tidyverse

**Objectifs :** maîtriser la manipulation de données avec dplyr et tidyr.

- **Lecture de données** — read_csv, read_excel, read_delim, options readr, gestion des encodages et fichiers désordonnés.
- **Verbes dplyr** — filter(), select(), mutate(), arrange(), summarise(), group_by(), across().
- **tidyr & remodelage** — pivot_longer(), pivot_wider(), separate(), unite(), gestion des NA (drop_na, replace_na).
- **Jointures & combinaisons** — left_join, inner_join, anti_join, bind_rows, bind_cols. Données relationnelles.

**TP 2 :** travailler avec un jeu de données multi-fichiers (ex. : statistiques de santé OMS pour les pays africains) : lire plusieurs CSV, les joindre, remodeler de large à long, nettoyer les valeurs manquantes, produire un jeu de données propre prêt pour l'analyse.

### Jour 3 — Visualisation avec ggplot2

**Objectifs :** construire une boîte à outils de visualisation complète avec la grammaire des graphiques.

- **Grammaire des graphiques** — esthétiques, géométries, échelles, systèmes de coordonnées, approche par couches.
- **Géométries principales** — geom_point, geom_line, geom_bar, geom_histogram, geom_boxplot, geom_violin, geom_density.
- **Personnalisation** — thèmes (theme_minimal, theme_classic, thèmes personnalisés), palettes de couleurs (viridis, brewer), étiquettes, annotations, légendes.
- **Techniques avancées** — facettes (facet_wrap, facet_grid), couches statistiques, transformations de coordonnées, combinaison de graphiques (patchwork), sauvegarde avec ggsave.

**TP 3 :** créer un rapport visuel avec 6+ figures de qualité publication explorant le jeu de données de santé. Inclure : graphiques de distribution, lignes de tendance, comparaisons en facettes et carte de chaleur de corrélation.

### Jour 4 — Modélisation statistique & rapports reproductibles

**Objectifs :** effectuer des analyses statistiques courantes et produire des rapports reproductibles.

- **Statistiques descriptives & inférentielles** — statistiques résumées, tests t, tests du chi-deux, intervalles de confiance, p-values et leur interprétation.
- **Modèles linéaires** — lm(), interprétation des coefficients, R², diagnostics des résidus, régression multiple, ANOVA avec aov().
- **Diagnostics & au-delà** — graphiques des résidus, Q-Q plots, mesures d'influence, régression logistique avec glm(), broom pour la sortie propre des modèles.
- **R Markdown** — en-tête YAML, blocs de code, code en ligne, tableaux (kable), options de figures, formats de sortie (HTML, PDF, Word).
- **Projet final & bilan** — présentations des mini-projets, ressources, questions, certificats.

**TP 4 (projet final) :** produire un rapport R Markdown reproductible complet : charger les données, effectuer une EDA avec ggplot2, ajuster un modèle linéaire, le diagnostiquer et présenter les résultats avec narration, tableaux et figures. Sujets :
- Modélisation de résultats de santé (espérance de vie ~ PIB, éducation, etc.).
- Analyse de rendements agricoles.
- Analyse d'indicateurs financiers.

### Évaluation

- **TPs quotidiens** (50 %) — complétion et qualité des exercices.
- **Rapport final** (30 %) — document R Markdown produit le Jour 4.
- **Participation** (20 %) — engagement et devoirs.

### Ressources

- [R for Data Science (2e)](https://r4ds.hadley.nz/) — Hadley Wickham & Garrett Grolemund
- [ggplot2 Book](https://ggplot2-book.org/)
- [The Shape of Data](https://nostarch.com/shapeofdata) — livre compagnon avec implémentations R
- [Aide-mémoires RStudio](https://posit.co/resources/cheatsheets/)
- [CRAN Task Views](https://cran.r-project.org/web/views/)

## Objectifs pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Naviguer dans RStudio et écrire du code R propre et lisible.
2. Manipuler les données efficacement avec dplyr et tidyr.
3. Créer des visualisations statistiques convaincantes avec ggplot2.
4. Effectuer des analyses statistiques courantes (tests t, ANOVA, régression).
5. Produire des rapports reproductibles avec R Markdown.

## Public visé

Étudiants de master/doctorat, chercheurs et analystes en sciences sociales, santé publique, économie, biologie, agriculture, ou tout domaine dont le travail implique de l'analyse statistique sur des données réelles et où la reproductibilité compte. L'atelier convient aussi aux universitaires qui utilisent SAS, SPSS ou Stata et veulent migrer vers un workflow open-source sans perdre en rigueur.

**Prérequis :**

- Statistiques de base (moyenne, variance, concepts de tests d'hypothèses).
- Aucune expérience préalable en R requise.
- Ordinateur portable avec accès internet.

## Plaquette

Les notes de cours et notebooks sont accessibles depuis la barre latérale.

Pour une plaquette d'une page, à transmettre à un comité de programme, un organisateur de conférence ou une équipe formation interne, écrivez à <a href="mailto:gabayae2@gmail.com?subject=Demande%20de%20plaquette%20%E2%80%94%20R%20pour%20l%27Analyse%20Statistique">gabayae2@gmail.com</a> en précisant la taille de l'audience et les dates envisagées.
