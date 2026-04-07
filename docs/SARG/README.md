# Substrate‑Agnostic Resonance Grammar (SARG)

## Purpose

A reusable grammar for detecting, encoding, and aligning resonance patterns across any substrate:
- universal communication
- cross‑species translation
- cross‑domain pattern alignment
- resonance‑based encoding
- substrate‑aware teaching signals
- future 3D spin operators

SARG sits *above* specific lenses (like VREL) and *above* specific substrates (like URS).  
It defines how invariants, echoes, and alignments are described in a common language.

---

## Core Concepts

- **Substrate:**  
  Any domain carrying structure (linguistic, acoustic, geometric, biological, cosmological, etc.).

- **Lens:**  
  An operator that extracts invariants from a substrate (e.g., VREL, VREL‑A).

- **Invariant:**  
  A pattern that persists under a defined transformation (mirror, rotation, scaling, decay arc, etc.).

- **Resonance Family:**  
  A set of invariants that share structural similarity across substrates.

- **Alignment:**  
  A mapping between invariants in different substrates that preserves structure.

---

## Minimal Data Model

SARG expects three layers:

1. **Substrate description**  
2. **Lens output (invariants)**  
3. **Resonance / alignment layer**

---

## Example JSON Shape

```json
{
  "substrate": {
    "name": "Latin Alphabet",
    "type": "linguistic",
    "epoch": "Classical/Modern"
  },
  "lens": {
    "name": "VREL",
    "version": "1.0.0"
  },
  "invariants": {
    "vertical": ["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y"],
    "horizontal": ["B", "C", "D", "E", "H", "I", "K", "O", "X"],
    "dual": ["H", "I", "O", "X"]
  },
  "resonance_mapping": {
    "universal_anchors": [
      { "form": "I", "mapped_to": "line" },
      { "form": "O", "mapped_to": "circle" },
      { "form": "X", "mapped_to": "cross" },
      { "form": "H", "mapped_to": "line+cross_hybrid" }
    ]
  }
}
