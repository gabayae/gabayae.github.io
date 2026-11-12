"""Standalone HTML preview of supervision.yml — bypasses Jekyll for fast iteration."""
import yaml, webbrowser, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / '_data' / 'supervision.yml'
data = yaml.safe_load(DATA.read_text(encoding='utf-8'))

students = [s for s in data['students'] if not s.get('hide', False)]
phd     = [s for s in students if s['level'] == 'phd']
masters = [s for s in students if s['level'] == 'masters']
honors  = [s for s in students if s['level'] == 'honors']

def initials(name: str) -> str:
    parts = name.split()
    return (parts[0][0] + parts[-1][0]).upper()

def is_pending(title: str) -> bool:
    t = title.lower()
    return any(x in t for x in ('pending', 'verify', 'compléter'))

LEVEL_LABEL = {'phd': 'PhD', 'masters': 'M', 'honors': 'H'}

def entry(s: dict) -> str:
    name = s['name']
    ini = initials(name)
    av = (f'<img src="{s["photo"]}" alt="">' if s.get('photo')
          else f'<span>{ini}</span>')
    nm = (f'<a href="{s["url"]}" class="thesis-name-link" target="_blank" rel="noopener">'
          f'{name} <i class="fa-solid fa-arrow-up-right-from-square"></i></a>'
          if s.get('url') else name)
    if is_pending(s['title']):
        title_html = '<div class="thesis-title pending">Title forthcoming</div>'
    else:
        badge = ' <span class="thesis-ongoing-badge">Ongoing</span>' if s.get('ongoing') else ''
        title_html = f'<div class="thesis-title">{s["title"]}{badge}</div>'
    summary_html = (f'<div class="thesis-summary">{s["summary_en"].strip()}</div>'
                    if s.get('summary_en') else '')
    level_badge_class = f'thesis-badge {s["level"]}'
    level_label = LEVEL_LABEL[s['level']]
    return (f'<div class="thesis-row">'
            f'<div class="thesis-avatar">{av}</div>'
            f'<span class="{level_badge_class}">{level_label}</span>'
            f'<div>'
            f'<div class="thesis-name">{nm}</div>'
            f'{title_html}{summary_html}'
            f'</div></div>')

def section(name: str, icon: str, entries: list, reverse: bool, count_suffix: str) -> str:
    if not entries:
        return ''
    years = {}
    for s in entries:
        years.setdefault(str(s['year']), []).append(s)
    year_keys = sorted(years.keys(), reverse=reverse) if reverse else list(years.keys())
    blocks = []
    for yr in year_keys:
        rows = ''.join(entry(s) for s in years[yr])
        blocks.append(
            f'<div class="thesis-year-block">'
            f'<div class="thesis-year-label">{yr}</div>'
            f'{rows}'
            f'</div>')
    return (f'<div class="thesis-section">'
            f'<h2><i class="fa-solid {icon}"></i>{name}</h2>'
            f'<span class="count">{len(entries)} {count_suffix}</span>'
            f'</div>{"".join(blocks)}')

intro = ' '.join(data['intro']['en'].split())

body = (
    f'<p class="supervision-intro">{intro}</p>'
    f'{section("Doctoral theses", "fa-user-graduate", phd, reverse=False, count_suffix="thesis" if len(phd)==1 else "theses")}'
    f'{section("Master&#39;s dissertations", "fa-graduation-cap", masters, reverse=True, count_suffix="dissertations")}'
    f'{section("Honors essays", "fa-scroll", honors, reverse=True, count_suffix="essays")}'
)

