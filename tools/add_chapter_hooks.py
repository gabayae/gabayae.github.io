#!/usr/bin/env python3
"""
Insert a motivational opening paragraph into each FR chapter file,
between the opening quote block and the first \\section.

Each hook is 2-3 sentences with concrete stakes, written to replace
the previous cold "quote → definition" pattern with something that
gives the reader a reason to keep reading.

Run from repo root:
    python tools/add_chapter_hooks.py

Idempotent: if a hook marker is already present, the script skips the file.
"""

from __future__ import annotations
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

HOOK_MARKER = "% --- hook ---"  # sentinel comment to detect already-inserted hooks

HOOKS: dict[str, str] = {
    # ============================================================
    # IA Générative
    # ============================================================
    "courses/ia-generative/fr/chapitres/ch01_foundations.tex": r"""GPT, Claude, LLaMA, Mistral, Gemini --- tous ces systèmes reposent sur la même idée : prédire le token suivant. Pas une idée par modèle. La même idée, à des échelles différentes. Ce chapitre construit cette idée de zéro, des tokens et de leurs plongements jusqu'à la perplexité et à votre première génération de texte avec GPT-2. À la fin, vous comprendrez ce que fait \emph{réellement} un modèle de langage --- avant qu'on l'appelle assistant, chatbot, ou agent.""",

    "courses/ia-generative/fr/chapitres/ch02_transformers.tex": r"""Avant 2017, les modèles de séquence lisaient le texte mot par mot, de gauche à droite, et oubliaient le début quand ils arrivaient à la fin. Les RNN avaient deux problèmes durs : pas de parallélisme, et un contexte qui s'efface. Le Transformer a balayé les deux d'un coup avec un seul mécanisme --- l'attention. Aujourd'hui, à peu près tout en IA générative repose sur cette architecture ; en comprendre l'intérieur revient à comprendre la moitié du domaine.""",

    "courses/ia-generative/fr/chapitres/ch03_gpt_generation.tex": r"""De GPT-1 (117M de paramètres en 2018) à GPT-4 (plusieurs centaines de milliards, en 2023), l'objectif d'entraînement n'a jamais changé : prédire le token suivant. Ce qui change, c'est l'échelle, et avec elle des capacités qui n'étaient pas programmées. Ce chapitre démonte la boucle de génération autorégressive, montre pourquoi le choix de la stratégie de décodage importe autant que le modèle lui-même, et vous fait écrire votre premier générateur de texte en quelques lignes.""",

    "courses/ia-generative/fr/chapitres/ch04_prompt_engineering.tex": r"""Le même modèle, deux prompts différents, deux comportements complètement différents. Capacités du modèle : fixées. Ce que vous en obtenez : presque entièrement déterminé par la manière dont vous lui parlez. Ce chapitre n'est pas un guide de << astuces magiques >> ; c'est une boîte à outils structurée --- zero-shot, few-shot, chain-of-thought, sortie structurée, prompt par rôle --- avec les cas où chaque outil échoue.""",

    "courses/ia-generative/fr/chapitres/ch05_finetuning.tex": r"""Vous pouvez prompter un LLM pour qu'il fasse semblant d'être un médecin. Pour qu'il en parle vraiment comme un --- avec le vocabulaire, le format de note SOAP, les conventions de prescription --- il faut le fine-tuner. Pendant longtemps, ça demandait plusieurs GPU A100. LoRA, puis QLoRA, ont changé l'équation : on peut désormais fine-tuner un modèle 7B sur un seul GPU Colab gratuit. Ce chapitre montre comment, et où sont les pièges.""",

    "courses/ia-generative/fr/chapitres/ch06_rag.tex": r"""Un LLM ne connaît rien après sa date d'entraînement. Posez-lui une question sur vos données internes, et il \emph{inventera} une réponse plausible. Le RAG résout les deux problèmes en une étape : on récupère d'abord les documents pertinents, puis on génère la réponse en s'appuyant dessus. C'est aujourd'hui le pattern d'IA générative le plus déployé en production --- bien plus que le fine-tuning, parce qu'il est plus simple, plus traçable, et plus facile à mettre à jour.""",

    "courses/ia-generative/fr/chapitres/ch07_diffusion.tex": r"""Stable Diffusion, Midjourney, DALL-E, Imagen --- toutes les images générées par IA que vous avez vues cette année viennent d'un modèle de diffusion. L'idée est élégante au point d'en paraître trompeuse : partir d'un bruit pur, et apprendre à le débruiter étape par étape. Ce qui émerge à la fin n'est ni du bruit ni rien d'aléatoire, mais une image cohérente conditionnée par un prompt. Ce chapitre démonte la mécanique, code l'objectif d'entraînement, et fait tourner Stable Diffusion sur des prompts qui comptent.""",

    "courses/ia-generative/fr/chapitres/ch08_evaluation_safety.tex": r"""<< Si vous ne pouvez pas le mesurer, vous ne pouvez pas l'améliorer. >> --- l'aphorisme classique. Pour les modèles génératifs, il faut en ajouter un deuxième : si vous ne testez pas pour le pr\'ejudice, vous l'embarquerez en production. L'évaluation de modèles génératifs est intrinsèquement difficile parce que << correct >> est subjectif, et que les métriques automatiques (BLEU, ROUGE, perplexité) sont des proxys, jamais des vérités. Ce chapitre couvre les métriques quand elles fonctionnent, le red-teaming quand elles ne suffisent pas, et l'alignement (RLHF, DPO) comme tentative de réponse de fond.""",

    "courses/ia-generative/fr/chapitres/ch09_agents.tex": r"""Un LLM standard prend un prompt et renvoie du texte. Un agent prend un prompt et \emph{agit} --- il interroge une API, lit un fichier, exécute du code, observe le résultat, et recommence jusqu'à avoir résolu la tâche. Même modèle de base, mais avec un échafaudage qui transforme un générateur de texte en système autonome. C'est aussi là que les enjeux de sûreté deviennent concrets : un agent qui se trompe ne dit pas une bêtise, il l'exécute.""",

    "courses/ia-generative/fr/chapitres/ch10_capstone.tex": r"""Vous avez vu les briques. Maintenant, vous construisez. Cinq projets de fin de cours, chacun intégrant des notions de plusieurs chapitres et aboutissant à une application qui tourne. Le but n'est pas d'écrire le modèle le plus astucieux --- c'est de livrer quelque chose qu'un lecteur extérieur peut ouvrir, comprendre, exécuter, et auquel il peut faire confiance en quinze minutes. Choisissez un projet (ou plusieurs) selon votre intérêt.""",

    # ============================================================
    # Prétraitement des données
    # ============================================================
    "courses/pretraitement-donnees/fr/chapitres/ch01_data_landscape.tex": r"""Les enquêtes sectorielles sont unanimes : un data scientist passe entre 60 et 80\% de son temps à nettoyer et préparer ses données. Pourtant, la majorité des cours de machine learning expédient cette phase en un seul chapitre, pressés d'arriver aux mod\`eles. Ce cours fait le pari inverse : trente heures sur ce qui consomme \emph{vraiment} le temps de projet. Avant le premier modèle, on regarde ce qu'on a, ce qui manque, ce qui ment, et comment fabriquer un jeu de données dont les conclusions tiennent debout.""",

    "courses/pretraitement-donnees/fr/chapitres/ch02_data_loading.tex": r"""On ne peut pas analyser ce qu'on n'arrive pas à charger. Les vrais CSV ont des encodages incohérents, des d\'elimiteurs surprenants, des en-t\^etes sales, des types mélangés. Les JSON d'API sont imbriqués et paginés. Les bases SQL exigent qu'on pousse le filtrage côté serveur sous peine de saturer la mémoire. Ce chapitre couvre les six sources de données les plus fréquentes en pratique et les pi\`eges connus de chacune, avant qu'ils ne deviennent vos pi\`eges.""",

    "courses/pretraitement-donnees/fr/chapitres/ch03_missing_data.tex": r"""Une valeur manquante n'est pas du bruit, c'est de l'information. Et l'information la plus importante, c'est \emph{pourquoi} elle manque. Rubin (1976) a formalis\'e trois m\'ecanismes --- MCAR, MAR, MNAR --- et cette distinction n'est pas un d\'etail th\'eorique : elle d\'etermine si votre imputation est valide ou si vous \^etes en train d'introduire un biais syst\'ematique sans le savoir. Ce chapitre montre comment d\'etecter, visualiser, et traiter les valeurs manquantes sans casser silencieusement votre analyse.""",

    "courses/pretraitement-donnees/fr/chapitres/ch04_outliers.tex": r"""Un patient pesant 800\,kg est une erreur de saisie. Une maison à 10 millions de dollars dans un quartier où la médiane est 500\,000 est peut-être réelle. Une valeur aberrante n'est pas du bruit tant que vous n'avez pas prouvé que c'en est. La supprimer sans investiguer corrompt votre analyse aussi sûrement que la garder. Ce chapitre couvre les outils de détection (z-score, IQR, Mahalanobis, Isolation Forest), mais surtout la discipline qui doit les accompagner.""",

    "courses/pretraitement-donnees/fr/chapitres/ch05_type_transforms.tex": r"""Les algorithmes de machine learning ne comprennent pas les catégories. Ils comprennent les nombres. << Male/Female >>, << Low/Medium/High >>, des âges en années et des revenus en milliers de FCFA --- tout cela doit être encodé, mis à l'échelle, parfois discrétisé, avant qu'un modèle puisse en faire quoi que ce soit. Ces transformations paraissent mécaniques, mais le choix entre one-hot et target encoding sur une colonne à forte cardinalit\'e peut faire varier la performance plus que le choix d'algorithme.""",

    "courses/pretraitement-donnees/fr/chapitres/ch06_feature_engineering.tex": r"""Andrew Ng le résume : le machine learning appliqué, c'est essentiellement du feature engineering. Une variable bien construite peut battre un mod\`ele complexe. Une régression linéaire alimentée par les bonnes variables surpasse régulièrement un réseau profond alimenté par les variables brutes. Ce chapitre est l'endroit où la connaissance métier rencontre les données : prix au mètre carré au lieu de prix, âge du bâtiment au lieu d'année de construction, taux de croissance au lieu de valeur absolue.""",

    "courses/pretraitement-donnees/fr/chapitres/ch07_text_preprocessing.tex": r"""Le langage naturel est la donnée la moins structurée qui soit. Un modèle ne lit pas << Le patient présente une fièvre élevée. >> ; il lit une suite d'octets qui doivent être nettoyés, normalisés, tokenis\'es et vectorisés avant qu'il puisse les manipuler. La qualité de chacune de ces quatre étapes se r\'epercute directement sur la qualité de tout système TAL en aval. Ce chapitre couvre le pipeline standard avec une attention particulière aux pi\`eges multilingues, parce que beaucoup de cours TAL supposent implicitement de l'anglais.""",

    "courses/pretraitement-donnees/fr/chapitres/ch08_temporal_data.tex": r"""Le temps est la variable la plus importante d'une série temporelle, et la plus souvent mal traitée. Parser une date << 01/02/2024 >> sans préciser le format vous fera mélanger janvier et février selon la machine. Réagréger des températures par la somme au lieu de la moyenne fait sauter tout votre pipeline. Cr\'eer une variable lag-30 sans pr\'evoir les NaN en t\^ete de s\'erie injecte des bugs muets. Ce chapitre traite ces erreurs comme du contenu pédagogique --- vous les verrez, vous saurez les repérer.""",

    "courses/pretraitement-donnees/fr/chapitres/ch09_pipelines.tex": r"""Le prétraitement à la main est fuite-de-données par d\'efaut. Vous ajustez un scaler sur tout le jeu, vous oubliez d'appliquer la m\^eme transformation au moment de la pr\'ediction, vous changez l'ordre des op\'erations entre entra\^inement et inf\'erence --- chacune de ces erreurs est silencieuse et chacune ruine la validation. Les pipelines scikit-learn empaquettent une fois pour toutes l'ensemble du workflow et garantissent qu'il s'applique identiquement \`a chaque pr\'ediction.""",

    "courses/pretraitement-donnees/fr/chapitres/ch10_capstone.tex": r"""Vous avez les outils. Maintenant, choisissez un vrai problème et appliquez-les de bout en bout. Cinq projets, chacun b\^ati sur un jeu de donn\'ees public r\'eel et d\'esordonn\'e, chacun pens\'e pour \^etre fait en environ trois heures. Le livrable n'est pas un notebook qui tourne en local --- c'est un notebook document\'e, un fichier Parquet propre, et un court rapport qui d\'efend chaque choix de pr\'etraitement. Ce qu'un employeur ouvrira et lira en quinze minutes.""",
}


