#!/usr/bin/env python3
"""
Insert a freshly-written FR preface into each FR cours.tex file that
currently lacks one, between \\tableofcontents and \\mainmatter.

The 19 prefaces below are written to match the existing voice of the
17 courses that already have prefaces (e.g., topologie-generale,
maths-discretes, series-temporelles): concrete motivation, stakes,
where the discipline sits, who the course is for, prerequisites.
Each ends with the standard `\\vfill\\hfill\\textit{L'auteur}` sign-off.

Run from repo root:
    python tools/add_prefaces.py

Idempotent: skips any file that already contains \\chapter*{...face}.
"""

from __future__ import annotations
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

PREFACES_FR: dict[str, str] = {
    "analyse-fonctionnelle": r"""L'analyse fonctionnelle est née d'une contradiction : les méthodes de l'analyse classique, conçues pour la droite réelle et $\R^n$, devaient s'étendre à des espaces de fonctions, c'est-à-dire à des espaces de dimension infinie. Ce qui s'y joue n'est pas seulement technique. Dans un espace de dimension infinie, la boule unité n'est jamais compacte, deux normes équivalentes peuvent ne pas exister, et la notion même de convergence se dédouble entre topologie forte et topologie faible.

\medskip

Ce cours construit progressivement les outils qui ont permis de surmonter ces obstacles : espaces de Banach et de Hilbert, théorèmes fondamentaux (Hahn--Banach, Banach--Steinhaus, application ouverte, graphe fermé), théorie spectrale des opérateurs compacts et auto-adjoints. Les applications visées sont l'analyse harmonique, la mécanique quantique, et la théorie moderne des équations aux dérivées partielles.

\medskip

\noindent\textbf{Prérequis.} Topologie générale (compacité, convergence), théorie de la mesure (espaces $L^p$), algèbre linéaire.

\vfill
\hfill\textit{L'auteur}""",

    "apprentissage-automatique": r"""L'apprentissage automatique est devenu l'outil par défaut pour transformer des données en décisions. Il ne se réduit pourtant ni à un catalogue d'algorithmes ni à une question d'optimisation : son cœur conceptuel est la \emph{généralisation} --- la capacité d'un modèle entraîné sur un échantillon fini à se comporter correctement sur des données qu'il n'a jamais vues. C'est cette question, et non l'astuce algorithmique du jour, qui sépare un système qui tient en production d'un système qui s'effondre au premier changement de distribution.

\medskip

Ces notes parcourent l'apprentissage supervisé (régression, classification, SVM, arbres, méthodes d'ensemble), non supervisé (clustering, réduction de dimension), bayésien, et l'apprentissage par noyaux. La théorie de la généralisation --- biais-variance, VC-dimension, marges, complexité de Rademacher --- est traitée au même niveau de rigueur que les algorithmes, parce qu'elle est leur justification.

\medskip

\noindent\textbf{Prérequis.} Algèbre linéaire, probabilités, calcul différentiel, Python.

\vfill
\hfill\textit{L'auteur}""",

    "apprentissage-geometrique": r"""La plupart des architectures de deep learning classiques (CNN, RNN) ont une structure cachée : elles exploitent les symétries de leur domaine d'entrée. Une convolution est une opération invariante par translation ; un RNN est récurrent parce qu'une séquence a une géométrie temporelle. L'\emph{apprentissage géométrique profond}, formalisé par Bronstein, Bruna, Cohen et Veličković, prend cette observation au sérieux et la généralise : construire des réseaux dont l'architecture reflète directement la structure géométrique --- groupe de symétries, variété, graphe --- du domaine considéré.

\medskip

Ce cours avancé couvre les réseaux de neurones sur graphes (GCN, GAT, message passing), les architectures équivariantes, l'apprentissage sur variétés et nuages de points, et les liens avec l'analyse topologique des données. Les applications sont concrètes : chimie computationnelle, biologie structurale, robotique, traitement de signaux 3D.

\medskip

\noindent\textbf{Prérequis.} Deep learning (CNN, architectures de base), algèbre linéaire avancée, théorie des graphes, notions de géométrie différentielle.

\vfill
\hfill\textit{L'auteur}""",

    "apprentissage-renforcement": r"""L'apprentissage par renforcement (RL) résout une classe de problèmes que ni l'apprentissage supervisé ni l'apprentissage non supervisé ne savent traiter : apprendre à \emph{agir} dans un environnement qui répond. Un programme qui joue au Go contre lui-même, un robot qui apprend à marcher par essais, un système qui alloue dynamiquement des ressources réseau --- tous sont des instances du même cadre mathématique : un agent prenant des décisions séquentielles dans un processus de décision markovien.

\medskip

Ce cours part des fondements (MDP, équations de Bellman, programmation dynamique) et conduit aux algorithmes profonds modernes (DQN, gradients de politique, acteur-critique, PPO, SAC). Il couvre également le RL multi-agents, le RL sûr (safe RL), et les applications en robotique, jeux et contrôle. Le fil conducteur est la \emph{théorie des points fixes} : la plupart des algorithmes RL convergent parce qu'ils itèrent un opérateur contractant.

\medskip

\noindent\textbf{Prérequis.} Probabilités, algèbre linéaire, deep learning, programmation Python (PyTorch ou TensorFlow).

\vfill
\hfill\textit{L'auteur}""",

    "bases-donnees": r"""Toute application non triviale finit par avoir besoin d'une base de données. La question n'est pas \emph{si} mais \emph{laquelle}, et selon quel modèle. Le modèle relationnel, formalisé par Codd en 1970 et incarné par SQL, reste le standard pour 80 \% des cas. Les bases NoSQL --- documents, clé-valeur, colonnes larges, graphes --- répondent aux 20 \% restants, lorsque le schéma évolue trop vite, lorsque les jointures coûtent trop cher, ou lorsque l'application est massivement distribuée.

\medskip

Ce cours couvre les deux mondes : la modélisation entité-relation et l'algèbre relationnelle, le langage SQL (requêtes, jointures, agrégation, fenêtres), la normalisation (1NF à BCNF), les transactions ACID et leur affaiblissement BASE, l'indexation et les plans d'exécution, les pipelines ETL, et une introduction structurée aux quatre familles NoSQL.

\medskip

\noindent\textbf{Prérequis.} Programmation Python, notions de structures de données (listes, arbres, hachage).

\vfill
\hfill\textit{L'auteur}""",

    "edp": r"""Les équations aux dérivées partielles décrivent à peu près tout ce qui varie dans le temps et dans l'espace : la chaleur dans un solide, le son dans un fluide, le champ électromagnétique dans le vide, la population d'une espèce sur un territoire, le prix d'une option financière. Elles forment ainsi le langage commun de la physique mathématique, de la mécanique des milieux continus, de l'analyse stochastique et de la modélisation biologique.

\medskip

Ces notes présentent les équations classiques (transport, chaleur, ondes, Laplace) avec les méthodes fondamentales (séparation de variables, séries et transformée de Fourier, principe du maximum) puis les outils modernes (espaces de Sobolev, méthodes variationnelles, formulation faible). L'accent est placé sur l'articulation entre l'analyse classique et l'analyse fonctionnelle : on ne peut traiter sérieusement les EDP du second ordre sans Sobolev.

\medskip

\noindent\textbf{Prérequis.} Analyse réelle avancée, théorie de la mesure et espaces $L^p$, algèbre linéaire, notions d'analyse fonctionnelle.

\vfill
\hfill\textit{L'auteur}""",

    "finance-quantitative": r"""La finance quantitative ne consiste pas à prédire le prochain mouvement du marché --- chose dont une longue littérature montre qu'elle est essentiellement impossible. Elle consiste à modéliser le \emph{risque} : à quantifier ce qui peut arriver, avec quelle probabilité, à quel coût. L'édifice intellectuel a été construit en quarante ans, depuis le modèle de Black--Scholes (1973) jusqu'aux approches actuelles combinant calcul stochastique et machine learning.

\medskip

Ce cours couvre le modèle de Black--Scholes, le pricing et la couverture des options (européennes, américaines, exotiques), le calcul stochastique d'Itô, les modèles de volatilité (Heston, SABR), les modèles de taux (Vasicek, CIR, HJM), l'optimisation de portefeuille (Markowitz, Black--Litterman), les mesures de risque (VaR, Expected Shortfall) et les applications récentes du machine learning au pricing et à la détection d'anomalies.

\medskip

\noindent\textbf{Prérequis.} Probabilités à un niveau mesure-théorique, processus stochastiques (en particulier le mouvement brownien), analyse, programmation Python.

\vfill
\hfill\textit{L'auteur}""",

    "geometrie-riemannienne": r"""La géométrie riemannienne est née de la nécessité de faire de la géométrie sur des espaces courbes : surfaces de la Terre, surfaces minimales, variétés de l'espace-temps en relativité générale. Elle ajoute à une variété lisse la donnée d'une métrique --- un produit scalaire en chaque point qui varie régulièrement --- et c'est de cette donnée que dérive tout le reste : longueurs, angles, géodésiques, courbure.

\medskip

Ces notes développent la théorie des connexions de Levi-Civita, des géodésiques, de la courbure de Riemann, Ricci et scalaire, et culminent avec les grands théorèmes de comparaison (Bonnet--Myers, Cartan--Hadamard, Synge). Une introduction au flot de Ricci ferme le cours --- l'outil qui a permis à Perelman de démontrer la conjecture de Poincaré.

\medskip

\noindent\textbf{Prérequis.} Topologie différentielle (variétés lisses, applications différentiables), algèbre tensorielle, analyse réelle avancée.

\vfill
\hfill\textit{L'auteur}""",

    "mesure-integration": r"""L'intégrale de Riemann, enseignée en première année, présente un défaut subtil : elle ne se comporte pas bien avec les passages à la limite. La somme d'une série de fonctions Riemann-intégrables peut ne pas être Riemann-intégrable, et même quand elle l'est, intervertir somme et intégrale demande des hypothèses fortes. Lebesgue, au début du xx\textsuperscript{e} siècle, a refondé entièrement l'édifice à partir de la notion de mesure --- une généralisation de la longueur, de l'aire et du volume.

\medskip

Ce cours construit rigoureusement la théorie : $\sigma$-algèbres, mesures, théorème d'extension de Carathéodory, fonctions mesurables, intégrale de Lebesgue, théorèmes de convergence (Beppo Levi, Fatou, convergence dominée), espaces $L^p$ et leur dualité, théorème de Radon--Nikodym, théorème de Fubini--Tonelli. La théorie est essentielle à toute mathématique avancée : probabilités modernes, analyse harmonique, analyse fonctionnelle, équations aux dérivées partielles.

\medskip

\noindent\textbf{Prérequis.} Analyse réelle solide (suites, séries, continuité, topologie de $\R$).

\vfill
\hfill\textit{L'auteur}""",

    "mlops": r"""Un modèle de machine learning qui marche sur le notebook d'un data scientist n'est pas un produit. Pour qu'il devienne un produit, il faut le sortir du notebook, le déployer derrière une API, le surveiller en production, le mettre à jour quand les données dérivent, le rendre reproductible pour qu'un autre membre de l'équipe puisse l'auditer ou le relancer. C'est le rôle du MLOps : transformer un script qui s'exécute une fois en un système qui s'exécute correctement pendant des mois.

\medskip

Ces notes couvrent l'ensemble du pipeline : versioning de code et de données (Git, DVC), suivi d'expériences et registre de modèles (MLflow), pipelines de données, conteneurisation (Docker), déploiement (FastAPI, BentoML), CI/CD pour ML, monitoring (drift de données, drift de prédictions, dégradation), et reproductibilité. L'objectif est qu'à la fin du cours, l'étudiant puisse prendre un modèle entraîné en local et l'opérer pendant six mois sans qu'il casse silencieusement.

\medskip

\noindent\textbf{Prérequis.} Programmation Python solide, notions de machine learning, ligne de commande Linux, familiarité avec Git.

\vfill
\hfill\textit{L'auteur}""",

    "modelisation": r"""Modéliser, c'est choisir : choisir ce qu'on garde du monde et ce qu'on jette. Un bon modèle n'est pas celui qui décrit tout, mais celui qui décrit ce qui compte pour la question posée, et qui peut être étudié mathématiquement. Le modèle SIR à trois équations différentielles ordinaires a permis de prédire l'allure des grandes épidémies du xx\textsuperscript{e} siècle ; il n'a fallu ni neuronal ni big data pour cela, mais une décision de modélisation juste.

\medskip

Ce cours enseigne la pratique de la modélisation : passer d'un phénomène concret à un système mathématique tractable, l'analyser, le valider, et savoir quand le rejeter. Les exemples traversent la dynamique des populations, les modèles épidémiologiques (SIR, SEIR, modèles à compartiments), les équations de diffusion et de transport, les modèles stochastiques, et la modélisation économique et financière simple.

\medskip

\noindent\textbf{Prérequis.} Analyse réelle, algèbre linéaire, équations différentielles ordinaires.

\vfill
\hfill\textit{L'auteur}""",

    "optimisation-convexe": r"""La convexité est l'une des rares propriétés mathématiques où la théorie devient \emph{plus simple} à mesure qu'on l'approfondit. Un problème d'optimisation convexe a un optimum global, qui est en pratique calculable, et qu'on peut souvent caractériser par les conditions de Karush--Kuhn--Tucker. Ce fait fonde une grande partie de la statistique moderne (régression régularisée, SVM, méthodes spectrales), du machine learning (apprentissage profond passé par la convexité de la couche finale), et de l'optimisation industrielle.

\medskip

Ces notes couvrent les fondements théoriques (ensembles convexes, fonctions convexes, sous-différentiabilité, dualité de Lagrange et de Fenchel) puis les algorithmes les plus utilisés (méthodes de gradient, méthodes proximales, méthodes de points intérieurs). Chaque méthode est présentée avec sa preuve de convergence et une implémentation en Python.

\medskip

\noindent\textbf{Prérequis.} Algèbre linéaire, analyse réelle, calcul différentiel à plusieurs variables.

\vfill
\hfill\textit{L'auteur}""",

    "points-fixes": r"""Un théorème de point fixe affirme qu'une certaine transformation $T : X \to X$ laisse au moins un point invariant, c'est-à-dire qu'il existe $x \in X$ tel que $T(x) = x$. C'est une condition d'apparence inoffensive, mais c'est elle qui garantit l'existence des solutions de la plupart des équations différentielles, la convergence des algorithmes d'apprentissage par renforcement, l'équilibre de Nash en théorie des jeux, et bien d'autres résultats qui structurent les mathématiques modernes.

\medskip

Ce cours présente de manière unifiée les grands théorèmes : Banach (contraction métrique), Brouwer (continuité sur le disque), Schauder (extension à la dimension infinie), Kakutani (multi-applications convexes), Tarski--Knaster (treillis complets). Pour chacun : démonstration complète, généralisations dans les espaces métriques généralisés et les espaces ordonnés, et applications en analyse, en économie et en informatique. Une section finale couvre les développements récents : points fixes aléatoires, contractions interpolatives, contractions $\alpha$-admissibles.

\medskip

\noindent\textbf{Prérequis.} Topologie générale (compacité, connexité), analyse fonctionnelle de base.

\vfill
\hfill\textit{L'auteur}""",

    "probabilites": r"""La théorie des probabilités a longtemps vécu sans fondement rigoureux : Pascal, Fermat, Laplace, Poisson, Tchebychev ont produit des résultats profonds en s'appuyant sur des intuitions qu'aucun cadre formel ne validait. C'est Kolmogorov qui, en 1933, a unifié l'ensemble en une axiomatique fondée sur la théorie de la mesure : un espace probabilisé n'est rien d'autre qu'un espace mesuré de masse $1$, une variable aléatoire est une fonction mesurable, l'espérance est une intégrale.

\medskip

Ces notes adoptent ce point de vue dès le départ. Espaces probabilisés, variables aléatoires, lois classiques (uniforme, exponentielle, gaussienne, etc.), fonctions caractéristiques, indépendance, lois des grands nombres, théorème central limite, chaînes de Markov. Le but est de donner au lecteur les fondations sur lesquelles reposent les probabilités modernes, les statistiques inférentielles, et les processus stochastiques.

\medskip

\noindent\textbf{Prérequis.} Analyse réelle (suites, séries, intégration), notions de théorie de la mesure utiles mais non requises (un bref rappel est fourni).

\vfill
\hfill\textit{L'auteur}""",

    "processus-stochastiques": r"""Un processus stochastique est une famille de variables aléatoires indexée par le temps. Cette définition apparemment anodine cache une richesse considérable : il faut une mesure de probabilité sur un espace de \emph{trajectoires}, et la construction de cette mesure --- justifiée par le théorème de Kolmogorov --- est l'une des plus belles applications de la théorie de la mesure. Une fois ce cadre posé, on accède à toute la machinerie qui sous-tend la finance moderne, la physique statistique, la biologie des populations, et la mécanique quantique.

\medskip

Ces notes présentent les principaux processus : chaînes de Markov à temps discret et continu, processus de Poisson, martingales, mouvement brownien. Le cours aboutit à la construction de l'intégrale stochastique d'Itô, à la formule d'Itô, et à la résolution des équations différentielles stochastiques. L'exposition est rigoureuse, mesure-théorique, et débouche sur les applications modernes.

\medskip

\noindent\textbf{Prérequis.} Théorie de la mesure, probabilités à un niveau Kolmogorov, espérance conditionnelle.

\vfill
\hfill\textit{L'auteur}""",

    "recherche-operationnelle": r"""La recherche opérationnelle est née pendant la Seconde Guerre mondiale, lorsque les Alliés ont confié à des équipes de mathématiciens des questions opérationnelles : comment escorter un convoi de cargos, comment répartir les charges sur un avion, comment programmer la production d'usines. Le passage du temps de guerre au temps de paix a élargi les applications : logistique, planification de production, télécommunications, finance, transport. Le formalisme commun, lui, est resté : poser un problème comme l'optimisation d'une fonction sous contraintes, et le résoudre par un algorithme polynomial.

\medskip

Ces notes couvrent la programmation linéaire (algorithme du simplexe, dualité, post-optimalité), les problèmes de transport et d'affectation, les flots dans les réseaux (Ford--Fulkerson, Edmonds--Karp), la programmation en nombres entiers (branch and bound, plans coupants), et une introduction à la programmation dynamique. Chaque chapitre s'accompagne d'études de cas réelles et d'implémentations en Python.

\medskip

\noindent\textbf{Prérequis.} Algèbre linéaire, notions d'algorithmique, programmation Python.

\vfill
\hfill\textit{L'auteur}""",

    "statistique-bayesienne": r"""La statistique bayésienne traite la probabilité comme un degré de croyance et l'inférence comme une mise à jour de cette croyance à la lumière des données. Ce cadre, longtemps marginalisé pour des raisons calculatoires, a été remis au centre de la statistique appliquée par deux progrès parallèles : les méthodes MCMC, qui rendent calculables les distributions a posteriori difficiles, et la puissance informatique disponible. Aujourd'hui, l'approche bayésienne est dominante dans les modèles hiérarchiques (santé publique, épidémiologie, économétrie), dans l'inférence sur petits échantillons, et dans le machine learning probabiliste.

\medskip

Ce cours présente le paradigme : lois a priori et a posteriori, conjugaison, modèles hiérarchiques, méthodes MCMC (Metropolis--Hastings, Gibbs, NUTS), inférence variationnelle, modèles non-paramétriques (Dirichlet, processus gaussien). Les implémentations sont faites en \texttt{PyMC} et en \texttt{Stan}.

\medskip

\noindent\textbf{Prérequis.} Probabilités, statistique mathématique fréquentiste, programmation Python.

\vfill
\hfill\textit{L'auteur}""",

    "systemes-dynamiques": r"""Un système dynamique est une règle qui décrit comment un état évolue dans le temps. Cette définition très générale recouvre des objets aussi divers que les équations de Newton, les itérations d'une fonction sur l'intervalle $[0,1]$, les modèles de prédateur-proie, ou les flots géodésiques sur une variété riemannienne. Le miracle, mis en lumière au xx\textsuperscript{e} siècle, est que des systèmes très simples peuvent engendrer un comportement extrêmement complexe : c'est la découverte du \emph{chaos déterministe}.

\medskip

Ce cours couvre les systèmes continus et discrets, la stabilité linéaire et de Lyapunov, les bifurcations, les portraits de phase, les cycles limites, les exposants de Lyapunov, les attracteurs étranges (Lorenz, Hénon, Rössler), et conclut par une introduction à la théorie ergodique. Les exemples viennent de la mécanique, de la biologie, de l'économie, et du climat.

\medskip

\noindent\textbf{Prérequis.} Équations différentielles ordinaires, algèbre linéaire, analyse réelle.

\vfill
\hfill\textit{L'auteur}""",

    "tal-nlp": r"""Le traitement automatique des langues a connu trois révolutions en vingt ans : les méthodes statistiques de la fin des années 1990, les plongements distribués (Word2Vec, GloVe) du milieu des années 2010, et l'architecture Transformer (\textit{Attention Is All You Need}, 2017) qui a tout balayé. Les grands modèles de langage actuels --- GPT-4, Claude, Llama, Gemini --- sont les héritiers directs de cette dernière, à des échelles que personne n'imaginait il y a dix ans.

\medskip

Ce cours couvre les représentations classiques (n-grammes, TF-IDF), les plongements distribués, les modèles séquentiels (RNN, LSTM), l'architecture Transformer en détail, les modèles pré-entraînés et le fine-tuning, la génération de texte, le RAG (retrieval-augmented generation), et les enjeux éthiques (biais, hallucinations, désinformation). Une attention particulière est portée aux applications multilingues, et notamment aux langues africaines à ressources limitées.

\medskip

\noindent\textbf{Prérequis.} Probabilités, algèbre linéaire, deep learning de base, programmation Python (PyTorch).

\vfill
\hfill\textit{L'auteur}""",

    "tda": r"""L'analyse topologique des données (TDA) part d'une observation simple : les données ont une forme. Un nuage de points peut être étendu, courbé, troué, fragmenté ; ces propriétés de forme contiennent souvent une information que les statistiques sommaires (moyenne, variance, axes principaux) ratent. La TDA, formalisée à partir des années 2000 par Carlsson, Edelsbrunner, Ghrist et leurs collaborateurs, fournit les outils pour extraire cette information de manière mathématiquement rigoureuse et computationnellement tractable.

\medskip

Ces notes présentent le cœur de la discipline : complexes simpliciaux, homologie persistante, diagrammes et codes-barres de persistance, théorèmes de stabilité, algorithme Mapper, et intégration de la TDA dans des pipelines de machine learning (persistance landscapes, persistence images, deep persistence). Les applications traversent la biologie (protéines, neurones), la médecine (imagerie), la dynamique des systèmes et les séries temporelles.

\medskip

\noindent\textbf{Prérequis.} Topologie générale, algèbre linéaire, notions d'algèbre homologique (rappelées dans le texte), Python.

\vfill
\hfill\textit{L'auteur}""",

    "topologie-ponctuelle-avancee": r"""La topologie ponctuelle dont on enseigne habituellement les bases prend pour acquis le cadre des espaces de Hausdorff. Mais en informatique théorique --- sémantique dénotationnelle, théorie des domaines, analyse non standard --- on rencontre fréquemment des espaces dont la topologie ne sépare pas les points : domaines de Scott, locales, espaces sobres. La topologie asymétrique, où une distance peut ne pas être symétrique, joue un rôle similaire pour modéliser des processus irréversibles ou des préordres.

\medskip

Ce cours explore ces structures qui sortent du confort Hausdorff : espaces sobres et locales, domaines de Scott, topologie asymétrique, espaces bitopologiques, espaces de convergence. Le but est de donner un cadre théorique unifié à des objets qui sont apparus séparément en informatique, en analyse non standard et en théorie des points fixes généralisés.

\medskip

\noindent\textbf{Prérequis.} Topologie générale (espaces séparés, compacité, connexité), notions de théorie des catégories, théorie des ordres.

\vfill
\hfill\textit{L'auteur}""",
}


