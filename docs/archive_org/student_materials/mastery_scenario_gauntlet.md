# **RTT Mastery Scenario Gauntlet — Internet Archive**  
### *student_materials/mastery_scenario_gauntlet.md*

---

# **Overview**

This gauntlet tests your ability to:

- analyze snapshot timelines  
- detect drift  
- identify continuity kernels  
- evaluate substrate stability  
- interpret lineage graphs  
- choose the most reliable snapshot  

You will complete **five scenarios**, each requiring full use of the RTT operator chain.

All scenarios are **synthetic** and do not correspond to real Internet Archive pages.

---

# **Scenario 1 — Government Records Portal**

**Target URL:**  
`https://archive.org/details/gov-records-portal`

**Snapshot Timeline:**  
2012, 2013, 2016, 2019, 2023

**Observed Structure:**  
- 2012 → 2013: identical  
- 2013 → 2016: template update  
- 2016 → 2019: navigation restructure  
- 2019 → 2023: minor CSS shift  

**Substrate:** HTML  
**Collection:** govdocs  

### **Tasks**

1. Identify drift levels for each transition.  
2. Identify the continuity kernel.  
3. Determine whether any continuity breaks exist.  
4. Evaluate substrate stability.  
5. Choose the most reliable snapshot and justify your answer.

---

# **Scenario 2 — Vintage Software Index**

**Target URL:**  
`https://archive.org/details/vsoft-index`

**Snapshot Timeline:**  
2011, 2014, 2018, 2022

**Observed Structure:**  
- 2011 → 2014: no change  
- 2014 → 2018: minor layout update  
- 2018 → 2022: no change  

**Substrate:** HTML  
**Collection:** vintagesoftware  

### **Tasks**

1. Identify drift levels.  
2. Identify the continuity kernel.  
3. Evaluate stability and drift risk.  
4. Explain why vintage software collections tend to be stable.  
5. Choose the most reliable snapshot.

---

# **Scenario 3 — Academic Journal Archive**

**Target URL:**  
`https://archive.org/details/journal-hub`

**Snapshot Timeline:**  
2012, 2015, 2018, 2021, 2024

**Observed Structure:**  
- 2012 → 2015: template refresh  
- 2015 → 2018: navigation restructure  
- 2018 → 2021: CMS migration  
- 2021 → 2024: minor CSS update  

**Substrate:** Mixed (HTML + PDF)  
**Collection:** journals  

### **Tasks**

1. Identify drift levels for each transition.  
2. Identify the regime shift.  
3. Identify the continuity kernel.  
4. Explain how mixed substrates affect stability.  
5. Choose the most reliable snapshot and justify your answer.

---

# **Scenario 4 — Local News Archive**

**Target URL:**  
`https://archive.org/details/localnews-chronicle`

**Snapshot Timeline:**  
2010, 2011, 2013, 2016, 2017, 2020, 2024

**Observed Structure:**  
- 2010 → 2011: minor CSS change  
- 2011 → 2013: moderate layout shift  
- 2013 → 2016: full redesign  
- 2016 → 2017: no change  
- 2017 → 2020: CMS migration  
- 2020 → 2024: minor CSS update  

**Substrate:** HTML  
**Collection:** news  

### **Tasks**

1. Identify drift levels for each transition.  
2. Identify continuity breaks.  
3. Identify the continuity kernel (if any).  
4. Explain why news sites tend to have high drift.  
5. Choose the most reliable snapshot and justify your answer.

---

# **Scenario 5 — Museum Exhibit Archive**

**Target URL:**  
`https://archive.org/details/museum-exhibit-collection`

**Snapshot Timeline:**  
2013, 2014, 2016, 2019, 2023

**Observed Structure:**  
- 2013 → 2014: no change  
- 2014 → 2016: minor layout update  
- 2016 → 2019: mixed substrate introduced (HTML + image)  
- 2019 → 2023: navigation restructure  

**Substrate:** Mixed  
**Collection:** cultural  

### **Tasks**

1. Identify drift levels.  
2. Identify the continuity kernel.  
3. Explain how mixed substrates affect drift risk.  
4. Identify any regime shifts.  
5. Choose the most reliable snapshot and justify your answer.

---

# **Mastery Criteria**

To demonstrate mastery, your answers must:

- correctly identify drift levels  
- correctly identify continuity kernels  
- correctly detect regime shifts  
- correctly evaluate substrate stability  
- correctly identify continuity breaks  
- justify snapshot selection using RTT logic  
- avoid content‑based reasoning  

---

# **Teacher Rubric**

| Skill | Description | Points |
|-------|-------------|--------|
| Drift Analysis | Correct drift classification across scenarios | 10 |
| Continuity Kernel | Accurate identification of stable elements | 10 |
| Substrate Reasoning | Correct evaluation of stability and drift risk | 10 |
| Regime Shifts | Correct identification and explanation | 5 |
| Continuity Breaks | Correct detection and interpretation | 5 |
| Final Snapshot Choice | RTT‑aligned justification | 10 |
| **Total** |  | **50 points** |

**Mastery:** 45–50  
**Proficiency:** 38–44  
**Developing:** 30–37  
**Needs Support:** ≤29  
