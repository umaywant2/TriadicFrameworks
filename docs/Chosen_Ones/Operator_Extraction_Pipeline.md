# Operator Extraction Pipeline

**Module:** Chosen Ones | **RTT Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

This pipeline converts clean transcript text (output of `Transcript_Ingestion_Pipeline.md`) into a structured RTT operator manifest. The pipeline has five stages: Segmentation, Classification, Operator Binding, Paradox Resolution, and Manifest Assembly.

---

## Pipeline Overview

```
[CLEAN TRANSCRIPT]
        ↓
  STAGE 1: SEGMENTATION
  Split into functional utterance units (FUUs)
        ↓
  STAGE 2: CLASSIFICATION
  Assign each FUU to S–N–R zone + SET layer + DCO stage
        ↓
  STAGE 3: OPERATOR BINDING
  Map each classified FUU to one or more RTT operators
        ↓
  STAGE 4: PARADOX RESOLUTION
  Identify structural paradoxes; resolve via operator algebra
        ↓
  STAGE 5: MANIFEST ASSEMBLY
  Output structured JSON operator manifest
        ↓
[RTT OPERATOR MANIFEST]
```

---

## Stage 1 — Segmentation into Functional Utterance Units (FUUs)

A **Functional Utterance Unit (FUU)** is the minimal transcript segment that performs a single structural function. FUUs are not sentences — they are semantic units.

### Segmentation Rules

1. **Split on structural function change**, not punctuation. A speaker may deliver one FUU across three sentences.
2. **Merge run-on fragments** that share a single structural function (e.g., a list of noise examples is one FUU).
3. **Preserve speaker emphasis markers** — repetition, cadence breaks, and rhetorical questions are segmentation boundaries.
4. **Minimum FUU length:** 8 words. Fragments below this threshold are merged with adjacent FUU.
5. **Tag each FUU** with: `[FUU_ID]`, `[TIMESTAMP_RANGE]`, `[RAW_TEXT]`, `[WORD_COUNT]`

### Example Segmentation

**Raw transcript excerpt:**
> "You've been in rooms where you were the smartest person and no one saw it. You built things in silence. You outlasted people who had every advantage. And you're still here. That is not luck. That is architecture."

**FUU Output:**
```
FUU-001 | 00:00–00:12 | "You've been in rooms where you were the smartest person and no one saw it." | 16w
FUU-002 | 00:12–00:16 | "You built things in silence." | 5w → MERGE WITH FUU-003
FUU-003 | 00:16–00:23 | "You outlasted people who had every advantage." | 8w → MERGED: FUU-002+003
FUU-004 | 00:23–00:27 | "And you're still here." | 4w → MERGE WITH FUU-005
FUU-005 | 00:27–00:33 | "That is not luck. That is architecture." | 7w → MERGED: FUU-004+005
```

---

## Stage 2 — Classification

Each FUU receives three classification tags:

| Tag Type | Options | Assignment Logic |
|---|---|---|
| `snr_zone` | `silence`, `noise`, `resonance` | Dominant structural function (see Triadic_Substrate_Map.md §1) |
| `set_layer` | `substrate`, `envelope`, `threshold` | What dimension of transformation the FUU addresses (see §2) |
| `dco_stage` | `0D`, `1D`, `3D`, `8D`, `9D` | Dimensional signature of the experience described (see §3) |
| `intensity` | `0.0–1.0` | Estimated activation strength; 1.0 = maximum compression or release |

### Classification Heuristics

**SNR Zone Assignment:**
- Does the FUU *acknowledge latent state without directing action?* → `silence`
- Does the FUU *name, isolate, or dismiss incoherent perturbation?* → `noise`
- Does the FUU *describe or transmit coherent expression?* → `resonance`

**SET Layer Assignment:**
- Does the FUU address *who the person is fundamentally?* → `substrate`
- Does the FUU address *timing, context, or the environment's readiness?* → `envelope`
- Does the FUU address *the crossing event itself or its cost?* → `threshold`

**DCO Stage Assignment:**
- Undeniable-self / pre-expression content → `0D`
- Path, trajectory, long arc → `1D`
- Embodied field, magnetic presence, room effect → `3D`
- Recognition moment, field reorganization → `8D`
- Destiny, ancestry, purpose-as-given → `9D`

### Example Classification
```
FUU-001: snr_zone=silence, set_layer=substrate, dco_stage=0D, intensity=0.85
FUU-002+003: snr_zone=silence, set_layer=substrate, dco_stage=1D, intensity=0.70
FUU-004+005: snr_zone=resonance, set_layer=threshold, dco_stage=8D, intensity=0.95
```

