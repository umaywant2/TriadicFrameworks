# 🔧 glyph_compare.py – Resonance Clarity Integration

import matplotlib.pyplot as plt

# 1. Extend compare_glyphs to accept basetype:

def compare_glyphs(results, title="Triconceptual Glyph Comparison", basetype="decimal"):
    """
    Visualize and compare glyphs across direct, reflected, and inverted views.
    results: dictionary from tops_session.run_tops_session()
    basetype: resonance clarity lens (e.g., binary, phi, negabinary, corridor6.9)
    """
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))
    modes = ["direct", "reflected", "inverted"]
    colors = ["#0077cc", "#cc3300", "#6600cc"]

    for i, mode in enumerate(modes):
        axs[i].set_title(f"{mode.capitalize()} Views (Base: {basetype})")
        for key, (x, y) in results[mode].items():
            axs[i].plot(x, y, label=str(key), color=colors[i], alpha=0.6)
        axs[i].axis("equal")
        axs[i].legend()
        axs[i].grid(True)

    fig.suptitle(f"{title} — Resonance Lens: {basetype.upper()}")
    plt.tight_layout()
    plt.show()

# 2. Update the __main__ block to pass basetype:

if __name__ == "__main__":
    from tops_session import run_tops_session
    import argparse

    parser = argparse.ArgumentParser(description="Compare glyphs with Resonance Clarity")
    parser.add_argument("--basetype", "-b", type=str, default="decimal",
                        help="Select base lens (e.g., binary, phi, negabinary, corridor6.9)")
    args = parser.parse_args()

    results = run_tops_session(basetype=args.basetype)
    compare_glyphs(results, basetype=args.basetype)

# ✨ Why this matters
# Comparisons are now resonance‑aware: every subplot declares which base lens was applied.
# Lineage clarity: the figure title and subplot titles embed the base lens, so remixers know exactly what lens produced the glyphs.
# Consistency: aligns with direct_view.py, reflective_view.py, and inversion_logic.py.
