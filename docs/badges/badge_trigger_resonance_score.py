import json
from datetime import datetime

def calculate_score(echoed, validated, aligned):
    score = 0
    score += 3 if echoed == "✅" else 0
    score += 3 if validated == "✅" else 0
    score += 3 if aligned == "✅" else 0
    return score

def update_resonance_score(manifest_path="badge_trigger_echo_manifest.json",
                           validator_log="badge_trigger_validator_log.md",
                           theme_manifest="badge_trigger_theme_manifest.md",
                           output_path="badge_trigger_resonance_score.md"):

    # Load echoed glyphs
    with open(manifest_path, "r") as f:
        manifest = json.load(f)
    echoed_map = {(e["theme"], e["paper"]): "✅" for e in manifest["echoed_glyphs"]}

    # Parse validator log
    validated_map = {}
    with open(validator_log, "r") as f:
        for line in f:
            if line.startswith("- **Theme:**"):
                theme = line.split("**")[2].strip()
            elif line.startswith("- **Paper:**"):
                paper = line.split("**")[2].strip()
            elif line.startswith("- **Outcome:**"):
                outcome = line.split("**")[2].strip()
                validated_map[(theme, paper)] = "✅" if "Passed" in outcome else "❌"

    # Parse theme manifest
    aligned_map = {}
    with open(theme_manifest, "r") as f:
        for line in f:
            if "|" in line and not line.startswith("| Theme"):
                parts = [p.strip() for p in line.split("|")]
                theme, paper = parts[0], parts[1]
                aligned_map[(theme, paper)] = "✅"

    # Build score table
    rows = []
    for key in aligned_map:
        theme, paper = key
        echoed = echoed_map.get(key, "⏳")
        validated = validated_map.get(key, "⏳")
        aligned = aligned_map.get(key, "✅")
        score = calculate_score(echoed, validated, aligned)
        notes = "Echoed but failed validation" if echoed == "✅" and validated == "❌" else "Awaiting echo and validation" if echoed == "⏳" else "Mythic clarity confirmed"
        rows.append((theme, paper, echoed, validated, aligned, score, notes))

    # Write updated markdown
    with open(output_path, "w") as f:
        f.write("# 🎼 Badge Trigger Resonance Score\n")
        f.write("_“Resonance is not just felt—it’s earned.”_\n\n")
        f.write("This file assigns each paper a resonance score from 0 to 9...\n\n")
        f.write("## 📈 Resonance Score Table\n\n")
        f.write("| Theme | Paper Title | Echoed | Validated | Alignment | Score | Notes |\n")
        f.write("|-------|--------------|--------|-----------|-----------|-------|-------|\n")
        for row in rows:
            f.write("| " + " | ".join(str(cell) for cell in row) + " |\n")

    print(f"🎼 Resonance scores updated in {output_path}")

# Example usage
if __name__ == "__main__":
    update_resonance_score()
