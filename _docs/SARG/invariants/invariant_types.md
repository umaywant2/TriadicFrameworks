# **Invariant Types — Classification**

*The taxonomy of everything that persists.*

An invariant is a pattern that survives a defined transformation.
Mirror it, stretch it, decompose it, decay it — if the pattern remains, it is an invariant.

Invariants are the atomic currency of SARG.
Lenses extract them from substrates.
The grammar aligns them across domains.
The Resonance Atlas organizes them into families and lineage.

This file classifies **every type of invariant** that SARG currently recognizes, defines their properties, describes how they relate to each other, and explains how new invariant types enter the grammar.

---

## **1. What Makes Something an Invariant**

A feature qualifies as a SARG invariant when it meets three criteria:

1. **Persistence** — it survives at least one defined transformation.
2. **Extractability** — at least one lens can detect and return it.
3. **Anchor‑mappability** — it can be mapped (even tentatively) to a universal resonance anchor (● ○ × |).

Features that satisfy (1) and (2) but not (3) are classified as **anchorless** and routed to the SARG error taxonomy (A1: Anchorless Pattern).

Features that satisfy none are **noise** — not invariants, not errors, just substrate weather.

---

## **2. The Two Invariant Families**

SARG currently recognizes two invariant families, one per lens.
Each family contains a primary set, a secondary set, and an intersection set.

### **2.1 Spatial Invariants (VREL)**

Extracted by mirror‑axis analysis. The lens reflects the substrate across spatial axes and records what survives.

| Type | Transformation Survived | Set Role |
|------|------------------------|----------|
| **Vertical** | Reflection across a vertical axis | Primary set |
| **Horizontal** | Reflection across a horizontal axis | Secondary set |
| **Dual** | Reflection across *both* axes simultaneously | Intersection set |

### **2.2 Oscillatory Invariants (VREL‑A)**

Extracted by harmonic‑family analysis. The lens decomposes the substrate into frequency and rhythm and records what survives.

| Type | Transformation Survived | Set Role |
|------|------------------------|----------|
| **Harmonic** | Frequency decomposition | Primary set |
| **Rhythmic** | Temporal pattern analysis | Secondary set |
| **Phase‑coherent** | Simultaneous frequency *and* rhythm decomposition | Intersection set |

### **2.3 The Parallel Structure**

Both families share the same triadic shape:

```
Primary set ∩ Secondary set = Intersection set
```

- VREL: `vertical ∩ horizontal = dual`
- VREL‑A: `harmonic ∩ rhythmic = phase_coherent`

The intersection set always contains the **most structurally stable** elements in the substrate.
It is the first candidate for resonance anchor mapping.
It is the closest visible‑side structure to the 0D anchor.

---

## **3. Detailed Type Definitions**

### **3.1 Vertical Invariants**

**Lens:** VREL
**Transformation:** Reflection across a vertical (left–right) axis.
**What survives:** Any feature whose left half mirrors its right half.

| Substrate | Example Vertical Invariants |
|-----------|-----------------------------|
| Linguistic | A, H, I, M, O, T, U, V, W, X, Y |
| Geometric | Shapes with bilateral vertical symmetry |
| Crystalline | Planes of vertical mirror symmetry |
| Symbolic | Operators or tokens with left–right equivalence |
| Biological | Sagittal‑plane mirror structures |
| Cosmological | Polar‑axis symmetry shells |
| Lostational | Visible‑side axis features |

**JSON key:** `"vertical"`
**Typical set size:** Largest of the three VREL sets.

---

### **3.2 Horizontal Invariants**

**Lens:** VREL
**Transformation:** Reflection across a horizontal (top–bottom) axis.
**What survives:** Any feature whose top half mirrors its bottom half.

| Substrate | Example Horizontal Invariants |
|-----------|-------------------------------|
| Linguistic | B, C, D, E, H, I, K, O, X |
| Geometric | Shapes with bilateral horizontal symmetry |
| Acoustic | Waveforms with top–bottom amplitude symmetry |
| Biological | Transverse‑plane mirror structures |
| Cosmological | Equatorial‑plane symmetry shells |
| Lostational | Inversion‑side axis features |

**JSON key:** `"horizontal"`
**Typical set size:** Smaller than or overlapping with the vertical set.

