# `SARG_Error_Taxonomy.md`
**SARG Error Taxonomy**  
_A unified triadic classification system for structural, anchor, lineage, and novelty‑driven errors across any SARG‑described substrate._

---

## 1. Overview

The **SARG Error Taxonomy** provides a universal grammar for describing, classifying, and resolving errors that arise during:

- substrate parsing  
- lens application  
- invariant extraction  
- resonance mapping  
- lineage traversal  
- cross‑substrate synthesis  

Errors are grouped into **four primary classes**, each aligned with a SARG operator:

| Class | Operator | Meaning |
|-------|----------|---------|
| **S‑Errors** | Structure | Something is malformed, missing, or contradictory in the substrate or its declared structure. |
| **A‑Errors** | Anchors | Resonance anchors, axes, or cluster mappings fail or conflict. |
| **L‑Errors** | Lineage | Lineage chains, inheritance paths, or cross‑substrate references break. |
| **H‑Errors** | High‑Novelty | The system encounters something outside its known invariants or resonance space. |

Each class contains **three subtypes**, forming a triadic 3×3 grid.

---

## 2. The SARG 3×3 Error Grid

### **S‑Errors (Structural)**
Structural errors arise when the substrate or its declared shape cannot be trusted.

| Code | Name | Description |
|------|------|-------------|
| **S1** | Missing Structure | Required fields, elements, or properties are absent. |
| **S2** | Contradictory Structure | Declared structure conflicts with observed structure. |
| **S3** | Unstable Structure | Structure is present but inconsistent across passes. |

---

### **A‑Errors (Anchor)**
Anchor errors occur when resonance anchors cannot be established or maintained.

| Code | Name | Description |
|------|------|-------------|
| **A1** | Missing Anchor | Expected anchor or cluster not found. |
| **A2** | Conflicting Anchor | Multiple anchors claim the same element. |
| **A3** | Drifted Anchor | Anchor exists but no longer matches invariants. |

---

### **L‑Errors (Lineage)**
Lineage errors arise when the system cannot trace or validate lineage relationships.

| Code | Name | Description |
|------|------|-------------|
| **L1** | Missing Lineage | Required lineage reference not found. |
| **L2** | Broken Lineage | Lineage chain exists but cannot be resolved. |
| **L3** | Cyclic Lineage | Lineage forms a loop or illegal recursion. |

---

### **H‑Errors (High‑Novelty)**
High‑novelty errors indicate the system has encountered something outside its known resonance space.

| Code | Name | Description |
|------|------|-------------|
| **H1** | Novel Element | Element not in substrate or known invariants. |
| **H2** | Novel Pattern | Pattern does not match any known invariant class. |
| **H3** | Novel Resonance | Resonance signature cannot be mapped. |

---

## 3. Error Event Shape (Canonical)

Every SARG error is represented using the standard event shape:

```json
{
  "pattern_id": "string",
  "source_node": "string",
  "timestamp": "ISO-8601",
  "sarg_stage": "substrate | lens | invariants | resonance | lineage",
  "error_code": "S1 | S2 | ... | H3",
  "details": {
    "message": "Human-readable description",
    "context": {},
    "suggested_rectification": "optional"
  }
}
```

This shape is used by:

- local node validators  
- the Cloud Rectification Cluster  
- lineage walkers  
- resonance mappers  
- substrate loaders  

---

## 4. Rectification Actions (Summary Table)

This table matches the one we generated earlier, now embedded in the taxonomy.

| Error Code | Rectification Action |
|------------|----------------------|
| **S1** | Request missing structure or regenerate substrate. |
| **S2** | Reconcile contradictions or choose canonical structure. |
| **S3** | Stabilize structure via re‑sampling or majority vote. |
| **A1** | Recompute anchors from invariants. |
| **A2** | Resolve anchor conflicts using priority rules. |
| **A3** | Re‑align anchor to updated invariants. |
| **L1** | Request missing lineage or fallback to root. |
| **L2** | Rebuild lineage chain using nearest valid nodes. |
| **L3** | Break cycle and re‑establish legal lineage. |
| **H1** | Add element to novelty buffer for human review. |
| **H2** | Attempt invariant generalization. |
| **H3** | Create provisional resonance signature. |

---

## 5. Error Flow (SARG‑Aligned)

```
[Substrate] → S‑Errors
      ↓
[Lens Application] → A‑Errors
      ↓
[Invariant Extraction] → H‑Errors (pattern-level)
      ↓
[Resonance Mapping] → A‑Errors (anchor-level)
      ↓
[Lineage Traversal] → L‑Errors
```

This flow mirrors the Capture.md pipeline you have open.

---

## 6. High‑Novelty Handling

High‑novelty events (H‑class) are not “failures” — they are **expansion points**.

The system:

1. Captures the novel element/pattern/resonance  
2. Stores it in the novelty buffer  
3. Attempts generalization  
4. Emits a provisional signature  
5. Awaits human confirmation  

This is how SARG evolves.

---

## 7. Example Error Events

### Example 1 — Missing Structure (S1)

```json
{
  "pattern_id": "latin_A",
  "source_node": "substrate_loader",
  "timestamp": "2026-04-20T14:00:00",
  "sarg_stage": "substrate",
  "error_code": "S1",
  "details": {
    "message": "Substrate missing required field: elements",
    "context": {}
  }
}
```

### Example 2 — Conflicting Anchor (A2)

```json
{
  "pattern_id": "letter_O",
  "source_node": "resonance_mapper",
  "timestamp": "2026-04-20T14:01:00",
  "sarg_stage": "resonance",
  "error_code": "A2",
  "details": {
    "message": "Element O claimed by both curved_forms and rotational_symmetry clusters.",
    "context": {}
  }
}
```

---

## 8. Notes for Implementers

- Keep error messages **short, structural, and substrate‑agnostic**.  
- Never embed domain‑specific assumptions in error codes.  
- Use **triadic grouping** to maintain SARG coherence.  
- Emit **H‑class errors** liberally — they are how the system learns.  
- Maintain lineage integrity; L‑errors are the most expensive to repair.  

---

If you want, AI can also generate:

- `/docs/SARG/error/SARG_Error_Examples.json`  
- `/docs/SARG/error/rectification_flow.md` (diagram‑first)  
- `/docs/SARG/error/error_signatures.json` (machine‑readable)  
- or fold all of this into a **SARG Error Pack** for the repo.
