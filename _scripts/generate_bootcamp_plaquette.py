"""Generate 2-page PDF brochures of the ML & AI Bootcamp (FR + EN) via Chrome headless.

Writes inline-styled HTML files to a temp dir, then shells out to chrome.exe
--headless --print-to-pdf. No Python PDF library needed (weasyprint libpango is
broken on this Windows env; playwright would also work but adds a deps chain).

Usage:
    python _scripts/generate_bootcamp_plaquette.py

Output:
    assets/pdf/bootcamp_ml_ai_fr.pdf
    assets/pdf/bootcamp_ml_ai_en.pdf
"""

from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "assets" / "pdf"
OUT_DIR.mkdir(parents=True, exist_ok=True)

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

STYLE = """
@page { size: A4; margin: 14mm 16mm; }
body { font-family: 'Inter', 'Segoe UI', Arial, sans-serif; font-size: 10pt; line-height: 1.45; color: #171717; margin: 0; }
h1 { font-family: 'Iowan Old Style', 'Palatino Linotype', Georgia, serif; font-size: 22pt; color: #0f2a4a; margin: 0 0 4pt; letter-spacing: -0.02em; font-weight: 700; }
h2 { font-family: 'Iowan Old Style', 'Palatino Linotype', Georgia, serif; font-size: 13pt; color: #0f2a4a; margin: 12pt 0 4pt; letter-spacing: -0.01em; font-weight: 600; }
h3 { font-size: 9pt; text-transform: uppercase; letter-spacing: 0.08em; color: #555; font-weight: 600; margin: 8pt 0 2pt; }
p { margin: 3pt 0; }
.tagline { font-size: 11pt; color: #555; margin: 4pt 0 6pt; font-style: italic; }
.hero { border-bottom: 1px solid #e4e1d8; padding-bottom: 8pt; margin-bottom: 10pt; }
.hero-meta { display: flex; flex-wrap: wrap; gap: 3pt 12pt; margin-top: 6pt; font-size: 8.5pt; color: #171717; }
.hero-meta strong { color: #c85c3c; }
.cohort-box { background: #f4e4dd; border-left: 3px solid #c85c3c; padding: 7pt 10pt; margin: 8pt 0; font-size: 9pt; }
.cohort-box strong { color: #0f2a4a; }
table.facts { width: 100%; border-collapse: collapse; margin: 4pt 0; font-size: 9pt; }
table.facts td { padding: 2pt 6pt 2pt 0; vertical-align: top; border-bottom: 1px dotted #e4e1d8; }
table.facts tr td:first-child { font-weight: 600; width: 38%; color: #0f2a4a; }
.modules { display: grid; grid-template-columns: 1fr 1fr; gap: 3pt 14pt; margin: 4pt 0; font-size: 9pt; }
.module { padding: 2pt 0; border-bottom: 1px dotted #e4e1d8; }
.module-num { font-weight: 700; color: #c85c3c; margin-right: 4pt; }
.faq dt { font-weight: 600; margin-top: 7pt; color: #0f2a4a; font-size: 9.5pt; }
.faq dd { margin: 1pt 0 3pt; font-size: 9pt; color: #171717; }
.cta-box { background: #0f2a4a; color: #fafaf7; padding: 10pt 12pt; margin-top: 12pt; border-radius: 4pt; font-size: 9.5pt; }
.cta-box a { color: #e88b70; text-decoration: underline; }
.cta-box strong { color: #e88b70; }
a { color: #0f2a4a; }
.page-break { page-break-before: always; }
.small { font-size: 8pt; color: #555; }
ul.compact { margin: 2pt 0 2pt 14pt; padding: 0; font-size: 9pt; }
ul.compact li { margin-bottom: 1pt; }
"""

MODULES_FR = [
    ("01", "Python pour le travail sur données"),
    ("02", "Introduction au machine learning"),
    ("03", "ML classique : classification, régression, clustering"),
    ("04", "Systèmes de recommandation"),
    ("05", "Traitement automatique du langage"),
    ("06", "ML moderne : ANN, CNN, RNN"),
    ("07", "LLM et IA générative"),
    ("08", "MLOps et déploiement"),
    ("09", "Projet capstone"),
    ("10", "Portfolio"),
]

