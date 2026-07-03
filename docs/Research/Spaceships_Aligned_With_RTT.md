# RTT Craft Taxonomy
### `docs/Research/Spaceships_Aligned_With_RTT.md`
> **TriadicFrameworks** · Research Branch · Canonical Reference

---

## Overview

The **RTT Craft Taxonomy** is a layered classification framework for mapping spacecraft archetypes against the Recursive Triadic Taxonomy (RTT). Each craft is evaluated across five hierarchical layers that together describe how a vessel *operates*, *navigates dimensionally*, *sustains a working regime*, *manages drift*, and *maintains coherence* across conditions.

This document is the canonical source for layer definitions, module structure, and session alignment guidelines.

---

## Taxonomy Hierarchy

The five layers are applied **top-down** during classification and **bottom-up** during coherence validation. Each layer inherits constraints from the layer above it.

```
┌─────────────────────────────────────────────────────────┐
│  LAYER 1 · OPERATOR                                     │
│  Who or what drives the craft's intent and agency       │
├─────────────────────────────────────────────────────────┤
│  LAYER 2 · DIMENSIONAL                                  │
│  What space(s) the craft is capable of traversing       │
├─────────────────────────────────────────────────────────┤
│  LAYER 3 · REGIME                                       │
│  The operating logic / rule-set the craft sustains      │
├─────────────────────────────────────────────────────────┤
│  LAYER 4 · DRIFT                                        │
│  How the craft departs from or resists nominal state    │
├─────────────────────────────────────────────────────────┤
│  LAYER 5 · COHERENCE                                    │
│  Whether the craft's layers resolve into a stable RTT   │
└─────────────────────────────────────────────────────────┘
```

---

## Layer Definitions

### Layer 1 — Operator
**What it captures:** The locus of agency aboard or governing the craft. This is not merely crew composition — it encodes *decision authority*, *feedback loop origin*, and *triadic role assignment*.

| Sub-class | Description |
|---|---|
| `AUTONOMOUS` | Craft governs itself via closed internal loop |
| `DIRECTED` | External operator holds primary agency |
| `TRIADIC` | Agency is distributed across three balanced nodes (canonical RTT form) |
| `HYBRID` | Mixed or context-dependent authority model |

**RTT Alignment Rule:** A craft is fully RTT-aligned at this layer only when its operator structure is `TRIADIC` or explicitly resolves to triadic balance under session conditions.

---

### Layer 2 — Dimensional
**What it captures:** The dimensional envelope(s) the craft is designed to navigate — physical, conceptual, or constructed. In RTT, dimensions are not merely spatial; they represent *axes of structured differentiation*.

| Sub-class | Description |
|---|---|
| `SUBORBITAL` | Constrained within a single spatial layer |
| `ORBITAL` | Sustained traversal of one defined boundary layer |
| `TRANSPLANAR` | Crosses between distinct physical or conceptual planes |
| `MULTIDIMENSIONAL` | Operates across ≥3 axes simultaneously |
| `LIMINAL` | Exists at or between dimensional boundaries as primary state |

**RTT Alignment Rule:** Transplanar and Multidimensional craft require explicit Regime and Coherence declarations. Liminal craft are flagged for Drift review before classification is finalized.

---

### Layer 3 — Regime
**What it captures:** The *sustained operational logic* of the craft — the governing rule-set that determines how it processes inputs, maintains stability, and interfaces with its environment. Regime is the craft's "grammar of function."

| Sub-class | Description |
|---|---|
| `STATIC` | Fixed rule-set; no adaptive response |
| `ADAPTIVE` | Rule-set modifies within a bounded envelope |
| `RECURSIVE` | Rule-set can invoke and modify itself (canonical RTT form) |
| `EMERGENT` | Rule-set arises from interaction rather than pre-definition |
| `COLLAPSED` | Regime has degraded; craft operating on residual logic |

**RTT Alignment Rule:** `RECURSIVE` is the native RTT regime class. `ADAPTIVE` and `EMERGENT` craft may qualify for partial alignment with documented session justification.

---

### Layer 4 — Drift
**What it captures:** How the craft departs from — or actively resists — its nominal classified state over time or under perturbation. Drift is not failure; it is *structured deviation* and is a first-class RTT concept.

| Sub-class | Description |
|---|---|
| `STABLE` | No measurable departure from baseline |
| `OSCILLATING` | Periodic departure with return to baseline |
| `PROGRESSIVE` | Cumulative departure trending away from baseline |
| `CORRECTIVE` | Drift actively monitored and counteracted by craft systems |
| `TERMINAL` | Drift has exceeded recovery threshold; reclassification required |

