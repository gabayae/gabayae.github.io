---
layout: page
permalink: /workshops/ml-ai-bootcamp/fr/schedule/
title: "Bootcamp — Calendrier hebdomadaire"
description: "Calendrier semaine par semaine du Bootcamp Machine Learning et IA d'AIRINA Labs."
lang: fr
nav: false
---

Calendrier opérationnel pour une cohorte à temps plein (dix semaines). Les cohortes à temps partiel suivent le même contenu sur vingt semaines à la moitié de la charge hebdomadaire. Les dates propres à chaque cohorte sont fixées à l'inscription ; la structure ci-dessous reste stable d'une cohorte à l'autre.

Pour la motivation du programme, les prérequis et la vue d'ensemble des dix modules du cursus, voir le [syllabus]({{ '/workshops/ml-ai-bootcamp/fr/' | relative_url }}). Pour le projet final, voir la [fiche du projet capstone]({{ '/workshops/ml-ai-bootcamp/CAPSTONE/' | relative_url }}).

---

<div class="bootcamp-schedule">

<table>
  <thead>
    <tr><th>Semaine</th><th>Module</th><th>Titre</th><th>Livrable</th><th>Détail</th></tr>
  </thead>
  <tbody>
  {% for week in site.data.bootcamp_fr.weeks %}
    <tr>
      <td><strong>{{ week.number }}</strong></td>
      <td>{{ week.module }}</td>
      <td><a href="{{ '/workshops/ml-ai-bootcamp/fr/week-' | append: week.number | append: '/' | relative_url }}"><strong>{{ week.title }}</strong></a><br><em>{{ week.pitch }}</em></td>
      <td>{{ week.deliverable | markdownify | remove: "<p>" | remove: "</p>" | truncate: 140 }}</td>
      <td><a href="{{ '/workshops/ml-ai-bootcamp/fr/week-' | append: week.number | append: '/' | relative_url }}">semaine {{ week.number }} →</a></td>
    </tr>
  {% endfor %}
  </tbody>
</table>

</div>

## Fonctionnement des pages hebdomadaires

Chaque page de semaine est générée à partir d'une source unique — [`_data/bootcamp_fr.yml`](https://github.com/gabayae/gabayae.github.io/blob/main/_data/bootcamp_fr.yml) pour la version française, [`_data/bootcamp.yml`](https://github.com/gabayae/gabayae.github.io/blob/main/_data/bootcamp.yml) pour la version anglaise — pour que les données vivent à un seul endroit. Chaque page affiche :

1. **Ce que vous livrez cette semaine** — le livrable, la date limite, le canal de soumission, la grille d'évaluation.
2. **Sessions en direct et travaux pratiques** — la cadence hebdomadaire par défaut (sessions live et blocs TP du lundi au jeudi, vendredi intervenant invité / revue de TP / rétrospective), avec les dates propres à chaque cohorte et les liens Zoom intégrés.
3. **Objectifs d'apprentissage et sujets abordés.**
4. **Travaux pratiques** — trois à quatre projets pratiques par semaine, avec le lien du jeu de données et le cahier des charges.
5. **Lectures** — séparées en obligatoires (avec le jour « avant X » précisé) et en approfondissement optionnel.
6. **Renvois au catalogue** — vers les [notes de cours]({{ '/courses/' | relative_url }}) existants lorsqu'un cours correspond.

## Notes opérationnelles

- Les sessions se tiennent par défaut à l'**heure Afrique/Lagos (UTC+1)**. Les cohortes à temps partiel négocient les horaires à l'inscription.
- Les notebooks de TP vivent dans un [dépôt GitHub public](https://github.com/AI-Technipreneurs) qui suit ce calendrier. Chaque TP hebdomadaire correspond à une release taguée.
- Les jalons du projet capstone s'entrelacent avec les modules réguliers : proposition en semaine 4, revue de mi-parcours en semaine 7, gel du code en semaine 9, présentations finales en semaine 10.
- Les enregistrements des cohortes passées sont liés sur chaque page hebdomadaire une fois la session terminée et sont conservés au moins douze mois.
