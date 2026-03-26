# Analyse Numerique / Numerical Analysis

**Niveau / Level:** Licence L2/L3

## Structure

```
analyse-numerique/
├── fr/
│   ├── cours.tex          — Notes de cours (francais)
│   └── chapitres/         — Fichiers par chapitre
├── en/
│   ├── notes.tex          — Course notes (English)
│   └── chapters/          — Per-chapter files
├── code/
│   ├── python/            — Python implementations (NumPy/SciPy)
│   └── julia/             — Julia implementations
└── README.md
```

## Compilation

```bash
cd fr && xelatex -shell-escape cours.tex && xelatex -shell-escape cours.tex && xelatex -shell-escape cours.tex
cd en && xelatex -shell-escape notes.tex && xelatex -shell-escape notes.tex && xelatex -shell-escape notes.tex
```

## References

- Quarteroni, Sacco, Saleri — *Numerical Mathematics*
- Suli, Mayers — *An Introduction to Numerical Analysis*
- Trefethen, Bau — *Numerical Linear Algebra*
- Higham — *Accuracy and Stability of Numerical Algorithms*
- Demailly — *Analyse Numerique et Equations Differentielles*