MODULES_EN = [
    ("01", "Python for data work"),
    ("02", "Introduction to machine learning"),
    ("03", "Classical ML: classification, regression, clustering"),
    ("04", "Recommender systems"),
    ("05", "Natural language processing"),
    ("06", "Modern ML: ANN, CNN, RNN"),
    ("07", "LLMs and generative AI"),
    ("08", "MLOps and deployment"),
    ("09", "Capstone project"),
    ("10", "Portfolio"),
]

HTML_FR = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<style>{STYLE}</style>
</head>
<body>

<div class="hero">
  <h1>Bootcamp Machine Learning &amp; IA</h1>
  <p class="tagline">Programme en cohorte de 10 semaines. Dix modules de Python au MLOps, capstone déployé, portfolio public.</p>
  <div class="hero-meta">
    <span><strong>Formateur</strong> Dr. Yaé Ulrich Gaba</span>
    <span><strong>Durée</strong> 10 sem. temps plein / 20 sem. temps partiel</span>
    <span><strong>Niveau</strong> Intermédiaire à Avancé</span>
    <span><strong>Format</strong> Sur site, en ligne, ou hybride</span>
    <span><strong>Langues</strong> Français &amp; Anglais</span>
    <span><strong>Certificat</strong> Attestation de réalisation</span>
  </div>
</div>

<div class="cohort-box">
<strong>Cohorte fondatrice :</strong> février – avril 2027 (temps plein, 10 semaines) · février – juin 2027 (temps partiel, 20 semaines). Candidatures ouvertes jusqu'à mi-janvier 2027.<br>
<strong>Tarif :</strong> Résidents Afrique <strong>€2 000</strong> · International <strong>€3 500</strong> · Cohortes privées d'entreprise : devis sur demande.
</div>

<h2>Pourquoi ce bootcamp</h2>
<p>La demande mondiale d'ingénieurs ML déployables en production dépasse largement l'offre formée, et l'écart est plus marqué en Afrique qu'ailleurs. La plupart des cursus universitaires en informatique se terminent avant le deep learning ; les MOOC supposent un premier emploi en ingénierie logicielle. Ce bootcamp cible exactement ce trou : il prend des diplômés quantitatifs et les amène en dix semaines au niveau de mise en production que recherchent les équipes ML africaines et internationales.</p>

<h2>Le programme en bref</h2>
<table class="facts">
<tr><td>Sessions en direct</td><td>60+ (cours, ateliers, revues capstone, intervenants)</td></tr>
<tr><td>Heures de cours</td><td>200 (60 % en direct · 40 % asynchrone)</td></tr>
<tr><td>Projet capstone</td><td>1 (équipe ou individuel) — déployé en ligne</td></tr>
<tr><td>Intervenants industriels</td><td>8</td></tr>
<tr><td>Permanences</td><td>Hebdomadaires avec assistants d'enseignement</td></tr>
<tr><td>Livrable final</td><td>Capstone déployé + pièce de portfolio publique</td></tr>
</table>

<h2>Les dix modules</h2>
<div class="modules">
{''.join(f'<div class="module"><span class="module-num">{n}</span>{t}</div>' for n, t in MODULES_FR)}
</div>

<div class="page-break"></div>

<h2>Pédagogie</h2>
<p>« Approche par la pratique » recouvre ici deux choix concrets. D'abord, les erreurs sont attendues et exploitées : certaines versions de notebooks d'atelier sont volontairement truffées de fuites de données ou d'évaluations mal construites pour que les participants les repèrent et les corrigent. Ensuite, le rythme est hebdomadaire et cumulatif : chaque semaine ferme sur un livrable repris la semaine suivante — pas de sprint final où l'on essaie de tout recoller.</p>

