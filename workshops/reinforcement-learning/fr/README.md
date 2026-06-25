---
layout: workshop
permalink: /workshops/reinforcement-learning/fr/
lang: fr
title: "Apprentissage par Renforcement : de la Théorie à la Pratique"
tagline: "Des MDPs et de la théorie du point fixe à DQN, PPO et aux perspectives topologiques sur la convergence — implémenté depuis zéro."
description: "Atelier de 5 jours : MDPs, Q-learning, DQN, policy gradients, acteur-critique."

# --- Métadonnées de la barre latérale ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "5 jours (≈ 30 heures)"
level: "Intermédiaire à Avancé"
format: "Sur site, en ligne en direct, ou hybride"
languages: "Français &amp; anglais"
certificate: "Certificat de complétion"

# --- Liens des supports ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/reinforcement-learning

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Demande d'atelier — Apprentissage par Renforcement : de la Théorie à la Pratique"
---

## Présentation du programme

Cet atelier offre une introduction rigoureuse et pratique à l'apprentissage par renforcement (RL), reliant les fondements mathématiques — y compris les perspectives topologiques et métriques — aux algorithmes modernes de deep RL. Les participants implémentent des méthodes RL classiques et profondes depuis zéro, les appliquent à des problèmes concrets et acquièrent une compréhension des structures mathématiques sous-jacentes à la convergence et l'optimalité.

### Logiciels Requis

- Python 3.10+
- Bibliothèques : numpy, gymnasium, matplotlib, torch (PyTorch), stable-baselines3
- Optionnel : tensorboard, wandb

### Jour 1 : Fondements — MDP & Programmation Dynamique

**Objectifs :** Formaliser les problèmes RL et résoudre exactement de petits MDP.

- **Qu'est-ce que le RL ?** — La boucle agent-environnement, hypothèse de la récompense, comparaison avec l'apprentissage supervisé/non supervisé, panorama des applications
- **Processus de Décision de Markov** — États, actions, transitions, récompenses, facteur d'actualisation $$\gamma$$, politiques, fonctions de valeur $$V^\pi(s)$$ et $$Q^\pi(s,a)$$
- **Équations de Bellman** — Équation d'espérance de Bellman, équation d'optimalité de Bellman, l'opérateur de Bellman $$\mathcal{T}$$ comme application contractante
- **Programmation Dynamique** — Évaluation de politique (itérative), amélioration de politique, itération de politique, itération de valeur. Preuves de convergence via le théorème du point fixe de Banach
- **Implémentation** — Coder un environnement GridWorld et le résoudre avec l'itération de politique et de valeur. Visualiser les fonctions de valeur et les politiques optimales

**TP 1 :** Implémenter un solveur MDP complet : définir un GridWorld avec obstacles et récompenses, implémenter l'évaluation de politique, l'amélioration de politique et l'itération de valeur. Visualiser la politique optimale sous forme de flèches sur la grille.

**Devoir :** Résoudre un autre MDP (ex. : FrozenLake de Gymnasium) avec vos implémentations.

### Jour 2 : Méthodes Tabulaires — MC, TD, Q-Learning

**Objectifs :** Apprendre les méthodes RL sans modèle qui fonctionnent sans connaître la dynamique de l'environnement.

- **Méthodes de Monte Carlo** — MC première visite vs. chaque visite, prédiction MC, contrôle MC avec exploration ε-greedy, échantillonnage d'importance
- **Apprentissage par Différence Temporelle** — Prédiction TD(0), l'erreur TD $$\delta_t$$, SARSA (contrôle TD on-policy), Q-Learning (contrôle TD off-policy), comparaison de convergence
- **Exploration vs. Exploitation** — ε-greedy, softmax, UCB, initialisation optimiste. Le dilemme exploration-exploitation. Bandits multi-bras comme cas particulier
- **Perspective du Point Fixe** — L'opérateur de Bellman comme contraction dans les espaces métriques, vitesses de convergence, connexions aux structures quasi-métriques, pourquoi Q-learning converge

**TP 2 :** Implémenter Q-Learning et SARSA depuis zéro. Entraîner des agents sur des environnements Gymnasium (Taxi-v3, CliffWalking). Comparer les courbes d'apprentissage, explorer l'effet de ε, α et γ sur la convergence.

**Devoir :** Implémenter le TD n-étapes et comparer avec le TD 1-étape sur le même environnement.

### Jour 3 : Deep RL — DQN & Extensions

**Objectifs :** Passer à l'échelle avec l'approximation de fonctions par réseaux de neurones.

- **Approximation de Fonctions** — Pourquoi les méthodes tabulaires ne passent pas à l'échelle, approximation linéaire, la triade mortelle (approximation + bootstrapping + off-policy), réseaux de neurones comme approximateurs
- **Deep Q-Networks (DQN)** — Replay d'expérience, réseaux cibles, la loss DQN, schedules de décroissance de ε. Implémentation avec PyTorch
- **Extensions DQN** — Double DQN, Dueling DQN, Replay d'Expérience Priorisé, Noisy Nets, Rainbow DQN (vue d'ensemble)
- **DQN en Pratique** — Réglage des hyperparamètres, astuces de débogage, modes d'échec courants, quand DQN fonctionne bien et quand non

**TP 3 :** Implémenter DQN depuis zéro en PyTorch. Entraîner sur CartPole-v1 et LunarLander-v2. Implémenter Double DQN et comparer les performances. Logger les courbes d'entraînement avec TensorBoard.