---

### **3.3 Dual Invariants**

**Lens:** VREL
**Transformation:** Simultaneous reflection across *both* vertical and horizontal axes.
**What survives:** Features with full bilateral symmetry — the most structurally stable spatial elements.

| Substrate | Example Dual Invariants |
|-----------|-------------------------|
| Linguistic | H, I, O, X |
| Geometric | Circles, squares, regular even‑order polygons |
| Crystalline | Highly symmetric unit cells |
| Cosmological | Isotropic structures (spherical shells, uniform fields) |
| Lostational | Structures stable across the visible–inverted boundary |

**JSON key:** `"dual"`
**Typical set size:** Smallest of the three VREL sets — always ⊆ vertical ∩ horizontal.

**Stability rule:**
> If an element appears in the dual set, it is guaranteed to persist under any single‑axis transformation.
> Dual invariants are the **spatial anchoring layer** of the substrate.

---

### **3.4 Harmonic Invariants**

**Lens:** VREL‑A
**Transformation:** Frequency decomposition (Fourier‑like spectral analysis).
**What survives:** Frequency components that remain stable across the substrate's spectrum.

| Substrate | Example Harmonic Invariants |
|-----------|-----------------------------|
| Acoustic | Fundamental frequency (f₀), dominant overtones (2f₀, 3f₀, 5f₀), formant peaks |
| Biological | Heartbeat base rate, respiratory cadence, circadian period |
| Crystalline | Lattice vibration modes (phonon frequencies) |
| Cosmological | Orbital resonance ratios, pulsar spin frequencies |
| Linguistic | Vowel formants, prosodic pitch contours |

**JSON key:** `"harmonic"`
**Typical set size:** Largest of the three VREL‑A sets.

---

### **3.5 Rhythmic Invariants**

**Lens:** VREL‑A
**Transformation:** Temporal pattern analysis (timing independent of pitch).
**What survives:** Patterns whose timing structure remains stable when frequency content is removed.

| Substrate | Example Rhythmic Invariants |
|-----------|-----------------------------|
| Acoustic | Beat patterns, meter signatures, rhythmic groupings |
| Biological | Gait cycles, peristaltic rhythms, firing‑burst intervals |
| Geological | Tidal periodicities, eruption intervals, seismic recurrence |
| Cosmological | Orbital periods, rotation–revolution ratios |
| Symbolic | Repetition intervals, sequence cadences |

**JSON key:** `"rhythmic"`
**Typical set size:** Smaller than or overlapping with the harmonic set.

---

### **3.6 Phase‑Coherent Invariants**

**Lens:** VREL‑A
**Transformation:** Simultaneous frequency *and* rhythm decomposition.
**What survives:** Features whose phase relationships remain locked across both axes.

| Substrate | Example Phase‑Coherent Invariants |
|-----------|-----------------------------------|
| Acoustic | Consonant intervals, stable overtone‑to‑fundamental ratios |
| Biological | Synchronized oscillators (firefly flash sync, neural coherence) |
| Crystalline | Phonon modes maintaining phase across grain boundaries |
| Cosmological | Orbital resonance locks (e.g., Jupiter–Io 4:1) |
| Lostational | Resonance shells maintaining coherence across the visible–inverted boundary |

**JSON key:** `"phase_coherent"`
**Typical set size:** Smallest of the three VREL‑A sets — always ⊆ harmonic ∩ rhythmic.

**Coherence stability rule:**
> If an element appears in the phase‑coherent set, it is guaranteed to persist under any single‑axis transformation (frequency shift or tempo change alone).
> Phase‑coherent invariants are the **oscillatory anchoring layer** of the substrate.

---

## **4. Compound and Cross‑Lens Invariant Types**

When both VREL and VREL‑A are applied to the same substrate, their outputs can be combined to produce richer invariant types.

### **4.1 Full Resonance Fingerprint**

The combination of both intersection sets:

```
dual (VREL) + phase_coherent (VREL‑A) = full resonance fingerprint
```

This is the substrate's most structurally stable signature — the features that survive both spatial reflection and oscillatory decomposition simultaneously.

On lostational substrates, this fingerprint captures both **dimensional shape** (VREL) and **dimensional pulse** (VREL‑A).

