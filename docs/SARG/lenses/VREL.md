# **VREL — Vertical Resonance Extraction Lens**

*A SARG lens for extracting structural invariants from any substrate.*

VREL is the primary lens in SARG.
It reads a substrate's structure and extracts the features that persist under mirror‑axis transformations — vertical, horizontal, and dual.
These invariants become the substrate's **resonance fingerprint**, which SARG then maps to universal anchors.

VREL is substrate‑agnostic: it operates identically whether the input is a glyph, a crystal lattice, a harmonic series, or a planetary envelope.

---

## **1. What VREL Extracts**

VREL applies mirror‑axis analysis to a substrate and returns three invariant classes:

### **1.1 Vertical Invariants**

Features that remain unchanged when the substrate is reflected across a vertical axis.

- In glyphs: letters like **A**, **H**, **M**, **T**, **U**, **V**, **W**, **X**, **Y**
- In geometry: shapes with bilateral vertical symmetry
- In crystals: planes of vertical mirror symmetry
- In symbolic substrates: operators or tokens with left–right equivalence

### **1.2 Horizontal Invariants**

Features that remain unchanged when the substrate is reflected across a horizontal axis.

- In glyphs: letters like **B**, **C**, **D**, **E**, **H**, **K**, **O**, **X**
- In geometry: shapes with bilateral horizontal symmetry
- In acoustic substrates: waveforms with top–bottom amplitude symmetry
- In biological substrates: dorsal–ventral mirror planes

### **1.3 Dual Invariants**

Features that persist under **both** vertical and horizontal reflection.
These are the most structurally stable elements in any substrate.

- In glyphs: **H**, **I**, **O**, **X**
- In geometry: circles, squares, regular polygons with even‑order symmetry
- In crystals: highly symmetric unit cells
- In cosmological substrates: isotropic structures (spherical shells, uniform fields)

Dual invariants are the strongest candidates for resonance anchor mapping.

---

## **2. How VREL Behaves Across Substrates**

VREL adapts its extraction logic to the substrate's native structure.
The lens itself does not change — the **interpretation of "axis"** changes.

| Substrate Type | Vertical Axis | Horizontal Axis | What VREL Reveals |
|----------------|---------------|-----------------|-------------------|
| Linguistic | Left–right midline of a glyph | Top–bottom midline of a glyph | Stroke families and symmetry classes |
| Geometric | Primary symmetry axis | Secondary symmetry axis | Axes, planes, and symmetry orders |
| Acoustic | Time‑axis symmetry of a waveform | Amplitude‑axis symmetry | Harmonic stability and phase coherence |
| Symbolic | Relational left–right equivalence | Relational top–bottom equivalence | Structural roles and operator symmetry |
| Biological | Sagittal plane | Transverse plane | Body‑plan invariants and mirror organs |
| Cosmological | Polar axis | Equatorial plane | Shell symmetries and radial invariants |
| Lostational | Visible‑side axis | Inversion‑side axis | Dimensional drift and resonance shells |

The same lens produces the same **invariant types** (vertical, horizontal, dual) regardless of domain.
Only the substrate determines what those invariants *are*.

---

## **3. Invariants Produced by VREL**

Every VREL extraction produces a structured invariant set:

```json
"invariants": {
  "vertical": ["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y"],
  "horizontal": ["B", "C", "D", "E", "H", "I", "K", "O", "X"],
  "dual": ["H", "I", "O", "X"]
}
