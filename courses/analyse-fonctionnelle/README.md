# Analyse Fonctionnelle / Functional Analysis

**Niveau / Level:** Master / Doctorat (Graduate)

## Structure

```
analyse-fonctionnelle/
├── fr/
│   ├── cours.tex          ← Notes de cours en français (9206 lignes)
│   ├── cours.pdf          ← PDF compilé (206 pages)
│   └── figures/
├── en/
│   ├── notes.tex          ← English course notes (9368 lines)
│   ├── notes.pdf          ← Compiled PDF (199 pages)
│   └── figures/
├── README.md
```

## Chapitres / Chapters

| # | Français | English |
|---|----------|---------|
| 1 | Espaces de Banach — Fondements | Banach Spaces — Foundations |
| 2 | Espaces de Hilbert | Hilbert Spaces |
| 3 | Opérateurs Linéaires Bornés | Bounded Linear Operators |
| 4 | Théorème de Hahn-Banach et Conséquences | The Hahn-Banach Theorem and Consequences |
| 5 | Théorème de Banach-Steinhaus et Applications | The Uniform Boundedness Principle |
| 6 | Théorème de l'Application Ouverte et du Graphe Fermé | The Open Mapping Theorem and Closed Graph Theorem |
| 7 | Espaces Duaux et Réflexivité | Dual Spaces and Reflexivity |
| 8 | Topologies Faibles | Weak Topologies |
| 9 | Théorie Spectrale des Opérateurs Compacts | Spectral Theory of Compact Operators |
| 10 | Théorème Spectral pour les Opérateurs Auto-Adjoints | The Spectral Theorem for Self-Adjoint Operators |
| 11 | Espaces $L^p$ et Dualité | $L^p$ Spaces and Duality |
| 12 | Algèbres de Banach et $C^*$-Algèbres — Introduction | Banach Algebras and $C^*$-Algebras — Introduction |

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
- Analyse Réelle / Real Analysis (Lebesgue integration)
- Algèbre Linéaire / Linear Algebra
- Calcul Différentiel / Differential Calculus
- Théorie de la Mesure utile / Measure Theory helpful
