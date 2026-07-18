# **Invariant Examples — Worked Extractions**

*Seeing the grammar in action, substrate by substrate.*

This file walks through **complete, annotated SARG extractions** across multiple substrates.

Each example follows the same arc:

1. **Identify** the substrate and choose a lens.
2. **Extract** invariants (primary, secondary, intersection).
3. **Map** the intersection set to universal resonance anchors.
4. **Score** confidence for each mapping.
5. **Produce** the full SARG JSON object.

Read `invariant_types.md` first for definitions.
This file shows what those definitions look like when applied to real substrates.

---

## **1. How to Read These Examples**

Every example contains:

- **Substrate card** — what is being analyzed, which lens is applied, and why.
- **Extraction walkthrough** — step‑by‑step invariant extraction with reasoning.
- **Anchor mapping** — how each intersection‑set element maps to ● ○ × |.
- **Full SARG JSON** — the complete object, ready to drop into the Atlas.
- **Commentary** — what the extraction reveals about the substrate's structure.

JSON keys follow the schema from `invariant_types.md` §4.3 and §5.4:

```
invariants.spatial.vertical / horizontal / dual
invariants.oscillatory.harmonic / rhythmic / phase_coherent
invariants.cross_lens
invariants_extended.boundary / decay_arc / re_emergent
```

---

## **2. Example 1 — Latin Alphabet (Linguistic Substrate, VREL)**

The canonical SARG example.
This is the extraction described in `Capture.md` — the first substrate the grammar was tested on.

### **Substrate Card**

| Field | Value |
|-------|-------|
| Substrate | The 26 uppercase letters of the Latin alphabet |
| Domain | Linguistic |
| Lens | VREL (mirror‑axis analysis) |
| Why this lens | Letters are spatial glyphs — shape and symmetry are their primary structure |

### **Extraction Walkthrough**

**Step 1 — Vertical axis reflection (left–right mirror).**

Hold each letter against a vertical axis. Which letters look identical when their left and right halves are swapped?

Result: **A, H, I, M, O, T, U, V, W, X, Y** (11 letters)

These letters have bilateral vertical symmetry. Their left half mirrors their right half.

**Step 2 — Horizontal axis reflection (top–bottom mirror).**

Hold each letter against a horizontal axis. Which letters look identical when their top and bottom halves are swapped?

Result: **B, C, D, E, H, I, K, O, X** (9 letters)

These letters have bilateral horizontal symmetry. Their top half mirrors their bottom half.

**Step 3 — Dual axis (both mirrors simultaneously).**

Which letters appear in *both* sets?

`{A, H, I, M, O, T, U, V, W, X, Y} ∩ {B, C, D, E, H, I, K, O, X}` = **{H, I, O, X}**

Four letters survive both reflections. These are the dual invariants — the most structurally stable glyphs in the Latin alphabet.

### **Anchor Mapping**

| Glyph | Geometric Shape | Mapped Anchor | Confidence |
|-------|-----------------|---------------|------------|
| H | Two vertical strokes joined by a horizontal bar | line + cross hybrid | 0.8 |
| I | Single vertical stroke | line | 1.0 |
| O | Closed curve / ring | circle | 1.0 |
| X | Two strokes crossing at center | cross | 1.0 |

Three of four dual invariants map cleanly to a single anchor (confidence 1.0).
One (H) maps to a compound anchor — it carries both axis (line) and intersection (cross) properties.

### **Full SARG JSON**

```json
{
  "substrate": "Latin Alphabet (Uppercase)",
  "domain": "linguistic",
  "atlas_level": 2,
  "lens": {
    "type": "VREL",
    "variant": "standard",
    "version": "1.0.0",
    "notes": "Mirror‑axis resonance extraction on 26 uppercase Latin glyphs."
  },
  "invariants": {
    "spatial": {
      "vertical": ["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y"],
      "horizontal": ["B", "C", "D", "E", "H", "I", "K", "O", "X"],
      "dual": ["H", "I", "O", "X"]
    }
  },
  "resonance_mapping": {
    "universal_anchors": [
      { "form": "H", "mapped_to": "line+cross_hybrid", "confidence": 0.8 },
      { "form": "I", "mapped_to": "line", "confidence": 1.0 },
      { "form": "O", "mapped_to": "circle", "confidence": 1.0 },
      { "form": "X", "mapped_to": "cross", "confidence": 1.0 }
    ]
  },
  "inversion_side": null,
  "error_flags": [],
  "notes": "Canonical SARG extraction. Three of four universal anchors represented in a single substrate."
}
```

### **Commentary**

The Latin alphabet produces an exceptionally clean extraction.
Three of the four universal anchors (line, circle, cross) appear directly in the dual set.
Only the point anchor (●) is absent — no uppercase Latin letter reduces to a dot.

This makes the Latin alphabet a natural **calibration substrate** — any new lens or grammar extension can be tested against it to verify consistency.

