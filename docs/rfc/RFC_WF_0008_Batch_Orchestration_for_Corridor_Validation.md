# RFC‑WF‑0008: Batch Orchestration for Corridor Validation

**Title:** Batch Corridor Orchestration and Remixathon Lineage Report  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## 1. Purpose
Enable batch processing of multiple corridor IDs, validate their RCI/glyph assignments, and generate a consolidated lineage report. This report is designed for remixathon events, where contributors can see corridor validation outcomes, glyph transitions, and remix ancestry in one artifact.

---

## 2. Workflow Steps

1. **Input corridor list**  
   - Accept corridor IDs (from API or file).  
   - Optionally include parent scroll ID for lineage anchoring.

2. **Batch validation**  
   - For each corridor: fetch metadata, compute RCI, assign glyph, compare with metadata.  
   - Record validation status and lineage event.

3. **Consolidated lineage report**  
   - Aggregate all lineage events into a single YAML/JSON report.  
   - Include summary statistics (glyph distribution, RCI band counts, validation pass/fail).  
   - Export report to `registry/reports/remixathon_<timestamp>.yml`.

---

## 3. Python Batch Script

File: [`workflows/batch_orchestrator.py`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/workflows/batch_orchestrator.py)

---

## 4. Example Usage

```bash
python workflows/batch_orchestrator.py
```

```python
corridors = ["c-001", "c-002", "c-003", "c-004"]
report = batch_process(corridors, parent_scroll="s-1000")
print(report["remixathon_report"]["summary"])
```

---

## 5. Report Structure

```yaml
remixathon_report:
  timestamp: 2025-11-12T15:31:00Z
  parent_scroll: s-1000
  events:
    - corridor_id: c-001
      previous_glyph: ◆
      new_glyph: ◆
      previous_rci: 0.420
      new_rci: 0.420
      status: validation_passed
    - corridor_id: c-002
      previous_glyph: ◇
      new_glyph: ◇
      previous_rci: 0.196
      new_rci: 0.196
      status: validation_passed
  summary:
    glyph_distribution: {◇: 1, ◆: 1}
    rci_band_counts: {low: 1, medium: 1, high: 0}
    validation_passed: 2
    validation_failed: 0
```

---

## 6. Notes
- Consolidated lineage report is remix‑ready: contributors can see glyph transitions and clarity bands at a glance.  
- Script supports incremental corridor lists; can be extended to pull corridor IDs dynamically from API.  
- Report artifacts are validator‑grade and can be archived in `registry/reports/` for remixathon events.  

---
