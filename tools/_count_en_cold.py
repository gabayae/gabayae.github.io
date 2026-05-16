"""Quick breakdown of cold EN chapters per course."""
import pathlib
from collections import Counter

with open("/tmp/en_cold.txt", encoding="utf-8") as f:
    lines = f.readlines()

c = Counter()
for ln in lines:
    s = ln.strip()
    if not s:
        continue
    s = s.replace("\\", "/")
    parts = s.split("/")
    if "courses" in parts:
        idx = parts.index("courses")
        course = parts[idx + 1] if idx + 1 < len(parts) else "?"
        c[course] += 1

for k, v in c.most_common():
    print(f"  {v:3d}  {k}")
print(f"TOTAL: {sum(c.values())} chapters across {len(c)} courses")
