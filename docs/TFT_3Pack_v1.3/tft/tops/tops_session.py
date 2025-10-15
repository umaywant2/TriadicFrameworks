from mirror_geometry import generate_spiral
from direct_view import generate_views
from reflective_view import generate_reflections
from inversion_logic import generate_inversions

def run_tops_session(a=1, b=0.15, turns=3):
    """
    Run full triconceptual simulation:
    - Direct views
    - Reflections
    - Inversions
    """
    x, y = generate_spiral(a=a, b=b, turns=turns)

    direct_views = generate_views(x, y)
    reflected_views = generate_reflections(x, y)
    inverted_views = generate_inversions(x, y)

    return {
        "direct": direct_views,
        "reflected": reflected_views,
        "inverted": inverted_views
    }

if __name__ == "__main__":
    results = run_tops_session()
    for mode, views in results.items():
        print(f"\n{mode.upper()} VIEWS:")
        for key, (x, y) in views.items():
            print(f"  {key}: {len(x)} points")
