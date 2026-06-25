---
layout: workshop
permalink: /workshops/mlops-in-practice/fr/
lang: fr
title: "MLOps en Pratique"
tagline: "Du notebook à la production : packager, déployer, surveiller et maintenir des systèmes ML avec les outils standards de l'industrie."
description: "Atelier de 4 jours : Docker, CI/CD, monitoring, MLflow, DVC — du notebook à la production."

# --- Métadonnées de la barre latérale ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "4 jours (≈ 24 heures)"
level: "Intermédiaire à Avancé"
format: "Sur site, en ligne en direct, ou hybride"
languages: "Français &amp; anglais"
certificate: "Certificat de complétion"

# --- Liens des supports ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/mlops-in-practice

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Demande d'atelier — MLOps en Pratique"
---

## Présentation du programme

Cet atelier comble le fossé entre les expériences en notebook et les systèmes ML en production. Les participants apprennent à packager, déployer, surveiller et maintenir des modèles de machine learning avec des outils standards de l'industrie. L'accent est mis sur des workflows pratiques et reproductibles fonctionnant dans des environnements à ressources limitées — y compris des configurations sans cloud pertinentes pour les contextes africains.

### Logiciels Requis

- Python 3.10+, pip, virtualenv
- Docker Desktop
- Git
- Bibliothèques : mlflow, dvc, fastapi, uvicorn, pytest, great-expectations
- Optionnel : compte GitHub, fournisseur cloud (niveaux gratuits suffisent)

### Jour 1 : Structure de Projet & Suivi d'Expériences

**Objectifs :** Organiser les projets ML pour la reproductibilité et suivre les expériences systématiquement.

- **Le Problème MLOps** — Pourquoi les notebooks échouent en production, le cycle de vie ML, la dette technique dans les systèmes ML, niveaux de maturité MLOps
- **Structure de Projet** — Template Cookiecutter Data Science, séparation config/données/code/modèles, gestion d'environnement (virtualenv, conda), fichiers requirements, patterns Makefile
- **Suivi d'Expériences avec MLflow** — Installation, journalisation des paramètres/métriques/artefacts, comparaison des runs, interface MLflow, organisation des expériences
- **Versioning de Données & Modèles avec DVC** — Git pour les données, DVC init, ajout de fichiers, stockage distant (local, S3, GCS), pipelines avec dvc.yaml, reproduction des expériences
- **Gestion de Configuration** — Hydra / OmegaConf pour gérer les hyperparamètres, fichiers de config vs. overrides en ligne de commande, configurations reproductibles

**TP 1 :** Prendre un notebook Jupyter désordonné (fourni) et le refactorer en un projet propre : structure de répertoires, fichiers de config, suivi MLflow, pipeline DVC. Lancer 5 expériences avec différents hyperparamètres et les comparer dans l'interface MLflow.

**Devoir :** Appliquer la même structure à l'un de vos propres projets ML.

### Jour 2 : Conteneurisation & APIs

**Objectifs :** Packager les modèles en conteneurs Docker et les servir via des APIs REST.

- **Fondamentaux de Docker** — Images vs. conteneurs, anatomie d'un Dockerfile, construction d'images, exécution de conteneurs, mapping de ports, volumes, .dockerignore
- **Dockeriser des Applications ML** — Images de base Python, installation de dépendances, copie d'artefacts modèle, builds multi-étapes pour des images plus petites, bases du support GPU
- **Servir des Modèles avec FastAPI** — Construire une API de prédiction : endpoints, modèles requête/réponse (Pydantic), chargement du modèle au démarrage, prédiction par lots, endpoints async, docs automatiques (Swagger)
- **Docker Compose** — Applications multi-conteneurs : API + base de données + serveur MLflow. docker-compose.yml, réseau, variables d'environnement, health checks

**TP 2 :** Construire une stack complète de serving : entraîner un modèle, le sauver avec MLflow, l'encapsuler dans une application FastAPI, conteneuriser avec Docker, orchestrer avec Docker Compose (API + MLflow UI). Tester l'endpoint avec curl et Python requests.

**Devoir :** Ajouter la validation des entrées et la gestion d'erreurs à votre API.

### Jour 3 : Tests & CI/CD

**Objectifs :** Tester le code ML et automatiser les pipelines avec l'intégration continue.

