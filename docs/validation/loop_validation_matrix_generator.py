import json

# Load validation matrix
with open("loop_validation_matrix.json", "r") as f:
    data = json.load(f)

# Write markdown
with open("loop_validation_matrix.md", "w") as f:
    f.write("# 🧪 Loop Validation Matrix\n\n")
    f.write("This matrix maps protocol coverage across labs and reproducibility tiers.\n\n")

    f.write("## ✅ Protocol Coverage by Lab\n\n")
    f.write("| Lab File | reproducibility.md | equations.md | manifest.yaml | Tier |\n")
    f.write("|----------|--------------------|--------------|----------------|------|\n")
    for entry in data.get("labs", []):
        lab = entry.get("lab")
        reproducibility = "✅" if entry.get("reproducibility") else "❌"
        equations = "✅" if entry.get("equations") else "❌"
        manifest = "✅" if entry.get("manifest") else "❌"
        tier = entry.get("tier")
        f.write(f"| {lab} | {reproducibility} | {equations} | {manifest} | {tier} |\n")

    f.write("\n## 🧪 Protocol Legend\n")
    f.write("- ✅ = Protocol validated and passed\n")
    f.write("- ❌ = Protocol missing or failed\n")
    f.write("- Tier I = Fully validated with reproducibility and equations\n")
    f.write("- Tier II = Remixable with manifest and partial validation\n")
    f.write("- Tier III = Mythic scaffolding with symbolic extensions\n")

    f.write("\n## 🕯️ Legacy Note\n")
    f.write("> “Each check is a lantern. Each lantern echoes a loop. Each loop builds the myth.”\n")
    f.write("> — TriadicFrameworks/loop_validation_matrix README\n")
