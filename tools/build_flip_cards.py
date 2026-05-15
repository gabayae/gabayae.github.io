#!/usr/bin/env python3
"""
Regenerate every courses/*/index.html as a flip-card landing page.

Front of card: course title (bilingual), author, badges, downloads.
Back of card:  short bilingual summary (FR + EN).

The script:
  1. Walks courses/<slug>/index.html.
  2. Extracts existing metadata via regex (title, subtitle, badges, downloads,
     ToC, prereqs, language).
  3. Looks up the course in COURSE_SUMMARIES (slug -> {fr, en}). If missing,
     uses the existing <p class="desc"> text as the primary-language summary
     and falls back to a short generic for the other language.
  4. Writes a new index.html with the flip-card hero element + ToC and
     prerequisites preserved below the card.

The CSS lives inline in each page (consistent with the existing courses/<slug>/
index.html convention). The HTML stays under 200 lines per file.

Run from repo root:
    python tools/build_flip_cards.py
"""

from __future__ import annotations
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
COURSES_DIR = REPO_ROOT / "courses"

# --------------------------------------------------------------------- summaries
# Each entry is a short, faithful summary (2-3 sentences) of the course,
# in both French and English. Written from the existing index.html
# description and the catalog metadata.
COURSE_SUMMARIES: dict[str, dict[str, str]] = {
    # === PURE MATHEMATICS ===
    "analyse-reelle": {
        "fr": "Fondements rigoureux de l'analyse réelle en deux parties : logique, construction des réels, suites, séries, continuité, dérivation, intégrale de Riemann, suites de fonctions, calcul différentiel en plusieurs variables.",
        "en": "A two-part rigorous introduction to real analysis: logic, construction of the reals, sequences, series, continuity, differentiation, Riemann integration, sequences of functions, and multivariable differential calculus.",
    },
    "analyse-fonctionnelle": {
        "fr": "Cours d'analyse fonctionnelle : espaces de Banach et Hilbert, grands théorèmes (Hahn-Banach, Banach-Steinhaus, application ouverte), théorie spectrale des opérateurs compacts, introduction aux C*-algèbres.",
        "en": "Functional analysis: Banach and Hilbert spaces, the four major theorems (Hahn-Banach, Banach-Steinhaus, open mapping, closed graph), spectral theory of compact and self-adjoint operators, and an introduction to C*-algebras.",
    },
    "analyse-numerique": {
        "fr": "Méthodes du calcul scientifique implémentées en Python : arithmétique flottante, systèmes linéaires (directs et itératifs), interpolation, intégration numérique, EDO. Chaque méthode est accompagnée d'une analyse de convergence et de stabilité.",
        "en": "Core scientific computing methods implemented in Python: floating-point arithmetic, direct and iterative linear solvers, interpolation, numerical integration, and ODE solvers. Each method is paired with a convergence and stability analysis.",
    },
    "edp": {
        "fr": "Équations aux dérivées partielles classiques (transport, chaleur, ondes, Laplace), avec les méthodes fondamentales (séparation de variables, Fourier, principe du maximum) et les outils modernes (Sobolev, méthodes variationnelles).",
        "en": "Classical partial differential equations (transport, heat, wave, Laplace), with foundational methods (separation of variables, Fourier series and transform, maximum principle) and modern tools (Sobolev spaces, variational methods).",
    },
    "topologie-ponctuelle-avancee": {
        "fr": "Topologie ponctuelle au-delà du cadre Hausdorff : espaces sobres et locales, domaines de Scott, topologie asymétrique, espaces bitopologiques. Liens avec l'informatique théorique et la théorie des points fixes.",
        "en": "Point-set topology beyond the Hausdorff setting: sober spaces and locales, Scott domains, asymmetric topology, bitopological spaces. Connections with theoretical computer science and fixed-point theory.",
    },
    "topologie-generale": {
        "fr": "Introduction à la topologie générale : axiomes, ouverts et fermés, continuité, axiomes de séparation, compacité (Tychonoff), connexité, espaces produits et quotients. Conclut par une ouverture vers la topologie algébrique.",
        "en": "Introduction to general topology: axioms, open and closed sets, continuity, separation axioms, compactness (including Tychonoff), connectedness, product and quotient spaces. Ends with a bridge to algebraic topology.",
    },
    "topologie-algebrique": {
        "fr": "Outils fondamentaux de la topologie algébrique : groupe fondamental, théorème de Van Kampen, homologie et cohomologie singulières, revêtements, dualité de Poincaré, groupes d'homotopie supérieurs.",
        "en": "Core tools of algebraic topology: the fundamental group, Van Kampen's theorem, singular homology and cohomology, covering spaces, Poincaré duality, and higher homotopy groups.",
    },
    "topologie-differentielle": {
        "fr": "Topologie différentielle : variétés lisses, applications différentiables, fibrés tangents, transversalité, formes différentielles. Théorèmes de Stokes, Sard et Whitney ; introduction à la théorie de Morse.",
        "en": "Differential topology: smooth manifolds, differentiable maps, tangent bundles, transversality, differential forms. Stokes', Sard's, and Whitney's theorems; introduction to Morse theory.",
    },
    "geometrie-riemannienne": {
        "fr": "Géométrie riemannienne : variétés munies d'une métrique, connexions, courbure (Riemann, Ricci, scalaire), géodésiques, théorèmes de comparaison, espaces symétriques. Brève introduction au flot de Ricci.",
        "en": "Riemannian geometry: manifolds with a metric, connections, curvature (Riemann, Ricci, scalar), geodesics, comparison theorems, symmetric spaces. Short introduction to Ricci flow.",
    },
    "theorie-categories": {
        "fr": "Théorie des catégories, langage unificateur des mathématiques : foncteurs, transformations naturelles, adjonctions, monades, lemme de Yoneda, catégories abéliennes et dérivées. Ouverture aux topos et aux infini-catégories.",
        "en": "Category theory as a unifying language for modern mathematics: functors, natural transformations, adjunctions, monads, the Yoneda lemma, abelian and derived categories. Brief glimpse of topoi and infinity-categories.",
    },
    "points-fixes": {
        "fr": "Théorèmes de points fixes (Banach, Brouwer, Schauder, Kakutani, Tarski-Knaster) avec démonstrations, généralisations et applications. Espaces métriques généralisés, ensembles ordonnés, points fixes aléatoires.",
        "en": "Fixed-point theorems (Banach, Brouwer, Schauder, Kakutani, Tarski-Knaster) with proofs, generalizations, and applications. Generalized metric spaces, ordered sets, and random fixed points.",
    },
    "algebre-abstraite": {
        "fr": "Algèbre abstraite en deux parties : théorie des groupes (sous-groupes, quotients, Sylow), anneaux (idéaux, factorialité), puis théorie des corps, extensions et théorie de Galois avec applications classiques.",
        "en": "Two-part course in abstract algebra: group theory (subgroups, quotients, Sylow theorems), rings (ideals, factorization), then field theory, extensions, and Galois theory with classical applications.",
    },
    "theorie-nombres": {
        "fr": "Théorie des nombres : divisibilité, algorithme d'Euclide, congruences, théorèmes de Fermat et Euler, réciprocité quadratique, formes quadratiques, fonctions arithmétiques. Ouverture aux nombres p-adiques et à la théorie analytique.",
        "en": "Number theory: divisibility, Euclid's algorithm, congruences, Fermat's and Euler's theorems, quadratic reciprocity, quadratic forms, arithmetic functions. Glimpses of p-adic numbers and analytic number theory.",
    },
    "LinearAlgebra": {
        "fr": "Algèbre linéaire : espaces vectoriels, applications linéaires, systèmes linéaires, déterminants, diagonalisation, espaces préhilbertiens, théorème spectral, forme normale de Jordan.",
        "en": "Linear algebra: vector spaces, linear maps, linear systems, determinants, diagonalization, inner-product spaces, spectral theorem, and Jordan normal form.",
    },
    "maths-discretes": {
        "fr": "Mathématiques discrètes : structures finies et dénombrables fondamentales en informatique. Logique, techniques de preuve, combinatoire (séries génératrices, récurrences), théorie des graphes, introduction aux codes.",
        "en": "Discrete mathematics: finite and enumerable structures fundamental to computer science. Logic, proof techniques, combinatorics (generating functions, recurrences), graph theory, and an introduction to coding theory.",
    },
    "mesure-integration": {
        "fr": "Construction rigoureuse de la théorie de la mesure et de l'intégration de Lebesgue : sigma-algèbres, mesures, théorème de Carathéodory, intégrale de Lebesgue, convergence, espaces Lp, Radon-Nikodym, Fubini-Tonelli.",
        "en": "Rigorous construction of measure theory and Lebesgue integration: sigma-algebras, measures, Carathéodory's theorem, Lebesgue integral, convergence theorems, Lp spaces, Radon-Nikodym, and Fubini-Tonelli.",
    },
    "analyse-complexe": {
        "fr": "Théorie des fonctions d'une variable complexe : équations de Cauchy-Riemann, théorème intégral de Cauchy, séries de Laurent, théorème des résidus, transformations conformes. Applications au calcul d'intégrales et à la théorie des nombres.",
        "en": "Theory of functions of one complex variable: Cauchy-Riemann equations, Cauchy's integral theorem, Laurent series, residue theorem, conformal mappings. Applications to real integrals, fluid mechanics, and number theory.",
    },
    "edo": {
        "fr": "Théorie et méthodes de résolution des équations différentielles ordinaires : EDO du premier et second ordre, existence et unicité, systèmes linéaires, transformée de Laplace, stabilité, bifurcations. Applications en physique et biologie.",
        "en": "Theory and methods for ordinary differential equations: first- and second-order ODEs, existence and uniqueness, linear systems, Laplace transforms, equilibrium stability, and bifurcations. Applications in physics and biology.",
    },
    "modelisation": {
        "fr": "Traduction de phénomènes concrets en modèles mathématiques : dynamique des populations, modèles épidémiologiques, équations de diffusion, modèles stochastiques. On apprend à poser, analyser et tester un modèle.",
        "en": "Translating concrete phenomena into mathematical models: population dynamics, epidemiological models, diffusion equations, stochastic models. Students learn to formulate, analyze, and stress-test models.",
    },

    # === APPLIED MATHEMATICS & STATISTICS ===
    "probabilites": {
        "fr": "Introduction rigoureuse à la théorie mathématique des probabilités fondée sur l'axiomatique de Kolmogorov : espaces probabilisés, variables aléatoires, lois classiques, fonctions caractéristiques, lois des grands nombres, théorème central limite, chaînes de Markov.",
        "en": "Rigorous introduction to mathematical probability built on Kolmogorov's axioms: probability spaces, random variables, classical distributions, characteristic functions, laws of large numbers, central limit theorem, and Markov chains.",
    },
    "statistique": {
        "fr": "Introduction rigoureuse à la statistique mathématique : statistique descriptive, estimation ponctuelle, tests d'hypothèses, régression linéaire. Implémentations en Python et R.",
        "en": "Rigorous introduction to mathematical statistics: descriptive statistics, point estimation, hypothesis testing, and linear regression. Hands-on implementations in Python and R.",
    },
    "statistique-bayesienne": {
        "fr": "Paradigme bayésien de l'inférence : lois a priori conjuguées, MCMC (Metropolis-Hastings, Gibbs), modèles hiérarchiques, inférence variationnelle, modèles non-paramétriques. Outils théoriques et computationnels.",
        "en": "Bayesian paradigm for statistical inference: conjugate priors, MCMC methods (Metropolis-Hastings, Gibbs sampling), hierarchical models, variational inference, and non-parametric models. Theoretical foundations alongside computation.",
    },
    "processus-stochastiques": {
        "fr": "Présentation rigoureuse, fondée sur la théorie de la mesure, des principaux processus aléatoires : chaînes de Markov, processus de Poisson, martingales, mouvement brownien. Aboutit à l'intégrale d'Itô et aux EDS.",
        "en": "Measure-theoretic treatment of the main stochastic processes: Markov chains, Poisson processes, martingales, Brownian motion. Builds up to the Itô integral and stochastic differential equations.",
    },
    "finance-quantitative": {
        "fr": "Modélisation mathématique des marchés financiers : modèle de Black-Scholes, pricing et couverture d'options, calcul stochastique, modèles de volatilité et de taux, optimisation de portefeuille, mesures de risque, applications du ML.",
        "en": "Mathematical modeling of financial markets: Black-Scholes, option pricing and hedging, stochastic calculus, volatility and interest-rate models, portfolio optimization, risk measures, and machine-learning applications.",
    },
    "optimisation-convexe": {
        "fr": "Fondements théoriques de la convexité et algorithmes : ensembles et fonctions convexes, conditions KKT, dualité de Lagrange et Fenchel, méthodes de gradient, proximales et de points intérieurs.",
        "en": "Theoretical foundations of convexity and the most important optimization algorithms: convex sets and functions, KKT conditions, Lagrange and Fenchel duality, gradient, proximal, and interior-point methods.",
    },
    "recherche-operationnelle": {
        "fr": "Outils mathématiques et algorithmiques de la recherche opérationnelle : programmation linéaire (simplexe, dualité), transport, flots dans les réseaux, programmation en nombres entiers. Méthodes d'aide à la décision et d'optimisation.",
        "en": "Mathematical and algorithmic toolkit of operations research: linear programming (simplex, duality), transportation problems, network flows, integer programming. Methods for decision support and optimization.",
    },
    "systemes-dynamiques": {
        "fr": "Systèmes dynamiques continus et discrets, de la stabilité de Lyapunov aux phénomènes chaotiques : portraits de phase, bifurcations, cycles limites, exposants de Lyapunov, attracteurs étranges. Introduction à la théorie ergodique.",
        "en": "Continuous and discrete dynamical systems, from Lyapunov stability to chaos: phase portraits, bifurcations, limit cycles, Lyapunov exponents, strange attractors. Introduction to ergodic theory.",
    },
    "series-temporelles": {
        "fr": "Analyse des séries temporelles : stationnarité, modèles ARIMA et GARCH, analyse spectrale, modèles à espace d'états, filtre de Kalman, séries multivariées (VAR), méthodes de prévision. Applications en finance, économie, météorologie.",
        "en": "Time-series analysis: stationarity, ARIMA and GARCH models, spectral analysis, state-space models, Kalman filter, multivariate series (VAR), forecasting methods. Applications in finance, economics, and meteorology.",
    },

    # === DATA SCIENCE & ML ===
    "intro-data-science": {
        "fr": "Cours pratique de science des données de bout en bout. Chaque chapitre part d'un jeu de données réel et passe par le pipeline complet : manipulation Pandas, visualisation, EDA, nettoyage, modélisation ML, évaluation.",
        "en": "End-to-end practical data science course. Each chapter starts from a real dataset and runs through the full pipeline: Pandas wrangling, visualization, exploratory analysis, cleaning, ML modeling, and evaluation.",
    },
    "apprentissage-automatique": {
        "fr": "Fondements théoriques et pratiques du machine learning : modèles supervisés (régression, classification, SVM, arbres, ensembles), apprentissage non supervisé (clustering, réduction de dimension), apprentissage bayésien et noyaux. Accent sur la théorie de la généralisation.",
        "en": "Theoretical and practical foundations of machine learning: supervised models (regression, classification, SVMs, trees, ensembles), unsupervised learning (clustering, dimensionality reduction), Bayesian methods, and kernels. Focus on generalization theory.",
    },
    "apprentissage-profond": {
        "fr": "Cours d'apprentissage profond couvrant les réseaux classiques (CNN, RNN, LSTM), les Transformers, les modèles génératifs (GAN, VAE, diffusion), et les questions théoriques de généralisation et d'expressivité.",
        "en": "Deep learning course covering classical architectures (CNN, RNN, LSTM), Transformers, generative models (GAN, VAE, diffusion), and the theoretical questions of generalization and expressivity that connect to them.",
    },
    "apprentissage-geometrique": {
        "fr": "Cours avancé sur l'apprentissage profond géométrique : architectures construites à partir des symétries et de la structure géométrique des données. Réseaux sur graphes, réseaux équivariants, apprentissage sur variétés et nuages de points, liens avec la TDA.",
        "en": "Advanced course on geometric deep learning: architectures built from the symmetries and geometric structure of data. Graph neural networks, equivariant networks, learning on manifolds and point clouds, and connections to topological data analysis.",
    },
    "apprentissage-renforcement": {
        "fr": "Apprentissage par renforcement, des fondements (MDP, programmation dynamique) aux algorithmes profonds modernes (DQN, Policy Gradient, Acteur-Critique, PPO, SAC). RL multi-agents, RL sûr, applications en robotique, jeux et contrôle.",
        "en": "Reinforcement learning from foundations (MDPs, dynamic programming) to modern deep algorithms (DQN, policy gradients, actor-critic, PPO, SAC). Multi-agent RL, safe RL, and applications to robotics, games, and control.",
    },
    "tda": {
        "fr": "Outils de l'analyse topologique des données : homologie persistante, diagrammes de persistance, complexes simpliciaux, algorithme Mapper, théorèmes de stabilité. Extraction d'informations topologiques et intégration dans des pipelines de machine learning.",
        "en": "Tools of topological data analysis: persistent homology, persistence diagrams, simplicial complexes, the Mapper algorithm, and stability theorems. Extracting topological information and integrating it into machine-learning pipelines.",
    },
    "tal-nlp": {
        "fr": "Traitement automatique du langage, des représentations classiques aux grands modèles : plongements de mots, architectures Transformer, modèles pré-entraînés, fine-tuning, génération de texte, RAG, éthique et biais.",
        "en": "Natural language processing, from classical representations to large language models: word embeddings, Transformer architectures, pretrained models, fine-tuning, text generation, RAG, and ethics and bias in NLP systems.",
    },
    "mlops": {
        "fr": "Pratiques et outils du MLOps : ce qu'il faut pour faire passer un modèle de ML du notebook à la production sans qu'il casse. Versioning (Git, DVC), suivi (MLflow), pipelines de données, Docker, déploiement (FastAPI), CI/CD, monitoring.",
        "en": "MLOps practices and tools: what it takes to move a machine-learning model from the notebook to production without it breaking. Versioning (Git, DVC), experiment tracking (MLflow), data pipelines, Docker, deployment (FastAPI), CI/CD, monitoring.",
    },
    "ia-generative": {
        "fr": "Cours sur l'IA générative moderne : Transformers, architectures GPT, prompt engineering, fine-tuning (LoRA/QLoRA), RAG, modèles de diffusion, évaluation et sûreté (hallucination, alignement, RLHF), agents LLM. Outillage volontairement gratuit.",
        "en": "Course on modern generative AI: Transformers, GPT architectures, prompt engineering, fine-tuning (LoRA/QLoRA), retrieval-augmented generation, diffusion models, evaluation and safety (hallucination, alignment, RLHF), and LLM agents. Tooling is deliberately free-tier.",
    },
    "pretraitement-donnees": {
        "fr": "Cours pratique qui couvre le pipeline complet de prétraitement : chargement depuis sources multiples, valeurs manquantes, outliers, encodage, mise à l'échelle, ingénierie de variables, texte, données temporelles, pipelines scikit-learn reproductibles.",
        "en": "Hands-on course covering the full data preprocessing pipeline: loading from multiple sources, missing values, outliers, encoding, scaling, feature engineering, text, temporal data, and reproducible scikit-learn pipelines.",
    },
    "programmation-julia": {
        "fr": "Cours pratique sur Julia, des fondamentaux du langage à la programmation scientifique et au ML : types, dispatch multiple, tableaux, DataFrames, visualisation (Plots.jl, Makie.jl), performance, EDO (DifferentialEquations.jl), ML (MLJ.jl, Flux.jl).",
        "en": "Hands-on Julia course, from language fundamentals to scientific computing and ML: types, multiple dispatch, arrays, DataFrames, visualization (Plots.jl, Makie.jl), performance work, differential equations, and machine learning (MLJ.jl, Flux.jl).",
    },
    "programmation-scientifiques": {
        "fr": "Programmation Python et R pour scientifiques. De l'installation aux bonnes pratiques, bases du langage, structures de données, et bibliothèques essentielles du calcul scientifique : NumPy, Matplotlib, Pandas, SciPy.",
        "en": "Python and R programming for scientists. From environment setup to development best practices, language basics, data structures, and the essential scientific computing libraries: NumPy, Matplotlib, Pandas, SciPy.",
    },
    "bases-donnees": {
        "fr": "Fondements des systèmes de bases relationnelles et au-delà : modélisation entité-relation, algèbre relationnelle, SQL (requêtes, jointures, agrégation), normalisation, transactions, indexation, ETL, introduction NoSQL.",
        "en": "Foundations of relational database systems and beyond: entity-relationship modeling, relational algebra, SQL (queries, joins, aggregation), normalization, transactions, indexing, ETL pipelines, and an introduction to NoSQL.",
    },
    "analyse-donnees-sante": {
        "fr": "Cours pratique pour professionnels de santé, épidémiologistes et étudiants en santé publique qui doivent analyser des données de santé avec Python : Pandas, mesures épidémiologiques, tests d'hypothèses, régression, ML clinique, cartographie géospatiale.",
        "en": "Practical course for health professionals, epidemiologists, and public health students who need to analyze health data with Python: Pandas, epidemiological measures, hypothesis testing, regression, clinical ML, and geospatial health mapping.",
    },
}

