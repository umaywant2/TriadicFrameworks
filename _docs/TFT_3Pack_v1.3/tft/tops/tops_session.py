import argparse
from mirror_geometry import generate_spiral
from direct_view import generate_views
from reflective_view import generate_reflections
from inversion_logic import generate_inversions

def run_tops_session(a=1, b=0.15, turns=3, basetype="decimal"):
    """
    Run full triconceptual simulation:
    - Direct views
    - Reflections
    - Inversions
    - Resonance Clarity base lens
    """
    x, y = generate_spiral(a=a, b=b, turns=turns)

    direct_views = generate_views(x, y, basetype=basetype)
    reflected_views = generate_reflections(x, y, basetype=basetype)
    inverted_views = generate_inversions(x, y, basetype=basetype)

    return {
        "direct": direct_views,
        "reflected": reflected_views,
        "inverted": inverted_views,
        "basetype": basetype
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run TFT Tops Session with Resonance Clarity")
    parser.add_argument("--basetype", "-b", type=str, default="decimal",
                        help="Select base lens (e.g., binary, phi, negabinary, corridor6.9)")
    args = parser.parse_args()

    results = run_tops_session(basetype=args.basetype)

    print(f"\nResonance Clarity Base Lens: {args.basetype.upper()}")
    for mode, views in results.items():
        if mode != "basetype":
            print(f"\n{mode.upper()} VIEWS:")
            for key, (x, y) in views.items():
                print(f" {key} : {len(x)} points")

