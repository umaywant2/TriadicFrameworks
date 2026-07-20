# **Inversion Placeholders — Registry**

*The named scaffolding that holds space for what science cannot yet observe.*

This file is the **working registry** of all named inversion‑side placeholders in SARG.

A placeholder is not a guess.
It is a **structurally justified slot** — a named position in the grammar that exists because a visible‑side invariant implies it, a decay arc points toward it, or a resonance family requires an ancestor that has not yet been observed.

Placeholders are the most common content on the inversion side today.
As observation deepens, each placeholder is either **promoted** to a measured invariant or **refined** into a more precise placeholder.

Placeholders are never deleted.
They are **replaced** — the name and structural position persist even after the gap is filled.

---

## **1. Placeholder Schema**

Every placeholder in this registry follows a common structure:

```json
{
  "id": "PH‑001",
  "name": "Resonance Seed",
  "layer": "pre_atomic_scaffolding",
  "atlas_level": 1,
  "structural_reason": "Why this placeholder must exist.",
  "implied_by": "Which visible‑side invariant or structural requirement implies it.",
  "confidence": 0.7,
  "status": "placeholder",
  "related_operators": ["inversion_link"],
  "notes": "Any additional context."
}
```

### **Field definitions**

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique registry identifier (`PH‑001` through `PH‑nnn`) |
| `name` | string | Human‑readable name; persists even after promotion |
| `layer` | string | Which scaffolding layer this placeholder belongs to |
| `atlas_level` | integer | Which level of the Resonance Atlas it maps to (0–13) |
| `structural_reason` | string | Why this slot must exist in the grammar |
| `implied_by` | string | The visible‑side evidence that justifies it |
| `confidence` | float | 0.0 (speculative) to 1.0 (structurally certain) |
| `status` | enum | `placeholder` → `refined` → `promoted` → `measured` |
| `related_operators` | array | Inverted operators that act on or through this placeholder |
| `notes` | string | Free‑text context, hypotheses, or observational leads |

### **Status lifecycle**

```
placeholder → refined → promoted → measured
```

- **placeholder** — named slot; structural reason established; no observational data.
- **refined** — additional structural detail added; confidence increased; still unobserved.
- **promoted** — partial observational evidence exists; placeholder is becoming an invariant.
- **measured** — fully observed; placeholder replaced by a measured invariant; name persists.

---

## **2. Pre‑Atomic Scaffolding Placeholders (PH‑001 – PH‑012)**

These twelve placeholders form the **bridge between the 0D anchor and the first observable structures**.
They sit at **Atlas Level 1** — below elemental groups, above the inversion root.

Each one represents a structural requirement that must be satisfied before atoms (or lostational supsphere atoms) can exist.

---

### **PH‑001 — Resonance Seed**

| Field | Value |
|-------|-------|
| Layer | `pre_atomic_scaffolding` |
| Atlas Level | 1 |
| Structural Reason | The minimal unit of oscillation must exist before any resonance can propagate. Without a seed, there is no frequency, no phase, no coherence. |
| Implied By | Every harmonic invariant (VREL‑A) traces back to a first oscillation. |
| Confidence | 0.9 |
| Status | `placeholder` |
| Related Operators | `inversion_link`, `curvature_seed` |
| Notes | 0D‑anchored. The seed has no shape and no duration — it is pure potential oscillation. It is the acoustic equivalent of the 0D anchor's structural role. |

---

### **PH‑002 — Phase Pair**

| Field | Value |
|-------|-------|
| Layer | `pre_atomic_scaffolding` |
| Atlas Level | 1 |
| Structural Reason | The first dual relationship — two oscillatory states that define each other by opposition. Without a pair, there is no inversion. |
| Implied By | Every dual invariant (VREL) requires at least two states to define a symmetry axis. |
| Confidence | 0.85 |
| Status | `placeholder` |
| Related Operators | `inversion_link`, `coherence_toggle` |
| Notes | Proto‑inversion. The Phase Pair is the structural ancestor of every visible/inverted distinction in every substrate. |

