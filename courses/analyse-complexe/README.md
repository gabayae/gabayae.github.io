# Analyse Complexe / Complex Analysis

**Niveau / Level:** Licence L3 (Undergraduate, 3rd year)

## Structure

```
analyse-complexe/
├── fr/
│   ├── cours.tex          ← Notes de cours en français (8586 lignes)
│   ├── cours.pdf          ← PDF compilé (141 pages)
│   └── figures/
├── en/
│   ├── notes.tex          ← English course notes (8411 lines)
│   ├── notes.pdf          ← Compiled PDF (136 pages)
│   └── figures/
├── README.md
```

## Chapitres / Chapters

| # | Français | English |
|---|----------|---------|
| 1 | Nombres complexes et géométrie du plan | Complex Numbers and Geometry of the Plane |
| 2 | Fonctions holomorphes et équations de Cauchy-Riemann | Holomorphic Functions and Cauchy-Riemann Equations |
| 3 | Fonctions élémentaires | Elementary Functions |
| 4 | Intégration complexe et théorème de Cauchy | Complex Integration and Cauchy's Theorem |
| 5 | Formule intégrale de Cauchy et applications | Cauchy Integral Formula and Applications |
| 6 | Séries de Laurent et singularités | Laurent Series and Singularities |
| 7 | Théorème des résidus et applications | Residue Theorem and Applications |
| 8 | Applications conformes | Conformal Mappings |
| 9 | Théorème de Rouché et principe de l'argument | Rouché's Theorem and the Argument Principle |
| 10 | Fonctions entières et méromorphes | Entire and Meromorphic Functions |

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

- Analyse Réelle I & II (Real Analysis)
- Topologie Générale (General Topology) — recommended
