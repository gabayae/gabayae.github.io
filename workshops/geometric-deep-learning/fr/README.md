---
layout: workshop
permalink: /workshops/geometric-deep-learning/fr/
lang: fr
title: "Apprentissage Géométrique Profond"
tagline: "Des réseaux de neurones sur graphes, variétés et nuages de points — ancrés dans la théorie des groupes, la géométrie différentielle et la topologie."
description: "Atelier de 4 jours : GNNs, apprentissage sur variétés, architectures équivariantes."

# --- Métadonnées de la barre latérale ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "4 jours (≈ 24 heures)"
level: "Avancé"
format: "Sur site, en ligne en direct, ou hybride"
languages: "Français &amp; anglais"
certificate: "Certificat de complétion"

# --- Liens des supports ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/geometric-deep-learning

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Demande d'atelier — Apprentissage Géométrique Profond"
---

## Présentation du programme

Cet atelier explore les fondements mathématiques et les applications pratiques de l'apprentissage géométrique profond — des réseaux de neurones qui opèrent sur des graphes, variétés, nuages de points et autres domaines non-euclidiens. Ancré dans la théorie des groupes, la géométrie différentielle et la topologie, les participants apprennent à construire et appliquer des réseaux de neurones sur graphes (GNN), des architectures équivariantes et des modèles adaptés aux variétés.

### Logiciels requis

- Python 3.10+
- PyTorch 2.0+
- PyTorch Geometric (torch-geometric)
- Bibliothèques : networkx, matplotlib, rdkit (données moléculaires), open3d (nuages de points)
- Optionnel : wandb pour le suivi d'expériences

### Jour 1 — Fondements : graphes, symétrie & passage de messages

**Objectifs :** comprendre pourquoi la géométrie compte pour le deep learning et implémenter des GNN de base.

- **Pourquoi l'apprentissage géométrique profond ?** — limites des MLP et CNN sur les données non-euclidiennes. Le plan GDL : domaines (grilles, graphes, groupes, variétés), symétries et les 5G du GDL.
- **Théorie des groupes pour le deep learning** — groupes de symétrie, invariance vs. équivariance, pourquoi les CNN sont équivariants par translation, extension à d'autres symétries.
- **Représentations de graphes** — matrices d'adjacence, listes d'arêtes, features de nœuds/arêtes, features de graphes. Construire des graphes à partir de données réelles. Bases de NetworkX.
- **Réseaux à passage de messages (MPNN)** — le framework MPNN : message, agrégation, mise à jour. Invariance/équivariance par permutation. GCN (Kipf & Welling), GraphSAGE, GIN.
- **Bases de PyTorch Geometric** — objets Data, DataLoader, construire un GNN depuis zéro avec la classe de base MessagePassing, exemple du Karate Club.

**TP 1 :** implémenter un GCN depuis zéro avec le framework MPNN. Puis utiliser PyTorch Geometric pour construire et entraîner un modèle de classification de nœuds sur le réseau de citations Cora. Visualiser les embeddings de nœuds appris avec t-SNE.

### Jour 2 — Méthodes spectrales & architectures avancées

**Objectifs :** comprendre la perspective spectrale des convolutions sur graphes et les designs GNN avancés.

- **Théorie spectrale des graphes** — Laplacien de graphe, valeurs et vecteurs propres, décomposition spectrale, transformée de Fourier sur graphes, polynômes de Chebyshev, convolutions spectrales vs. spatiales.
- **Attention sur les graphes** — Graph Attention Networks (GAT) : attention multi-têtes, coefficients d'attention, comparaison avec GCN. Architectures de type Transformer pour les graphes.
- **Tâches au niveau graphe** — pooling global (mean, sum, max), pooling hiérarchique (DiffPool, TopKPool, SAGPool), fonctions de readout, pipelines de classification de graphes.
- **Surlissage & expressivité** — le problème du surlissage dans les GNN profonds, le test WL et l'expressivité des GNN, skip connections, JumpingKnowledge, encodages positionnels.

**TP 2 :** construire un pipeline de classification de graphes avec PyTorch Geometric : charger un dataset moléculaire (MUTAG ou PROTEINS), implémenter le pooling global et hiérarchique, entraîner et évaluer. Expérimenter avec la profondeur et les stratégies de pooling.

### Jour 3 — Variétés, nuages de points & équivariance

**Objectifs :** étendre le deep learning aux variétés, nuages de points et concevoir des architectures équivariantes.

