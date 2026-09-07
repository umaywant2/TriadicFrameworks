# **RFC‑WF‑0007 — Validator Scroll Workflow Integration**  
### *Corridor Client Integration in Scroll Pipeline*  
RefId: turn0browsertab1

**Title:** Corridor Client Integration in Scroll Pipeline  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## **1. Purpose**

This RFC defines the canonical workflow for integrating **corridor clients** (Python/JS) directly into the validator scroll pipeline.  
The workflow automates:

- corridor metadata retrieval  
- RCI/glyph validation  
- lineage diff generation  
- registry event logging  

WF‑0007 is the foundational pattern for scroll‑level validation workflows and is referenced by WF‑0008 (Batch Orchestration) and WF‑0016 (Remix Generation Workflow).

---

# **2. Workflow Steps**

The validator scroll pipeline follows a four‑stage corridor‑validation loop.

---

## **2.1 Fetch Corridor Metadata**

Use the **CorridorClient** to query the Corridor Registry API for corridor IDs.

Retrieve full metadata:

- glyph  
- cipher_density  
- RCI  
- rail signatures  
- lineage context  

Metadata is normalized into scroll‑ready structures.

---

## **2.2 Validate Corridor Annotations**

Apply validator functions:

- `normalize()`  
- `compute_rci()`  
- `assign_glyph()`  

Compare computed values with metadata:

- If **match** → corridor passes validation  
- If **mismatch** → flag discrepancy for review  

Validator emits:

- clarity notes  
- glyph transition notes  
- anomaly flags  

---

## **2.3 Append Results to Remix Lineage**

If validation passes:

- generate a **child scroll** entry  
- attach lineage diff summary  
- record corridor validation outcome  

Lineage diff includes:

- glyph transitions  
- RCI recalculations  
- rail signature notes  

WF‑0007 ensures lineage continuity and validator‑grade reproducibility.

---

## **2.4 Update Registry Event Log**

Write events to:

```
registry/events/
```

Each event includes:

- corridor ID  
- glyph transition  
- RCI shift  
- checksum  
- timestamp  

Registry events feed:

- REG‑0004 (Registry Indexer)  
- UI‑0009 (Dashboard)  
- UI‑0017 (Cycle Monitoring Dashboard)  

---

# **3. Python Workflow Example**

File:  
```
workflows/scroll_pipeline.py
```

```python
from corridor_client import CorridorClient
from validator import normalize, compute_rci, assign_glyph
from lineage import append_child_scroll
from registry import write_event

client = CorridorClient()

def run_scroll_pipeline(corridor_ids):
    for cid in corridor_ids:
        meta = client.fetch_metadata(cid)

        computed_rci = compute_rci(meta)
        computed_glyph = assign_glyph(meta)

        if computed_rci == meta["rci"] and computed_glyph == meta["glyph"]:
            child = append_child_scroll(meta["parent_scroll"], cid, computed_rci, computed_glyph)
            write_event(cid, computed_glyph, computed_rci)
        else:
            print(f"Discrepancy detected for corridor {cid}")
```

---

# **4. JavaScript Workflow Example**

File:  
```
workflows/scrollPipeline.js
```

```javascript
import { CorridorClient } from "./corridorClient.js";
import { normalize, computeRci, assignGlyph } from "./validator.js";
import { appendChildScroll } from "./lineage.js";
import { writeEvent } from "./registry.js";

const client = new CorridorClient();

export async function runScrollPipeline(corridorIds) {
  for (const cid of corridorIds) {
    const meta = await client.fetchMetadata(cid);

    const computedRci = computeRci(meta);
    const computedGlyph = assignGlyph(meta);

    if (computedRci === meta.rci && computedGlyph === meta.glyph) {
      appendChildScroll(meta.parent_scroll, cid, computedRci, computedGlyph);
      writeEvent(cid, computedGlyph, computedRci);
    } else {
      console.warn(`Discrepancy detected for corridor ${cid}`);
    }
  }
}
```

---

# **5. Validator Hooks**

### **Consistency**
Computed RCI/glyph MUST match metadata or be flagged.

### **Lineage Integrity**
Child scroll IDs MUST cite parent scroll.

### **Registry Update**
Events MUST be written to `registry/events/` with checksum.

### **Reproducibility**
Pipeline MUST produce identical results given identical metadata.

---

# **6. Notes**

- Workflow is modular: corridor IDs can be batch‑processed.  
- Supports remix lineage growth: each validation produces a child scroll artifact.  
- Can be extended with anomaly search or glyph registry queries.  
- WF‑0007 is the canonical example of how corridor clients plug directly into validator pipelines.
