# Apprentissage par Renforcement : de la Théorie à la Pratique — Atelier de 5 jours

**Formateur :** Dr. Yaé Ulrich Gaba
**Durée :** 5 jours (30 heures)
**Niveau :** Intermédiaire à Avancé
**Langue :** Français

---

## Présentation

Cet atelier offre une introduction rigoureuse et pratique à l'apprentissage par renforcement (RL), reliant les fondements mathématiques — y compris les perspectives topologiques et métriques — aux algorithmes modernes de deep RL. Les participants implémentent des méthodes RL classiques et profondes depuis zéro, les appliquent à des problèmes concrets et acquièrent une compréhension des structures mathématiques sous-jacentes à la convergence et l'optimalité.

## Prérequis

- Programmation Python (à l'aise avec NumPy, classes, POO de base)
- Bases d'algèbre linéaire (vecteurs, matrices, valeurs propres)
- Probabilités et statistiques (distributions, espérance, probabilité conditionnelle)
- Familiarité avec les réseaux de neurones (passe avant, concepts de rétropropagation)

## Objectifs Pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Formaliser des problèmes de décision séquentielle comme des processus de décision de Markov (MDP)
2. Implémenter des algorithmes RL tabulaires (programmation dynamique, Q-learning, SARSA)
3. Comprendre les garanties de convergence à travers la théorie des points fixes
4. Construire des agents de deep RL (DQN, gradient de politique, acteur-critique)
5. Appliquer le RL à des problèmes pratiques (allocation de ressources, jeux, optimisation)
6. Évaluer et déboguer des systèmes RL

## Logiciels Requis

- Python 3.10+
- Bibliothèques : numpy, gymnasium, matplotlib, torch (PyTorch), stable-baselines3
- Optionnel : tensorboard, wandb

---

## Programme Jour par Jour

### Jour 1 : Fondements — MDP & Programmation Dynamique

**Objectifs :** Formaliser les problèmes RL et résoudre exactement de petits MDP.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:00 | **Qu'est-ce que le RL ?** — La boucle agent-environnement, hypothèse de la récompense, comparaison avec l'apprentissage supervisé/non supervisé, panorama des applications |
| 10:00–10:45 | **Processus de Décision de Markov** — États, actions, transitions, récompenses, facteur d'actualisation $$\gamma$$, politiques, fonctions de valeur $$V^\pi(s)$$ et $$Q^\pi(s,a)$$ |
| 10:45–11:00 | *Pause* |
| 11:00–12:30 | **Équations de Bellman** — Équation d'espérance de Bellman, équation d'optimalité de Bellman, l'opérateur de Bellman $$\mathcal{T}$$ comme application contractante |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Programmation Dynamique** — Évaluation de politique (itérative), amélioration de politique, itération de politique, itération de valeur. Preuves de convergence via le théorème du point fixe de Banach |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Implémentation** — Coder un environnement GridWorld et le résoudre avec l'itération de politique et de valeur. Visualiser les fonctions de valeur et les politiques optimales |

**TP 1 :** Implémenter un solveur MDP complet : définir un GridWorld avec obstacles et récompenses, implémenter l'évaluation de politique, l'amélioration de politique et l'itération de valeur. Visualiser la politique optimale sous forme de flèches sur la grille.

**Devoir :** Résoudre un autre MDP (ex. : FrozenLake de Gymnasium) avec vos implémentations.

---

### Jour 2 : Méthodes Tabulaires — MC, TD, Q-Learning

**Objectifs :** Apprendre les méthodes RL sans modèle qui fonctionnent sans connaître la dynamique de l'environnement.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Méthodes de Monte Carlo** — MC première visite vs. chaque visite, prédiction MC, contrôle MC avec exploration ε-greedy, échantillonnage d'importance |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Apprentissage par Différence Temporelle** — Prédiction TD(0), l'erreur TD $$\delta_t$$, SARSA (contrôle TD on-policy), Q-Learning (contrôle TD off-policy), comparaison de convergence |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Exploration vs. Exploitation** — ε-greedy, softmax, UCB, initialisation optimiste. Le dilemme exploration-exploitation. Bandits multi-bras comme cas particulier |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Perspective du Point Fixe** — L'opérateur de Bellman comme contraction dans les espaces métriques, vitesses de convergence, connexions aux structures quasi-métriques, pourquoi Q-learning converge |

**TP 2 :** Implémenter Q-Learning et SARSA depuis zéro. Entraîner des agents sur des environnements Gymnasium (Taxi-v3, CliffWalking). Comparer les courbes d'apprentissage, explorer l'effet de ε, α et γ sur la convergence.

**Devoir :** Implémenter le TD n-étapes et comparer avec le TD 1-étape sur le même environnement.

---

### Jour 3 : Deep RL — DQN & Extensions

**Objectifs :** Passer à l'échelle avec l'approximation de fonctions par réseaux de neurones.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Approximation de Fonctions** — Pourquoi les méthodes tabulaires ne passent pas à l'échelle, approximation linéaire, la triade mortelle (approximation + bootstrapping + off-policy), réseaux de neurones comme approximateurs |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Deep Q-Networks (DQN)** — Replay d'expérience, réseaux cibles, la loss DQN, schedules de décroissance de ε. Implémentation avec PyTorch |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Extensions DQN** — Double DQN, Dueling DQN, Replay d'Expérience Priorisé, Noisy Nets, Rainbow DQN (vue d'ensemble) |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **DQN en Pratique** — Réglage des hyperparamètres, astuces de débogage, modes d'échec courants, quand DQN fonctionne bien et quand non |

