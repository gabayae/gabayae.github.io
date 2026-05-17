"""Extract chapter titles from EN tex files for the 6 candidate courses."""
import re
import pathlib

SLUGS = [
    "tda",
    "apprentissage-geometrique",
    "apprentissage-renforcement",
    "mlops",
    "ia-generative",
    "apprentissage-automatique",
]
CHAPTER_RE = re.compile(r"\\chapter\*?\{([^}]+)\}")

for slug in SLUGS:
    print(f"\n=== {slug} ===")
    chap_dir = pathlib.Path("courses") / slug / "en" / "chapters"
    for tex in sorted(chap_dir.glob("ch[0-9]*.tex")):
        try:
            text = tex.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = tex.read_text(encoding="latin-1")
        m = CHAPTER_RE.search(text)
        title = m.group(1) if m else "?"
        title = title.replace("--", "—").strip()
        ch_num = tex.stem[2:4]
        print(f"  ch{ch_num}: {title}")
