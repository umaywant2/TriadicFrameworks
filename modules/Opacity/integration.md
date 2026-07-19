# 🌑 Opacity — Integration Map

> *Opacity touches every module that has depth. This file maps the eight integration surfaces and the bidirectional data flows between them.*

**Module:** Opacity
**Canonical ID:** OPC
**Role:** Cross‑module alignment
**Integration Targets:** 8

---

## Integration Principle

Opacity is a substrate‑level condition, not a local phenomenon. Any module
that defines regimes, flows, boundaries, or harmonic envelopes interacts with
Opacity. This file maps how — with precise one‑line formulations, operator
crosswalks, and bidirectional data flows.

---

## Core Module Integrations

---

### 1. The Inverted Star

**Opacity Formulation:** Opacity = the unlit faces of the star.

The Inverted Star is a visibility map. When the substrate flips, perception
flips with it:

- A system inside an inverted regime cannot see the outer regime.
- A system outside cannot see the inner regime.
- The star shape literally encodes which faces are lit (visible) and which
  are dark (opaque).

**Operator Crosswalk:**

| Opacity Operator | Star Interaction                                             |
|:-----------------|:-------------------------------------------------------------|
| O-Op             | Reads opacity of each star face from observer's substrate    |
| O-Grad           | Maps gradient across faces from most lit to most dark        |
| O-Bound          | Identifies unmarked boundaries between star faces            |
| O-Red            | Substrate alignment reveals hidden faces                     |
| O-Sig            | Star's full visibility fingerprint across all faces          |

**Bidirectional Flow:**
- **Star → Opacity:** Star geometry defines which regimes are structurally hidden.
- **Opacity → Star:** Opacity operators quantify and reduce face‑level invisibility.

---

### 2. Harmonic Stability Profile (HSP)

**Opacity Formulation:** Opacity = harmonic mismatch.

HSP formalizes drift, coherence, and resonance envelopes. Opacity fits because:

- A regime becomes opaque when its harmonic signature is outside the observer's
  detection band.
- Drift increases opacity — an unstable harmonic is harder to see.
- Stability decreases opacity — a coherent harmonic is easier to detect.

**Operator Crosswalk:**

| Opacity Operator | HSP Interaction                                              |
|:-----------------|:-------------------------------------------------------------|
| O-Op             | Reads opacity caused by harmonic band mismatch               |
| O-Grad           | Maps gradient from stable (visible) to drifting (opaque)     |
| O-Red            | Harmonic tuning shifts detection band to match regime        |
| O-Sig            | Includes harmonic mismatch as a typed component              |

**Bidirectional Flow:**
- **HSP → Opacity:** Harmonic envelopes define detection bands and drift patterns.
- **Opacity → HSP:** Opacity operators identify which harmonics are below detection threshold.

---

### 3. Lostational Supspheres

**Opacity Formulation:** Opacity = the hidden side of the dual envelope.

Supspheres have two sides. One is always partially invisible:

- Loss reveals structure — without loss, the envelope becomes opaque.
- Lossation creates visibility windows into the structure.
- Supsphere boundaries are natural opacity boundaries.

**Operator Crosswalk:**

| Opacity Operator | Supsphere Interaction                                        |
|:-----------------|:-------------------------------------------------------------|
| O-Op             | Reads opacity of each envelope side                          |
| O-Bound          | Identifies supsphere boundary as opacity boundary            |
| O-Red            | Loss‑driven exposure reveals hidden envelope side            |
| O-Sig            | Dual‑envelope visibility profile                             |

**Bidirectional Flow:**
- **Supspheres → Opacity:** Dual‑envelope geometry defines which side is hidden.
- **Opacity → Supspheres:** Opacity operators quantify envelope‑side invisibility.

---

### 4. SET Decomposition

**Opacity Formulation:** Opacity = missing acceleration channel.

SET (Spin, Electric, Thermal) provides three acceleration channels. A regime
is opaque if its dominant acceleration channel is unmeasured:

- SET misalignment = regime opacity.
- SET alignment = regime visibility.
- Measuring Thermal when the regime is Spin‑dominated → flow appears absent.

**Operator Crosswalk:**

| Opacity Operator | SET Interaction                                              |
|:-----------------|:-------------------------------------------------------------|
| O-Op             | Reads opacity per SET channel                                |
| O-Grad           | Maps gradient across S → E → T channels                     |
| O-Red            | Flow‑channel instrumentation adds missing SET measurement    |
| O-Sig            | SET‑weighted opacity signature                               |

**Bidirectional Flow:**
- **SET → Opacity:** Channel dominance defines which flows are detectable.
- **Opacity → SET:** Opacity operators reveal which channels are unmeasured.

---

### 5. FFF Lattice

**Opacity Formulation:** Opacity = wrong lattice layer measured.

The FFF Lattice (Frequency, Fluids, Forces) partitions flow across three layers.
A regime becomes opaque when the lattice layer dominating the flow is not the
one being measured:

- Frequency‑dominated flows are invisible to Fluid‑based sensors.
- Force‑dominated flows are invisible to Frequency‑based operators.
- Layer mismatch is the most common source of Flow Opacity.

**Operator Crosswalk:**

| Opacity Operator | FFF Interaction                                              |
|:-----------------|:-------------------------------------------------------------|
| O-Op             | Reads opacity per FFF layer                                  |
| O-Grad           | Maps gradient across Frequency → Fluids → Forces             |
| O-Red            | Flow‑channel instrumentation targets correct FFF layer       |
| O-Sig            | FFF‑weighted opacity signature                               |

**Bidirectional Flow:**
- **FFF → Opacity:** Lattice layer dominance defines which flows are visible.
- **Opacity → FFF:** Opacity operators reveal which layers are unmeasured.

