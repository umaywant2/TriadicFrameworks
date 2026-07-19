# 📘 **Teacher’s Answer Key — Trace the Lineage of a Webpage Using RTTcode**  
### *Instructor Guide for archive_org Worksheet*

This key provides:

- model answers  
- acceptable variations  
- what to look for  
- common student errors  
- how to evaluate drift‑bounded reasoning  

Use this to grade or guide student work.

---

# 🧩 **1. Choosing a Webpage**

**Expected:**  
Any valid URL that appears in the Internet Archive.

**Examples:**

- [https://www.whitehouse.gov](https://www.whitehouse.gov)  
- `https://en.wikipedia.org/wiki/Climate_change` [(en.wikipedia.org in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FClimate_change")  
- [https://www.nasa.gov](https://www.nasa.gov)  
- [https://www.mozilla.org](https://www.mozilla.org)  

**Common mistakes:**

- choosing a URL that has never been archived  
- choosing a login‑gated or private page  

---

# 🧱 **2. METADATA_OPERATOR — Expected Answers**

Students should identify:

- **substrate_type:** usually `"html"` or `"collection"`  
- **regime:** `"institutional"`, `"scholarly"`, `"commercial"`, `"media"`, etc.  
- **drift_sensitivity:**  
  - `"low"` for government or static pages  
  - `"medium"` for blogs or software sites  
  - `"high"` for news or commerce  
- **coherence:** `"high"` for structured sites, `"low"` for chaotic ones  
- **lineage_ids:** may be empty or contain a root identifier  

**Teacher notes:**  
Students should show awareness that metadata is *structural*, not content‑based.

---

# 🕰 **3. WAYBACK_OPERATOR — Expected Answers**

Students should collect **3+ snapshots** and compare them.

**Model drift patterns:**

- **None:** layout identical, minor text changes  
- **Minor:** small structural shifts  
- **Moderate:** layout redesign, navigation changes  
- **High:** complete rebuild, domain change, CMS migration  

**Continuity breaks:**  
- missing snapshots  
- redirects  
- 404 periods  
- domain ownership changes  

**Teacher notes:**  
Students should not confuse *content changes* with *structural drift*.  
RTT focuses on **structure**, not semantics.

---

# 🧬 **4. LINEAGE_OPERATOR — Expected Answers**

Students should produce a simple lineage graph.

**Model lineage:**

```
v2015 → v2018 → v2022
(minor layout change)   (major redesign)
```

**Expected observations:**

- what changed structurally  
- what remained stable  
- whether the page’s purpose shifted  

**Regime shifts examples:**

- informational → promotional  
- static HTML → CMS  
- government → archived / decommissioned  

**Teacher notes:**  
Look for **continuity reasoning**, not artistic diagrams.

---

# 📦 **5. COLLECTION_OPERATOR — Expected Answers**

Students should identify:

- whether the page belongs to a collection  
- what coherence clusters exist  
- what related objects appear  

**Examples:**

- Wikipedia pages → “web_wikipedia_org”  
- NASA pages → “nasaweb”  
- Government pages → “govdocs”  

**Teacher notes:**  
Students should understand that collections provide **context**, not correctness.

---

# 🧱 **6. PRESERVATION_OPERATOR — Expected Answers**

Students should identify substrate formats:

- HTML (drift‑prone)  
- PDF (stable)  
- OCR text (lossy)  
- images (stable but incomplete)  

**Expected stability scores:**

- HTML: 0.5–0.8  
- PDF: 0.9–1.0  
- OCR: 0.3–0.6  

**Expected drift risk:**

- HTML → medium/high  
- PDF → low  
- OCR → high  

**Teacher notes:**  
Students should connect **format** to **drift risk**.

---

# 🧠 **7. DRIFTBOUND_RETRIEVAL_OPERATOR — Expected Summary**

A correct summary includes:

### **A) Earliest stable version**  
- usually the earliest PDF or earliest HTML with consistent structure  

### **B) Most reliable version**  
- usually the most recent stable snapshot  

### **C) Key changes**  
Examples:

- navigation redesign  
- CMS migration  
- branding update  
- content expansion  
- domain redirect  

### **D) Warnings**  
Students must include warnings if:

- drift was moderate or high  
- substrate was unstable  
- continuity breaks occurred  

**Teacher notes:**  
The summary must be **drift‑bounded** — no hallucinated content, no claims beyond structural analysis.

---

# 🎓 **8. Reflection Questions — Model Responses**

### **1. What surprised you?**

Model answers:

- “How often the page changed.”  
- “How unstable HTML snapshots were.”  
- “How many versions were missing.”  
- “How consistent government pages are.”  

### **2. Did substrate affect reliability?**

Model answers:

- “PDF versions were far more stable.”  
- “OCR text lost structure.”  
- “HTML snapshots drifted across years.”  

### **3. How did RTT operators help?**

Model answers:

- “They forced me to separate structure from content.”  
- “They made drift visible.”  
- “They prevented me from trusting unstable snapshots.”  
- “They helped me build a continuity map.”  

---

# 🧩 **Teacher Evaluation Rubric**

| Category | Excellent | Satisfactory | Needs Work |
|---------|-----------|--------------|------------|
| Metadata | Correct regime + substrate + drift | Mostly correct | Missing or incorrect |
| Snapshots | 3+ snapshots, drift measured | 2–3 snapshots | Missing drift analysis |
| Lineage | Clear continuity map | Partial | No lineage reasoning |
| Collection | Correct ID + clusters | Partial | Missing |
| Substrate | Correct stability + risk | Partial | Incorrect |
| Summary | Drift‑bounded, structured | Mostly correct | Unbounded or speculative |
| Reflection | Insightful | Basic | Superficial |
