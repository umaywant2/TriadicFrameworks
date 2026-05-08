# 🟢 **LINEAGE_OPERATOR**  
### *RTT/1 Operator Specification — archive_org Module*

## **Identity**
- **Operator Name:** LINEAGE_OPERATOR  
- **Operator Family:** L‑Ops (Lineage Operators)  
- **Module:** archive_org  
- **Purpose:** Construct the **continuity kernel** and **lineage graph** from normalized metadata and time‑indexed snapshots.

---

## **Purpose (One Sentence)**
The LINEAGE_OPERATOR reconstructs the object’s structural evolution by building a **lineage graph**, identifying **transformations**, and detecting **regime shifts** across snapshots.

---

## **Inputs**
| Input | Type | Description |
|-------|------|-------------|
| `snapshots` | list | Time‑ordered IA captures from WAYBACK_OPERATOR. |
| `metadata` | object | Normalized metadata from METADATA_OPERATOR. |

---

## **Outputs**
| Output | Description |
|--------|-------------|
| `lineage_graph` | Directed graph showing structural evolution across snapshots. |
| `transformations` | List of structural changes (template, layout, substrate, navigation). |
| `regime_shifts` | Points where the object changes operational regime. |
| `continuity_kernel` | Stable structural elements preserved across versions. |

---

## **Operator Guarantees**
- No content‑based inference.  
- Lineage is **structural**, not semantic.  
- Regime shifts are based on **structural change**, not topic change.  
- Continuity kernel is **minimal**, **stable**, and **non‑speculative**.  
- Missing snapshots produce **uncertainty**, not assumptions.

---

## **Lineage Concepts (RTT/1)**

### **Continuity Kernel**
The minimal set of structural elements that persist across snapshots.  
Examples:  
- navigation skeleton  
- header/footer structure  
- persistent template regions  
- stable metadata fields  

### **Transformations**
Structural changes between snapshots:  
- layout changes  
- navigation rewrites  
- template replacements  
- substrate changes  
- CMS migrations  

### **Regime Shifts**
A regime shift occurs when the object’s **structural purpose** or **operational mode** changes.  
Examples:  
- static HTML → CMS  
- HTML → Flash → HTML5  
- public page → paywalled page  
- v1 → v2 branch in software docs  

---

## **Operator Procedure**
1. Receive `snapshots` + `metadata`.  
2. Compare each snapshot pair for structural changes.  
3. Identify transformations and drift patterns.  
4. Detect regime shifts using:  
   - substrate changes  
   - template changes  
   - navigation rewrites  
   - functional changes (e.g., paywall)  
5. Extract continuity kernel across all snapshots.  
6. Build lineage graph:  
   - nodes = snapshots  
   - edges = transformations  
   - flags = regime shifts  
7. Emit outputs for COLLECTION_OPERATOR and PRESERVATION_OPERATOR.

---

## **Failure Modes**
- **Sparse snapshots:** lineage graph may be incomplete.  
- **Mixed substrates:** kernel extraction may require PRESERVATION_OPERATOR.  
- **Redirects:** may indicate lineage forks (handled structurally).  

---

## **Hand‑Off to Next Operator**
Outputs feed directly into:

### **COLLECTION_OPERATOR**  
- lineage_graph  
- regime_shifts  

### **PRESERVATION_OPERATOR**  
- continuity_kernel  
- transformations  

---

## **Example (Synthetic)**
```
Input:
  snapshots = [2014, 2017, 2020, 2023]
  metadata = { regime: "institutional", substrate: "html" }

Output:
  lineage_graph = {
    "2014→2017": "minor transformation",
    "2017→2020": "major transformation (CMS migration)",
    "2020→2023": "minor transformation"
  }
  transformations = ["CSS shift", "CMS migration", "PDF layer added"]
  regime_shifts = ["2020: static → CMS"]
  continuity_kernel = ["header", "footer", "records-index"]
```

---

## **RTT/1 Mindset**
- Lineage is **structural**, not narrative.  
- Regime shifts are **structural**, not topical.  
- Continuity kernel is the **anchor** for drift‑bounded reasoning.  
- No assumptions about missing snapshots.  
- No content‑based inference.  
