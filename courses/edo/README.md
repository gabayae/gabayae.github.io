# Équations Différentielles Ordinaires / Ordinary Differential Equations

**Niveau / Level:** Licence L2-L3 (Undergraduate)

## Structure

```
edo/
├── fr/
│   ├── cours.tex          ← Notes de cours en français (7805 lignes)
│   ├── cours.pdf          ← PDF compilé (132 pages)
│   └── figures/
├── en/
│   ├── notes.tex          ← English course notes (7268 lines)
│   ├── notes.pdf          ← Compiled PDF (123 pages)
│   └── figures/
├── README.md
```

## Chapitres / Chapters

| # | Français | English |
|---|----------|---------|
| 1 | Introduction et Modélisation | Introduction and Modelling |
| 2 | Équations du 1er Ordre | First-Order Equations |
| 3 | Théorèmes d'Existence et d'Unicité | Existence and Uniqueness Theorems |
| 4 | Équations Linéaires du 2nd Ordre | 2nd Order Linear ODEs |
| 5 | Systèmes Différentiels Linéaires | Linear Differential Systems |
| 6 | Méthodes de Résolution Explicite | Explicit Solution Methods |
| 7 | Transformées de Laplace | Laplace Transform |
| 8 | Stabilité et Équilibres | Stability and Equilibria |
| 9 | Systèmes Non-Linéaires et Bifurcations | Nonlinear Systems and Bifurcations |
| 10 | Applications | Applications |

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
- Algèbre Linéaire (Linear Algebra)