**TP 3 :** Implémenter DQN depuis zéro en PyTorch. Entraîner sur CartPole-v1 et LunarLander-v2. Implémenter Double DQN et comparer les performances. Logger les courbes d'entraînement avec TensorBoard.

**Devoir :** Entraîner DQN sur un nouvel environnement et analyser les Q-values apprises.

---

### Jour 4 : Gradient de Politique & Méthodes Acteur-Critique

**Objectifs :** Apprendre les méthodes basées sur la politique et les algorithmes acteur-critique modernes.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Méthodes de Gradient de Politique** — Pourquoi optimiser directement les politiques, théorème du gradient de politique, algorithme REINFORCE, réduction de variance avec baselines |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Méthodes Acteur-Critique** — Fonction d'avantage $$A(s,a)$$, A2C, GAE (Estimation Généralisée de l'Avantage), régularisation par entropie |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **PPO — Proximal Policy Optimization** — Objectif surrogate clippé, régions de confiance (intuition), implémentation de PPO, pourquoi PPO est le standard du RL moderne |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Stable-Baselines3** — Prototypage rapide avec SB3 : PPO, A2C, SAC. Environnements personnalisés, callbacks, évaluation, réglage des hyperparamètres avec Optuna |

**TP 4 :** Implémenter REINFORCE depuis zéro. Puis utiliser Stable-Baselines3 pour entraîner PPO sur des tâches de contrôle continu (MountainCarContinuous, Pendulum). Comparer l'efficacité en échantillons et la stabilité entre algorithmes.

**Devoir :** Entraîner un agent PPO sur un environnement personnalisé pertinent pour votre recherche.

---

### Jour 5 : Applications & Sujets Avancés

**Objectifs :** Appliquer le RL à des problèmes réels et explorer les directions de pointe.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Présentations des devoirs** |
| 09:30–10:30 | **RL pour l'Allocation de Ressources** — Optimisation de réseaux sans fil (DQN pour l'allocation de canaux), gestion de réseaux énergétiques, problèmes d'ordonnancement. Connexion aux recherches du formateur |
| 10:30–10:45 | *Pause* |
| 10:45–12:00 | **RL Multi-Agents** — Apprenants indépendants, entraînement centralisé avec exécution décentralisée (CTDE), communication, settings coopératifs vs. compétitifs |
| 12:00–12:30 | **Perspectives Topologiques sur le RL** — Topologie des espaces d'états/actions/politiques, comment la structure topologique affecte la convergence, connexions aux recherches du formateur sur les fondements du RL |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Panorama des Sujets Avancés** — RL basé modèle, RL offline, reward shaping, RL inverse, RLHF, RL sûr |
| 15:30–15:45 | *Pause* |
| 15:45–16:30 | **Travail sur le Projet Final** — Finaliser et peaufiner les projets |
| 16:30–17:00 | **Présentations & Bilan** — Démos des projets, discussion, ressources, certificats |

**TP 5 (Projet Final) :** Choisir un projet :
- **Allocateur de ressources :** agent DQN pour l'allocation de canaux dans un réseau sans fil
- **Agent de jeu :** entraîner un agent à jouer à un jeu Atari classique avec DQN ou PPO
- **Système de contrôle :** agent PPO pour une tâche de contrôle continu avec reward shaping personnalisé
- **Application personnalisée :** appliquer le RL à un problème de votre propre domaine de recherche

---

## Évaluation

- **TPs quotidiens** (40 %) — Implémentations fonctionnelles et analyse
- **Projet final** (40 %) — Application RL complète avec évaluation
- **Participation** (20 %) — Engagement, devoirs et discussions

## Ressources

- [Sutton & Barto — Reinforcement Learning: An Introduction (2e éd.)](http://incompleteideas.net/book/the-book-2nd.html)
- [Documentation Stable-Baselines3](https://stable-baselines3.readthedocs.io/)
- [Documentation Gymnasium](https://gymnasium.farama.org/)
- [Spinning Up in Deep RL (OpenAI)](https://spinningup.openai.com/)
- [Topological Foundations of RL (Gaba, 2024)](https://arxiv.org/abs/2410.03706)
- [The Shape of Data](https://nostarch.com/shapeofdata)

## Certificat

Les participants ayant complété tous les TPs et le projet final reçoivent un certificat de complétion.
