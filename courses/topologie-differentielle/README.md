# Topologie Différentielle / Differential Topology

**Niveau / Level:** Master / Doctorat (Graduate)

## Structure

```
topologie-differentielle/
├── fr/
│   ├── cours.tex          ← Notes de cours en français (8334 lignes)
│   ├── cours.pdf          ← PDF compilé (133 pages)
│   └── figures/
├── en/
│   ├── notes.tex          ← English course notes (8645 lines)
│   ├── notes.pdf          ← Compiled PDF (126 pages)
│   └── figures/
├── README.md
```

## Chapitres / Chapters

| # | Français | English |
|---|----------|---------|
| 1 | Variétés Différentielles — Définitions et Exemples | Smooth Manifolds — Definitions and Examples |
| 2 | Applications Lisses et Difféomorphismes | Smooth Maps and Diffeomorphisms |
| 3 | Fibrés Tangents et Cotangents | Tangent and Cotangent Bundles |
| 4 | Sous-variétés et Théorème de la Valeur Régulière | Submanifolds and Regular Value Theorem |
| 5 | Transversalité | Transversality |
| 6 | Formes Différentielles et Intégration | Differential Forms and Integration |
| 7 | Théorème de Stokes | Stokes' Theorem |
| 8 | Théorème de Sard | Sard's Theorem |
| 9 | Théorie de Morse — Introduction | Morse Theory — Introduction |
| 10 | Degré d'une Application Lisse | Degree of a Smooth Map |
| 11 | Théorème de Whitney et Plongements | Whitney Embedding Theorem |

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

- Topologie Générale / General Topology
- Calcul Différentiel / Differential Calculus (Banach spaces)
- Algèbre Linéaire / Linear Algebra
- Géométrie riemannienne utile / Riemannian geometry helpful
