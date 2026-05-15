#!/usr/bin/env bash
# Build every FR cours.tex and EN notes.tex twice (for ToC accuracy).
# Runs up to 4 builds in parallel.
set -u
cd "$(dirname "$0")/.." || exit 1
REPO_ROOT=$(pwd)

build_one() {
  local dir="$1" master="$2"
  cd "$REPO_ROOT/$dir" || return 1
  xelatex -shell-escape -interaction=nonstopmode "$master" > /dev/null 2>&1
  xelatex -shell-escape -interaction=nonstopmode "$master" > /dev/null 2>&1
  local rc=$?
  local pages=$(grep -oE "Output written on [^ ]+\.pdf \([0-9]+ pages" "${master%.tex}.log" | tail -1 | grep -oE "[0-9]+ pages")
  echo "[$dir] $pages (rc=$rc)"
}

export -f build_one
export REPO_ROOT

# Collect all jobs
JOBS=()
while IFS= read -r master; do
  dir=$(dirname "$master")
  base=$(basename "$master")
  JOBS+=("$dir|$base")
done < <(find courses -maxdepth 3 \( -name "cours.tex" -o -name "notes.tex" \) | sort)

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
