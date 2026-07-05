---
layout: page
permalink: /fr/supervision/
title: encadrement
description: Mémoires de licence, mémoires de master et thèses de doctorat encadrés à l'IMSP (Bénin) et dans le réseau AIMS.
nav: true
nav_order: 6.5
lang: fr
---

<div class="teaching-page">

<p class="teaching-intro">
{{ site.data.supervision.intro.fr | strip_newlines }}
</p>

{% assign visible = site.data.supervision.students | where_exp: "s", "s.hide != true" %}
{% assign phd_all = visible | where: "level", "phd" %}
{% assign masters_all = visible | where: "level", "masters" %}
{% assign honors_all = visible | where: "level", "honors" %}

{% if phd_all.size > 0 %}
<h2 class="teaching-section-header"><i class="fa-solid fa-user-graduate"></i> Thèses de doctorat</h2>
{% assign phd_years = phd_all | map: "year" | uniq %}
{% for yr in phd_years %}
{% assign block = phd_all | where: "year", yr %}
<h4 style="margin-top: 1.5rem; margin-bottom: 0.75rem;"><i class="fa-solid fa-calendar" style="color: var(--global-hover-color); margin-right: 0.5rem;"></i>{{ yr }}</h4>
<div class="row row-cols-1 row-cols-md-2 g-3 mb-4">
{% for s in block %}
<div class="col"><div class="card hoverable h-100"><div class="card-body">
<h5 class="card-title">{{ s.name }}</h5>
<p class="card-text"><em>{{ s.title }}</em></p>
{% if s.institution %}<p class="card-text" style="font-size: 0.87rem; color: var(--global-text-color-light);">{{ s.institution }}</p>{% endif %}
{% assign summary = s.summary_fr | default: s.summary_en %}
{% if summary %}<p class="card-text" style="font-size: 0.92rem;">{{ summary | strip_newlines }}</p>{% endif %}
{% if s.pdf %}<a href="{{ s.pdf | relative_url }}" class="btn btn-sm btn-outline-primary"><i class="fa-solid fa-file-pdf" style="margin-right: 4px;"></i>Manuscrit</a>{% endif %}
</div></div></div>
{% endfor %}
</div>
{% endfor %}
{% endif %}

{% if masters_all.size > 0 %}
<h2 class="teaching-section-header"><i class="fa-solid fa-graduation-cap"></i> Mémoires de master</h2>
{% assign masters_years = masters_all | map: "year" | uniq | sort | reverse %}
{% for yr in masters_years %}
{% assign block = masters_all | where: "year", yr %}
<h4 style="margin-top: 1.5rem; margin-bottom: 0.75rem;"><i class="fa-solid fa-calendar" style="color: var(--global-hover-color); margin-right: 0.5rem;"></i>{{ yr }}</h4>
<div class="row row-cols-1 row-cols-md-2 g-3 mb-4">
{% for s in block %}
<div class="col"><div class="card hoverable h-100"><div class="card-body">
<h5 class="card-title">{{ s.name }}</h5>
<p class="card-text"><em>{{ s.title }}</em></p>
{% if s.institution %}<p class="card-text" style="font-size: 0.87rem; color: var(--global-text-color-light);">{{ s.institution }}</p>{% endif %}
{% assign summary = s.summary_fr | default: s.summary_en %}
{% if summary %}<p class="card-text" style="font-size: 0.92rem;">{{ summary | strip_newlines }}</p>{% endif %}
{% if s.pdf %}<a href="{{ s.pdf | relative_url }}" class="btn btn-sm btn-outline-primary"><i class="fa-solid fa-file-pdf" style="margin-right: 4px;"></i>Manuscrit</a>{% endif %}
</div></div></div>
{% endfor %}
</div>
{% endfor %}
{% endif %}

{% if honors_all.size > 0 %}
<h2 class="teaching-section-header"><i class="fa-solid fa-scroll"></i> Mémoires de licence</h2>
{% assign honors_years = honors_all | map: "year" | uniq | sort | reverse %}
{% for yr in honors_years %}
{% assign block = honors_all | where: "year", yr %}
<h4 style="margin-top: 1.5rem; margin-bottom: 0.75rem;"><i class="fa-solid fa-calendar" style="color: var(--global-hover-color); margin-right: 0.5rem;"></i>{{ yr }}</h4>
<div class="row row-cols-1 row-cols-md-2 g-3 mb-4">
{% for s in block %}
<div class="col"><div class="card hoverable h-100"><div class="card-body">
<h5 class="card-title">{{ s.name }}</h5>
<p class="card-text"><em>{{ s.title }}</em></p>
{% if s.institution %}<p class="card-text" style="font-size: 0.87rem; color: var(--global-text-color-light);">{{ s.institution }}</p>{% endif %}
{% assign summary = s.summary_fr | default: s.summary_en %}
{% if summary %}<p class="card-text" style="font-size: 0.92rem;">{{ summary | strip_newlines }}</p>{% endif %}
{% if s.pdf %}<a href="{{ s.pdf | relative_url }}" class="btn btn-sm btn-outline-primary"><i class="fa-solid fa-file-pdf" style="margin-right: 4px;"></i>Manuscrit</a>{% endif %}
</div></div></div>
{% endfor %}
</div>
{% endfor %}
{% endif %}

<div style="background: linear-gradient(135deg, rgba(59,111,212,0.10), rgba(59,111,212,0.03)); border: 1px solid rgba(59,111,212,0.35); border-radius: 12px; padding: 22px 24px; margin-top: 28px; text-align: center;">
<p style="font-size: 1.02rem; margin-bottom: 14px;">
<i class="fa-solid fa-envelope" style="margin-right: 8px; color: var(--global-theme-color);"></i>
Les étudiants intéressés par la <strong>topologie asymétrique</strong>, la <strong>théorie des points fixes</strong>, l'<strong>ATD</strong> ou l'<strong>apprentissage géométrique</strong> peuvent me contacter.
</p>
<a href="mailto:gabayae2@gmail.com?subject=Étudiant%20potentiel%20%E2%80%94%20demande%20d'encadrement" class="btn btn-primary" style="font-weight: 600; padding: 8px 22px; border-radius: 8px;">
<i class="fa-solid fa-arrow-right" style="margin-right: 8px;"></i> Demander un encadrement
</a>
</div>

</div>
