"""One-shot: prepend Jekyll frontmatter to each workshops/*/{fr,en}/README.md.

Jekyll needs frontmatter to publish these as pages at /workshops/<name>/<lang>/.
The existing H1 (line 1) becomes the frontmatter `title` so al-folio's page
layout renders the title header; the duplicate H1 is stripped from the body.
Idempotent: skips files that already start with a `---` frontmatter block.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent / "workshops"

descriptions = {
    "bayesian-statistics": {
        "fr": "Atelier de 4 jours sur la statistique bayésienne appliquée : PyMC, MCMC, modèles hiérarchiques.",
        "en": "4-day workshop on applied Bayesian statistics: PyMC, MCMC, hierarchical models.",
    },
    "data-science-decision-makers": {
        "fr": "Formation de 3 jours pour managers : comprendre l'IA, cas d'usage, ROI, pilotage de projet data.",
        "en": "3-day executive training: understanding AI, use cases, ROI, steering data projects.",
    },
    "generative-ai-llms": {
        "fr": "Atelier de 3 jours : LLMs, prompt engineering, fine-tuning (LoRA), RAG, déploiement.",
        "en": "3-day workshop: LLMs, prompt engineering, fine-tuning (LoRA), RAG, deployment.",
    },
    "geometric-deep-learning": {
        "fr": "Atelier de 4 jours : GNNs, apprentissage sur variétés, architectures équivariantes.",
        "en": "4-day workshop: GNNs, manifold learning, equivariant architectures.",
    },
    "mlops-in-practice": {
        "fr": "Atelier de 4 jours : Docker, CI/CD, monitoring, MLflow, DVC — du notebook à la production.",
        "en": "4-day workshop: Docker, CI/CD, monitoring, MLflow, DVC — from notebook to production.",
    },
    "python-data-science": {
        "fr": "Atelier de 5 jours : Pandas, visualisation, ML avec scikit-learn.",
        "en": "5-day workshop: Pandas, visualization, ML with scikit-learn.",
    },
    "reinforcement-learning": {
        "fr": "Atelier de 5 jours : MDPs, Q-learning, DQN, policy gradients, acteur-critique.",
        "en": "5-day workshop: MDPs, Q-learning, DQN, policy gradients, actor-critic methods.",
    },
    "r-statistical-analysis": {
        "fr": "Atelier de 4 jours : Tidyverse, ggplot2, modélisation statistique, R Markdown.",
        "en": "4-day workshop: Tidyverse, ggplot2, statistical modelling, R Markdown.",
    },
    "scientific-writing": {
        "fr": "Atelier de 3 jours : rédaction LaTeX, Overleaf, rédaction assistée par IA (Prism).",
        "en": "3-day workshop: LaTeX writing, Overleaf, AI-assisted writing (Prism).",
    },
}

def yaml_escape(s: str) -> str:
    return s.replace('"', '\\"')

def process(readme: Path) -> str:
    text = readme.read_text(encoding="utf-8")
    if text.lstrip().startswith("---"):
        return "skip (already has frontmatter)"

    lines = text.splitlines()
    if not lines or not lines[0].startswith("# "):
        return f"skip (no H1): {readme}"

    title = lines[0][2:].strip()
    workshop = readme.parent.parent.name
    lang = readme.parent.name
    desc = descriptions.get(workshop, {}).get(lang, title)

    body_start = 1
    while body_start < len(lines) and lines[body_start].strip() == "":
        body_start += 1
    body = "\n".join(lines[body_start:])

    frontmatter = (
        "---\n"
        f'layout: page\n'
        f'permalink: /workshops/{workshop}/{lang}/\n'
        f'title: "{yaml_escape(title)}"\n'
        f'description: "{yaml_escape(desc)}"\n'
        f'lang: {lang}\n'
        "---\n\n"
    )
    readme.write_text(frontmatter + body + ("\n" if not body.endswith("\n") else ""), encoding="utf-8")
    return f"wrote: /workshops/{workshop}/{lang}/"

def main():
    readmes = sorted(ROOT.glob("*/[fr,en]*/README.md"))
    if not readmes:
        print("no READMEs found", file=sys.stderr)
        sys.exit(1)
    for r in readmes:
        print(process(r))

if __name__ == "__main__":
    main()