<h2>Questions fréquentes</h2>
<dl class="faq">
<dt>Peut-on suivre le bootcamp à temps partiel ?</dt>
<dd>Oui. Un format 20 semaines à environ 10 heures par semaine fonctionne en parallèle du format intensif 10 semaines.</dd>

<dt>Quelle est la procédure de sélection ?</dt>
<dd>Dossier de candidature plus un court test technique. L'auto-évaluation honnête en amont réduit le risque de décrochage en semaine 1.</dd>

<dt>Le certificat aide-t-il à l'embauche ?</dt>
<dd>Le certificat est une attestation de réalisation, pas un diplôme accrédité. Ce qui est crédible auprès d'un recruteur technique : votre capstone déployé (lien public visitable) et votre portfolio GitHub. Le bootcamp construit explicitement les deux.</dd>

<dt>Les intervenants industriels recrutent-ils ?</dt>
<dd>Non. Ils partagent une réalité métier ; ils ne font pas de pitch produit et ne recrutent pas.</dd>
</dl>

<h2>Public visé &amp; prérequis</h2>
<ul class="compact">
<li>Professionnels en activité qui passent à des rôles ML/IA depuis des domaines voisins (génie logiciel, analyse de données, finance quantitative, actuariat).</li>
<li>Étudiants de licence avancée et de master en maths, informatique, statistique, ingénierie, sciences sociales quantitatives.</li>
<li>Cohortes d'entreprise : banques, télécoms, assureurs, fintech, équipes data du secteur public.</li>
<li><strong>Indispensable :</strong> Python au niveau « je peux lire et modifier un script de 200 lignes sans me perdre ». Algèbre linéaire, calcul, probabilités de niveau licence.</li>
</ul>

<div class="cta-box">
<strong>Candidater à la cohorte fondatrice</strong> : <a href="mailto:gabayae2@gmail.com?subject=Bootcamp%20ML%20%26%20IA%20%E2%80%94%20candidature%20cohorte%20fondatrice%20f%C3%A9vrier%202027">gabayae2@gmail.com</a><br>
Page web complète : <a href="https://gabayae.github.io/workshops/ml-ai-bootcamp/fr/">gabayae.github.io/workshops/ml-ai-bootcamp/fr/</a><br>
Organisation : AIRINA Labs · Dr. Yaé Ulrich Gaba (PhD topologie, UCT) · Cotonou, Bénin
</div>

