Here’s your **triad‑purity SVG heatmap** generator, tuned to your existing canon tooling and safe to paste into GitHub.

Save as:

```text
docs/tools/generate_triad_purity_heatmap.py
```

Run from repo root:

```bash
python3 docs/tools/generate_triad_purity_heatmap.py
```

---

```python
import os
import json

ROOT = "docs"
EXCLUDED = {"spine","_template","assets","images","tools"}

# We treat "triad‑pure" structurally as:
# - triads.structural_triads present and valid
# - triads.harmonic_triads present and valid
# - triads.coherence_triads present and valid

STRUCTURAL_KEYS = {
    "generative": ["resonance_source","structural_seed","temporal_onset"],
    "transformational": ["resonant_input","structural_transformation","temporal_modulation"],
    "coherence": ["resonant_field","structural_alignment","temporal_continuity"],
}

HARMONIC_KEYS = {
    "resonance_harmonic": ["resonant_mode","harmonic_factor","temporal_phase"],
    "structural_harmonic": ["structural_pattern","harmonic_coupling","temporal_cycle"],
    "coherence_harmonic": ["coherence_field","harmonic_alignment","temporal_stability"],
}

COHERENCE_KEYS = {
    "coherence_core": ["coherence_field","coherence_alignment","coherence_stability"],
    "coherence_harmonic": ["harmonic_alignment","harmonic_balance","harmonic_resonance"],
    "coherence_temporal": ["temporal_continuity","temporal_stability","temporal_resonance"],
}

def find_modules():
    out = []
    for root, dirs, files in os.walk(ROOT):
        if any(ex in root for ex in EXCLUDED):
            continue
        if "module.json" in files:
            out.append(os.path.join(root, "module.json"))
    return out

def check_block(block, expected):
    errs = []
    if not isinstance(block, dict):
        return ["block missing"]
    for triad_name, keys in expected.items():
        t = block.get(triad_name)
        if not isinstance(t, dict):
            errs.append(f"{triad_name} triad missing")
            continue
        for k in keys:
            if k not in t:
                errs.append(f"{triad_name}.{k} missing")
        for k in t.keys():
            if k not in keys:
                errs.append(f"{triad_name}.{k} not canonical")
    return errs

def triad_purity_score(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        return 4  # critical

    module = data.get("module", {})
    triads = module.get("triads")
    if not isinstance(triads, dict):
        return 4

    structural = triads.get("structural_triads")
    harmonic = triads.get("harmonic_triads")
    coherence = triads.get("coherence_triads")

    errs = []
    errs += check_block(structural, STRUCTURAL_KEYS)
    errs += check_block(harmonic, HARMONIC_KEYS)
    errs += check_block(coherence, COHERENCE_KEYS)

    c = len(errs)
    if c == 0: return 0
    if c <= 2: return 1
    if c <= 4: return 2
    if c <= 7: return 3
    return 4

def color_for_score(score):
    return {
        0: "#2ecc71",  # pure
        1: "#f1c40f",  # low drift
        2: "#e67e22",  # moderate
        3: "#e74c3c",  # high
        4: "#2c3e50",  # critical
    }[score]

def build_svg(report):
    svg_path = os.path.join(ROOT, "triad_purity_heatmap.svg")

    cell = 20
    pad = 5
    cols = 20
    rows = (len(report) + cols - 1) // cols
    width = cols * cell + pad * 2
    height = rows * cell + pad * 2

    rects = []
    for i, r in enumerate(report):
        row = i // cols
        col = i % cols
        x = pad + col * cell
        y = pad + row * cell
        color = color_for_score(r["score"])
        rects.append(
            f'<rect x="{x}" y="{y}" width="{cell-2}" height="{cell-2}" '
            f'fill="{color}" stroke="#333" stroke-width="0.5">'
            f'<title>{r["name"]} — triad score {r["score"]}</title>'
            f'</rect>'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
<rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>
{''.join(rects)}
</svg>
"""
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"✔ Created {svg_path}")

def main():
    print("\n=== TriadicFrameworks Triad‑Purity SVG Heatmap Generator ===\n")

    modules = find_modules()
    report = []

    for path in modules:
        name = os.path.basename(os.path.dirname(path))
        score = triad_purity_score(path)
        report.append({"name": name, "score": score})

    build_svg(report)
    print("\n✨ Triad‑purity SVG heatmap generated.\n")

if __name__ == "__main__":
    main()
```

---

This gives you a **single SVG heatmap** of triad‑purity across the entire canon, color‑coded by drift severity.