# --------------------------------------------------------------------- SVG library
# Five thematic SVG motifs, one per course family. Used as decorative
# corner art on the flip-card back. Kept tiny + monochromatic so they
# blend with the existing dark/gold theme.
SVG_NEURAL = """\
<svg class="card-svg" viewBox="0 0 100 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <g fill="none" stroke="var(--blue-light)" stroke-width="0.6" opacity="0.35">
    <line x1="10" y1="15" x2="40" y2="30"/><line x1="10" y1="30" x2="40" y2="30"/>
    <line x1="10" y1="45" x2="40" y2="30"/><line x1="10" y1="15" x2="40" y2="15"/>
    <line x1="10" y1="45" x2="40" y2="45"/><line x1="40" y1="15" x2="70" y2="30"/>
    <line x1="40" y1="30" x2="70" y2="30"/><line x1="40" y1="45" x2="70" y2="30"/>
    <line x1="70" y1="30" x2="90" y2="30"/>
  </g>
  <g fill="var(--gold)" opacity="0.85">
    <circle cx="10" cy="15" r="2"/><circle cx="10" cy="30" r="2"/><circle cx="10" cy="45" r="2"/>
    <circle cx="40" cy="15" r="2.5"/><circle cx="40" cy="30" r="2.5"/><circle cx="40" cy="45" r="2.5"/>
    <circle cx="70" cy="30" r="3"/><circle cx="90" cy="30" r="2"/>
  </g>
</svg>"""