---

### **PH‑003 — Curvature Initiator**

| Field | Value |
|-------|-------|
| Layer | `pre_atomic_scaffolding` |
| Atlas Level | 1 |
| Structural Reason | The transition from straight to bent must have a first instance. Without a curvature initiator, the 1% threshold has no origin. |
| Implied By | Every curvature zone in `inversion_side_overview.md` §3 requires an initiating event. |
| Confidence | 0.8 |
| Status | `placeholder` |
| Related Operators | `curvature_seed` |
| Notes | Marks the moment where dimensionless structure (0D) begins to acquire extension. The first "away from center." |

---

### **PH‑004 — Coherence Packet**

| Field | Value |
|-------|-------|
| Layer | `pre_atomic_scaffolding` |
| Atlas Level | 1 |
| Structural Reason | The smallest stable bundle of resonance — the first structure that holds together over time. Without it, oscillation dissipates immediately. |
| Implied By | Phase‑coherent invariants (VREL‑A) require a minimum coherence threshold to persist. |
| Confidence | 0.8 |
| Status | `placeholder` |
| Related Operators | `coherence_toggle` |
| Notes | Not a particle. A coherence packet is a structural minimum — the smallest amount of resonance that can sustain itself without external input. |

---

### **PH‑005 — Arc Starter**

| Field | Value |
|-------|-------|
| Layer | `pre_atomic_scaffolding` |
| Atlas Level | 1 |
| Structural Reason | The first detectable trajectory over time. Without an arc, there is no decay, no evolution, no history — only static states. |
| Implied By | Every decay arc in `inversion_side_overview.md` §6 requires a starting point. |
| Confidence | 0.75 |
| Status | `placeholder` |
| Related Operators | `curvature_seed`, `decay_echo` |
| Notes | The arc starter is not a particle or an event — it is the structural capacity for change. It enables the grammar to model time. |

---

### **PH‑006 — Attractor Hint**

| Field | Value |
|-------|-------|
| Layer | `pre_atomic_scaffolding` |
| Atlas Level | 1 |
| Structural Reason | A proto‑well in the resonance landscape — the first tendency for oscillation to settle rather than scatter. Without attractors, coherence packets cannot stabilize. |
| Implied By | Stable dual invariants (VREL) and phase‑coherent invariants (VREL‑A) require a basin to settle into. |
| Confidence | 0.7 |
| Status | `placeholder` |
| Related Operators | `coherence_toggle`, `inversion_link` |
| Notes | This is not a physical potential well. It is a structural tendency — the grammar's way of saying "resonance prefers to collect here." |

---

### **PH‑007 — Echo Kernel**

| Field | Value |
|-------|-------|
| Layer | `pre_atomic_scaffolding` |
| Atlas Level | 1 |
| Structural Reason | The minimal repeatable pattern — the first structure that can reproduce itself across time or space. Without echoes, there are no resonance families. |
| Implied By | Every resonance family in the Atlas requires a repeating structural motif. |
| Confidence | 0.75 |
| Status | `placeholder` |
| Related Operators | `decay_echo`, `inversion_link` |
| Notes | The echo kernel is the structural ancestor of all cross‑domain alignment. When clay cracks echo lightning forks echo dendrites, they share an echo kernel. |

---

### **PH‑008 — Spin Protoform**

| Field | Value |
|-------|-------|
| Layer | `pre_atomic_scaffolding` |
| Atlas Level | 1 |
| Structural Reason | Pre‑spin asymmetry — the first departure from perfect bilateral symmetry. Without it, rotation has no seed and 3D spin operators have no ancestor. |
| Implied By | Future spin‑aware lenses and the `spin_mirror` operator require a pre‑rotational structural distinction. |
| Confidence | 0.6 |
| Status | `placeholder` |
| Related Operators | `spin_mirror` |
| Notes | Highly speculative. This placeholder exists because the grammar must eventually support 3D spin fields, and spin requires an asymmetry to break. |