### **4.2 Cross‑Lens Alignment Invariants**

When an element appears in **both** lens outputs — e.g., a feature that is simultaneously a VREL dual invariant and a VREL‑A phase‑coherent invariant — it is classified as a **cross‑lens invariant**.

Cross‑lens invariants are:

- Extremely rare
- Extremely stable
- Strong candidates for universal anchor mapping with confidence ≥ 0.9
- Potential resonance family seeds

### **4.3 Compound JSON Shape**

When both lenses are applied, the SARG object carries both invariant blocks:

```json
"invariants": {
  "spatial": {
    "vertical": ["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y"],
    "horizontal": ["B", "C", "D", "E", "H", "I", "K", "O", "X"],
    "dual": ["H", "I", "O", "X"]
  },
  "oscillatory": {
    "harmonic": ["f₀", "2f₀", "3f₀", "5f₀"],
    "rhythmic": ["4/4 pulse", "dotted‑pair grouping", "hemiola"],
    "phase_coherent": ["f₀–2f₀ lock", "3f₀–5f₀ lock"]
  },
  "cross_lens": ["O"]
}
```

The `cross_lens` array is populated only when both lenses are applied and shared elements are detected.

---

## **5. Inversion‑Adjacent Invariant Types**

Some invariants sit near the visible–inverted boundary.
They are not on the inversion side — they are still extractable — but they exhibit properties that suggest proximity to the curvature zone or the 0D anchor.

### **5.1 Boundary Invariants**

Features that are fully extractable but show **curvature signatures** — early signs that the structure is beginning to bend toward inversion.

**Detection:** A dual or phase‑coherent invariant that holds perfectly but whose confidence score decreases when the lens resolution is increased. The feature is stable at coarse resolution but begins to wobble at fine resolution.

**Significance:** Boundary invariants may be sitting on a coherence anchor (see `inversion_placeholders.md`, PH‑300: Boundary Lock). They are the visible side's closest contact with the inversion side.

### **5.2 Decay‑Arc Invariants**

Features that persist along a substrate's decay arc — invariants that survive not just spatial or oscillatory transformation, but **degradation over time**.

**Detection:** Apply VREL or VREL‑A at multiple points along the decay arc. Features that remain in the intersection set at every point are decay‑arc invariants.

**Significance:** Decay‑arc invariants trace the trajectory from the visible side toward the 0D anchor. They are the structural skeleton of the substrate's aging process.

### **5.3 Re‑Emergent Invariants**

Features that disappear during decay but **reappear** in a transformed or related substrate — as if the invariant passed through 0D and came back on the visible side.

**Detection:** Cross‑domain alignment detects the same structural motif in a related substrate after the original substrate has decayed past the curvature threshold.

**Significance:** If confirmed, re‑emergent invariants would validate the `phase_bridge` operator (PH‑105) — oscillation that survives full inversion. These are the most speculative invariant type in the current taxonomy.

### **5.4 Inversion‑Adjacent JSON Shape**

Inversion‑adjacent invariants are stored in an optional extension block:

```json
"invariants_extended": {
  "boundary": ["H"],
  "decay_arc": ["O", "X"],
  "re_emergent": []
}
```

An empty `re_emergent` array is expected — it is a placeholder for future observation.

---

## **6. Invariant Properties**

Every invariant carries a set of properties that determine how it behaves in the grammar.

### **6.1 Core Properties**

| Property | Type | Description |
|----------|------|-------------|
| `form` | string | The invariant's representation in its native substrate (e.g., "H", "f₀", "4/4 pulse") |
| `type` | enum | One of: `vertical`, `horizontal`, `dual`, `harmonic`, `rhythmic`, `phase_coherent`, `cross_lens`, `boundary`, `decay_arc`, `re_emergent` |
| `lens` | string | Which lens extracted it (`VREL`, `VREL‑A`, or `both`) |
| `confidence` | float | 0.0 (speculative) to 1.0 (structurally certain) |
| `anchor` | string | Mapped universal anchor: `dot`, `circle`, `cross`, `line`, `none`, or a compound (e.g., `line+cross_hybrid`) |
| `stability` | enum | `high` (intersection set), `medium` (primary/secondary set), `low` (boundary or speculative) |

