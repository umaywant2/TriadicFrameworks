import pandas as pd
import json

# Load filtered glyphmap index
def load_filtered_data(path="badge_trigger_glyphmap_index_filtered.json"):
    with open(path, "r") as f:
        return pd.DataFrame(json.load(f))

# Badge trigger logic
def trigger_badge(row):
    glyph = row["Glyph"]
    theme = row["Theme"]
    title = row["Paper Title"]
    validated = row["Validated"]

    if validated:
        badge_id = f"{glyph}_{theme.replace(' ', '_')}"
        print(f"✅ Badge triggered for: {title}")
        print(f"🔖 Badge ID: {badge_id}")
        return {
            "title": title,
            "badge_id": badge_id,
            "theme": theme,
            "glyph": glyph,
            "status": "Issued"
        }
    else:
        print(f"⚠️ Skipped (not validated): {title}")
        return {
            "title": title,
            "badge_id": None,
            "theme": theme,
            "glyph": glyph,
            "status": "Skipped"
        }

# Main trigger loop
def main():
    df = load_filtered_data()
    results = [trigger_badge(row) for _, row in df.iterrows()]

    with open("badge_trigger_glyphmap_index_trigger_log.json", "w") as f:
        json.dump(results, f, indent=2)

    print("🎉 Badge trigger log saved to badge_trigger_glyphmap_index_trigger_log.json")

if __name__ == "__main__":
    main()
