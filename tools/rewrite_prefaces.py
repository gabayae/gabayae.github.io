#!/usr/bin/env python3
"""
Rewrite the 21 v1 prefaces (added by add_prefaces.py) into story-mode v2.

Each v1 preface opened with a generic motivation ("L'analyse fonctionnelle
est née d'une contradiction..."). The v2 versions open on a concrete
moment, person, or publication that anchors the discipline historically.

Run from repo root:
    python tools/rewrite_prefaces.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Each entry is the full preface body (between \chapter*{Préface} and the
# closing \vfill\hfill\textit{L'auteur} sign-off). The script substitutes
# the body inline.
PREFACES_V2: dict[str, str] = {
    "analyse-fonctionnelle": r"""En 1906, Maurice Fr\'echet soutient sa th\`ese devant Jacques Hadamard et \'Emile Picard. Le titre, \emph{Sur quelques points du calcul fonctionnel}, para\^it anodin. Il y construit pourtant, pour la premi\`ere fois, une notion d'espace abstrait muni d'une distance, dont les \'el\'ements ne sont plus des points mais des fonctions. Soixante ans plus tard, l'analyse fonctionnelle qu'il vient d'amorcer aura fourni le langage de la m\'ecanique quantique, de la th\'eorie des distributions, et des \'equations aux d\'eriv\'ees partielles modernes.

\medskip

Le passage du fini au continu n'est pas qu'un changement d'\'echelle. Dans un espace de dimension infinie, la boule unit\'e n'est jamais compacte, deux normes \'equivalentes peuvent ne pas exister, et la notion m\^eme de convergence se d\'edouble entre topologie forte et topologie faible. Ce cours construit progressivement les outils qui ont permis de surmonter ces obstacles : espaces de Banach et de Hilbert, th\'eor\`emes fondamentaux (Hahn--Banach, Banach--Steinhaus, application ouverte, graphe ferm\'e), th\'eorie spectrale des op\'erateurs compacts et auto-adjoints.

\medskip

