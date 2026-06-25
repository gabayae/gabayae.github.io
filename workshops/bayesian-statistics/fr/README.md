---
layout: workshop
permalink: /workshops/bayesian-statistics/fr/
lang: fr
title: "Statistique Bayésienne Appliquée"
tagline: "Pensée probabiliste, PyMC, diagnostics MCMC et modélisation hiérarchique — des priors aux décisions a posteriori."
description: "Atelier de 4 jours sur la statistique bayésienne appliquée : PyMC, MCMC, modèles hiérarchiques."

# --- Métadonnées de la barre latérale ---
instructor: "Dr. Yaé Ulrich Gaba"
duration: "4 jours (≈ 24 heures)"
level: "Intermédiaire à Avancé"
format: "Sur site, en ligne en direct, ou hybride"
languages: "Français &amp; anglais"
certificate: "Certificat de complétion"

# --- Liens des supports ---
notebooks_url: https://github.com/gabayae/gabayae.github.io/tree/main/workshops/bayesian-statistics

# --- Contact ---
contact_email: gabayae2@gmail.com
contact_subject: "Demande d'atelier — Statistique Bayésienne Appliquée"
---

## Présentation du programme

Cet atelier offre une introduction pratique à la statistique bayésienne avec un accent sur la modélisation, le calcul et les applications réelles. Les participants apprennent la pensée bayésienne, construisent des modèles probabilistes avec PyMC et appliquent des méthodes hiérarchiques à des problèmes de santé, finance et sciences sociales.

### Logiciels requis

- Python 3.10+
- Bibliothèques : pymc (v5+), arviz, numpy, matplotlib, seaborn, pandas, scipy
- Optionnel : Stan (via cmdstanpy), bambi (modèles bayésiens par formule)

### Jour 1 — Pensée bayésienne & premiers modèles

**Objectifs :** comprendre le paradigme bayésien et construire les premiers modèles probabilistes.

- **Pourquoi le bayésien ?** — philosophie fréquentiste vs. bayésienne, la probabilité comme croyance, avantages : quantification de l'incertitude, petits échantillons, incorporation de connaissances a priori.
- **Théorème de Bayes en pratique** — Prior × Vraisemblance = Postérieur (à normalisation près). Priors conjugués, exemples analytiques : Beta-Binomial, Normal-Normal.
- **Choisir les priors** — priors informatifs vs. faiblement informatifs vs. non informatifs. Vérifications prédictives a priori : le prior génère-t-il des données plausibles ? Priors courants pour les paramètres standards.
- **Introduction à PyMC** — spécification de modèle, variables aléatoires, données observées, échantillonnage avec NUTS, traces, ArviZ pour les diagnostics et la visualisation.
- **Régression linéaire bayésienne** — vraisemblance normale, priors sur les coefficients et la variance, interprétation du postérieur, intervalles de crédibilité vs. confiance, distribution prédictive a posteriori.

**TP 1 :** construire un modèle de régression linéaire bayésienne dans PyMC : prédire un résultat de santé (ex. : tension artérielle ~ âge + IMC). Explorer l'effet de différents priors, visualiser le postérieur, comparer avec les MCO fréquentistes.

### Jour 2 — MCMC, diagnostics & modèles généralisés

**Objectifs :** comprendre le fonctionnement du MCMC et étendre les modèles bayésiens au-delà de la régression linéaire.

- **Comment fonctionne le MCMC** — le problème d'échantillonnage, Metropolis-Hastings (intuition), Monte Carlo Hamiltonien (HMC), NUTS. Pourquoi NUTS est le défaut.
- **Diagnostiquer le MCMC** — traces, autocorrélation, R-hat (convergence), taille d'échantillon effective (ESS), divergences HMC. Que faire quand l'échantillonnage échoue : reparamétrisation, paramétrisation non centrée.
- **Critique du modèle** — vérifications prédictives a posteriori : le modèle génère-t-il des données semblables aux données réelles ? Analyse des résidus, calibration.
- **Régression logistique bayésienne** — vraisemblance Bernoulli/Binomiale, lien logit, priors pour les coefficients, interprétation des rapports de cotes a posteriori, classification avec incertitude.
- **GLM bayésiens** — régression de Poisson pour les données de comptage, binomiale négative pour la surdispersion, choisir la bonne famille de vraisemblance.

**TP 2 :** construire une régression logistique bayésienne pour le diagnostic de maladie (ex. : prédiction du diabète). Effectuer les diagnostics MCMC complets, les vérifications prédictives a posteriori, et comparer les probabilités prédites avec une régression logistique fréquentiste.

### Jour 3 — Modèles hiérarchiques

**Objectifs :** construire des modèles multiniveaux qui partagent l'information entre les groupes.

