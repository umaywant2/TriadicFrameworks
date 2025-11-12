# RFC‑UI‑0010: Collaborator Annotation Layer

**Title:** Symbolic Annotation and Remix Tagging for Dashboard Nodes  
**Status:** Concept Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## 1. Purpose
Enable contributors to enrich corridor resonance exploration by attaching annotations to dashboard nodes. These annotations can be symbolic (glyphs, icons), remix tags (semantic labels), or cultural narratives (textual overlays).  

---

## 2. Annotation Types

- **Symbolic Notes:**  
  - Glyphs or icons layered onto nodes (e.g., ◇, ◆, ⬣, custom cultural glyphs).  
  - Used to highlight resonance qualities or symbolic interpretations.  

- **Remix Tags:**  
  - Short semantic labels (e.g., “cipher‑dense”, “fluid‑turbulent”, “stable corridor”).  
  - Tags are searchable and filterable across dashboard panels.  

- **Cultural Narratives:**  
  - Free‑form text overlays capturing human interpretation, ritual notes, or artistic resonance.  
  - Stored in dignity layer of scroll schema; optional toggle in dashboard.  

---

## 3. Dashboard Integration

### Node Interaction
- **Click Node:** Opens annotation panel.  
- **Panel Fields:**  
  - Symbolic glyph selector.  
  - Remix tag input (autocomplete from tag registry).  
  - Narrative text box.  
- **Save Action:** Commits annotation to registry with lineage link.  

### Visual Overlays
- **Glyphs:** Rendered directly on node icon.  
- **Tags:** Displayed as hover tooltips.  
- **Narratives:** Accessible via expandable sidebar.  

---

## 4. Schema Extension

File: [`registry/annotations/annotation_schema.yml`](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/registry/annotations/annotation_schema.yml)

---

## 5. API Endpoints

- `POST /annotations` → Submit new annotation.  
- `GET /annotations/{corridor_id}` → Retrieve annotations for a corridor.  
- `GET /annotations/tags/{tag}` → Search corridors by remix tag.  
- `GET /annotations/contributor/{id}` → View annotations by contributor.  

---

## 6. Collaboration Features

- **Real‑time Sync:** WebSocket or polling to update dashboard nodes with new annotations.  
- **Contributor Attribution:** Each annotation linked to contributor ID; displayed in tooltips.  
- **Remix Lineage:** Annotations treated as remix events; child scrolls inherit annotation metadata.  

---

## 7. Validator Hooks

- **Schema compliance:** All annotations must conform to `annotation_schema.yml`.  
- **Checksum:** Each annotation event includes checksum for reproducibility.  
- **Lineage integrity:** Annotations must cite parent/child scroll IDs.  
- **Separation:** Cultural narratives stored in dignity layer, distinct from empirical metrics.  

---

## 8. Concept Sketch (textual)

```
[Lineage Graph Node: c-003 ⬣]
 └─ Symbolic Note: ⬣ (cipher-dense glyph)
 └─ Remix Tags: ["stable corridor", "gamma-band"]
 └─ Narrative: "This corridor resonates like encrypted chant lines."
 └─ Contributor: user42
```

---

This annotation layer makes the dashboard collaborative and remix‑ready: contributors can symbolically mark resonance corridors, tag them for semantic clarity, and narrate their cultural meaning.  
