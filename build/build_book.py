#!/usr/bin/env python3
"""BLACKBOOK UNDERCOVER — Book Compiler.

Fuehrt die modularen Kapitel aus chapters/ (numerisch sortiert) zu EINER Markdown-Datei
zusammen (dist/compiled_book.md), mit Seitenumbruch zwischen den Kapiteln (LaTeX \\newpage).
Liest metadata.json, prueft dass Kapitel vorhanden sind, und schreibt eine Build-Summary.

Aufruf:  python build/build_book.py
"""

from __future__ import annotations

import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HIER)
CHAPTERS = os.path.join(ROOT, "chapters")
META = os.path.join(ROOT, "metadata.json")
DIST = os.path.join(ROOT, "dist")
OUT = os.path.join(DIST, "compiled_book.md")


def compile_book() -> str:
    os.makedirs(DIST, exist_ok=True)
    with open(META, encoding="utf-8") as f:
        meta = json.load(f)

    kapitel = sorted(f for f in os.listdir(CHAPTERS) if f.endswith(".md"))
    if not kapitel:
        print("FEHLER: keine Kapitel in chapters/ gefunden.", file=sys.stderr)
        sys.exit(1)

    print(f"Kompiliere: {meta['title']} v{meta.get('version', '?')} — {len(kapitel)} Kapitel")

    teile: list[str] = []
    for i, name in enumerate(kapitel):
        with open(os.path.join(CHAPTERS, name), encoding="utf-8") as cf:
            teile.append(cf.read().strip())
        print(f"  + {name}")
        if i < len(kapitel) - 1:
            teile.append('\n\n```{=latex}\n\\newpage\n```\n\n')  # Seitenumbruch nur im PDF

    with open(OUT, "w", encoding="utf-8") as out:
        out.write("\n\n".join(teile) + "\n")

    kb = os.path.getsize(OUT) // 1024
    print(f"\nOK -> {os.path.relpath(OUT, ROOT)} ({kb} KB, {len(kapitel)} Kapitel)")
    return OUT


if __name__ == "__main__":
    compile_book()
