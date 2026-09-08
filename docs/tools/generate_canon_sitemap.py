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
