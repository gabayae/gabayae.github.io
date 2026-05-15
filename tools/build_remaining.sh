#!/usr/bin/env bash
# Build only the 27 masters not built in the previous round.
set -u
cd "$(dirname "$0")/.." || exit 1
REPO_ROOT=$(pwd)

build_one() {
  local dir="$1" master="$2"
  cd "$REPO_ROOT/$dir" || return 1
  xelatex -shell-escape -interaction=nonstopmode "$master" > /dev/null 2>&1
  xelatex -shell-escape -interaction=nonstopmode "$master" > /dev/null 2>&1
  local rc=$?
  local pages=$(grep -oE "Output written on [^ ]+\.pdf \([0-9]+ pages" "${master%.tex}.log" 2>/dev/null | tail -1 | grep -oE "[0-9]+ pages")
  echo "[$dir/$master] $pages (rc=$rc)"
}

export -f build_one
export REPO_ROOT

JOBS=(
  "assets/pdf|cv_gaba.tex"
  "courses/algebre-abstraite/I/en|notes.tex"
  "courses/algebre-abstraite/I/fr|cours.tex"
  "courses/algebre-abstraite/II/en|notes.tex"
  "courses/algebre-abstraite/II/fr|cours.tex"
  "courses/analyse-reelle/I/en|notes.tex"
  "courses/analyse-reelle/I/fr|cours.tex"
  "courses/analyse-reelle/II/en|notes.tex"
  "courses/analyse-reelle/II/fr|cours.tex"
  "courses/LinearAlgebra/linear-algebra/en|notes.tex"
  "courses/LinearAlgebra/linear-algebra/fr|cours.tex"
  "courses/theorie-categories/en|chunk1.tex"
  "courses/theorie-categories/fr|chunk1.tex"
  "courses/analyse-donnees-sante/modules/slides|module_01_slides.tex"
  "courses/analyse-donnees-sante/modules/slides|module_02_slides.tex"
  "courses/analyse-donnees-sante/modules/slides|module_03_slides.tex"
  "courses/analyse-donnees-sante/modules/slides|module_04_slides.tex"
  "courses/analyse-donnees-sante/modules/slides|module_05_slides.tex"
  "courses/analyse-donnees-sante/modules/slides|module_06_slides.tex"
  "courses/analyse-donnees-sante/modules/slides|module_07_slides.tex"
  "courses/analyse-donnees-sante/modules/slides|module_08_slides.tex"
  "courses/analyse-donnees-sante/modules/slides|module_09_slides.tex"
  "courses/analyse-donnees-sante/modules/slides|module_10_slides.tex"
  "workshops/scientific-writing/templates|beamer_slides.tex"
  "workshops/scientific-writing/templates|first_document.tex"
  "workshops/scientific-writing/templates|math_paper_template.tex"
  "workshops/scientific-writing/templates|thesis_template.tex"
)

echo "Total masters: ${#JOBS[@]}"
PARALLEL=4
RUNNING=0
for job in "${JOBS[@]}"; do
  dir="${job%|*}"
  base="${job#*|}"
  build_one "$dir" "$base" &
  RUNNING=$((RUNNING + 1))
  if [ $RUNNING -ge $PARALLEL ]; then
    wait -n
    RUNNING=$((RUNNING - 1))
  fi
done
wait
echo "Done."