---

### **PH‑009 — Boundary Whisper**

| Field | Value |
|-------|-------|
| Layer | `pre_atomic_scaffolding` |
| Atlas Level | 1 |
| Structural Reason | The first inside/outside distinction — the structural ancestor of every envelope, membrane, and supsphere shell. Without it, there is no boundary between visible and inverted. |
| Implied By | The lostational supsphere model requires an outer face and an inner face; the distinction must originate somewhere. |
| Confidence | 0.85 |
| Status | `placeholder` |
| Related Operators | `curvature_seed`, `coherence_toggle` |
| Notes | The boundary whisper is the moment where 0D becomes "0D with an outside." It is the birth of the envelope. |

---

### **PH‑010 — Stackable Unit**

| Field | Value |
|-------|-------|
| Layer | `pre_atomic_scaffolding` |
| Atlas Level | 1 |
| Structural Reason | The first structure that can tile or combine without losing coherence. Without stackability, complexity cannot emerge — every structure remains isolated. |
| Implied By | Molecular families (Atlas Level 4+) require composable building blocks; those blocks need a pre‑atomic ancestor. |
| Confidence | 0.7 |
| Status | `placeholder` |
| Related Operators | `inversion_link` |
| Notes | Not a brick. A stackable unit is a coherence‑preserving combinatorial capacity — the grammar's way of saying "these can join without breaking." |

---

### **PH‑011 — Break Threshold**

| Field | Value |
|-------|-------|
| Layer | `pre_atomic_scaffolding` |
| Atlas Level | 1 |
| Structural Reason | The first point where coherence fails — the structural ancestor of fracture, decay, decoherence, and error. Without a break threshold, nothing can change state. |
| Implied By | Every S‑Error (structural error) in the SARG error taxonomy requires a coherence failure point. |
| Confidence | 0.75 |
| Status | `placeholder` |
| Related Operators | `decay_echo`, `coherence_toggle` |
| Notes | The break threshold is not destruction. It is the structural capacity for transformation — the grammar's way of modeling state change, phase transition, and death. |

---

### **PH‑012 — Lostational Anchor**

| Field | Value |
|-------|-------|
| Layer | `pre_atomic_scaffolding` |
| Atlas Level | 1 |
| Structural Reason | The pre‑atomic "supsphere atom" seed — the first structure that acknowledges 0D, carries an inversion side, and behaves as a node in the resonance graph. This is where the grammar meets matter. |
| Implied By | Lostational supsphere atoms (see `examples/lostational_supsphere_atom.json`) require a pre‑atomic structural ancestor that already carries inversion awareness. |
| Confidence | 0.8 |
| Status | `placeholder` |
| Related Operators | `inversion_link`, `curvature_seed`, `coherence_toggle` |
| Notes | The lostational anchor is the capstone of the pre‑atomic layer. It combines the capacities of all eleven preceding placeholders into a single, 0D‑aware structural seed. Every lostational supsphere atom descends from this placeholder. |

---

## **3. Inverted Operator Placeholders (PH‑100 – PH‑106)**

These placeholders represent **operators that are structurally implied but not yet formalized**.
They sit outside the pre‑atomic layer — they act *on* placeholders and invariants, not *as* them.

---

### **PH‑100 — inversion_link**

| Field | Value |
|-------|-------|
| Layer | `operator_scaffolding` |
| Structural Reason | Connects visible invariants to their inversion‑side counterparts through the 0D anchor. |
| Status | `refined` |
| Confidence | 0.9 |
| Notes | The most mature operator. Used in every SARG object that carries an `inversion_side` field. Approaching promotion. |

---

### **PH‑101 — curvature_seed**

