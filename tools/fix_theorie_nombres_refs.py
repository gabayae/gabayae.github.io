#!/usr/bin/env python3
"""One-off: remove the stray backslash-r that the Edit tool round-trip left
in front of \\ref{cor:gauss:premier_divise_produit} in
theorie-nombres/fr/cours.tex.
"""
import pathlib

p = pathlib.Path(__file__).resolve().parents[1] / "courses" / "theorie-nombres" / "fr" / "cours.tex"
data = p.read_bytes()

# Backslash byte
BS = bytes([0x5C])
# The corruption is: Le~ + BS + r + BS + r + e + f + { + cor:...
target = b"Le~" + BS + b"r" + BS + b"ref{cor:gauss:premier_divise_produit}"
replacement = b"Le~" + BS + b"ref{cor:gauss:premier_divise_produit}"

n = data.count(target)
print(f"Target occurrences: {n}")
if n:
    data = data.replace(target, replacement)
    p.write_bytes(data)
    print(f"Wrote {p.stat().st_size} bytes")
else:
    # Hex search to debug
    import re
    pos = data.find(b"Le~")
    while pos >= 0:
        print(f"  Le~ at {pos}: {data[pos:pos+30].hex()}")
        pos = data.find(b"Le~", pos + 1)
