# Apprentissage Géométrique Profond — Atelier de 4 jours

**Formateur :** Dr. Yaé Ulrich Gaba
**Durée :** 4 jours (24 heures)
**Niveau :** Avancé
**Langue :** Français

---

## Présentation

Cet atelier explore les fondements mathématiques et les applications pratiques de l'apprentissage géométrique profond — des réseaux de neurones qui opèrent sur des graphes, variétés, nuages de points et autres domaines non-euclidiens. Ancré dans la théorie des groupes, la géométrie différentielle et la topologie, les participants apprennent à construire et appliquer des réseaux de neurones sur graphes (GNN), des architectures équivariantes et des modèles adaptés aux variétés.

## Prérequis

- Programmation Python avec PyTorch (tenseurs, autograd, nn.Module)
- Algèbre linéaire (valeurs propres, décomposition spectrale)
- Bases du machine learning (boucles d'entraînement, fonctions de perte, optimisation)
- La théorie des graphes de base (nœuds, arêtes, matrices d'adjacence) est utile mais non requise

## Objectifs Pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Comprendre les principes mathématiques du GDL (symétrie, invariance, équivariance)
2. Implémenter des réseaux à passage de messages et des variantes de GNN
3. Travailler avec PyTorch Geometric pour des tâches au niveau nœud et graphe
4. Appliquer les méthodes spectrales et spatiales pour les convolutions sur graphes
5. Comprendre l'apprentissage sur variétés et les architectures équivariantes
6. Appliquer le GDL à des problèmes réels (prédiction de propriétés moléculaires, analyse de réseaux sociaux, classification de nuages de points)

## Logiciels Requis

- Python 3.10+
- PyTorch 2.0+
- PyTorch Geometric (torch-geometric)
- Bibliothèques : networkx, matplotlib, rdkit (données moléculaires), open3d (nuages de points)
- Optionnel : wandb pour le suivi d'expériences

---

## Programme Jour par Jour

### Jour 1 : Fondements — Graphes, Symétrie & Passage de Messages

**Objectifs :** Comprendre pourquoi la géométrie compte pour le deep learning et implémenter des GNN de base.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:00 | **Pourquoi l'Apprentissage Géométrique Profond ?** — Limites des MLP et CNN sur les données non-euclidiennes. Le plan GDL : domaines (grilles, graphes, groupes, variétés), symétries et les 5G du GDL |
| 10:00–10:45 | **Théorie des Groupes pour le Deep Learning** — Groupes de symétrie, invariance vs. équivariance, pourquoi les CNN sont équivariants par translation, extension à d'autres symétries |
| 10:45–11:00 | *Pause* |
| 11:00–12:30 | **Représentations de Graphes** — Matrices d'adjacence, listes d'arêtes, features de nœuds/arêtes, features de graphes. Construire des graphes à partir de données réelles. Bases de NetworkX |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Réseaux à Passage de Messages (MPNN)** — Le framework MPNN : message, agrégation, mise à jour. Invariance/équivariance par permutation. GCN (Kipf & Welling), GraphSAGE, GIN |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Bases de PyTorch Geometric** — Objets Data, DataLoader, construire un GNN depuis zéro avec la classe de base MessagePassing, exemple du Karate Club |

**TP 1 :** Implémenter un GCN depuis zéro avec le framework MPNN. Puis utiliser PyTorch Geometric pour construire et entraîner un modèle de classification de nœuds sur le réseau de citations Cora. Visualiser les embeddings de nœuds appris avec t-SNE.

**Devoir :** Expérimenter avec différentes architectures GNN (GCN, GAT, GIN) sur Cora et comparer les performances.

---

### Jour 2 : Méthodes Spectrales & Architectures Avancées

**Objectifs :** Comprendre la perspective spectrale des convolutions sur graphes et les designs GNN avancés.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Théorie Spectrale des Graphes** — Laplacien de graphe, valeurs et vecteurs propres, décomposition spectrale, transformée de Fourier sur graphes, polynômes de Chebyshev, convolutions spectrales vs. spatiales |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Attention sur les Graphes** — Graph Attention Networks (GAT) : attention multi-têtes, coefficients d'attention, comparaison avec GCN. Architectures de type Transformer pour les graphes |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Tâches au Niveau Graphe** — Pooling global (mean, sum, max), pooling hiérarchique (DiffPool, TopKPool, SAGPool), fonctions de readout, pipelines de classification de graphes |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Surlissage & Expressivité** — Le problème du surlissage dans les GNN profonds, le test WL et l'expressivité des GNN, skip connections, JumpingKnowledge, encodages positionnels |

**TP 2 :** Construire un pipeline de classification de graphes avec PyTorch Geometric : charger un dataset moléculaire (MUTAG ou PROTEINS), implémenter le pooling global et hiérarchique, entraîner et évaluer. Expérimenter avec la profondeur et les stratégies de pooling.

**Devoir :** Comparer GAT vs. GCN vs. GIN en précision de classification et temps d'entraînement.

---

### Jour 3 : Variétés, Nuages de Points & Équivariance

**Objectifs :** Étendre le deep learning aux variétés, nuages de points et concevoir des architectures équivariantes.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Apprentissage sur les Variétés** — Maillages, surfaces, géométrie intrinsèque vs. extrinsèque. Distances géodésiques, noyaux de chaleur, opérateur de Laplace-Beltrami. MeshCNN et DiffusionNet |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Traitement de Nuages de Points** — PointNet et PointNet++ : fonctions symétriques pour l'invariance par permutation, agrégation de features locales, traitement hiérarchique. DGCNN |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Réseaux de Neurones Équivariants** — Équivariance SE(3), Tensor Field Networks, EGNN, SchNet pour la dynamique moléculaire. Pourquoi l'équivariance améliore l'efficacité des données |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Features Topologiques pour le GDL** — Homologie persistante comme features de nœuds/graphes, apprentissage de filtrations, TopologyLayer, combiner TDA et GNN |

**TP 3 :** Implémenter un classificateur de nuages de points avec PointNet (depuis zéro en PyTorch) sur ModelNet10 ou ShapeNet. Puis augmenter un GNN avec des features topologiques (nombres de Betti, statistiques de persistance) et mesurer l'amélioration.

**Devoir :** Appliquer EGNN à une tâche de prédiction de propriétés moléculaires et comparer avec un GNN standard.

---

### Jour 4 : Applications & Projet Final

**Objectifs :** Appliquer le GDL à des domaines réels et compléter un projet final.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Prédiction de Propriétés Moléculaires** — Graphes moléculaires, conversion SMILES vers graphe, dataset QM9, SchNet, DimeNet, SphereNet. Applications en découverte de médicaments |
| 10:30–10:45 | *Pause* |
| 10:45–12:00 | **Analyse de Réseaux Sociaux** — Détection de communautés avec GNN, prédiction de liens, influence de nœuds, graphes temporels, graphes hétérogènes |
| 12:00–12:30 | **Autres Applications** — Prédiction de structure protéique (contexte AlphaFold), prédiction de trafic, systèmes de recommandation, simulation physique, prévision météo |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Travail sur le Projet Final** — Implémenter un pipeline GDL complet sur une application choisie |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Présentations & Bilan** — Démos des projets, discussion sur les frontières du GDL, ressources, certificats |

**TP 4 (Projet Final) :** Choisir un projet :
- **Moléculaire :** Prédire des propriétés moléculaires (solubilité, toxicité) avec des GNN sur MoleculeNet
- **Social :** Détection de communautés ou prédiction de liens sur un vrai dataset de réseau social
- **3D :** Classification ou segmentation de nuages de points sur ModelNet/ShapeNet
- **Personnalisé :** Appliquer le GDL à un problème de votre recherche avec construction de graphe appropriée

---

## Évaluation

- **TPs quotidiens** (40 %) — Implémentations fonctionnelles et analyse
- **Projet final** (40 %) — Application GDL complète avec évaluation
- **Participation** (20 %) — Engagement, devoirs et discussions

## Ressources

- [Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, Gauges (Bronstein et al.)](https://geometricdeeplearning.com/)
- [Documentation PyTorch Geometric](https://pytorch-geometric.readthedocs.io/)
- [Graph Representation Learning Book (Hamilton)](https://www.cs.mcgill.ca/~wlh/grl_book/)
- [The Shape of Data](https://nostarch.com/shapeofdata)
- [Stanford CS224W: Machine Learning with Graphs](http://web.stanford.edu/class/cs224w/)

## Certificat

Les participants ayant complété tous les TPs et le projet final reçoivent un certificat de complétion.
