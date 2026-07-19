# Latin Alphabet — Resonance Cluster Map
_A diagrammatic overview of structural, phonetic, and graphical clusters._

## 1. Structural Symmetry Map

```
Vertical symmetry:     A H I M O T U V W X Y
Horizontal symmetry:   B C D E H I K O X
Rotational symmetry:   H I N O S X Z
```

---

## 2. Phonetic Resonance Clusters

```
[Vowel Core] (PH-V)
A  E  I  O  U

[Consonant Ring] (PH-C)
B C D F G H J K L M N P Q R S T V W X Y Z
```

---

## 3. Graphical / Stroke Geometry Clusters

```
[Curved Forms] (GR-C)
B C D G J O P Q R S U

[Angular Forms] (GR-A)
A E F H I K L M N T V W X Y Z
```

---

## 4. Combined Resonance Map (Tri‑Layer)

```
-
          ┌──────────────────────────────┐
          │        STRUCTURAL AXIS       │
          └──────────────────────────────┘
A–Z linear progression
Symmetry clusters overlay

          ┌──────────────────────────────┐
          │        PHONETIC LAYER        │
          └──────────────────────────────┘
Vowel core ↔ consonant ring

          ┌──────────────────────────────┐
          │       GRAPHICAL LAYER        │
          └──────────────────────────────┘
Curved ↔ Angular stroke geometry
```

---

## 5. Example: Letter “O” Across All Layers

```
Structural: rotational symmetry
Phonetic:   vowel core
Graphical:  curved form
Resonance:  triple‑aligned anchor (R1, PH-V, GR-C)
```

---

# ✅ `latin_alphabet_minimal.json`
_Ultra‑tiny teaching version — the smallest valid SARG object._

```json
{
  "sarg_version": "1.0.0",
  "id": "latin_alphabet_minimal",
  "description": "Minimal SARG example for teaching: Latin alphabet as a bare substrate.",
  "substrate": {
    "type": "symbolic",
    "domain": "alphabetic",
    "name": "Latin Alphabet",
    "elements": ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  },
  "lens": { "primary": "structural" },
  "invariants": {},
  "resonance": {},
  "examples": {}
}
```

---

# ✅ `latin_alphabet_phonetic.json`
_IPA‑aware variant — includes phonetic categories but stays structural-first._

```json
{
  "sarg_version": "1.0.0",
  "id": "latin_alphabet_phonetic",
  "description": "Latin alphabet with IPA-aware phonetic groupings.",
  "substrate": {
    "type": "symbolic",
    "domain": "alphabetic",
    "name": "Latin Alphabet",
    "elements": ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  },
  "lens": {
    "primary": "phonetic",
    "secondary": ["structural"],
    "notes": "Phonetic categories are approximate and language-agnostic."
  },
  "invariants": {
    "phonetic": {
      "vowels": ["A","E","I","O","U"],
      "semivowels": ["Y","W"],
      "plosives": ["P","B","T","D","K","G"],
      "fricatives": ["F","V","S","Z","H"],
      "nasals": ["M","N"],
      "liquids": ["L","R"],
      "affricates": ["C","J","Q","X"]
    }
  },
  "resonance": {
    "anchors": {
      "clusters": [
        { "name": "vowel_core", "members": ["A","E","I","O","U"], "signature": "PH-V" },
        { "name": "consonant_ring", "members": ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"], "signature": "PH-C" }
      ]
    }
  },
  "examples": {
    "extraction_walkthrough": [
      {
        "letter": "A",
        "identified_invariants": ["vowel"],
        "resonance_anchor": "PH-V"
      }
    ]
  }
}
```

---

# ✅ `latin_alphabet_graphical.json`
_Stroke‑based invariants — geometric, diagram‑friendly, perfect for your visual canon._

```json
{
  "sarg_version": "1.0.0",
  "id": "latin_alphabet_graphical",
  "description": "Latin alphabet with stroke-based graphical invariants.",
  "substrate": {
    "type": "symbolic",
    "domain": "alphabetic",
    "name": "Latin Alphabet",
    "elements": ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  },
  "lens": {
    "primary": "graphical",
    "secondary": ["structural"],
    "notes": "Graphical invariants based on stroke geometry and symmetry."
  },
  "invariants": {
    "strokes": {
      "single_stroke_forms": ["C","I","J","L","O","S","U","V"],
      "multi_stroke_forms": ["A","B","D","E","F","G","H","K","M","N","P","Q","R","T","W","X","Y","Z"]
    },
    "geometry": {
      "curved": ["B","C","D","G","J","O","P","Q","R","S","U"],
      "angular": ["A","E","F","H","I","K","L","M","N","T","V","W","X","Y","Z"],
      "mixed": ["R","G"]
    },
    "symmetry": {
      "vertical": ["A","H","I","M","O","T","U","V","W","X","Y"],
      "horizontal": ["B","C","D","E","H","I","K","O","X"],
      "rotational": ["H","I","N","O","S","X","Z"]
    }
  },
  "resonance": {
    "anchors": {
      "clusters": [
        { "name": "curved_forms", "members": ["B","C","D","G","J","O","P","Q","R","S","U"], "signature": "GR-C" },
        { "name": "angular_forms", "members": ["A","E","F","H","I","K","L","M","N","T","V","W","X","Y","Z"], "signature": "GR-A" }
      ]
    }
  },
  "examples": {
    "extraction_walkthrough": [
      {
        "letter": "O",
        "identified_invariants": ["curved", "rotational_symmetry"],
        "resonance_anchor": "GR-C"
      }
    ]
  }
}
```

---

If you want, AI can also generate:

- a **tri‑layer SVG diagram**  
- a **cluster‑aware teaching sheet**  
- a **SARG‑walkable interactive JSON bundle**  
- or fold these into a **full Latin Alphabet SARG Pack** for `/docs/SARG/examples/latin/`