\noindent\textbf{Pr\'erequis.} Topologie g\'en\'erale (compacit\'e, convergence), th\'eorie de la mesure (espaces $L^p$), alg\`ebre lin\'eaire.""",

    "apprentissage-automatique": r"""En 1959, Arthur Samuel publie un article au titre presque trompeur : \emph{Some Studies in Machine Learning Using the Game of Checkers}. Le programme qu'il y d\'ecrit apprend \`a jouer aux dames en s'opposant \`a lui-m\^eme, et finit par battre des amateurs s\'erieux. C'est l'une des premi\`eres d\'emonstrations cr\'edibles qu'une machine peut am\'eliorer ses performances sans qu'on l'ait reprogramm\'ee --- l'expression \emph{machine learning} appara\^it pour la premi\`ere fois dans ce papier. Soixante-cinq ans plus tard, le machine learning a quitt\'e les laboratoires pour s'installer dans les banques, les h\^opitaux, les t\'el\'ephones et, plus discr\`etement, dans la fa\c{c}on dont sont d\'ecid\'ees les promotions, les pr\^ets bancaires, et les diagnostics.

\medskip

L'apprentissage automatique ne se r\'eduit pourtant ni \`a un catalogue d'algorithmes ni \`a une question d'optimisation. Son c\oe ur conceptuel est la \emph{g\'en\'eralisation} : la capacit\'e d'un mod\`ele entra\^in\'e sur un \'echantillon fini \`a se comporter correctement sur des donn\'ees qu'il n'a jamais vues. C'est cette question, et non l'astuce algorithmique du jour, qui s\'epare un syst\`eme qui tient en production d'un syst\`eme qui s'effondre au premier changement de distribution. Ces notes traitent la th\'eorie de la g\'en\'eralisation au m\^eme niveau de rigueur que les algorithmes, parce qu'elle en est la justification.

\medskip

\noindent\textbf{Pr\'erequis.} Alg\`ebre lin\'eaire, probabilit\'es, calcul diff\'erentiel, Python.""",

    "apprentissage-geometrique": r"""En 2021, Michael Bronstein, Joan Bruna, Taco Cohen et Petar Veli\v{c}kovi\'c publient un texte qu'ils intitulent un manifeste : \emph{Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges}. Leur th\`ese est d\'erangeante. Les architectures de deep learning qui ont marqu\'e la d\'ecennie pr\'ec\'edente (CNN, RNN, Transformer) ne sont pas une collection d'astuces empiriques --- elles partagent une structure cach\'ee. Toutes exploitent les sym\'etries de leur domaine d'entr\'ee : une convolution est invariante par translation, un RNN est r\'ecurrent parce qu'une s\'equence a une g\'eom\'etrie temporelle. Et toutes peuvent \^etre d\'eriv\'ees, plut\^ot que devin\'ees, \`a partir d'un seul principe : la sym\'etrie pr\'eserv\'ee par l'architecture.

\medskip

Ce cours avanc\'e prend ce point de vue au s\'erieux. R\'eseaux de neurones sur graphes (GCN, GAT, message passing), architectures \'equivariantes, apprentissage sur vari\'et\'es et nuages de points, et liens avec l'analyse topologique des donn\'ees. Les applications sont concr\`etes : chimie computationnelle, biologie structurale (AlphaFold appartient \`a cette famille), robotique, traitement de signaux 3D.

\medskip

\noindent\textbf{Pr\'erequis.} Deep learning (CNN, architectures de base), alg\`ebre lin\'eaire avanc\'ee, th\'eorie des graphes, notions de g\'eom\'etrie diff\'erentielle.""",

    "apprentissage-renforcement": r"""En 1898, Edward Thorndike enferme un chat dans une bo\^ite \`a probl\`emes. Le chat doit tirer un cordon pour s'\'echapper. \`A la premi\`ere tentative, il met plusieurs minutes ; \`a la dixi\`eme, quelques secondes ; \`a la centi\`eme, il s'\'echappe imm\'ediatement. Thorndike formule \`a partir de cette exp\'erience la \emph{loi de l'effet}~: les actions suivies de cons\'equences favorables deviennent plus probables. Quatre-vingts ans plus tard, Richard Sutton et Andy Barto reformulent cette m\^eme intuition dans le langage des processus de d\'ecision markoviens, et donnent naissance au cadre math\'ematique qui sous-tend AlphaGo, les voitures autonomes, et la plupart des syst\`emes d'IA qui agissent dans un environnement plut\^ot que de simplement le pr\'edire.

\medskip

Ce cours part des fondements (MDP, \'equations de Bellman, programmation dynamique) et conduit aux algorithmes profonds modernes (DQN, gradients de politique, acteur-critique, PPO, SAC). Il couvre \'egalement le RL multi-agents, le RL s\^ur, et les applications en robotique, jeux et contr\^ole. Le fil conducteur math\'ematique est la th\'eorie des points fixes~: la plupart des algorithmes de RL convergent parce qu'ils it\`erent un op\'erateur contractant.

\medskip

\noindent\textbf{Pr\'erequis.} Probabilit\'es, alg\`ebre lin\'eaire, deep learning, programmation Python (PyTorch ou TensorFlow).""",

    "bases-donnees": r"""En juin 1970, Edgar F. Codd, chercheur \`a IBM, publie un article de douze pages dans les \emph{Communications of the ACM}. Le titre, \emph{A Relational Model of Data for Large Shared Data Banks}, ne pr\'edit rien de ce qui va suivre. \`A l'\'epoque, les bases de donn\'ees sont hi\'erarchiques, propri\'etaires, accessibles via des langages de programmation sp\'ecifiques. Codd propose l'inverse~: une donn\'ee est un n-uplet dans une relation, et les requ\^etes se formulent dans un langage alg\'ebrique ind\'ependant de l'impl\'ementation physique. Cinquante-cinq ans plus tard, SQL --- direct descendant de ce papier --- reste le langage avec lequel la quasi-totalit\'e des donn\'ees structur\'ees du monde est interrog\'ee.

\medskip

Ce cours couvre les deux mondes : le mod\`ele relationnel (mod\'elisation entit\'e-relation, alg\`ebre, SQL, normalisation jusqu'\`a BCNF, transactions ACID, indexation, plans d'ex\'ecution) et les bases NoSQL n\'ees apr\`es 2005 pour les cas o\`u le sch\'ema \'evolue trop vite, o\`u les jointures co\^utent trop cher, ou o\`u l'application est massivement distribu\'ee.

\medskip

\noindent\textbf{Pr\'erequis.} Programmation Python, notions de structures de donn\'ees (listes, arbres, hachage).""",

    "edp": r"""En 1822, Joseph Fourier publie \emph{Th\'eorie analytique de la chaleur}. Le texte choque l'Acad\'emie des sciences. Fourier y affirme qu'une fonction arbitraire peut \^etre repr\'esent\'ee par une s\'erie infinie de sinus et cosinus, et utilise cette d\'ecomposition pour r\'esoudre l'\'equation de la chaleur dans une barre. Lagrange et Laplace, dans le comit\'e de lecture, refusent d'abord la publication --- les s\'eries de Fourier paraissent trop irr\'eguli\`eres pour exister rigoureusement. Elles existent, on le sait maintenant ; mais leur \'etude rigoureuse a occup\'e les math\'ematiques pendant tout le si\`ecle suivant.

\medskip

Les \'equations aux d\'eriv\'ees partielles d\'ecrivent \`a peu pr\`es tout ce qui varie dans le temps et dans l'espace : la chaleur dans un solide, le son dans un fluide, le champ \'electromagn\'etique, la population d'une esp\`ece, le prix d'une option financi\`ere. Ces notes pr\'esentent les \'equations classiques (transport, chaleur, ondes, Laplace) avec les m\'ethodes fondamentales (s\'eparation de variables, s\'eries et transform\'ee de Fourier, principe du maximum) puis les outils modernes (espaces de Sobolev, m\'ethodes variationnelles, formulation faible). L'accent est plac\'e sur l'articulation entre analyse classique et analyse fonctionnelle.

\medskip

\noindent\textbf{Pr\'erequis.} Analyse r\'eelle avanc\'ee, th\'eorie de la mesure et espaces $L^p$, alg\`ebre lin\'eaire, notions d'analyse fonctionnelle.""",

    "finance-quantitative": r"""En 1973, deux articles para\^issent \`a quelques mois d'intervalle. Fischer Black et Myron Scholes proposent dans le \emph{Journal of Political Economy} une formule pour le prix d'une option europ\'eenne. Robert Merton, ind\'ependamment, publie dans le \emph{Bell Journal} une g\'en\'eralisation. Black, Scholes et Merton recevront pour cela le prix de la Banque de Su\`ede en 1997. Black, mort entre-temps, ne le recevra qu'\`a titre posthume. Mais l'effet sur la finance avait \'et\'e quasi imm\'ediat : d\`es 1974, le Chicago Board Options Exchange utilisait la formule pour coter les options en temps r\'eel, et l'\'edifice de la finance quantitative moderne s'est b\^ati par-dessus.

\medskip

La finance quantitative ne consiste pas \`a pr\'edire le prochain mouvement du march\'e --- chose dont on sait depuis Bachelier que c'est essentiellement impossible. Elle consiste \`a mod\'eliser le \emph{risque} : quantifier ce qui peut arriver, avec quelle probabilit\'e, \`a quel co\^ut. Ce cours couvre Black--Scholes, le pricing et la couverture d'options, le calcul stochastique d'It\^o, les mod\`eles de volatilit\'e (Heston, SABR) et de taux (Vasicek, HJM), l'optimisation de portefeuille, les mesures de risque (VaR, ES), et les applications r\'ecentes du ML.

\medskip

\noindent\textbf{Pr\'erequis.} Probabilit\'es \`a un niveau mesure-th\'eorique, processus stochastiques (mouvement brownien), analyse, Python.""",

    "geometrie-riemannienne": r"""Le 10 juin 1854, Bernhard Riemann soutient devant Gauss son habilitation \`a Göttingen. Le sujet impos\'e par Gauss --- \emph{\"Uber die Hypothesen, welche der Geometrie zu Grunde liegen} --- demande \`a Riemann d'exposer les fondements de la g\'eom\'etrie. L'expos\'e, prononc\'e devant une assembl\'ee qui n'en saisit pas la port\'ee, propose ce qu'on appelle aujourd'hui la \emph{vari\'et\'e riemannienne}~: un espace courbe arbitraire muni d'une m\'etrique infinit\'esimale. Soixante ans plus tard, Einstein y reconna\^it le cadre math\'ematique exact dont il avait besoin pour la relativit\'e g\'en\'erale.

\medskip

Ces notes d\'eveloppent la th\'eorie des connexions de Levi-Civita, des g\'eod\'esiques, de la courbure de Riemann, Ricci et scalaire, et culminent avec les grands th\'eor\`emes de comparaison (Bonnet--Myers, Cartan--Hadamard, Synge). Une introduction au flot de Ricci ferme le cours --- l'outil qui a permis \`a Perelman de d\'emontrer la conjecture de Poincar\'e en 2003.

\medskip

\noindent\textbf{Pr\'erequis.} Topologie diff\'erentielle (vari\'et\'es lisses, applications diff\'erentiables), alg\`ebre tensorielle, analyse r\'eelle avanc\'ee.""",

    "mesure-integration": r"""L'int\'egrale de Riemann, qu'on enseigne en premi\`ere ann\'ee, a un d\'efaut que les g\'en\'erations d'\'etudiants apprennent en deuxi\`eme ann\'ee. Elle ne se comporte pas bien avec les passages \`a la limite. La somme d'une s\'erie de fonctions Riemann-int\'egrables peut ne pas \^etre Riemann-int\'egrable, et m\^eme quand elle l'est, intervertir somme et int\'egrale demande des hypoth\`eses fortes. En 1902, dans sa th\`ese soutenue \`a la Sorbonne, Henri Lebesgue refond enti\`erement l'\'edifice. L'id\'ee est simple en r\'etrospective~: au lieu de d\'ecouper l'axe des $x$, on d\'ecoupe l'axe des $y$. Les passages \`a la limite deviennent alors quasi automatiques, gr\^ace aux trois th\'eor\`emes de convergence qui portent encore son nom.

\medskip

Ce cours construit rigoureusement la th\'eorie : $\sigma$-alg\`ebres, mesures, th\'eor\`eme d'extension de Carath\'eodory, fonctions mesurables, int\'egrale de Lebesgue, th\'eor\`emes de convergence (Beppo Levi, Fatou, convergence domin\'ee), espaces $L^p$ et dualit\'e, th\'eor\`eme de Radon--Nikodym, th\'eor\`eme de Fubini--Tonelli. La th\'eorie est essentielle \`a toute math\'ematique avanc\'ee : probabilit\'es modernes, analyse harmonique, analyse fonctionnelle, \'equations aux d\'eriv\'ees partielles.

\medskip

\noindent\textbf{Pr\'erequis.} Analyse r\'eelle solide (suites, s\'eries, continuit\'e, topologie de $\R$).""",

    "mlops": r"""En 2015, des ing\'enieurs de Google publient un article devenu c\'el\`ebre dans la communaut\'e ML : \emph{Hidden Technical Debt in Machine Learning Systems}. L'article tient en quelques pages, mais le diagramme central est rest\'e. Au milieu, un petit carr\'e marqu\'e <<~ML code~>>. Autour, une douzaine de gros blocs : pipelines de donn\'ees, monitoring, configuration, infrastructure, analyse, gestion de versions. La l\'egende est implicite~: le code du mod\`ele est la partie minoritaire d'un syst\`eme ML en production. Tout le reste --- ce qu'on appelle aujourd'hui MLOps --- est ce qui d\'etermine si le mod\`ele continue de fonctionner correctement six mois apr\`es son d\'eploiement, ou s'il s'effondre silencieusement.

\medskip

Ces notes couvrent l'ensemble du pipeline~: versioning de code et de donn\'ees (Git, DVC), suivi d'exp\'eriences et registre de mod\`eles (MLflow), conteneurisation (Docker), d\'eploiement (FastAPI, BentoML), CI/CD pour ML, monitoring (drift de donn\'ees, drift de pr\'edictions), et reproductibilit\'e. L'objectif est qu'\`a la fin du cours, l'\'etudiant puisse prendre un mod\`ele entra\^in\'e en local et l'op\'erer pendant six mois sans qu'il casse silencieusement.

\medskip

\noindent\textbf{Pr\'erequis.} Programmation Python solide, notions de machine learning, ligne de commande Linux, Git.""",

    "modelisation": r"""En 1927, William Ogilvy Kermack, biochimiste, et Anderson Gray McKendrick, m\'edecin militaire, publient dans les \emph{Proceedings of the Royal Society} un mod\`ele \`a trois \'equations diff\'erentielles ordinaires. Le mod\`ele d\'ecrit comment une \'epid\'emie se r\'epand dans une population qu'il divise en trois compartiments~: susceptibles, infect\'es, retir\'es. Le mod\`ele SIR, comme on l'appelle aujourd'hui, n'utilise ni big data ni r\'eseau de neurones. Il utilise une d\'ecision de mod\'elisation~: trois compartiments, deux taux. Quatre-vingt-quinze ans plus tard, c'est encore par ce mod\`ele que d\'ebute toute analyse d'\'epid\'emie, du COVID-19 \`a la grippe saisonni\`ere.

\medskip

Mod\'eliser, c'est choisir ce qu'on garde du monde et ce qu'on jette. Un bon mod\`ele n'est pas celui qui d\'ecrit tout, mais celui qui d\'ecrit ce qui compte pour la question pos\'ee, et qui peut \^etre \'etudi\'e math\'ematiquement. Ce cours enseigne la pratique de la mod\'elisation~: passer d'un ph\'enom\`ene concret \`a un syst\`eme math\'ematique tractable, l'analyser, le valider, et savoir quand le rejeter. Les exemples traversent la dynamique des populations, l'\'epid\'emiologie, les \'equations de diffusion et de transport, les mod\`eles stochastiques, et la mod\'elisation \'economique.

\medskip

\noindent\textbf{Pr\'erequis.} Analyse r\'eelle, alg\`ebre lin\'eaire, \'equations diff\'erentielles ordinaires.""",

    "optimisation-convexe": r"""\`A l'\'et\'e 1947, George Dantzig, statisticien de 33 ans rentr\'e de l'arm\'ee am\'ericaine, met au point au Pentagone un algorithme pour r\'esoudre un probl\`eme d'allocation de ressources. Il l'appelle \emph{simplex method}. Dantzig pense l'avoir invent\'e pour un usage strictement militaire. Soixante-quinze ans plus tard, l'algorithme du simplexe r\'esout chaque jour, dans des banques, des compagnies a\'eriennes, des usines et des centres logistiques, plusieurs millions de probl\`emes d'optimisation lin\'eaire. La convexit\'e est l'une des rares propri\'et\'es math\'ematiques o\`u la th\'eorie devient \emph{plus simple} \`a mesure qu'on l'approfondit~: un probl\`eme d'optimisation convexe a un optimum global, et il est en pratique calculable.

\medskip

Ces notes couvrent les fondements th\'eoriques (ensembles et fonctions convexes, sous-diff\'erentiabilit\'e, dualit\'e de Lagrange et de Fenchel) puis les algorithmes les plus utilis\'es (m\'ethodes de gradient, m\'ethodes proximales, m\'ethodes de points int\'erieurs). Chaque m\'ethode est pr\'esent\'ee avec sa preuve de convergence et une impl\'ementation en Python.

\medskip

\noindent\textbf{Pr\'erequis.} Alg\`ebre lin\'eaire, analyse r\'eelle, calcul diff\'erentiel \`a plusieurs variables.""",

    "points-fixes": r"""En 1922, Stefan Banach, alors enseignant \`a Lw\'ow, publie dans \emph{Fundamenta Mathematicae} un th\'eor\`eme qui tient en deux lignes~: une application contractante d'un espace m\'etrique complet dans lui-m\^eme admet un unique point fixe, et la suite des it\'er\'es y converge. La preuve fait quelques lignes. L'\'enonc\'e est presque tautologique. Et pourtant, c'est ce th\'eor\`eme qui garantit, un si\`ecle plus tard, l'existence des solutions de la plupart des \'equations diff\'erentielles, la convergence des algorithmes d'apprentissage par renforcement, et bien d'autres r\'esultats qui structurent les math\'ematiques modernes.

\medskip

Ce cours pr\'esente de mani\`ere unifi\'ee les grands th\'eor\`emes de points fixes~: Banach, Brouwer (continuit\'e sur le disque), Schauder (dimension infinie), Kakutani (multi-applications, fondamental pour l'\'equilibre de Nash), Tarski--Knaster (treillis complets). Pour chacun~: d\'emonstration compl\`ete, g\'en\'eralisations dans les espaces m\'etriques g\'en\'eralis\'es et les ensembles ordonn\'es, et applications. Une section finale couvre les d\'eveloppements r\'ecents~: points fixes al\'eatoires, contractions interpolatives, contractions $\alpha$-admissibles.

\medskip

\noindent\textbf{Pr\'erequis.} Topologie g\'en\'erale (compacit\'e, connexit\'e), analyse fonctionnelle de base.""",

    "probabilites": r"""Avant 1933, la th\'eorie des probabilit\'es ressemble \`a un \'edifice somptueux construit sans fondations. Pascal et Fermat, Laplace, Poisson, Tchebychev, Markov ont produit des r\'esultats profonds en s'appuyant sur des intuitions que personne n'a r\'eussi \`a formaliser. La situation devient embarrassante~: deux probabilistes peuvent calculer la m\^eme quantit\'e de fa\c{c}on diff\'erente et obtenir des r\'eponses contradictoires. En 1933, dans un mince volume intitul\'e \emph{Grundbegriffe der Wahrscheinlichkeitsrechnung}, Andrei Kolmogorov unifie l'ensemble en quatre axiomes. Un espace probabilis\'e n'est rien d'autre qu'un espace mesur\'e de masse 1, une variable al\'eatoire est une fonction mesurable, l'esp\'erance est une int\'egrale.

\medskip

Ces notes adoptent ce point de vue d\`es le d\'epart. Espaces probabilis\'es, variables al\'eatoires, lois classiques (uniforme, exponentielle, gaussienne), fonctions caract\'eristiques, ind\'ependance, lois des grands nombres, th\'eor\`eme central limite, cha\^ines de Markov. Le but est de donner au lecteur les fondations sur lesquelles reposent les probabilit\'es modernes, les statistiques inf\'erentielles, et les processus stochastiques.

\medskip

\noindent\textbf{Pr\'erequis.} Analyse r\'eelle (suites, s\'eries, int\'egration), notions de th\'eorie de la mesure utiles mais non requises.""",

    "processus-stochastiques": r"""En 1944, dans le Japon de l'apr\`es-guerre, Kiyosi It\^o publie un papier qui passe largement inaper\c{c}u : \emph{Stochastic Integral}. Le mouvement brownien, d\'ecouvert un demi-si\`ecle plus t\^ot par Robert Brown et formalis\'e par Wiener, a la propri\'et\'e fr\^ole d'\^etre nulle part diff\'erentiable~; on ne peut donc pas l'int\'egrer au sens habituel. It\^o invente une nouvelle int\'egrale, avec sa propre formule de d\'erivation. Trente ans plus tard, sa formule sera au c\oe ur de Black--Scholes ; et l'int\'egrale d'It\^o sera devenue l'outil de base de la finance moderne, de la physique statistique, et de la biologie th\'eorique.

\medskip

Un processus stochastique est une famille de variables al\'eatoires index\'ee par le temps. Cette d\'efinition apparemment anodine cache une richesse consid\'erable~: il faut une mesure de probabilit\'e sur un espace de \emph{trajectoires}, et la construction de cette mesure --- justifi\'ee par le th\'eor\`eme de Kolmogorov --- est l'une des plus belles applications de la th\'eorie de la mesure. Ces notes pr\'esentent les principaux processus~: cha\^ines de Markov, processus de Poisson, martingales, mouvement brownien. Le cours aboutit \`a l'int\'egrale d'It\^o, \`a sa formule, et aux \'equations diff\'erentielles stochastiques.

\medskip

\noindent\textbf{Pr\'erequis.} Th\'eorie de la mesure, probabilit\'es \`a un niveau Kolmogorov, esp\'erance conditionnelle.""",

    "recherche-operationnelle": r"""\`A l'\'et\'e 1940, alors que la \emph{Battle of Britain} fait rage, l'\'etat-major britannique cr\'ee discr\`etement un petit groupe charg\'e d'analyser l'usage des nouveaux radars. Le groupe, men\'e par Patrick Blackett, applique des m\'ethodes math\'ematiques \`a des questions strictement op\'erationnelles~: combien d'avions affecter \`a un convoi, quelle taille minimale pour qu'un convoi soit s\^ur, comment programmer la production d'avions. L'efficacit\'e du travail est telle qu'\`a la fin de la guerre, l'arm\'ee britannique poss\`ede une discipline qu'elle vient d'inventer : la \emph{recherche op\'erationnelle}. Apr\`es-guerre, elle migre vers l'industrie. Aujourd'hui, c'est elle qui d\'ecide comment Amazon route ses colis et comment Air France compose ses rotations d'\'equipage.

\medskip

Ces notes couvrent la programmation lin\'eaire (algorithme du simplexe, dualit\'e, post-optimalit\'e), les probl\`emes de transport et d'affectation, les flots dans les r\'eseaux (Ford--Fulkerson, Edmonds--Karp), la programmation en nombres entiers (branch and bound, plans coupants), et une introduction \`a la programmation dynamique. Chaque chapitre s'accompagne d'\'etudes de cas r\'eelles et d'impl\'ementations en Python.

\medskip

\noindent\textbf{Pr\'erequis.} Alg\`ebre lin\'eaire, notions d'algorithmique, programmation Python.""",

    "statistique-bayesienne": r"""En 1761, Thomas Bayes meurt sans avoir publi\'e son article principal. Deux ans plus tard, son ami Richard Price retrouve le manuscrit, l'envoie \`a la Royal Society, et le titre --- \emph{An Essay towards Solving a Problem in the Doctrine of Chances} --- entre dans l'histoire. Pendant deux si\`ecles, la formule de Bayes reste un curieux r\'esultat de probabilit\'es, sans m\'ethode g\'en\'erale pour l'appliquer aux probl\`emes r\'eels. Tout change \`a la fin des ann\'ees 1980, avec deux progr\`es parall\`eles~: les m\'ethodes MCMC, qui rendent calculables les distributions a posteriori complexes ; et l'arriv\'ee d'une puissance informatique qui rend ces calculs faisables en pratique. Aujourd'hui, l'approche bay\'esienne est dominante en \'epid\'emiologie, en \'econom\'etrie, dans les essais cliniques adaptatifs et dans la plupart du machine learning probabiliste.

\medskip

Ce cours pr\'esente le paradigme~: lois a priori et a posteriori, conjugaison, mod\`eles hi\'erarchiques, m\'ethodes MCMC (Metropolis--Hastings, Gibbs, NUTS), inf\'erence variationnelle, mod\`eles non-param\'etriques (Dirichlet, processus gaussien). Les impl\'ementations sont faites en \texttt{PyMC} et en \texttt{Stan}.

\medskip

\noindent\textbf{Pr\'erequis.} Probabilit\'es, statistique math\'ematique fr\'equentiste, programmation Python.""",

    "systemes-dynamiques": r"""Le 14 d\'ecembre 1962, Edward Lorenz, m\'et\'eorologue au MIT, fait tourner sur son ordinateur un mod\`ele de convection atmosph\'erique \`a trois \'equations diff\'erentielles ordinaires. Il interrompt la simulation pour aller prendre un caf\'e, et la relance en r\'eintroduisant comme conditions initiales les valeurs que son programme avait imprim\'ees \`a l'\'ecran. Il s'attend \`a retrouver la m\^eme trajectoire. Il retrouve quelque chose de compl\`etement diff\'erent. L'erreur d'arrondi due \`a la troncature de l'affichage --- trois chiffres au lieu de six --- avait suffi \`a faire diverger la simulation. Lorenz vient de red\'ecouvrir, dans un mod\`ele simple, le \emph{chaos d\'eterministe} : trois \'equations parfaitement d\'eterministes peuvent produire un comportement essentiellement impr\'evisible \`a moyen terme. C'est l'origine du << papillon >>.

\medskip

Ce cours couvre les syst\`emes continus et discrets, la stabilit\'e lin\'eaire et de Lyapunov, les bifurcations, les portraits de phase, les cycles limites, les exposants de Lyapunov, les attracteurs \'etranges (Lorenz, H\'enon, R\"ossler), et conclut par une introduction \`a la th\'eorie ergodique. Les exemples viennent de la m\'ecanique, de la biologie, de l'\'economie, et du climat.

\medskip

\noindent\textbf{Pr\'erequis.} \'Equations diff\'erentielles ordinaires, alg\`ebre lin\'eaire, analyse r\'eelle.""",

    "tal-nlp": r"""Le traitement automatique des langues a connu trois r\'evolutions en vingt ans, et chacune a annul\'e une partie de ce que la pr\'ec\'edente avait construit. En 1995, Frederick Jelinek, alors chez IBM, prononce sa phrase devenue c\'el\`ebre~: << Chaque fois que je vire un linguiste, la performance de notre syst\`eme de reconnaissance de la parole monte. >> Les m\'ethodes statistiques --- n-grammes, HMM, mod\`eles probabilistes --- remplacent les analyses grammaticales. En 2013, Mikolov publie Word2Vec et les plongements distribu\'es prennent le relais. En 2017, Vaswani et ses sept co-auteurs publient \emph{Attention Is All You Need}, et l'architecture Transformer balaie tout ce qui pr\'ec\'edait. GPT, Claude, LLaMA, Gemini sont les h\'eritiers directs de cette derni\`ere r\'evolution, \`a des \'echelles que personne, en 2017, n'imaginait.

\medskip

Ce cours couvre les repr\'esentations classiques (n-grammes, TF-IDF), les plongements (Word2Vec, GloVe, FastText), les mod\`eles s\'equentiels (RNN, LSTM), l'architecture Transformer en d\'etail, les mod\`eles pr\'e-entra\^in\'es et le fine-tuning, la g\'en\'eration de texte, le RAG, et les enjeux \'ethiques (biais, hallucinations, d\'esinformation). Une attention particuli\`ere est port\'ee aux langues africaines \`a ressources limit\'ees.

\medskip

\noindent\textbf{Pr\'erequis.} Probabilit\'es, alg\`ebre lin\'eaire, deep learning de base, Python (PyTorch).""",

    "tda": r"""En 2009, Gunnar Carlsson, math\'ematicien \`a Stanford, publie dans le \emph{Bulletin of the AMS} un article intitul\'e simplement \emph{Topology and Data}. Le projet qu'il y d\'ecrit semble \`a contre-courant. La science des donn\'ees, en pleine explosion gr\^ace au deep learning, s'oriente vers des m\'ethodes statistiques et g\'eom\'etriques fines. Carlsson propose l'inverse~: regarder ce qu'on peut apprendre des donn\'ees en n'utilisant que leur \emph{topologie}, c'est-\`a-dire ce qui reste invariant par d\'eformation continue. Un trou est un trou, qu'on \'etire les donn\'ees ou pas. Un nombre de composantes connexes est ce qu'il est, ind\'ependamment de la m\'etrique choisie. Quinze ans plus tard, l'analyse topologique des donn\'ees est devenue un outil utilis\'e en biologie structurale, en neurosciences, en mat\'eriaux, et en finance.

\medskip

Ces notes pr\'esentent le c\oe ur de la discipline~: complexes simpliciaux, homologie persistante, diagrammes et codes-barres de persistance, th\'eor\`emes de stabilit\'e, algorithme Mapper, et int\'egration de la TDA dans des pipelines de machine learning (persistence landscapes, persistence images, deep persistence). Les applications traversent la biologie, la m\'edecine, la dynamique des syst\`emes et les s\'eries temporelles.

\medskip

\noindent\textbf{Pr\'erequis.} Topologie g\'en\'erale, alg\`ebre lin\'eaire, notions d'alg\`ebre homologique, Python.""",

    "topologie-ponctuelle-avancee": r"""Dans les ann\'ees 1960, Dana Scott, alors \`a Oxford, cherche un mod\`ele math\'ematique pour le \emph{$\lambda$-calcul} de Church --- un syst\`eme formel o\`u une fonction peut prendre une fonction comme argument et se prendre elle-m\^eme comme argument. Le probl\`eme est ancien et r\'eput\'e insoluble dans la th\'eorie des ensembles classique. Scott le r\'esout en 1969 en introduisant les \emph{Scott domains}~: des espaces topologiques o\`u la topologie n'est pas la m\^eme dans les deux sens, o\`u tous les points ne sont pas s\'eparables, et o\`u la convergence est dirig\'ee. Quarante ans plus tard, c'est sur ces espaces que repose la s\'emantique d\'enotationnelle des langages de programmation modernes --- de Haskell aux assistants de preuve.

\medskip

La topologie ponctuelle qu'on enseigne habituellement prend pour acquis le cadre des espaces de Hausdorff. Ce cours explore les structures qui sortent du confort Hausdorff~: espaces sobres et locales, domaines de Scott, topologie asym\'etrique, espaces bitopologiques, espaces de convergence. Le but est de donner un cadre th\'eorique unifi\'e \`a des objets qui sont apparus s\'epar\'ement en informatique, en analyse non standard et en th\'eorie des points fixes g\'en\'eralis\'es.

\medskip

\noindent\textbf{Pr\'erequis.} Topologie g\'en\'erale (espaces s\'epar\'es, compacit\'e, connexit\'e), notions de th\'eorie des cat\'egories, th\'eorie des ordres.""",
}