CSS = r"""
:root {
  --global-theme-color: #3665b8;
  --global-hover-color: #5a86d0;
  --global-text-color: #1c1c1c;
  --global-text-color-light: #666;
  --global-divider-color: #e8e8e8;
  --global-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
}
* { box-sizing: border-box; }
body {
  font-family: var(--global-font-family);
  color: var(--global-text-color);
  max-width: 62rem;
  margin: 3rem auto;
  padding: 0 2rem;
  line-height: 1.55;
  font-size: 15px;
}
.supervision-intro {
  font-size: 1rem; line-height: 1.65;
  color: var(--global-text-color); margin-bottom: 2rem; max-width: 62rem;
}
.thesis-section {
  display: flex; align-items: baseline; justify-content: space-between;
  border-bottom: 2px solid var(--global-divider-color);
  padding-bottom: 0.4rem; margin-top: 2.75rem; margin-bottom: 1.4rem;
}
.thesis-section h2 {
  margin: 0; font-size: 1.35rem; font-weight: 600;
  color: var(--global-theme-color);
}
.thesis-section h2 i { margin-right: 0.5rem; opacity: 0.85; }
.thesis-section .count {
  font-size: 0.85rem; font-weight: 400;
  color: var(--global-text-color-light); letter-spacing: 0.02em;
}
.thesis-year-block { margin-bottom: 1.35rem; }
.thesis-year-label {
  font-weight: 600; color: var(--global-hover-color);
  font-size: 0.92rem; letter-spacing: 0.03em;
  margin-bottom: 0.5rem; padding-left: 0.55rem;
  border-left: 3px solid var(--global-theme-color);
}
.thesis-row {
  display: grid; grid-template-columns: 2.2rem 3rem 1fr; gap: 0.75rem;
  align-items: start;
  padding: 0.7rem 0.5rem 0.7rem 0.6rem;
  border-bottom: 1px solid var(--global-divider-color);
  transition: background-color 0.15s ease;
}
.thesis-row:hover { background-color: rgba(0,0,0,0.02); }
.thesis-row:last-child { border-bottom: none; }
.thesis-avatar {
  width: 2.1rem; height: 2.1rem; border-radius: 50%;
  background: linear-gradient(135deg, var(--global-theme-color), var(--global-hover-color));
  color: #fff; display: flex; align-items: center; justify-content: center;
  font-size: 0.66rem; font-weight: 700; letter-spacing: 0.04em;
  overflow: hidden; flex-shrink: 0; margin-top: 0.05rem; user-select: none;
}
.thesis-avatar img { width: 100%; height: 100%; object-fit: cover; }
.thesis-badge {
  display: inline-block; font-size: 0.66rem; letter-spacing: 0.09em;
  text-transform: uppercase; font-weight: 700;
  padding: 3px 7px; border-radius: 3px;
  align-self: start; text-align: center; margin-top: 0.28rem;
}
.thesis-badge.phd { background: rgba(52, 91, 168, 0.13); color: #345bb0; }
.thesis-badge.masters { background: rgba(30, 120, 90, 0.13); color: #1e785a; }
.thesis-badge.honors { background: rgba(180, 100, 40, 0.15); color: #a05820; }
.thesis-name {
  font-size: 0.98rem; font-weight: 600;
  color: var(--global-text-color); margin-bottom: 0.15rem;
}
.thesis-name-link { color: inherit; text-decoration: none; transition: color 0.15s; }
.thesis-name-link:hover { color: var(--global-theme-color); }
.thesis-name-link .fa-arrow-up-right-from-square {
  font-size: 0.6em; margin-left: 0.35rem; opacity: 0.55; vertical-align: 0.1em;
}
.thesis-title {
  font-size: 0.94rem; font-style: italic;
  color: var(--global-text-color); line-height: 1.5; margin-bottom: 0.3rem;
}
.thesis-title.pending {
  font-style: normal; color: var(--global-text-color-light);
  font-size: 0.88rem; opacity: 0.75;
}
.thesis-summary {
  font-size: 0.88rem; color: var(--global-text-color-light);
  line-height: 1.55; margin-bottom: 0.15rem;
}
.thesis-ongoing-badge {
  display: inline-block; font-size: 0.63rem; letter-spacing: 0.14em;
  text-transform: uppercase; font-weight: 700;
  color: #a05820; background: rgba(180, 100, 40, 0.13);
  padding: 2px 7px; border-radius: 3px; margin-left: 0.5rem;
  vertical-align: 0.12rem; font-style: normal;
}
"""

html = (f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
        f'<title>Supervision — preview</title>'
        f'<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">'
        f'<style>{CSS}</style></head><body>{body}</body></html>')

out = Path(tempfile.gettempdir()) / 'supervision-preview.html'
out.write_text(html, encoding='utf-8')
print(f'wrote: {out}')
webbrowser.open(f'file:///{out.as_posix()}')
