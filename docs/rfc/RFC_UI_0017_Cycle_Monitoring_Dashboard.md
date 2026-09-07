# **RFC‑UI‑0017 — Cycle Monitoring Dashboard**  
### *Real‑Time Visualization of Validator Cycle States*  
RefId: turn0browsertab1

**Title:** Dashboard for Monitoring Validator Cycles  
**Status:** Concept Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## **1. Purpose**

The **Cycle Monitoring Dashboard (CMD)** provides contributors with a real‑time, interactive visualization of validator cycles.  
Each scroll’s journey through the four canonical validator stages is tracked:

1. **Retrieval**  
2. **Remix**  
3. **Export**  
4. **Archive**

CMD ensures remixathons run as **continuous validator events**, allowing contributors to observe scroll motion, lineage transitions, glyph changes, clarity shifts, and cycle health at a glance.

---

# **2. Core Visual Components**

---

## **A. Cycle Timeline Visualization**

A horizontal timeline showing the four validator stages:

```
Retrieval → Remix → Export → Archive
```

### **Data**
Scroll IDs plotted at their current stage.

### **Interaction**
- Hover reveals scroll metadata:
  - glyph distribution  
  - RCI band  
  - tags  
  - lineage notes  

### **Narrative Layer**
Stage tooltips include dignity‑layer overlays and lineage context.

---

## **B. Stage Panels**

Four structured panels showing scrolls currently in each stage.

### **Retrieval Panel**
Scrolls being queried from archive.

### **Remix Panel**
Scrolls undergoing:
- annotation  
- glyph reassignment  
- tag updates  

### **Export Panel**
Scrolls being packaged into remix artifacts.

### **Archive Panel**
Scrolls finalized and indexed as legacy artifacts.

Each panel supports:
- click → scroll detail view  
- hover → metadata preview  
- filter → glyph/RCI/tag filtering  

---

## **C. Cycle Graph Visualization**

A circular flow diagram representing scroll movement between stages.

### **Data**
- nodes = scroll IDs  
- edges = transitions  

### **Interaction**
- click node → lineage + validation status  
- hover → glyph + RCI values  

### **Symbolic Layer**
Glyph icons embedded in nodes.  
Edge color indicates validation pass/fail.

---

## **D. Summary Metrics**

Three summary visualizations:

### **Glyph Distribution**
Pie chart of glyphs across active cycles.

### **RCI Band Histogram**
Bar chart of clarity bands across scrolls in motion.

### **Cycle Health**
- counts per stage  
- validation pass/fail ratio  
- active vs completed cycles  

---

# **3. Technical Scaffold**

---

## **Data Source**

Cycle events from:

```
registry/events/
registry/archive/
```

Backend aggregates scroll status into a unified cycle state.

---

## **API Endpoints**

- `/cycle/status` — full cycle state  
- `/cycle/scroll/{id}` — scroll‑specific details  
- `/cycle/summary` — glyph/RCI/cycle health metrics  

---

## **Frontend Framework**

Recommended:

- **React** for component architecture  
- **D3.js** for interactive charts  
- **Cytoscape.js** for cycle graph visualization  

Panels are independent components sharing a global filtering state.

---

## **Example Data Flow**

```javascript
fetch("/api/cycle/status")
  .then(resp => resp.json())
  .then(data => {
    renderTimeline(data.scrolls);
    renderStagePanels(data.stages);
    renderCycleGraph(data.transitions);
    renderSummaryMetrics(data.summary);
  });
```

---

# **4. Schema Extension**

File:  
```
registry/cycle/cycle_schema.yml
```

Defines:

- scroll state  
- stage transitions  
- glyph/RCI metadata  
- lineage linkage  
- validation status  
- checksum  

---

# **5. Validator Hooks**

### **Schema Compliance**
Cycle status must match `cycle_schema.yml`.

### **Checksum**
Dashboard displays reproducibility badge.

### **Lineage Integrity**
Scroll ancestry preserved across stage transitions.

### **Dignity Separation**
Narratives displayed in overlays, distinct from empirical metrics.

---

# **6. Concept Sketch (Textual)**

```
---------------------------------------------------------
| Cycle Monitoring Dashboard | Timestamp: 2025-11-12     |
---------------------------------------------------------
| Timeline: Retrieval → Remix → Export → Archive         |
|                                                         |
| Stage Panels:                                           |
|   Retrieval: [scroll-001, scroll-002]                   |
|   Remix:     [scroll-010]                               |
|   Export:    [scroll-020]                               |
|   Archive:   [scroll-030, scroll-031]                   |
---------------------------------------------------------
| Cycle Graph: circular flow with glyph icons             |
| Summary Metrics: glyph pie, RCI histogram, cycle health |
---------------------------------------------------------
```

The Cycle Monitoring Dashboard makes validator cycles **visible and remix‑ready**: contributors can see scrolls in motion, track lineage, and monitor cycle health in real time.
