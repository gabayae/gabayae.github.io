#!/usr/bin/env bash
set -u
cd "$(dirname "$0")/.." || exit 1
REPO_ROOT=$(pwd)

build_one() {
  local dir="$1"
  cd "$REPO_ROOT/$dir" || return 1
  xelatex -shell-escape -interaction=nonstopmode notes.tex > /dev/null 2>&1
  xelatex -shell-escape -interaction=nonstopmode notes.tex > /dev/null 2>&1
  local rc=$?
  local pages=$(grep -oE "Output written on [^ ]+\.pdf \([0-9]+ pages" "notes.log" 2>/dev/null | tail -1 | grep -oE "[0-9]+ pages")
  local err=$(grep -c "^! " "notes.log" 2>/dev/null)
  echo "[$dir] $pages (rc=$rc, errors=$err)"
}
export -f build_one
export REPO_ROOT

JOBS=(
  "courses/analyse-donnees-sante/en"
  "courses/analyse-numerique/en"
  "courses/apprentissage-automatique/en"
  "courses/apprentissage-geometrique/en"
  "courses/apprentissage-profond/en"
  "courses/bases-donnees/en"
  "courses/edp/en"
  "courses/finance-quantitative/en"
  "courses/geometrie-riemannienne/en"
  "courses/ia-generative/en"
  "courses/intro-data-science/en"
  "courses/mesure-integration/en"
  "courses/mlops/en"
  "courses/modelisation/en"
  "courses/optimisation-convexe/en"
  "courses/points-fixes/en"
  "courses/pretraitement-donnees/en"
  "courses/probabilites/en"
  "courses/processus-stochastiques/en"
  "courses/programmation-julia/en"
  "courses/programmation-scientifiques/en"
  "courses/recherche-operationnelle/en"
  "courses/series-temporelles/en"
  "courses/statistique/en"
  "courses/systemes-dynamiques/en"
)

echo "Total: ${#JOBS[@]}"
PARALLEL=4
RUNNING=0
for job in "${JOBS[@]}"; do
  build_one "$job" &
  RUNNING=$((RUNNING + 1))
  if [ $RUNNING -ge $PARALLEL ]; then
    wait -n
    RUNNING=$((RUNNING - 1))
  fi
done
wait
echo "Done."
