Here's your complete, commit‑ready **lostational_supsphere_atom.json** — the canonical SARG reference object. I studied `Capture.md`'s original schema, the formal JSON Schema block, and every field the evolved grammar established across all the docs we've built. This bridges both into a single definitive artifact. Copy and paste into your GitHub editor.

---

```json
{
  "$schema": "https://triadicframeworks.org/schemas/sarg.schema.json",
  "sarg_version": "1.0.0",

  "substrate": {
    "name": "Lostational Supsphere Atom",
    "type": "natural",
    "domain": "lostational",
    "scale": "sub-atomic / conceptual",
    "epoch": "post-RTT theoretical"
  },

  "atlas_level": 3,

  "lens": [
    {
      "type": "VREL",
      "variant": "standard",
      "version": "1.0.0",
      "notes": "Spatial extraction on supsphere envelope geometry. Reads visible-side axis and inversion-side axis to detect dimensional shape."
    },
    {
      "type": "VREL-A",
      "variant": "standard",
      "version": "1.0.0",
      "notes": "Harmonic-family extraction on shell vibration modes. Reads visible-side oscillation and inversion-side echo timing to detect dimensional pulse."
    }
  ],

  "invariants": {
    "spatial": {
      "vertical": [
        "spherical_shell_symmetry",
        "radial_axis_N",
        "radial_axis_E",
        "radial_axis_S",
        "radial_axis_W"
      ],
      "horizontal": [
        "equatorial_mirror",
        "hemisphere_equivalence"
      ],
      "dual": [
        "spherical_shell_symmetry"
      ]
    },
    "oscillatory": {
      "harmonic": [
        "shell_f1",
        "shell_f2",
        "shell_f3"
      ],
      "rhythmic": [
        "transition_cadence_1to2",
        "transition_cadence_2to3",
        "transition_onset"
      ],
      "phase_coherent": [
        "shell_transition_phase_lock"
      ]
    },
    "cross_lens": [
      "shell_boundary"
    ]
  },

  "invariants_extended": {
    "boundary": [
      "spherical_shell_symmetry"
    ],
    "decay_arc": [
      "shell_frequency_ratio_persistence"
    ],
    "re_emergent": []
  },

  "resonance_mapping": {
    "universal_anchors": [
      {
        "form": "spherical_shell_symmetry",
        "mapped_to": "circle",
        "confidence": 1.0,
        "notes": "Maximally isotropic spatial envelope. The sphere is the purest closed path in three dimensions — perfect self-return."
      },
      {
        "form": "shell_transition_phase_lock",
        "mapped_to": "cross",
        "confidence": 0.9,
        "notes": "Phase relationship locks across shell boundaries. Two oscillatory states meeting at fixed phase — structural crossing."
      },
      {
        "form": "shell_boundary",
        "mapped_to": "circle+cross_compound",
        "confidence": 0.9,
        "notes": "Cross-lens invariant. Simultaneously a shape (spherical shell via VREL dual) and a phase relationship (shell transition lock via VREL-A phase-coherent). Strongest resonance family seed candidate in the current grammar."
      },
      {
        "form": "shell_f1",
        "mapped_to": "line",
        "confidence": 0.85,
        "notes": "Fundamental shell vibration frequency. The carrier wave — the tonal spine of the atom's oscillatory identity."
      },
      {
        "form": "transition_onset",
        "mapped_to": "dot",
        "confidence": 0.8,
        "notes": "The quantum jump — the minimal oscillatory event marking the beginning of a shell transition."
      }
    ],
    "anchor_coverage": {
      "dot": true,
      "circle": true,
      "cross": true,
      "line": true
    }
  },

  "coherence_threshold": {
    "value_percent": 1.0,
    "scale_class": "sub-atomic",
    "arc_entry_description": "Below 1%: fully visible — lenses extract clean invariants. At 1%: arc-entry point — structure begins curving toward inversion. Beyond 1%: invariants become progressively less observable; placeholders take over. At 0D: full inversion — only structural inference."
  },

  "decay_arc": {
    "arc_length": "long",
    "resilience": "high",
    "boundary_crossing_curvature_percent": 1.2,
    "trajectory": "visible_side > arc_entry > curvature_zone > 0D_anchor",
    "description": "Shell structure persists as the atom ionizes. Even as electrons are stripped, remaining shells maintain their relative frequency ratios until the atom is fully ionized. Long decay arc indicates wide curvature zone — the atom bends slowly toward inversion."
  },

  "inversion_side": {
    "hypotheses": "Spherical shell implies Shape Mirror (PH-200). Shell transition lock implies Pulse Mirror (PH-201). Cross-lens shell boundary may sit on Boundary Lock (PH-300). 0D anchor inferred stable — spherical symmetry is maximally isotropic, producing the strongest possible inversion root.",
    "operators": [
      "inversion_link",
      "curvature_seed",
      "coherence_toggle"
    ],
    "future_operators": [
      "spin_mirror",
      "decay_echo",
      "phase_bridge",
      "lineage_root"
    ],
    "anchor_0d": {
      "status": "inferred_stable",
      "evidence": "Spherical symmetry is maximally isotropic. All axes converge at center. Dual invariant (spherical_shell_symmetry) is perfectly stable with no wobble, suggesting a strong inversion anchor. All curvature originates here. All resonance families trace their lineage here.",
      "properties": [
        "dimensionless",
        "no extension",
        "no shape",
        "no frequency",
        "pure structural reference",
        "unique per substrate"
      ]
    },
    "placeholder_references": [
      {
        "id": "PH-200",
        "name": "Shape Mirror",
        "layer": "mirror_scaffolding",
        "implied_by": "spherical_shell_symmetry (VREL dual invariant)",
        "confidence": 0.6,
        "status": "placeholder"
      },
      {
        "id": "PH-201",
        "name": "Pulse Mirror",
        "layer": "mirror_scaffolding",
        "implied_by": "shell_transition_phase_lock (VREL-A phase-coherent invariant)",
        "confidence": 0.55,
        "status": "placeholder"
      },
      {
        "id": "PH-300",
        "name": "Boundary Lock",
        "layer": "coherence_scaffolding",
        "implied_by": "shell_boundary (cross-lens invariant, perfectly stable dual set)",
        "confidence": 0.7,
        "status": "refined"
      }
    ]
  },

  "pre_atomic_ancestry": {
    "description": "Structural lineage tracing the lostational supsphere atom back through the 12 pre-atomic scaffolding seeds (Atlas Level 1) to the 0D anchor (Atlas Level 0). Every lostational supsphere atom descends from PH-012, which combines all eleven preceding seeds into a single 0D-aware structural seed.",
    "lineage_path": "0D_anchor > PH-001..PH-012 > lostational_supsphere_atom",
    "seeds": [
      {
        "id": "PH-001",
        "name": "Resonance Seed",
        "role_in_this_atom": "Provides the minimal unit of oscillation. Without it, shell frequencies (shell_f1, shell_f2, shell_f3) have no origin.",
        "confidence": 0.9,
        "status": "placeholder"
      },
      {
        "id": "PH-002",
        "name": "Phase Pair",
        "role_in_this_atom": "Provides the first dual relationship. Without it, the visible/inverted distinction has no structural ancestor.",
        "confidence": 0.85,
        "status": "placeholder"
      },
      {
        "id": "PH-003",
        "name": "Curvature Initiator",
        "role_in_this_atom": "Provides the first transition from straight to bent. Without it, the 1% curvature threshold has no origin.",
        "confidence": 0.8,
        "status": "placeholder"
      },
      {
        "id": "PH-004",
        "name": "Coherence Packet",
        "role_in_this_atom": "Provides the smallest stable bundle of resonance. Without it, shell structure cannot hold together over time.",
        "confidence": 0.8,
        "status": "placeholder"
      },
      {
        "id": "PH-005",
        "name": "Arc Starter",
        "role_in_this_atom": "Provides the first detectable trajectory. Without it, the atom has no decay arc, no ionization path, no history.",
        "confidence": 0.75,
        "status": "placeholder"
      },
      {
        "id": "PH-006",
        "name": "Attractor Hint",
        "role_in_this_atom": "Provides the proto-well where oscillation settles. Without it, coherence packets cannot stabilize into discrete shells.",
        "confidence": 0.7,
        "status": "placeholder"
      },
      {
        "id": "PH-007",
        "name": "Echo Kernel",
        "role_in_this_atom": "Provides the minimal repeatable pattern. Without it, shell frequencies cannot reproduce across transitions — no spectral identity.",
        "confidence": 0.75,
        "status": "placeholder"
      },
      {
        "id": "PH-008",
        "name": "Spin Protoform",
        "role_in_this_atom": "Provides pre-spin asymmetry. Without it, orbital angular momentum (l > 0 orbitals) has no structural ancestor.",
        "confidence": 0.6,
        "status": "placeholder"
      },
      {
        "id": "PH-009",
        "name": "Boundary Whisper",
        "role_in_this_atom": "Provides the first inside/outside distinction. Without it, the supsphere envelope has no boundary — no visible face, no inner face.",
        "confidence": 0.85,
        "status": "placeholder"
      },
      {
        "id": "PH-010",
        "name": "Stackable Unit",
        "role_in_this_atom": "Provides the capacity to combine without losing coherence. Without it, this atom cannot participate in molecular families (Atlas Level 4+).",
        "confidence": 0.7,
        "status": "placeholder"
      },
      {
        "id": "PH-011",
        "name": "Break Threshold",
        "role_in_this_atom": "Provides the first point where coherence fails. Without it, ionization, decay, and state transitions have no structural mechanism.",
        "confidence": 0.75,
        "status": "placeholder"
      },
      {
        "id": "PH-012",
        "name": "Lostational Anchor",
        "role_in_this_atom": "Capstone of the pre-atomic layer. Combines all eleven preceding seeds into a single 0D-aware structural seed. This atom descends directly from PH-012.",
        "confidence": 0.8,
        "status": "placeholder"
      }
    ]
  },

  "error_flags": [],

  "notes": "Canonical SARG reference object. Full resonance fingerprint: spatial + oscillatory + cross-lens + inversion-side + extended invariants. Anchor-complete — all four universal anchors (dot, circle, cross, line) are represented. Cross-lens invariant (shell_boundary) is the strongest resonance family seed candidate in the current grammar. This object demonstrates every feature of the SARG schema: dual-lens extraction, compound invariant types, inversion-side scaffolding with 0D anchor inference, pre-atomic ancestry tracing through all 12 seeds, decay-arc modeling, and coherence threshold specification. Unlike standard atomic models, this atom acknowledges 0D, carries an inversion side, and behaves as a node in the resonance graph.",

  "metadata": {
    "created": "2026-04-20",
    "created_by": "Nawder Loswin",
    "schema_version": "1.0.0",
    "object_status": "canonical_reference",
    "related_files": [
      "docs/SARG/Capture.md",
      "docs/SARG/lenses/VREL.md",
      "docs/SARG/lenses/VREL-A.md",
      "docs/SARG/invariants/invariant_types.md",
      "docs/SARG/invariants/invariant_examples.md",
      "docs/SARG/inversion/inversion_side_overview.md",
      "docs/SARG/inversion/inversion_placeholders.md"
    ]
  }
}
```

