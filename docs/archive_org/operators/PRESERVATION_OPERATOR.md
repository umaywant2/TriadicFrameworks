# 🟡 **PRESERVATION_OPERATOR**  
### *RTT/1 Operator Specification — archive_org Module*

## **Identity**
- **Operator Name:** PRESERVATION_OPERATOR  
- **Operator Family:** B‑Ops (Boundary / Substrate Operators)  
- **Module:** archive_org  
- **Purpose:** Evaluate the object’s **substrate stability**, **drift risk**, and **multi‑layer structure** to determine which versions are most reliable for continuity‑aligned retrieval.

---

## **Purpose (One Sentence)**
The PRESERVATION_OPERATOR assesses the object’s **substrate format**, **stability score**, **drift risk**, and **multi‑layer flags** to determine which snapshots are structurally trustworthy.

---

## **Inputs**
| Input | Type | Description |
|-------|------|-------------|
| `target` | URL | The object being evaluated. |
| `collection_id` | string | Collection context from COLLECTION_OPERATOR. |
| `regime_profile` | string | Combined regime identity from COLLECTION_OPERATOR. |
| `continuity_kernel` | list | Stable structural elements from LINEAGE_OPERATOR. |
| `transformations` | list | Structural changes from LINEAGE_OPERATOR. |

---

## **Outputs**
| Output | Description |
|--------|-------------|
| `format` | The detected substrate format (html, pdf, image, ocr, mixed). |
| `stability_score` | Numerical stability estimate (0–1). |
| `drift_risk` | Expected drift level based on substrate + regime. |
| `multi_layer_flags` | Indicators for mixed or layered substrates. |

---

## **Operator Guarantees**
- No content‑based inference.  
- Substrate classification is **structural**, not semantic.  
- Stability score is **evidence‑based**, not assumed.  
- Drift risk is **predictive**, not retrospective.  
- Mixed substrates are handled explicitly, not collapsed.

---

## **Substrate Stability (RTT/1)**
| Substrate | Stability | Notes |
|-----------|-----------|-------|
| **pdf** | high | Static, layout‑preserving. |
| **image** | high | Stable but incomplete. |
| **html** | medium | Layout‑dependent, drift‑prone. |
| **cms‑html** | medium/low | Template‑driven, redesign‑prone. |
| **ocr** | low | Lossy, structurally degraded. |
| **mixed** | variable | Requires multi‑layer analysis. |

---

## **Drift Risk Levels**
| Level | Meaning |
|-------|---------|
| **low** | Stable substrate, minimal expected drift. |
| **medium** | Occasional structural changes. |
| **high** | Frequent redesigns, migrations, or lossy layers. |

---

## **Multi‑Layer Flags**
Examples:
- `pdf + html`  
- `image + ocr`  
- `html + js‑rendered`  
- `flash + html5`  

Multi‑layer objects require careful stability evaluation.

---

## **Operator Procedure**
1. Detect substrate format(s) for the target.  
2. Evaluate stability based on:  
   - substrate type  
   - collection context  
   - regime profile  
   - continuity kernel  
   - transformations  
3. Compute stability score (0–1).  
4. Assign drift risk (low/medium/high).  
5. Identify multi‑layer structures.  
6. Emit outputs for DRIFTBOUND_RETRIEVAL_OPERATOR.

---

## **Failure Modes**
- **Ambiguous substrate:** mark as `mixed`.  
- **Missing layers:** lower stability score.  
- **OCR‑only snapshots:** mark as high drift risk.  

---

## **Hand‑Off to Next Operator**
Outputs feed directly into:

### **DRIFTBOUND_RETRIEVAL_OPERATOR**  
- format  
- stability_score  
- drift_risk  
- multi_layer_flags  

---

## **Example (Synthetic)**
```
Input:
  target = "https://example.gov/records"
  collection_id = "govdocs"
  regime_profile = "institutional (CMS-era)"
  continuity_kernel = ["header", "footer", "records-index"]
  transformations = ["CMS migration", "PDF layer added"]

Output:
  format = "html + pdf"
  stability_score = 0.78
  drift_risk = "medium"
  multi_layer_flags = ["html", "pdf"]
```

---

## **RTT/1 Mindset**
- Substrate determines **trustworthiness**, not content.  
- Stability is **measured**, not assumed.  
- Mixed substrates require **layer‑aware reasoning**.  
- Drift risk must be **explicit** in the final summary.  