- **Apprentissage sur les variétés** — maillages, surfaces, géométrie intrinsèque vs. extrinsèque. Distances géodésiques, noyaux de chaleur, opérateur de Laplace-Beltrami. MeshCNN et DiffusionNet.
- **Traitement de nuages de points** — PointNet et PointNet++ : fonctions symétriques pour l'invariance par permutation, agrégation de features locales, traitement hiérarchique. DGCNN.
- **Réseaux de neurones équivariants** — équivariance SE(3), Tensor Field Networks, EGNN, SchNet pour la dynamique moléculaire. Pourquoi l'équivariance améliore l'efficacité des données.
- **Features topologiques pour le GDL** — homologie persistante comme features de nœuds/graphes, apprentissage de filtrations, TopologyLayer, combiner TDA et GNN.

**TP 3 :** implémenter un classificateur de nuages de points avec PointNet (depuis zéro en PyTorch) sur ModelNet10 ou ShapeNet. Puis augmenter un GNN avec des features topologiques (nombres de Betti, statistiques de persistance) et mesurer l'amélioration.

### Jour 4 — Applications & projet final

**Objectifs :** appliquer le GDL à des domaines réels et compléter un projet final.

- **Prédiction de propriétés moléculaires** — graphes moléculaires, conversion SMILES vers graphe, dataset QM9, SchNet, DimeNet, SphereNet. Applications en découverte de médicaments.
- **Analyse de réseaux sociaux** — détection de communautés avec GNN, prédiction de liens, influence de nœuds, graphes temporels, graphes hétérogènes.
- **Autres applications** — prédiction de structure protéique (contexte AlphaFold), prédiction de trafic, systèmes de recommandation, simulation physique, prévision météo.
- **Travail sur le projet final** — implémenter un pipeline GDL complet sur une application choisie.
- **Présentations & bilan** — démos des projets, discussion sur les frontières du GDL, ressources, certificats.

**TP 4 (projet final) :** choisir un projet :
- **Moléculaire :** prédire des propriétés moléculaires (solubilité, toxicité) avec des GNN sur MoleculeNet.
- **Social :** détection de communautés ou prédiction de liens sur un vrai dataset de réseau social.
- **3D :** classification ou segmentation de nuages de points sur ModelNet/ShapeNet.
- **Personnalisé :** appliquer le GDL à un problème de votre recherche avec construction de graphe appropriée.

### Évaluation

- **TPs quotidiens** (40 %) — implémentations fonctionnelles et analyse.
- **Projet final** (40 %) — application GDL complète avec évaluation.
- **Participation** (20 %) — engagement, devoirs et discussions.

### Ressources

- [Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, Gauges (Bronstein et al.)](https://geometricdeeplearning.com/)
- [Documentation PyTorch Geometric](https://pytorch-geometric.readthedocs.io/)
- [Graph Representation Learning Book (Hamilton)](https://www.cs.mcgill.ca/~wlh/grl_book/)
- [The Shape of Data](https://nostarch.com/shapeofdata)
- [Stanford CS224W: Machine Learning with Graphs](http://web.stanford.edu/class/cs224w/)

## Objectifs pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Comprendre les principes mathématiques du GDL (symétrie, invariance, équivariance).
2. Implémenter des réseaux à passage de messages et des variantes de GNN.
3. Travailler avec PyTorch Geometric pour des tâches au niveau nœud et graphe.
4. Appliquer les méthodes spectrales et spatiales pour les convolutions sur graphes.
5. Comprendre l'apprentissage sur variétés et les architectures équivariantes.
6. Appliquer le GDL à des problèmes réels (prédiction de propriétés moléculaires, analyse de réseaux sociaux, classification de nuages de points).

## Public visé

Praticiens et chercheurs ML avancés qui travaillent sur des données non-euclidiennes : graphes moléculaires, réseaux sociaux, formes 3D, maillages, nuages de points. Étudiants de master/doctorat en chimie computationnelle, découverte de médicaments, vision par ordinateur ou science des réseaux. Ingénieurs construisant des systèmes de recommandation ou des systèmes qui raisonnent sur des données relationnelles. Chercheurs en physique, biologie ou chimie qui veulent appliquer des architectures équivariantes.

**Prérequis :**

- Programmation Python avec PyTorch (tenseurs, autograd, nn.Module).
- Algèbre linéaire (valeurs propres, décomposition spectrale).
- Bases du machine learning (boucles d'entraînement, fonctions de perte, optimisation).
- La théorie des graphes de base (nœuds, arêtes, matrices d'adjacence) est utile mais non requise.

## Plaquette

Les notes de cours et notebooks sont accessibles depuis la barre latérale.

Pour une plaquette d'une page, à transmettre à un comité de programme, un organisateur de conférence ou une équipe formation interne, écrivez à <a href="mailto:gabayae2@gmail.com?subject=Demande%20de%20plaquette%20%E2%80%94%20Apprentissage%20G%C3%A9om%C3%A9trique%20Profond">gabayae2@gmail.com</a> en précisant la taille de l'audience et les dates envisagées.
