# 📘 **RTT Operator Mastery Exam (25 Questions)**  
### *TriadicFrameworks — archive_org Module (RTT/1)*  
### *Mastery Level Assessment*

**Instructions:**  
Answer all questions.  
Stay structural, not semantic.  
No speculation.  
Use RTT operators and drift‑bounded reasoning.

---

# ============================================================
# **SECTION A — Multiple Choice (10 questions)**
# ============================================================

### **1. Which operator determines the object’s substrate type?**  
A. WAYBACK_OPERATOR  
B. METADATA_OPERATOR  
C. PRESERVATION_OPERATOR  
D. COLLECTION_OPERATOR  

---

### **2. A webpage shows a CMS migration. Which operator detects this?**  
A. LINEAGE_OPERATOR  
B. DRIFTBOUND_RETRIEVAL_OPERATOR  
C. METADATA_OPERATOR  
D. COLLECTION_OPERATOR  

---

### **3. Which operator identifies continuity breaks?**  
A. WAYBACK_OPERATOR  
B. PRESERVATION_OPERATOR  
C. COLLECTION_OPERATOR  
D. METADATA_OPERATOR  

---

### **4. Which operator evaluates drift risk?**  
A. LINEAGE_OPERATOR  
B. PRESERVATION_OPERATOR  
C. WAYBACK_OPERATOR  
D. DRIFTBOUND_RETRIEVAL_OPERATOR  

---

### **5. Which format is typically most stable?**  
A. HTML  
B. OCR text  
C. PDF  
D. Mixed images  

---

### **6. Which operator produces the final answer?**  
A. COLLECTION_OPERATOR  
B. DRIFTBOUND_RETRIEVAL_OPERATOR  
C. METADATA_OPERATOR  
D. WAYBACK_OPERATOR  

---

### **7. Which operator builds the dimensional envelope?**  
A. PRESERVATION_OPERATOR  
B. COLLECTION_OPERATOR  
C. LINEAGE_OPERATOR  
D. WAYBACK_OPERATOR  

---

### **8. Which operator constructs the continuity kernel?**  
A. LINEAGE_OPERATOR  
B. METADATA_OPERATOR  
C. PRESERVATION_OPERATOR  
D. DRIFTBOUND_RETRIEVAL_OPERATOR  

---

### **9. Which operator is most sensitive to missing snapshots?**  
A. COLLECTION_OPERATOR  
B. WAYBACK_OPERATOR  
C. PRESERVATION_OPERATOR  
D. DRIFTBOUND_RETRIEVAL_OPERATOR  

---

### **10. Drift warnings must appear in the final summary when:**  
A. The student thinks drift is possible  
B. Snapshots look different  
C. Any upstream operator detected moderate/high drift  
D. The URL belongs to a collection  

---

# ============================================================
# **SECTION B — Short Answer (10 questions)**
# ============================================================

### **11. Explain why HTML snapshots drift more than PDF snapshots.**  
____________________________________________________________  
____________________________________________________________  

---

### **12. What is the purpose of the drift_map?**  
____________________________________________________________  
____________________________________________________________  

---

### **13. Describe one scenario where COLLECTION_OPERATOR changes your interpretation of a webpage.**  
____________________________________________________________  
____________________________________________________________  

---

### **14. What does the continuity kernel represent?**  
____________________________________________________________  
____________________________________________________________  

---

### **15. Why must DRIFTBOUND_RETRIEVAL_OPERATOR never reason directly from a single snapshot?**  
____________________________________________________________  
____________________________________________________________  

---

### **16. Name two outputs of PRESERVATION_OPERATOR and explain why they matter.**  
____________________________________________________________  
____________________________________________________________  

---

### **17. What does a regime shift indicate in LINEAGE_OPERATOR?**  
____________________________________________________________  
____________________________________________________________  

---

