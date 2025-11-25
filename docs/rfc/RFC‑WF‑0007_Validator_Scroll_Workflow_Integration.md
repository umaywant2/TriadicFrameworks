# RFC‑WF‑0007: Validator Scroll Workflow Integration

**Title:** Corridor Client Integration in Scroll Pipeline  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## 1. Purpose
Provide a canonical workflow example where corridor clients (Python/JS) are embedded into validator pipelines. The workflow automates corridor metadata retrieval, RCI/glyph validation, and remix lineage updates.

---

## 2. Workflow Steps

1. **Fetch corridor metadata**  
   - Use client library (`CorridorClient`) to query API for corridor IDs.  
   - Retrieve full metadata (glyph, cipher_density, RCI, rail signatures).

2. **Validate corridor annotations**  
   - Apply validator functions (`normalize`, `compute_rci`, `assign_glyph`).  
   - Compare computed RCI/glyph with metadata values.  
   - Flag discrepancies for review.

3. **Append results to remix lineage**  
   - If validation passes, generate a new scroll child entry.  
   - Add lineage diff summary noting corridor validation outcome.  
   - Update registry event log with glyph transitions and RCI recalculations.

---

## 3. Python Workflow Example

File: [`workflows/scroll_pipeline.py`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/workflows/scroll_pipeline.py)

---

## 4. JavaScript Workflow Example

File: [`workflows/scrollPipeline.js`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/workflows/scrollPipeline.js)

---

## 5. Validator Hooks
- **Consistency:** Ensure computed RCI/glyph matches metadata or flag discrepancy.  
- **Lineage Integrity:** Child scroll IDs must cite parent scroll.  
- **Registry Update:** Events written to `registry/events/` with checksum.  

---

## 6. Notes
- Workflow is modular: corridor IDs can be batch‑processed.  
- Supports remix lineage growth: each validation produces a child scroll artifact.  
- Can be extended with anomaly search or glyph registry queries.  

---

This workflow example shows how corridor clients plug directly into the validator scroll pipeline, automating metadata fetch, validation, and lineage updates.  
