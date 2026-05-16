---
layout: page
permalink: /workshops/ml-ai-bootcamp/fr/
title: "Bootcamp Machine Learning & IA — Programme"
description: "Programme en cohorte AIRINA Labs. 10 semaines à temps plein / 20 semaines à temps partiel. Dix modules, de Python au MLOps, capstone, portfolio."
lang: fr
---

**Programme :** Bootcamp Machine Learning &amp; IA — *Une approche par la pratique*
**Opéré par :** [AIRINA Labs](https://github.com/AI-Technipreneurs)
**Instructeur principal :** Dr. Yaé Ulrich Gaba
**Format :** 100 % en ligne, synchrone, en cohorte
**Langue :** Anglais (cohorte FR disponible sur demande)
**Cadence :** 10 semaines à temps plein ou 20 semaines à temps partiel
**Taille de cohorte :** 12 à 24 participants par session

**Pages opérationnelles.** &nbsp; [Calendrier hebdomadaire]({{ '/workshops/ml-ai-bootcamp/fr/schedule/' | relative_url }}) &nbsp;|&nbsp; [Brief du capstone]({{ '/workshops/ml-ai-bootcamp/CAPSTONE/' | relative_url }})

---

En janvier 2023, BioNTech a racheté InstaDeep — une entreprise d'apprentissage automatique fondée à Tunis et exploitant des bureaux à Lagos, Nairobi et Paris — pour 562 millions de dollars. L'opération a rendu public ce que les recruteurs du secteur en Afrique observaient depuis plusieurs années : la demande mondiale d'ingénieurs ML déployables en production dépasse très largement l'offre formée, et l'écart est plus marqué sur le continent qu'ailleurs. La plupart des cursus universitaires africains en informatique se terminent avant le deep learning ; les MOOC qui comblent le vide sont calibrés pour des prérequis nord-américains et supposent généralement un premier emploi en ingénierie logicielle. Ce bootcamp cible exactement ce trou. Il prend des diplômés quantitatifs — mathématiques, statistique, informatique, finance quantitative, génie scientifique — et les amène en dix semaines au niveau de mise en production que recherchent les équipes ML africaines et internationales qui les recrutent.

---

## Le programme en bref

| | |
|---|---|
| **Sessions en direct** | 60+ |
| **Projet capstone** | 1 (en équipe ou individuel) |
| **Intervenants industriels** | 8 |
| **Heures de cours** | 200 |
| **Étude personnelle (TP)** | 20 heures / semaine |
| **Étude personnelle (T.partiel)** | 10 heures / semaine |
| **Permanences** | Hebdomadaires, avec assistants d'enseignement |
| **Livrable final** | Capstone déployé + pièce de portfolio |
| **Certificat** | Oui, à l'issue de tous les modules et du capstone |

Les 200 heures de cours se répartissent environ 60 % en direct (cours magistraux, ateliers, code-along, revues de capstone) et 40 % en travail structuré asynchrone (lectures, notebooks, problèmes). Les 60+ sessions en direct couvrent les cours, les ateliers pratiques, les interventions industriels, les permanences, les revues de capstone et la présentation finale.

---

## Public

- **Professionnels en activité** qui passent à des rôles ML/IA depuis des domaines voisins — génie logiciel, analyse de données, finance quantitative, actuariat, calcul scientifique.
- **Étudiants de licence avancée et de master** en mathématiques, informatique, statistique, ingénierie ou sciences sociales quantitatives, qui veulent un parcours intensif plutôt qu'un cours étalé sur un semestre.
- **Cohortes d'entreprise** organisant un programme interne de montée en compétences : banques, opérateurs télécom, assureurs, fintech, équipes data du secteur public.

Vous tirerez davantage du programme si vous arrivez avec une syntaxe Python à l'aise (fonctions, classes, comprehensions), une familiarité avec la ligne de commande, et des mathématiques de niveau licence (algèbre linéaire, calcul, probabilités). Aucune expérience préalable en machine learning n'est requise, mais elle aide.

## Prérequis

- **Indispensable.** Maîtrise de Python au niveau *"je peux lire et modifier un script de 200 lignes sans me perdre"*. À l'aise avec fonctions, classes, imports, dictionnaires, comprehensions. Familier avec `pip` et les environnements virtuels.
- **Indispensable.** Algèbre linéaire (vecteurs, matrices, valeurs propres), calcul (dérivées, gradients, intégrales), probabilités (variables aléatoires, espérance, probabilité conditionnelle) au niveau licence.
- **Fortement recommandé.** Une exposition même brève à NumPy / Pandas.
- **Utile mais non obligatoire.** Une exposition antérieure au ML (un cours en ligne, une compétition Kaggle, un cours d'introduction universitaire), familiarité avec Git/GitHub, ligne de commande Linux de base.

Si vous n'êtes pas sûr d'avoir les prérequis, le dossier de candidature inclut un court test technique. Une auto-évaluation honnête en amont vaut mieux qu'une semaine 1 stressante.

## Outils

- **Python 3.11+** comme langage de travail tout au long
- **Jupyter** (notebook + Lab) pour les ateliers
- **NumPy, Pandas, scikit-learn, matplotlib, seaborn** comme pile analytique
- **PyTorch** (principal) et **TensorFlow/Keras** (secondaire) pour le deep learning
- **HuggingFace** (`transformers`, `datasets`, `peft`, `accelerate`) pour le TAL et les LLM
- **LangChain, ChromaDB, FAISS** pour le RAG
- **MLflow, DVC, Docker, FastAPI** pour le module MLOps
- **Google Colab** (offre gratuite avec GPU) comme solution de repli ; les participants sans GPU local utilisent Colab Pro ou Kaggle pour les semaines deep learning
- **Git / GitHub** pour le contrôle de version tout au long du bootcamp ; la pièce finale de portfolio est publiée sur le GitHub du participant

---

## Les dix modules

Chaque module ci-dessous renvoie aux supports existants du [catalogue de cours](../../../courses/) quand un cours équivalent existe. Le bootcamp condense, séquence et ajoute des projets par-dessus le catalogue, plutôt que de réécrire le contenu.

### Module 1 — Python pour le travail sur données

**En une phrase.** Prendre le Python que vous connaissez à moitié et le rendre assez précis pour livrer en production.

**Acquis d'apprentissage.** À l'issue du module, les participants pourront :

1. Écrire du Python idiomatique — comprehensions list/dict/set, générateurs, gestionnaires de contexte, décorateurs
2. Utiliser NumPy et Pandas couramment pour la manipulation vectorisée de données
3. Construire un projet Python reproductible (virtualenv, `pyproject.toml`, pre-commit, tests de base)
4. Lire, modifier et écrire des notebooks Jupyter sans perdre la reproductibilité

**Sujets.** Types et contrôle de flux · fonctions, portée, closures · classes et protocoles · tableaux NumPy, broadcasting, indexation · Series et DataFrames Pandas, jointures, group-by, reshape · matplotlib et seaborn pour la visualisation · environnements virtuels et gestion de dépendances · bases de Git pour code et notebooks.

**Ateliers.** (1) Refactorer un script de 300 lignes désordonné en un module propre avec tests. (2) Manipuler un vrai jeu de données public (données d'établissements de santé au Kenya) de bout en bout en Pandas. (3) Publier votre projet sur GitHub avec README, lockfile, et installation reproductible.

**S'appuie sur.** Catalogue : [Programmation pour Scientifiques](../../../courses/programmation-scientifiques/) et [Introduction à la Science des Données](../../../courses/intro-data-science/).

---

### Module 2 — Introduction au machine learning

**En une phrase.** Ce que le ML est, ce qu'il n'est pas, et le workflow qui tourne sous chaque projet.

**Acquis.**

1. Formuler un problème comme apprentissage supervisé, non supervisé ou par renforcement, et reconnaître quand aucun de ces cadres n'est le bon
2. Construire un pipeline train/validation/test propre qui évite les fuites
3. Choisir, ajuster et évaluer un modèle simple sur un jeu de données réel
4. Lire une courbe d'apprentissage et une matrice de confusion sans se mélanger

**Sujets.** La boucle d'apprentissage supervisé · fonctions de perte et risque · minimisation du risque empirique · biais-variance · validation croisée, split train/val/test, fuites · métriques d'évaluation pour la classification et la régression · le « no free lunch » dans le choix de modèle.

**Ateliers.** (1) Prédire la réadmission de patients sur un jeu de données hospitalier réel (régression logistique, évaluée avec calibration et non seulement précision). (2) Diagnostiquer une mauvaise évaluation : repérer la fuite dans un notebook délibérément cassé.

**S'appuie sur.** Catalogue : [Fondements de l'Apprentissage Automatique](../../../courses/apprentissage-automatique/) (chapitres d'introduction).

---

### Module 3 — ML classique : classification, régression, clustering

**En une phrase.** La boîte à outils pré-deep-learning — toujours la bonne réponse pour la plupart des problèmes tabulaires.

**Acquis.**

1. Ajuster et calibrer une régression linéaire et régularisée (ridge, lasso, elastic net)
2. Construire et interpréter des ensembles d'arbres (random forests, gradient boosting)
3. Appliquer des méthodes non supervisées (k-means, hiérarchique, DBSCAN, GMM, PCA, UMAP)
4. Interpréter feature-importance et partial-dependence honnêtement, sans surinterpréter la causalité

**Sujets.** Régression linéaire et logistique · régularisation (ridge, lasso, elastic net) · SVM et astuce du noyau · arbres de décision, random forests, gradient boosting (XGBoost, LightGBM) · clustering (k-means, hiérarchique, DBSCAN, GMM) · réduction de dimension (PCA, UMAP, t-SNE) · interprétation de modèles (permutation importance, SHAP, partial dependence) · ce que ces méthodes peuvent et ne peuvent pas dire sur la causalité.

**Ateliers.** (1) Scoring de crédit sur un jeu de données Kaggle / banque africaine — pipeline complet de l'EDA à une fonction de scoring déployable, avec audit d'équité. (2) Segmentation client par patterns de transactions mobile money. (3) Interprétation SHAP d'un modèle XGBoost, en incluant les modes de défaillance de SHAP lui-même.

**S'appuie sur.** Catalogue : [Fondements de l'Apprentissage Automatique](../../../courses/apprentissage-automatique/) (corps principal).

---

### Module 4 — Systèmes de recommandation

**En une phrase.** Comment fonctionnent vraiment les systèmes à la Netflix, et le problème d'évaluation honnête qu'ils posent.

**Acquis.**

1. Implémenter du filtrage collaboratif (user-based, item-based, factorisation matricielle)
2. Implémenter du filtrage par contenu avec des embeddings
3. Construire un recommandeur hybride et l'évaluer avec les métriques offline (precision@k, NDCG, MAP)
4. Comprendre pourquoi les métriques offline divergent souvent des résultats d'A/B en ligne

**Sujets.** Le problème de la recommandation · feedback explicite vs implicite · filtrage collaboratif · factorisation matricielle (SVD, ALS, NMF) · filtrage par contenu avec embeddings · modèles hybrides · évaluation : precision@k, recall@k, NDCG, MAP, métriques offline vs online · cold-start, biais de popularité, bulles de filtre · le problème du « vous ne saurez jamais avant d'A/B tester ».

**Ateliers.** (1) Filtre collaboratif sur MovieLens (SVD puis ALS). (2) Construire un recommandeur hybride sur un jeu e-commerce public. (3) Faire passer le même recommandeur dans trois métriques d'évaluation et expliquer pourquoi elles classent les modèles différemment.

**S'appuie sur.** Pas d'équivalent direct dans le catalogue — contenu nouveau écrit spécifiquement pour le bootcamp.

---

### Module 5 — Traitement automatique du langage

**En une phrase.** Des méthodes classiques aux pipelines de l'ère Transformer.

**Acquis.**

1. Construire un pipeline de classification de texte (nettoyage, tokenisation, vectorisation, entraînement, évaluation)
2. Fine-tuner un transformer pré-entraîné sur une tâche spécifique à un domaine
3. Appliquer le TAL dans un contexte multilingue ou à faibles ressources (avec attention aux langues africaines)
4. Reconnaître les limites : hallucination, biais, difficulté d'évaluation

**Sujets.** Prétraitement de texte et tokenisation (BPE, WordPiece) · embeddings de mots (Word2Vec, GloVe, FastText) · modèles séquentiels (RNN, LSTM, GRU) · l'architecture Transformer · modèles de la famille BERT et fine-tuning · NER, sentiment, classification, résumé · TAL multilingue et à faibles ressources · évaluation : BLEU, ROUGE, exact match, évaluation humaine.

**Ateliers.** (1) Classification de sentiment sur avis clients (baseline régression logistique → DistilBERT fine-tuné). (2) Reconnaissance d'entités nommées sur un jeu multilingue incluant au moins une langue africaine. (3) Résumé de documents avec un T5/BART fine-tuné.

**S'appuie sur.** Catalogue : [Traitement Automatique du Langage](../../../courses/tal-nlp/).

---

### Module 6 — ML moderne : ANN, CNN, RNN

**En une phrase.** Le deep learning de bout en bout, avec assez de théorie pour savoir quand *ne pas* l'utiliser.

**Acquis.**

1. Entraîner un réseau feed-forward à partir de zéro, d'abord en NumPy puis en PyTorch
2. Construire, entraîner et évaluer des CNN sur des tâches de classification d'images
3. Construire, entraîner et évaluer des RNN/LSTM sur des tâches séquentielles
4. Diagnostiquer les pathologies d'entraînement : gradients qui s'évanouissent, surapprentissage, neurones morts, dérive de distribution

**Sujets.** Réseaux feed-forward, rétropropagation, optimisation (SGD, Adam, AdamW) · régularisation (dropout, batch norm, weight decay, early stopping) · CNN (LeNet, AlexNet, ResNet, architectures modernes) · RNN, LSTM, GRU · l'attention comme primitive · apprentissage de représentations · les leçons amères du deep learning (scaling de compute, ce qui ne se transfère pas).

**Ateliers.** (1) Construire un MLP à 2 couches à partir de zéro en NumPy, puis le porter en PyTorch. (2) Classification d'images sur un jeu d'imagerie médicale publique (radiographie thoracique par exemple, avec discussion des biais de dataset). (3) Prédiction de séquence sur des séries temporelles financières avec un LSTM.

**S'appuie sur.** Catalogue : [Apprentissage Profond](../../../courses/apprentissage-profond/).

---

### Module 7 — LLM et IA générative

**En une phrase.** Ce qu'il y a sous le capot de GPT/Claude/LLaMA, ce qu'on peut vraiment en faire, et où ils échouent.

**Acquis.**

1. Comprendre l'architecture Transformer telle qu'elle apparaît dans les LLM modernes
2. Appliquer efficacement le prompt engineering et les techniques de sortie structurée
3. Fine-tuner un petit LLM open-source avec LoRA/QLoRA sur un jeu de domaine
4. Construire un système RAG (Retrieval-Augmented Generation)
5. Évaluer la génération honnêtement : quand un LLM est vraiment utile, et quand il fabule

**Sujets.** Le transformer, mécanisme d'attention, scaling laws · pré-entraînement, fine-tuning, RLHF/DPO au niveau survol · prompt engineering, sortie structurée, function calling · fine-tuning par paramètres (LoRA, QLoRA, PEFT) · RAG : chunking, embedding, retrieval, reranking, génération · modèles de diffusion (intuition + usage pratique) · évaluation : BLEU, ROUGE, LLM-as-judge, évaluation humaine, pourquoi toutes ces métriques sont partielles · systèmes agentiques et tool use · sûreté, alignement, hallucination, biais.

**Ateliers.** (1) Construire un RAG sur un corpus de domaine (rapports OMS/AFRO par exemple) avec ChromaDB et un LLM local ou via API. (2) Fine-tuner un modèle ouvert 1-7B paramètres avec LoRA sur une tâche de domaine. (3) Construire un agent multi-étape avec tool use (recherche, calculatrice, exécution de code) via LangChain ou LangGraph.

**S'appuie sur.** Catalogue : [IA Générative](../../../courses/ia-generative/).

---

### Module 8 — MLOps et déploiement

**En une phrase.** Ce qu'il faut pour que le modèle continue à fonctionner après que le notebook est fermé.

**Acquis.**

1. Versionner code, données et modèles de manière à soutenir la reproductibilité
2. Conteneuriser un modèle et le déployer comme API REST
3. Mettre en place tracking d'expériences, model registry et monitoring
4. Construire un pipeline CI/CD basique pour un système ML

**Sujets.** Reproductibilité (Git, DVC, MLflow) · tracking d'expériences et model registry (MLflow, Weights &amp; Biases) · conteneurisation (Docker, docker-compose) · servir des modèles (FastAPI, BentoML, model registries) · monitoring (dérive des données, des prédictions, de la performance, latence, coût) · CI/CD pour pipelines ML · la différence entre « ça marche sur mon laptop » et « ça marche en production pendant six mois ».

**Ateliers.** (1) Envelopper un modèle entraîné dans un service FastAPI, conteneuriser, déployer sur un cloud gratuit (Render ou Railway), l'appeler depuis un notebook. (2) Mettre en place le tracking MLflow pour une boucle de réentraînement. (3) Simuler une dérive de données sur un modèle déployé et la détecter depuis le dashboard de monitoring.

**S'appuie sur.** Catalogue : [MLOps](../../../courses/mlops/).

---

### Module 9 — Projet capstone

**En une phrase.** Prendre un problème réel et le mener de l'idée au système déployé en deux semaines.

Ce module tourne en parallèle des modules 8 et 10, sur les deux dernières semaines du programme. Chaque participant (ou petite équipe de 2-3) livre un projet complet : jeu de données réel, modèle réel, endpoint déployé, rapport écrit, dépôt public, démonstration live.

Voir [`CAPSTONE.md`](../CAPSTONE.md) pour la spécification complète du projet, les jalons, la grille d'évaluation, et des exemples de pistes de projets.

---

### Module 10 — Portfolio

**En une phrase.** Le capstone, les ateliers, et un profil public clair qui dit *« je sais effectivement faire ça »*.

**Acquis.**

1. Curater trois à cinq projets du bootcamp dans un portfolio cohérent
2. Écrire un README qu'un lecteur extérieur peut suivre en cinq minutes
3. Publier le capstone en démo hébergée + rédaction technique
4. Construire un profil public (GitHub, LinkedIn, site personnel si applicable) qui pointe vers le portfolio

**Sujets.** Curation de portfolio (moins, c'est plus) · discipline du README · écriture technique pour projets ML · publication de notebooks (nbviewer, Colab, GitHub Pages, Jupyter Book) · hébergement de démos de modèles (Gradio, Streamlit, HuggingFace Spaces) · utiliser son portfolio pour poser de meilleures questions en entretien technique.

**Référence.** Le [portfolio data-science](https://gabayae.github.io/data-portfolio/) de l'instructeur principal est un modèle parmi d'autres. Le module 10 ne prescrit pas un template unique — il enseigne la discipline de *rendre son travail trouvable et lisible pour des lecteurs extérieurs à la cohorte*.

---

## Calendrier (cohorte temps plein 10 semaines)

| Semaine | Thème | Modules |
|------|-------|---------|
| 1 | Boîte à outils Python pour le travail sur données | M1 |
| 2 | Introduction au ML + début du ML classique | M2 + M3 (partie 1) |
| 3 | ML classique en profondeur, atelier scoring de crédit | M3 |
| 4 | Systèmes de recommandation | M4 |
| 5 | Traitement automatique du langage | M5 |
| 6 | Deep learning (ANN, CNN, RNN) | M6 |
| 7 | LLM et IA générative | M7 |
| 8 | MLOps et déploiement | M8 |
| 9 | Travail sur le capstone + sessions portfolio | M9 + M10 |
| 10 | Finalisation du capstone, présentations finales, lancement du portfolio | M9 + M10 |

Les cohortes à temps partiel parcourent le même contenu sur 20 semaines avec une intensité hebdomadaire de moitié. Les sessions d'intervenants industriels sont réparties sur les semaines 2-9 (environ une par semaine, parfois deux).

Une semaine type à temps plein :

- **Lundi-jeudi matins (3 h chacun).** Cours en direct, code-along, atelier
- **Lundi-jeudi après-midis (2 h chacun).** Travail d'atelier indépendant, avec permanences d'assistants d'enseignement
- **Vendredi.** Intervenant industriel (1 h) + revue d'atelier (1 h) + rétrospective de cohorte (1 h)
- **Étude personnelle (20 h sur la semaine).** Lectures, pré-travail pour la semaine suivante, finalisation des ateliers

## Pédagogie

L'« approche par la pratique » n'est pas du marketing — c'est un choix délibéré avec deux conséquences concrètes :

1. **Chaque module a un vrai jeu de données et un livrable déployable.** Pas un jeu de tutoriel choisi pour la propreté pédagogique, mais des données que les participants rencontreront plausiblement dans leur propre travail : dossiers bancaires africains, données d'établissements de santé, CDR télécom, imagerie satellite, texte multilingue. Le livrable en fin de module est quelque chose qu'un participant pourrait mettre sur GitHub.

2. **Les erreurs font partie du programme.** Plusieurs ateliers sont délibérément semés de fuites de données, de mauvais choix d'évaluation, ou de pathologies d'entraînement. L'exercice consiste à les trouver. Le principe : *repérer un pipeline ML cassé vaut plus que d'en construire un qui marche en vase clos*.

Le cadre « cas-centré » se traduit ainsi : chaque semaine s'ouvre sur un cas réel (un système déployé, un échec publié, un rapport d'audit), et le contenu technique est motivé par ce que le cas a nécessité.

## Évaluation et certificat

- **Livrables hebdomadaires des ateliers** (40 %) — chaque atelier de module est noté sur la justesse, la qualité du code, et une courte interprétation écrite
- **Projet capstone** (40 %) — système déployé + rédaction technique + démonstration live
- **Participation** (20 %) — engagement dans les sessions en direct, revue de code par pairs, présentations de jalons du capstone

Les participants qui complètent tous les livrables et passent le capstone (grille dans `CAPSTONE.md`) reçoivent un **Certificat de réalisation** signé par l'instructeur principal et AIRINA Labs.

Le certificat est une attestation de réalisation, pas un diplôme accrédité. Il est surtout utile comme ancrage de portfolio dans les conversations avec employeurs, pas comme un titre en soi.

## Série d'intervenants industriels

Les 8 intervenants industriels d'une cohorte sont issus des réseaux AIRINA Labs et AIMS : praticiens ML/IA dans des banques africaines, télécoms, fintech, et bureaux régionaux d'entreprises tech globales ; un ou deux chercheurs seniors dans des laboratoires internationaux. Chaque session dure une heure : 30 minutes de *« ce qu'on construit vraiment, et pourquoi »*, 30 minutes de Q&amp;R avec la cohorte. Les noms et affiliations sont confirmés par cohorte et partagés à la clôture des inscriptions.

Les intervenants ne font pas de pitch produit et ne recrutent pas. Ils viennent dire à la cohorte à quoi ressemble le travail hors du bootcamp.

## Après le programme

Pendant trois mois après la fin de la cohorte, les participants conservent l'accès à :

- L'espace Slack de la cohorte (réseau de pairs + canal alumni)
- Un échange 1-à-1 de 30 minutes avec l'instructeur principal pour un suivi technique ou carrière
- La version hébergée de leur capstone (l'instructeur maintient le déploiement actif pendant au moins 3 mois sur un cloud gratuit)

Ce n'est pas un service de placement. L'objectif est de laisser les participants avec un portfolio fonctionnel, un réseau de pairs, et la base technique pour faire leur propre prochain pas.

## Ressources

Lectures recommandées et références, par module :

- **Modules 1-3 (Python, fondements ML).** Aurélien Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3e éd., O'Reilly).
- **Module 3 (ML classique).** Trevor Hastie, Robert Tibshirani, Jerome Friedman, *The Elements of Statistical Learning* (Springer, 2e éd.). PDF gratuit sur le site de Hastie.
- **Module 4 (Systèmes de recommandation).** Charu Aggarwal, *Recommender Systems: The Textbook* (Springer, 2016).
- **Module 5 (TAL).** Dan Jurafsky et James Martin, *Speech and Language Processing* (3e éd. draft). Gratuit sur le site des auteurs.
- **Module 6 (Deep learning).** Ian Goodfellow, Yoshua Bengio, Aaron Courville, *Deep Learning* (MIT Press, 2016). Gratuit en ligne.
- **Module 7 (LLM / GenAI).** Sebastian Raschka, *Build a Large Language Model From Scratch* (Manning, 2024). Le cours NLP HuggingFace (gratuit en ligne).
- **Module 8 (MLOps).** Chip Huyen, *Designing Machine Learning Systems* (O'Reilly, 2022). Le blog MLOps d'Eugene Yan.
- **Compagnon ML topologie/géométrie (optionnel).** Colleen M. Farrelly et Yaé Ulrich Gaba, [*The Shape of Data*](https://nostarch.com/shapeofdata) (No Starch Press) — pour les membres de cohorte qui veulent appliquer outils topologiques et géométriques aux mêmes problèmes.

---

## Candidater

Les cohortes ont lieu plusieurs fois par an. Pour manifester un intérêt pour une cohorte future, ou pour discuter d'une cohorte privée d'entreprise pour votre organisation :

📧 [gabayae2@gmail.com](mailto:gabayae2@gmail.com?subject=Bootcamp%20ML%20%26%20IA%20%E2%80%94%20renseignements%20cohorte)

Merci d'inclure dans votre message : votre profil, votre objectif pour le bootcamp, et si vous parlez d'une cohorte ouverte (individuelle) ou d'une cohorte privée d'entreprise (équipe). Pour les cohortes d'entreprise, précisez aussi la taille d'équipe et la fenêtre temporelle visée.