SVG_PIPELINE = """\
<svg class="card-svg" viewBox="0 0 110 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <g stroke="var(--gold)" stroke-width="1" fill="none" opacity="0.4">
    <rect x="5"  y="13" width="18" height="14" rx="2"/>
    <rect x="33" y="13" width="18" height="14" rx="2"/>
    <rect x="61" y="13" width="18" height="14" rx="2"/>
    <rect x="89" y="13" width="18" height="14" rx="2"/>
  </g>
  <g stroke="var(--blue-light)" stroke-width="0.7" fill="none">
    <path d="M23 20 L33 20" marker-end="url(#a)"/>
    <path d="M51 20 L61 20" marker-end="url(#a)"/>
    <path d="M79 20 L89 20" marker-end="url(#a)"/>
  </g>
  <defs><marker id="a" markerWidth="4" markerHeight="4" refX="3" refY="2"
   orient="auto"><polygon points="0 0, 4 2, 0 4" fill="var(--blue-light)"/></marker></defs>
</svg>"""

SVG_TOPOLOGY = """\
<svg class="card-svg" viewBox="0 0 100 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <g fill="none" stroke="var(--gold)" stroke-width="0.7" opacity="0.55">
    <ellipse cx="50" cy="30" rx="32" ry="14"/>
    <ellipse cx="50" cy="30" rx="32" ry="14" transform="rotate(45 50 30)"/>
    <ellipse cx="50" cy="30" rx="32" ry="14" transform="rotate(90 50 30)"/>
    <ellipse cx="50" cy="30" rx="32" ry="14" transform="rotate(135 50 30)"/>
  </g>
  <circle cx="50" cy="30" r="2.5" fill="var(--blue-light)"/>
</svg>"""

