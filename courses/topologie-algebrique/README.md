# Topologie Algébrique / Algebraic Topology

**Niveau / Level:** Master / Doctorat (Graduate)

## Structure

```
topologie-algebrique/
├── fr/
│   ├── cours.tex          ← Notes de cours en français (8421 lignes)
│   ├── cours.pdf          ← PDF compilé (140 pages)
│   └── figures/
├── en/
│   ├── notes.tex          ← English course notes (8576 lines)
│   ├── notes.pdf          ← Compiled PDF (131 pages)
│   └── figures/
├── README.md
```

## Chapitres / Chapters

| # | Français | English |
|---|----------|---------|
| 1 | Rappels de Topologie et Motivations | Topology Review and Motivations |
| 2 | Le Groupe Fondamental | The Fundamental Group |
| 3 | Théorème de Van Kampen | Seifert-Van Kampen Theorem |
| 4 | Revêtements et Groupe Fondamental | Covering Spaces and Fundamental Group |
| 5 | Homologie Singulière | Singular Homology |
| 6 | Suites Exactes Longues et Excision | Long Exact Sequences and Excision |
| 7 | Théorème de Mayer-Vietoris | Mayer-Vietoris Theorem |
| 8 | Cohomologie Singulière et Cup-Produit | Singular Cohomology and Cup Product |
| 9 | Dualité de Poincaré | Poincaré Duality |
| 10 | Groupes d'Homotopie Supérieurs | Higher Homotopy Groups |
| 11 | Théorie de l'Obstruction et Applications | Obstruction Theory and Applications |

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
- Algèbre Abstraite I & II / Abstract Algebra I & II
- Algèbre Linéaire / Linear Algebra
- Familiarité avec la théorie des catégories utile / Category theory familiarity helpful