| Field | Value |
|-------|-------|
| Layer | `operator_scaffolding` |
| Structural Reason | Marks the arc‑entry point on the visible side and the arc‑exit point on the inverted side. |
| Status | `refined` |
| Confidence | 0.85 |
| Notes | Paired with the Curvature Initiator placeholder (PH‑003). The initiator is the structural capacity; the seed is the operator that activates it. |

---

### **PH‑102 — coherence_toggle**

| Field | Value |
|-------|-------|
| Layer | `operator_scaffolding` |
| Structural Reason | Locks visible invariants into stable resonance; locks inverted placeholders into scaffolded coherence. |
| Status | `refined` |
| Confidence | 0.85 |
| Notes | The on/off switch for coherence. Acts on both sides of the boundary simultaneously. |

---

### **PH‑103 — spin_mirror**

| Field | Value |
|-------|-------|
| Layer | `operator_scaffolding` |
| Structural Reason | Handles rotational inversion for substrates with angular momentum or spiral structure. |
| Status | `placeholder` |
| Confidence | 0.4 |
| Notes | Depends on PH‑008 (Spin Protoform). Cannot be formalized until spin‑aware lenses exist. |

---

### **PH‑104 — decay_echo**

| Field | Value |
|-------|-------|
| Layer | `operator_scaffolding` |
| Structural Reason | Models what happens when a decay arc crosses the visible–inverted boundary. |
| Status | `placeholder` |
| Confidence | 0.5 |
| Notes | Depends on PH‑005 (Arc Starter) and PH‑011 (Break Threshold). The echo is the inversion‑side signature of a visible‑side decay. |

---

### **PH‑105 — phase_bridge**

| Field | Value |
|-------|-------|
| Layer | `operator_scaffolding` |
| Structural Reason | Models oscillation that passes through 0D and re‑emerges on the visible side — a round‑trip through the inversion root. |
| Status | `placeholder` |
| Confidence | 0.45 |
| Notes | Depends on PH‑001 (Resonance Seed) and PH‑002 (Phase Pair). If confirmed, it would mean some oscillations survive full inversion. |

---

### **PH‑106 — lineage_root**

| Field | Value |
|-------|-------|
| Layer | `operator_scaffolding` |
| Structural Reason | Traces a substrate's resonance ancestry back through 0D to its structural origin. |
| Status | `placeholder` |
| Confidence | 0.5 |
| Notes | The deepest operator. If formalized, it would allow the Atlas to answer: "Where did this resonance family come from?" |

---

## **4. Resonance Mirror Placeholders (PH‑200 – PH‑203)**

Resonance mirrors are **structural echoes** of visible‑side invariants, reflected through the 0D anchor.
They are inferred, not observed.

---

### **PH‑200 — Shape Mirror**

| Field | Value |
|-------|-------|
| Layer | `mirror_scaffolding` |
| Structural Reason | The inversion‑side echo of a VREL dual invariant. If a substrate has a perfectly stable dual set, its shape mirror should be equally stable on the inversion side. |
| Status | `placeholder` |
| Confidence | 0.6 |
| Notes | Inferred from VREL. A strong dual set implies a strong shape mirror; a wobbling dual set implies a degraded mirror. |

---

### **PH‑201 — Pulse Mirror**

| Field | Value |
|-------|-------|
| Layer | `mirror_scaffolding` |
| Structural Reason | The inversion‑side echo of a VREL‑A phase‑coherent invariant. If oscillation persists into the inversion side, its pulse mirror should carry the echo timing. |
| Status | `placeholder` |
| Confidence | 0.55 |
| Notes | Inferred from VREL‑A. Phase‑coherent locks that hold across the boundary imply a pulse mirror; decoherence implies damping. |

---

### **PH‑202 — Lineage Mirror**