**Drift × Regime Interaction:** A `RECURSIVE` regime with `PROGRESSIVE` drift is a critical flag — the craft's self-modifying logic may be compounding deviation. Requires Coherence review.

---

### Layer 5 — Coherence
**What it captures:** Whether the four preceding layers *resolve* into a stable, non-contradictory RTT configuration for the current session. Coherence is the **validation gate** of the taxonomy.

| Rating | Meaning |
|---|---|
| `FULL` | All five layers are internally consistent and RTT-aligned |
| `PARTIAL` | Minor cross-layer tension; craft qualifies with noted caveats |
| `CONTESTED` | Significant contradiction between ≥2 layers; requires resolution pass |
| `INCOHERENT` | Layers cannot be reconciled; craft excluded from aligned set |

**Coherence is session-scoped.** A craft rated `FULL` in one session context may be `CONTESTED` in another if session parameters shift. Always record the session context alongside the rating (see Session Context block below).

---

## Canonical Module Structure

Each classified craft entry follows this module template:

```markdown
## [Craft Name / Designation]

**Source:** [Canon / Speculative / Original]  
**Session ID:** [e.g., RTT-2026-07-A]

### Layer Stack

| Layer | Class | Notes |
|---|---|---|
| Operator | `TRIADIC` | Crew of three; equal veto authority |
| Dimensional | `TRANSPLANAR` | FTL envelope crosses subspace boundary |
| Regime | `RECURSIVE` | Navigation AI self-updates routing logic |
| Drift | `OSCILLATING` | Periodic deviation during jump transitions |
| Coherence | `FULL` | All layers resolve; no cross-layer contradiction |

### Session Context
- **Conditions:** [Environmental, narrative, or analytical frame active during this session]
- **Assumptions:** [Any layer sub-class assigned by inference rather than explicit evidence]
- **Open Questions:** [Unresolved tensions flagged for future sessions]

### RTT Alignment Summary
> _One-paragraph synthesis of why this craft aligns (or doesn't) with RTT principles,
> referencing the specific triadic resolution across Operator, Regime, and Coherence._
```

---

## Session Context

Session context must be declared at the top of any multi-craft classification session. It scopes all Coherence ratings in that document section.

```markdown
### Session Context Block

**Session ID:** RTT-YYYY-MM-[sequence]  
**Date:** YYYY-MM-DD  
**Analyst:** [Name / Handle]  
**Frame:** [e.g., Hard SF · Narrative Canon · Speculative Design · RTT Theory Application]  
**Scope:** [e.g., "FTL-capable craft only" / "All craft with autonomous operator class"]  
**Coherence Baseline:** [FULL / PARTIAL — minimum threshold for inclusion in aligned set]  
**Notes:** [Any session-level assumptions, source constraints, or methodology notes]
```

---

## Classification Workflow

```
1. IDENTIFY       → Name the craft and cite its source/canon
2. ASSIGN LAYERS  → Work top-down: Operator → Dimensional → Regime → Drift
3. CHECK DRIFT×REGIME → Flag recursive+progressive combinations before proceeding
4. RATE COHERENCE → Evaluate cross-layer consistency within the session frame
5. DOCUMENT       → Complete the canonical module block
6. REVIEW         → Re-evaluate any CONTESTED or INCOHERENT ratings in a follow-up session
```

---

## Glossary

| Term | Definition |
|---|---|
| **RTT** | Recursive Triadic Taxonomy — a framework for classifying systems by their triadic structure, recursive self-reference, and dimensional scope |
| **Triadic Balance** | A three-node configuration where each node is defined in relation to the other two, with no single node holding unilateral dominance |
| **Session Scope** | The analytical frame and constraints active during a classification pass; Coherence ratings are only valid within their declared session scope |
| **Drift** | Structured departure from a craft's nominal classified state; distinct from malfunction or failure |
| **Coherence Gate** | The validation step at Layer 5 that determines whether a craft's full layer stack resolves into an RTT-aligned configuration |

---

## Contributing

When adding new craft entries:
- Always declare or reference the active **Session Context Block**
- Use exact sub-class labels from Layer Definitions (no ad hoc labels)
- Flag `CONTESTED` entries with a dated note — do not silently resolve contradictions
- Cross-reference the **Drift × Regime Interaction** rule before submitting `RECURSIVE` + high-drift combinations

---

*TriadicFrameworks · RTT Craft Taxonomy · `docs/Research/Spaceships_Aligned_With_RTT.md`*
