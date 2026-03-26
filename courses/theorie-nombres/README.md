# Théorie des Nombres / Number Theory

**Niveau / Level:** Licence L2-L3 (Undergraduate)

## Structure

```
theorie-nombres/
├── fr/
│   ├── cours.tex          ← Notes de cours en français (7452 lignes)
│   ├── cours.pdf          ← PDF compilé (114 pages)
│   └── figures/
├── en/
│   ├── notes.tex          ← English course notes (6768 lines)
│   ├── notes.pdf          ← Compiled PDF (99 pages)
│   └── figures/
├── README.md
```

## Chapitres / Chapters

| # | Français | English |
|---|----------|---------|
| 1 | Divisibilité et Algorithme d'Euclide | Divisibility and Euclidean Algorithm |
| 2 | Nombres Premiers | Prime Numbers |
| 3 | Congruences et Arithmétique Modulaire | Congruences and Modular Arithmetic |
| 4 | Théorèmes de Fermat, Euler, Wilson | Fermat, Euler, Wilson Theorems |
| 5 | Restes Chinois et Applications | Chinese Remainder Theorem |
| 6 | Résidus Quadratiques et Réciprocité | Quadratic Residues and Reciprocity |
| 7 | Formes Quadratiques | Quadratic Forms |
| 8 | Fonctions Arithmétiques | Arithmetic Functions |
| 9 | Nombres p-adiques | p-adic Numbers |
| 10 | Théorie Analytique des Nombres | Analytic Number Theory Preview |

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

- Algèbre Abstraite I (Abstract Algebra I) — or concurrent
- Basic proof writing
