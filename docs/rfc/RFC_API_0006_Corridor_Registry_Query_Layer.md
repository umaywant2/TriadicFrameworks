# RFC‑API‑0006: Corridor Registry Query Layer

**Title:** API Query Layer for Corridor Indices  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## 1. Purpose
Provide REST‑style endpoints and query functions so external tools can request corridor data without parsing YAML directly. The API consumes the registry indices built by the indexer and returns structured JSON responses.

---

## 2. Endpoints

### `GET /corridors/glyph/{glyph}`
- **Description:** Return all corridor IDs annotated with a given glyph (◇, ◆, ⬣).  
- **Response:**
```json
{
  "glyph": "◆",
  "corridors": ["c-001", "c-004", "c-011"]
}
```

---

### `GET /corridors/rci/{band}`
- **Description:** Return corridor IDs grouped by RCI band (`low`, `medium`, `high`).  
- **Response:**
```json
{
  "band": "high",
  "corridors": ["c-003", "c-007"]
}
```

---

### `GET /corridors/remix/{parent_scroll}`
- **Description:** Return child scrolls linked to a given parent scroll.  
- **Response:**
```json
{
  "parent_scroll": "s-1001",
  "children": ["s-1002", "s-1003"]
}
```

---

### `GET /corridors/{id}`
- **Description:** Return full metadata for a specific corridor.  
- **Response:**
```json
{
  "id": "c-001",
  "glyph": "◆",
  "cipher_density": "beta",
  "resonance_clarity_index": 0.420,
  "rail_signatures": {
    "frequency": 0.42,
    "fluids": 0.39,
    "forces": 0.45
  },
  "lineage": {
    "parent_scroll": "s-1000",
    "child_scrolls": ["s-1001"]
  }
}
```

---

## 3. Python‑style API Stub

File: `api/corridor_api.py`

```python
from flask import Flask, jsonify
import yaml

app = Flask(__name__)

# Load indices once at startup
with open("registry/index/index_schema.yml", "r") as stream:
    indices = yaml.safe_load(stream)["index"]

@app.route("/corridors/glyph/<glyph>", methods=["GET"])
def get_corridors_by_glyph(glyph):
    return jsonify({"glyph": glyph, "corridors": indices["glyph_type"].get(glyph, [])})

@app.route("/corridors/rci/<band>", methods=["GET"])
def get_corridors_by_rci(band):
    return jsonify({"band": band, "corridors": indices["rci_band"].get(band, [])})

@app.route("/corridors/remix/<parent_scroll>", methods=["GET"])
def get_corridors_by_remix(parent_scroll):
    return jsonify({"parent_scroll": parent_scroll, "children": indices["remix_ancestry"].get(parent_scroll, [])})

@app.route("/corridors/<cid>", methods=["GET"])
def get_corridor_metadata(cid):
    # In practice, load from scroll registry
    # Here we stub with minimal metadata
    return jsonify({
        "id": cid,
        "glyph": "◆",
        "cipher_density": "beta",
        "resonance_clarity_index": 0.42,
        "rail_signatures": {"frequency": 0.42, "fluids": 0.39, "forces": 0.45},
        "lineage": {"parent_scroll": "s-1000", "child_scrolls": ["s-1001"]}
    })
```

---

## 4. Validator Hooks
- **Schema compliance:** All responses must conform to JSON schema defined in RFC‑QEB‑0002.  
- **Checksum:** API responses include optional checksum header for reproducibility.  
- **Versioning:** Endpoints tagged with API version (`/v1/corridors/...`).  

---

## 5. Notes
- API abstracts YAML; external tools interact only with JSON.  
- Supports incremental updates: indexer rebuild triggers API refresh.  
- Glyph, RCI band, and ancestry queries are lightweight and cacheable.  

---

This API layer makes your corridor registry accessible to external tools without touching raw YAML.  
