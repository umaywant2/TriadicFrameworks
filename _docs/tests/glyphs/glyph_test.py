# glyph_test.py — TriadicFrameworks Glyph Assignment Test Harness

import json

GLYPH_RULES = {
    "classical": "◻",
    "diffusion": "◯",
    "quantum": "◆"
}

PHASE_RULES = {
    "emergence": "↑",
    "stabilization": "→",
    "resonance": "✦",
    "collapse": "↓"
}

DRIFT_RULES = {
    "none": "",
    "minor": "~",
    "major": "!"
}

def assign_glyph(substrate, phase, drift):
    return GLYPH_RULES[substrate] + PHASE_RULES[phase] + DRIFT_RULES[drift]

def test_case(case):
    expected = case["expected"]
    actual = assign_glyph(case["substrate"], case["phase"], case["drift"])
    return actual == expected

if __name__ == "__main__":
    with open("cases.json") as f:
        cases = json.load(f)
    results = {c["name"]: test_case(c) for c in cases}
    print(json.dumps(results, indent=2))
