# Topologie Générale / General Topology

**Niveau / Level:** Licence L2–L3
**Prérequis / Prerequisites:** Analyse Réelle I & II (suites, continuité, espaces métriques)

## Structure

```
topologie-generale/
├── fr/
│   ├── cours.tex          ← Notes de cours complètes (français, conventions Bourbaki)
│   └── figures/            ← Figures TikZ compilées
├── en/
│   ├── notes.tex          ← Complete course notes (English, Munkres-style)
│   └── figures/            ← Compiled TikZ figures
└── README.md
```

## Compilation

```bash
# French version
cd fr && pdflatex -interaction=nonstopmode cours.tex && pdflatex cours.tex && makeindex cours && pdflatex cours.tex

# English version
cd en && pdflatex -interaction=nonstopmode notes.tex && pdflatex notes.tex && makeindex notes && pdflatex notes.tex
```

## Chapitres / Chapters

1. Espaces Topologiques / Topological Spaces
2. Ouverts, Fermés, Intérieur, Adhérence, Frontière / Open Sets, Closed Sets, Interior, Closure, Boundary
3. Bases et Sous-bases / Bases and Sub-bases
4. Continuité et Homéomorphismes / Continuity and Homeomorphisms
5. Axiomes de Séparation / Separation Axioms
6. Compacité et Théorème de Tychonoff / Compactness and Tychonoff's Theorem
7. Connexité / Connectedness
8. Espaces Produits et Topologie Quotient / Product Spaces and Quotient Topology
9. Lemme d'Urysohn et Théorème de Tietze / Urysohn's Lemma and Tietze Extension Theorem
10. Aperçu de Topologie Algébrique / Preview of Algebraic Topology

## Références / References

- Munkres, J.R. *Topology* (2nd ed.)
- Bourbaki, N. *Topologie Générale*
- Willard, S. *General Topology*
- Kelley, J.L. *General Topology*
- Dugundji, J. *Topology*
- Dixmier, J. *Topologie Générale*