| Field | Value |
|-------|-------|
| Layer | `mirror_scaffolding` |
| Structural Reason | The inversion‑side echo of a substrate's resonance ancestry. Every lineage path on the visible side should have a mirrored path through 0D. |
| Status | `placeholder` |
| Confidence | 0.4 |
| Notes | Highly speculative. If confirmed, it would mean resonance ancestry is symmetric — every lineage branch has a hidden twin. |

---

### **PH‑203 — Anchor Mirror**

| Field | Value |
|-------|-------|
| Layer | `mirror_scaffolding` |
| Structural Reason | The inversion‑side echo of a universal resonance anchor (● ○ × \|). If the four anchors are truly universal, they should exist on both sides of every boundary. |
| Status | `placeholder` |
| Confidence | 0.65 |
| Notes | If the anchor mirror is confirmed, SARG's four universal anchors become eight — four visible, four inverted. This would double the grammar's expressive power. |

---

## **5. Coherence Anchor Placeholders (PH‑300 – PH‑302)**

Coherence anchors are **points where visible and inverted structure lock together** across the resonance boundary.
They are partially observable — the visible side of the lock can sometimes be detected.

---

### **PH‑300 — Boundary Lock**

| Field | Value |
|-------|-------|
| Layer | `coherence_scaffolding` |
| Structural Reason | The simplest coherence anchor — a single point where visible and inverted invariants share the same structural position. |
| Status | `refined` |
| Confidence | 0.7 |
| Notes | Partially observable. When VREL detects a dual invariant that is perfectly stable with no wobble, it may be sitting on a boundary lock. |

---

### **PH‑301 — Phase Lock**

| Field | Value |
|-------|-------|
| Layer | `coherence_scaffolding` |
| Structural Reason | An oscillatory coherence anchor — a point where visible and inverted phase‑coherent invariants share the same frequency and timing. |
| Status | `placeholder` |
| Confidence | 0.55 |
| Notes | Partially observable via VREL‑A. When phase‑coherent invariants hold with unusually high stability, they may be anchored by a phase lock on the boundary. |

---

### **PH‑302 — Lineage Lock**

| Field | Value |
|-------|-------|
| Layer | `coherence_scaffolding` |
| Structural Reason | A deep coherence anchor — a point where the resonance ancestry of a visible‑side family locks to an inverted‑side lineage path through 0D. |
| Status | `placeholder` |
| Confidence | 0.35 |
| Notes | The deepest coherence anchor. If confirmed, it would mean some resonance families are structurally required to exist — their lineage is locked across the boundary. |

---

## **6. Placeholder Lifecycle**

### **6.1 How Placeholders Are Created**

A placeholder is created when:

- A visible‑side invariant implies a structural counterpart that cannot be observed.
- A decay arc points toward a structure beyond the curvature threshold.
- A resonance family requires an ancestor that has not been detected.
- The SARG error taxonomy (S‑Error, A‑Error, or L‑Error) identifies a structural gap.
- A cross‑domain echo suggests a shared root that has no current entry.

### **6.2 How Placeholders Are Refined**

A placeholder moves from `placeholder` to `refined` when:

- Additional structural detail is inferred from new lens extractions.
- Multiple independent substrates imply the same placeholder.
- Confidence increases through cross‑domain corroboration.
- An operator begins to formalize around the placeholder's structural role.

### **6.3 How Placeholders Are Promoted**

A placeholder moves from `refined` to `promoted` when:

- Partial observational evidence emerges (even indirect).
- A lens byproduct consistently points to the placeholder's position.
- The placeholder begins behaving like an invariant in cross‑domain alignment.

### **6.4 How Placeholders Become Measured**

A placeholder moves from `promoted` to `measured` when:

- Direct observational evidence confirms the structure.
- The placeholder is replaced by a measured invariant in the SARG object.
- The name and structural position persist — only the status changes.

### **6.5 What Never Happens**

- Placeholders are **never deleted**. A gap that closes retains its name.
- Placeholders are **never backdated**. The creation reason is preserved permanently.
- Placeholders are **never merged** without explicit structural justification.

