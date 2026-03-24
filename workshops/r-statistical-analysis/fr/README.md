# R pour l'Analyse Statistique — Atelier de 4 jours

**Formateur :** Dr. Yaé Ulrich Gaba
**Durée :** 4 jours (24 heures)
**Niveau :** Débutant à Intermédiaire
**Langue :** Français

---

## Présentation

Cet atelier propose une introduction complète à R pour l'analyse de données et la modélisation statistique. Les participants apprennent l'écosystème Tidyverse, créent des visualisations de qualité publication avec ggplot2 et produisent des rapports reproductibles avec R Markdown. L'atelier sert de compagnon pratique à *The Shape of Data* (No Starch Press).

## Prérequis

- Statistiques de base (moyenne, variance, concepts de tests d'hypothèses)
- Aucune expérience préalable en R requise
- Ordinateur portable avec accès internet

## Objectifs Pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Naviguer dans RStudio et écrire du code R propre et lisible
2. Manipuler les données efficacement avec dplyr et tidyr
3. Créer des visualisations statistiques convaincantes avec ggplot2
4. Effectuer des analyses statistiques courantes (tests t, ANOVA, régression)
5. Produire des rapports reproductibles avec R Markdown

## Logiciels Requis

- R 4.3+ ([CRAN](https://cran.r-project.org/))
- RStudio Desktop ([posit.co](https://posit.co/download/rstudio-desktop/))
- Packages : tidyverse, rmarkdown, knitr, broom, palmerpenguins

---

## Programme Jour par Jour

### Jour 1 : Fondamentaux de R & RStudio

**Objectifs :** Configurer l'environnement, apprendre la syntaxe R, comprendre les types et structures de données.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:30 | **Installation & Visite de RStudio** — Installer R & RStudio, console, scripts, projets, panneau environnement, système d'aide |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Bases de R** — Variables, vecteurs, types (numeric, character, logical, factor), indexation, opérations vectorisées |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Structures de Données** — Matrices, listes, data frames, tibbles. Création, sous-ensembles, modification |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Flux de Contrôle & Fonctions** — if/else, boucles for, famille apply, écriture de fonctions personnalisées, pipes (`|>` et `%>%`) |

**TP 1 :** Charger le jeu de données `iris`, calculer les statistiques descriptives par espèce, et écrire une fonction qui classifie une fleur selon les mesures des pétales.

**Devoir :** Explorer le jeu de données `mtcars` — calculer des statistiques groupées et répondre à 3 questions sur les données.

---

### Jour 2 : Manipulation de Données avec le Tidyverse

**Objectifs :** Maîtriser la manipulation de données avec dplyr et tidyr.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Lecture de Données** — read_csv, read_excel, read_delim, options readr, gestion des encodages et fichiers désordonnés |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Verbes dplyr** — filter(), select(), mutate(), arrange(), summarise(), group_by(), across() |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **tidyr & Remodelage** — pivot_longer(), pivot_wider(), separate(), unite(), gestion des NA (drop_na, replace_na) |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Jointures & Combinaisons** — left_join, inner_join, anti_join, bind_rows, bind_cols. Données relationnelles |

**TP 2 :** Travailler avec un jeu de données multi-fichiers (ex. : statistiques de santé OMS pour les pays africains) : lire plusieurs CSV, les joindre, remodeler de large à long, nettoyer les valeurs manquantes, produire un jeu de données propre prêt pour l'analyse.

**Devoir :** À partir du jeu de données nettoyé, produire 5 tableaux récapitulatifs avec des pipelines dplyr.

---

### Jour 3 : Visualisation avec ggplot2

**Objectifs :** Construire une boîte à outils de visualisation complète avec la grammaire des graphiques.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Grammaire des Graphiques** — Esthétiques, géométries, échelles, systèmes de coordonnées, approche par couches |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Géométries Principales** — geom_point, geom_line, geom_bar, geom_histogram, geom_boxplot, geom_violin, geom_density |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Personnalisation** — Thèmes (theme_minimal, theme_classic, thèmes personnalisés), palettes de couleurs (viridis, brewer), étiquettes, annotations, légendes |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Techniques Avancées** — Facettes (facet_wrap, facet_grid), couches statistiques, transformations de coordonnées, combinaison de graphiques (patchwork), sauvegarde avec ggsave |

**TP 3 :** Créer un rapport visuel avec 6+ figures de qualité publication explorant le jeu de données de santé. Inclure : graphiques de distribution, lignes de tendance, comparaisons en facettes et carte de chaleur de corrélation.

**Devoir :** Reproduire une figure d'un article publié (fourni) en utilisant ggplot2.

---

### Jour 4 : Modélisation Statistique & Rapports Reproductibles

**Objectifs :** Effectuer des analyses statistiques courantes et produire des rapports reproductibles.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Statistiques Descriptives & Inférentielles** — Statistiques résumées, tests t, tests du chi-deux, intervalles de confiance, p-values et leur interprétation |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Modèles Linéaires** — lm(), interprétation des coefficients, R², diagnostics des résidus, régression multiple, ANOVA avec aov() |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:00 | **Diagnostics & Au-delà** — Graphiques des résidus, Q-Q plots, mesures d'influence, régression logistique avec glm(), broom pour la sortie propre des modèles |
| 15:00–15:15 | *Pause* |
| 15:15–16:15 | **R Markdown** — En-tête YAML, blocs de code, code en ligne, tableaux (kable), options de figures, formats de sortie (HTML, PDF, Word) |
| 16:15–17:00 | **Projet Final & Bilan** — Présentations des mini-projets, ressources, questions, certificats |

**TP 4 (Projet Final) :** Produire un rapport R Markdown reproductible complet : charger les données, effectuer une EDA avec ggplot2, ajuster un modèle linéaire, le diagnostiquer et présenter les résultats avec narration, tableaux et figures. Sujets :
- Modélisation de résultats de santé (espérance de vie ~ PIB, éducation, etc.)
- Analyse de rendements agricoles
- Analyse d'indicateurs financiers

---

## Évaluation

- **TPs quotidiens** (50 %) — Complétion et qualité des exercices
- **Rapport final** (30 %) — Document R Markdown produit le Jour 4
- **Participation** (20 %) — Engagement et devoirs

## Ressources

- [R for Data Science (2e)](https://r4ds.hadley.nz/) — Hadley Wickham & Garrett Grolemund
- [ggplot2 Book](https://ggplot2-book.org/)
- [The Shape of Data](https://nostarch.com/shapeofdata) — Livre compagnon avec implémentations R
- [Aide-mémoires RStudio](https://posit.co/resources/cheatsheets/)
- [CRAN Task Views](https://cran.r-project.org/web/views/)

## Certificat

Les participants ayant complété tous les TPs et le rapport final reçoivent un certificat de complétion.
