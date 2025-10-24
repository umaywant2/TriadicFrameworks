"""
Idiom Validator Logic
---------------------
Takes idioms + their mapped triads (Freqi, Flui, Forci) and produces
an alignment score based on how well the mapping fits mythmatical rules.
"""

import math

def validate_idiom(idiom_entry):
    """
    idiom_entry = {
        "idiom": "Grace under pressure",
        "forci": "...",
        "flui": "...",
        "freqi": "...",
        "interpretation": "...",
    }
    """

    # Step 1: Check presence of triads
    triad_hits = sum(1 for k in ["forci", "flui", "freqi"] if idiom_entry.get(k))

    # Step 2: Assign base score for completeness
    score = triad_hits / 3.0

    # Step 3: Boost if idiom implies balance/harmony (Freqi resonance)
    if "grace" in idiom_entry["idiom"].lower() or "harmony" in idiom_entry.get("freqi", "").lower():
        score += 0.1

    # Step 4: Boost if idiom implies compression/flow (Forci + Flui interaction)
    if "pressure" in idiom_entry["idiom"].lower() or "flow" in idiom_entry.get("flui", "").lower():
        score += 0.1

    # Step 5: Clamp score between 0 and 1
    score = min(1.0, round(score, 2))

    return score

# Example usage
idioms = [
    {
        "idiom": "Grace under pressure",
        "forci": "applied force",
        "flui": "distributed medium",
        "freqi": "harmonic resonance (grace)",
        "interpretation": "Freqi maintains clarity even when Forci + Flui compress the lattice"
    },
    {
        "idiom": "Strength in numbers",
        "forci": "collective force",
        "flui": "distributed network of agents",
        "freqi": "synchronized rhythm of group action",
        "interpretation": "Forci amplified by Flui, stabilized by Freqi alignment"
    }
]

for entry in idioms:
    print(entry["idiom"], "->", validate_idiom(entry))