### **6.2 Set‑Theoretic Properties**

These rules hold for every extraction, regardless of lens or substrate:

1. The **intersection set** is always a subset of both the primary and secondary sets.
2. The intersection set is always the **smallest** of the three sets.
3. An element in the intersection set is **guaranteed to persist** under any single‑axis transformation.
4. An **empty intersection set** indicates low structural coherence — the substrate may require a different lens, finer resolution, or may be genuinely incoherent.
5. The intersection set contains the substrate's **strongest anchor candidates**.
6. Cross‑lens invariants (elements in both intersection sets) are the **strongest candidates of all**.

### **6.3 Confidence Scoring Rules**

| Condition | Confidence Range |
|-----------|-----------------|
| Element in intersection set, clean anchor mapping | 0.9 – 1.0 |
| Element in intersection set, compound anchor mapping | 0.7 – 0.9 |
| Element in primary or secondary set only | 0.5 – 0.7 |
| Boundary invariant (resolution‑dependent wobble) | 0.3 – 0.5 |
| Decay‑arc invariant (time‑dependent persistence) | 0.4 – 0.7 |
| Re‑emergent invariant (cross‑domain reappearance) | 0.1 – 0.3 |
| Cross‑lens invariant | 0.9 – 1.0 |

---

## **7. How Invariants Enter the Grammar**

Invariants enter the SARG grammar through three pathways:

### **7.1 Lens Extraction (Primary Pathway)**

A lens is applied to a substrate. Invariants are extracted, typed, scored, and mapped to anchors.
This is the standard pathway — it produces the six core types (vertical, horizontal, dual, harmonic, rhythmic, phase‑coherent).

### **7.2 Placeholder Promotion (Inversion Pathway)**

A placeholder in `inversion_placeholders.md` accumulates enough observational evidence to move through the lifecycle:

```
placeholder → refined → promoted → measured
```

When a placeholder reaches `measured` status, it becomes a full invariant entry in this taxonomy.
Its name persists. Its structural position persists. Only its status changes.

**Example:** If PH‑300 (Boundary Lock) is ever directly observed, it becomes a measured `boundary` invariant — the first confirmed coherence anchor in SARG.

### **7.3 Error Rectification (Discovery Pathway)**

The SARG error taxonomy identifies structural gaps:

- **S1 (Invariant Absence)** — may reveal new substrate types that require new invariant definitions.
- **A3 (Novel Anchor Combination)** — may reveal new invariant types that map to previously unknown anchor configurations.
- **L3 (Cross‑Domain Echo Without Ancestry)** — may reveal re‑emergent invariants or cross‑lens invariants that were not previously recognized.
- **H1 (New Resonance Family)** — may produce new invariant groupings that expand the taxonomy.
- **H2 (New Anchor Emergence)** — would create a new anchor target, potentially requiring a new invariant type definition.

Each discovery pathway feeds back into this file.
The taxonomy grows as the Atlas grows.

---

## **8. Invariant Type Summary**

### **8.1 Core Types (Lens‑Extracted)**

| Type | Lens | Set Role | Stability | JSON Key |
|------|------|----------|-----------|----------|
| Vertical | VREL | Primary | Medium | `spatial.vertical` |
| Horizontal | VREL | Secondary | Medium | `spatial.horizontal` |
| Dual | VREL | Intersection | High | `spatial.dual` |
| Harmonic | VREL‑A | Primary | Medium | `oscillatory.harmonic` |
| Rhythmic | VREL‑A | Secondary | Medium | `oscillatory.rhythmic` |
| Phase‑coherent | VREL‑A | Intersection | High | `oscillatory.phase_coherent` |

### **8.2 Compound Types (Cross‑Lens)**

| Type | Source | Stability | JSON Key |
|------|--------|-----------|----------|
| Cross‑lens | VREL ∩ VREL‑A intersection sets | Very high | `cross_lens` |
| Full resonance fingerprint | dual + phase‑coherent combined | Very high | (composite of both intersection sets) |

### **8.3 Inversion‑Adjacent Types**

