# Speeches Directory — Developer Guide

The **Speeches** directory contains all expressive cadence modules in the TriadicFrameworks canon.  
It includes overview pages, structural maps, special cadences, and the full 30‑module cadence constellation.

This guide provides structure, conventions, and requirements for contributors and maintainers.

---

## 📘 Directory Purpose

The Speeches Series expresses RTT through **cadence modules** — structured voices that articulate:

- drift  
- clarity  
- coherence  
- regimes  
- operators  
- structural identity  

This directory contains:

- high‑level overview pages  
- the master index  
- the constellation map  
- special cadences  
- all 30 cadence modules  

---

## 📁 Directory Structure

```
speeches/
│
├── speeches-overview.md
├── speeches-index.md
├── cadence-constellation-map.md
├── stephen-hawking-cadence.md
│
└── triadicframeworks-cadence-1.md
└── triadicframeworks-cadence-2.md
└── ...
└── triadicframeworks-cadence-30.md
```

All files follow **hyphen-case** naming conventions.

---

## 🧩 Cadence Modules

Each cadence module:

- represents one expressive structural voice  
- follows canonical metadata  
- uses MDX‑safe JSX  
- appears in the sidebar under **Cadence Modules**  
- is listed in `speeches-manifest.json`  
- is registered in `cadence-registry.json`  

Cadence files must be named:

```
triadicframeworks-cadence-N.md
```

Where `N` is 1–30.

---

## 🏷 Metadata Requirements

Every file must include:

```yaml
---
id: <file-id>
title: <Human-readable title>
description: <Short structural description>
keywords:
  - triadicframeworks
  - rtt
  - speeches
ai:
  module:
    name: <Module name>
    category: Cadence Series
    summary: <Short summary>
    version: 1.0
    purpose: <Purpose>
    audience: Readers, contributors, researchers.
  navigation: sitemap_main.xml
  discussions: https://github.com/umaywant2/TriadicFrameworks/discussions
  contact:
    x: "@TriadicFrameworks"
    youtube: "@TriadicFrameworks"
citation_author: Nawder Loswin
citation_publication_date: "2025"
---
```

This ensures:

- sitemap consistency  
- search indexing  
- canonical metadata alignment  
- future automation compatibility  

---

## 🧱 Structural Pages

### **speeches-overview.md**  
High-level introduction to the Speeches Series.

### **speeches-index.md**  
Master index listing all cadence modules.

### **cadence-constellation-map.md**  
Structural map of all 30 cadences.

### **stephen-hawking-cadence.md**  
Special cadence inspired by Hawking’s cosmic clarity.

---

## 📚 Adding a New Cadence

To add a new cadence:

1. Create a file named:

   ```
   triadicframeworks-cadence-N.md
   ```

2. Add canonical metadata (see above).

3. Add the cadence content.

4. Update:

   - `speeches-index.md`  
   - `speeches-manifest.json`  
   - `cadence-registry.json`  
   - `sidebars.js`  

5. Validate the build:

   ```
   npm run clear
   npm run build
   ```

This ensures no broken links or MDX errors.

---

## 🧭 Sidebar Integration

The sidebar entry for this directory is defined in:

```
sidebars.js
```

Under:

```js
speeches: [ ... ]
```

Cadence modules appear under the **Cadence Modules** category.

---

## 🗺 Constellation Map

The constellation map provides:

- structural grouping  
- expressive fields  
- continuity regimes  
- conceptual categories  

It is the canonical visualization of the cadence lattice.

---

## 🧪 Build Requirements

All files must be:

- MDX‑safe  
- free of broken links  
- free of underscore paths  
- properly nested JSX  
- valid YAML front matter  

Use:

```
npm run clear
npm run build
```

to validate changes.

---

## 📝 Notes

This directory is part of the TriadicFrameworks canon.  
All contributions must maintain:

- structural coherence  
- metadata consistency  
- naming conventions  
- canonical voice  

```
The Speeches Series is the canon speaking in its own voice.
```