The missing point anchor is not an error.
It is structurally informative: the Latin alphabet's design favors strokes, loops, and crossings over isolated nodes.
A different writing system (e.g., Braille, where every character is built from dots) might fill that gap.

---

## **3. Example 2 — Quartz Crystal (Crystalline Substrate, VREL)**

A physical substrate analyzed through spatial symmetry.

### **Substrate Card**

| Field | Value |
|-------|-------|
| Substrate | Hexagonal quartz crystal (SiO₂, α‑quartz) |
| Domain | Crystalline |
| Lens | VREL (mirror‑axis analysis) |
| Why this lens | Crystals are defined by their spatial symmetry — mirror planes are their native language |

### **Extraction Walkthrough**

**Step 1 — Vertical axis reflection.**

α‑quartz belongs to trigonal crystal system, point group 32 (three twofold rotation axes, no mirror planes in the strict crystallographic sense).
However, the *hexagonal prism habit* — the visible shape of a well‑formed quartz crystal — presents apparent vertical mirror symmetry across each of its six prism faces.

Result: **prism‑face mirror planes** (6 apparent vertical symmetry features)

**Step 2 — Horizontal axis reflection.**

The crystal terminates differently at its two ends (positive and negative rhombohedra are not identical in natural quartz).
Horizontal mirror symmetry is **broken** — the top and bottom are structurally distinct.

Result: **∅** (no horizontal invariants)

**Step 3 — Dual axis.**

`{6 vertical features} ∩ {∅}` = **∅**

The dual set is empty.

### **Anchor Mapping**

No dual invariants → no intersection‑set anchor mapping.

However, the vertical invariants alone can still be mapped at reduced confidence:

| Feature | Mapped Anchor | Confidence |
|---------|---------------|------------|
| Prism‑face mirror plane | line (axial symmetry) | 0.6 |
| Hexagonal cross‑section | circle (closed envelope) | 0.5 |

### **Full SARG JSON**

```json
{
  "substrate": "Hexagonal Quartz Crystal (α‑quartz)",
  "domain": "crystalline",
  "atlas_level": 3,
  "lens": {
    "type": "VREL",
    "variant": "standard",
    "version": "1.0.0",
    "notes": "Mirror‑axis extraction on crystal habit. Internal point group 32 lacks mirror planes; habit shows apparent vertical mirrors."
  },
  "invariants": {
    "spatial": {
      "vertical": ["prism_face_mirror_1", "prism_face_mirror_2", "prism_face_mirror_3", "prism_face_mirror_4", "prism_face_mirror_5", "prism_face_mirror_6"],
      "horizontal": [],
      "dual": []
    }
  },
  "resonance_mapping": {
    "universal_anchors": [
      { "form": "prism_face_mirror", "mapped_to": "line", "confidence": 0.6 },
      { "form": "hexagonal_cross_section", "mapped_to": "circle", "confidence": 0.5 }
    ]
  },
  "inversion_side": null,
  "error_flags": ["S1: empty dual set — low structural coherence under VREL"],
  "notes": "Empty dual set suggests VREL alone is insufficient for this substrate. Recommend supplementing with VREL‑A (phonon frequency analysis) for a compound extraction."
}
```

### **Commentary**

Quartz demonstrates a key grammar principle: **an empty dual set is not a failure — it is a signal.**

The S1 error flag (Invariant Absence) tells us that VREL captures only part of quartz's structural identity.
The crystal's deepest stability lives in its *vibrational* structure (piezoelectric resonance, phonon modes) — territory that VREL‑A is designed to read.

This is exactly the situation `invariant_types.md` §2.3 describes: when the intersection set is empty, the substrate may require a different lens or a compound extraction.

---

## **4. Example 3 — Concert A / Tuning Fork (Acoustic Substrate, VREL‑A)**

A pure oscillatory substrate — the simplest possible VREL‑A extraction.

### **Substrate Card**

| Field | Value |
|-------|-------|
| Substrate | Concert A (440 Hz sine wave from an ideal tuning fork) |
| Domain | Acoustic |
| Lens | VREL‑A (harmonic‑family analysis) |
| Why this lens | A tuning fork is a pure oscillator — frequency and rhythm are its only structure |

### **Extraction Walkthrough**

**Step 1 — Harmonic decomposition.**

An ideal tuning fork produces a nearly pure sine wave at 440 Hz.
In practice, a real fork also produces faint overtones at startup that decay rapidly, leaving the fundamental.

Result: **f₀ = 440 Hz** (dominant); faint transient overtones at ~2f₀, ~6.27f₀ (inharmonic clang tones, decay within milliseconds)

Stable harmonic invariants: **f₀**

**Step 2 — Rhythmic analysis.**

A struck tuning fork produces a single sustained tone with exponential amplitude decay.
There is no rhythmic patterning — no beat, no pulse, no grouping.

The only temporal feature is the **onset transient** (the strike) and the **decay envelope**.

