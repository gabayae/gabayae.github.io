# Analyse Réelle I & II / Real Analysis I & II

**Niveau / Level:** Licence L1 (First Year)
**Prérequis / Prerequisites:** Mathématiques de lycée / High school mathematics only
**Public / Audience:** Première rencontre avec les preuves rigoureuses / First contact with rigorous proofs

## Structure

```
analyse-reelle/
├── I/
│   ├── fr/
│   │   ├── cours.tex          ← Analyse Réelle I (français, conventions Bourbaki)
│   │   └── figures/
│   └── en/
│       ├── notes.tex          ← Real Analysis I (English)
│       └── figures/
├── II/
│   ├── fr/
│   │   ├── cours.tex          ← Analyse Réelle II (français)
│   │   └── figures/
│   └── en/
│       ├── notes.tex          ← Real Analysis II (English)
│       └── figures/
└── README.md
```

## Chapitres / Chapters

### Analyse I / Real Analysis I
1. Logique, Ensembles et Raisonnement Mathématique / Logic, Sets, and Mathematical Reasoning
2. Le Corps des Réels — Axiomes et Complétude / The Real Numbers — Axioms and Completeness
3. Suites Numériques / Sequences — Convergence, Limits, Cauchy Sequences
4. Séries Numériques / Numerical Series — Convergence Tests, Power Series
5. Limites et Continuité des Fonctions / Limits and Continuity of Functions
6. Dérivation / Differentiation — MVT, Taylor's Formula

### Analyse II / Real Analysis II
7. Intégrale de Riemann / Riemann Integration
8. Suites et Séries de Fonctions / Sequences and Series of Functions — Uniform Convergence
9. Calcul Différentiel en Plusieurs Variables / Multivariable Differential Calculus
10. Intégrales Multiples / Multiple Integrals and Change of Variables
11. Courbes et Intégrales Curvilignes / Curves and Line Integrals

## Compilation

```bash
# Analyse I — French
cd I/fr && xelatex -interaction=nonstopmode cours.tex && xelatex cours.tex && makeindex cours && xelatex cours.tex

# Analyse I — English
cd I/en && xelatex -interaction=nonstopmode notes.tex && xelatex notes.tex && makeindex notes && xelatex notes.tex

# Analyse II — French
cd II/fr && xelatex -interaction=nonstopmode cours.tex && xelatex cours.tex && makeindex cours && xelatex cours.tex

# Analyse II — English
cd II/en && xelatex -interaction=nonstopmode notes.tex && xelatex notes.tex && makeindex notes && xelatex notes.tex
```

## Références / References

- Rudin, W. *Principles of Mathematical Analysis* (3rd ed.)
- Zuily, C. & Queffélec, H. *Analyse pour l'agrégation*
- Ramis, E., Deschamps, C. & Odoux, J. *Cours de mathématiques spéciales*
- Pompeïani, F. & Tarrago, P. *Analyse*
- Tao, T. *Analysis I & II*