- **Tester les Systèmes ML** — Tests unitaires (pytest), tester les fonctions de traitement de données, tester les prédictions, fixtures, parametrize, mocking
- **Validation des Données** — Great Expectations : définir des attentes, valider des datasets, contrats de données, attraper les problèmes de qualité avant le modèle
- **Validation du Modèle** — Seuils de performance, tests de régression, comparaison avec la baseline, smoke tests pour les endpoints
- **CI/CD avec GitHub Actions** — Fichiers workflow, déclencheurs, jobs et steps, exécution des tests à chaque push, construction d'images Docker, secrets, cache d'artefacts
- **Pipelines ML Automatisés** — De bout en bout : push code → tests → validation données → entraînement → évaluation → construction conteneur → déploiement. Workflows par branches (dev/staging/prod)

**TP 3 :** Mettre en place un pipeline CI/CD complet pour le modèle du Jour 2 : écrire des tests unitaires, ajouter la validation des données, créer un workflow GitHub Actions qui lance les tests, entraîne le modèle et construit une image Docker à chaque push.

**Devoir :** Ajouter une barrière de performance — le pipeline doit échouer si la précision descend sous un seuil.

### Jour 4 : Monitoring, Détection de Dérive & Production

**Objectifs :** Surveiller les modèles déployés et gérer les défis de production.

- **Monitoring de Modèles** — Quoi surveiller : latence de prédiction, taux d'erreur, distributions d'entrée/sortie. Stratégies de logging et d'alertes. Bases de Prometheus + Grafana
- **Dérive des Données & du Modèle** — Dérive conceptuelle, dérive de données, dérive de features. Méthodes de détection : PSI, test KS, Evidently AI. Quand réentraîner, déclencheurs automatiques
- **Tests A/B & Déploiement Shadow** — Releases canary, mode shadow, feature flags pour ML, comparaison de versions en production
- **Patterns de Production** — Registres de modèles (MLflow), déploiement blue-green, stratégies de rollback, inférence batch vs. temps réel, considérations de mise à l'échelle
- **MLOps en Environnements à Ressources Limitées** — Stratégies pour infrastructure limitée : serving léger (Flask + systemd), réentraînement par cron, serveurs MLflow locaux, DVC avec remotes locaux, déploiement edge
- **Présentations & Bilan** — Présentation des pipelines MLOps complets, discussion, questions, certificats

**TP 4 (Projet Final) :** Ajouter le monitoring au modèle déployé : implémenter la détection de dérive avec Evidently AI, configurer les alertes basiques, créer un tableau de bord montrant les métriques de santé du modèle. Présenter le pipeline complet : code → test → build → déploiement → monitoring.

### Évaluation

- **TPs quotidiens** (50 %) — Pipelines et infrastructure fonctionnels
- **Pipeline final** (30 %) — Système MLOps complet démontré le Jour 4
- **Participation** (20 %) — Engagement et devoirs

### Ressources

- [Documentation MLflow](https://mlflow.org/docs/latest/index.html)
- [Documentation DVC](https://dvc.org/doc)
- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Documentation Docker](https://docs.docker.com/)
- [Evidently AI](https://www.evidentlyai.com/)
- [Made With ML — Cours MLOps](https://madewithml.com/)

## Objectifs pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Structurer des projets ML pour la reproductibilité et la collaboration
2. Suivre les expériences systématiquement avec MLflow
3. Versionner les données et modèles avec DVC
4. Conteneuriser les applications ML avec Docker
5. Construire des pipelines CI/CD pour les tests et le déploiement automatisés
6. Surveiller les modèles en production et détecter la dérive

## Public visé

Data scientists et praticiens ML qui ont entraîné des modèles en notebook mais n'en ont jamais déployé un. Ingénieurs logiciels qui passent à l'infrastructure ML. Ingénieurs de recherche responsables de la reproductibilité et du déploiement. Ingénieurs DevOps qui doivent supporter des charges de travail ML.

**Prérequis :**

- Programmation Python (à l'aise avec les fonctions, classes, packages)
- Bases du machine learning (entraînement, évaluation, scikit-learn ou équivalent)
- Familiarité avec la ligne de commande (terminal, commandes shell de base)
- Ordinateur portable avec Docker Desktop installé ([docker.com](https://www.docker.com/products/docker-desktop/))

## Plaquette

Les notes de cours et notebooks sont accessibles depuis la barre latérale.

Pour une plaquette d'une page, à transmettre à un comité de programme, un organisateur de conférence ou une équipe formation interne, écrivez à <a href="mailto:gabayae2@gmail.com?subject=Demande%20de%20plaquette%20%E2%80%94%20MLOps%20en%20Pratique">gabayae2@gmail.com</a> en précisant la taille de l'audience et les dates envisagées.