SVG_CURVE = """\
<svg class="card-svg" viewBox="0 0 110 50" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <g fill="none" stroke="var(--gold)" stroke-width="0.6" opacity="0.4">
    <line x1="5" y1="42" x2="105" y2="42"/>
    <line x1="5" y1="42" x2="5" y2="5"/>
  </g>
  <path d="M 5 42 Q 25 5 50 30 T 100 12" fill="none"
        stroke="var(--blue-light)" stroke-width="1.5" opacity="0.85"/>
  <path d="M 5 42 Q 30 25 55 25 T 100 20" fill="none"
        stroke="var(--gold)" stroke-width="0.8" opacity="0.55" stroke-dasharray="2,2"/>
</svg>"""

SVG_GRID = """\
<svg class="card-svg" viewBox="0 0 100 60" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <g stroke="var(--gold)" stroke-width="0.5" fill="none" opacity="0.4">
    <rect x="10" y="10" width="80" height="40"/>
    <line x1="30" y1="10" x2="30" y2="50"/>
    <line x1="50" y1="10" x2="50" y2="50"/>
    <line x1="70" y1="10" x2="70" y2="50"/>
    <line x1="10" y1="25" x2="90" y2="25"/>
    <line x1="10" y1="40" x2="90" y2="40"/>
  </g>
  <g fill="var(--blue-light)" opacity="0.7">
    <rect x="12" y="12" width="16" height="11"/>
    <rect x="52" y="27" width="16" height="11"/>
    <rect x="72" y="12" width="16" height="11"/>
  </g>
</svg>"""