### **18. Why is drift sensitivity important in METADATA_OPERATOR?**  
____________________________________________________________  
____________________________________________________________  

---

### **19. Give an example of a high‑drift webpage type and explain why.**  
____________________________________________________________  
____________________________________________________________  

---

### **20. What must every drift‑bounded summary include?**  
____________________________________________________________  
____________________________________________________________  

---

# ============================================================
# **SECTION C — Applied Analysis (5 questions)**
# ============================================================

### **21. You have three snapshots: 2015, 2018, 2022.  
2015→2018: minor drift  
2018→2022: high drift  
What does this imply about the lineage?**  
____________________________________________________________  
____________________________________________________________  

---

### **22. A webpage belongs to a “news” collection.  
What expectations should you have about drift and stability?**  
____________________________________________________________  
____________________________________________________________  

---

### **23. A page has HTML snapshots and one PDF snapshot.  
Which is likely the most reliable and why?**  
____________________________________________________________  
____________________________________________________________  

---

### **24. A continuity break occurs between 2017 and 2019.  
What must the final summary include?**  
____________________________________________________________  
____________________________________________________________  

---

### **25. Write the six operators in canonical order.**  
1. _________________________________________________________  
2. _________________________________________________________  
3. _________________________________________________________  
4. _________________________________________________________  
5. _________________________________________________________  
6. _________________________________________________________  

---

# ============================================================
# 🧠 **ANSWER KEY (Teacher Use Only)**
# ============================================================

# **SECTION A — Multiple Choice**

1. **B — METADATA_OPERATOR**  
2. **A — LINEAGE_OPERATOR**  
3. **A — WAYBACK_OPERATOR**  
4. **B — PRESERVATION_OPERATOR**  
5. **C — PDF**  
6. **B — DRIFTBOUND_RETRIEVAL_OPERATOR**  
7. **B — COLLECTION_OPERATOR**  
8. **A — LINEAGE_OPERATOR**  
9. **B — WAYBACK_OPERATOR**  
10. **C — Upstream drift detected**  

---

# **SECTION B — Short Answer (Model Responses)**

11. HTML is dynamic and structurally unstable; PDF is static and preserves layout.  
12. It measures structural change between snapshots and identifies drift.  
13. Example: A page in a government collection is expected to be stable and institutional.  
14. The continuity kernel is the stable structural core across versions.  
15. Because snapshots drift; only lineage reveals stable structure.  
16. Format (stability), drift risk (trustworthiness), stability score (confidence).  
17. A major structural or purpose change in the webpage.  
18. It predicts how likely the object is to drift over time.  
19. News sites — frequent updates, layout changes, CMS migrations.  
20. Earliest stable version, most reliable version, key changes, warnings.

---

# **SECTION C — Applied Analysis (Model Responses)**

21. The 2022 version likely represents a regime shift; lineage splits or transforms.  
22. Expect moderate/high drift and lower stability.  
23. The PDF — static, stable, and less drift‑prone.  
24. A warning about the continuity break and reduced reliability.  
25.  
1. METADATA_OPERATOR  
2. WAYBACK_OPERATOR  
3. LINEAGE_OPERATOR  
4. COLLECTION_OPERATOR  
5. PRESERVATION_OPERATOR  
6. DRIFTBOUND_RETRIEVAL_OPERATOR  

---

# ============================================================
# 📝 **Mastery Rubric (Print‑Friendly)**
# ============================================================

| Level | Description |
|-------|-------------|
| **Mastery (24–25)** | Fully RTT‑aligned, precise drift reasoning, flawless operator order, continuity‑aware, substrate‑literate. |
| **Proficient (20–23)** | Strong understanding, minor gaps, mostly correct drift + lineage reasoning. |
| **Developing (15–19)** | Partial operator understanding, inconsistent drift reasoning, some speculation. |
| **Beginning (0–14)** | Operator order incorrect, drift misunderstood, continuity missing, substrate misinterpreted. |
