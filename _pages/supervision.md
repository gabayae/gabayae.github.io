---
layout: page
permalink: /en/supervision/
title: supervision
description: Honors essays, master's dissertations, and doctoral theses supervised or co-supervised.
nav: true
nav_order: 6.5
lang: en
---

<style>
.supervision-intro {
  font-size: 1rem;
  line-height: 1.65;
  color: var(--global-text-color);
  margin-bottom: 2rem;
  max-width: 62rem;
}
.thesis-section {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  border-bottom: 2px solid var(--global-divider-color);
  padding-bottom: 0.4rem;
  margin-top: 2.75rem;
  margin-bottom: 1.4rem;
}
.thesis-section h2 {
  margin: 0;
  font-size: 1.35rem;
  font-weight: 600;
  color: var(--global-theme-color);
}
.thesis-section h2 i { margin-right: 0.5rem; opacity: 0.85; }
.thesis-section .count {
  font-size: 0.85rem;
  font-weight: 400;
  color: var(--global-text-color-light);
  letter-spacing: 0.02em;
}
.thesis-year-block { margin-bottom: 1.35rem; }
.thesis-year-label {
  font-weight: 600;
  color: var(--global-hover-color);
  font-size: 0.92rem;
  letter-spacing: 0.03em;
  margin-bottom: 0.5rem;
  padding-left: 0.55rem;
  border-left: 3px solid var(--global-theme-color);
}
.thesis-row {
  display: grid;
  grid-template-columns: 2.2rem 3rem 1fr;
  gap: 0.75rem;
  align-items: start;
  padding: 0.7rem 0.5rem 0.7rem 0.6rem;
  border-bottom: 1px solid var(--global-divider-color);
  transition: background-color 0.15s ease;
}
.thesis-row:hover { background-color: rgba(0,0,0,0.02); }
.thesis-row:last-child { border-bottom: none; }
.thesis-avatar {
  width: 2.1rem;
  height: 2.1rem;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--global-theme-color), var(--global-hover-color));
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.66rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  overflow: hidden;
  flex-shrink: 0;
  margin-top: 0.05rem;
  user-select: none;
}
.thesis-avatar img { width: 100%; height: 100%; object-fit: cover; }
.thesis-badge {
  display: inline-block;
  font-size: 0.66rem;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  font-weight: 700;
  padding: 3px 7px;
  border-radius: 3px;
  align-self: start;
  text-align: center;
  margin-top: 0.28rem;
}
.thesis-badge.phd { background: rgba(52, 91, 168, 0.13); color: #345bb0; }
.thesis-badge.masters { background: rgba(30, 120, 90, 0.13); color: #1e785a; }
.thesis-badge.honors { background: rgba(180, 100, 40, 0.15); color: #a05820; }
.thesis-name {
  font-size: 0.98rem;
  font-weight: 600;
  color: var(--global-text-color);
  margin-bottom: 0.15rem;
}
.thesis-name-link { color: inherit; text-decoration: none; transition: color 0.15s; }
.thesis-name-link:hover { color: var(--global-theme-color); text-decoration: none; }
.thesis-name-link .fa-arrow-up-right-from-square {
  font-size: 0.6em; margin-left: 0.35rem; opacity: 0.55; vertical-align: 0.1em;
}
.thesis-title {
  font-size: 0.94rem;
  font-style: italic;
  color: var(--global-text-color);
  line-height: 1.5;
  margin-bottom: 0.3rem;
}
.thesis-title.pending {
  font-style: normal;
  color: var(--global-text-color-light);
  font-size: 0.88rem;
  opacity: 0.75;
}
.thesis-summary {
  font-size: 0.88rem;
  color: var(--global-text-color-light);
  line-height: 1.55;
  margin-bottom: 0.15rem;
}
.thesis-ongoing-badge {
  display: inline-block;
  font-size: 0.63rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  font-weight: 700;
  color: #a05820;
  background: rgba(180, 100, 40, 0.13);
  padding: 2px 7px;
  border-radius: 3px;
  margin-left: 0.5rem;
  vertical-align: 0.12rem;
  font-style: normal;
}
.thesis-pdf {
  display: inline-block;
  margin-top: 0.4rem;
  font-size: 0.85rem;
}
.supervision-cta {
  background: linear-gradient(135deg, rgba(59,111,212,0.08), rgba(59,111,212,0.02));
  border: 1px solid rgba(59,111,212,0.25);
  border-radius: 10px;
  padding: 20px 24px;
  margin-top: 3rem;
  text-align: center;
}
.supervision-cta p { font-size: 1rem; margin-bottom: 12px; }
html[data-theme='dark'] .thesis-row:hover { background-color: rgba(255,255,255,0.03); }
html[data-theme='dark'] .thesis-ongoing-badge { color: #d38a4a; background: rgba(211, 138, 74, 0.15); }
@media (max-width: 700px) {
  .thesis-row { grid-template-columns: 2rem 1fr; gap: 0.6rem; }
  .thesis-badge { grid-column: 2; margin-bottom: 0.15rem; margin-top: 0; }
}
</style>

<p class="supervision-intro">
{{ site.data.supervision.intro.en | strip_newlines }}
</p>

{% assign visible = site.data.supervision.students | where_exp: "s", "s.hide != true" %}
{% assign phd_all = visible | where: "level", "phd" %}
{% assign masters_all = visible | where: "level", "masters" %}
{% assign honors_all = visible | where: "level", "honors" %}

{% if phd_all.size > 0 %}
<div class="thesis-section">
  <h2><i class="fa-solid fa-user-graduate"></i>Doctoral theses</h2>
  <span class="count">{{ phd_all.size }} thes{% if phd_all.size > 1 %}es{% else %}is{% endif %}</span>
</div>
{% assign phd_years = phd_all | map: "year" | uniq %}
{% for yr in phd_years %}
{% assign block = phd_all | where: "year", yr %}
<div class="thesis-year-block">
<div class="thesis-year-label">{{ yr }}</div>
{% for s in block %}
<div class="thesis-row">
<div class="thesis-avatar">{% if s.photo %}<img src="{{ s.photo | relative_url }}" alt="{{ s.name }}">{% else %}{% assign words = s.name | split: " " %}{% assign init1 = words | first | slice: 0, 1 | upcase %}{% assign init2 = words | last | slice: 0, 1 | upcase %}<span>{{ init1 }}{{ init2 }}</span>{% endif %}</div>
<span class="thesis-badge phd">PhD</span>
<div>
<div class="thesis-name">{% if s.url %}<a href="{{ s.url }}" class="thesis-name-link" target="_blank" rel="noopener">{{ s.name }} <i class="fa-solid fa-arrow-up-right-from-square"></i></a>{% else %}{{ s.name }}{% endif %}</div>
{% assign t = s.title | downcase %}{% if t contains "pending" or t contains "verify" or t contains "compléter" %}<div class="thesis-title pending">Title forthcoming</div>{% else %}<div class="thesis-title">{{ s.title }}{% if s.ongoing %} <span class="thesis-ongoing-badge">Ongoing</span>{% endif %}</div>{% endif %}
{% if s.summary_en %}<div class="thesis-summary">{{ s.summary_en | strip_newlines }}</div>{% endif %}
{% if s.pdf %}<a href="{{ s.pdf | relative_url }}" class="thesis-pdf"><i class="fa-solid fa-file-pdf" style="margin-right: 4px;"></i>Manuscript</a>{% endif %}
</div>
</div>
{% endfor %}
</div>
{% endfor %}
{% endif %}

{% if masters_all.size > 0 %}
<div class="thesis-section">
  <h2><i class="fa-solid fa-graduation-cap"></i>Master's dissertations</h2>
  <span class="count">{{ masters_all.size }} dissertations</span>
</div>
{% assign masters_years = masters_all | map: "year" | uniq | sort | reverse %}
{% for yr in masters_years %}
{% assign block = masters_all | where: "year", yr %}
<div class="thesis-year-block">
<div class="thesis-year-label">{{ yr }}</div>
{% for s in block %}
<div class="thesis-row">
<div class="thesis-avatar">{% if s.photo %}<img src="{{ s.photo | relative_url }}" alt="{{ s.name }}">{% else %}{% assign words = s.name | split: " " %}{% assign init1 = words | first | slice: 0, 1 | upcase %}{% assign init2 = words | last | slice: 0, 1 | upcase %}<span>{{ init1 }}{{ init2 }}</span>{% endif %}</div>
<span class="thesis-badge masters">M</span>
<div>
<div class="thesis-name">{% if s.url %}<a href="{{ s.url }}" class="thesis-name-link" target="_blank" rel="noopener">{{ s.name }} <i class="fa-solid fa-arrow-up-right-from-square"></i></a>{% else %}{{ s.name }}{% endif %}</div>
{% assign t = s.title | downcase %}{% if t contains "pending" or t contains "verify" or t contains "compléter" %}<div class="thesis-title pending">Title forthcoming</div>{% else %}<div class="thesis-title">{{ s.title }}{% if s.ongoing %} <span class="thesis-ongoing-badge">Ongoing</span>{% endif %}</div>{% endif %}
{% if s.summary_en %}<div class="thesis-summary">{{ s.summary_en | strip_newlines }}</div>{% endif %}
{% if s.pdf %}<a href="{{ s.pdf | relative_url }}" class="thesis-pdf"><i class="fa-solid fa-file-pdf" style="margin-right: 4px;"></i>Manuscript</a>{% endif %}
</div>
</div>
{% endfor %}
</div>
{% endfor %}
{% endif %}

{% if honors_all.size > 0 %}
<div class="thesis-section">
  <h2><i class="fa-solid fa-scroll"></i>Honors essays</h2>
  <span class="count">{{ honors_all.size }} essays</span>
</div>
{% assign honors_years = honors_all | map: "year" | uniq | sort | reverse %}
{% for yr in honors_years %}
{% assign block = honors_all | where: "year", yr %}
<div class="thesis-year-block">
<div class="thesis-year-label">{{ yr }}</div>
{% for s in block %}
<div class="thesis-row">
<div class="thesis-avatar">{% if s.photo %}<img src="{{ s.photo | relative_url }}" alt="{{ s.name }}">{% else %}{% assign words = s.name | split: " " %}{% assign init1 = words | first | slice: 0, 1 | upcase %}{% assign init2 = words | last | slice: 0, 1 | upcase %}<span>{{ init1 }}{{ init2 }}</span>{% endif %}</div>
<span class="thesis-badge honors">H</span>
<div>
<div class="thesis-name">{% if s.url %}<a href="{{ s.url }}" class="thesis-name-link" target="_blank" rel="noopener">{{ s.name }} <i class="fa-solid fa-arrow-up-right-from-square"></i></a>{% else %}{{ s.name }}{% endif %}</div>
{% assign t = s.title | downcase %}{% if t contains "pending" or t contains "verify" or t contains "compléter" %}<div class="thesis-title pending">Title forthcoming</div>{% else %}<div class="thesis-title">{{ s.title }}{% if s.ongoing %} <span class="thesis-ongoing-badge">Ongoing</span>{% endif %}</div>{% endif %}
{% if s.summary_en %}<div class="thesis-summary">{{ s.summary_en | strip_newlines }}</div>{% endif %}
{% if s.pdf %}<a href="{{ s.pdf | relative_url }}" class="thesis-pdf"><i class="fa-solid fa-file-pdf" style="margin-right: 4px;"></i>Manuscript</a>{% endif %}
</div>
</div>
{% endfor %}
</div>
{% endfor %}
{% endif %}

<div class="supervision-cta">
<p><i class="fa-solid fa-envelope" style="margin-right: 8px; color: var(--global-theme-color);"></i>
Prospective students interested in <strong>asymmetric topology</strong>, <strong>fixed-point theory</strong>, <strong>TDA</strong>, or <strong>geometric ML</strong> are welcome to reach out.</p>
<a href="mailto:gabayae2@gmail.com?subject=Prospective%20student%20%E2%80%94%20supervision%20inquiry" class="btn btn-primary" style="font-weight: 600; padding: 8px 22px; border-radius: 8px;">
<i class="fa-solid fa-arrow-right" style="margin-right: 8px;"></i> Inquire about supervision
</a>
</div>