# Course -> SVG mapping. Default falls back to the curve motif.
SVG_FOR: dict[str, str] = {
    # Neural / ML / agents
    "ia-generative": SVG_NEURAL, "apprentissage-profond": SVG_NEURAL,
    "apprentissage-geometrique": SVG_NEURAL, "apprentissage-renforcement": SVG_NEURAL,
    "apprentissage-automatique": SVG_NEURAL, "tal-nlp": SVG_NEURAL,
    "tda": SVG_TOPOLOGY,
    # Pipelines / data
    "pretraitement-donnees": SVG_PIPELINE, "mlops": SVG_PIPELINE,
    "intro-data-science": SVG_PIPELINE, "bases-donnees": SVG_PIPELINE,
    "analyse-donnees-sante": SVG_PIPELINE,
    # Topology / geometry
    "topologie-generale": SVG_TOPOLOGY, "topologie-algebrique": SVG_TOPOLOGY,
    "topologie-differentielle": SVG_TOPOLOGY, "topologie-ponctuelle-avancee": SVG_TOPOLOGY,
    "geometrie-riemannienne": SVG_TOPOLOGY, "theorie-categories": SVG_TOPOLOGY,
    "points-fixes": SVG_TOPOLOGY,
    # Analysis / curves
    "analyse-reelle": SVG_CURVE, "analyse-complexe": SVG_CURVE,
    "analyse-fonctionnelle": SVG_CURVE, "analyse-numerique": SVG_CURVE,
    "edp": SVG_CURVE, "edo": SVG_CURVE,
    "mesure-integration": SVG_CURVE, "series-temporelles": SVG_CURVE,
    "modelisation": SVG_CURVE, "systemes-dynamiques": SVG_CURVE,
    "finance-quantitative": SVG_CURVE,
    # Grids / discrete / algebra
    "algebre-abstraite": SVG_GRID, "theorie-nombres": SVG_GRID,
    "LinearAlgebra": SVG_GRID, "maths-discretes": SVG_GRID,
    "recherche-operationnelle": SVG_GRID, "optimisation-convexe": SVG_GRID,
    "probabilites": SVG_GRID, "statistique": SVG_GRID,
    "statistique-bayesienne": SVG_GRID, "processus-stochastiques": SVG_GRID,
    "programmation-julia": SVG_GRID, "programmation-scientifiques": SVG_GRID,
}


