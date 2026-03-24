# MLOps en Pratique — Atelier de 4 jours

**Formateur :** Dr. Yaé Ulrich Gaba
**Durée :** 4 jours (24 heures)
**Niveau :** Intermédiaire à Avancé
**Langue :** Français

---

## Présentation

Cet atelier comble le fossé entre les expériences en notebook et les systèmes ML en production. Les participants apprennent à packager, déployer, surveiller et maintenir des modèles de machine learning avec des outils standards de l'industrie. L'accent est mis sur des workflows pratiques et reproductibles fonctionnant dans des environnements à ressources limitées — y compris des configurations sans cloud pertinentes pour les contextes africains.

## Prérequis

- Programmation Python (à l'aise avec les fonctions, classes, packages)
- Bases du machine learning (entraînement, évaluation, scikit-learn ou équivalent)
- Familiarité avec la ligne de commande (terminal, commandes shell de base)
- Ordinateur portable avec Docker Desktop installé ([docker.com](https://www.docker.com/products/docker-desktop/))

## Objectifs Pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Structurer des projets ML pour la reproductibilité et la collaboration
2. Suivre les expériences systématiquement avec MLflow
3. Versionner les données et modèles avec DVC
4. Conteneuriser les applications ML avec Docker
5. Construire des pipelines CI/CD pour les tests et le déploiement automatisés
6. Surveiller les modèles en production et détecter la dérive

## Logiciels Requis

- Python 3.10+, pip, virtualenv
- Docker Desktop
- Git
- Bibliothèques : mlflow, dvc, fastapi, uvicorn, pytest, great-expectations
- Optionnel : compte GitHub, fournisseur cloud (niveaux gratuits suffisent)

---

## Programme Jour par Jour

### Jour 1 : Structure de Projet & Suivi d'Expériences

**Objectifs :** Organiser les projets ML pour la reproductibilité et suivre les expériences systématiquement.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:00 | **Le Problème MLOps** — Pourquoi les notebooks échouent en production, le cycle de vie ML, la dette technique dans les systèmes ML, niveaux de maturité MLOps |
| 10:00–10:45 | **Structure de Projet** — Template Cookiecutter Data Science, séparation config/données/code/modèles, gestion d'environnement (virtualenv, conda), fichiers requirements, patterns Makefile |
| 10:45–11:00 | *Pause* |
| 11:00–12:30 | **Suivi d'Expériences avec MLflow** — Installation, journalisation des paramètres/métriques/artefacts, comparaison des runs, interface MLflow, organisation des expériences |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Versioning de Données & Modèles avec DVC** — Git pour les données, DVC init, ajout de fichiers, stockage distant (local, S3, GCS), pipelines avec dvc.yaml, reproduction des expériences |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Gestion de Configuration** — Hydra / OmegaConf pour gérer les hyperparamètres, fichiers de config vs. overrides en ligne de commande, configurations reproductibles |

**TP 1 :** Prendre un notebook Jupyter désordonné (fourni) et le refactorer en un projet propre : structure de répertoires, fichiers de config, suivi MLflow, pipeline DVC. Lancer 5 expériences avec différents hyperparamètres et les comparer dans l'interface MLflow.

**Devoir :** Appliquer la même structure à l'un de vos propres projets ML.

---

### Jour 2 : Conteneurisation & APIs

**Objectifs :** Packager les modèles en conteneurs Docker et les servir via des APIs REST.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Fondamentaux de Docker** — Images vs. conteneurs, anatomie d'un Dockerfile, construction d'images, exécution de conteneurs, mapping de ports, volumes, .dockerignore |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Dockeriser des Applications ML** — Images de base Python, installation de dépendances, copie d'artefacts modèle, builds multi-étapes pour des images plus petites, bases du support GPU |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Servir des Modèles avec FastAPI** — Construire une API de prédiction : endpoints, modèles requête/réponse (Pydantic), chargement du modèle au démarrage, prédiction par lots, endpoints async, docs automatiques (Swagger) |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Docker Compose** — Applications multi-conteneurs : API + base de données + serveur MLflow. docker-compose.yml, réseau, variables d'environnement, health checks |

**TP 2 :** Construire une stack complète de serving : entraîner un modèle, le sauver avec MLflow, l'encapsuler dans une application FastAPI, conteneuriser avec Docker, orchestrer avec Docker Compose (API + MLflow UI). Tester l'endpoint avec curl et Python requests.

**Devoir :** Ajouter la validation des entrées et la gestion d'erreurs à votre API.

---

### Jour 3 : Tests & CI/CD

**Objectifs :** Tester le code ML et automatiser les pipelines avec l'intégration continue.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Tester les Systèmes ML** — Tests unitaires (pytest), tester les fonctions de traitement de données, tester les prédictions, fixtures, parametrize, mocking |
| 10:30–10:45 | *Pause* |
| 10:45–12:00 | **Validation des Données** — Great Expectations : définir des attentes, valider des datasets, contrats de données, attraper les problèmes de qualité avant le modèle |
| 12:00–12:30 | **Validation du Modèle** — Seuils de performance, tests de régression, comparaison avec la baseline, smoke tests pour les endpoints |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **CI/CD avec GitHub Actions** — Fichiers workflow, déclencheurs, jobs et steps, exécution des tests à chaque push, construction d'images Docker, secrets, cache d'artefacts |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Pipelines ML Automatisés** — De bout en bout : push code → tests → validation données → entraînement → évaluation → construction conteneur → déploiement. Workflows par branches (dev/staging/prod) |

**TP 3 :** Mettre en place un pipeline CI/CD complet pour le modèle du Jour 2 : écrire des tests unitaires, ajouter la validation des données, créer un workflow GitHub Actions qui lance les tests, entraîne le modèle et construit une image Docker à chaque push.

**Devoir :** Ajouter une barrière de performance — le pipeline doit échouer si la précision descend sous un seuil.

---

### Jour 4 : Monitoring, Détection de Dérive & Production

**Objectifs :** Surveiller les modèles déployés et gérer les défis de production.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Monitoring de Modèles** — Quoi surveiller : latence de prédiction, taux d'erreur, distributions d'entrée/sortie. Stratégies de logging et d'alertes. Bases de Prometheus + Grafana |
| 10:30–10:45 | *Pause* |
| 10:45–12:00 | **Dérive des Données & du Modèle** — Dérive conceptuelle, dérive de données, dérive de features. Méthodes de détection : PSI, test KS, Evidently AI. Quand réentraîner, déclencheurs automatiques |
| 12:00–12:30 | **Tests A/B & Déploiement Shadow** — Releases canary, mode shadow, feature flags pour ML, comparaison de versions en production |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:00 | **Patterns de Production** — Registres de modèles (MLflow), déploiement blue-green, stratégies de rollback, inférence batch vs. temps réel, considérations de mise à l'échelle |
| 15:00–15:15 | *Pause* |
| 15:15–16:15 | **MLOps en Environnements à Ressources Limitées** — Stratégies pour infrastructure limitée : serving léger (Flask + systemd), réentraînement par cron, serveurs MLflow locaux, DVC avec remotes locaux, déploiement edge |
| 16:15–17:00 | **Présentations & Bilan** — Présentation des pipelines MLOps complets, discussion, questions, certificats |

**TP 4 (Projet Final) :** Ajouter le monitoring au modèle déployé : implémenter la détection de dérive avec Evidently AI, configurer les alertes basiques, créer un tableau de bord montrant les métriques de santé du modèle. Présenter le pipeline complet : code → test → build → déploiement → monitoring.

---

## Évaluation

- **TPs quotidiens** (50 %) — Pipelines et infrastructure fonctionnels
- **Pipeline final** (30 %) — Système MLOps complet démontré le Jour 4
- **Participation** (20 %) — Engagement et devoirs

## Ressources

- [Documentation MLflow](https://mlflow.org/docs/latest/index.html)
- [Documentation DVC](https://dvc.org/doc)
- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Documentation Docker](https://docs.docker.com/)
- [Evidently AI](https://www.evidentlyai.com/)
- [Made With ML — Cours MLOps](https://madewithml.com/)

## Certificat

Les participants ayant complété tous les TPs et le pipeline final reçoivent un certificat de complétion.
