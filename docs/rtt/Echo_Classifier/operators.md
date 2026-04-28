# 🧪 Echo Classifier — Operators

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
