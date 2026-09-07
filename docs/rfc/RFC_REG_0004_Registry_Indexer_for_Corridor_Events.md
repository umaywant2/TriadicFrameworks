# **RFC‑REG‑0004 — Registry Indexer for Corridor Events**  
### *Canonical Indexer for Glyph, RCI Band, and Remix Lineage Metadata*  
RefId: turn0browsertab1

**Title:** Corridor Registry Indexer  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.2  

---

## **1. Purpose**

The **Corridor Registry Indexer (CRI)** consumes `rci_registry_event.yml` entries, normalizes corridor metadata, and builds **searchable, validator‑grade indices** across three dimensions:

- **Glyph Type** (cipher‑density classification)  
- **RCI Band** (resonance clarity classification)  
- **Remix Ancestry** (lineage mapping between scrolls)

CRI is the backbone of corridor search, lineage visualization, dashboard filtering, and archival retrieval.

It ensures:

- deterministic indexing  
- drift‑safe classification  
- lineage integrity  
- validator‑grade reproducibility  

---

## **2. Index Dimensions**

CRI builds three canonical indices.

---

### **2.1 Glyph Type Index**

Glyphs represent **cipher‑density classes**:

- **◇** — alpha (low density)  
- **◆** — beta (medium density)  
- **⬣** — gamma (high density)

**Index Structure:**

```
glyph_type:
  ◇: [c-002, c-010, ...]
  ◆: [c-001, c-004, ...]
  ⬣: [c-003, c-007, ...]
```

Glyph index enables:

- dashboard glyph wheel  
- corridor search filtering  
- lineage glyph inheritance  
- archival glyph queries  

---

### **2.2 RCI Band Index**

RCI (Resonance Clarity Index) is a composite clarity score (0–1).

Bands:

- **Low:** 0.00–0.33  
- **Medium:** 0.34–0.66  
- **High:** 0.67–1.00  

**Index Structure:**

```
rci_band:
  low:    [c-002, c-005]
  medium: [c-001, c-004]
  high:   [c-003, c-007]
```

RCI band index powers:

- clarity histogram  
- search filtering  
- validator clarity checks  
- remix lineage clarity inheritance  

---

### **2.3 Remix Ancestry Index**

Tracks parent → child lineage relationships.

**Index Structure:**

```
remix_ancestry:
  parent_scrolls:
    s-1001: [s-1002, s-1003]
    s-2001: [s-2002]
```

Ancestry index powers:

- lineage graph  
- remix diff protocol  
- archival ancestry queries  
- validator lineage integrity checks  

---

## **3. Schema Extension**

File:  
```
registry/index/index_schema.yml
```

Canonical schema:

```yaml
index:
  glyph_type:
    ◇: [c-002, c-010]
    ◆: [c-001, c-004]
    ⬣: [c-003, c-007]

  rci_band:
    low:    [c-002, c-005]
    medium: [c-001, c-004]
    high:   [c-003, c-007]

  remix_ancestry:
    parent_scrolls:
      s-1001: [s-1002, s-1003]
      s-2001: [s-2002]
```

Schema integrates with:

- **RFC_SCHEMA_0001** (scroll artifact schema)  
- **RFC_REMIX_0005** (lineage diff protocol)  
- **RFC_EXP_0013** (export module)  
- **RFC_ARC_0014** (archival protocol)  
- **RFC_ENG_0012** (search/filter engine)  

---

## **4. Python‑Style Indexer Stub**

File:  
```
registry/index/indexer.py
```

This scaffold ingests event YAMLs, builds indices, and exports them.

```python
import yaml
from collections import defaultdict

def load_events(event_files):
    events = []
    for f in event_files:
        with open(f, "r") as stream:
            events.append(yaml.safe_load(stream))
    return events

def build_indices(events):
    glyph_index = defaultdict(list)
    rci_index = {"low": [], "medium": [], "high": []}
    ancestry_index = defaultdict(list)

    for ev in events:
        cid = ev["event"]["corridor_id"]
        glyph = ev["event"]["new_glyph"]
        rci = ev["event"]["new_rci"]
        parent = ev["event"]["lineage"]["parent_scroll"]
        child = ev["event"]["lineage"]["child_scroll"]

        # Glyph index
        glyph_index[glyph].append(cid)

        # RCI band index
        if rci <= 0.33:
            rci_index["low"].append(cid)
        elif rci <= 0.66:
            rci_index["medium"].append(cid)
        else:
            rci_index["high"].append(cid)

        # Remix ancestry
        if parent and child:
            ancestry_index[parent].append(child)

    return {
        "glyph_type": glyph_index,
        "rci_band": rci_index,
        "remix_ancestry": ancestry_index
    }

def export_index(indices, outfile="registry/index/index_schema.yml"):
    with open(outfile, "w") as stream:
        yaml.dump({"index": indices}, stream, sort_keys=False)
```

---

## **5. Validator Hooks**

### **Consistency**
Corridor IDs must appear in:

- exactly one glyph bucket  
- exactly one RCI band  

### **Lineage Integrity**
Parent scrolls must exist before child scrolls are indexed.

### **Checksum**
Each index export includes a checksum of source events.

### **Determinism**
Given the same event set, CRI must produce identical indices.

### **Incremental Updates**
New events append cleanly; indices rebuild deterministically.

---

## **6. Notes**

- CRI is the backbone of corridor search, lineage visualization, and archival retrieval.  
- Glyph, RCI band, and ancestry indices are queryable via API endpoints.  
- Indexer is deterministic and validator‑grade.  
- Integrates with all Remixathon workflows.
