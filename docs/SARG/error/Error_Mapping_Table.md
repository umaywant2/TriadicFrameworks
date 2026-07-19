# `Error_Mapping_Table.md`
**SARG Error → Rectification Mapping Table**  
_A complete mapping of all SARG error codes (S1–H3) to their rectification actions, decision logic, and escalation paths._

This table is the **single source of truth** for how the system responds to each error type across:

- substrate parsing  
- lens application  
- invariant extraction  
- resonance mapping  
- lineage traversal  
- novelty handling  

It is intentionally **triadic**, **structural**, and **implementation‑ready**.

---

## 1. Full Error → Action Mapping Table

| Error Code | Class | Meaning | Trigger Conditions | Primary Rectification | Secondary / Escalation |
|-----------|--------|----------|--------------------|------------------------|--------------------------|
| **S1** | Structure | Missing Structure | Required fields, elements, or properties absent | Request missing structure or regenerate substrate | Escalate to CRC if substrate cannot be reconstructed |
| **S2** | Structure | Contradictory Structure | Declared structure conflicts with observed structure | Reconcile contradictions or choose canonical structure | CRC consensus if multiple nodes disagree |
| **S3** | Structure | Unstable Structure | Structure inconsistent across passes | Stabilize via re‑sampling or majority vote | CRC stabilization sweep |
| **A1** | Anchor | Missing Anchor | Expected anchor or cluster not found | Recompute anchors from invariants | CRC anchor inference |
| **A2** | Anchor | Conflicting Anchor | Multiple anchors claim same element | Resolve conflicts using priority rules | CRC anchor arbitration |
| **A3** | Anchor | Drifted Anchor | Anchor no longer matches invariants | Re‑align anchor to updated invariants | CRC drift‑correction |
| **L1** | Lineage | Missing Lineage | Required lineage reference not found | Request missing lineage or fallback to root | CRC lineage reconstruction |
| **L2** | Lineage | Broken Lineage | Lineage chain exists but cannot be resolved | Rebuild lineage chain using nearest valid nodes | CRC chain repair |
| **L3** | Lineage | Cyclic Lineage | Illegal recursion or loop detected | Break cycle and re‑establish legal lineage | CRC cycle‑breaker |
| **H1** | Novelty | Novel Element | Element not in substrate or known invariants | Add to novelty buffer for human review | CRC novelty clustering |
| **H2** | Novelty | Novel Pattern | Pattern does not match any invariant class | Attempt invariant generalization | CRC pattern generalization |
| **H3** | Novelty | Novel Resonance | Resonance signature cannot be mapped | Create provisional resonance signature | CRC resonance synthesis |

---

## 2. Triadic 3×3 Grid (Canonical Layout)

```
*
┌───────────────┬───────────────┬────────────────┐
│   S‑Errors    │   A‑Errors    │    L‑Errors    │
│ (Structure)   │  (Anchors)    │   (Lineage)    │
├───────────────┼───────────────┼────────────────┤
│ S1 Missing    │ A1 Missing    │ L1 Missing     │
│ Structure     │ Anchor        │ Lineage        │
├───────────────┼───────────────┼────────────────┤
│ S2 Contradic. │ A2 Conflict   │ L2 Broken      │
│ Structure     │ Anchor        │ Lineage        │
├───────────────┼───────────────┼────────────────┤
│ S3 Unstable   │ A3 Drifted    │ L3 Cyclic      │
│ Structure     │ Anchor        │ Lineage        │
└───────────────┴───────────────┴────────────────┘

                 H‑Errors (High‑Novelty)
                 H1 Novel Element
                 H2 Novel Pattern
                 H3 Novel Resonance
```

---

## 3. Error → Stage Mapping

| SARG Stage | Possible Errors | Notes |
|------------|-----------------|-------|
| **Substrate Parsing** | S1, S2, S3 | Structural integrity failures |
| **Lens Application** | A1, A2, A3 | Early anchor failures |
| **Invariant Extraction** | H1, H2 | Pattern‑level novelty |
| **Resonance Mapping** | A2, A3, H3 | Anchor conflicts or resonance novelty |
| **Lineage Traversal** | L1, L2, L3 | Lineage integrity failures |
| **Atlas Integration** | — | Errors escalate here if unresolved |

---

## 4. Rectification Priority Rules

Rectification always follows this order:

1. **Fix Structure (S‑Errors)**  
2. **Fix Anchors (A‑Errors)**  
3. **Handle Novelty (H‑Errors)**  
4. **Repair Lineage (L‑Errors)**  
5. **Integrate into Atlas**

If any step fails → escalate to CRC.

---

## 5. CRC (Cloud Rectification Cluster) Mapping

| Error Class | CRC Role |
|-------------|----------|
| **S‑Errors** | Structural consensus, canonicalization |
| **A‑Errors** | Anchor arbitration, drift correction |
| **L‑Errors** | Lineage reconstruction, cycle breaking |
| **H‑Errors** | Novelty clustering, generalization, signature synthesis |

CRC emits:

- updated invariants  
- updated anchors  
- updated lineage chains  
- new resonance signatures  
- new Atlas nodes  

---

## 6. Example Mapping Snippets

### **Example: A2 → Anchor Conflict**

```
Input:
Element O claimed by both curved_forms and rotational_symmetry clusters.

Mapping:
A2 → Anchor Conflict
Rectification: resolve via priority rules → if unresolved → CRC arbitration
```

### **Example: H2 → Novel Pattern**

```
Input:
Pattern does not match any known invariant class.

Mapping:
H2 → Novel Pattern
Rectification: attempt invariant generalization → if unresolved → CRC pattern generalization
```

---

## 7. Notes for Contributors

- Keep mappings **stable**, **triadic**, and **substrate‑agnostic**.  
- Never introduce domain‑specific error codes.  
- All new error types must fit into the S/A/L/H structure.  
- CRC escalation should be rare but deterministic.  
- Mapping tables must remain machine‑readable.  

---

If you want, AI can also generate:

- **Error_Mapping_Table.json** (machine‑readable version)  
- **Error_Mapping_Examples.md** (teaching‑first)  
- **Error_Signatures.md** (canonical signatures for each error)  
- or a **full SARG Error Pack** bundling taxonomy + flow + mapping + examples  
