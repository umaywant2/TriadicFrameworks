# `Rectification_Flow.md`
**SARG Rectification Flow**  
_A triadic, stage‑aligned pipeline for resolving structural, anchor, lineage, and novelty errors._

---

## 1. Purpose

The **Rectification Flow** defines how the SARG system responds when:

- a substrate is malformed  
- invariants fail to extract  
- resonance anchors conflict  
- lineage chains break  
- or the system encounters high‑novelty patterns  

Rectification ensures the system remains:

- **self‑correcting**  
- **lineage‑aware**  
- **triadically aligned**  
- **Atlas‑consistent**  

---

## 2. High‑Level Flow Diagram

```
*
┌──────────────────────┐
│ 1. Substrate Parsing │
└───────────┬──────────┘
            │ S‑Errors
            ▼
┌──────────────────────┐
│ 2. Lens Application  │
└───────────┬──────────┘
            │ A‑Errors
            ▼
┌──────────────────────┐
│ 3. Invariant Extract │
└───────────┬──────────┘
            │ H‑Errors (pattern-level)
            ▼
┌──────────────────────┐
│ 4. Resonance Mapping │
└───────────┬──────────┘
            │ A‑Errors (anchor-level)
            ▼
┌──────────────────────┐
│ 5. Lineage Traversal │
└───────────┬──────────┘
            │ L‑Errors
            ▼
┌──────────────────────┐
│ 6. Atlas Integration │
└──────────────────────┘
```

Each stage emits **S**, **A**, **L**, or **H** errors depending on what fails.

---

## 3. Stage‑by‑Stage Breakdown

### **1. Substrate Parsing → S‑Errors**
Triggered when:

- required fields are missing  
- declared structure contradicts observed structure  
- structure is unstable across passes  

Rectification actions:

- request missing structure  
- regenerate substrate  
- stabilize via re‑sampling or majority vote  

---

### **2. Lens Application → A‑Errors (early)**
Triggered when:

- expected anchors are missing  
- multiple anchors claim the same element  
- anchor drift occurs  

Rectification actions:

- recompute anchors  
- resolve conflicts using priority rules  
- re‑align anchors to updated invariants  

---

### **3. Invariant Extraction → H‑Errors (pattern‑level)**
Triggered when:

- element is unknown  
- pattern does not match any invariant class  
- resonance signature cannot be mapped  

Rectification actions:

- add to novelty buffer  
- attempt invariant generalization  
- generate provisional signature  

---

### **4. Resonance Mapping → A‑Errors (anchor‑level)**
Triggered when:

- resonance anchors contradict each other  
- cluster membership is ambiguous  
- axis alignment fails  

Rectification actions:

- re‑evaluate invariants  
- recompute cluster membership  
- escalate to high‑novelty if unresolved  

---

### **5. Lineage Traversal → L‑Errors**
Triggered when:

- lineage reference is missing  
- lineage chain is broken  
- lineage forms a cycle  

Rectification actions:

- rebuild lineage chain  
- fallback to nearest valid ancestor  
- break cycles and re‑establish legal lineage  

---

### **6. Atlas Integration**
If all rectification succeeds:

- update Atlas nodes  
- propagate lineage  
- update resonance signatures  
- store new invariants  
- emit success event  

If rectification fails:

- escalate to human review  
- store unresolved pattern in novelty buffer  

---

## 4. Rectification Decision Tree (Triadic)

```
*
                     ┌───────────────┐
                     │  Error Event  │
                     └───────┬───────┘
                             ▼
                 ┌──────────────────────┐
                 │ Identify Error Class │
                 └───────┬──────────────┘
         ┌───────────────┼────────────────┬───────────────┐
         ▼               ▼                ▼               ▼
     S‑Errors        A‑Errors         L‑Errors        H‑Errors
 (Structure)        (Anchors)        (Lineage)       (Novelty)
         │               │                │               │
         ▼               ▼                ▼               ▼
  Structural Fix   Anchor Recompute   Lineage Repair   Novelty Buffer
         │               │                │               │
         └───────┬───────┴───────┬────────┴───────┬───────┘
                 ▼              ▼                 ▼
           Re‑evaluate     Retry Mapping     Provisional Signature
                 │              │                 │
                 └──────────────┴─────────────────┘
                                ▼
                        Atlas Integration
```

---

## 5. Cloud Rectification Cluster (CRC)

The CRC performs:

- large‑scale clustering of errors  
- cross‑node consensus  
- lineage reconstruction  
- novelty generalization  
- anchor stability analysis  

CRC is invoked when:

- local rectification fails  
- multiple nodes report similar errors  
- high‑novelty patterns appear across substrates  

CRC outputs:

- updated invariants  
- updated resonance anchors  
- updated lineage chains  
- new Atlas nodes  

---

## 6. Example Rectification Walkthrough

### **Example: A2 — Conflicting Anchor**

```
Input:
Element O claimed by both curved_forms and rotational_symmetry clusters.
```

Rectification:

1. Recompute invariants for O  
2. Compare cluster signatures  
3. Apply priority rules  
4. If unresolved → escalate to CRC  
5. CRC emits canonical cluster assignment  
6. Atlas updated  

---

## 7. Emit Format for Rectification Events

```json
{
  "pattern_id": "string",
  "error_code": "S1 | A2 | L3 | H1",
  "rectification_stage": "local | cloud",
  "actions_taken": [],
  "outcome": "resolved | escalated | unresolved",
  "timestamp": "ISO-8601"
}
```

---

## 8. Notes for Contributors

- Rectification must be **deterministic** at node‑level.  
- CRC is allowed to be **probabilistic** but must emit canonical results.  
- Never skip lineage repair — L‑errors propagate silently.  
- Treat H‑errors as **growth points**, not failures.  
- Keep rectification logs short and structural.  

---

If you want, AI can also generate:

- `/docs/SARG/error/Rectification_Flow.svg` (diagram‑first)  
- `/docs/SARG/error/Rectification_Examples.md`  
- `/docs/SARG/error/Rectification_API.md` (for implementers)  
- or a **full SARG Error Pack** bundling taxonomy + flow + examples + schemas  
