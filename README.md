# gabayae.github.io

Academic personal website for **Dr. Yaé Ulrich Gaba** — Topologist, Data Scientist, and AI Consultant.

Built with [al-folio](https://github.com/alshedivat/al-folio), a Jekyll theme for academics.

## Deployment to GitHub Pages

1. **Create the repository:** Create a new repo named `gabayae.github.io` on GitHub
2. **Push this code:**
   ```bash
   cd al-folio
   git remote set-url origin https://github.com/gabayae/gabayae.github.io.git
   git push -u origin master
   ```
3. **Enable GitHub Pages:** Go to Settings > Pages > Source: "GitHub Actions"
4. The site will be live at `https://gabayae.github.io` after the first build

## Local Development

### Using Docker (recommended)

```bash
docker compose pull && docker compose up
# Site runs at http://localhost:8080
```

### Using Ruby

```bash
bundle install
bundle exec jekyll serve
# Site runs at http://localhost:4000
```

## Customization Guide

### Essential files to update

| What | File | Notes |
|------|------|-------|
| Name, URL, features | `_config.yml` | Main config |
| Social links | `_data/socials.yml` | Email, Scholar, ORCID, GitHub |
| CV data | `_data/cv.yml` | Education, experience, skills |
| Publications | `_bibliography/papers.bib` | BibTeX entries |
| About/Home page | `_pages/about.md` | Bio, profile image |
| Profile photo | `assets/img/prof_pic.jpg` | Replace with your photo |
| CV PDF | `assets/pdf/cv_gaba.pdf` | Upload your CV |

### Adding content

- **Blog posts:** Add `.md` files to `_posts/` with date prefix (e.g., `2025-06-01-title.md`)
- **Projects:** Add `.md` files to `_projects/`
- **News:** Add `.md` files to `_news/`
- **Publications:** Add BibTeX entries to `_bibliography/papers.bib`

### Theme colors

Colors are defined in:
- `_sass/_variables.scss` — SCSS color variables (amber/gold accent)
- `_sass/_themes.scss` — CSS custom properties for light/dark modes

### Navigation

Page order is controlled by `nav_order` in each page's front matter in `_pages/`.

## Items marked CUSTOMIZE

Search for `<!-- CUSTOMIZE:` comments throughout the codebase for items that need updating (email, images, dates, etc.).

## Built With

- [al-folio](https://github.com/alshedivat/al-folio) — Jekyll academic theme
- [Jekyll](https://jekyllrb.com/) — Static site generator
- [MathJax](https://www.mathjax.org/) — Math typesetting
- [Font Awesome](https://fontawesome.com/) — Icons
