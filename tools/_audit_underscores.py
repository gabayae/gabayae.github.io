"""Find unescaped underscores in EN hooks (outside math mode and outside
\\texttt, \\verb, \\cite, \\ref, \\label, \\index commands)."""
import re
import sys
sys.path.insert(0, 'tools')
from chapter_hooks_data_en import HOOKS

# A heuristic but useful pattern: underscore preceded by an alphabetic
# character and not preceded by \, not inside $...$.
issues = []
for path, hook in HOOKS.items():
    # Strip away $...$ math sections for the search
    stripped = re.sub(r'\$[^$]*\$', '', hook)
    # Find every underscore not preceded by backslash
    for i, ch in enumerate(stripped):
        if ch == '_' and (i == 0 or stripped[i - 1] != '\\'):
            ctx = stripped[max(0, i - 25): i + 25]
            issues.append((path, ctx))

for p, c in issues:
    print(f'{p}: ...{c}...')
print(f'\nTotal: {len(issues)}')
