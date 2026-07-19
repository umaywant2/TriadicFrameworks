# 💗 **COLLECTION_OPERATOR**  
### *RTT/1 Operator Specification — archive_org Module*

## **Identity**
- **Operator Name:** COLLECTION_OPERATOR  
- **Operator Family:** E‑Ops (Envelope Operators)  
- **Module:** archive_org  
- **Purpose:** Determine the object’s **dimensional envelope** by identifying its collection context, coherence clusters, related objects, and regime profile.

---

## **Purpose (One Sentence)**
The COLLECTION_OPERATOR places the target object inside its **dimensional envelope** by identifying its collection membership, coherence clusters, related objects, and structural regime context.

---

## **Inputs**
| Input | Type | Description |
|-------|------|-------------|
| `target` | URL | The webpage or object being analyzed. |
| `lineage_graph` | object | Structural evolution graph from LINEAGE_OPERATOR. |
| `regime_shifts` | list | Regime shift markers from LINEAGE_OPERATOR. |

---

## **Outputs**
| Output | Description |
|--------|-------------|
| `collection_id` | The Internet Archive collection or sub‑collection the object belongs to. |
| `coherence_clusters` | Structural clusters grouping related objects. |
| `related_objects` | Other IA objects structurally or contextually linked. |
| `regime_profile` | Combined regime identity across lineage + collection context. |

---

## **Operator Guarantees**
- No content‑based inference.  
- Collection membership is **structural**, not semantic.  
- Related objects are determined by **structural similarity**, not topic.  
- Regime profile is **derived**, not assumed.  
- Output is **deterministic** given IA metadata + lineage.

---

## **Dimensional Envelope (RTT/1)**
The dimensional envelope is the **structural context** surrounding an object:

- its collection  
- its cluster  
- its related objects  
- its regime profile  
- its lineage‑informed identity  

This envelope constrains how drift, stability, and continuity should be interpreted.

---

## **Collection Types**
| Collection | Notes |
|------------|-------|
| **govdocs** | High stability, institutional. |
| **news** | High drift, frequent redesigns. |
| **journals** | Medium drift, periodic updates. |
| **vintagesoftware** | Stable, versioned. |
| **cultural** | Mixed substrates, medium drift. |

---

## **Coherence Clusters**
Clusters are formed by structural similarity:

- shared templates  
- shared navigation skeleton  
- shared metadata patterns  
- shared lineage identifiers  

Clusters help determine whether the object is part of a larger structural family.

---

## **Operator Procedure**
1. Retrieve IA collection metadata for `target`.  
2. Identify collection membership (`collection_id`).  
3. Analyze structural similarity across related objects to form `coherence_clusters`.  
4. Identify related objects using:  
   - lineage identifiers  
   - collection metadata  
   - structural similarity  
5. Combine collection regime + lineage regime to produce `regime_profile`.  
6. Emit outputs for PRESERVATION_OPERATOR and DRIFTBOUND_RETRIEVAL_OPERATOR.

---

## **Failure Modes**
- **Missing collection metadata:** mark collection as `unknown`.  
- **Ambiguous clusters:** return multiple clusters with confidence scores.  
- **Sparse lineage:** regime profile may be incomplete.  

---

## **Hand‑Off to Next Operator**
Outputs feed directly into:

### **PRESERVATION_OPERATOR**  
- collection_id  
- regime_profile  

### **DRIFTBOUND_RETRIEVAL_OPERATOR**  
- coherence_clusters  
- related_objects  

---

## **Example (Synthetic)**
```
Input:
  target = "https://example.gov/records"
  lineage_graph = { ... }
  regime_shifts = ["2020: static → CMS"]

Output:
  collection_id = "govdocs"
  coherence_clusters = ["public-records", "agency-index"]
  related_objects = ["govdocs/records-archive"]
  regime_profile = "institutional (CMS-era)"
```

---

## **RTT/1 Mindset**
- Collections shape **expectations**, not conclusions.  
- Clusters reveal **structural families**, not topics.  
- Regime profile is **derived**, not assumed.  
- Dimensional envelope is essential for drift‑bounded reasoning.  
