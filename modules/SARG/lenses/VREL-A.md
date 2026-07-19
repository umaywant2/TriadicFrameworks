# **VREL‑A — Vertical Resonance Extraction Lens (Acoustic Variant)**

*A SARG lens for extracting harmonic invariants from any substrate.*

VREL‑A is the acoustic variant of VREL.
Where VREL reads a substrate through mirror‑axis symmetry, VREL‑A reads it through **oscillatory structure** — frequency, phase, rhythm, and overtone relationships.

VREL‑A does not require the substrate to be audible.
Any substrate that carries periodic, quasi‑periodic, or oscillatory behavior can be read acoustically:
heartbeats, tidal cycles, crystal vibrations, orbital periods, neural firing patterns, stellar pulsations.

VREL‑A is substrate‑agnostic: it operates identically whether the input is a birdsong, a seismic trace, a circadian rhythm, or a pulsar envelope.

---

## **1. What VREL‑A Extracts**

VREL‑A applies harmonic‑family analysis to a substrate and returns three invariant classes:

### **1.1 Harmonic Invariants**

Features that persist across the substrate's **frequency spectrum** — the tones that remain stable when the signal is decomposed into its component frequencies.

- In acoustic substrates: fundamental frequency, dominant overtones, formant peaks
- In biological substrates: heartbeat base rate, respiratory cadence, circadian period
- In crystalline substrates: lattice vibration modes (phonon frequencies)
- In cosmological substrates: orbital resonance ratios, pulsar spin frequencies
- In linguistic substrates: vowel formants, prosodic pitch contours

### **1.2 Rhythmic Invariants**

Features that persist across the substrate's **temporal structure** — the patterns that remain stable when timing is analyzed independently of pitch.

- In acoustic substrates: beat patterns, rhythmic groupings, meter signatures
- In biological substrates: gait cycles, peristaltic rhythms, firing‑burst intervals
- In geological substrates: tidal periodicities, eruption intervals, seismic recurrence
- In cosmological substrates: orbital periods, rotation‑revolution ratios
- In symbolic substrates: repetition intervals, sequence cadences

### **1.3 Phase‑Coherent Invariants**

Features that persist when both **frequency and rhythm** are analyzed together — elements whose phase relationships remain locked across transformations.

- In acoustic substrates: consonant intervals, stable overtone‑to‑fundamental ratios
- In biological substrates: synchronized oscillators (e.g., firefly flash sync, neural coherence)
- In crystalline substrates: phonon modes that maintain phase across grain boundaries
- In cosmological substrates: orbital resonance locks (e.g., Jupiter–Io 4:1)
- In lostational substrates: resonance shells that maintain coherence across the visible–inverted boundary

Phase‑coherent invariants are the most structurally stable elements in any oscillatory substrate.
They are the strongest candidates for resonance anchor mapping.

---

## **2. How VREL‑A Behaves Across Substrates**

VREL‑A adapts its extraction logic to the substrate's native oscillatory structure.
The lens itself does not change — the **interpretation of "oscillation"** changes.

| Substrate Type | Frequency Axis | Temporal Axis | What VREL‑A Reveals |
|----------------|----------------|---------------|---------------------|
| Acoustic | Pitch / spectral peaks | Beat / rhythm | Harmonic families, consonance, timbre |
| Biological | Oscillation rate (heart, breath, neural) | Cycle duration / interval | Biorhythmic coherence, sync patterns |
| Crystalline | Phonon frequency modes | Vibration decay time | Lattice stability, thermal coherence |
| Geological | Seismic wave frequency | Recurrence interval | Tectonic rhythm, resonance cavities |
| Cosmological | Orbital / spin frequency | Period / epoch | Resonance locks, shell harmonics |
| Symbolic | Token repetition frequency | Sequence spacing | Pattern cadence, recursive structure |
| Lostational | Visible‑side oscillation | Inversion‑side echo timing | Dimensional pulse, cross‑boundary phase |

The same lens produces the same **invariant types** (harmonic, rhythmic, phase‑coherent) regardless of domain.
Only the substrate determines what those invariants *are*.

---

## **3. Invariants Produced by VREL‑A**

Every VREL‑A extraction produces a structured invariant set:

```json
"invariants": {
  "harmonic": ["f₀", "2f₀", "3f₀", "5f₀"],
  "rhythmic": ["4/4 pulse", "dotted‑pair grouping", "hemiola"],
  "phase_coherent": ["f₀–2f₀ lock", "3f₀–5f₀ lock"]
}
```

### **Properties of VREL‑A invariants**

- **Harmonic invariants** describe *what* oscillates — the frequency content.
- **Rhythmic invariants** describe *when* it oscillates — the temporal patterning.
- **Phase‑coherent invariants** are always the intersection of harmonic and rhythmic — elements locked in both dimensions simultaneously.
- The **phase‑coherent set** contains the substrate's most resonance‑stable elements.
- An empty phase‑coherent set indicates **low oscillatory coherence** — the substrate may be aperiodic, chaotic, or require a different lens resolution.

### **Coherence stability rule**

> If an element appears in the phase‑coherent set, it is guaranteed to persist under any single‑axis transformation (frequency shift or tempo change alone).
> Phase‑coherent invariants are the **anchoring layer** of the substrate.

---

## **4. Resonance Anchor Mapping**

