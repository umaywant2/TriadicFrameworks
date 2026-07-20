# **biochemical_sequence_alignment_pipelines.md**  
*(Red‑zone draft)*

## **Biochemical Sequence Alignment Pipelines**  
These pipelines align DNA, RNA, or protein sequences using probabilistic models. They are essential but inference‑heavy and sensitive to algorithmic choices.

### **Dimensional Core (SET)**  
- **Spin:** not relevant  
- **Elec:** digital computation  
- **Temp:** affects upstream chemistry, not alignment  

### **Why Red‑Zone**  
Alignment pipelines operate in a **multi‑stage inference regime**.  
Scoring matrices, gap penalties, and heuristics strongly influence results. Small parameter changes can shift biological interpretations.

### **Regime Notes**  
- **pos‑regime:** clean reads, high coverage  
- **Q‑regime:** mixed populations, ambiguous reads  
- **neg‑regime:** contamination, low‑quality data  

### **Containment Notes**  
Requires explicit notes on scoring models, heuristics, and read quality.