# --------------------------------------------------------------------- helpers
META_RE = {
    "lang":     re.compile(r'<html lang="([^"]+)"'),
    "h1":       re.compile(r"<h1>(.*?)</h1>", re.DOTALL),
    "subtitle": re.compile(r'<p class="subtitle">(.*?)</p>', re.DOTALL),
    "author":   re.compile(r'<p class="author">(.*?)</p>', re.DOTALL),
    "badges":   re.compile(r'<div class="badges">(.*?)</div>', re.DOTALL),
    "toc":      re.compile(r"<h2>(?:Table of contents|Table des mati[eè]res)</h2>\s*<ol[^>]*>(.*?)</ol>",
                           re.DOTALL | re.IGNORECASE),
    "prereq":   re.compile(r"<h2>(?:Prerequisites|Pr[eé]requis)</h2>\s*<p[^>]*>(.*?)</p>",
                           re.DOTALL | re.IGNORECASE),
    "downloads":re.compile(r'<div class="downloads">(.*?)</div>', re.DOTALL),
    "title":    re.compile(r"<title>(.*?)</title>", re.DOTALL),
}


def extract(html: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for key, pat in META_RE.items():
        m = pat.search(html)
        out[key] = m.group(1).strip() if m else ""
    return out


def render(slug: str, meta: dict[str, str]) -> str:
    summaries = COURSE_SUMMARIES.get(slug)
    if not summaries:
        # Fallback: use the existing description fragment for FR, generic for EN.
        desc_match = re.search(r'<p class="(?:desc|prereqs?)">(.*?)</p>', meta.get("downloads", ""), re.DOTALL)
        fr_text = "Notes de cours du Dr. Yaé Ulrich Gaba sur ce sujet."
        en_text = "Lecture notes by Dr. Yaé Ulrich Gaba on this topic."
        summaries = {"fr": fr_text, "en": en_text}

    lang = meta.get("lang") or "fr"
    h1   = meta.get("h1") or slug
    sub  = meta.get("subtitle") or ""
    auth = meta.get("author") or "Yaé Ulrich Gaba"
    bdgs = meta.get("badges") or ""
    toc  = meta.get("toc") or ""
    pre  = meta.get("prereq") or ""
    dl   = meta.get("downloads") or ""
    page_title = meta.get("title") or f"{h1} — Y.U. Gaba"
    svg  = SVG_FOR.get(slug, SVG_CURVE)

    # Localized labels (page is in lang)
    if lang == "fr":
        L = {
            "back": "&larr; Retour au catalogue",
            "hint": "Survolez ou touchez pour voir le r&eacute;sum&eacute;",
            "in_brief": "En bref · In brief",
            "toc": "Table des mati&egrave;res",
            "prereq": "Pr&eacute;requis",
            "downloads": "T&eacute;l&eacute;chargements",
        }
    else:
        L = {
            "back": "&larr; Back to catalog",
            "hint": "Hover or tap to see the summary",
            "in_brief": "In brief · En bref",
            "toc": "Table of contents",
            "prereq": "Prerequisites",
            "downloads": "Download",
        }

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
:root{{--bg:#162240;--bg-card:#1d2d4f;--bg-card-2:#243560;--text:#EDE9E2;--text-muted:#a8a196;--gold:#E8C230;--blue:#3B6FD4;--blue-light:#5a8be6;--border:rgba(237,233,226,.08);--font:'IBM Plex Sans',sans-serif;--mono:'IBM Plex Mono',monospace}}
html{{scroll-behavior:smooth}}body{{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.6;min-height:100vh}}
a{{color:var(--blue-light);text-decoration:none;transition:color .2s}}a:hover{{color:var(--gold)}}
.container{{max-width:880px;margin:0 auto;padding:0 24px}}
.back{{display:inline-block;margin:32px 0 18px;font-size:.95rem;font-family:var(--mono);color:var(--text-muted)}}
.back:hover{{color:var(--gold)}}

/* ----- Flip card hero ----- */
.flip-wrap{{perspective:1800px;margin:8px 0 36px}}
.flip-card{{position:relative;width:100%;min-height:440px;transform-style:preserve-3d;
  transition:transform .85s cubic-bezier(.2,.85,.3,1);cursor:pointer;outline:none}}
.flip-wrap:hover .flip-card,.flip-card.flipped,.flip-card:focus-visible{{transform:rotateY(180deg)}}
.flip-face{{position:absolute;inset:0;width:100%;height:100%;min-height:inherit;
  -webkit-backface-visibility:hidden;backface-visibility:hidden;
  background:linear-gradient(140deg,var(--bg-card) 0%,var(--bg-card-2) 100%);
  border:1px solid var(--border);border-radius:16px;padding:28px 32px 24px;
  display:flex;flex-direction:column;overflow:hidden}}
.flip-back{{transform:rotateY(180deg);background:linear-gradient(140deg,var(--bg-card-2) 0%,var(--bg-card) 100%)}}
.card-svg{{position:absolute;top:18px;right:24px;width:130px;height:auto;opacity:.55;pointer-events:none}}
.flip-back .card-svg{{top:auto;right:24px;bottom:20px;opacity:.35}}
h1{{font-size:2.1rem;font-weight:700;line-height:1.15;margin-bottom:6px;max-width:80%}}
.subtitle{{font-size:1.1rem;color:var(--text-muted);margin-bottom:14px;font-style:italic}}
.author{{font-size:.92rem;color:var(--gold);margin-bottom:14px;font-family:var(--mono);letter-spacing:.02em}}
.badges{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px;position:relative;z-index:1}}
.badge{{background:rgba(255,255,255,.04);border:1px solid var(--border);padding:4px 14px;
  border-radius:20px;font-size:.78rem;font-family:var(--mono);color:var(--text-muted)}}
.downloads{{display:flex;flex-wrap:wrap;gap:10px;margin-top:auto;padding-top:14px}}
.btn,.btn-outline{{display:inline-block;padding:10px 22px;border-radius:8px;font-weight:500;font-size:.9rem;
  font-family:var(--font);transition:background .2s,transform .15s}}
.btn{{background:var(--blue);color:#fff}}.btn:hover{{background:var(--blue-light);transform:translateY(-1px)}}
.btn-outline{{background:transparent;border:1px solid var(--blue);color:var(--blue-light)}}
.btn-outline:hover{{background:rgba(59,111,212,.15);color:#fff}}
.flip-hint{{position:absolute;bottom:14px;right:24px;font-family:var(--mono);font-size:.72rem;
  color:var(--text-muted);opacity:.65;letter-spacing:.04em}}
.flip-back h2{{font-size:.85rem;font-family:var(--mono);font-weight:500;color:var(--gold);
  letter-spacing:.12em;text-transform:uppercase;margin-bottom:18px}}
.summary{{font-size:.94rem;line-height:1.7;color:var(--text);max-width:95%;position:relative;z-index:1}}
.summary + .summary{{margin-top:14px;padding-top:14px;border-top:1px solid var(--border)}}
.summary-lang{{display:inline-block;font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;
  text-transform:uppercase;color:var(--gold);margin-bottom:6px;padding:2px 8px;
  border:1px solid var(--gold);border-radius:3px;opacity:.85}}

/* ----- Sections below the card ----- */
section{{margin-bottom:30px}}
section h2{{font-size:1.15rem;font-weight:600;color:var(--gold);margin-bottom:10px;
  border-bottom:1px solid var(--border);padding-bottom:6px}}
ol.toc{{list-style:none}}ol.toc li{{padding:7px 0;border-bottom:1px solid var(--border);
  font-size:.93rem;color:var(--text-muted)}}ol.toc li:last-child{{border-bottom:none}}
.ch-num{{color:var(--blue-light);font-family:var(--mono);font-size:.8rem;margin-right:10px}}
.prereq{{color:var(--text-muted);font-size:.95rem;line-height:1.6}}
footer{{border-top:1px solid var(--border);padding:32px 0;margin-top:48px;text-align:center;
  font-size:.82rem;color:var(--text-muted);font-family:var(--mono)}}
@media(max-width:640px){{
  h1{{font-size:1.55rem;max-width:100%}}.card-svg{{width:80px;opacity:.3}}
  .flip-card{{min-height:520px}}.flip-face{{padding:22px}}
  .container{{padding:0 18px}}
}}
@media(prefers-reduced-motion:reduce){{
  .flip-card{{transition:none}}
}}
</style>
</head>
<body>
<div class="container">
  <a href="../index.html" class="back">{L["back"]}</a>

  <div class="flip-wrap">
    <div class="flip-card" tabindex="0" role="button"
         aria-label="{L["hint"]}" onclick="this.classList.toggle('flipped')"
         onkeydown="if(event.key==='Enter'||event.key===' '){{event.preventDefault();this.classList.toggle('flipped')}}">

      <div class="flip-face flip-front">
        {svg}
        <h1>{h1}</h1>
        <p class="subtitle">{sub}</p>
        <p class="author">{auth}</p>
        <div class="badges">{bdgs}</div>
        <div class="downloads">{dl}</div>
        <span class="flip-hint">{L["hint"]}</span>
      </div>

      <div class="flip-face flip-back">
        {svg}
        <h2>{L["in_brief"]}</h2>
        <div class="summary">
          <span class="summary-lang">Fran&ccedil;ais</span>
          <p>{summaries["fr"]}</p>
        </div>
        <div class="summary">
          <span class="summary-lang">English</span>
          <p>{summaries["en"]}</p>
        </div>
      </div>
    </div>
  </div>

  {f'<section><h2>{L["toc"]}</h2><ol class="toc">{toc}</ol></section>' if toc else ''}
  {f'<section><h2>{L["prereq"]}</h2><p class="prereq">{pre}</p></section>' if pre else ''}
</div>
<footer><div class="container">&copy; 2026 Y.U. Gaba</div></footer>
</body>
</html>
"""


def main() -> int:
    if not COURSES_DIR.is_dir():
        print(f"Courses dir not found: {COURSES_DIR}", file=sys.stderr)
        return 1

    written, skipped, missing_summary = 0, 0, []
    for path in sorted(COURSES_DIR.iterdir()):
        if not path.is_dir():
            continue
        index = path / "index.html"
        if not index.exists():
            continue
        slug = path.name
        html = index.read_text(encoding="utf-8")
        meta = extract(html)
        new_html = render(slug, meta)
        index.write_text(new_html, encoding="utf-8")
        if slug not in COURSE_SUMMARIES:
            missing_summary.append(slug)
        written += 1
        print(f"  wrote {slug}/index.html")

    print(f"\nDone. {written} pages rewritten.")
    if missing_summary:
        print(f"\nMissing summaries (used fallback): {', '.join(missing_summary)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