VREL‑A invariants map to the same four universal resonance anchors as VREL, but through an acoustic interpretation:

| Anchor | Symbol | Acoustic Root | What It Represents |
|--------|--------|---------------|---------------------|
| Point | ● | Impulse / attack / onset | Minimal oscillatory event; percussive seed |
| Loop | ○ | Sustained tone / drone / cycle | Closed oscillation; self‑return; standing wave |
| Intersection | × | Beating / interference / consonance | Meeting of frequencies; harmonic crossing |
| Axis | \| | Fundamental / pitch spine / carrier wave | Directional frequency coherence; tonal anchor |

### **Mapping logic**

VREL‑A maps each phase‑coherent invariant to the anchor whose acoustic root it most closely resembles:

```json
"resonance_mapping": {
  "universal_anchors": [
    { "form": "f₀", "mapped_to": "line" },
    { "form": "f₀–2f₀ lock", "mapped_to": "circle" },
    { "form": "3f₀–5f₀ beating", "mapped_to": "cross" },
    { "form": "onset transient", "mapped_to": "dot" }
  ]
}
```

- **Pure carrier forms** (fundamental, drone, sustained tone) → map to **line**
- **Pure cyclic forms** (standing wave, looped oscillation, stable orbit) → map to **circle**
- **Pure interference forms** (beating, consonance nodes, harmonic crossing) → map to **cross**
- **Pure impulse forms** (onset, attack, percussive seed) → map to **dot**
- **Hybrid forms** (e.g., a pulsed drone) → map to compound anchors (e.g., `dot+line_hybrid`)

Forms that do not cleanly map to any anchor are classified as **anchorless** and routed to the SARG error taxonomy (see `error/`).

### **Confidence scoring**

Each mapping carries an optional confidence value (0.0–1.0):

```json
{ "form": "f₀", "mapped_to": "line", "confidence": 1.0 }
{ "form": "3f₀–5f₀ beating", "mapped_to": "cross", "confidence": 0.7 }
```

Confidence reflects how unambiguously the invariant maps to a single anchor.
Phase‑coherent invariants with high confidence are the substrate's **resonance core**.

---

## **5. VREL‑A in the SARG Object**

Every SARG object that uses VREL‑A includes a lens block:

```json
"lens": {
  "type": "VREL‑A",
  "variant": "standard",
  "version": "1.0.0",
  "notes": "Harmonic‑family resonance extraction for oscillatory substrates."
}
```

- **type** — always `VREL‑A` for this lens
- **variant** — `standard` for the base lens; future variants may include `spectral`, `rhythmic‑only`, or `phase‑locked`
- **version** — semantic version for tracking lens evolution
- **notes** — any special considerations for this extraction

---

## **6. Relationship to VREL**

VREL and VREL‑A are **complementary**, not competing.

| Dimension | VREL | VREL‑A |
|-----------|------|--------|
| Primary axis | Spatial (mirror symmetry) | Temporal (oscillatory structure) |
| Invariant source | Shape persistence under reflection | Pattern persistence under frequency/rhythm decomposition |
| Strongest on | Glyphs, geometry, crystals, symbols | Sound, biorhythm, orbits, waves, pulsations |
| Dual / phase‑coherent set | Intersection of vertical + horizontal | Intersection of harmonic + rhythmic |
| Anchor mapping | Geometric resemblance | Acoustic resemblance |

Both lenses produce the same **invariant types** (a primary set, a secondary set, and an intersection set) and map to the same **universal anchors** (● ○ × |).

On **lostational substrates**, both lenses can be applied simultaneously:
VREL reads the dimensional shape; VREL‑A reads the dimensional pulse.
Together they produce a **full resonance fingerprint** — structure + oscillation.

---

## **7. Relationship to Other Files**

- `lens_overview.md` — what a lens is, how lenses fit into SARG
- `VREL.md` — the spatial (mirror‑axis) parent lens
- `invariants/invariant_types.md` — detailed invariant classification
- `resonance/resonance_mapping.md` — full anchor mapping logic
- `resonance/resonance_families.md` — how invariants group into families
- `examples/` — working SARG objects using VREL‑A
- `error/` — what happens when VREL‑A extraction fails or produces ambiguous results

---

### What's in the file

| Section | Covers |
|---|---|
| **§1 What VREL‑A Extracts** | Harmonic, rhythmic, and phase‑coherent invariant classes with per‑substrate examples |
| **§2 Substrate Behavior** | 7‑row table showing how "oscillation" reinterprets across acoustic → lostational domains |
| **§3 Invariants Produced** | JSON shape, set‑theoretic properties, coherence‑stability rule |
| **§4 Resonance Anchor Mapping** | ● ○ × \| anchor table reframed acoustically, mapping logic, confidence scoring |
| **§5 SARG Object Block** | Lens block JSON with `VREL‑A` type and future variant roadmap |
| **§6 Relationship to VREL** | Side‑by‑side comparison table; how both lenses combine on lostational substrates for a full resonance fingerprint |
| **§7 Cross‑links** | Pointers to `VREL.md`, `invariants/`, `resonance/`, `examples/`, `error/` |

The file mirrors VREL.md's architecture so the two read as a matched pair — spatial lens and acoustic lens, same grammar, same anchors, complementary perspectives. 
