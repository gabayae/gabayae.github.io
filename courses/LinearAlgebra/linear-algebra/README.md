# Linear Algebra / Algèbre Linéaire

Comprehensive undergraduate course notes in **English** and **French**.

## Structure

```
linear-algebra/
├── common/
│   └── preamble.sty          # Shared macros, theorem environments, notation
├── fr/
│   ├── cours.tex              # French main document
│   └── chapters/              # French chapter files
├── en/
│   ├── notes.tex              # English main document
│   └── chapters/              # English chapter files
├── bibliography.bib           # Shared references
└── README.md
```

## Contents

| Chapter | Title (EN) | Title (FR) |
|---------|-----------|------------|
| 0 | Preliminaries | Préliminaires |
| 1 | Vector Spaces and Subspaces | Espaces vectoriels et sous-espaces |
| 2 | Linear Maps and Matrices | Applications linéaires et matrices |
| 3 | Systems of Linear Equations | Systèmes d'équations linéaires |
| 4 | Determinants | Déterminants |
| 5 | Eigenvalues and Diagonalization | Valeurs propres et diagonalisation |
| 6 | Inner Product Spaces | Espaces préhilbertiens et orthogonalité |
| 7 | Spectral Theorem | Théorème spectral et matrices symétriques |
| 8 | Jordan Normal Form | Forme normale de Jordan |

## Compilation

Requires **XeLaTeX** and **Biber**. Compile each version separately:

### English version
```bash
cd en
xelatex notes.tex
biber notes
xelatex notes.tex
xelatex notes.tex
```

### French version
```bash
cd fr
xelatex cours.tex
biber cours
xelatex cours.tex
xelatex cours.tex
```

## Prerequisites

- TeX Live 2023+ or MiKTeX (with XeLaTeX)
- Biber (for bibliography)
- Packages: amsmath, amssymb, tcolorbox, tikz, pgfplots, fontspec, unicode-math, polyglossia, biblatex, cleveref, imakeidx

## Level

Undergraduate (1st-2nd year), for mathematics and engineering students.

## License

These notes are provided for educational purposes.
