# 📘 **RTT Operator Literacy — Extended Quiz (10 Questions)**  
### *Student Assessment — archive_org Module (RTT/1)*

**Instructions:**  
Answer each question using RTT operator concepts.  
Keep answers structural, not semantic.  
No speculation — stay drift‑bounded.

---

# ------------------------------------------------------------
# **SECTION A — Multiple Choice (5 questions)**
# ------------------------------------------------------------

### **1. Which operator is responsible for detecting continuity breaks?**
A. METADATA_OPERATOR  
B. WAYBACK_OPERATOR  
C. COLLECTION_OPERATOR  
D. PRESERVATION_OPERATOR  

---

### **2. A webpage switches from static HTML to a CMS. Which operator identifies this regime shift?**
A. LINEAGE_OPERATOR  
B. DRIFTBOUND_RETRIEVAL_OPERATOR  
C. METADATA_OPERATOR  
D. COLLECTION_OPERATOR  

---

### **3. Which substrate format is typically the most stable across snapshots?**
A. HTML  
B. OCR text  
C. PDF  
D. Mixed images  

---

### **4. Which operator determines the object’s “dimensional envelope”?**
A. WAYBACK_OPERATOR  
B. COLLECTION_OPERATOR  
C. PRESERVATION_OPERATOR  
D. LINEAGE_OPERATOR  

---

### **5. The final summary must include drift warnings if:**
A. The student thinks drift is possible  
B. The snapshots look different  
C. Any upstream operator detected moderate or high drift  
D. The URL belongs to a collection  

---

# ------------------------------------------------------------
# **SECTION B — Short Answer (5 questions)**
# ------------------------------------------------------------

### **6. Explain why HTML snapshots often show more drift than PDF snapshots.**
Your answer:  
____________________________________________________________  
____________________________________________________________  

---

### **7. What is the purpose of the continuity kernel in LINEAGE_OPERATOR?**
Your answer:  
____________________________________________________________  
____________________________________________________________  

---

### **8. Name two things PRESERVATION_OPERATOR evaluates and explain why they matter.**
Your answer:  
____________________________________________________________  
____________________________________________________________  

---

### **9. Describe one situation where COLLECTION_OPERATOR significantly changes how you interpret a webpage.**
Your answer:  
____________________________________________________________  
____________________________________________________________  

---

### **10. Write the six operators in the correct canonical order.**
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

**1. B — WAYBACK_OPERATOR**  
It detects continuity breaks and drift between snapshots.

**2. A — LINEAGE_OPERATOR**  
Regime shifts are part of lineage transformations.

**3. C — PDF**  
PDF is the most stable substrate in IA.

**4. B — COLLECTION_OPERATOR**  
It defines the dimensional envelope and context.

**5. C — Any upstream operator detected moderate or high drift**  
Drift warnings are mandatory when drift is non‑trivial.

---

# **SECTION B — Short Answer**

### **6. HTML vs PDF drift**
**Model answer:**  
HTML is rendered dynamically and often changes structure over time (CSS, JS, layout, CMS updates).  
PDF is static and preserves structure, so it drifts far less.

---

### **7. Purpose of the continuity kernel**
**Model answer:**  
It identifies the stable structural elements across versions and anchors the lineage graph.  
It prevents misinterpreting drift as a new object.

---

### **8. PRESERVATION_OPERATOR evaluates:**
**Two examples:**  
- **Format:** determines stability (PDF vs HTML vs OCR).  
- **Stability score:** indicates how reliable snapshots are.  
- **Drift risk:** predicts how much structure may change.  
- **Multi‑layer flags:** show whether multiple substrates exist.

**Why it matters:**  
It tells you which snapshots you can trust.

---

### **9. COLLECTION_OPERATOR interpretation shift**
**Model answer:**  
If a webpage belongs to a government collection, it is likely stable and institutional.  
If it belongs to a news collection, drift is expected.  
Collection context changes expectations about stability and purpose.

---

### **10. Canonical operator order**
1. METADATA_OPERATOR  
2. WAYBACK_OPERATOR  
3. LINEAGE_OPERATOR  
4. COLLECTION_OPERATOR  
5. PRESERVATION_OPERATOR  
6. DRIFTBOUND_RETRIEVAL_OPERATOR  