</body>
</html>
"""

HTML_EN = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>{STYLE}</style>
</head>
<body>

<div class="hero">
  <h1>Machine Learning &amp; AI Bootcamp</h1>
  <p class="tagline">A 10-week cohort program. Ten modules from Python to MLOps, deployed capstone, public portfolio.</p>
  <div class="hero-meta">
    <span><strong>Instructor</strong> Dr. Yaé Ulrich Gaba</span>
    <span><strong>Duration</strong> 10 wk full-time / 20 wk part-time</span>
    <span><strong>Level</strong> Intermediate to Advanced</span>
    <span><strong>Format</strong> On-site, live online, or hybrid</span>
    <span><strong>Languages</strong> English &amp; French</span>
    <span><strong>Certificate</strong> Completion attestation</span>
  </div>
</div>

<div class="cohort-box">
<strong>Founding cohort:</strong> February – April 2027 (full-time, 10 weeks) · February – June 2027 (part-time, 20 weeks). Applications open until mid-January 2027.<br>
<strong>Pricing:</strong> Africa residents <strong>€2,000</strong> · International <strong>€3,500</strong> · Private corporate cohorts: on request.
</div>

<h2>Why this bootcamp</h2>
<p>Global demand for production-ready ML engineers far exceeds trained supply, and the gap is wider in Africa than anywhere else. Most African undergraduate computer-science curricula end before deep learning; the MOOCs that fill the void presume a prior software-engineering job. This bootcamp targets that gap directly — it takes quantitatively trained graduates and brings them in ten weeks to the production-ready level that African and international ML teams now hire for.</p>

<h2>Program at a glance</h2>
<table class="facts">
<tr><td>Live sessions</td><td>60+ (lectures, labs, capstone reviews, speakers)</td></tr>
<tr><td>Course hours</td><td>200 (60 % live · 40 % structured asynchronous)</td></tr>
<tr><td>Capstone project</td><td>1 (team or individual) — publicly deployed</td></tr>
<tr><td>Industry speakers</td><td>8</td></tr>
<tr><td>Office hours</td><td>Weekly, with teaching assistants</td></tr>
<tr><td>Final deliverable</td><td>Deployed capstone + public portfolio piece</td></tr>
</table>

<h2>The ten modules</h2>
<div class="modules">
{''.join(f'<div class="module"><span class="module-num">{n}</span>{t}</div>' for n, t in MODULES_EN)}
</div>

<div class="page-break"></div>

<h2>Pedagogy</h2>
<p>"Hands-on approach" means two concrete choices here. First, errors are expected and leveraged: some lab-notebook versions are deliberately seeded with data leaks or badly-constructed evaluations for participants to spot and correct. Second, the cadence is weekly and cumulative — each week closes on a deliverable that gets picked up the next week, with no final sprint trying to glue everything together.</p>

<h2>Frequently asked questions</h2>
<dl class="faq">
<dt>Can I take the bootcamp part-time while working?</dt>
<dd>Yes. A 20-week part-time format at roughly 10 hours per week runs in parallel with the 10-week full-time intensive.</dd>

<dt>What is the selection process?</dt>
<dd>Application form plus a short technical test. An honest self-assessment up front reduces the risk of dropping out in week 1.</dd>

<dt>Does the certificate help with hiring?</dt>
<dd>The certificate is a completion attestation, not an accredited degree. What is credible to a technical recruiter is your deployed capstone (a public, visitable link) and your GitHub portfolio. The bootcamp explicitly builds both.</dd>

<dt>Do the industry speakers recruit?</dt>
<dd>No. They share a working reality; they do not pitch products and do not recruit.</dd>
</dl>

<h2>Target audience &amp; prerequisites</h2>
<ul class="compact">
<li>Working professionals transitioning into ML/AI roles from adjacent fields (software engineering, data analysis, quantitative finance, actuarial science).</li>
<li>Advanced undergraduate and master's students in maths, CS, statistics, engineering, quantitative social sciences.</li>
<li>Corporate cohorts: banks, telecoms, insurers, fintech, public-sector data teams.</li>
<li><strong>Required:</strong> Python at the "I can read and modify a 200-line script without getting lost" level. Undergraduate linear algebra, calculus, probability.</li>
</ul>

<div class="cta-box">
<strong>Apply to the founding cohort</strong>: <a href="mailto:gabayae2@gmail.com?subject=ML%20%26%20AI%20Bootcamp%20%E2%80%94%20Application%20for%20the%20founding%20cohort%20February%202027">gabayae2@gmail.com</a><br>
Full page: <a href="https://gabayae.github.io/workshops/ml-ai-bootcamp/en/">gabayae.github.io/workshops/ml-ai-bootcamp/en/</a><br>
Organization: AIRINA Labs · Dr. Yaé Ulrich Gaba (PhD Topology, UCT) · Cotonou, Benin
</div>

</body>
</html>
"""


def render(html: str, out_path: Path) -> None:
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(html)
        tmp_path = Path(tmp.name)
    try:
        subprocess.run(
            [
                CHROME,
                "--headless",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={out_path}",
                tmp_path.as_uri(),
            ],
            check=True,
            capture_output=True,
        )
        print(f"OK: {out_path.relative_to(REPO_ROOT)}  ({out_path.stat().st_size:,} B)")
    finally:
        os.unlink(tmp_path)


if __name__ == "__main__":
    render(HTML_FR, OUT_DIR / "bootcamp_ml_ai_fr.pdf")
    render(HTML_EN, OUT_DIR / "bootcamp_ml_ai_en.pdf")