---

### What this object delivers

| Block | What It Establishes |
|---|---|
| **`substrate`** | Formal name, type, domain, scale, epoch — bridges `Capture.md`'s original object shape with the evolved lostational vocabulary |
| **`lens` (array)** | Dual-lens declaration: VREL for spatial extraction on envelope geometry, VREL‑A for harmonic extraction on shell vibration modes |
| **`invariants.spatial`** | Full VREL triad — 5 vertical (spherical shell + 4 cardinal radial axes), 2 horizontal (equatorial mirror, hemisphere equivalence), 1 dual (spherical shell symmetry) |
| **`invariants.oscillatory`** | Full VREL‑A triad — 3 harmonic (shell frequencies f1–f3), 3 rhythmic (two transition cadences + onset), 1 phase‑coherent (shell transition phase lock) |
| **`invariants.cross_lens`** | `shell_boundary` — the single feature that is simultaneously a VREL dual invariant and a VREL‑A phase‑coherent invariant; the rarest, most stable type in the grammar |
| **`invariants_extended`** | Boundary invariant (spherical shell wobbles at fine resolution), decay‑arc invariant (frequency ratios persist through ionization), empty re‑emergent placeholder |
| **`resonance_mapping`** | All 5 anchor mappings with confidence scores + `anchor_coverage` confirming all four universal anchors (● ○ × \|) are represented |
| **`coherence_threshold`** | 1% curvature at sub‑atomic scale with arc‑entry description |
| **`decay_arc`** | Long arc, high resilience, 1.2% boundary crossing, full trajectory path from visible side through curvature zone to 0D |
| **`inversion_side`** | Hypotheses, 3 active operators + 4 future operators, full `anchor_0d` status block (inferred stable with evidence), 3 placeholder references (PH‑200, PH‑201, PH‑300) with individual confidence and status |
| **`pre_atomic_ancestry`** | Complete lineage through all 12 PH seeds (PH‑001 → PH‑012), each with `role_in_this_atom` explaining precisely why that seed is structurally required for this object to exist |
| **`error_flags`** | Empty — this is a clean, canonical extraction |
| **`metadata`** | Provenance (created date, author, schema version, canonical status) + full `related_files` cross‑reference to every doc that references this object |

### Why this object matters

This is the **reference implementation** that every SARG doc we've built points to:
- `VREL.md` §7 → `examples/lostational_supsphere_atom.json` ✓
- `VREL‑A.md` §7 → ✓
- `inversion_side_overview.md` §10 → ✓
- `inversion_placeholders.md` §8 → ✓
- `invariant_types.md` §10 → ✓
- `invariant_examples.md` §10 (Example 6 counterpart) → ✓

Paste it in and commit — all those links go live. 
