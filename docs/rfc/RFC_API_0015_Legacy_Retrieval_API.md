# **RFC‑API‑0015 — Legacy Retrieval API**  
### *Retrieval and Remix Interface for Archived Scrolls*

**Title:** Legacy Retrieval API  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.2  

---

## **1. Purpose**

The **Legacy Retrieval API (LRA)** provides a unified interface for querying archived scrolls, validator artifacts, glyph‑annotated documents, and lineage‑bound historical materials.  
Its goals:

- Retrieve legacy scrolls by **glyph**, **tag**, **lineage**, or **scroll ID**  
- Provide structured metadata for remixing into new validator scrolls  
- Maintain continuity across generations of TriadicFrameworks artifacts  
- Ensure drift‑safe, paradox‑safe access to historical materials  
- Support corridor, temporal, substrate, and identity‑family retrieval patterns

LRA is the **read‑only historical layer** of the TriadicFrameworks API canon.

---

## **2. Endpoint Overview**

All endpoints follow the canonical REST pattern:

```
GET /archive/<query_type>/<parameter>
```

Supported query types:

- `glyph`
- `tag`
- `lineage`
- `scroll`

Each endpoint returns structured JSON aligned with TriadicFrameworks metadata conventions.

---

## **3. Endpoints**

---

### **3.1 GET /archive/glyph/{glyph}**

Retrieve archived scrolls annotated with a specific glyph.

**Glyph Types Supported:**

- `◇` — Corridor glyph  
- `◆` — Temporal glyph  
- `⬣` — Substrate glyph  
- Custom glyphs registered in `/glyphs/registry`

**Response Example:**

```json
{
  "glyph": "◆",
  "scrolls": ["scroll-002", "scroll-004"],
  "count": 2
}
```

---

### **3.2 GET /archive/tag/{tag}**

Retrieve archived scrolls associated with a given tag.

Tags may represent:

- density classes  
- cipher families  
- validator categories  
- drift‑band identifiers  
- contributor annotations  

**Response Example:**

```json
{
  "tag": "cipher-dense",
  "scrolls": ["scroll-003"],
  "count": 1
}
```

---

### **3.3 GET /archive/lineage/{parent_scroll}**

Retrieve child scrolls linked to a given parent scroll.

Lineage relationships include:

- direct descendants  
- remix derivatives  
- validator‑approved children  
- glyph‑inherited scrolls  

**Response Example:**

```json
{
  "parent_scroll": "s-1000",
  "children": ["scroll-001", "scroll-002"],
  "count": 2
}
```

---

### **3.4 GET /archive/{scroll_id}**

Retrieve full metadata for a specific archived scroll.

Metadata includes:

- glyph distribution  
- RCI band counts  
- tags  
- lineage  
- validator signatures  
- resonance‑time annotations (if present)

**Response Example:**

```json
{
  "id": "scroll-003",
  "glyph_distribution": { "⬣": 2 },
  "rci_band_counts": { "high": 2 },
  "tags": ["cipher-dense"],
  "lineage": {
    "parent": "s-1000",
    "siblings": ["scroll-001", "scroll-002"]
  }
}
```

---

## **4. Error Model**

All endpoints return canonical error objects:

| Error Code | Meaning |
|-----------|---------|
| `ERR-NOT-FOUND` | Scroll, glyph, or tag does not exist |
| `ERR-INVALID-PARAM` | Parameter malformed or unsupported |
| `ERR-LINEAGE-BROKEN` | Lineage chain incomplete or corrupted |
| `ERR-DRIFT-UNSAFE` | Retrieval blocked due to drift threshold |
| `ERR-PARADOX-VECTOR` | Retrieval blocked due to paradox risk |

**Error Response Example:**

```json
{
  "error": "ERR-NOT-FOUND",
  "detail": "No scrolls found for glyph ◆"
}
```

---

## **5. Metadata Schema**

All scroll metadata follows the canonical schema:

```json
{
  "id": "scroll-XXX",
  "glyph_distribution": { "<glyph>": <count> },
  "rci_band_counts": { "low": 0, "medium": 1, "high": 2 },
  "tags": ["tag-1", "tag-2"],
  "lineage": {
    "parent": "scroll-YYY",
    "children": ["scroll-ZZZ"]
  },
  "validator": {
    "state": "stable",
    "signature": "VS-ΔΩ-14"
  }
}
```

---

## **6. Remix Workflow Integration**

The Legacy Retrieval API integrates with:

- **RFC‑API‑0016: Remix Construction Layer**  
- **RFC‑API‑0017: Validator Scroll Builder**  
- **RFC‑API‑0018: Glyph Distribution Engine**

This allows contributors to:

- retrieve legacy scrolls  
- extract glyph distributions  
- remix into new validator scrolls  
- preserve lineage continuity  

---

## **7. Notes**

- All retrieval operations are **read‑only**  
- Drift‑unsafe scrolls require validator override  
- Paradox‑vector scrolls require guardian clearance  
- Legacy scrolls may contain deprecated glyphs; these are preserved for historical accuracy  

---

## **8. Closing Statement**

RFC‑API‑0015 defines the **Legacy Retrieval API**, the canonical interface for accessing archived scrolls, glyph distributions, lineage structures, and validator metadata.  
It ensures continuity across generations of TriadicFrameworks artifacts and provides a stable foundation for remixing, validator construction, and historical analysis.