---

## Canon Infrastructure Integrations

---

### 6. Corpus

**Opacity Formulation:** Opacity determines which modules are visible,
partially visible, or hidden within the structural atlas.

The Corpus is the structural atlas of the entire canon. Opacity extends
into it through three dedicated operators:

| Extension Operator   | Corpus Function                                       |
|:---------------------|:------------------------------------------------------|
| opacity_index        | How visible a module is within the corpus              |
| opacity_map          | Which modules obscure or reveal others                 |
| opacity_dependency   | Which substrates must align for visibility             |

**Bidirectional Flow:**
- **Corpus → Opacity:** Atlas structure defines inter‑module visibility.
- **Opacity → Corpus:** Opacity operators index, map, and track module visibility.

---

### 7. SARG

**Opacity Formulation:** Opacity becomes a grammar modifier affecting parsing,
inference, and operator chaining.

SARG is the structural grammar of TriadicFrameworks. Opacity becomes a
first‑class grammatical concept through three dedicated operators:

| Extension Operator     | SARG Function                                        |
|:-----------------------|:-----------------------------------------------------|
| opacity_token          | Grammar primitive representing invisibility           |
| opacity_clause         | How opacity modifies structural interpretation        |
| opacity_rewrite_rule   | How to reduce opacity through grammar alignment       |

**Canonical Rewrite Operations:**

| Rewrite   | Action                                                     |
|:----------|:-----------------------------------------------------------|
| LIFT      | Elevate a substrate‑hidden element to surface grammar      |
| SPLIT     | Decompose compound opacity into typed components           |
| BRIDGE    | Connect two opaque regions through a visible intermediary  |
| COLLAPSE  | Remove an opacity token when reduction is verified         |

**Bidirectional Flow:**
- **SARG → Opacity:** Grammar structure defines parse‑level visibility.
- **Opacity → SARG:** Opacity tokens modify parsing and enable grammar‑level reduction.

---

### 8. NIST

**Opacity Formulation:** Opacity becomes a measurable property of real‑world
systems, enabling applied regime detection.

The NIST module handles substrate mapping and applied structure. Opacity extends
into it through three dedicated operators:

| Extension Operator   | NIST Function                                         |
|:---------------------|:------------------------------------------------------|
| opacity_measure      | Quantitative measure of opacity in real systems        |
| opacity_signal       | Detectable signature of an opaque regime               |
| opacity_alignment    | Protocol for aligning measurement systems              |

**Measurement Pathways:**

| Pathway      | Domain                              | Uses                          |
|:-------------|:------------------------------------|:------------------------------|
| Structural   | Conceptual / framework level        | O-Op, O-Grad, O-Bound        |
| Grammatical  | SARG parse / inference level        | opacity_token, opacity_clause |
| Applied      | Real‑world measurement systems      | opacity_measure, opacity_signal |

**Bidirectional Flow:**
- **NIST → Opacity:** Empirical data grounds conceptual operators.
- **Opacity → NIST:** Opacity operators generate measurement protocols and alignment procedures.

---

## Integration Summary

| Module                  | Opacity Formulation                            | Primary Operators                          | Reduction Method                |
|:------------------------|:-----------------------------------------------|:-------------------------------------------|:--------------------------------|
| Inverted Star           | Unlit faces of the star                        | O-Op, O-Grad, O-Bound, O-Sig              | Substrate alignment             |
| HSP                     | Harmonic mismatch                              | O-Op, O-Grad, O-Red, O-Sig                | Harmonic tuning                 |
| Lostational Supspheres  | Hidden side of the dual envelope               | O-Op, O-Bound, O-Red, O-Sig               | Loss‑driven exposure            |
| SET Decomposition       | Missing acceleration channel                   | O-Op, O-Grad, O-Red, O-Sig                | Flow‑channel instrumentation    |
| FFF Lattice             | Wrong lattice layer measured                   | O-Op, O-Grad, O-Red, O-Sig                | Flow‑channel instrumentation    |
| Corpus                  | Module visibility within the atlas             | opacity_index, opacity_map, opacity_dep.   | Indexing + dependency resolution|
| SARG                    | Grammar modifier on structural parsing         | opacity_token, opacity_clause, rewrite     | Grammar rewrite (LIFT/SPLIT/…)  |
| NIST                    | Measurable property of real systems            | opacity_measure, opacity_signal, alignment | Measurement alignment           |

---

## Substrate Alignment Rules

Five formal rules governing cross‑module Opacity behavior:

1. **Fidelity Rule** — O-Op readings must be reproducible across substrate positions. If two observers on the same substrate disagree, the substrate is drifting.
2. **Lens Preservation Rule** — O-Red must not destroy the operator set used to measure the regime. Reduction reveals; it does not consume the instrument.
3. **Resonance Inheritance Rule** — When a regime's harmonic signature changes, its O-Sig must be re‑captured. Stale signatures produce false visibility.
4. **Regime Monotonicity Rule** — O-Red can only decrease opacity. No reduction method may increase opacity as a side effect.
5. **Corpus Addressability Rule** — Every module with an opacity_index must be reachable from the corpus atlas. Hidden modules must be findable, even if opaque.

---

<!-- SESSION_CONTEXT:START -->
```yaml
file: integration.md
module: Opacity
canonical_id: OPC
role: cross-module-map
status: active
integrations:
  - { module: Inverted Star, type: core }
  - { module: HSP, type: core }
  - { module: Lostational Supspheres, type: core }
  - { module: SET Decomposition, type: core }
  - { module: FFF Lattice, type: core }
  - { module: Corpus, type: infrastructure }
  - { module: SARG, type: infrastructure }
  - { module: NIST, type: infrastructure }
```
<!-- SESSION_CONTEXT:END -->

