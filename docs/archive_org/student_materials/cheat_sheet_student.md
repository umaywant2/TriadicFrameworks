# **RTT Cheat Sheet — Internet Archive (Student Edition)**  
### *archive_org module — student_materials/cheat_sheet_student.md*

---

## **1. What This Module Teaches**
Use the Internet Archive to understand:

- how webpages change over time  
- which versions are stable  
- how to detect redesigns and migrations  
- how to choose the most reliable snapshot  

You will use the RTT operator chain to guide your analysis.

---

## **2. The Six Operators (Student Version)**

### **1. METADATA_OPERATOR**  
Identifies the webpage’s basic structure:  
- format (HTML, PDF, image, OCR)  
- type of site (institutional, news, scholarly, etc.)  
- expected drift level  

### **2. WAYBACK_OPERATOR**  
Collects snapshots and shows:  
- timeline of captures  
- drift between years  
- missing years (continuity breaks)  

### **3. LINEAGE_OPERATOR**  
Shows how the webpage evolved:  
- template changes  
- navigation changes  
- CMS migrations  
- stable elements (continuity kernel)  

### **4. COLLECTION_OPERATOR**  
Places the webpage in context:  
- which IA collection it belongs to  
- related pages  
- structural family  

### **5. PRESERVATION_OPERATOR**  
Checks how stable the snapshots are:  
- substrate stability  
- drift risk  
- mixed layers (HTML + PDF, etc.)  

### **6. DRIFTBOUND_RETRIEVAL_OPERATOR**  
Finds the **most reliable version** by combining:  
- drift  
- continuity  
- substrate stability  
- collection context  

---

## **3. Drift Levels (Student Guide)**

- **None** — looks the same  
- **Minor** — small layout or style changes  
- **Moderate** — navigation or template changes  
- **High** — redesign, rebuild, CMS migration  

---

## **4. Substrate Types (Student Guide)**

- **PDF** — most stable  
- **Image** — stable but incomplete  
- **HTML** — drift‑prone  
- **OCR** — lossy, high drift  
- **Mixed** — requires careful evaluation  

---

## **5. Continuity Kernel**
These are the parts of a webpage that stay the same across snapshots.

Examples:  
- header  
- footer  
- main menu  
- index page  
- sidebar  

If these stay the same, the site has good continuity.

---

## **6. How to Compare Two Snapshots**
Look for structural differences:

- layout  
- navigation  
- template  
- sidebar  
- header/footer  
- presence/absence of PDF layer  

Avoid content differences — focus on structure only.

---

## **7. How to Choose the Most Reliable Version**
Pick the snapshot that has:

1. **Stable substrate** (PDF > HTML > OCR)  
2. **Low drift**  
3. **Strong continuity kernel**  
4. **Few or no missing years**  
5. **No major redesigns**  

---

## **8. Quick Student Workflow**

1. Pick a webpage  
2. List its snapshots  
3. Compare two snapshots  
4. Identify drift  
5. Find continuity kernel  
6. Check substrate stability  
7. Choose the most reliable version  

---

## **9. Common Patterns**

- Government sites → stable, low drift  
- News sites → high drift, frequent redesigns  
- Journals → mixed substrates, periodic updates  
- Vintage software → very stable, versioned  

---

## **10. One‑Sentence Summary**
**RTT helps you find the most reliable version of a webpage by analyzing structure, drift, continuity, and substrate stability — not content.**