| Type | Detection Method | Stability | JSON Key |
|------|-----------------|-----------|----------|
| Boundary | Resolution‑dependent confidence wobble | Low–Medium | `invariants_extended.boundary` |
| Decay‑arc | Multi‑point temporal extraction | Medium | `invariants_extended.decay_arc` |
| Re‑emergent | Cross‑domain post‑decay alignment | Low | `invariants_extended.re_emergent` |

### **8.4 Future Types (Planned)**

| Type | Awaiting | Depends On |
|------|----------|------------|
| Spin invariants | Spin‑aware lens development | PH‑008 (Spin Protoform), `spin_mirror` operator |
| Curved‑mirror invariants | Curved‑mirror lens variant | Curvature zone modeling beyond 1% threshold |
| Bent‑mirror invariants | Bent‑mirror lens variant | Non‑planar substrate geometry |
| Composite invariants | Multi‑substrate lens application | Stackable Unit (PH‑010) formalization |

---

## **9. Invariants and the Resonance Atlas**

Every invariant maps to a position in the Resonance Atlas through the anchor system:

| Anchor | Symbol | Geometric Root | Acoustic Root |
|--------|--------|----------------|---------------|
| Point | ● | Dot / node | Impulse / attack / onset |
| Loop | ○ | Circle / ring | Sustained tone / drone / cycle |
| Intersection | × | Cross / junction | Beating / interference / consonance |
| Axis | \| | Line / stroke | Fundamental / pitch spine / carrier wave |

Invariants with high confidence and clean anchor mappings become **resonance family members** — entries in the Atlas with identity, lineage, and cross‑domain links.

Invariants with low confidence or anchorless mappings are held in the rectification pipeline until they can be classified or dismissed.

The Atlas does not store invariants directly.
It stores **resonance signatures** — structured collections of invariants that define a substrate's identity.
This file defines what those invariants *are*.

---

## **10. Relationship to Other Files**

- `../lenses/VREL.md` — the spatial lens that produces vertical, horizontal, and dual invariants
- `../lenses/VREL-A.md` — the acoustic lens that produces harmonic, rhythmic, and phase‑coherent invariants
- `../lenses/lens_overview.md` — what a lens is, how lenses fit into SARG
- `../inversion/inversion_side_overview.md` — the inversion model; §10 references this file for "inversion‑adjacent types"
- `../inversion/inversion_placeholders.md` — the placeholder registry; §8 references this file as the destination for promoted placeholders
- `../resonance/resonance_mapping.md` — how invariants map to universal anchors
- `../resonance/resonance_families.md` — how invariants group into families
- `../error/` — error taxonomy; S‑Errors originate from invariant extraction failures; A‑Errors from anchor mapping failures; discovery pathways feed back into this taxonomy
- `../examples/` — working SARG objects demonstrating invariant sets
- `../Capture.md` — the full SARG source text, including the SARG schema, invariant JSON shapes, and the triadic decision tree

---

That's the full **invariant_types.md** — all 10 sections, ready to paste and commit. Here's a quick structural rundown of what it delivers:

**Cross‑reference resolution:**
| Inbound Link | What It Finds |
|---|---|
| VREL.md §7 → "detailed invariant classification" | §2.1 + §3.1–3.3 (spatial triad fully defined) |
| VREL‑A.md §7 → "detailed invariant classification" | §2.2 + §3.4–3.6 (oscillatory triad fully defined) |
| inversion_side_overview.md §10 → "inversion‑adjacent types" | §5 (boundary, decay‑arc, re‑emergent — all three defined with detection methods and JSON shape) |
| inversion_placeholders.md §8 → "promoted placeholders become entries here" | §7.2 (placeholder → refined → promoted → measured lifecycle, with PH‑300 example) |

**New structural contributions this file introduces:**
- **Cross‑lens invariants** (§4) — elements appearing in *both* intersection sets, the rarest and most stable type
- **Full resonance fingerprint** — dual + phase‑coherent as the substrate's deepest identity signature
- **Error‑driven discovery pathway** (§7.3) — S1, A3, L3, H1, H2 errors feeding new types back into the taxonomy
- **Confidence scoring table** (§6.3) — consistent 0.0–1.0 ranges for every invariant type
- **Future types registry** (§8.4) — spin, curved‑mirror, bent‑mirror, composite — each with dependencies traced to specific placeholders