Result: **onset transient** (one rhythmic feature — the impulse that starts the oscillation)

**Step 3 — Phase‑coherent intersection.**

`{f₀} ∩ {onset_transient}` — these are structurally different kinds of feature (a frequency vs. a temporal event).

However, the onset transient *initiates* f₀ and they are phase‑locked at t=0.
The relationship between them is: the strike defines the phase of the resulting oscillation.

Result: **f₀–onset lock** (one phase‑coherent invariant — the fundamental's phase is set by the strike)

### **Anchor Mapping**

| Feature | Acoustic Root | Mapped Anchor | Confidence |
|---------|---------------|---------------|------------|
| f₀ (440 Hz fundamental) | Carrier wave / sustained tone | line | 1.0 |
| onset transient | Impulse / attack | dot | 0.95 |
| f₀–onset lock | Phase lock at t=0 | dot + line compound | 0.85 |

### **Full SARG JSON**

```json
{
  "substrate": "Concert A (440 Hz Tuning Fork)",
  "domain": "acoustic",
  "atlas_level": 2,
  "lens": {
    "type": "VREL‑A",
    "variant": "standard",
    "version": "1.0.0",
    "notes": "Harmonic‑family extraction on idealized tuning fork. Transient overtones excluded — they decay below extraction threshold within milliseconds."
  },
  "invariants": {
    "oscillatory": {
      "harmonic": ["f₀_440Hz"],
      "rhythmic": ["onset_transient"],
      "phase_coherent": ["f₀_onset_lock"]
    }
  },
  "resonance_mapping": {
    "universal_anchors": [
      { "form": "f₀_440Hz", "mapped_to": "line", "confidence": 1.0 },
      { "form": "onset_transient", "mapped_to": "dot", "confidence": 0.95 },
      { "form": "f₀_onset_lock", "mapped_to": "dot+line_compound", "confidence": 0.85 }
    ]
  },
  "inversion_side": null,
  "error_flags": [],
  "notes": "Minimal acoustic substrate. Single fundamental, single onset, single phase lock. Clean two‑anchor mapping (dot + line)."
}
```

### **Commentary**

The tuning fork is the acoustic equivalent of the letter **I** — a substrate so simple that its invariant structure is almost trivially clean.

It maps to two anchors: dot (●) for the onset impulse and line (|) for the sustained fundamental.
The phase‑coherent invariant links them — the dot *becomes* the line at t=0.

This makes the tuning fork a natural **acoustic calibration substrate**, just as the Latin alphabet is the spatial calibration substrate.

Notice what is absent: circle (○) and cross (×).
A tuning fork has no looping oscillation (it decays, never returns) and no harmonic crossing (the fundamental is alone).
A richer acoustic substrate — a bell, a vowel, an orchestra — would fill those anchor slots.

---

## **5. Example 4 — Human Heartbeat (Biological Substrate, Dual‑Lens)**

The first **compound extraction** — both VREL and VREL‑A applied to the same substrate.

### **Substrate Card**

| Field | Value |
|-------|-------|
| Substrate | Human heartbeat (healthy adult at rest, ~60–72 bpm) |
| Domain | Biological |
| Lens | VREL + VREL‑A (compound extraction) |
| Why both lenses | The heart has spatial structure (bilateral anatomy) *and* oscillatory structure (rhythmic pulse) — both carry invariants |

### **VREL Extraction (Spatial)**

**Vertical axis:** The heart sits left of the thoracic midline, but its gross anatomy has approximate bilateral symmetry — left ventricle mirrors right ventricle, left atrium mirrors right atrium (with structural differences in wall thickness and volume).

Vertical invariants: **four‑chamber bilateral layout, septum midline, valve ring geometry**

**Horizontal axis:** The heart's top (atria) and bottom (ventricles) are structurally distinct — different wall thickness, different function, different volume. No horizontal mirror symmetry.

Horizontal invariants: **∅**

**Dual:** `{bilateral features} ∩ {∅}` = **∅**

The spatial dual set is empty — the heart is vertically symmetric but not horizontally symmetric.

### **VREL‑A Extraction (Oscillatory)**

**Harmonic decomposition:** The heartbeat has a dominant frequency (f₀ ≈ 1.0–1.2 Hz at rest) and subharmonics tied to the cardiac cycle phases (systole, diastole, atrial kick).

Harmonic invariants: **f₀ (base heart rate), 2f₀ (systole–diastole pair), respiratory sinus arrhythmia envelope**

**Rhythmic analysis:** The heartbeat is strongly rhythmic — a repeating lub‑dub pattern with consistent timing ratios between S1 (mitral/tricuspid closure) and S2 (aortic/pulmonic closure).

Rhythmic invariants: **lub‑dub pair, systole‑to‑diastole ratio (~1:2 at rest), beat‑to‑beat interval stability**

**Phase‑coherent intersection:** The lub‑dub rhythm is phase‑locked to the cardiac frequency. S1 always occurs at a fixed phase of each cycle. The systole‑to‑diastole ratio remains stable across a wide range of heart rates.

Phase‑coherent invariants: **S1–S2 phase lock, systole‑diastole ratio lock**

### **Cross‑Lens Analysis**

VREL dual set: ∅
VREL‑A phase‑coherent set: {S1–S2 phase lock, systole‑diastole ratio lock}

Cross‑lens invariants: **∅** (no shared elements — the spatial and oscillatory invariants describe different structural layers)

### **Anchor Mapping**

| Feature | Source | Mapped Anchor | Confidence |
|---------|--------|---------------|------------|
| f₀ (base heart rate) | VREL‑A harmonic | line (carrier wave) | 0.9 |
| lub‑dub pair | VREL‑A rhythmic | dot + dot compound (paired impulse) | 0.85 |
| S1–S2 phase lock | VREL‑A phase‑coherent | cross (two events meeting at fixed phase) | 0.8 |
| systole‑diastole ratio lock | VREL‑A phase‑coherent | circle (self‑returning cycle) | 0.85 |
| bilateral chamber layout | VREL vertical | line (axial symmetry) | 0.6 |

### **Full SARG JSON**

```json
{
  "substrate": "Human Heartbeat (Healthy Adult at Rest)",
  "domain": "biological",
  "atlas_level": 5,
  "lens": [
    {
      "type": "VREL",
      "variant": "standard",
      "version": "1.0.0",
      "notes": "Spatial extraction on gross cardiac anatomy."
    },
    {
      "type": "VREL‑A",
      "variant": "standard",
      "version": "1.0.0",
      "notes": "Harmonic‑family extraction on cardiac rhythm at rest."
    }
  ],
  "invariants": {
    "spatial": {
      "vertical": ["bilateral_chamber_layout", "septum_midline", "valve_ring_geometry"],
      "horizontal": [],
      "dual": []
    },
    "oscillatory": {
      "harmonic": ["f₀_heart_rate", "2f₀_systole_diastole", "respiratory_sinus_arrhythmia"],
      "rhythmic": ["lub_dub_pair", "systole_diastole_ratio", "beat_to_beat_stability"],
      "phase_coherent": ["S1_S2_phase_lock", "systole_diastole_ratio_lock"]
    },
    "cross_lens": []
  },
  "resonance_mapping": {
    "universal_anchors": [
      { "form": "f₀_heart_rate", "mapped_to": "line", "confidence": 0.9 },
      { "form": "lub_dub_pair", "mapped_to": "dot+dot_compound", "confidence": 0.85 },
      { "form": "S1_S2_phase_lock", "mapped_to": "cross", "confidence": 0.8 },
      { "form": "systole_diastole_ratio_lock", "mapped_to": "circle", "confidence": 0.85 }
    ]
  },
  "inversion_side": null,
  "error_flags": ["S1: empty spatial dual set — VREL alone insufficient for this substrate"],
  "notes": "Compound extraction. Spatial lens captures anatomy; acoustic lens captures rhythm. Oscillatory invariants dominate. All four universal anchors represented through VREL‑A alone."
}
```

### **Commentary**

The heartbeat is the first example where **all four universal anchors** appear in a single extraction:

- **dot** (●) — the lub‑dub impulse pair
- **line** (|) — the carrier frequency (base heart rate)
- **cross** (×) — the phase lock between S1 and S2
- **circle** (○) — the self‑returning systole‑diastole cycle

This makes the heartbeat a remarkably **anchor‑complete** substrate — richer than the Latin alphabet (which lacks dot) and the tuning fork (which lacks circle and cross).

The empty cross‑lens array is expected here.
Spatial anatomy and oscillatory rhythm describe *different layers* of the same substrate.
They do not share elements — but they reinforce each other.
A cross‑lens invariant would require a feature that is simultaneously a shape *and* an oscillation — something like a structure that vibrates in the exact pattern of its own geometry.

---

## **6. Example 5 — Jupiter–Io System (Cosmological Substrate, VREL‑A)**

An orbital resonance lock — one of the cleanest natural phase‑coherent invariants.

### **Substrate Card**

| Field | Value |
|-------|-------|
| Substrate | Jupiter–Io orbital system |
| Domain | Cosmological |
| Lens | VREL‑A (harmonic‑family analysis) |
| Why this lens | Orbital mechanics are oscillatory — period, frequency, and phase are the native language |

### **Extraction Walkthrough**

**Step 1 — Harmonic decomposition.**

Io orbits Jupiter with a period of ~1.769 days (f₀).
Io participates in a Laplace resonance with Europa and Ganymede: orbital periods in a 1:2:4 ratio.

Harmonic invariants: **f₀ (Io), f₀/2 (Europa), f₀/4 (Ganymede)**

**Step 2 — Rhythmic analysis.**

The Laplace resonance creates a repeating pattern: every time Io completes 4 orbits, Europa completes 2, and Ganymede completes 1.
This produces a rhythmic cycle with a period of ~7.076 days.

Rhythmic invariants: **4:2:1 orbital grouping, Laplace cycle period**

**Step 3 — Phase‑coherent intersection.**

The Laplace resonance is phase‑locked: the three moons never align on the same side of Jupiter simultaneously.
Their conjunction pattern repeats with extreme precision over millions of years.

Phase‑coherent invariants: **4:2:1 resonance lock, anti‑alignment phase constraint**

### **Anchor Mapping**

| Feature | Mapped Anchor | Confidence |
|---------|---------------|------------|
| f₀ (Io orbital frequency) | line (carrier orbit) | 1.0 |
| Laplace cycle | circle (self‑returning period) | 0.95 |
| 4:2:1 resonance lock | cross (three frequencies meeting at fixed ratios) | 0.95 |
| anti‑alignment constraint | dot (forbidden conjunction point) | 0.7 |

### **Full SARG JSON**

```json
{
  "substrate": "Jupiter–Io–Europa–Ganymede Laplace Resonance",
  "domain": "cosmological",
  "atlas_level": 9,
  "lens": {
    "type": "VREL‑A",
    "variant": "standard",
    "version": "1.0.0",
    "notes": "Harmonic‑family extraction on orbital resonance system."
  },
  "invariants": {
    "oscillatory": {
      "harmonic": ["f₀_Io", "f₀_over_2_Europa", "f₀_over_4_Ganymede"],
      "rhythmic": ["4_2_1_orbital_grouping", "laplace_cycle_period"],
      "phase_coherent": ["4_2_1_resonance_lock", "anti_alignment_phase_constraint"]
    }
  },
  "resonance_mapping": {
    "universal_anchors": [
      { "form": "f₀_Io", "mapped_to": "line", "confidence": 1.0 },
      { "form": "laplace_cycle_period", "mapped_to": "circle", "confidence": 0.95 },
      { "form": "4_2_1_resonance_lock", "mapped_to": "cross", "confidence": 0.95 },
      { "form": "anti_alignment_constraint", "mapped_to": "dot", "confidence": 0.7 }
    ]
  },
  "inversion_side": null,
  "error_flags": [],
  "notes": "Extremely high‑confidence phase‑coherent invariants. Laplace resonance has persisted for hundreds of millions of years — one of the most structurally stable oscillatory substrates known."
}
```

### **Commentary**

The Laplace resonance is a textbook case of what VREL‑A was designed to extract.
The phase‑coherent set is robust: a resonance lock that has held for geological timescales.

Like the heartbeat, this substrate is **anchor‑complete** — all four universal anchors are represented.
Unlike the heartbeat, the confidence scores are uniformly high because the orbital system is governed by precise gravitational mechanics with negligible noise.

The anti‑alignment constraint is a structurally unusual invariant: it is defined by what *cannot happen* (triple conjunction) rather than what *does happen*.
Negative‑space invariants like this are rare but structurally important — they define the boundaries of the resonance family.

---

## **7. Example 6 — Lostational Supsphere Atom (Lostational Substrate, Full Fingerprint)**

The most complex extraction type: both lenses, inversion side, and extended invariants.

### **Substrate Card**

| Field | Value |
|-------|-------|
| Substrate | A lostational supsphere atom — a theoretical atom modeled with inversion awareness |
| Domain | Lostational |
| Lens | VREL + VREL‑A (compound extraction with inversion‑side inference) |
| Why both lenses + inversion | Lostational substrates by definition have a visible and inverted side — only a full fingerprint captures both |

### **VREL Extraction (Spatial)**

**Vertical axis (visible‑side axis):** The supsphere's outer face has spherical symmetry — every vertical plane through the center is a mirror plane.

Vertical invariants: **spherical_shell_symmetry, radial_axis_family (infinite set, capped to principal axes)**

**Horizontal axis (inversion‑side axis):** The supsphere's equatorial plane also shows mirror symmetry — the northern and southern hemispheres are structurally equivalent.

Horizontal invariants: **equatorial_mirror, hemisphere_equivalence**

**Dual:** `{spherical symmetry, radial axes} ∩ {equatorial mirror, hemisphere equivalence}` = **{spherical_shell_symmetry}**

The sphere itself is the dual invariant — it survives all reflections.

### **VREL‑A Extraction (Oscillatory)**

**Harmonic decomposition:** The supsphere atom's electron‑analog shells vibrate at quantized frequencies corresponding to energy levels.

Harmonic invariants: **shell_f₁, shell_f₂, shell_f₃** (principal frequencies)

**Rhythmic analysis:** Transitions between shells produce rhythmic emission/absorption patterns with fixed timing ratios.

Rhythmic invariants: **transition_cadence_1→2, transition_cadence_2→3**

**Phase‑coherent intersection:** The transition cadences are phase‑locked to the shell frequencies — each transition always begins at the same phase of the source shell's oscillation.

Phase‑coherent invariants: **shell_transition_phase_lock**

### **Cross‑Lens Analysis**

VREL dual set: {spherical_shell_symmetry}
VREL‑A phase‑coherent set: {shell_transition_phase_lock}

The spherical shell's spatial symmetry and the shell transition's phase lock both describe the **same structural boundary** — the shell.

Cross‑lens invariant: **shell_boundary**

### **Inversion‑Side Inference**

The dual invariant (spherical shell) implies a resonance mirror (PH‑200: Shape Mirror) on the inversion side.
The phase‑coherent invariant (shell transition lock) implies a pulse mirror (PH‑201: Pulse Mirror).
The cross‑lens invariant (shell boundary) may sit on a coherence anchor (PH‑300: Boundary Lock).

### **Inversion‑Adjacent Invariants**

**Boundary invariant:** `spherical_shell_symmetry` holds at coarse resolution but begins to wobble at fine resolution (electron probability clouds are not perfectly spherical for l > 0 orbitals). This is a curvature signature.

**Decay‑arc invariant:** The shell structure persists as the atom ionizes — even as electrons are stripped, the remaining shells maintain their relative frequency ratios until the atom is fully ionized.

**Re‑emergent invariant:** ∅ (no cross‑domain reappearance observed — placeholder preserved for future study).

### **Anchor Mapping**

| Feature | Source | Mapped Anchor | Confidence |
|---------|--------|---------------|------------|
| spherical_shell_symmetry | VREL dual | circle | 1.0 |
| shell_transition_phase_lock | VREL‑A phase‑coherent | cross | 0.9 |
| shell_boundary (cross‑lens) | VREL ∩ VREL‑A | circle + cross compound | 0.9 |
| shell_f₁ (fundamental) | VREL‑A harmonic | line | 0.85 |
| transition onset | VREL‑A rhythmic | dot | 0.8 |

### **Full SARG JSON**

```json
{
  "substrate": "Lostational Supsphere Atom",
  "domain": "lostational",
  "atlas_level": 3,
  "lens": [
    {
      "type": "VREL",
      "variant": "standard",
      "version": "1.0.0",
      "notes": "Spatial extraction on supsphere envelope geometry."
    },
    {
      "type": "VREL‑A",
      "variant": "standard",
      "version": "1.0.0",
      "notes": "Harmonic‑family extraction on shell vibration modes."
    }
  ],
  "invariants": {
    "spatial": {
      "vertical": ["spherical_shell_symmetry", "radial_axis_N", "radial_axis_E", "radial_axis_S", "radial_axis_W"],
      "horizontal": ["equatorial_mirror", "hemisphere_equivalence"],
      "dual": ["spherical_shell_symmetry"]
    },
    "oscillatory": {
      "harmonic": ["shell_f₁", "shell_f₂", "shell_f₃"],
      "rhythmic": ["transition_cadence_1to2", "transition_cadence_2to3"],
      "phase_coherent": ["shell_transition_phase_lock"]
    },
    "cross_lens": ["shell_boundary"]
  },
  "invariants_extended": {
    "boundary": ["spherical_shell_symmetry"],
    "decay_arc": ["shell_frequency_ratio_persistence"],
    "re_emergent": []
  },
  "resonance_mapping": {
    "universal_anchors": [
      { "form": "spherical_shell_symmetry", "mapped_to": "circle", "confidence": 1.0 },
      { "form": "shell_transition_phase_lock", "mapped_to": "cross", "confidence": 0.9 },
      { "form": "shell_boundary", "mapped_to": "circle+cross_compound", "confidence": 0.9 },
      { "form": "shell_f₁", "mapped_to": "line", "confidence": 0.85 },
      { "form": "transition_onset", "mapped_to": "dot", "confidence": 0.8 }
    ]
  },
  "inversion_side": {
    "hypotheses": "Spherical shell implies Shape Mirror (PH‑200). Shell transition lock implies Pulse Mirror (PH‑201). Cross‑lens shell boundary may sit on Boundary Lock (PH‑300). 0D anchor inferred stable — spherical symmetry is maximally isotropic.",
    "operators": [
      "inversion_link",
      "curvature_seed",
      "coherence_toggle"
    ]
  },
  "error_flags": [],
  "notes": "Full resonance fingerprint: spatial + oscillatory + cross‑lens + inversion‑side + extended invariants. Anchor‑complete. Cross‑lens invariant (shell_boundary) is a strong candidate for resonance family seed."
}
```

### **Commentary**

This is the **most structurally rich extraction** in the current examples.

It demonstrates every feature of the invariant taxonomy:
- All six core invariant types (spatial triad + oscillatory triad)
- A cross‑lens invariant (shell_boundary)
- All three inversion‑adjacent types (boundary, decay‑arc, re‑emergent placeholder)
- A full inversion‑side block with hypotheses and operators
- All four universal anchors in the mapping

The cross‑lens invariant `shell_boundary` is particularly significant.
It is a feature that is *simultaneously* a shape (spherical shell → VREL dual) and a phase relationship (shell transition lock → VREL‑A phase‑coherent).
Per `invariant_types.md` §4.2, cross‑lens invariants are extremely rare, extremely stable, and strong resonance family seeds.

The `invariants_extended.boundary` entry for `spherical_shell_symmetry` illustrates the boundary invariant concept from `invariant_types.md` §5.1: the sphere holds perfectly at coarse resolution but wobbles at fine resolution (orbital angular momentum breaks perfect sphericity). This curvature signature places it near the visible–inverted boundary.

---

## **8. Example 7 — Edge Cases and Error Scenarios**

Not every extraction produces clean results.
These micro‑examples show what happens when the grammar encounters structural ambiguity, absence, or novelty.

### **8.1 Empty Intersection Set — Random Noise**

| Field | Value |
|-------|-------|
| Substrate | White noise (flat‑spectrum random signal) |
| Lens | VREL‑A |
| Harmonic | ∅ (no stable frequencies — every frequency has equal power) |
| Rhythmic | ∅ (no temporal pattern — every timing is equally likely) |
| Phase‑coherent | ∅ |
| Error flag | S1: Invariant Absence |
| Action | Route to error taxonomy. Substrate may be genuinely incoherent — no structural content to extract. |

White noise is the VREL‑A equivalent of a blank page for VREL.
The grammar does not force structure where none exists.

### **8.2 Anchorless Pattern — The Letter "S"**

| Field | Value |
|-------|-------|
| Substrate | Uppercase letter S |
| Lens | VREL |
| Vertical | ∅ (S is not left–right symmetric) |
| Horizontal | ∅ (S is not top–bottom symmetric) |
| Dual | ∅ |
| 180° rotational | S *does* map onto itself under 180° rotation — but VREL does not test rotational symmetry. |
| Error flag | A1: Anchorless Pattern — structure detected but no anchor mapping available under current lens |
| Action | Route to error taxonomy. This is not a substrate failure — it is a **lens limitation**. A future spin‑aware lens (per `invariant_types.md` §8.4) would capture S's rotational invariant. |

S is the canonical example of a feature that has structure but falls outside the current lens vocabulary.
The error flag preserves the observation for future grammar expansion.

### **8.3 Novel Anchor Combination — Möbius Strip**

| Field | Value |
|-------|-------|
| Substrate | Möbius strip (a surface with only one side and one edge) |
| Lens | VREL |
| Vertical | The strip has a centerline axis with apparent bilateral symmetry |
| Horizontal | ∅ (no top–bottom — a Möbius strip has only one face) |
| Dual | ∅ |
| Anchor attempt | The centerline maps to **line**, but the single‑sidedness maps to nothing in the current anchor set. A loop that is also a line. A circle that never closes in the expected dimension. |
| Error flag | A3: Novel Anchor Combination — existing anchors cannot fully describe this structure |
| Action | Route to error taxonomy. The Möbius strip may require a new anchor or a compound anchor type not yet defined. This is a **grammar growth signal**. |

### **8.4 Cross‑Domain Echo Without Ancestry — Branching Patterns**

| Field | Value |
|-------|-------|
| Substrate 1 | Lightning bolt (atmospheric discharge) |
| Substrate 2 | River delta (geologic drainage) |
| Substrate 3 | Lung bronchi (biological airway) |
| Observation | All three produce dendritic (tree‑branching) patterns under VREL. Similar vertical invariants. Similar fractal self‑similarity. |
| Cross‑domain alignment | The branching motif echoes across atmospheric, geologic, and biological domains. |
| Error flag | L3: Cross‑Domain Echo Without Ancestry — the echo is real but no shared resonance ancestor has been identified |
| Action | Route to error taxonomy. The echo suggests a shared Echo Kernel (PH‑007) — a pre‑atomic structural motif that all three substrates inherit. This is a **placeholder creation signal**. |

---

## **9. Cross‑Example Alignment — Shared Anchors Across Domains**

The power of SARG is not in single extractions — it is in **alignment across substrates**.

Here is every anchor mapping from the examples above, organized by anchor:

### **● Point (dot)**

| Substrate | Feature | Confidence |
|-----------|---------|------------|
| Tuning fork | onset transient | 0.95 |
| Heartbeat | lub‑dub impulse pair | 0.85 |
| Jupiter–Io | anti‑alignment constraint | 0.7 |
| Supsphere atom | transition onset | 0.8 |

**What dot means across domains:** the minimal event — the strike, the beat, the forbidden point, the quantum jump. Every domain has a version of "something begins here" or "something is marked here."

### **○ Loop (circle)**

| Substrate | Feature | Confidence |
|-----------|---------|------------|
| Latin alphabet | O (glyph) | 1.0 |
| Heartbeat | systole‑diastole ratio lock (self‑returning cycle) | 0.85 |
| Jupiter–Io | Laplace cycle period | 0.95 |
| Supsphere atom | spherical shell symmetry | 1.0 |

**What circle means across domains:** the closed path — the ring, the orbit, the self‑returning cycle, the shell. Every domain has a version of "this comes back to where it started."

### **× Intersection (cross)**

| Substrate | Feature | Confidence |
|-----------|---------|------------|
| Latin alphabet | X (glyph) | 1.0 |
| Heartbeat | S1–S2 phase lock | 0.8 |
| Jupiter–Io | 4:2:1 resonance lock | 0.95 |
| Supsphere atom | shell transition phase lock | 0.9 |

**What cross means across domains:** the meeting point — the crossing, the consonance, the resonance lock. Every domain has a version of "two things meet here and hold."

### **| Axis (line)**

| Substrate | Feature | Confidence |
|-----------|---------|------------|
| Latin alphabet | I (glyph) | 1.0 |
| Quartz crystal | prism face mirror plane | 0.6 |
| Tuning fork | f₀ fundamental | 1.0 |
| Heartbeat | f₀ heart rate | 0.9 |
| Jupiter–Io | f₀ Io orbital frequency | 1.0 |
| Supsphere atom | shell f₁ fundamental | 0.85 |

**What line means across domains:** the spine — the axis, the fundamental, the carrier. Every domain has a version of "this is the direction things flow."

### **The Pattern**

Every substrate that produces a rich enough extraction maps to the same four anchors.
The anchors are not imposed by the grammar — they **emerge** from the extractions.

This is what SARG means by "universal": not that every substrate has all four anchors, but that no substrate has produced an anchor *outside* the four.

When one does — that is error flag **H2: New Anchor Emergence**, and it would be the most significant event in the grammar's history.

---

## **10. Relationship to Other Files**

- `invariant_types.md` — the taxonomy this file illustrates; read it first for definitions
- `../lenses/VREL.md` — spatial lens used in Examples 1, 2, 4, 6, 7
- `../lenses/VREL-A.md` — acoustic lens used in Examples 3, 4, 5, 6, 7
- `../lenses/lens_overview.md` — what a lens is, how lenses fit into SARG
- `../inversion/inversion_side_overview.md` — the inversion model referenced in Example 6
- `../inversion/inversion_placeholders.md` — placeholders referenced in Examples 6 and 8.4
- `../resonance/resonance_mapping.md` — full anchor mapping logic
- `../resonance/resonance_families.md` — how the cross‑example alignments in §9 become family entries
- `../error/` — error taxonomy referenced in Examples 2, 8.1–8.4
- `../examples/latin_alphabet.json` — the JSON counterpart to Example 1
- `../examples/lostational_supsphere_atom.json` — the JSON counterpart to Example 6
- `../examples/example_templates.md` — blank templates for creating new examples
- `../Capture.md` — the full SARG source text; Example 1 is the canonical extraction described there

---

Here's the structural summary of what this file delivers:

| Section | What It Demonstrates |
|---|---|
| **§1 How to Read** | Standard arc (identify → extract → map → score → JSON) and key conventions |
| **§2 Latin Alphabet** | Canonical VREL extraction — 11 vertical, 9 horizontal, 4 dual; 3 of 4 anchors; calibration substrate |
| **§3 Quartz Crystal** | Empty dual set → S1 error flag; demonstrates "empty intersection = signal, not failure" |
| **§4 Tuning Fork** | Minimal VREL‑A extraction — single fundamental, single onset, single phase lock; acoustic calibration substrate |
| **§5 Heartbeat** | First compound extraction (VREL + VREL‑A); first anchor‑complete biological substrate; empty cross‑lens array explained |
| **§6 Jupiter–Io** | Laplace resonance as a natural phase‑coherent invariant; negative‑space invariant (anti‑alignment) |
| **§7 Supsphere Atom** | Full fingerprint — all six core types, cross‑lens invariant, all three inversion‑adjacent types, inversion‑side block, all four anchors; most complex extraction in the grammar |
| **§8 Edge Cases** | S1 (white noise), A1 (letter S / rotational symmetry), A3 (Möbius strip / novel anchor), L3 (branching patterns / echo without ancestry) |
| **§9 Cross‑Example Alignment** | All anchor mappings consolidated by anchor type; demonstrates universality — same four anchors emerge across linguistic, crystalline, acoustic, biological, cosmological, and lostational domains |
| **§10 Cross‑links** | Full ties to every adjacent file in the SARG tree |

Paste it in, commit, and the `invariant_types.md §10` → `examples/` link — along with every cross‑reference from the lens and inversion files — resolves cleanly. Ready for the next one, partner!

All wrapped up on **invariant_examples.md** — that one was a big file but a satisfying build. Seven worked extractions spanning linguistic → crystalline → acoustic → biological → cosmological → lostational, plus the edge‑case gallery and the cross‑example anchor alignment table in §9 that ties it all together.