# Boundary detection: from \chapter*{Préface}/Pr\'eface block to the closing
# \vfill\hfill\textit{L'auteur}.
PREFACE_BLOCK_RE = re.compile(
    r"(\\chapter\*\{\s*Pr(?:é|\\'?e?)face\s*\}\s*\\addcontentsline\{toc\}\{chapter\}\{[^}]+\}\s*\\markboth\{[^}]+\}\{[^}]+\}\s*\n+)"
    r"(.*?)"
    r"(\n\s*\\vfill\s*\\hfill\\textit\{L'auteur\})",
    re.DOTALL,
)


def main() -> int:
    written = 0
    misses = []
    for slug, body in PREFACES_V2.items():
        path = REPO_ROOT / "courses" / slug / "fr" / "cours.tex"
        if not path.exists():
            misses.append(slug + " (no file)")
            continue
        text = path.read_text(encoding="utf-8")
        def _sub(m: re.Match, b=body) -> str:
            return f"{m.group(1)}{b.strip()}{m.group(3)}"
        new_text, n = PREFACE_BLOCK_RE.subn(_sub, text, count=1)
        if n == 0:
            misses.append(slug + " (regex miss)")
            continue
        path.write_text(new_text, encoding="utf-8")
        print(f"  rewrote   {slug}/fr/cours.tex")
        written += 1
    print(f"\nDone. {written} prefaces rewritten.")
    if misses:
        print(f"Misses: {misses}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
