# 🧪 **RTT Operator Lab — Instructor Edition**  
### *With Grading Notes, Expected Outputs, and Instructor‑Mode Guidance*  
### TriadicFrameworks — archive_org Module (RTT/1)

This instructor version includes:

- model answers  
- drift‑bounded reasoning checks  
- common student errors  
- evaluation criteria  
- instructor prompts  
- safety notes (no content‑based inference)  

Students use the **student lab** (H16).  
Instructors use this version to guide, grade, and correct.

---

# ============================================================
# 📘 **LAB OVERVIEW (Instructor Notes)**
# ============================================================

**Learning objectives:**

- Students must demonstrate correct operator order  
- Students must reason structurally, not semantically  
- Students must identify drift, continuity, substrate stability  
- Students must produce a drift‑bounded final summary  
- Students must avoid speculation  

**Instructor watch‑outs:**

- Students often confuse *content changes* with *structural drift*  
- Students often skip PRESERVATION_OPERATOR  
- Students sometimes treat missing snapshots as “no change”  
- Students sometimes produce unbounded summaries  

---

# ============================================================
# 🧩 **SAMPLE TARGET URL (Provided to Students)**  
# ============================================================

`https://www.example.gov/public-records`

This is a **controlled synthetic URL** with **sample data** provided in the lab.

---

# ============================================================
# 🧱 **STEP 1 — METADATA_OPERATOR**  
# ============================================================

### **Student Task:**  
Extract substrate, regime, drift sensitivity, coherence, lineage IDs.

### **Sample Data Provided to Students:**
- substrate: `html`  
- regime: `institutional`  
- drift_sensitivity: `low`  
- coherence: `high`  
- lineage_ids: `["govdocs-root"]`  

### **Instructor Expected Output:**
- Correct transcription of metadata  
- Recognition that metadata suggests *low drift*  
- Awareness that metadata is *not authoritative* — it’s a structural hint  

### **Common Errors:**
- Treating metadata as “truth”  
- Ignoring drift_sensitivity  
- Assuming content stability  

### **Instructor Prompt:**  
“What does the metadata *predict* about stability — and how might later operators confirm or contradict it?”

---

# ============================================================
# 🕰 **STEP 2 — WAYBACK_OPERATOR**  
# ============================================================

### **Student Task:**  
Analyze snapshots and produce drift_map + continuity_breaks.

### **Sample Snapshots Provided:**

| Year | Notes |
|------|-------|
| 2014 | Static HTML |
| 2017 | Minor CSS changes |
| 2020 | CMS migration |
| 2023 | Same CMS, PDFs added |

### **Instructor Expected Drift Map:**

- 2014→2017: **minor drift**  
- 2017→2020: **high drift** (CMS migration)  
- 2020→2023: **minor drift**  

### **Continuity Breaks:**  
None (all snapshots present).

### **Instructor Expected Insight:**  
Students should notice that **metadata predicted low drift**, but **2020 contradicts this**.

### **Common Errors:**
- Calling CMS migration “minor drift”  
- Confusing content changes with structural drift  
- Missing the 2020 regime shift  

### **Instructor Prompt:**  
“What changed structurally, not semantically?”

---

# ============================================================
# 🧬 **STEP 3 — LINEAGE_OPERATOR**  
# ============================================================

### **Student Task:**  
Build lineage graph + identify regime shifts.

### **Instructor Expected Lineage Graph:**

```
2014 ──→ 2017 ──→ 2020* ──→ 2023
                     ↑
             (regime shift)
```

### **Instructor Expected Notes:**
- 2020 is a **regime shift** (static HTML → CMS)  
- 2023 is a continuation of the CMS regime  

### **Common Errors:**
- Treating 2020 as a new object  
- Missing the structural significance of CMS migration  
- Over‑focusing on content  

### **Instructor Prompt:**  
“What structural elements persisted across the shift?”

---

# ============================================================
# 📦 **STEP 4 — COLLECTION_OPERATOR**  
# ============================================================

### **Student Task:**  
Identify collection context.

### **Sample Data Provided:**
- collection_id: `govdocs`  
- coherence_clusters: `["public-records", "agency-index"]`  
- related_objects: `["govdocs/records-archive"]`  

### **Instructor Expected Insight:**
- Government collections tend to be **stable**  
- But stability is not guaranteed — drift still occurs  

### **Common Errors:**
- Assuming government pages never drift  
- Treating collection membership as “proof” of stability  

### **Instructor Prompt:**  
“How does collection context *inform* your expectations without overriding evidence?”

---

# ============================================================
# 🧱 **STEP 5 — PRESERVATION_OPERATOR**  
# ============================================================

### **Student Task:**  
Evaluate substrate stability.

### **Sample Data Provided:**
- 2014: HTML  
- 2017: HTML  
- 2020: HTML (CMS)  
- 2023: HTML + PDF attachments  

### **Instructor Expected Output:**
- HTML: medium drift risk  
- CMS HTML: medium/high drift risk  
- PDF: high stability  

### **Instructor Expected Insight:**
- The **PDF attachments (2023)** are likely the most stable layer  
- HTML snapshots are drift‑prone  

### **Common Errors:**
- Treating CMS HTML as “more stable”  
- Ignoring PDF stability  

### **Instructor Prompt:**  
“Which substrate would you trust for long‑term continuity?”

---

# ============================================================
# 🟣 **STEP 6 — DRIFTBOUND_RETRIEVAL_OPERATOR**  
# ============================================================

### **Student Task:**  
Produce a drift‑bounded final summary.

### **Instructor Expected Summary (Model):**

> **Earliest stable version:** 2014 (static HTML)  
> **Most reliable version:** 2023 PDF attachments  
> **Key changes:** minor drift (2014→2017), major CMS migration (2020), minor drift (2020→2023)  
> **Warnings:** metadata predicted low drift, but 2020 shows high drift; HTML snapshots are drift‑prone  

### **Instructor Expected Qualities:**
- No speculation  
- Drift explicitly acknowledged  
- Substrate stability incorporated  
- Continuity preserved  

### **Common Errors:**
- Claiming content changes as structural  
- Ignoring the CMS migration  
- Failing to include drift warnings  
- Treating metadata as authoritative  

### **Instructor Prompt:**  
“Does your summary reflect *all* operator outputs, not just snapshots?”

---

# ============================================================
# 📝 **GRADING RUBRIC (Instructor Edition)**  
# ============================================================

| Category | Excellent (4) | Satisfactory (3) | Developing (2) | Needs Work (1) |
|---------|----------------|------------------|----------------|----------------|
| Metadata | Fully correct, insightful | Mostly correct | Partial | Incorrect |
| Drift Analysis | Accurate drift_map + breaks | Mostly correct | Partial | Missing |
| Lineage | Clear graph + regime shift | Basic graph | Partial | Missing |
| Collection | Correct + contextualized | Basic | Partial | Missing |
| Substrate | Correct stability + risk | Mostly correct | Partial | Incorrect |
| Final Summary | Fully drift‑bounded | Mostly correct | Partial | Unbounded |
| Reasoning | Continuity‑aligned | Mostly aligned | Some speculation | Speculative |

**Total: 28 points**

---

# ============================================================
# 🏁 **End of Instructor Lab**
# ============================================================
