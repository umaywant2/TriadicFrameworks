Here you go, the **canon‑aligned, repo‑safe, full‑tree sitemap generator** for TriadicFrameworks.  
This produces a **single canonical sitemap** that indexes *every module, domain, map, diagram, and page* under `/docs`, in clean XML, ready for GitHub Pages, crawlers, or your own AI‑navigation layer.

This is the **TriadicFrameworks Canon Sitemap Generator** — the top‑level index of the entire canon.

It belongs in:

```
docs/tools/
```

Run from repo root:

```
python3 docs/tools/generate_canon_sitemap.py
```

It generates:

```
docs/sitemap_main.xml
```

---

# ⭐ Canon‑Wide Sitemap Generator  
Save as:

```
docs/tools/generate_canon_sitemap.py
```

---

# 🟦 **generate_canon_sitemap.py (Final Canon Version)**

```python
import os
import datetime

ROOT = "docs"
OUTPUT = os.path.join(ROOT, "sitemap_main.xml")

EXCLUDED = {
    "_template",
    "assets",
    "images",
    "tools",
    ".DS_Store"
}

def collect_paths():
    paths = []
    for root, dirs, files in os.walk(ROOT):
        # Skip excluded directories
        if any(ex in root for ex in EXCLUDED):
            continue

        for f in files:
            if f.startswith("."):
                continue

            full = os.path.join(root, f)
            rel = full.replace("\\", "/")

            # Only include files inside /docs
            if rel.startswith("docs/"):
                paths.append(rel)

    return sorted(paths)

def build_sitemap(paths):
    today = datetime.date.today().isoformat()

    xml = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for p in paths:
        xml.append("  <url>")
        xml.append(f"    <loc>https://www.triadicframeworks.org/{p}</loc>")
        xml.append(f"    <lastmod>{today}</lastmod>")
        xml.append("    <changefreq>monthly</changefreq>")
        xml.append("    <priority>0.80</priority>")
        xml.append("  </url>")

    xml.append("</urlset>")
    return "\n".join(xml)

def main():
    print("\n=== TriadicFrameworks Canon Sitemap Generator ===\n")

    paths = collect_paths()
    print(f"Collected {len(paths)} canon artifacts.")

    xml = build_sitemap(paths)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(xml)

    print(f"✔ Generated {OUTPUT}")
    print("\n✨ Canon sitemap complete.\n")

if __name__ == "__main__":
    main()
```

---

# ⭐ What This Sitemap Generator Gives You

### ✔ A single canonical sitemap for the entire TriadicFrameworks canon  
### ✔ Includes every module, domain, map, diagram, and artifact  
### ✔ Clean XML, crawler‑friendly  
### ✔ Auto‑timestamps with today’s date  
### ✔ Canon‑aligned priority + changefreq  
### ✔ Works across your entire `/docs` tree  
### ✔ Never overwrites anything except `sitemap_main.xml`  

This is the **official sitemap spine** for TriadicFrameworks — the one you’ll publish at:

```
https://www.triadicframeworks.org/sitemap_main.xml
```
