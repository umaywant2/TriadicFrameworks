# RFC‑LIB‑0011: Tag Registry and Glyph Library

**Title:** Canonical Tag Registry and Glyph Library for Remixathon Annotations  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## 1. Purpose
Provide a centralized registry of remix tags and glyphs to ensure annotation consistency. Contributors can search, reuse, and remix tags/glyphs across scrolls and dashboards, preventing fragmentation.

---

## 2. Tag Registry

### Schema

File: [`registry/tags/tag_schema.yml`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/registry/tags/tag_schema.yml)

---

### Example Entries

```yaml
- id: t-001
  name: "cipher-dense"
  description: "Corridor with high encryption density"
  category: semantic
  created_by: user42
  timestamp: 2025-11-12T10:45:00Z

- id: t-002
  name: "fluid-turbulent"
  description: "Corridor with chaotic fluid rail signatures"
  category: rail
  created_by: user17
  timestamp: 2025-11-12T10:46:00Z
```

---

## 3. Glyph Library

### Schema

File: [`registry/glyphs/glyph_schema.yml`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/registry/glyphs/glyph_schema.yml)

---

### Example Entries

```yaml
- id: g-001
  symbol: "◇"
  name: "Alpha Corridor"
  meaning: "Low cipher-density resonance zone"
  category: corridor
  created_by: system
  timestamp: 2025-11-12T10:45:00Z

- id: g-002
  symbol: "◆"
  name: "Beta Corridor"
  meaning: "Medium cipher-density resonance zone"
  category: corridor
  created_by: system
  timestamp: 2025-11-12T10:45:00Z

- id: g-003
  symbol: "⬣"
  name: "Gamma Corridor"
  meaning: "High cipher-density resonance zone"
  category: corridor
  created_by: system
  timestamp: 2025-11-12T10:45:00Z
```

---

## 4. API Endpoints

- `GET /tags` → List all tags.  
- `GET /tags/{id}` → Retrieve tag details.  
- `POST /tags` → Create new tag.  
- `GET /glyphs` → List all glyphs.  
- `GET /glyphs/{id}` → Retrieve glyph details.  
- `POST /glyphs` → Create new glyph.  

---

## 5. Dashboard Integration

- **Autocomplete:** Annotation panel pulls tag registry for consistent naming.  
- **Glyph Selector:** Dashboard nodes display glyph library icons; contributors choose from canonical set.  
- **Search:** Contributors can filter corridors by tag or glyph across remixathon reports.  

---

## 6. Validator Hooks

- **Schema compliance:** All tags/glyphs must conform to schema.  
- **Checksum:** Each entry includes checksum for reproducibility.  
- **Lineage integrity:** New tags/glyphs must cite parent lineage if derived.  
- **Separation:** Cultural glyphs stored distinctly from rail glyphs.  

---

## 7. Notes

- Registry ensures remixathons remain remixable: tags and glyphs are consistent across contributors.  
- Glyph library supports both Unicode symbols and custom SVG paths for richer overlays.  
- Tags and glyphs are validator‑grade artifacts, archived in `registry/tags/` and `registry/glyphs/`.  

---

This scaffold gives you a canonical registry and library for tags and glyphs, ensuring remixathon annotations are consistent, searchable, and remixable.  
