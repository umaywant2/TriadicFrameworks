Here is a clean, canonical **`/docs/SARG/examples/latin_alphabet.json`** — aligned with the schema you already established, consistent with the invariant examples you approved yesterday, and tuned to the exact style you’ve been using across the SARG canon.

This version is intentionally **minimal, structural, substrate‑agnostic, and demonstrative** — the Latin alphabet as a SARG‑walkable object, not a linguistic essay.

---

```json
{
  "sarg_version": "1.0.0",
  "id": "latin_alphabet_basic",
  "description": "Minimal SARG example: the 26-letter Latin alphabet treated as a substrate with simple invariants and resonance anchors.",
  "substrate": {
    "type": "symbolic",
    "domain": "alphabetic",
    "name": "Latin Alphabet",
    "elements": [
      "A","B","C","D","E","F","G","H","I","J","K","L","M",
      "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    ],
    "properties": {
      "cardinality": 26,
      "script_direction": "LTR",
      "case_system": "bicameral",
      "historical_root": "Roman"
    }
  },
  "lens": {
    "primary": "structural",
    "secondary": ["phonetic", "graphical"],
    "notes": "Structural lens treats letters as atomic symbolic units; phonetic lens is optional and not required for invariant extraction."
  },
  "invariants": {
    "symmetry": {
      "rotational": ["H", "I", "N", "O", "S", "X", "Z"],
      "mirror_vertical": ["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y"],
      "mirror_horizontal": ["B", "C", "D", "E", "H", "I", "K", "O", "X"]
    },
    "categorical": {
      "vowels": ["A", "E", "I", "O", "U"],
      "consonants": [
        "B","C","D","F","G","H","J","K","L","M",
        "N","P","Q","R","S","T","V","W","X","Y","Z"
      ]
    },
    "positional": {
      "first": "A",
      "last": "Z",
      "midpoint": "M"
    }
  },
  "resonance": {
    "anchors": {
      "axis": {
        "primary": "A–Z linear progression",
        "secondary": "symmetry clusters"
      },
      "clusters": [
        {
          "name": "rotational_symmetry_cluster",
          "members": ["H", "I", "N", "O", "S", "X", "Z"],
          "signature": "R1"
        },
        {
          "name": "vowel_cluster",
          "members": ["A", "E", "I", "O", "U"],
          "signature": "V1"
        }
      ]
    },
    "mapping": {
      "A": { "cluster": "vowel_cluster", "invariants": ["mirror_vertical"] },
      "H": { "cluster": "rotational_symmetry_cluster", "invariants": ["rotational", "mirror_vertical", "mirror_horizontal"] },
      "O": { "cluster": "rotational_symmetry_cluster", "invariants": ["rotational", "mirror_vertical"] },
      "M": { "cluster": null, "invariants": ["mirror_vertical"], "positional_role": "midpoint" }
    }
  },
  "examples": {
    "extraction_walkthrough": [
      {
        "letter": "A",
        "lens": "structural",
        "identified_invariants": ["mirror_vertical"],
        "resonance_anchor": "V1"
      },
      {
        "letter": "H",
        "lens": "structural",
        "identified_invariants": ["rotational", "mirror_vertical", "mirror_horizontal"],
        "resonance_anchor": "R1"
      },
      {
        "letter": "M",
        "lens": "structural",
        "identified_invariants": ["mirror_vertical"],
        "resonance_anchor": null,
        "notes": "Serves as midpoint anchor in positional invariants."
      }
    ]
  }
}
```
