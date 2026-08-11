#!/usr/bin/env python3
"""
patch_spine_index.py — Clarity Overlay wiring for docs/spine/index.html
Run from the root of your TriadicFrameworks repo: python3 patch_spine_index.py
"""
import sys, shutil
from pathlib import Path

TARGET = Path("docs/spine/index.html")
BACKUP = Path("docs/spine/index.html.bak")

def replace_once(html, old, new):
    return html.replace(old, new, 1), html.count(old)

def patch(html):
    changes = []

    # 1. A3 Modules 196→197
    old = '<div class="val">196</div><div class="lbl">A3 Modules</div>'
    html, n = replace_once(html, old, old.replace(">196<", ">197<")); changes.append(("A3 Modules 196→197", n))

    # 2. Files 1,450→1,454
    old = '<div class="val">1,450</div><div class="lbl">Files</div>'
    html, n = replace_once(html, old, old.replace(">1,450<", ">1,454<")); changes.append(("Files 1,450→1,454", n))

    # 3. Hierarchy Edges 195→196
    old = '<div class="val">195</div><div class="lbl">Hierarchy Edges</div>'
    html, n = replace_once(html, old, old.replace(">195<", ">196<")); changes.append(("Hierarchy Edges 195→196", n))

    # 4. Directed Edges 65→72
    old = '<div class="val">65</div><div class="lbl">Directed Edges</div>'
    html, n = replace_once(html, old, old.replace(">65<", ">72<")); changes.append(("Directed Edges 65→72", n))

    # 5. R5 New 30→31
    old = '<div class="val">30</div><div class="lbl">R5 New</div>'
    html, n = replace_once(html, old, old.replace(">30<", ">31<")); changes.append(("R5 New 30→31", n))

    # 6. Version 6.0→6.1
    old = '<td>6.0 (R5-stable)</td>'
    html, n = replace_once(html, old, '<td>6.1 (R5-clarity)</td>'); changes.append(("Version 6.0→6.1", n))

    # 7. Coherence six→seven-overlay
    old = '<td>stable · six-overlay</td>'
    html, n = replace_once(html, old, '<td>stable · seven-overlay</td>'); changes.append(("Coherence →seven-overlay", n))

    # 8. Generated date
    old = '<td>2026-08-03</td>'
    html, n = replace_once(html, old, '<td>2026-08-08</td>'); changes.append(("Generated date →08-08", n))

    # 9. CSS: add .link.gates
    old = '  .link.contains-ref{stroke:#555;stroke-dasharray:2,4;}'
    new = old + '\n  .link.gates{stroke:#10b981;stroke-width:2;stroke-dasharray:4,3;}'
    html, n = replace_once(html, old, new); changes.append(("CSS .link.gates added", n))

    # 10. Sidebar: add ⑦ Clarity
    old = ('    <div>④ Substrate · ⑤ Dimensional · ⑥ Domain</div>\n'
           '    <div style="color:#1abc9c;margin-top:4px;">')
    new = ('    <div>④ Substrate · ⑤ Dimensional · ⑥ Domain</div>\n'
           '    <div style="color:#00d4ff;">⑦ Clarity <span style="font-size:9px;opacity:.7;">'
           '· RTT::Clarity v2 · R5</span></div>\n'
           '    <div style="color:#1abc9c;margin-top:4px;">')
    html, n = replace_once(html, old, new); changes.append(("Sidebar ⑦ Clarity", n))

    # 11. Append spine-clarity node before closing of nodes[]
    old = '  ],\n  "links":'
    new = ''',
    {
      "id": "spine-clarity",
      "label": "Clarity Overlay",
      "name": "Clarity Overlay",
      "layer": "Core Frameworks \u2014 Structural Spine",
      "depth": 2,
      "parent": "spine-overlay-pack",
      "color": "#1abc9c",
      "size": 18,
      "status": "Active Canonical",
      "namespace": "RTT::Clarity",
      "version": "2.0",
      "round": "R5",
      "enriched_r5": true,
      "url": "https://www.triadicframeworks.org/spine/clarity/",
      "file_count": 4
    }
  ],
  "links":'''
    html, n = replace_once(html, old, new); changes.append(("Node spine-clarity appended", n))

    # 12. Append 7 edges before closing of links[]
    old = '  ]\n};\n'
    new = '''  ,
    {"source":"spine-structural","target":"spine-clarity","type":"feeds"},
    {"source":"spine-drift","target":"spine-clarity","type":"feeds"},
    {"source":"spine-coherence","target":"spine-clarity","type":"feeds"},
    {"source":"spine-substrate","target":"spine-clarity","type":"feeds"},
    {"source":"spine-dimensional","target":"spine-clarity","type":"feeds"},
    {"source":"spine-domain","target":"spine-clarity","type":"feeds"},
    {"source":"spine-clarity","target":"spine-coherence","type":"gates"}
  ]
};
'''
    html, n = replace_once(html, old, new); changes.append(("7 edges appended", n))

    print("\n  patch_spine_index.py — Clarity Overlay R5")
    print("  " + "─"*44)
    ok = True
    for label, count in changes:
        mark = "✓" if count == 1 else ("⚠ SKIPPED" if count == 0 else "✗ MULTI")
        if count != 1: ok = False
        print(f"  {mark}  {label}")
    print(f"\n  {'All 12 patches applied cleanly.' if ok else 'WARNING: review skipped items.'}")
    return html

def main():
    if not TARGET.exists():
        print(f"ERROR: {TARGET} not found. Run from repo root."); sys.exit(1)
    html = TARGET.read_text(encoding="utf-8")
    shutil.copy2(TARGET, BACKUP)
    TARGET.write_text(patch(html), encoding="utf-8")
    print(f"  Written to {TARGET}\n")

if __name__ == "__main__":
    main()
