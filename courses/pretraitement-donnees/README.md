# Prétraitement des données avec Python / Data pre-processing with Python

Cours pratique de 30 heures destiné aux analystes de données, data scientists et étudiants de master qui doivent nettoyer, transformer et préparer des données réelles pour l'analyse et le machine learning.

A 30-hour practical course designed for data analysts, data scientists, and graduate students who need to clean, transform, and prepare real-world data for analysis and machine learning.

## Structure

| Chapitre / Chapter | Sujet / Topic | Heures / Hours | Jeux de données clés |
|---|---|---|---|
| 1 | Paysage et pipelines de données | 3h | Melbourne Housing, Gapminder |
| 2 | Chargement des données | 3h | Titanic, Adult Census UCI |
| 3 | Valeurs manquantes | 3h | Titanic, Melbourne Housing |
| 4 | Détection et traitement des valeurs aberrantes | 3h | FIFA 21 Raw, Air Quality UCI |
| 5 | Transformations de types de données | 3h | Adult Census UCI, Titanic |
| 6 | Ingénierie de variables | 3h | Melbourne Housing, Gapminder |
| 7 | Prétraitement de texte | 3h | 20 Newsgroups, Amazon Reviews |
| 8 | Séries temporelles et données chronologiques | 3h | Jena Climate, Air Quality UCI |
| 9 | Pipelines et automatisation | 3h | Adult Census UCI, Melbourne Housing |
| 10 | Projet de fin de cours | 3h | Au choix de l'étudiant |

## Jeux de données ouverts utilisés / Open datasets used

Tous les jeux de données utilisés dans ce cours sont librement accessibles :

- **Melbourne Housing (Kaggle):** https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot
- **Titanic (Kaggle):** https://www.kaggle.com/c/titanic
- **FIFA 21 Raw Data (Kaggle):** https://www.kaggle.com/datasets/stefanoleone992/fifa-21-complete-player-dataset
- **Adult Census (UCI):** https://archive.ics.uci.edu/dataset/2/adult
- **Jena Climate (Kaggle):** https://www.kaggle.com/datasets/mnassrib/jena-climate
- **Air Quality UCI:** https://archive.ics.uci.edu/dataset/360/air+quality
- **20 Newsgroups:** via `sklearn.datasets.fetch_20newsgroups`
- **Amazon Reviews:** https://www.kaggle.com/datasets/bittlingmayer/amazonreviews
- **Gapminder:** https://www.gapminder.org/data/

## Prérequis / Prerequisites

Python de base (variables, listes, boucles, fonctions). Une familiarité avec les DataFrames pandas est utile mais sera rappelée.

Basic Python knowledge (variables, lists, loops, functions). Familiarity with pandas DataFrames is helpful but will be reviewed.

## Outils / Tools

- Python 3.10+
- Jupyter Notebook / Google Colab
- Bibliothèques : pandas, numpy, matplotlib, seaborn, scikit-learn, missingno, nltk, spacy, joblib

## Structure du dépôt / Repository structure

- `fr/` — Notes de cours en français (LaTeX + PDF)
- `en/` — English lecture notes (LaTeX + PDF)
- `code/python/` — Scripts Python par chapitre / Python scripts per chapter

## Compilation

```bash
# Version française
cd fr && xelatex -shell-escape cours.tex && xelatex -shell-escape cours.tex

# English version
cd en && xelatex -shell-escape notes.tex && xelatex -shell-escape notes.tex
```