PREFACE_TEMPLATE = """\\chapter*{{Pr\\'eface}}
\\addcontentsline{{toc}}{{chapter}}{{Pr\\'eface}}
\\markboth{{Pr\\'eface}}{{Pr\\'eface}}

{body}

% ============================================================
"""


def has_preface(text: str) -> bool:
    return bool(re.search(r"\\chapter\*\{\s*Pr(?:é|\\'?e?)face\s*\}", text))


def insert_preface(text: str, body: str) -> str:
    block = PREFACE_TEMPLATE.format(body=body.strip())
    # Insert between \tableofcontents and \mainmatter.
    pattern = re.compile(
        r"(\\tableofcontents\s*(?:\\newpage\s*)?)(\s*)(\\mainmatter)",
        re.MULTILINE,
    )
    new, n = pattern.subn(lambda m: f"{m.group(1)}\n\n{block}\n{m.group(2)}{m.group(3)}", text, count=1)
    return new if n else text


def main() -> int:
    written, skipped, missing = 0, 0, []
    for slug, body in PREFACES_FR.items():
        path = REPO_ROOT / "courses" / slug / "fr" / "cours.tex"
        if not path.exists():
            missing.append(str(path))
            continue
        text = path.read_text(encoding="utf-8")
        if has_preface(text):
            print(f"  skipped  {slug}/fr  (already has a preface)")
            skipped += 1
            continue
        new_text = insert_preface(text, body)
        if new_text == text:
            print(f"  NO MATCH {slug}/fr  (no \\tableofcontents...\\mainmatter pair)", file=sys.stderr)
            continue
        path.write_text(new_text, encoding="utf-8")
        print(f"  wrote    {slug}/fr/cours.tex")
        written += 1

    print(f"\nDone. {written} prefaces inserted, {skipped} skipped.")
    if missing:
        print(f"\nMissing files: {', '.join(missing)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
