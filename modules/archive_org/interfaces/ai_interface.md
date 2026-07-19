# 🟪 **AI Interface — archive_org Module**  
### *RTT/1 Interface Specification*

## **Identity**
- **Interface Name:** ai_interface  
- **Module:** archive_org  
- **Purpose:** Define the contract, modes, inputs, outputs, and behavioral rules for AI agents interacting with the Internet Archive using the RTT operator chain.

---

# 1. **Interface Purpose**
The AI interface provides a **strict, deterministic, operator‑first contract** that governs how an AI agent must:

- receive requests  
- execute the six‑operator chain  
- enforce drift‑bounded reasoning  
- avoid content‑based inference  
- produce continuity‑aligned answers  

This interface is the **only valid entrypoint** for AI execution in the archive_org module.

---

# 2. **Entrypoint**

The AI interface exposes a single entrypoint:

```
archive_org_agent.handle_request(goal, target, constraints)
```

Where:

- **goal** = what the user wants (explain, audit, compare, locate_stable)  
- **target** = the IA URL  
- **constraints** = optional filters (time range, snapshot limits, etc.)

The entrypoint **must** execute the full operator chain before producing any answer.

---

# 3. **Inputs**

| Field | Type | Description |
|-------|------|-------------|
| `goal` | string | The agent’s mode (explain, audit, compare, locate_stable). |
| `target` | URL | The Internet Archive object to analyze. |
| `constraints` | object (optional) | Time range, snapshot filters, or structural constraints. |

---

# 4. **Outputs**

| Field | Description |
|--------|-------------|
| `answer` | Final drift‑bounded retrieval. |
| `operators_used` | List of operators executed (always all six). |
| `warnings` | Drift, continuity, or substrate warnings. |
| `artifacts` | Structured outputs from each operator. |

---

# 5. **Supported Modes**

The AI interface supports four modes, all of which still require the full operator chain:

### **1. explain**
Explain operator outputs, drift, lineage, substrate, or continuity.

### **2. audit**
Verify structural correctness, drift levels, or lineage mapping.

### **3. compare**
Compare two snapshots structurally (not semantically).

### **4. locate_stable**
Identify earliest stable and most reliable versions.

---

# 6. **Operator Contract**

The AI must execute operators in this exact order:

1. **METADATA_OPERATOR**  
2. **WAYBACK_OPERATOR**  
3. **LINEAGE_OPERATOR**  
4. **COLLECTION_OPERATOR**  
5. **PRESERVATION_OPERATOR**  
6. **DRIFTBOUND_RETRIEVAL_OPERATOR**

No skipping.  
No reordering.  
No merging.  
No collapsing.  
No shortcuts.

---

# 7. **Behavioral Rules (RTT/1 Agent Contract)**

The AI must:

### **Structural Rules**
- Use **all six operators** for every request.  
- Treat drift as **explicit**, never implied.  
- Treat missing snapshots as **uncertainty**, not “no change.”  
- Prefer **lineage continuity** over recency.  
- Prefer **stable substrates** (PDF > HTML > OCR).  
- Use collection context to shape expectations, not conclusions.  

### **Safety Rules**
- No content‑based reasoning.  
- No semantic inference.  
- No speculation.  
- No hallucinated snapshots.  
- No assumptions about missing years.  
- No collapsing mixed substrates.  
- No overriding operator outputs.  

### **Output Rules**
- All answers must be **drift‑bounded**.  
- All drift > none must produce warnings.  
- All substrate instability must be explicit.  
- All regime shifts must be acknowledged.  

---

# 8. **Artifacts Returned**

The AI interface returns structured artifacts from each operator:

- metadata  
- snapshots  
- drift_map  
- continuity_breaks  
- lineage_graph  
- transformations  
- regime_shifts  
- collection_id  
- coherence_clusters  
- related_objects  
- format  
- stability_score  
- drift_risk  
- multi_layer_flags  
- final drift‑bounded summary  

These artifacts allow downstream systems (or students) to inspect the full reasoning chain.

---

# 9. **Interface Summary**

The AI interface is:

- deterministic  
- operator‑first  
- drift‑bounded  
- lineage‑aware  
- substrate‑aware  
- collection‑contextual  
- non‑speculative  
- RTT/1‑aligned  

It defines the **complete behavioral contract** for any AI agent interacting with the Internet Archive through the TriadicFrameworks canon.
