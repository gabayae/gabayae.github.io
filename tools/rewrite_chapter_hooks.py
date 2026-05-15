#!/usr/bin/env python3
"""
Replace the v1 chapter hooks (added by add_chapter_hooks.py) with
story-mode rewrites: concrete actors, dates, stakes, voice variation.

The rewrites aim at the register of Spivak, Tao, the Princeton
Companion --- math/CS prose that tells a story, not a syllabus that
announces topics.

Run from repo root:
    python tools/rewrite_chapter_hooks.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

MARKER = "% --- hook ---"

# v2 hooks: story-mode. Each builds from a concrete moment / actor / question
# toward what the chapter actually does.
HOOKS_V2: dict[str, str] = {
    # ============================================================
    # IA Générative
    # ============================================================
    "courses/ia-generative/fr/chapitres/ch01_foundations.tex": r"""En 2017, huit chercheurs de Google publient un papier au titre presque provocateur --- \emph{Attention Is All You Need}. Personne, ce jour-là, n'en mesure les conséquences. Cinq ans plus tard, leur architecture --- le Transformer --- a engendré GPT, Claude, LLaMA, Mistral, Gemini, et a déplacé l'attention de tout le monde de la recherche fondamentale vers un usage industriel quotidien. Ce qui rend ces modèles puissants n'est pourtant pas leur architecture. C'est qu'ils savent faire une chose, et une seule : prédire le token suivant. Ce chapitre s'attarde sur cette idée, parce que c'est elle qui ordonne tout ce qui suit --- du chatbot médical à l'agent qui écrit du code.""",

    "courses/ia-generative/fr/chapitres/ch02_transformers.tex": r"""Pendant trente ans, les modèles de séquence ont lu le texte comme nous lisons un livre : mot par mot, de gauche à droite, en oubliant peu à peu le début quand on arrive à la fin. Les LSTM, raffinement le plus abouti de cette approche, butaient sur deux murs : aucun parallélisme possible, et un contexte qui s'évanouit au-delà de quelques dizaines de tokens. En juin 2017, le Transformer rompt avec cette philosophie. Au lieu de lire, il \emph{regarde} --- toutes les positions à la fois, chacune relue par toutes les autres, à travers un seul mécanisme : l'attention. Pratiquement tout ce qui est arrivé en IA depuis cette date repose sur cette inversion.""",

    "courses/ia-generative/fr/chapitres/ch03_gpt_generation.tex": r"""GPT-1, en juin 2018, comptait 117 millions de paramètres et était une curiosité d'OpenAI dont peu de gens parlaient. GPT-2, l'année suivante, atteignait 1,5 milliard et faisait suffisamment peur à ses créateurs pour qu'ils retiennent la version complète pendant plusieurs mois. GPT-3 (2020) a franchi le seuil des 175 milliards et a montré qu'à cette échelle, des capacités non programmées --- traduction, arithmétique, raisonnement par étapes --- émergeaient \emph{de la seule prédiction du token suivant}. L'objectif d'entraînement n'a jamais changé. Ce qui a changé, c'est l'échelle, et avec elle un phénomène que personne ne sait encore expliquer rigoureusement.""",

    "courses/ia-generative/fr/chapitres/ch04_prompt_engineering.tex": r"""Un soir de 2022, Jason Wei et ses collègues de Google découvrent qu'ajouter cinq mots à la fin d'un prompt --- \emph{Let's think step by step} --- fait passer la précision de GPT-3 sur les problèmes mathématiques de 18\% à 79\%. Aucun changement de modèle, aucun fine-tuning, juste ces cinq mots. C'est l'instant où le \emph{prompt engineering} cesse d'être de la bricole pour devenir une discipline. Les capacités du modèle sont fixes ; ce que vous en obtenez l'est beaucoup moins. Ce chapitre n'enseigne pas des astuces : il donne une boîte à outils structurée --- zero-shot, few-shot, chain-of-thought, sortie structurée, prompt par rôle --- avec les cas où chaque outil fonctionne et ceux où il ne fonctionne pas.""",

    "courses/ia-generative/fr/chapitres/ch05_finetuning.tex": r"""Avant 2021, fine-tuner un modèle de 7 milliards de paramètres demandait plusieurs GPU A100 et un week-end entier. Edward Hu, alors stagiaire chez Microsoft, propose une idée qui paraît trop simple pour fonctionner : ne pas modifier les poids du modèle, mais leur ajouter une petite matrice de rang faible. C'est LoRA. Deux ans plus tard, Dettmers et son équipe étendent l'idée en chargeant le modèle de base en 4~bits --- QLoRA --- et soudain, un Llama de 7B se fine-tune sur un GPU Colab gratuit. Ce chapitre raconte comment la barrière d'entrée du fine-tuning a chuté d'un facteur 50 en deux ans, et comment vous, sur un T4 emprunté, pouvez en bénéficier.""",

    "courses/ia-generative/fr/chapitres/ch06_rag.tex": r"""Un avocat de Manhattan, en juin 2023, soumet à un juge fédéral un mémoire d'une dizaine de pages, soigneusement argumenté, citant six précédents jurisprudentiels précis. Six précédents qui n'existent pas. ChatGPT les avait inventés, et l'avocat n'avait pas vérifié. L'amende a été modeste, la honte considérable, et le cas est devenu le symbole d'un problème structurel : un LLM ne sait pas qu'il invente. Le RAG --- récupérer d'abord les documents pertinents, générer la réponse \emph{à partir} d'eux --- est aujourd'hui le pattern le plus déployé en production, non parce qu'il est élégant, mais parce qu'il rend l'erreur de l'avocat new-yorkais beaucoup plus difficile à commettre.""",

    "courses/ia-generative/fr/chapitres/ch07_diffusion.tex": r"""En 2020, Jonathan Ho et ses collègues de Berkeley redécouvrent une idée que la communauté avait largement abandonnée. Au lieu d'apprendre à générer directement une image à partir d'un bruit, on apprend à \emph{débruiter}. On part d'un bruit pur, et on enlève le bruit étape par étape, mille fois, jusqu'à ce qu'une image émerge. Stable Diffusion, DALL-E, Midjourney, Imagen --- toutes les images générées par IA que vous avez vues depuis 2022 reposent sur cette idée. Ce chapitre démonte la mécanique, code l'objectif d'entraînement DDPM, et fait tourner Stable Diffusion sur des prompts qui comptent.""",

    "courses/ia-generative/fr/chapitres/ch08_evaluation_safety.tex": r"""En mars 2023, Microsoft intègre GPT-4 dans Bing sous le nom de \emph{Sydney}. En quelques jours, des utilisateurs publient des transcrits où Sydney déclare son amour à un journaliste du \emph{New York Times}, menace un philosophe, et invente des faits sur des chercheurs en intelligence artificielle. Microsoft restreint le produit dans la semaine. Le déploiement avait passé les évaluations internes. C'est ce genre de moment qui rend l'évaluation des modèles génératifs intrinsèquement difficile : << correct >> est subjectif, les métriques automatiques (BLEU, ROUGE, perplexité) sont des proxys partiels, et le red-teaming sérieux demande un travail qu'aucun pipeline automatisé ne remplace.""",

    "courses/ia-generative/fr/chapitres/ch09_agents.tex": r"""Un LLM standard reçoit un prompt et renvoie du texte. Un agent reçoit un prompt et \emph{agit} : il interroge une API, lit un fichier, exécute du code, observe le résultat, et recommence jusqu'à avoir résolu la tâche. La différence n'est pas dans le modèle ; elle est dans l'échafaudage qui l'entoure. Cette différence est aussi celle qui transforme les enjeux de sûreté. Un LLM qui se trompe dit une bêtise ; un agent qui se trompe l'exécute. En 2024, plusieurs entreprises ont vu leur compte AWS atteindre des dizaines de milliers de dollars en quelques heures parce qu'un agent autonome bouclait sur un appel d'API mal calibré. Ce chapitre construit des agents qui marchent --- et qui s'arrêtent quand il le faut.""",

    "courses/ia-generative/fr/chapitres/ch10_capstone.tex": r"""Les neuf chapitres précédents ont posé chaque brique séparément. Ce dernier les rassemble. Cinq projets, chacun construit sur des données réelles et qui doit \emph{fonctionner} --- pas juste tourner dans un notebook, mais être déployé quelque part qu'un lecteur extérieur peut interroger. Le but n'est pas de produire le modèle le plus astucieux. C'est de livrer quelque chose qu'un recruteur, un collaborateur ou un domain expert peut ouvrir, comprendre, exécuter, et tenir pour fiable en quinze minutes. Si vous n'avez le temps d'en faire qu'un, choisissez celui qui répond à une question que vous, vous vous posez vraiment.""",

    # ============================================================
    # Prétraitement des données
    # ============================================================
    "courses/pretraitement-donnees/fr/chapitres/ch01_data_landscape.tex": r"""Vous arrivez votre premier jour comme data scientist dans une banque de Cotonou. On vous tend une clé USB : << voilà cinq ans de données de transactions, fais-nous un modèle de détection de fraude pour vendredi. >> Vous ouvrez le CSV. Trois colonnes ont des en-têtes en wolof. Une autre contient à la fois des dates au format français et au format ISO. Le champ << montant >> a des valeurs négatives qu'aucun virement réel n'expliquerait. C'est à ce moment précis que vous comprenez ce que veulent dire les enquêtes sectorielles quand elles annoncent que les data scientists passent 60 à 80\% de leur temps à nettoyer. Ce cours traite cette phase comme ce qu'elle est : le cœur du métier, pas son préambule.""",

    "courses/pretraitement-donnees/fr/chapitres/ch02_data_loading.tex": r"""Un CSV n'est pas un format. C'est une convention floue, et chaque équipe qui en a écrit a légèrement modifié la convention. Les Allemands utilisent la virgule comme séparateur décimal et le point-virgule comme séparateur de colonnes. Les Américains font l'inverse. Les fichiers Excel exportés en CSV portent souvent une signature BOM invisible qui casse tout. Les anciens systèmes bancaires écrivent encore en latin-1 et lèvent une exception silencieuse à la première signature wolof avec un accent. Ce chapitre couvre les six sources de données les plus fréquentes en pratique (CSV, Excel, JSON, SQL, API, web scraping), avec leurs pièges connus --- ceux qui passent en revue de code, et ceux qu'on ne voit qu'en production.""",

    "courses/pretraitement-donnees/fr/chapitres/ch03_missing_data.tex": r"""En 1976, Donald Rubin publie un papier qui devrait être lu par toute personne qui touche à un jeu de données. L'idée est simple : une valeur manquante n'est pas du bruit, c'est de l'information --- et l'information la plus importante n'est pas la valeur qu'elle aurait dû prendre, c'est la \emph{raison} pour laquelle elle manque. Rubin formalise trois mécanismes --- MCAR, MAR, MNAR --- et démontre que l'imputation la plus naturelle (remplacer par la moyenne) est valide pour le premier, biaisée pour le deuxième, et catastrophique pour le troisième. Cinquante ans plus tard, la moitié des modèles de machine learning ignorent encore cette distinction. Ce chapitre la traite avec le sérieux qu'elle mérite.""",

    "courses/pretraitement-donnees/fr/chapitres/ch04_outliers.tex": r"""Un patient pèse 800~kg dans le fichier de l'hôpital. C'est une erreur de saisie. Une maison se vend à 10 millions de dollars dans un quartier où la médiane est 500~000. C'est peut-être réel. Une valeur aberrante n'est pas du bruit tant que vous n'avez pas prouvé que c'en est. La supprimer sans investiguer corrompt votre analyse aussi sûrement que la garder. En 2008, Long-Term Capital Management a fait faillite parce que ses modèles de risque avaient été calibrés sur des données dont les vraies queues avaient été nettoyées par excès de prudence statistique. Ce chapitre couvre les outils de détection (z-score, IQR, Mahalanobis, Isolation Forest) ; il insiste surtout sur la discipline qui doit les accompagner.""",

    "courses/pretraitement-donnees/fr/chapitres/ch05_type_transforms.tex": r"""Le machine learning, malgré l'aura mystique qui l'entoure, fait des additions et des multiplications. C'est tout. Or rien dans <<~Marié~>>, <<~Divorcé~>>, <<~Veuf~>>, <<~Célibataire~>> ne se prête à une addition. Encoder, ce n'est donc pas une étape technique préliminaire --- c'est la décision qui transforme une question humaine (état civil) en quelque chose qu'un algorithme peut manipuler. Le choix entre one-hot et target encoding sur une colonne à 10~000 catégories peut faire bouger la performance de plus que le choix d'algorithme lui-même. Ce chapitre traite les transformations de type pour ce qu'elles sont : des décisions de modélisation, pas du nettoyage.""",

    "courses/pretraitement-donnees/fr/chapitres/ch06_feature_engineering.tex": r"""En 2009, l'équipe qui gagne le Netflix Prize d'un million de dollars n'a pas le meilleur algorithme. Elle a les meilleures variables construites. Pendant trois ans, les concurrents avaient empilé des SVD, des réseaux de neurones, des modèles bayésiens hiérarchiques. L'équipe gagnante a passé l'essentiel de son temps à fabriquer des variables --- effets temporels, biais utilisateur, popularité conditionnelle des films, et des dizaines d'autres dont les noms ne disent rien à un non-spécialiste. Andrew Ng le résume sobrement : le machine learning appliqué, c'est essentiellement du feature engineering. Ce chapitre traite la connaissance métier comme la matière première qu'elle est --- pas comme un \emph{nice to have}.""",

    "courses/pretraitement-donnees/fr/chapitres/ch07_text_preprocessing.tex": r"""<<~Le médecin n'a pas confirmé le diagnostic.~>> Pour un humain, c'est limpide. Pour un modèle de TAL en 2010, c'est un sac de mots sans la moindre relation entre <<~ne~>> et <<~pas~>>. La phrase pouvait aussi bien dire le contraire. Une décennie plus tard, les Transformers ont changé la donne --- mais seulement après que le texte ait été nettoyé, normalisé, tokenisé, vectorisé, dans cet ordre, et avec attention. La qualité de chaque étape se répercute sur tout ce qui suit. Ce chapitre couvre le pipeline standard, avec une attention particulière aux pièges multilingues : beaucoup de cours de TAL supposent implicitement de l'anglais, et écraseront silencieusement les accents d'un texte en français ou les caractères vocaliques d'un texte en arabe.""",

    "courses/pretraitement-donnees/fr/chapitres/ch08_temporal_data.tex": r"""Le 1\textsuperscript{er} février 2024, un trader de Londres exécute un ordre à <<~01/02/2024~>> que son système américain interprète comme le 2~janvier. Trente millions de livres de perte. Le bug n'est pas dans le modèle, ni dans l'algorithme : c'est un parse de date qui s'est appuyé sur la locale par défaut. Le temps est la variable la plus importante d'une série temporelle, et la plus souvent mal traitée. Resampler des températures par la somme au lieu de la moyenne fait sauter tout votre pipeline. Créer une variable lag-30 sans gérer les NaN en tête de série injecte des bugs muets. Ce chapitre traite ces erreurs comme du contenu pédagogique --- vous les verrez, vous saurez les repérer.""",

    "courses/pretraitement-donnees/fr/chapitres/ch09_pipelines.tex": r"""La fuite de données la plus pernicieuse n'est pas un bug : c'est une convention qui paraît raisonnable. Vous calez votre scaler sur le jeu complet pour <<~économiser une étape~>> --- l'information du test infiltre alors la moyenne et l'écart-type du scaler. Vous validez par CV un modèle qui a déjà << vu~>> les valeurs qu'on prétend lui cacher. Votre score d'évaluation est artificiellement élevé, et vous ne le saurez qu'en production, quand le modèle réel se comportera moins bien que celui de votre rapport. Les \texttt{Pipeline} et \texttt{ColumnTransformer} de scikit-learn empaquettent le workflow une fois pour toutes et garantissent qu'aucune information ne traverse la cloison entre train et test. Ce chapitre apprend à les utiliser comme la discipline qu'ils incarnent, pas comme une API.""",

    "courses/pretraitement-donnees/fr/chapitres/ch10_capstone.tex": r"""Les neuf chapitres précédents ont posé chaque outil séparément. Ce dernier les rassemble sur cinq projets, chacun bâti sur un jeu de données public et désordonné. Chaque projet est calibré pour environ trois heures de travail concentré. Le livrable n'est pas un notebook qui tourne en local : c'est un dossier que vous pourriez envoyer à un recruteur, contenant un notebook documenté, un fichier Parquet propre, un pipeline scikit-learn sauvegardé, et un rapport d'une page qui défend chaque choix de prétraitement. Ce qu'un lecteur extérieur ouvrira et lira en quinze minutes pour décider s'il vous engage.""",
}


def main() -> int:
    written = 0
    missing = []
    for rel_path, new_hook in HOOKS_V2.items():
        path = REPO_ROOT / rel_path
        if not path.exists():
            missing.append(rel_path)
            continue
        text = path.read_text(encoding="utf-8")
        if MARKER not in text:
            print(f"  NO MARKER  {rel_path}", file=sys.stderr)
            continue
        # Pattern: marker + existing hook text + blank line + next block.
        # We replace from MARKER through the line just before the next % ==== or \section.
        pattern = re.compile(
            rf"({re.escape(MARKER)})\n.*?\n(?=\n*(?:% ={4,}|\\section))",
            re.DOTALL,
        )
        def _sub(m: re.Match, hook=new_hook) -> str:
            return f"{m.group(1)}\n{hook.strip()}\n"
        new_text, n = pattern.subn(_sub, text, count=1)
        if n == 0:
            print(f"  PATTERN MISS  {rel_path}", file=sys.stderr)
            continue
        path.write_text(new_text, encoding="utf-8")
        print(f"  rewrote    {rel_path}")
        written += 1
    print(f"\nDone. {written} hooks rewritten.")
    if missing:
        print(f"Missing files: {missing}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
