# RFC‑REG‑0004: Registry Indexer for Corridor Events

**Title:** Corridor Registry Indexer  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## 1. Purpose
Define the indexer that consumes `rci_registry_event.yml` entries, normalizes corridor metadata, and builds searchable indices by glyph type, RCI band, and remix ancestry.  

---

## 2. Index Dimensions

- **Glyph Type Index:**  
  - Keys: ◇ (alpha), ◆ (beta), ⬣ (gamma)  
  - Values: corridor IDs grouped by glyph  

- **RCI Band Index:**  
  - Bands:  
    - Low: 0.00–0.33  
    - Medium: 0.34–0.66  
    - High: 0.67–1.00  
  - Values: corridor IDs grouped by band  

- **Remix Ancestry Index:**  
  - Keys: parent_scroll UUID  
  - Values: list of child_scroll UUIDs  

---

## 3. Schema Extension

File: `registry/index/index_schema.yml`

```yaml
index:
  glyph_type:
    ◇: [c-002, c-010, ...]
    ◆: [c-001, c-004, ...]
    ⬣: [c-003, c-007, ...]
  rci_band:
    low: [c-002, c-005]
    medium: [c-001, c-004]
    high: [c-003, c-007]
  remix_ancestry:
    parent_scrolls:
      s-1001: [s-1002, s-1003]
      s-2001: [s-2002]
```

---

## 4. Python‑style Indexer Stub

File: `registry/index/indexer.py`

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

    return {"glyph_type": glyph_index, "rci_band": rci_index, "remix_ancestry": ancestry_index}

def export_index(indices, outfile="registry/index/index_schema.yml"):
    with open(outfile, "w") as stream:
        yaml.dump({"index": indices}, stream, sort_keys=False)
```

---

## 5. Validator Hooks
- **Consistency:** Ensure corridor IDs appear in exactly one glyph bucket and one RCI band.  
- **Lineage Integrity:** Parent scrolls must exist before child scrolls are indexed.  
- **Checksum:** Each index export includes checksum of source events.  

---

## 6. Notes
- Indexer is deterministic: same event set yields identical indices.  
- Supports incremental updates: new events appended, indices rebuilt.  
- Glyph, RCI band, and ancestry indices are queryable via API endpoints.  

---

This scaffold gives you a working indexer: it ingests event YAMLs, builds glyph/RCI/ancestry indices, and exports them back into the registry.  
