# **pull_request_template.md**  
*(draft — for all contributors)*

## **Summary of Changes**

Provide a short, clear description of what this PR adds or updates.

- What instrument(s) did you add or modify?  
- Which zone folder did you place them in (Green / Yellow / Red)?  
- Any supporting updates (appendix, glossary links, etc.)?

Keep this section minimal and structural.

---

## **Checklist for Contributors**

Before submitting, please confirm the following:

### **1. Template Compliance**
- [ ] I used `template.md` as the base for each new instrument file.  
- [ ] All required sections are present (Dimensional Core, Why Zone, Regime Notes, Alignment/Containment Notes).  
- [ ] The tone is minimal, friendly, and aligned with the rest of the review.

---

### **2. Correct Zone Placement**
- [ ] The instrument is placed in the correct folder:  
  - `01_green_zone/`  
  - `02_yellow_zone/`  
  - `03_red_zone/`  
- [ ] The zone justification is clear and matches the triadic glossary.

---

### **3. Dimensional Core (SET)**
- [ ] The SET section is present and accurate.  
- [ ] Only relevant axes are included (Spin, Elec, Temp).  
- [ ] No unnecessary detail or domain‑specific jargon.

---

### **4. Regime Notes**
- [ ] The file includes **pos‑regime**, **Q‑regime**, and **neg‑regime** notes.  
- [ ] Each bullet is one line and describes behavior, not theory.  
- [ ] No deep domain dives or equations.

---

### **5. Alignment or Containment Notes**
- [ ] Green‑zone: “Already aligned” with minimal edge‑case notes.  
- [ ] Yellow‑zone: clear notes on assumptions, drift, or environmental sensitivity.  
- [ ] Red‑zone: explicit containment boundaries for fragile regimes.

---

### **6. File Structure & Naming**
- [ ] The filename uses lowercase with underscores (e.g., `mass_spectrometer.md`).  
- [ ] The file is placed in the correct zone folder.  
- [ ] No spaces or special characters in filenames.

---

### **7. Appendix Updates (if needed)**
- [ ] `instrument_list_raw.md` updated if this is a new instrument type.  
- [ ] No glossary terms redefined inside instrument files.  
- [ ] Cross‑links added to `glossary_links.md` only when appropriate.

---

### **8. Style & Length**
- [ ] The file is short (150–300 words).  
- [ ] Tone is student‑friendly and aligned with the project.  
- [ ] No diagrams, equations, or domain‑heavy explanations.

---

## **Additional Notes (optional)**

Add any context, references, or reasoning that may help reviewers understand your choices. Keep it brief.
