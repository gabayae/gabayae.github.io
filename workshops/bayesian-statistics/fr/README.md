# Statistique Bayésienne Appliquée — Atelier de 4 jours

**Formateur :** Dr. Yaé Ulrich Gaba
**Durée :** 4 jours (24 heures)
**Niveau :** Intermédiaire à Avancé
**Langue :** Français

---

## Présentation

Cet atelier offre une introduction pratique à la statistique bayésienne avec un accent sur la modélisation, le calcul et les applications réelles. Les participants apprennent la pensée bayésienne, construisent des modèles probabilistes avec PyMC et appliquent des méthodes hiérarchiques à des problèmes de santé, finance et sciences sociales.

## Prérequis

- Bases de probabilités et statistiques (distributions, vraisemblance, probabilité conditionnelle, théorème de Bayes)
- Programmation Python (NumPy, Matplotlib)
- Une familiarité avec la régression (linéaire/logistique) est utile
- Aucune expérience bayésienne préalable requise

## Objectifs Pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Penser de manière probabiliste et formuler des problèmes dans un cadre bayésien
2. Spécifier des distributions a priori et comprendre leur impact sur l'inférence
3. Construire et ajuster des modèles bayésiens avec PyMC
4. Comprendre et diagnostiquer l'échantillonnage MCMC (traces, R-hat, taille d'échantillon effective)
5. Construire des modèles hiérarchiques (multiniveaux)
6. Effectuer la comparaison de modèles et les vérifications prédictives a posteriori
7. Appliquer les méthodes bayésiennes à des problèmes spécifiques à un domaine

## Logiciels Requis

- Python 3.10+
- Bibliothèques : pymc (v5+), arviz, numpy, matplotlib, seaborn, pandas, scipy
- Optionnel : Stan (via cmdstanpy), bambi (modèles bayésiens par formule)

---

## Programme Jour par Jour

### Jour 1 : Pensée Bayésienne & Premiers Modèles

**Objectifs :** Comprendre le paradigme bayésien et construire les premiers modèles probabilistes.

| Horaire | Sujet |
|---------|-------|
| 09:00–10:00 | **Pourquoi le Bayésien ?** — Philosophie fréquentiste vs. bayésienne, la probabilité comme croyance, avantages : quantification de l'incertitude, petits échantillons, incorporation de connaissances a priori |
| 10:00–10:45 | **Théorème de Bayes en Pratique** — Prior × Vraisemblance = Postérieur (à normalisation près). Priors conjugués, exemples analytiques : Beta-Binomial, Normal-Normal |
| 10:45–11:00 | *Pause* |
| 11:00–12:30 | **Choisir les Priors** — Priors informatifs vs. faiblement informatifs vs. non informatifs. Vérifications prédictives a priori : le prior génère-t-il des données plausibles ? Priors courants pour les paramètres standards |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Introduction à PyMC** — Spécification de modèle, variables aléatoires, données observées, échantillonnage avec NUTS, traces, ArviZ pour les diagnostics et la visualisation |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Régression Linéaire Bayésienne** — Vraisemblance normale, priors sur les coefficients et la variance, interprétation du postérieur, intervalles de crédibilité vs. confiance, distribution prédictive a posteriori |

**TP 1 :** Construire un modèle de régression linéaire bayésienne dans PyMC : prédire un résultat de santé (ex. : tension artérielle ~ âge + IMC). Explorer l'effet de différents priors, visualiser le postérieur, comparer avec les MCO fréquentistes.

**Devoir :** Ajuster une régression bayésienne sur un jeu de données de votre choix. Expérimenter la sensibilité au prior.

---

### Jour 2 : MCMC, Diagnostics & Modèles Généralisés

**Objectifs :** Comprendre le fonctionnement du MCMC et étendre les modèles bayésiens au-delà de la régression linéaire.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Comment Fonctionne le MCMC** — Le problème d'échantillonnage, Metropolis-Hastings (intuition), Monte Carlo Hamiltonien (HMC), NUTS. Pourquoi NUTS est le défaut |
| 10:30–10:45 | *Pause* |
| 10:45–12:00 | **Diagnostiquer le MCMC** — Traces, autocorrélation, R-hat (convergence), taille d'échantillon effective (ESS), divergences HMC. Que faire quand l'échantillonnage échoue : reparamétrisation, paramétrisation non centrée |
| 12:00–12:30 | **Critique du Modèle** — Vérifications prédictives a posteriori : le modèle génère-t-il des données semblables aux données réelles ? Analyse des résidus, calibration |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Régression Logistique Bayésienne** — Vraisemblance Bernoulli/Binomiale, lien logit, priors pour les coefficients, interprétation des rapports de cotes a posteriori, classification avec incertitude |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **GLM Bayésiens** — Régression de Poisson pour les données de comptage, binomiale négative pour la surdispersion, choisir la bonne famille de vraisemblance |

