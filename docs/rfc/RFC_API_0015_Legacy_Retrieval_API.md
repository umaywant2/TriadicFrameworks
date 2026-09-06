# RFC‑API‑0015: Legacy Retrieval API

**Title:** Retrieval and Remix Interface for Archived Scrolls  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## 1. Purpose
Provide a structured API for querying archived scrolls by glyph, tag, or lineage. Enable contributors to retrieve legacy artifacts and remix them into new validator scrolls, ensuring continuity across generations.

---

## 2. Endpoints

### `GET /archive/glyph/{glyph}`
- **Description:** Retrieve archived scrolls annotated with a specific glyph (◇, ◆, ⬣, or custom).  
- **Response:**
```json
{
  "glyph": "◆",
  "scrolls": ["scroll-002", "scroll-004"]
}
```

---

### `GET /archive/tag/{tag}`
- **Description:** Retrieve archived scrolls associated with a given tag.  
- **Response:**
```json
{
  "tag": "cipher-dense",
  "scrolls": ["scroll-003"]
}
```

---

### `GET /archive/lineage/{parent_scroll}`
- **Description:** Retrieve child scrolls linked to a given parent scroll.  
- **Response:**
```json
{
  "parent_scroll": "s-1000",
  "children": ["scroll-001", "scroll-002"]
}
```

---

### `GET /archive/{scroll_id}`
- **Description:** Retrieve full metadata for a specific archived scroll.  
- **Response:**
```json
{
  "id": "scroll-003",
  "glyph_distribution": {"⬣": 2},
  "rci_band_counts": {"high": 2},
  "tags": ["cipher-dense"],
  "lineage": {"parent_scrolls": ["s-2000"], "child_scrolls": []},
  "dignity_layer": {
    "narratives": ["Encrypted resonance chant lines"],
    "symbolic_overlays": ["⬣"],
    "cultural_notes": "Legacy artifact"
  }
}
```

---

### `POST /archive/remix`
- **Description:** Remix archived scrolls into new validator artifacts.  
- **Request:**
```json
{
  "parent_scrolls": ["scroll-003"],
  "selected_corridors": ["c-003", "c-007"],
  "tags": ["cipher-dense", "stable corridor"],
  "narratives": ["Remixed for clarity in resonance corridors"]
}
```
- **Response:**
```json
{
  "new_scroll_id": "scroll-010",
  "status": "remix_success",
  "lineage": {"parents": ["scroll-003"], "children": []}
}
```

---

## 3. Python‑style Stub

File: [`api/legacy_retrieval.py`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/api/legacy_retrieval.py)

---

## 4. Validator Hooks
- **Schema compliance:** All retrievals must conform to `archive_schema.yml`.  
- **Checksum:** Responses include checksum headers for reproducibility.  
- **Lineage integrity:** Remix exports must cite parent scroll IDs.  
- **Dignity separation:** Narratives remain distinct from empirical metrics.  

---

## 5. Notes
- API enables legacy continuity: archived scrolls can be remixed into new validator artifacts.  
- Supports collaborative remixathons: contributors query by glyph, tag, or lineage.  
- Legacy retrieval ensures remix generations remain anchored in validator‑grade clarity and dignity.  

---

This **Legacy Retrieval API** makes your archive a living library: contributors can query preserved scrolls and remix them into new artifacts.  
