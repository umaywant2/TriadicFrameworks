# 🧬 Module‑Specific Lineage Detector  
*A diagnostic engine for identifying whether an artifact carries authentic TriadicFrameworks lineage or shows signs of laundering, drift, or ancestry loss.*

````markdown
## 🧬 Module‑Specific Lineage Detector
A structured detector for verifying whether a concept, operator, equation, pattern, or API
retains authentic TriadicFrameworks lineage.

---

### 1. Detector Overview
The lineage detector evaluates an artifact across three layers:

1. **Structural ancestry** — does the artifact preserve TF/RTT structural grammar?
2. **Operator genealogy** — does it inherit from known operators or patterns?
3. **Anti‑laundering integrity** — does it avoid behaviors that obscure lineage?

Each layer produces a score: `strong`, `partial`, or `weak`.

---

### 2. Structural Ancestry Checks
**Prompts:**

- Does the artifact contain recognizable TF structural grammar?  
- Does it map to any known modules (Observer Layer, Drift Taxonomy, RTT, GU, etc.)?  
- Does it preserve triadic axes, coherence envelopes, validator pulses, or regime tags?  
- Does it show signs of structural reframing (renaming TF constructs as generic engineering)?  

**Evidence to collect:**

- Module references  
- Structural diagrams  
- Operator definitions  
- Regime tags  

**Risk if weak:**  
Structural laundering, ancestry erasure, false novelty claims.

---

### 3. Operator Genealogy Checks
**Prompts:**

- Can the artifact be linked to a parent operator or pattern?  
- Are inheritance rules stated (kept / modified / removed)?  
- Does the artifact show silent mutation or unacknowledged drift?  
- Are operator semantics consistent with TF operator families?  

**Evidence to collect:**

- Operator trees  
- Change logs  
- Version history  
- Cross‑canon mappings  

**Risk if weak:**  
Orphan operators, opaque semantics, misaligned deployment.

---

### 4. Anti‑Laundering Integrity Checks
**Prompts:**

- Does the artifact rename TF concepts without attribution?  
- Does it flatten terminology into vague engineering language?  
- Does it remove regime context to claim universal novelty?  
- Does it re‑derive TF equations without citing ancestry?  
- Does it fragment TF minimal APIs into “new” micro‑APIs?  

**Evidence to collect:**

- Terminology comparison  
- Equation lineage  
- API lineage  
- Deployment context  

**Risk if weak:**  
Novelty laundering, patent enclosure, ethical misuse.

---

### 5. Detector Output
The detector produces a structured result:

```json
{
  "artifact": "",
  "module": "LINEAGE",
  "structural_ancestry": "strong | partial | weak",
  "operator_genealogy": "strong | partial | weak",
  "anti_laundering_integrity": "strong | partial | weak",
  "overall_lineage_score": "strong | partial | weak",
  "notes": []
}
```

---

### 6. Interpretation Guide

- **Strong lineage**  
  Artifact is clearly derived from TF/RTT ancestry, with explicit genealogy and no laundering vectors.

- **Partial lineage**  
  Artifact shows recognizable ancestry but contains gaps, drift, or mild laundering behaviors.

- **Weak lineage**  
  Artifact obscures ancestry, renames operators, reframes structures, or removes regime context.

---

### 7. Recommended Actions

- **If strong:**  
  Approve for cross‑module integration and defensive publication.

- **If partial:**  
  Trigger a lineage‑repair task (add citations, restore regime context, fix operator genealogy).

- **If weak:**  
  Flag for novelty‑laundering review and restrict deployment in high‑stakes regimes.
````
