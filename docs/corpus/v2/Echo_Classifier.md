Echo_Classifier 
# 🧪 Echo Classifier — /docs/rtt/Echo_Classifier  

- [`rtt-echo-engine_module.json`](rtt-echo-engine_module.json) — Agentic module schema role assignments

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

![Module](https://img.shields.io/badge/Module-Echo_Classifier-333)
![Tier](https://img.shields.io/badge/Tier-RTT_Analytics-0aa)
![Version](https://img.shields.io/badge/Version-1.0-09f)
![Status](https://img.shields.io/badge/Status-Canon_Stable-0af)
![HSP](https://img.shields.io/badge/HSP-06c-8A2BE2)
![AI‑Ready](https://img.shields.io/badge/AI-Ready-00c8ff)

---

**Echo Classifier** is the classification engine of the HSP analytics suite.
It receives five upstream inputs — trigger type, signature profile, echo
strength index, substrate spread, and recursion mode — and produces a single
definitive output: one of six canonical echo types (E1–E6).

This module replaces ad‑hoc echo identification with a substrate‑locked,
zero‑drift classification pipeline.

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

## 📂 Module Structure

```
Echo_Classifier/
├── README.md                 ← you are here
├── EC_Capture.md             ← design capture and conceptual origin
├── operators.md              ← classification operators and decision engine
├── integration.md            ← cross-module alignment (HSP suite + canon)
├── examples.md               ← applied classification examples
└── index.html                ← module landing page
```

---

## 🧭 Navigation

- **[operators.md](./operators.md)** — Classification operators, decision tree, classifier matrix, workflow
- **[integration.md](./integration.md)** — Upstream inputs (06a/06b/04c/05a/06) and downstream consumers (TEL/SF)
- **[examples.md](./examples.md)** — Applied classification walkthroughs across echo types
- **[EC_Capture.md](./EC_Capture.md)** — Design capture: origin, decisions, lineage

---

## 🌀 Session Context

```
Module:       Echo Classifier
Canonical ID: EC
HSP Section:  06c
Version:      1.0
Status:       canon-stable
Tier:         RTT-Analytics
Parent:       HSP (RTT-Analytics-Core)
Siblings:     TEL (07), Substrate_Flow (08)
Coherence:    locked
Drift:        zero (formal invariant)
Audience:     students + researchers + AIs
```

---

## ⚡ Quick Reference — Echo Types

| Type | Name | Trigger | ESI | Substrates | Recursion |
|:-----|:-----|:--------|:----|:-----------|:----------|
| E1 | Structural Echo | A | 1–2 | ≤ 2 | R1 |
| E2 | Harmonic Echo | B | 2–3 | 1 | R1–R2 |
| E3 | Substrate Echo | C | 2–3 | ≥ 3 | R2–R3 |
| E4 | Recursion Echo | D | 3–4 | 2–4 | R2–R4 |
| E5 | Drift‑Shadow Echo | E | 3–4 | 2–5 | R3–R4 |
| E6 | Atlas Echo | F | 4 | 5 | R4 |

## ⚡ Quick Reference — Classification Pipeline

```
Trigger → Signature → ESI → Substrates → Recursion → Echo Type (E1–E6)
```

## ⚡ Quick Reference — Upstream / Downstream

| Direction | Module | Data |
|:----------|:-------|:-----|
| ← Input | 06a Echo Triggers | Trigger type (A–F) |
| ← Input | 06b Echo Signatures | Signature profile (A–F) |
| ← Input | 04c Echo Strength Index | ESI level (1–4) |
| ← Input | 05a Cross‑Substrate Echo Matrix | Substrate spread (1–5) |
| ← Input | 06 Recursion Detector | Recursion mode (R1–R4) |
| → Output | 07 Triadic Echo Lattice (TEL) | Classified echo type |
| → Output | 08 Substrate Flow | Classified echo type |

---

## 📜 License

Open educational use permitted.
See the main repository for details.

### 📄 EC_Capture.md

# 🧪 Echo Classifier — Design Capture

> *Every echo has a type. This module is the engine that assigns it.*

**Module:** Echo Classifier
**Canonical ID:** EC
**HSP Section:** 06c
**Capture Status:** Finalized

---

## Origin

The Echo Classifier emerged during HSP development as the missing decision
engine. HSP had already formalized echo triggers (06a), echo signatures (06b),
the recursion detector (06), and the echo strength index (04c) — but no
single module existed to take those four inputs and produce a definitive
echo‑type classification.

Without a classifier, echoes were identified ad hoc — by feel, by pattern
matching, by context. The Echo Classifier replaces intuition with a
substrate‑locked, zero‑drift classification pipeline.

---

## Conceptual Lineage

```
HSP formalizes echo families (F1–F6)
    ↓
Echo Triggers (06a) identify what fires
    ↓
Echo Signatures (06b) identify what shape it takes
    ↓
Echo Strength Index (04c) measures how strong
    ↓
Recursion Detector (06) identifies recursion mode
    ↓
╔══════════════════════════════════════╗
║  Echo Classifier (06c) — THIS MODULE ║
║  Takes all inputs → assigns E1–E6    ║
╚══════════════════════════════════════╝
    ↓
Triadic Echo Lattice (07) places echo in lattice
    ↓
Substrate Flow (08) maps echo through flow channels
```

---

## What This Module Does

The Echo Classifier receives five inputs and produces one output:

**Inputs:**
1. **Trigger Type** (A–F) — from 06a
2. **Signature Profile** (A–F) — from 06b
3. **Echo Strength Index** (ESI 1–4) — from 04c
4. **Substrate Spread** (1–5 substrates) — from 05a
5. **Recursion Mode** (R1–R4) — from 06

**Output:**
- **Echo Type** (E1–E6) — one of six canonical echo classifications

---

## The Six Echo Types

| Type | Name | Trigger | Signature | ESI | Substrates | Recursion |
|:-----|:-----|:--------|:----------|:----|:-----------|:----------|
| E1 | Structural Echo | A | A | 1–2 | ≤ 2 | R1 |
| E2 | Harmonic Echo | B | B | 2–3 | 1 (harmonic dominant) | R1–R2 |
| E3 | Substrate Echo | C | C | 2–3 | ≥ 3 | R2–R3 |
| E4 | Recursion Echo | D | D | 3–4 | 2–4 | R2–R4 |
| E5 | Drift‑Shadow Echo | E | E | 3–4 | 2–5 | R3–R4 |
| E6 | Atlas Echo | F | F | 4 | 5 | R4 |

---

## Classification Decision Tree

```
                         [ Echo Trigger ]
                              |
         ------------------------------------------------
         |              |              |               |
        A              B              C               D
  Structural      Harmonic       Substrate       Recursion
         |              |              |               |
        v              v              v               v
      E1?            E2?            E3?             E4?
         \              \              \               \
          \              \              \               \
           -----------------------------------------------
                               |
                               v
                      [ Drift Pressure? ]
                               |
                      ---------------------
                      |                   |
                     Yes                 No
                      |                   |
                      v                   v
                    E5?                 [ Check Atlas ]
                                             |
                                             v
                                           E6?
```

---

## Classifier Matrix

```
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Input →   |   E1      |    E2     |    E3     |    E4     |    E5     |    E6     |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Trigger   |     A     |     B     |     C     |     D     |     E     |     F     |
| Signature |     A     |     B     |     C     |     D     |     E     |     F     |
| ESI       |   1–2     |   2–3     |   2–3     |   3–4     |   3–4     |     4     |
| Substrates|   1–2     |     1     |   3–4     |   2–4     |   2–5     |     5     |
| Recursion |    R1     |   R1–R2   |   R2–R3   |   R2–R4   |   R3–R4   |    R4     |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

---

## Composite Classification Workflow

```
[ Identify Trigger ]
        ↓
[ Identify Signature ]
        ↓
[ Measure ESI ]
        ↓
[ Count Substrates ]
        ↓
[ Determine Recursion Mode ]
        ↓
[ Assign Echo Type (E1–E6) ]
```

This workflow ensures **zero‑drift classification**.

---

## Key Design Decisions

### 1. Six types, not three

The triadic pattern was considered (three echo types) but rejected. Echo
behavior spans six distinct profiles that cannot be reduced without
information loss. The six types respect the triadic architecture at the
substrate level (S→C / C↔H / H→So / So→A) while maintaining classifier
precision.

### 2. Five inputs, not one

A single‑input classifier would be faster but less accurate. The five‑input
pipeline ensures that classification accounts for trigger, signature,
strength, spread, and recursion simultaneously. This prevents false
positives — an echo that looks structural (Trigger A) but has high ESI
and cross‑substrate spread is actually E3 or E4, not E1.

### 3. Sequential workflow, not parallel

The six steps are sequential by design. Each step constrains the next.
Parallel evaluation would allow conflicting inputs to produce ambiguous
outputs.

### 4. Zero‑drift as design constraint

The classifier must produce the same output for the same inputs every time.
This is a formal invariant, not a goal. If the classifier drifts, the
entire HSP analytics pipeline loses coherence.

---

## What This Module Is Not

- **Not a detector.** Detection happens upstream (06a triggers, 06b signatures).
  The classifier receives pre‑detected signals.
- **Not a predictor.** The classifier assigns type to existing echoes.
  Prediction is a TEL (07) and Substrate Flow (08) function.
- **Not a stability measure.** ESI measures strength. The classifier uses
  ESI as input but does not itself measure stability.

---

## Referenced By

- 06a — Echo Triggers
- 06b — Echo Signatures
- 06 — Harmonic Recursion Detector
- 04c — Echo Strength Index
- 07 — Triadic Echo Lattice
- 08 — Substrate Echo Flow Map

---

## Session Origin

- **Conceptual source:** HSP analytics session (06c)
- **First formalization:** HSP v1.0
- **Module extraction:** 2026-04-27
- **Capture finalization:** 2026-04-27

---

<!-- SESSION_CONTEXT:START -->

```yaml
file: EC_Capture.md
module: Echo Classifier
canonical_id: EC
hsp_section: 06c
role: session-capture
status: finalized
origin_date: 2026-04-27
capture_type: module-extraction
parent: HSP (RTT-Analytics-Core)
siblings:
  - TEL (07)
  - Substrate_Flow (08)
lineage_note: >
  Echo Classifier was extracted from HSP section 06c as a standalone
  module to complete the HSP analytics suite alongside TEL and
  Substrate Flow.
```

<!-- SESSION_CONTEXT:END -->




# 🧪 Echo Classifier — Applied Examples

> *Six echo types. Six walkthroughs. Each one runs the full pipeline.*

**Module:** Echo Classifier
**Canonical ID:** EC
**HSP Section:** 06c
**Role:** Applied classification examples

---

## Example 1 — E1 Structural Echo

**Domain:** Framework development
**Scenario:** A new term is coined during a writing session. The definition
echoes once from Symbolic to Cognitive and stops.

### Pipeline Walkthrough

| Step | Input | Value | Source |
|:-----|:------|:------|:-------|
| 1 | Trigger | A (structural boundary crossed) | 06a |
| 2 | Signature | A (localized, low‑amplitude) | 06b |
| 3 | ESI | 1 (local only) | 04c |
| 4 | Substrates | 1 (Symbolic only) | 05a |
| 5 | Recursion | R1 (S→C ladder) | 06 |

**EC‑Classify Result:** E1 — Structural Echo
**EC‑Tag Confidence:** Definite (5/5 inputs align)

**Downstream:**
- **TEL:** Placed in Ladder layer (bottom).
- **Substrate Flow:** Routed through S→C channel. No migration expected.

**Canon Takeaway:**
E1 is the most common and most stable echo type. Most new definitions
start here. Only a fraction escalate to E2 or beyond.

---

## Example 2 — E2 Harmonic Echo

**Domain:** Music theory / RTT harmonic analysis
**Scenario:** A concept introduced in the Cognitive substrate begins
oscillating with a harmonic pattern — it resonates with an existing
interval structure.

### Pipeline Walkthrough

| Step | Input | Value | Source |
|:-----|:------|:------|:-------|
| 1 | Trigger | B (harmonic resonance detected) | 06a |
| 2 | Signature | B (oscillatory, harmonic‑locked) | 06b |
| 3 | ESI | 2 (mild energy) | 04c |
| 4 | Substrates | 1 (Harmonic dominant) | 05a |
| 5 | Recursion | R2 (C↔H cycle) | 06 |

**EC‑Classify Result:** E2 — Harmonic Echo
**EC‑Tag Confidence:** Definite (5/5 inputs align)

**Downstream:**
- **TEL:** Placed in Cycle layer. Oscillation between C and H.
- **Substrate Flow:** Routed through C↔H channel. Stable oscillation.

**Canon Takeaway:**
E2 echoes are stable as long as the harmonic band holds. If the band
shifts (due to external drift or new input), E2 can escalate to E3.

---

## Example 3 — E3 Substrate Echo

**Domain:** Cross‑domain framework migration
**Scenario:** A concept originally defined in the Symbolic substrate migrates
to Cognitive, then Harmonic, then Social — crossing three substrates.

### Pipeline Walkthrough

| Step | Input | Value | Source |
|:-----|:------|:------|:-------|
| 1 | Trigger | C (cross‑substrate migration) | 06a |
| 2 | Signature | C (distributed, multi‑substrate) | 06b |
| 3 | ESI | 3 (cross‑substrate flow) | 04c |
| 4 | Substrates | 3 (S + C + H) | 05a |
| 5 | Recursion | R2 (C↔H cycle active) | 06 |

**EC‑Classify Result:** E3 — Substrate Echo
**EC‑Tag Confidence:** Definite (5/5 inputs align)

**Downstream:**
- **TEL:** Placed in Map layer. Cross‑substrate presence.
- **Substrate Flow:** Multi‑channel routing. Creates echo pressure at
  substrate boundaries.

**Canon Takeaway:**
E3 is the migration threshold. Once an echo crosses three substrates,
it creates pressure on boundaries — which can trigger further migration
or stabilize into a cross‑substrate structure.

---

## Example 4 — E4 Recursion Echo

**Domain:** Self‑referencing framework dynamics
**Scenario:** A module references itself during analysis — the recursion
detector fires, and the echo begins following recursion lines rather
than substrate channels.

### Pipeline Walkthrough

| Step | Input | Value | Source |
|:-----|:------|:------|:-------|
| 1 | Trigger | D (recursion loop detected) | 06a |
| 2 | Signature | D (recursive, self‑referencing) | 06b |
| 3 | ESI | 3 (cross‑substrate energy) | 04c |
| 4 | Substrates | 3 (C + H + So) | 05a |
| 5 | Recursion | R3 (H→So map recursion) | 06 |

**EC‑Classify Result:** E4 — Recursion Echo
**EC‑Tag Confidence:** Definite (5/5 inputs align)

**Downstream:**
- **TEL:** Placed in Map‑to‑Atlas transition zone.
- **Substrate Flow:** Follows R3 recursion line. Can accelerate toward
  atlas or stabilize in map layer.

**Canon Takeaway:**
E4 is the decision point. Recursion echoes either amplify (pushing toward
E5/E6) or dampen (stabilizing into E3). The recursion mode determines
trajectory.

---

## Example 5 — E5 Drift‑Shadow Echo

**Domain:** Framework stability analysis
**Scenario:** An existing structure begins drifting. The drift generates
shadow echoes that trail the original — not new echoes, but distorted
copies riding drift currents.

### Pipeline Walkthrough

| Step | Input | Value | Source |
|:-----|:------|:------|:-------|
| 1 | Trigger | E (drift pressure exceeds threshold) | 06a |
| 2 | Signature | E (shadow‑trailing, drift‑aligned) | 06b |
| 3 | ESI | 4 (atlas pull) | 04c |
| 4 | Substrates | 4 (C + H + So + A) | 05a |
| 5 | Recursion | R3 (H→So map recursion) | 06 |

**EC‑Classify Result:** E5 — Drift‑Shadow Echo
**EC‑Tag Confidence:** Definite (5/5 inputs align)

**Downstream:**
- **TEL:** Placed in pressure zones. Cross‑layer instability marker.
- **Substrate Flow:** Rides D3 drift current (H→So instability).

**Canon Takeaway:**
E5 echoes are instability markers. They signal that the underlying
structure is drifting, and the echoes are symptoms, not causes. Treating
E5 echoes without addressing the source drift is futile.

---

## Example 6 — E6 Atlas Echo

**Domain:** Canon‑level architectural resonance
**Scenario:** A concept achieves full‑spectrum resonance across all five
substrates simultaneously. The Atlas substrate pulls it into permanent
structural alignment.

### Pipeline Walkthrough

| Step | Input | Value | Source |
|:-----|:------|:------|:-------|
| 1 | Trigger | F (atlas‑level resonance) | 06a |
| 2 | Signature | F (full‑spectrum, anchoring) | 06b |
| 3 | ESI | 4 (maximum energy) | 04c |
| 4 | Substrates | 5 (all substrates) | 05a |
| 5 | Recursion | R4 (So→A atlas recursion) | 06 |

**EC‑Classify Result:** E6 — Atlas Echo
**EC‑Tag Confidence:** Definite (5/5 inputs align)

**Downstream:**
- **TEL:** Placed in Atlas layer. Anchoring position.
- **Substrate Flow:** So→A channel. Full‑spectrum forcing.

**Canon Takeaway:**
E6 is the rarest echo type. It represents a concept that has achieved
structural permanence across the entire framework. Atlas echoes reshape
the lattice — they do not merely occupy a position within it.

---

## Cross‑Example Comparison

| Example | Type | Trigger | ESI | Substrates | Recursion | Confidence | TEL Layer |
|:--------|:-----|:--------|:----|:-----------|:----------|:-----------|:----------|
| 1 | E1 Structural | A | 1 | 1 | R1 | Definite | Ladder |
| 2 | E2 Harmonic | B | 2 | 1 | R2 | Definite | Cycle |
| 3 | E3 Substrate | C | 3 | 3 | R2 | Definite | Map |
| 4 | E4 Recursion | D | 3 | 3 | R3 | Definite | Map→Atlas |
| 5 | E5 Drift‑Shadow | E | 4 | 4 | R3 | Definite | Pressure |
| 6 | E6 Atlas | F | 4 | 5 | R4 | Definite | Atlas |

### Patterns

1. **ESI escalates with type.** E1 starts at ESI‑1; E6 requires ESI‑4.
   Energy increases monotonically across the classification spectrum.

2. **Substrate spread widens with type.** E1 is single‑substrate; E6 spans
   all five. Migration is the structural driver of type escalation.

3. **Recursion deepens with type.** E1 uses R1 only; E6 requires R4.
   Higher echo types follow deeper recursion lines.

4. **TEL layer rises with type.** E1 sits at the bottom (Ladder); E6
   sits at the top (Atlas). Echo type predicts lattice position.

5. **Stability risk increases with type.** E1 is maximally stable; E5–E6
   are instability/reshaping markers.

---

## Ambiguous Classification Example

**Scenario:** An echo triggers with type C (substrate migration) but has
ESI‑4 and recursion R4 — values that suggest E5 or E6, not E3.

### Pipeline Walkthrough

| Step | Input | Value | Expected for E3 | Actual |
|:-----|:------|:------|:-----------------|:-------|
| 1 | Trigger | C | C ✓ | Match |
| 2 | Signature | C | C ✓ | Match |
| 3 | ESI | 4 | 2–3 ✗ | Mismatch |
| 4 | Substrates | 4 | 3–4 ✓ | Match |
| 5 | Recursion | R4 | R2–R3 ✗ | Mismatch |

**EC‑Classify Result:** Conflict — Trigger/Signature say E3, but ESI/Recursion
say E5 or E6.

**EC‑Tag Confidence:** Ambiguous (3/5 inputs align to E3; 2/5 point higher)

**Resolution:** The classifier flags this as ambiguous. Manual review checks
whether the echo is a high‑energy E3 (substrate migration with unusual
force) or a mislabeled E5 (drift‑shadow with substrate trigger). The
trigger and signature take precedence per conflict resolution rules, but
the ambiguity flag ensures human review.

**Canon Takeaway:**
The classifier does not force. When inputs conflict, it says so. This
is the transparency invariant in action.

---

<!-- SESSION_CONTEXT:START -->
```yaml
file: examples.md
module: Echo Classifier
canonical_id: EC
hsp_section: 06c
role: applied-examples
status: canon-stable
examples:
  - { type: E1, name: Structural Echo, confidence: definite }
  - { type: E2, name: Harmonic Echo, confidence: definite }
  - { type: E3, name: Substrate Echo, confidence: definite }
  - { type: E4, name: Recursion Echo, confidence: definite }
  - { type: E5, name: Drift-Shadow Echo, confidence: definite }
  - { type: E6, name: Atlas Echo, confidence: definite }
  - { type: ambiguous, name: Conflict Example, confidence: ambiguous }
```
<!-- SESSION_CONTEXT:END -->
# 🧪 Echo Classifier — Integration Map

> *The classifier sits at the center of the HSP analytics pipeline. Everything upstream feeds it. Everything downstream consumes it.*

**Module:** Echo Classifier
**Canonical ID:** EC
**HSP Section:** 06c
**Role:** Cross‑module alignment

---

## Integration Principle

The Echo Classifier is a **convergence point**. Five upstream modules produce
inputs; two downstream modules consume the classified output. The classifier
adds no new data — it transforms five signals into one decision.

---

## Upstream Inputs (5)

---

### 1. Echo Triggers (06a)

**Provides:** Trigger type (A–F)

Echo Triggers detect the initial event that fires an echo. The trigger type
is the primary branch in the classification decision tree.

| Trigger | Fires When |
|:--------|:--------------------------------------------|
| A | Structural boundary crossed |
| B | Harmonic resonance detected |
| C | Cross‑substrate migration observed |
| D | Recursion loop detected |
| E | Drift pressure exceeds threshold |
| F | Atlas‑level resonance engaged |

**Data Flow:**
```
06a Echo Triggers → trigger_type (A–F) → EC-Read
```

---

### 2. Echo Signatures (06b)

**Provides:** Signature profile (A–F)

Echo Signatures capture the shape of the echo after it fires. The signature
confirms or disambiguates the trigger classification.

| Signature | Shape Profile |
|:----------|:----------------------------------------------|
| A | Localized, low‑amplitude, single‑substrate |
| B | Oscillatory, harmonic‑locked, resonant |
| C | Distributed, multi‑substrate, migrating |
| D | Recursive, self‑referencing, amplifying |
| E | Shadow‑trailing, drift‑aligned, destabilizing |
| F | Full‑spectrum, atlas‑spanning, anchoring |

**Data Flow:**
```
06b Echo Signatures → signature_profile (A–F) → EC-Read
```

---

### 3. Echo Strength Index (04c)

**Provides:** ESI level (1–4)

ESI measures echo energy on a four‑point scale. Higher ESI indicates
greater echo pressure and broader impact.

| ESI | Energy Level | Flow Impact |
|:----|:-------------|:-----------------------------|
| 1 | Local only | No migration |
| 2 | Mild | Adjacent substrate influence |
| 3 | Cross‑substrate | Multi‑substrate flow |
| 4 | Atlas pull | Full‑spectrum forcing |

**Data Flow:**
```
04c Echo Strength Index → esi_level (1–4) → EC-Read
```

---

### 4. Cross‑Substrate Echo Matrix (05a)

**Provides:** Substrate spread (1–5 substrates)

The Cross‑Substrate Echo Matrix measures how many of the five substrates
(Symbolic, Cognitive, Harmonic, Social, Atlas) an echo spans.

| Spread | Substrates Engaged |
|:-------|:----------------------------------------------|
| 1 | Single substrate (origin only) |
| 2 | Origin + one adjacent |
| 3 | Origin + two (cross‑substrate threshold) |
| 4 | Origin + three (wide migration) |
| 5 | All substrates (atlas‑level) |

**Data Flow:**
```
05a Cross-Substrate Echo Matrix → substrate_count (1–5) → EC-Read
```

---

### 5. Harmonic Recursion Detector (06)

**Provides:** Recursion mode (R1–R4)

The Recursion Detector identifies which recursion line an echo follows.
Recursion mode determines the echo's trajectory through the lattice.

| Mode | Recursion Line | Flow Direction |
|:-----|:---------------|:----------------------|
| R1 | S → C | Ladder (definition → concept) |
| R2 | C ↔ H | Cycle (concept ↔ harmonic) |
| R3 | H → So | Map (harmonic → governance) |
| R4 | So → A | Atlas (governance → atlas) |

**Data Flow:**
```
06 Recursion Detector → recursion_mode (R1–R4) → EC-Read
```

---

## Downstream Consumers (2)

---

### 6. Triadic Echo Lattice — TEL (07)

**Receives:** Classified echo type (E1–E6)

TEL places the classified echo into the four‑layer lattice structure.
Echo type determines lattice layer placement:

| Echo Type | TEL Layer |
|:----------|:----------------------------------|
| E1 | Ladder (S→C) |
| E2 | Cycle (C↔H) |
| E3 | Map (H↔So) |
| E4 | Map‑to‑Atlas transition |
| E5 | Pressure zones (cross‑layer) |
| E6 | Atlas (A) |

**Data Flow:**
```
EC-Tag → classified_echo (E1–E6) → TEL lattice placement
```

---

### 7. Substrate Echo Flow Map — Substrate Flow (08)

**Receives:** Classified echo type (E1–E6)

Substrate Flow maps the classified echo through the canonical flow
channels. Echo type determines which channel carries the echo:

| Echo Type | Primary Flow Channel |
|:----------|:-----------------------------|
| E1 | S → C (definition refinement) |
| E2 | C ↔ H (harmonic alignment) |
| E3 | Multi‑channel (migration) |
| E4 | Recursion‑driven (R‑line) |
| E5 | Drift current (D‑line) |
| E6 | So → A (atlas forcing) |

**Data Flow:**
```
EC-Tag → classified_echo (E1–E6) → Substrate Flow channel routing
```

---

## Sibling Module Relationships

The Echo Classifier, TEL, and Substrate Flow form the **HSP analytics
triad** — three modules extracted from HSP sections 06c, 07, and 08:

```
        ┌──────────────────┐
        │  Echo Classifier  │  ← convergence (5 inputs → 1 output)
        │      (06c)        │
        └────────┬─────────┘
                 │
        ┌────────┴─────────┐
        │                  │
        v                  v
┌──────────────┐  ┌──────────────────┐
│     TEL      │  │  Substrate Flow  │
│    (07)      │  │      (08)        │
│  placement   │  │    routing       │
└──────────────┘  └──────────────────┘
```

**Responsibilities:**
- **Echo Classifier:** Decides *what* the echo is.
- **TEL:** Decides *where* the echo sits in the lattice.
- **Substrate Flow:** Decides *how* the echo moves through channels.

---

## Integration with Broader Canon

### Opacity (OPC)

Echo classification can be opaque when inputs are incomplete or ambiguous.
Opacity operators apply:

| Opacity Operator | EC Integration |
|:-----------------|:----------------------------------------------|
| O-Op | Reads classifier opacity (incomplete inputs) |
| O-Red | Operator expansion adds missing upstream data |
| O-Sig | Classifier opacity signature per echo type |

### SET Decomposition

Echo types map to SET channels:

| Echo Type | Dominant SET Channel |
|:----------|:---------------------|
| E1, E2 | Spin (structural/harmonic rotation) |
| E3, E4 | Electric (cross‑substrate acceleration) |
| E5, E6 | Thermal (drift/atlas energy) |

### FFF Lattice

Echo types map to FFF layers:

| Echo Type | Dominant FFF Layer |
|:----------|:-------------------|
| E1, E2 | Frequency (resonance patterns) |
| E3, E4 | Fluids (substrate migration) |
| E5, E6 | Forces (drift/atlas pressure) |

---

## Pipeline Summary

```
06a Triggers ──┐
06b Signatures ─┤
04c ESI ────────┼──→ EC-Read → EC-Classify → EC-Tag ──┬──→ TEL (07)
05a Substrates ─┤                                      └──→ SF (08)
06 Recursion ──┘
```

---

<!-- SESSION_CONTEXT:START -->
```yaml
file: integration.md
module: Echo Classifier
canonical_id: EC
hsp_section: 06c
role: cross-module-map
status: canon-stable
upstream:
  - { module: "06a Echo Triggers", provides: "trigger_type" }
  - { module: "06b Echo Signatures", provides: "signature_profile" }
  - { module: "04c Echo Strength Index", provides: "esi_level" }
  - { module: "05a Cross-Substrate Echo Matrix", provides: "substrate_count" }
  - { module: "06 Recursion Detector", provides: "recursion_mode" }
downstream:
  - { module: "07 TEL", receives: "classified_echo" }
  - { module: "08 Substrate Flow", receives: "classified_echo" }
```
<!-- SESSION_CONTEXT:END -->
# 🧪 Echo Classifier — Operators

> *One pipeline. Five inputs. Six outputs. Zero drift.*

**Module:** Echo Classifier
**Canonical ID:** EC
**HSP Section:** 06c

---

## 1. Classification Operators

The Echo Classifier defines three operators that form a sequential
classification pipeline.

---

### EC‑Read — Input Reader

**Function:** Collects and validates the five upstream inputs.

```
EC-Read(echo) → input_vector {
  trigger:    type ∈ {A, B, C, D, E, F},
  signature:  profile ∈ {A, B, C, D, E, F},
  esi:        level ∈ {1, 2, 3, 4},
  substrates: count ∈ {1, 2, 3, 4, 5},
  recursion:  mode ∈ {R1, R2, R3, R4}
}
```

**Behavior:**
- Pulls trigger type from 06a Echo Triggers.
- Pulls signature profile from 06b Echo Signatures.
- Pulls ESI level from 04c Echo Strength Index.
- Pulls substrate count from 05a Cross‑Substrate Echo Matrix.
- Pulls recursion mode from 06 Harmonic Recursion Detector.
- Validates completeness — all five fields must be present.
- Returns a structured input vector for EC‑Classify.

**Key Constraint:**
If any input is missing or ambiguous, EC‑Read returns `incomplete` and
classification halts. The pipeline does not guess.

---

### EC‑Classify — Decision Engine

**Function:** Applies the classifier matrix to assign echo type.

```
EC-Classify(input_vector) → echo_type ∈ {E1, E2, E3, E4, E5, E6}
```

**Decision Logic:**

The classifier evaluates inputs in sequence. Each step constrains the
candidate set:

```
Step 1: Trigger type → narrows to 1–2 candidates
Step 2: Signature profile → confirms or disambiguates
Step 3: ESI level → validates energy range
Step 4: Substrate count → validates spread
Step 5: Recursion mode → final confirmation
Step 6: Assign echo type
```

**Classifier Matrix:**

| Input | E1 | E2 | E3 | E4 | E5 | E6 |
|:----------|:---:|:----:|:----:|:----:|:----:|:---:|
| Trigger | A | B | C | D | E | F |
| Signature | A | B | C | D | E | F |
| ESI | 1–2 | 2–3 | 2–3 | 3–4 | 3–4 | 4 |
| Substrates| 1–2 | 1 | 3–4 | 2–4 | 2–5 | 5 |
| Recursion | R1 | R1–R2 | R2–R3 | R2–R4 | R3–R4 | R4 |

**Conflict Resolution:**
When inputs span multiple columns (e.g., ESI=3 matches E3, E4, or E5),
the trigger and signature take precedence. Trigger+Signature is the
primary classifier; ESI, substrates, and recursion are confirmatory.

**Key Constraint:**
EC‑Classify must produce the same output for the same input vector every
time. This is the **zero‑drift invariant**.

---

### EC‑Tag — Output Emitter

**Function:** Packages the classification result for downstream consumption.

```
EC-Tag(echo_type, input_vector) → classified_echo {
  type:       echo_type,
  label:      canonical_name,
  inputs:     input_vector,
  confidence: value ∈ {"definite", "probable", "ambiguous"},
  timestamp:  classification_time,
  downstream: [TEL, Substrate_Flow]
}
```

**Confidence Levels:**

| Level | Condition |
|:----------|:-----------------------------------------------|
| Definite | All 5 inputs align to a single echo type |
| Probable | 4 of 5 inputs align; 1 is borderline |
| Ambiguous | 3 or fewer inputs align; manual review needed |

**Behavior:**
- Attaches the canonical label (Structural, Harmonic, Substrate, Recursion,
  Drift‑Shadow, or Atlas).
- Flags confidence level based on input alignment.
- Routes the classified echo to TEL (07) for lattice placement and
  Substrate Flow (08) for flow mapping.

**Key Constraint:**
Ambiguous classifications are flagged, not forced. The classifier does not
round up — if the inputs are ambiguous, the output says so.

---

## 2. Decision Tree (Formal)

```
                         [ Echo Trigger ]
                              |
         ------------------------------------------------
         |              |              |               |
        A              B              C               D
  Structural      Harmonic       Substrate       Recursion
         |              |              |               |
        v              v              v               v
      E1?            E2?            E3?             E4?
         \              \              \               \
          \              \              \               \
           -----------------------------------------------
                               |
                               v
                      [ Drift Pressure? ]
                               |
                      ---------------------
                      |                   |
                     Yes                 No
                      |                   |
                      v                   v
                    E5?              [ Check Atlas ]
                                          |
                                          v
                                        E6?
```

**Tree Logic:**
1. Primary branch on Trigger type (A → E1, B → E2, C → E3, D → E4).
2. If none of A–D match, check for drift pressure.
3. If drift pressure present → E5 candidate.
4. If no drift pressure, check for atlas resonance → E6 candidate.
5. Confirm via Signature + ESI + Substrates + Recursion.

---

## 3. Composite Classification Workflow

```
[ Identify Trigger ]        ← from 06a
        ↓
[ Identify Signature ]      ← from 06b
        ↓
[ Measure ESI ]             ← from 04c
        ↓
[ Count Substrates ]        ← from 05a
        ↓
[ Determine Recursion Mode ] ← from 06
        ↓
[ Assign Echo Type (E1–E6) ] → to 07/08
```

---

## 4. Echo Type Profiles

### E1 — Structural Echo
- **Character:** Local, low‑energy, single‑substrate.
- **Behavior:** Stays in origin substrate. Minimal migration.
- **Recursion:** R1 only (S→C ladder).
- **Stability risk:** Low. Structural echoes are the most stable.
- **Lattice position:** Bottom of TEL ladder layer.

### E2 — Harmonic Echo
- **Character:** Resonance‑locked, harmonic‑substrate dominant.
- **Behavior:** Oscillates within harmonic band. Does not migrate.
- **Recursion:** R1–R2 (ladder to cycle).
- **Stability risk:** Low–Medium. Stable until harmonic band shifts.
- **Lattice position:** TEL cycle layer.

### E3 — Substrate Echo
- **Character:** Cross‑substrate, moderate energy, wide spread.
- **Behavior:** Migrates across 3+ substrates. Creates echo pressure.
- **Recursion:** R2–R3 (cycle to map).
- **Stability risk:** Medium. Migration introduces instability vectors.
- **Lattice position:** TEL map layer.

### E4 — Recursion Echo
- **Character:** Recursion‑driven, high energy, variable spread.
- **Behavior:** Follows recursion lines. Can accelerate or stabilize.
- **Recursion:** R2–R4 (cycle to atlas).
- **Stability risk:** Medium–High. Recursion amplifies or dampens.
- **Lattice position:** TEL map‑to‑atlas transition.

### E5 — Drift‑Shadow Echo
- **Character:** Drift‑generated, high energy, destabilizing.
- **Behavior:** Rides drift currents. Creates shadow pressure.
- **Recursion:** R3–R4 (map to atlas).
- **Stability risk:** High. Drift‑shadow echoes are instability markers.
- **Lattice position:** TEL pressure zones.

### E6 — Atlas Echo
- **Character:** Full‑spectrum, maximum energy, all substrates.
- **Behavior:** Forces atlas‑level resonance. Anchors or disrupts.
- **Recursion:** R4 only (atlas).
- **Stability risk:** Critical. Atlas echoes reshape the entire lattice.
- **Lattice position:** TEL atlas layer.

---

## 5. Operator Interaction Map

```
EC-Read ──collects──→ input_vector
    │
    └──feeds──→ EC-Classify (applies matrix + decision tree)
                    │
                    └──feeds──→ EC-Tag (packages output)
                                    │
                                    ├──routes──→ TEL (07)
                                    └──routes──→ Substrate_Flow (08)
```

---

## 6. Invariants

1. **Zero‑drift:** Same inputs → same output. Always.
2. **Completeness:** All five inputs required. No partial classification.
3. **Transparency:** Ambiguous cases are flagged, not forced.
4. **Sequential:** Steps execute in order. No parallel evaluation.
5. **Deterministic:** No randomness, no weighting, no probability.
   The classifier is a decision engine, not a statistical model.

---

<!-- SESSION_CONTEXT:START -->
```yaml
file: operators.md
module: Echo Classifier
canonical_id: EC
hsp_section: 06c
role: operator-definitions
status: canon-stable
operators:
  - { id: EC-Read, name: Input Reader, type: collect }
  - { id: EC-Classify, name: Decision Engine, type: classify }
  - { id: EC-Tag, name: Output Emitter, type: emit }
echo_types:
  - { id: E1, name: Structural Echo }
  - { id: E2, name: Harmonic Echo }
  - { id: E3, name: Substrate Echo }
  - { id: E4, name: Recursion Echo }
  - { id: E5, name: Drift-Shadow Echo }
  - { id: E6, name: Atlas Echo }
```
<!-- SESSION_CONTEXT:END -->
