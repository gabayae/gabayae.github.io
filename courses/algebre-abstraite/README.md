# Algèbre Abstraite I & II / Abstract Algebra I & II

**Niveau / Level:** Licence L2 (Algèbre I) and L3 (Algèbre II)
**Prérequis / Prerequisites:** Algèbre linéaire, théorie des ensembles, rédaction de preuves
**Public / Audience:** Étudiants en mathématiques / Mathematics students

## Structure

```
algebre-abstraite/
├── I/
│   ├── fr/
│   │   ├── cours.tex          ← Algèbre I: Groupes et Anneaux (français)
│   │   └── figures/
│   └── en/
│       ├── notes.tex          ← Algebra I: Groups and Rings (English)
│       └── figures/
├── II/
│   ├── fr/
│   │   ├── cours.tex          ← Algèbre II: Corps et Théorie de Galois (français)
│   │   └── figures/
│   └── en/
│       ├── notes.tex          ← Algebra II: Fields and Galois Theory (English)
│       └── figures/
└── README.md
```

## Chapitres / Chapters

### Algèbre I — Groupes et Anneaux / Groups and Rings
1. Groupes — Définitions et Exemples / Groups — Definitions and Examples
2. Sous-groupes, Sous-groupes Distingués, Quotients / Subgroups, Normal Subgroups, Quotients
3. Homomorphismes et Théorèmes d'Isomorphisme / Homomorphisms and Isomorphism Theorems
4. Actions de Groupes et Théorèmes de Sylow / Group Actions and Sylow Theorems
5. Anneaux — Définitions, Exemples, Idéaux / Rings — Definitions, Ideals
6. Anneaux Quotients, Domaines d'Intégrité, Corps de Fractions / Quotient Rings, Integral Domains
7. Anneaux Principaux, Euclidiens et Factoriels / PID, Euclidean Domains, UFD

### Algèbre II — Corps et Théorie de Galois / Fields and Galois Theory
8. Corps — Extensions Algébriques et Transcendantes / Fields — Algebraic and Transcendental Extensions
9. Corps de Rupture et Corps de Décomposition / Splitting Fields
10. Clôture Algébrique / Algebraic Closure
11. Extensions Galoisiennes / Galois Extensions
12. Théorie de Galois — Théorème Fondamental / Galois Theory — Fundamental Theorem
13. Applications: Constructibilité, Insolubilité par Radicaux / Applications

## Compilation

```bash
cd I/fr && xelatex cours.tex && xelatex cours.tex && makeindex cours && xelatex cours.tex
cd I/en && xelatex notes.tex && xelatex notes.tex && makeindex notes && xelatex notes.tex
cd II/fr && xelatex cours.tex && xelatex cours.tex && makeindex cours && xelatex cours.tex
cd II/en && xelatex notes.tex && xelatex notes.tex && makeindex notes && xelatex notes.tex
```

## Références / References

- Dummit, D. & Foote, R. *Abstract Algebra* (3rd ed.)
- Lang, S. *Algebra* (3rd ed.)
- Artin, M. *Algebra* (2nd ed.)
- Jacobson, N. *Basic Algebra I & II*
- Bourbaki, N. *Algèbre*
- Perrin, D. *Algèbre* (Cours de mathématiques)