---

## Stage 3 — Operator Binding

Each classified FUU is bound to one **primary operator** and zero or more **secondary operators** from the RTT family.

### Binding Decision Table

| SNR Zone | SET Layer | DCO Stage | Primary Operator | Secondary Operators |
|---|---|---|---|---|
| silence | substrate | 0D | `QMROOT(0D)` | `E_a` |
| silence | substrate | 1D | `A_τ(t_past, t_now)` | `∇_τ`, `R_anc` |
| silence | envelope | 1D | `D_δ` | `S_coh` |
| noise | any | any | `D_δ` | `∇_cross` |
| resonance | substrate | 3D | `∇_cross` | `C_R` |
| resonance | envelope | 3D | `C_R` | `Φ_lock` |
| resonance | threshold | 8D | `A_θ` | `Φ_lock`, `Ir` |
| resonance | substrate | 9D | `∂_anc` | `R_anc`, `ε_ij` |
| silence→resonance | threshold | 1D→3D | `A_θ` | `E_a`, `Ir` |

### Operator Binding Format
```json
{
  "fuu_id": "FUU-001",
  "primary_operator": "QMROOT(0D)",
  "secondary_operators": ["E_a"],
  "operator_note": "Subject's unseen intelligence constitutes the 0D identity kernel; the gap between capacity and recognition quantifies E_a"
}
```

---

## Stage 4 — Paradox Resolution

Run a paradox scan on the full FUU set. A paradox is flagged when two FUUs in the same transcript bind to operators that appear to contradict each other structurally.

### Paradox Detection Rules

1. **Simultaneity paradox:** Same subject assigned both `QMROOT(0D)` (no-expression) and `C_R` (active coupling) — apparent contradiction.
   - **Resolution:** `QMROOT(0D)` governs the substrate layer; `C_R` governs the envelope layer. Different layers are non-contradictory.

2. **Temporal paradox:** `A_τ(past, now)` and `∂_anc` both claim origin of identity.
   - **Resolution:** `A_τ` is experiential integration; `∂_anc` is archetypal pull. These are additive, not competing.

3. **Activation paradox:** `D_δ` (do not chase) and `A_θ` (cross the threshold) appear to conflict.
   - **Resolution:** `D_δ` applies to *external validation*; `A_θ` applies to *internal commitment*. Directionality is orthogonal.

4. **Stillness/impact paradox:** `S_coh` (maintain coherence quietly) and `∇_cross` (field leaks outward) appear passive vs. active.
   - **Resolution:** `S_coh` is the cause; `∇_cross` is the effect. No conflict — this is the core Chosen One mechanic.

### Paradox Resolution Output
```json
{
  "paradox_id": "P-001",
  "type": "simultaneity",
  "fuu_ids": ["FUU-001", "FUU-007"],
  "operators": ["QMROOT(0D)", "C_R"],
  "resolution": "Layer separation: 0D governs substrate identity; C_R governs envelope coupling. Non-contradictory.",
  "resolved": true
}
```

---

## Stage 5 — Manifest Assembly

The full operator manifest is assembled as a structured JSON document.

### Manifest Schema
```json
{
  "manifest_id": "CO-MANIFEST-[VIDEO_ID]",
  "rtt_context": "rtt=1 | coherence=declared | drift=bounded | paradox=structural",
  "source_url": "[YouTube URL]",
  "source_title": "[Video Title]",
  "processed_at": "[ISO 8601 timestamp]",
  "fuu_count": 0,
  "snr_distribution": {
    "silence": 0.0,
    "noise": 0.0,
    "resonance": 0.0
  },
  "set_distribution": {
    "substrate": 0.0,
    "envelope": 0.0,
    "threshold": 0.0
  },
  "dco_distribution": {
    "0D": 0.0, "1D": 0.0, "3D": 0.0, "8D": 0.0, "9D": 0.0
  },
  "dominant_archetype": "[from Triadic_Substrate_Map.md §4]",
  "primary_operator_set": [],
  "paradoxes_detected": 0,
  "paradoxes_resolved": 0,
  "fuu_manifest": [],
  "actionable_outputs": {
    "reframe_prompt": "",
    "activation_scaffold": "",
    "drift_corrector": "",
    "agent_hook": ""
  }
}
```

### Manifest Quality Checks
- `snr_distribution` values must sum to `1.0` (±0.02 tolerance)
- `paradoxes_resolved` must equal `paradoxes_detected` (drift=bounded enforcement)
- `dominant_archetype` must map to a row in `Triadic_Substrate_Map.md §4`
- At least one `primary_operator` must come from the Activation family (module design constraint)
