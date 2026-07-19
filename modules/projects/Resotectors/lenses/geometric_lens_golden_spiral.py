"""
🌀 Resotectors — Golden Spiral Lens
Dev-friendly example lens that outlines golden spiral curves in image data.

- Input: any .jpg or .png
- Output: same image with golden spirals overlaid for detected edges
"""

import cv2
import numpy as np
import os

def apply_golden_spiral_lens(image_path, output_path=None):
    if output_path is None:
        base, ext = os.path.splitext(image_path)
        output_path = f"{base}_golden_spiral{ext}"

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"[!] Could not load {image_path}")

    # Basic edge detection
    edges = cv2.Canny(img, 50, 150)

    # Prepare overlay
    overlay = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    h, w = overlay.shape[:2]
    center = (w // 2, h // 2)
    color = (0, 215, 255)  # Gold (BGR)

    # Draw spiral arcs (demo style)
    for r in range(40, min(w, h)//2, 40):
        cv2.ellipse(overlay, center, (r, int(r * 0.618)), 0, 0, 270, color, 1)

    cv2.imwrite(output_path, overlay)
    print(f"[+] Golden Spiral Lens applied — saved to {output_path}")
    return output_path

if __name__ == "__main__":
    # Swap "sample_input.jpg" with an actual file in demos/
    apply_golden_spiral_lens("sample_input.jpg")
