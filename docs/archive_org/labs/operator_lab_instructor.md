# **RTT Operator Lab — Instructor Version**  
### *archive_org module — labs/operator_lab_instructor.md*

---

# **Purpose of This Instructor Guide**

This guide provides:

- expected student outputs  
- structural reasoning notes  
- common misconceptions  
- grading guidance  
- operator‑chain alignment  

It corresponds directly to the **student RTT Operator Lab** in:

```
/docs/archive_org/labs/operator_lab.md
```

All reasoning is **structural**, not content‑based.

---

# **Scenario Used in the Lab**

**Target URL:**  
`https://archive.org/details/sample-training-page`

**Snapshots:**  
2013, 2016, 2019, 2023

**Structural Changes:**  
- 2013 → 2016: minor template update  
- 2016 → 2019: navigation restructure  
- 2019 → 2023: minor CSS shift  

**Substrate:** HTML  
**Collection:** govdocs  

This scenario is fully synthetic and designed to isolate structural reasoning.

---

# **Operator‑by‑Operator Instructor Notes**

---

## **1. METADATA_OPERATOR**

### **Expected Student Output**
- Substrate: HTML  
- Regime: institutional  
- Drift sensitivity: low  
- Coherence: high  
- Lineage IDs: synthetic (e.g., “govdocs-root”)  

### **Instructor Notes**
Students should identify **structural metadata**, not content.  
Common error: describing the *topic* of the page instead of its *structure*.

---

## **2. WAYBACK_OPERATOR**

### **Expected Student Output**
- Snapshots: 2013, 2016, 2019, 2023  
- Drift map:  
  - 2013→2016: minor  
  - 2016→2019: moderate  
  - 2019→2023: minor  
- Continuity breaks: none  
- Time crystal: any value between 0.6–0.9 is acceptable  

### **Instructor Notes**
Students often confuse **visual differences** with **structural drift**.  
Remind them: drift is about **layout, navigation, template**, not content.

---

## **3. LINEAGE_OPERATOR**

### **Expected Student Output**
- Lineage graph:  
  - template update  
  - navigation restructure  
  - CSS shift  
- Transformations: list of the above  
- Regime shifts: none  
- Continuity kernel:  
  - header  
  - footer  
  - records index  

### **Instructor Notes**
The continuity kernel must be **structural** and **persistent**.  
Students sometimes list content blocks — redirect them to layout elements.

---

## **4. COLLECTION_OPERATOR**

### **Expected Student Output**
- Collection ID: govdocs  
- Coherence clusters:  
  - public‑records  
  - agency‑index  
- Related objects: synthetic examples  
- Regime profile: institutional  

### **Instructor Notes**
Students should not infer meaning from the collection name.  
They should focus on **structural similarity**.

---

## **5. PRESERVATION_OPERATOR**

### **Expected Student Output**
- Format: HTML  
- Stability score: ~0.8  
- Drift risk: low  
- Multi‑layer flags: ["html"]  

### **Instructor Notes**
Students must justify stability based on **substrate**, not content.  
HTML is stable but drift‑prone; PDF would be more stable.

---

## **6. DRIFTBOUND_RETRIEVAL_OPERATOR**

### **Expected Student Output**
- Earliest stable version: 2013  
- Most reliable version: 2023  
- Key changes:  
  - template update  
  - navigation restructure  
  - CSS shift  
- Warnings: none  
- Final answer: 2023 is most reliable due to stability + continuity  

### **Instructor Notes**
Students must combine:

- drift  
- continuity  
- substrate stability  
- absence of breaks  

The newest snapshot is correct **only because** it is structurally stable.

---

# **Grading Guidance**

| Skill | Points | Criteria |
|-------|--------|----------|
| Drift Classification | 10 | Correct minor/moderate distinctions |
| Continuity Kernel | 10 | Identifies persistent structural elements |
| Substrate Reasoning | 10 | Correct stability logic |
| Regime Shifts | 5 | Correctly identifies none |
| Continuity Breaks | 5 | Correctly identifies none |
| Final Snapshot Choice | 10 | RTT‑aligned justification |
| **Total** | **50** | |

**Mastery:** 45–50  
**Proficiency:** 38–44  
**Developing:** 30–37  
**Needs Support:** ≤29  

---

# **Common Student Misconceptions**

- Confusing **content changes** with **structural drift**  
- Treating **visual differences** as drift  
- Misidentifying **substrate stability**  
- Assuming the newest snapshot is always best  
- Listing content blocks as continuity kernel elements  

---

# **Instructor Tips**

- Emphasize structure over content  
- Encourage sketching snapshot layouts  
- Reinforce drift as **structural**, not semantic  
- Use continuity kernel as anchor for reasoning  
