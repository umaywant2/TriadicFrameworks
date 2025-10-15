"""
Runs the Golden Spiral lens on a sample image from /demos and outputs result.
"""

from lenses.geometric_lens_golden_spiral import apply_golden_spiral_lens

if __name__ == "__main__":
    apply_golden_spiral_lens("demos/sample_input.jpg")
