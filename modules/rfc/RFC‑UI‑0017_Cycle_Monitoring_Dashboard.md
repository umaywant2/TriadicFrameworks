# RFC‑UI‑0017: Cycle Monitoring Dashboard

**Title:** Dashboard for Monitoring Validator Cycles  
**Status:** Concept Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## 1. Purpose
Provide contributors with a real‑time dashboard that visualizes validator cycles. Each scroll’s journey through retrieval, remix, export, and archive stages is tracked, ensuring remixathons run as continuous validator events.

---

## 2. Core Visual Components

### A. Cycle Timeline
- **Visualization:** Horizontal timeline with four stages: Retrieval → Remix → Export → Archive.  
- **Data:** Scroll IDs plotted at their current stage.  
- **Interaction:** Hover reveals scroll metadata (glyph distribution, RCI band, tags).  
- **Narrative Layer:** Stage tooltips include lineage notes and dignity overlays.

---

### B. Stage Panels
- **Retrieval Panel:** List of scrolls currently being queried from archive.  
- **Remix Panel:** Scrolls undergoing annotation, glyph reassignment, or tag updates.  
- **Export Panel:** Scrolls packaged into remix artifacts.  
- **Archive Panel:** Scrolls finalized and indexed as legacy artifacts.  

---

### C. Cycle Graph
- **Visualization:** Circular flow diagram showing scroll movement between stages.  
- **Data:** Arrows represent transitions; nodes represent scroll IDs.  
- **Interaction:** Click node to view scroll lineage and validation status.  
- **Symbolic Layer:** Glyph icons embedded in nodes; edge color indicates pass/fail validation.

---

### D. Summary Metrics
- **Glyph Distribution:** Pie chart of glyphs across active cycles.  
- **RCI Band Histogram:** Bar chart of clarity bands across scrolls in motion.  
- **Cycle Health:** Counts of scrolls per stage; validation pass/fail ratio.  

---

## 3. Technical Scaffold

### Data Source
- Input: Cycle events from `registry/events/` and `registry/archive/`.  
- Backend: Aggregates scroll status into cycle state.  
- API: Expose endpoints `/cycle/status`, `/cycle/scroll/{id}`, `/cycle/summary`.

### Frontend Framework
- Suggested: React + D3.js for interactive charts; Cytoscape.js for cycle graph.  
- Modular: Panels as independent components; shared state for filtering.

### Example Data Flow
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

## 4. Schema Extension

File: [`registry/cycle/cycle_schema.yml`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/registry/cycle/cycle_schema.yml)

---

## 5. Validator Hooks
- **Schema compliance:** Cycle status must match `cycle_schema.yml`.  
- **Checksum:** Dashboard displays checksum badge for reproducibility.  
- **Lineage integrity:** Scroll ancestry preserved across stages.  
- **Dignity separation:** Narratives displayed in overlays, distinct from metrics.

---

## 6. Concept Sketch (textual)

```
 ---------------------------------------------------------
| Cycle Monitoring Dashboard | Timestamp: 2025-11-12      |
 ---------------------------------------------------------
| Timeline: Retrieval → Remix → Export → Archive          |
| Stage Panels:                                            |
|   Retrieval: [scroll-001, scroll-002]                   |
|   Remix:     [scroll-010]                               |
|   Export:    [scroll-020]                               |
|   Archive:   [scroll-030, scroll-031]                   |
 ---------------------------------------------------------
| Cycle Graph: circular flow with glyph icons             |
| Summary Metrics: glyph pie, RCI histogram, cycle health |
 ---------------------------------------------------------
```

---

This **Cycle Monitoring Dashboard** makes validator cycles visible and remix‑ready: contributors can see scrolls in motion, track lineage, and monitor cycle health in real time.  