**TP 2 :** Construire une régression logistique bayésienne pour le diagnostic de maladie (ex. : prédiction du diabète). Effectuer les diagnostics MCMC complets, les vérifications prédictives a posteriori, et comparer les probabilités prédites avec une régression logistique fréquentiste.

**Devoir :** Ajuster un modèle de Poisson à des données de comptage (ex. : nombre de visites médicales) et vérifier la surdispersion.

---

### Jour 3 : Modèles Hiérarchiques

**Objectifs :** Construire des modèles multiniveaux qui partagent l'information entre les groupes.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Pourquoi le Hiérarchique ?** — Le problème : trop de groupes, trop peu de données par groupe. Pooling complet vs. pas de pooling vs. pooling partiel. Rétrécissement et le phénomène de James-Stein |
| 10:30–10:45 | *Pause* |
| 10:45–12:30 | **Modèles Linéaires Hiérarchiques** — Intercepts variables, pentes variables, prédicteurs de niveau groupe. La paramétrisation non centrée pour un échantillonnage efficace. Visualiser le pooling partiel |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:30 | **Modèles Hiérarchiques sur Données Réelles** — Données de santé multi-pays : estimer les effets par pays avec pooling partiel. Structures croisées et emboîtées |
| 15:30–15:45 | *Pause* |
| 15:45–17:00 | **Comparaison de Modèles** — WAIC, LOO-CV avec ArviZ, comparer des modèles avec différentes structures, interprétation des critères d'information |

**TP 3 :** Construire un modèle hiérarchique pour les résultats éducatifs à travers les pays africains : scores de test d'étudiants emboîtés dans des écoles dans des pays. Comparer pooling complet, pas de pooling et estimations hiérarchiques. Visualiser le rétrécissement.

**Devoir :** Étendre le modèle hiérarchique avec un prédicteur de niveau groupe (ex. : niveau de financement de l'école).

---

### Jour 4 : Sujets Avancés & Applications

**Objectifs :** Appliquer les méthodes bayésiennes à des problèmes spécifiques et explorer des techniques avancées.

| Horaire | Sujet |
|---------|-------|
| 09:00–09:30 | **Revue du devoir** |
| 09:30–10:30 | **Séries Temporelles Bayésiennes** — Priors autorégressifs, processus gaussiens pour les séries temporelles, modèles structurels, détection de points de changement |
| 10:30–10:45 | *Pause* |
| 10:45–12:00 | **Modèles de Mélange & Clustering** — Modèles de mélange gaussien, non-paramétrique bayésien (intuition du processus de Dirichlet), modèles à variables latentes |
| 12:00–12:30 | **Tests A/B Bayésiens** — Comparer des traitements/interventions, probabilité a posteriori de supériorité, prise de décision sous incertitude, avantages par rapport aux p-values |
| 12:30–14:00 | *Déjeuner* |
| 14:00–15:00 | **Applications par Domaine** — Études de cas : analyse d'essais cliniques, modélisation du risque de crédit, modélisation épidémiologique (SIR avec inférence bayésienne), analyse de données d'enquête |
| 15:00–15:15 | *Pause* |
| 15:15–16:15 | **Travail sur le Projet Final** — Compléter une analyse bayésienne sur un jeu de données choisi |
| 16:15–17:00 | **Présentations & Bilan** — Présentations des projets, résumé du workflow bayésien, ressources, certificats |

**TP 4 (Projet Final) :** Choisir un projet :
- **Santé :** Estimation bayésienne de la prévalence d'une maladie avec modèles hiérarchiques par région
- **Finance :** Modélisation du défaut de crédit avec régression logistique bayésienne et quantification de l'incertitude
- **Éducation :** Modèle multiniveau de la performance des étudiants avec effets école et pays
- **Personnalisé :** Appliquer les méthodes bayésiennes à un problème de votre propre domaine

---

## Évaluation

- **TPs quotidiens** (40 %) — Modèles fonctionnels avec diagnostics appropriés
- **Projet final** (40 %) — Analyse bayésienne complète avec interprétation
- **Participation** (20 %) — Engagement, devoirs et discussions

## Ressources

- [Bayesian Analysis with Python (3e éd.) — Osvaldo Martin](https://www.packtpub.com/product/bayesian-analysis-with-python-third-edition/9781805127161)
- [Statistical Rethinking (2e éd.) — Richard McElreath](https://xcelab.net/rm/statistical-rethinking/)
- [Documentation PyMC](https://www.pymc.io/projects/docs/en/stable/)
- [Documentation ArviZ](https://python.arviz.org/en/stable/)
- [Bayesian Data Analysis (Gelman et al.)](http://www.stat.columbia.edu/~gelman/book/)

## Certificat

Les participants ayant complété tous les TPs et le projet final reçoivent un certificat de complétion.
