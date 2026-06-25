---
layout: workshop
permalink: /workshops/ml-ai-bootcamp/fr/
lang: fr
title: "Bootcamp Machine Learning & IA"
tagline: "Un programme en cohorte de 10 semaines, par la pratique — dix modules de Python au MLOps, capstone déployé, portfolio public."
description: "Programme en cohorte AIRINA Labs. 10 semaines à temps plein / 20 semaines à temps partiel. Dix modules, de Python au MLOps, capstone, portfolio."

# --- Métadonnées de la barre latérale ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "10 semaines temps plein / 20 semaines temps partiel (≈ 200 heures de cours)"
level: "Intermédiaire à Avancé"
format: "Sur site, en ligne en direct, ou hybride"
languages: "Français &amp; anglais"
certificate: "Certificat de complétion"

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Demande d'atelier — Bootcamp Machine Learning & IA"
---

## Présentation du programme

**Pages opérationnelles.** [Calendrier hebdomadaire (EN)]({{ '/workshops/ml-ai-bootcamp/en/schedule/' | relative_url }}) | [Brief du capstone]({{ '/workshops/ml-ai-bootcamp/CAPSTONE/' | relative_url }})

*Note : le calendrier opérationnel et les pages hebdomadaires sont en anglais. La traduction française suivra après la première cohorte, une fois la structure stabilisée par le retour des participants.*

En janvier 2023, BioNTech a racheté InstaDeep — une entreprise d'apprentissage automatique fondée à Tunis et exploitant des bureaux à Lagos, Nairobi et Paris — pour 562 millions de dollars. L'opération a rendu public ce que les recruteurs du secteur en Afrique observaient depuis plusieurs années : la demande mondiale d'ingénieurs ML déployables en production dépasse très largement l'offre formée, et l'écart est plus marqué sur le continent qu'ailleurs. La plupart des cursus universitaires africains en informatique se terminent avant le deep learning ; les MOOC qui comblent le vide sont calibrés pour des prérequis nord-américains et supposent généralement un premier emploi en ingénierie logicielle. Ce bootcamp cible exactement ce trou. Il prend des diplômés quantitatifs — mathématiques, statistique, informatique, finance quantitative, génie scientifique — et les amène en dix semaines au niveau de mise en production que recherchent les équipes ML africaines et internationales qui les recrutent.

### Le programme en bref

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

### Outils

- **Python 3.11+** comme langage de travail tout au long.
- **Jupyter** (notebook + Lab) pour les ateliers.
- **NumPy, Pandas, scikit-learn, matplotlib, seaborn** comme pile analytique.
- **PyTorch** (principal) et **TensorFlow/Keras** (secondaire) pour le deep learning.
- **HuggingFace** (`transformers`, `datasets`, `peft`, `accelerate`) pour le TAL et les LLM.
- **LangChain, ChromaDB, FAISS** pour le RAG.
- **MLflow, DVC, Docker, FastAPI** pour le module MLOps.
- **Google Colab** (offre gratuite avec GPU) comme solution de repli ; les participants sans GPU local utilisent Colab Pro ou Kaggle pour les semaines deep learning.
- **Git / GitHub** pour le contrôle de version tout au long du bootcamp ; la pièce finale de portfolio est publiée sur le GitHub du participant.

### Les dix modules

Chaque module ci-dessous renvoie aux supports existants du [catalogue de cours]({{ '/courses/' | relative_url }}) quand un cours équivalent existe. Le bootcamp condense, séquence et ajoute des projets par-dessus le catalogue, plutôt que de réécrire le contenu.

#### Module 1 — Python pour le travail sur données

*En une phrase.* Prendre le Python que vous connaissez à moitié et le rendre assez précis pour livrer en production.

**Sujets.** Types et contrôle de flux · fonctions, portée, closures · classes et protocoles · tableaux NumPy, broadcasting, indexation · Series et DataFrames Pandas, jointures, group-by, reshape · matplotlib et seaborn pour la visualisation · environnements virtuels et gestion de dépendances · bases de Git pour code et notebooks.

