# Statistique Mathématique / Mathematical Statistics

**Niveau / Level:** Licence L2/L3

## Structure

```
statistique/
├── fr/
│   ├── cours.tex          — Notes de cours complètes (français)
│   └── figures/            — Figures TikZ
├── en/
│   ├── notes.tex          — Full course notes (English)
│   └── figures/            — TikZ figures
├── code/python/
│   ├── ch01_descriptive.py
│   ├── ch02_sampling.py
│   ├── ch03_estimation.py
│   ├── ch04_properties.py
│   ├── ch05_confidence.py
│   ├── ch06_hypothesis.py
│   ├── ch07_classical_tests.py
│   ├── ch08_simple_regression.py
│   ├── ch09_multiple_regression.py
│   ├── ch10_bayesian.py
│   └── ch11_nonparametric.py
└── README.md
```

## Compilation

```bash
# French
cd fr && pdflatex -shell-escape cours.tex && bibtex cours && pdflatex -shell-escape cours.tex && pdflatex -shell-escape cours.tex

# English
cd en && pdflatex -shell-escape notes.tex && bibtex notes && pdflatex -shell-escape notes.tex && pdflatex -shell-escape notes.tex
```

## Prerequisites

- Théorie des Probabilités / Probability Theory
- Analyse Réelle I / Real Analysis I
- Algèbre Linéaire / Linear Algebra

## References

- Casella, G. & Berger, R.L. — *Statistical Inference* (2nd ed.)
- Wasserman, L. — *All of Statistics*
- Saporta, G. — *Probabilités, Analyse des Données et Statistique*
- Wackerly, Mendenhall & Scheaffer — *Mathematical Statistics with Applications*