# Pattern: opening quote block + comment separator + first section.
# We insert the hook between `\end{quote}\n\n` and the first `% ====`
# or `\section{` line. The hook gets a sentinel comment so re-runs are no-ops.
OPENING_RE = re.compile(
    r"(\\end\{quote\}\s*\n)\s*(\n% =+|\n\\section\{)",
    re.MULTILINE,
)


def main() -> int:
    written = 0
    skipped = 0
    for rel_path, hook in HOOKS.items():
        path = REPO_ROOT / rel_path
        if not path.exists():
            print(f"  MISSING  {rel_path}", file=sys.stderr)
            continue

        content = path.read_text(encoding="utf-8")
        if HOOK_MARKER in content:
            print(f"  skipped  {rel_path}  (hook already present)")
            skipped += 1
            continue

        def _sub(m: re.Match) -> str:
            return f"{m.group(1)}\n{HOOK_MARKER}\n{hook.strip()}\n{m.group(2)}"
        new, n = OPENING_RE.subn(_sub, content, count=1)
        if n == 0:
            print(f"  NO MATCH {rel_path}  (pattern not found, file unchanged)", file=sys.stderr)
            continue

        path.write_text(new, encoding="utf-8")
        print(f"  wrote    {rel_path}")
        written += 1

    print(f"\nDone. {written} chapters updated, {skipped} skipped (already had hooks).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