- **Pourquoi le hiérarchique ?** — le problème : trop de groupes, trop peu de données par groupe. Pooling complet vs. pas de pooling vs. pooling partiel. Rétrécissement et le phénomène de James-Stein.
- **Modèles linéaires hiérarchiques** — intercepts variables, pentes variables, prédicteurs de niveau groupe. La paramétrisation non centrée pour un échantillonnage efficace. Visualiser le pooling partiel.
- **Modèles hiérarchiques sur données réelles** — données de santé multi-pays : estimer les effets par pays avec pooling partiel. Structures croisées et emboîtées.
- **Comparaison de modèles** — WAIC, LOO-CV avec ArviZ, comparer des modèles avec différentes structures, interprétation des critères d'information.

**TP 3 :** construire un modèle hiérarchique pour les résultats éducatifs à travers les pays africains : scores de test d'étudiants emboîtés dans des écoles dans des pays. Comparer pooling complet, pas de pooling et estimations hiérarchiques. Visualiser le rétrécissement.

### Jour 4 — Sujets avancés & applications

**Objectifs :** appliquer les méthodes bayésiennes à des problèmes spécifiques et explorer des techniques avancées.

- **Séries temporelles bayésiennes** — priors autorégressifs, processus gaussiens pour les séries temporelles, modèles structurels, détection de points de changement.
- **Modèles de mélange & clustering** — modèles de mélange gaussien, non-paramétrique bayésien (intuition du processus de Dirichlet), modèles à variables latentes.
- **Tests A/B bayésiens** — comparer des traitements/interventions, probabilité a posteriori de supériorité, prise de décision sous incertitude, avantages par rapport aux p-values.
- **Applications par domaine** — études de cas : analyse d'essais cliniques, modélisation du risque de crédit, modélisation épidémiologique (SIR avec inférence bayésienne), analyse de données d'enquête.
- **Travail sur le projet final** — compléter une analyse bayésienne sur un jeu de données choisi.
- **Présentations & bilan** — présentations des projets, résumé du workflow bayésien, ressources, certificats.

**TP 4 (projet final) :** choisir un projet :
- **Santé :** estimation bayésienne de la prévalence d'une maladie avec modèles hiérarchiques par région.
- **Finance :** modélisation du défaut de crédit avec régression logistique bayésienne et quantification de l'incertitude.
- **Éducation :** modèle multiniveau de la performance des étudiants avec effets école et pays.
- **Personnalisé :** appliquer les méthodes bayésiennes à un problème de votre propre domaine.

### Évaluation

- **TPs quotidiens** (40 %) — modèles fonctionnels avec diagnostics appropriés.
- **Projet final** (40 %) — analyse bayésienne complète avec interprétation.
- **Participation** (20 %) — engagement, devoirs et discussions.

### Ressources

- [Bayesian Analysis with Python (3e éd.) — Osvaldo Martin](https://www.packtpub.com/product/bayesian-analysis-with-python-third-edition/9781805127161)
- [Statistical Rethinking (2e éd.) — Richard McElreath](https://xcelab.net/rm/statistical-rethinking/)
- [Documentation PyMC](https://www.pymc.io/projects/docs/en/stable/)
- [Documentation ArviZ](https://python.arviz.org/en/stable/)
- [Bayesian Data Analysis (Gelman et al.)](http://www.stat.columbia.edu/~gelman/book/)

## Objectifs pédagogiques

À la fin de cet atelier, les participants seront capables de :

1. Penser de manière probabiliste et formuler des problèmes dans un cadre bayésien.
2. Spécifier des distributions a priori et comprendre leur impact sur l'inférence.
3. Construire et ajuster des modèles bayésiens avec PyMC.
4. Comprendre et diagnostiquer l'échantillonnage MCMC (traces, R-hat, taille d'échantillon effective).
5. Construire des modèles hiérarchiques (multiniveaux).
6. Effectuer la comparaison de modèles et les vérifications prédictives a posteriori.
7. Appliquer les méthodes bayésiennes à des problèmes spécifiques à un domaine.

## Public visé

Data scientists, statisticiens et chercheurs quantitatifs en santé, finance, sciences sociales ou politiques publiques qui veulent dépasser les p-values et rapporter l'incertitude honnêtement. Étudiants de master/doctorat dont la recherche dépend d'inférence sur des échantillons petits ou bruités. Praticiens qui utilisent déjà la régression et veulent une manière rigoureuse d'incorporer des connaissances a priori et de propager l'incertitude dans les décisions.

**Prérequis :**

- Bases de probabilités et statistiques (distributions, vraisemblance, probabilité conditionnelle, théorème de Bayes).
- Programmation Python (NumPy, Matplotlib).
- Une familiarité avec la régression (linéaire/logistique) est utile.
- Aucune expérience bayésienne préalable requise.

## Plaquette

Les notes de cours et notebooks sont accessibles depuis la barre latérale.

Pour une plaquette d'une page, à transmettre à un comité de programme, un organisateur de conférence ou une équipe formation interne, écrivez à <a href="mailto:gabayae2@gmail.com?subject=Demande%20de%20plaquette%20%E2%80%94%20Statistique%20Bay%C3%A9sienne%20Appliqu%C3%A9e">gabayae2@gmail.com</a> en précisant la taille de l'audience et les dates envisagées.
