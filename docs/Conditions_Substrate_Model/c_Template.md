# c_Template.md  
### Canonical Module Template — TriadicFrameworks

This file provides the **standard structural scaffold** for any TriadicFrameworks module.  
Use it when creating new modules or refreshing existing ones.

---

## 1. Identity
**Module:**  
**Category:**  
**Purpose:**  
**Version:** 2026.07  
**Front door:** /docs/<module_name>/

---

## 2. Roles (TriadicFrameworks Grammar)
- **engine** — core logic or substrate model  
- **profile** — dimensional or substrate-specific mapping  
- **signature** — canonical signatures  
- **diagnostic** — thresholds, audits, diff tables  
- **map** — atlases, flows, vectors  
- **example** — worked examples  
- **extension** — optional expansions  
- **index** — front door / capture page  
- **reference** — dictionaries, glossaries  
- **template** — this file

---

## 3. Analyzer Layers
- operator  
- dimensional  
- regime  
- drift  
- coherence  
- cross-cutting  

Enable layers as needed in `module.json`.

---

## 4. Canonical Blocks
Each module includes:

- **Metadata block** (`c_Metadata.html`)  
- **Session context** (`c_Session_Context.html`)  
- **Badge** (`c_Badge.html`)  
- **Sidebar audit** (`c_Sidebar_Audit.html`)  
- **Diff table** (`c_Diff_Table.html`)  
- **module.json**  
- **modules_group.json**  
- **sitemap_entry.xml**

These blocks are required for canonical compliance.

---

## 5. File Structure (example)
```
/docs/<module_name>/
  c_Capture.md
  c_Metadata.html
  c_Session_Context.html
  c_Badge.html
  c_Sidebar_Audit.html
  c_Diff_Table.html
  module.json
  modules_group.json
  sitemap_entry.xml
  c_Template.md
```

---

## 6. Notes
Use this template as the starting point for any new module.  
Replace placeholders with module-specific content.

---

## 7. Maintainers
Nawder Loswin — TriadicFrameworks  
AI-assisted canonical maintenance (2025–2026)