**Devoir :** Entraîner DQN sur un nouvel environnement et analyser les Q-values apprises.

### Jour 4 : Gradient de Politique & Méthodes Acteur-Critique

**Objectifs :** Apprendre les méthodes basées sur la politique et les algorithmes acteur-critique modernes.

- **Méthodes de Gradient de Politique** — Pourquoi optimiser directement les politiques, théorème du gradient de politique, algorithme REINFORCE, réduction de variance avec baselines
- **Méthodes Acteur-Critique** — Fonction d'avantage $$A(s,a)$$, A2C, GAE (Estimation Généralisée de l'Avantage), régularisation par entropie
- **PPO — Proximal Policy Optimization** — Objectif surrogate clippé, régions de confiance (intuition), implémentation de PPO, pourquoi PPO est le standard du RL moderne
- **Stable-Baselines3** — Prototypage rapide avec SB3 : PPO, A2C, SAC. Environnements personnalisés, callbacks, évaluation, réglage des hyperparamètres avec Optuna

**TP 4 :** Implémenter REINFORCE depuis zéro. Puis utiliser Stable-Baselines3 pour entraîner PPO sur des tâches de contrôle continu (MountainCarContinuous, Pendulum). Comparer l'efficacité en échantillons et la stabilité entre algorithmes.

**Devoir :** Entraîner un agent PPO sur un environnement personnalisé pertinent pour votre recherche.

### Jour 5 : Applications & Sujets Avancés

**Objectifs :** Appliquer le RL à des problèmes réels et explorer les directions de pointe.

- **RL pour l'Allocation de Ressources** — Optimisation de réseaux sans fil (DQN pour l'allocation de canaux), gestion de réseaux énergétiques, problèmes d'ordonnancement. Connexion aux recherches du formateur
- **RL Multi-Agents** — Apprenants indépendants, entraînement centralisé avec exécution décentralisée (CTDE), communication, settings coopératifs vs. compétitifs
- **Perspectives Topologiques sur le RL** — Topologie des espaces d'états/actions/politiques, comment la structure topologique affecte la convergence, connexions aux recherches du formateur sur les fondements du RL
- **Panorama des Sujets Avancés** — RL basé modèle, RL offline, reward shaping, RL inverse, RLHF, RL sûr
- **Travail sur le Projet Final** — Finaliser et peaufiner les projets
- **Présentations & Bilan** — Démos des projets, discussion, ressources, certificats

**TP 5 (Projet Final) :** Choisir un projet :
- **Allocateur de ressources :** agent DQN pour l'allocation de canaux dans un réseau sans fil
- **Agent de jeu :** entraîner un agent à jouer à un jeu Atari classique avec DQN ou PPO
- **Système de contrôle :** agent PPO pour une tâche de contrôle continu avec reward shaping personnalisé
- **Application personnalisée :** appliquer le RL à un problème de votre propre domaine de recherche

### Évaluation

- **TPs quotidiens** (40 %) — Implémentations fonctionnelles et analyse
- **Projet final** (40 %) — Application RL complète avec évaluation
- **Participation** (20 %) — Engagement, devoirs et discussions

### Ressources

- [Sutton & Barto — Reinforcement Learning: An Introduction (2e éd.)](http://incompleteideas.net/book/the-book-2nd.html)
- [Documentation Stable-Baselines3](https://stable-baselines3.readthedocs.io/)
- [Documentation Gymnasium](https://gymnasium.farama.org/)
- [Spinning Up in Deep RL (OpenAI)](https://spinningup.openai.com/)
- [Topological Foundations of RL (Gaba, 2024)](https://arxiv.org/abs/2410.03706)
- [The Shape of Data](https://nostarch.com/shapeofdata)

## Objectifs pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Formaliser des problèmes de décision séquentielle comme des processus de décision de Markov (MDP)
2. Implémenter des algorithmes RL tabulaires (programmation dynamique, Q-learning, SARSA)
3. Comprendre les garanties de convergence à travers la théorie des points fixes
4. Construire des agents de deep RL (DQN, gradient de politique, acteur-critique)
5. Appliquer le RL à des problèmes pratiques (allocation de ressources, jeux, optimisation)
6. Évaluer et déboguer des systèmes RL

## Public visé

Praticiens ML et chercheurs qui veulent une base rigoureuse en théorie RL avec une expérience pratique d'implémentation. Doctorants travaillant sur des problèmes de décision séquentielle, contrôle ou optimisation. Ingénieurs construisant des agents pour les jeux, la robotique, l'ordonnancement ou l'allocation de ressources. Chercheurs intéressés par les fondements mathématiques (théorie du point fixe, topologie) du RL moderne.

**Prérequis :**

- Programmation Python (à l'aise avec NumPy, classes, POO de base)
- Bases d'algèbre linéaire (vecteurs, matrices, valeurs propres)
- Probabilités et statistiques (distributions, espérance, probabilité conditionnelle)
- Familiarité avec les réseaux de neurones (passe avant, concepts de rétropropagation)

## Plaquette

Les notes de cours et notebooks sont accessibles depuis la barre latérale.

Pour une plaquette d'une page, à transmettre à un comité de programme, un organisateur de conférence ou une équipe formation interne, écrivez à <a href="mailto:gabayae2@gmail.com?subject=Demande%20de%20plaquette%20%E2%80%94%20Apprentissage%20par%20Renforcement%20%3A%20de%20la%20Th%C3%A9orie%20%C3%A0%20la%20Pratique">gabayae2@gmail.com</a> en précisant la taille de l'audience et les dates envisagées.