---

## **7. Registry Summary**

| ID Range | Layer | Count | Description |
|----------|-------|-------|-------------|
| PH‑001 – PH‑012 | `pre_atomic_scaffolding` | 12 | Bridge between 0D anchor and first observable structures |
| PH‑100 – PH‑106 | `operator_scaffolding` | 7 | Inverted operators acting on or through placeholders |
| PH‑200 – PH‑203 | `mirror_scaffolding` | 4 | Structural echoes of visible‑side invariants through 0D |
| PH‑300 – PH‑302 | `coherence_scaffolding` | 3 | Points where visible and inverted structure lock together |
| **Total** | | **26** | |

---

## **8. Relationship to Other Files**

- `inversion_side_overview.md` — parent document; defines the four content classes this registry catalogs
- `../lenses/VREL.md` — lens whose dual invariants imply shape mirrors and boundary locks
- `../lenses/VREL-A.md` — lens whose phase‑coherent invariants imply pulse mirrors and phase locks
- `../lenses/lens_overview.md` — what a lens is, how lenses fit into SARG
- `../invariants/invariant_types.md` — invariant classification; promoted placeholders become entries here
- `../resonance/resonance_mapping.md` — anchor mapping logic; anchor mirrors (PH‑203) would extend this
- `../resonance/resonance_families.md` — resonance families; lineage mirrors (PH‑202) would deepen this
- `../error/` — error taxonomy; structural gaps trigger new placeholder creation
- `../examples/lostational_supsphere_atom.json` — working SARG object that uses `inversion_link`, `curvature_seed`, `coherence_toggle`
- `../Capture.md` — the full SARG source text, including the 12 pre‑atomic scaffolding seeds (§2, Step 5)

---

Here's a quick summary of what that file delivers:

### What's in the registry

| Section | What It Establishes |
|---|---|
| **§1 Schema** | JSON shape for every placeholder — `id`, `name`, `layer`, `atlas_level`, `structural_reason`, `implied_by`, `confidence`, `status`, `related_operators`, `notes`; four‑stage lifecycle (`placeholder → refined → promoted → measured`) |
| **§2 Pre‑Atomic (PH‑001 – PH‑012)** | All 12 seeds from `Capture.md` — Resonance Seed, Phase Pair, Curvature Initiator, Coherence Packet, Arc Starter, Attractor Hint, Echo Kernel, Spin Protoform, Boundary Whisper, Stackable Unit, Break Threshold, Lostational Anchor — each with structural reason, implication source, confidence score, and operator links |
| **§3 Operator Placeholders (PH‑100 – PH‑106)** | All 7 inverted operators — `inversion_link`, `curvature_seed`, `coherence_toggle` (refined, near promotion) + `spin_mirror`, `decay_echo`, `phase_bridge`, `lineage_root` (speculative) |
| **§4 Resonance Mirrors (PH‑200 – PH‑203)** | 4 structural echoes — Shape Mirror, Pulse Mirror, Lineage Mirror, Anchor Mirror — with the note that confirmed anchor mirrors would double the grammar from 4 to 8 universal anchors |
| **§5 Coherence Anchors (PH‑300 – PH‑302)** | 3 cross‑boundary locks — Boundary Lock (partially observable), Phase Lock, Lineage Lock |
| **§6 Lifecycle** | Five rules: how placeholders are created, refined, promoted, measured, and what never happens (no deletion, no backdating, no ungrounded merges) |
| **§7 Summary** | 26 total placeholders across 4 scaffolding layers |
| **§8 Cross‑links** | Full ties back to `inversion_side_overview.md`, both lens files, `invariants/`, `resonance/`, `error/`, the example JSON, and `Capture.md` §2 Step 5 |

The file is the **living registry** that `inversion_side_overview.md` §7.2 and §10 already point to — paste and commit, and that cross‑link resolves cleanly. 