**Ateliers.** (1) Refactorer un script de 300 lignes désordonné en un module propre avec tests. (2) Manipuler un vrai jeu de données public (données d'établissements de santé au Kenya) de bout en bout en Pandas. (3) Publier votre projet sur GitHub avec README, lockfile, et installation reproductible.

#### Module 2 — Introduction au machine learning

*En une phrase.* Ce que le ML est, ce qu'il n'est pas, et le workflow qui tourne sous chaque projet.

**Sujets.** La boucle d'apprentissage supervisé · fonctions de perte et risque · minimisation du risque empirique · biais-variance · validation croisée, split train/val/test, fuites · métriques d'évaluation pour la classification et la régression · le « no free lunch » dans le choix de modèle.

**Ateliers.** (1) Prédire la réadmission de patients sur un jeu de données hospitalier réel (régression logistique, évaluée avec calibration et non seulement précision). (2) Diagnostiquer une mauvaise évaluation : repérer la fuite dans un notebook délibérément cassé.

#### Module 3 — ML classique : classification, régression, clustering

*En une phrase.* La boîte à outils pré-deep-learning — toujours la bonne réponse pour la plupart des problèmes tabulaires.

**Sujets.** Régression linéaire et logistique · régularisation (ridge, lasso, elastic net) · SVM et astuce du noyau · arbres de décision, random forests, gradient boosting (XGBoost, LightGBM) · clustering (k-means, hiérarchique, DBSCAN, GMM) · réduction de dimension (PCA, UMAP, t-SNE) · interprétation de modèles (permutation importance, SHAP, partial dependence) · ce que ces méthodes peuvent et ne peuvent pas dire sur la causalité.

**Ateliers.** (1) Scoring de crédit sur un jeu de données Kaggle / banque africaine — pipeline complet avec audit d'équité. (2) Segmentation client par patterns de transactions mobile money. (3) Interprétation SHAP d'un modèle XGBoost, en incluant les modes de défaillance de SHAP lui-même.

#### Module 4 — Systèmes de recommandation

*En une phrase.* Comment fonctionnent vraiment les systèmes à la Netflix, et le problème d'évaluation honnête qu'ils posent.

**Sujets.** Le problème de la recommandation · feedback explicite vs implicite · filtrage collaboratif · factorisation matricielle (SVD, ALS, NMF) · filtrage par contenu avec embeddings · modèles hybrides · évaluation : precision@k, recall@k, NDCG, MAP, métriques offline vs online · cold-start, biais de popularité, bulles de filtre.

**Ateliers.** (1) Filtre collaboratif sur MovieLens (SVD puis ALS). (2) Construire un recommandeur hybride sur un jeu e-commerce public. (3) Faire passer le même recommandeur dans trois métriques d'évaluation et expliquer pourquoi elles classent les modèles différemment.

#### Module 5 — Traitement automatique du langage

*En une phrase.* Des méthodes classiques aux pipelines de l'ère Transformer.

**Sujets.** Prétraitement de texte et tokenisation (BPE, WordPiece) · embeddings de mots (Word2Vec, GloVe, FastText) · modèles séquentiels (RNN, LSTM, GRU) · l'architecture Transformer · modèles de la famille BERT et fine-tuning · NER, sentiment, classification, résumé · TAL multilingue et à faibles ressources · évaluation : BLEU, ROUGE, exact match, évaluation humaine.

**Ateliers.** (1) Classification de sentiment sur avis clients (baseline régression logistique → DistilBERT fine-tuné). (2) Reconnaissance d'entités nommées sur un jeu multilingue incluant au moins une langue africaine. (3) Résumé de documents avec un T5/BART fine-tuné.

#### Module 6 — ML moderne : ANN, CNN, RNN

*En une phrase.* Le deep learning de bout en bout, avec assez de théorie pour savoir quand *ne pas* l'utiliser.

**Sujets.** Réseaux feed-forward, rétropropagation, optimisation (SGD, Adam, AdamW) · régularisation (dropout, batch norm, weight decay, early stopping) · CNN (LeNet, AlexNet, ResNet, architectures modernes) · RNN, LSTM, GRU · l'attention comme primitive · apprentissage de représentations · les leçons amères du deep learning.

**Ateliers.** (1) Construire un MLP à 2 couches à partir de zéro en NumPy, puis le porter en PyTorch. (2) Classification d'images sur un jeu d'imagerie médicale publique. (3) Prédiction de séquence sur des séries temporelles financières avec un LSTM.

#### Module 7 — LLM et IA générative

*En une phrase.* Ce qu'il y a sous le capot de GPT/Claude/LLaMA, ce qu'on peut vraiment en faire, et où ils échouent.

**Sujets.** Le transformer, mécanisme d'attention, scaling laws · pré-entraînement, fine-tuning, RLHF/DPO au niveau survol · prompt engineering, sortie structurée, function calling · fine-tuning par paramètres (LoRA, QLoRA, PEFT) · RAG : chunking, embedding, retrieval, reranking, génération · modèles de diffusion · évaluation : BLEU, ROUGE, LLM-as-judge, évaluation humaine · systèmes agentiques et tool use · sûreté, alignement, hallucination, biais.

**Ateliers.** (1) Construire un RAG sur un corpus de domaine (rapports OMS/AFRO par exemple) avec ChromaDB et un LLM local ou via API. (2) Fine-tuner un modèle ouvert 1-7B paramètres avec LoRA sur une tâche de domaine. (3) Construire un agent multi-étape avec tool use (recherche, calculatrice, exécution de code) via LangChain ou LangGraph.

#### Module 8 — MLOps et déploiement

*En une phrase.* Ce qu'il faut pour que le modèle continue à fonctionner après que le notebook est fermé.

**Sujets.** Reproductibilité (Git, DVC, MLflow) · tracking d'expériences et model registry (MLflow, Weights & Biases) · conteneurisation (Docker, docker-compose) · servir des modèles (FastAPI, BentoML, model registries) · monitoring (dérive des données, des prédictions, de la performance, latence, coût) · CI/CD pour pipelines ML.

**Ateliers.** (1) Envelopper un modèle entraîné dans un service FastAPI, conteneuriser, déployer sur un cloud gratuit, l'appeler depuis un notebook. (2) Mettre en place le tracking MLflow pour une boucle de réentraînement. (3) Simuler une dérive de données sur un modèle déployé et la détecter depuis le dashboard de monitoring.

#### Module 9 — Projet capstone

*En une phrase.* Prendre un problème réel et le mener de l'idée au système déployé en deux semaines.

Ce module tourne en parallèle des modules 8 et 10, sur les deux dernières semaines du programme. Chaque participant (ou petite équipe de 2-3) livre un projet complet : jeu de données réel, modèle réel, endpoint déployé, rapport écrit, dépôt public, démonstration live.

Voir [`CAPSTONE.md`]({{ '/workshops/ml-ai-bootcamp/CAPSTONE/' | relative_url }}) pour la spécification complète du projet, les jalons, la grille d'évaluation, et des exemples de pistes de projets.

#### Module 10 — Portfolio

*En une phrase.* Le capstone, les ateliers, et un profil public clair qui dit *« je sais effectivement faire ça »*.

**Sujets.** Curation de portfolio (moins, c'est plus) · discipline du README · écriture technique pour projets ML · publication de notebooks (nbviewer, Colab, GitHub Pages, Jupyter Book) · hébergement de démos de modèles (Gradio, Streamlit, HuggingFace Spaces) · utiliser son portfolio pour poser de meilleures questions en entretien technique.

### Calendrier (cohorte temps plein 10 semaines)

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

Les cohortes à temps partiel parcourent le même contenu sur 20 semaines avec une intensité hebdomadaire de moitié. Les sessions d'intervenants industriels sont réparties sur les semaines 2-9.

### Pédagogie

L'« approche par la pratique » n'est pas du marketing — c'est un choix délibéré avec deux conséquences concrètes :

1. **Chaque module a un vrai jeu de données et un livrable déployable.** Pas un jeu de tutoriel choisi pour la propreté pédagogique, mais des données que les participants rencontreront plausiblement dans leur propre travail : dossiers bancaires africains, données d'établissements de santé, CDR télécom, imagerie satellite, texte multilingue. Le livrable en fin de module est quelque chose qu'un participant pourrait mettre sur GitHub.

2. **Les erreurs font partie du programme.** Plusieurs ateliers sont délibérément semés de fuites de données, de mauvais choix d'évaluation, ou de pathologies d'entraînement. L'exercice consiste à les trouver. Le principe : *repérer un pipeline ML cassé vaut plus que d'en construire un qui marche en vase clos*.

### Évaluation et certificat

- **Livrables hebdomadaires des ateliers** (40 %) — chaque atelier de module est noté sur la justesse, la qualité du code, et une courte interprétation écrite.
- **Projet capstone** (40 %) — système déployé + rédaction technique + démonstration live.
- **Participation** (20 %) — engagement dans les sessions en direct, revue de code par pairs, présentations de jalons du capstone.

Les participants qui complètent tous les livrables et passent le capstone (grille dans `CAPSTONE.md`) reçoivent un **Certificat de réalisation** signé par l'instructeur principal et AIRINA Labs. Le certificat est une attestation de réalisation, pas un diplôme accrédité.

### Série d'intervenants industriels

Les 8 intervenants industriels d'une cohorte sont issus des réseaux AIRINA Labs et AIMS : praticiens ML/IA dans des banques africaines, télécoms, fintech, et bureaux régionaux d'entreprises tech globales ; un ou deux chercheurs seniors dans des laboratoires internationaux. Chaque session dure une heure : 30 minutes de *« ce qu'on construit vraiment, et pourquoi »*, 30 minutes de Q&R avec la cohorte. Les intervenants ne font pas de pitch produit et ne recrutent pas.

### Après le programme

Pendant trois mois après la fin de la cohorte, les participants conservent l'accès à :

- L'espace Slack de la cohorte (réseau de pairs + canal alumni).
- Un échange 1-à-1 de 30 minutes avec l'instructeur principal pour un suivi technique ou carrière.
- La version hébergée de leur capstone (l'instructeur maintient le déploiement actif pendant au moins 3 mois sur un cloud gratuit).

Ce n'est pas un service de placement. L'objectif est de laisser les participants avec un portfolio fonctionnel, un réseau de pairs, et la base technique pour faire leur propre prochain pas.

### Ressources

- **Modules 1-3 (Python, fondements ML).** Aurélien Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3e éd., O'Reilly).
- **Module 3 (ML classique).** Trevor Hastie, Robert Tibshirani, Jerome Friedman, *The Elements of Statistical Learning* (Springer, 2e éd.).
- **Module 4 (Systèmes de recommandation).** Charu Aggarwal, *Recommender Systems: The Textbook* (Springer, 2016).
- **Module 5 (TAL).** Dan Jurafsky et James Martin, *Speech and Language Processing* (3e éd. draft).
- **Module 6 (Deep learning).** Ian Goodfellow, Yoshua Bengio, Aaron Courville, *Deep Learning* (MIT Press, 2016).
- **Module 7 (LLM / GenAI).** Sebastian Raschka, *Build a Large Language Model From Scratch* (Manning, 2024). Cours NLP HuggingFace.
- **Module 8 (MLOps).** Chip Huyen, *Designing Machine Learning Systems* (O'Reilly, 2022).
- **Compagnon ML topologie/géométrie.** Colleen M. Farrelly et Yaé Ulrich Gaba, [*The Shape of Data*](https://nostarch.com/shapeofdata) (No Starch Press).

## Objectifs pédagogiques

À la fin du bootcamp, les participants seront capables de :

1. Construire, évaluer et déployer un système ML complet de bout en bout — des données brutes à une démonstration hébergée fonctionnelle.
2. Choisir la bonne famille de modèles pour un problème et défendre ce choix face à des baselines plus simples.
3. Diagnostiquer les modes d'échec classiques (fuites de données, mauvaise calibration, dérive de distribution, entraînement mort) avant le déploiement.
4. Appliquer la boîte à outils LLM moderne (prompt engineering, fine-tuning avec LoRA, RAG, agents) à de vrais problèmes de domaine.
5. Mettre en place la machinerie MLOps (versionnage, conteneurisation, monitoring, CI/CD) nécessaire pour garder un modèle déployé en vie.
6. Curater un portfolio public qui démontre une capacité ML production-ready à un recruteur technique.

## Public visé

- **Professionnels en activité** qui passent à des rôles ML/IA depuis des domaines voisins — génie logiciel, analyse de données, finance quantitative, actuariat, calcul scientifique.
- **Étudiants de licence avancée et de master** en mathématiques, informatique, statistique, ingénierie ou sciences sociales quantitatives, qui veulent un parcours intensif plutôt qu'un cours étalé sur un semestre.
- **Cohortes d'entreprise** organisant un programme interne de montée en compétences : banques, opérateurs télécom, assureurs, fintech, équipes data du secteur public.

Vous tirerez davantage du programme si vous arrivez avec une syntaxe Python à l'aise (fonctions, classes, comprehensions), une familiarité avec la ligne de commande, et des mathématiques de niveau licence (algèbre linéaire, calcul, probabilités). Aucune expérience préalable en machine learning n'est requise, mais elle aide.

**Prérequis :**

- **Indispensable.** Maîtrise de Python au niveau *« je peux lire et modifier un script de 200 lignes sans me perdre »*. À l'aise avec fonctions, classes, imports, dictionnaires, comprehensions. Familier avec `pip` et les environnements virtuels.
- **Indispensable.** Algèbre linéaire (vecteurs, matrices, valeurs propres), calcul (dérivées, gradients, intégrales), probabilités (variables aléatoires, espérance, probabilité conditionnelle) au niveau licence.
- **Fortement recommandé.** Une exposition même brève à NumPy / Pandas.
- **Utile mais non obligatoire.** Une exposition antérieure au ML, familiarité avec Git/GitHub, ligne de commande Linux de base.

Si vous n'êtes pas sûr d'avoir les prérequis, le dossier de candidature inclut un court test technique. Une auto-évaluation honnête en amont vaut mieux qu'une semaine 1 stressante.

## Plaquette

Pour une plaquette d'une page, à transmettre à une équipe formation interne d'entreprise, un département universitaire ou un comité d'admission, écrivez à <a href="mailto:gabayae2@gmail.com?subject=Demande%20de%20plaquette%20%E2%80%94%20Bootcamp%20ML%20%26%20IA">gabayae2@gmail.com</a> en précisant la taille de l'audience et la fenêtre temporelle envisagée pour la cohorte.

Pour candidater directement à une cohorte ouverte future, ou pour discuter d'une cohorte privée d'entreprise pour votre organisation, écrivez à <a href="mailto:gabayae2@gmail.com?subject=Bootcamp%20ML%20%26%20IA%20%E2%80%94%20renseignements%20cohorte">gabayae2@gmail.com</a>. Merci d'inclure dans votre message : votre profil, votre objectif pour le bootcamp, et si vous parlez d'une cohorte ouverte (individuelle) ou d'une cohorte privée d'entreprise (équipe). Pour les cohortes d'entreprise, précisez aussi la taille d'équipe et la fenêtre temporelle visée.
