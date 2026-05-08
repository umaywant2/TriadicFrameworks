# 🟣 **DRIFTBOUND_RETRIEVAL_OPERATOR**  
### *RTT/1 Operator Specification — archive_org Module*

## **Identity**
- **Operator Name:** DRIFTBOUND_RETRIEVAL_OPERATOR  
- **Operator Family:** C‑Ops (Continuity Operators)  
- **Module:** archive_org  
- **Purpose:** Produce the **final drift‑bounded retrieval**, synthesizing all upstream operator outputs into a safe, continuity‑aligned answer.

---

## **Purpose (One Sentence)**
The DRIFTBOUND_RETRIEVAL_OPERATOR generates the final **continuity‑aligned**, **substrate‑aware**, **drift‑bounded** answer using all upstream operator outputs.

---

## **Inputs**
| Input | Type | Description |
|-------|------|-------------|
| `snapshots` | list | Time‑ordered captures from WAYBACK_OPERATOR. |
| `drift_map` | object | Structural drift levels between snapshots. |
| `continuity_breaks` | list | Gaps or discontinuities in the timeline. |
| `lineage_graph` | object | Structural evolution graph from LINEAGE_OPERATOR. |
| `regime_shifts` | list | Regime shift markers from LINEAGE_OPERATOR. |
| `collection_id` | string | Collection context from COLLECTION_OPERATOR. |
| `coherence_clusters` | list | Structural clusters from COLLECTION_OPERATOR. |
| `related_objects` | list | Related IA objects from COLLECTION_OPERATOR. |
| `format` | string | Substrate format from PRESERVATION_OPERATOR. |
| `stability_score` | number | Stability estimate from PRESERVATION_OPERATOR. |
| `drift_risk` | string | Expected drift level from PRESERVATION_OPERATOR. |
| `multi_layer_flags` | list | Substrate layers from PRESERVATION_OPERATOR. |

---

## **Outputs**
| Output | Description |
|--------|-------------|
| `answer` | Final drift‑bounded retrieval. |
| `earliest_stable_version` | First structurally stable snapshot. |
| `most_reliable_version` | Snapshot with highest substrate stability. |
| `key_changes` | Summary of major structural transformations. |
| `warnings` | Drift, continuity, or substrate warnings. |

---

## **Operator Guarantees**
- No content‑based inference.  
- All reasoning is **structural**, not semantic.  
- Drift is **explicit**, never implied.  
- Continuity is **preserved**, never assumed.  
- Substrate stability is **mandatory** in the final answer.  
- Missing snapshots produce **uncertainty**, not assumptions.  

---

## **Final Summary Requirements (RTT/1)**  
Every drift‑bounded summary must include:

1. **Earliest stable version**  
2. **Most reliable version**  
3. **Key structural changes**  
4. **Continuity breaks** (if any)  
5. **Regime shifts** (if any)  
6. **Substrate stability + drift risk**  
7. **Warnings** (mandatory if drift > none)

This is the **canonical output contract** for the entire module.

---

## **Operator Procedure**
1. Identify earliest stable version using:  
   - continuity kernel  
   - drift_map  
   - stability_score  
2. Identify most reliable version using:  
   - substrate stability  
   - multi_layer_flags  
   - regime_profile  
3. Summarize structural changes using:  
   - transformations  
   - regime_shifts  
   - drift_map  
4. Detect continuity issues using:  
   - continuity_breaks  
   - missing snapshots  
5. Generate drift‑bounded warnings.  
6. Produce final answer object.

---

## **Failure Modes**
- **No stable snapshots:** return null + high‑drift warning.  
- **Mixed substrates:** require explicit layer‑aware warnings.  
- **High drift:** final answer must include caution.  

---

## **Example (Synthetic)**
```
Input:
  snapshots = [2014, 2017, 2020, 2023]
  drift_map = { "2014→2017": "minor", "2017→2020": "high", "2020→2023": "minor" }
  continuity_breaks = []
  lineage_graph = { ... }
  regime_shifts = ["2020: static → CMS"]
  collection_id = "govdocs"
  format = "html + pdf"
  stability_score = 0.78
  drift_risk = "medium"

Output:
  earliest_stable_version = 2014
  most_reliable_version = 2023 (PDF layer)
  key_changes = ["CSS shift", "CMS migration", "PDF layer added"]
  warnings = ["High drift detected in 2017→2020", "HTML substrate is drift‑prone"]
  answer = "The most reliable version is the 2023 PDF snapshot..."
```

---

## **RTT/1 Mindset**
- Retrieval is **continuity‑aligned**, not snapshot‑aligned.  
- Stability > recency.  
- Drift must be **explicit**.  
- Substrate determines **trustworthiness**.  
- No speculation.  
- No content‑based inference.  
