# **61_README.md — Grammar for Intelligence Module Metadata**

This directory contains the **canonical metadata** for the *Grammar for Intelligence* ebook module within the TriadicFrameworks documentation system. It provides structural identity, AI‑ready metadata, analyzer‑layer definitions, and file‑level roles used by agents, builders, and stewards.

The metadata in this directory follows the **TriadicFrameworks module.schema.json** specification:

- **role enums:** `engine`, `profile`, `signature`, `diagnostic`, `map`, `example`, `extension`, `index`, `reference`, `template`  
- **analyzer_layer enums:** `operator`, `dimensional`, `regime`, `drift`, `coherence`, `cross-cutting`

This directory is part of the **Education → eBooks** domain.

---

## **Files in This Directory**

### **`60_module.json`**  
The canonical manifest for the *Grammar for Intelligence* ebook module.  
Defines:

- module identity  
- structural purpose  
- analyzer layers  
- AI metadata block  
- canonical URL  
- citation fields  
- file‑level roles  

This file is required for:

- sitemap generation  
- agent discovery  
- module introspection  
- metadata refresh workflows  

### **`61_README.md`**  
You are reading it.  
Provides human‑readable documentation for the metadata directory.

---

## **Module Purpose**

The *Grammar for Intelligence* module defines the structural grammar of coherent AI systems:

- operators  
- invariants  
- regimes  
- substrates  
- governance  
- drift containment  
- coherence engineering  

Its metadata ensures the ebook is discoverable, analyzable, and structurally consistent across the TriadicFrameworks ecosystem.

---

## **Metadata Refresh Protocol (Summary)**

This module follows the standard TriadicFrameworks metadata refresh pattern:

1. **Canonical `<head>` block**  
2. **Session context section**  
3. **Module badge**  
4. **Sidebar phantom‑entry audit**  
5. **Diff table (old vs new)**  
6. **module.json validation**  
7. **AI metadata block alignment**

The current `60_module.json` is fully refreshed and structurally complete.

---

## **Upstream Source**

Primary manuscript:  
`docs/education/ebooks/Grammar_for_Intelligence/gi_Capture.md`

This file is referenced in the module manifest as the **signature** document.

---

## **Downstream Consumers**

- TriadicFrameworks agents  
- sitemap generators  
- module browsers  
- AI‑assisted documentation tools  
- metadata validators  
- coherence analyzers  

---

## **Notes for Maintainers**

- Keep `60_module.json` aligned with `module.schema.json`.  
- Update citation year only when the ebook receives a major revision.  
- Ensure AI metadata fields remain consistent with the ebook’s structural purpose.  
- Run phantom‑entry audits after adding or removing files.  
- Maintain neutral‑tone, canon‑aligned documentation.
