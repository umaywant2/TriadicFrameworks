import pandas as pd
from pathlib import Path

# Load logs
score_log = Path("badge_trigger_resonance_score.md").read_text()
echo_log = Path("badge_trigger_echo_log.md").read_text()
validator_log = Path("badge_trigger_validator_log.md").read_text()

# Parse logs (placeholder logic)
def extract_scores(log):
    # Replace with real parsing logic
    return pd.DataFrame([
        {"Title": "Triadic Framework for Spectrum Technologies", "Theme": "Elemental & Spectrum", "Score": 9, "Echoed": True, "Validated": True, "Contributor": "Nawder Loswin"},
        {"Title": "Triadic Number Genesis (1–9)", "Theme": "Cognitive & Symbolic", "Score": 9, "Echoed": True, "Validated": True, "Contributor": "Nawder Loswin"},
        {"Title": "Triadic Framework for Music – Quadratic Extensions", "Theme": "Music & Symbolic Extensions", "Score": 9, "Echoed": True, "Validated": True, "Contributor": "Nawder Loswin"},
        {"Title": "Ghost Particle & Triadic Resonance Vision", "Theme": "Quantum & Particle Vision", "Score": 6, "Echoed": True, "Validated": False, "Contributor": "Nawder Loswin"},
        {"Title": "Saturn’s Harmonic Engine", "Theme": "Planetary & Temporal Mapping", "Score": 3, "Echoed": False, "Validated": False, "Contributor": "Nawder Loswin"},
    ])

# Generate leaderboard
df = extract_scores(score_log)
df_sorted = df.sort_values(by="Score", ascending=False)

# Output markdown
leaderboard_md = "# 🏆 Badge Trigger Resonance Leaderboard\n"
leaderboard_md += "| Rank | Paper Title | Theme | Score | Echoed | Validated | Contributor |\n"
leaderboard_md += "|------|-------------|-------|-------|--------|-----------|-------------|\n"
for i, row in df_sorted.iterrows():
    leaderboard_md += f"| {i+1} | {row['Title']} | {row['Theme']} | {row['Score']} | {'✅' if row['Echoed'] else '⏳'} | {'✅' if row['Validated'] else '❌'} | {row['Contributor']} |\n"

Path("badge_trigger_resonance_leaderboard.md").write_text(leaderboard_md)
print("Leaderboard updated.")
