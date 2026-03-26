# Mathématiques Discrètes / Discrete Mathematics

**Niveau / Level:** Licence L1-L2 (Undergraduate)

## Structure

```
maths-discretes/
├── fr/
│   ├── cours.tex          ← Notes de cours en français (7366 lignes)
│   ├── cours.pdf          ← PDF compilé (119 pages)
│   └── figures/
├── en/
│   ├── notes.tex          ← English course notes (6928 lines)
│   ├── notes.pdf          ← Compiled PDF (103 pages)
│   └── figures/
├── README.md
```

## Chapitres / Chapters

| # | Français | English |
|---|----------|---------|
| 1 | Logique Propositionnelle et des Prédicats | Propositional and Predicate Logic |
| 2 | Techniques de Preuve | Proof Techniques |
| 3 | Ensembles, Relations, Fonctions | Sets, Relations, Functions |
| 4 | Combinatoire — Dénombrement | Combinatorics — Counting |
| 5 | Inclusion-Exclusion et Applications | Inclusion-Exclusion and Applications |
| 6 | Fonctions Génératrices | Generating Functions |
| 7 | Récurrences et Équations de Récurrence | Recurrences |
| 8 | Théorie des Graphes — Notions de Base | Graph Theory — Basics |
| 9 | Arbres, Graphes Eulériens et Hamiltoniens | Trees, Eulerian and Hamiltonian Graphs |
| 10 | Coloration, Planéité et Graphes Bipartis | Coloring, Planarity and Bipartite Graphs |
| 11 | Introduction à la Théorie des Codes | Introduction to Coding Theory |

## Compilation

```bash
# French
cd fr
xelatex -interaction=nonstopmode cours.tex
xelatex -interaction=nonstopmode cours.tex
makeindex cours
xelatex -interaction=nonstopmode cours.tex

# English
cd en
xelatex -interaction=nonstopmode notes.tex
xelatex -interaction=nonstopmode notes.tex
makeindex notes
xelatex -interaction=nonstopmode notes.tex
```

## Prérequis / Prerequisites

- Mathématiques de lycée / High school mathematics
- Basic proof writing (taught in Chapter 2)
