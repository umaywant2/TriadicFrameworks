# 🟣 **METADATA_OPERATOR**  
### *RTT/1 Operator Specification — archive_org Module*

## **Identity**
- **Operator Name:** METADATA_OPERATOR  
- **Operator Family:** R‑Ops (Registry / Root Operators)  
- **Module:** archive_org  
- **Purpose:** Normalize Internet Archive metadata into RTT grammar to determine substrate, regime, drift sensitivity, coherence, and lineage identifiers.

---

## **Purpose (One Sentence)**
The METADATA_OPERATOR extracts and normalizes IA metadata to identify the object’s **substrate type**, **regime**, **drift sensitivity**, **coherence**, and **lineage identifiers** before any temporal analysis occurs.

---

## **Inputs**
| Input | Type | Description |
|-------|------|-------------|
| `target` | URL | The webpage or object whose metadata is being analyzed. |

---

## **Outputs**
| Output | Description |
|--------|-------------|
| `substrate_type` | The structural substrate (html, pdf, image, mixed, etc.). |
| `regime` | The object’s operational regime (institutional, media, scholarly, cultural, etc.). |
| `drift_sensitivity` | Expected drift level based on substrate + regime. |
| `coherence` | Internal structural consistency of the object. |
| `lineage_ids` | Identifiers linking the object to collections, clusters, or prior versions. |

---

## **Operator Guarantees**
- No content‑based inference.  
- Metadata is treated as **structural hints**, not ground truth.  
- Drift sensitivity is **predictive**, not retrospective.  
- Regime classification is **structural**, not semantic.  
- Output is **deterministic** given the same IA metadata.

---

## **Substrate Types (RTT/1)**
| Substrate | Notes |
|-----------|-------|
| **html** | Drift‑prone, layout‑dependent. |
| **pdf** | Stable, low drift. |
| **image** | Stable but incomplete. |
| **ocr** | Lossy, high drift. |
| **mixed** | Requires PRESERVATION_OPERATOR to resolve. |

---

## **Regime Types**
| Regime | Meaning |
|--------|---------|
| **institutional** | Government, agency, or official records. |
| **media** | News, blogs, high‑update environments. |
| **scholarly** | Academic, research, journals. |
| **cultural** | Museums, exhibits, archives. |
| **technical** | Software, documentation, versioned systems. |

---

## **Drift Sensitivity Levels**
| Level | Meaning |
|-------|---------|
| **low** | Expected stability (PDF, institutional). |
| **medium** | Occasional structural change. |
| **high** | Frequent redesigns, CMS migrations. |

---

## **Coherence Levels**
| Level | Meaning |
|-------|---------|
| **high** | Strong structural consistency. |
| **medium** | Some inconsistencies. |
| **low** | Fragmented or unstable structure. |

---

## **Operator Procedure**
1. Retrieve IA metadata for `target`.  
2. Normalize fields into RTT grammar:  
   - substrate  
   - regime  
   - drift_sensitivity  
   - coherence  
   - lineage identifiers  
3. Validate substrate classification.  
4. Predict drift sensitivity based on substrate + regime.  
5. Emit normalized metadata for WAYBACK_OPERATOR and LINEAGE_OPERATOR.

---

## **Failure Modes**
- **Missing metadata:** return null fields + warning.  
- **Ambiguous substrate:** mark as `mixed` and defer to PRESERVATION_OPERATOR.  
- **Contradictory metadata:** flag for drift‑bounded review.  

---

## **Hand‑Off to Next Operator**
Outputs feed directly into:

### **WAYBACK_OPERATOR**  
- substrate_type  
- drift_sensitivity  

### **LINEAGE_OPERATOR**  
- regime  
- coherence  
- lineage_ids  

---

## **Example (Synthetic)**
```
Input:
  target = "https://example.gov/records"

Output:
  substrate_type = "html"
  regime = "institutional"
  drift_sensitivity = "low"
  coherence = "high"
  lineage_ids = ["govdocs-root"]
```

---

## **RTT/1 Mindset**
- Metadata is **structural**, not semantic.  
- Drift sensitivity is **predictive**, not retrospective.  
- Regime classification informs expectations, not conclusions.  
- Metadata never overrides observed drift.  
