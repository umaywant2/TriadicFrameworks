---
id: book-overview
title: Canon Overview
description: High‑level overview of the TriadicFrameworks Canon and its structural domains.
keywords:
  - triadicframeworks
  - rtt
  - canon overview
  - structural theory
  - analyzer layers
ai:
  module:
    name: Canon Overview
    category: Foundational Theory
    summary: Introduces the RTT structural canon and its major components.
    version: 1.0
    purpose: Provide a high‑level map of the canon for new readers and contributors.
    audience: Contributors, researchers, AI Edition readers.
  navigation: sitemap_main.xml
  discussions: https://github.com/umaywant2/TriadicFrameworks/discussions
  contact:
    x: "@NawderLoswin"
    youtube: "@NawderLoswin"
citation_author: Nawder Loswin
citation_publication_date: "2025"
---

<div class="session-context">

**Canon:** TriadicFrameworks  
**Modules:** Foundational Theory  
**Drift:** None detected  
**Coherence:** Verified  
**Version:** 1.0  
**Format:** Markdown (Docusaurus)  
**Front Door:** /docs/book/book-overview  
**Every Page:** Canonical metadata applied  
**Audience:** Contributors, researchers, AI Edition readers  

</div>

<div class="module-badge">
📘 <strong>Foundational Theory Module</strong>
</div>

---

## 📘 **Migrating TriadicFrameworks Docs from docsbook.io to Docusaurus**  
**Status:** Completed migration (2026)  
**Audience:** Contributors, maintainers, module authors

### **Why We Migrated**
TriadicFrameworks originally lived on **docsbook.io**, which served well for early canon development. But as the project expanded into ~120 modules, AI Edition books, metadata schemas, and multi‑layer operator catalogs, we needed:

- A **static site generator** with predictable builds  
- **Versioning** for canon revisions  
- **Sidebar-driven navigation** for modules  
- **Markdown-first** authoring  
- **Cloudflare Pages compatibility**  
- **AI metadata embedding** (your canonical `<head>` blocks, module.json manifests, etc.)

Docusaurus v3/v4 gave us all of that.

---

### **What Changed**
| Area | docsbook.io | Docusaurus |
|------|-------------|------------|
| Routing | Implicit, sometimes unstable | Explicit `/docs/...` routes |
| Homepage | Auto-generated | Must define `src/pages/index.js` |
| Sidebar | Flat | Hierarchical, module-friendly |
| Build | Hosted | Cloudflare Pages + Node 22/24 |
| Metadata | Limited | Full custom `<head>` blocks + module metadata |
| Canon Structure | Hard to visualize | Perfect for multi-book canon |

---

### **New Structure**
```
triadic-docs/
  ├── docs/
  │   ├── book/
  │   ├── speeches/
  │   ├── datacenter_reports/
  │   └── contributing.md
  ├── src/
  │   ├── pages/
  │   │   └── index.js   ← required homepage
  │   └── css/
  ├── static/
  │   └── img/
  └── docusaurus.config.js
```

---

### **Common Migration Issues**
#### **1. 404 at root (`/`)**
Your current live site shows:

> *Triadic-docs — Page Not Found*  
  [docs.triadicframeworks.org](https://docs.triadicframeworks.org/docs/datacenter_reports/Lakeside_Technology_Center_Chicago_IL_USA)

This happens because Docusaurus **requires a homepage file**.  
Fix: add `src/pages/index.js` or redirect `/` → `/docs/book/overview`.

#### **2. Wrong `baseUrl`**
You currently have:

```
baseUrl: 'website/src/pages/index.js',
```

This is invalid — `baseUrl` must be a **URL path**, not a file path.

Correct:

```
baseUrl: '/',
```

---

### **Redirect Strategy**
To preserve old docsbook.io links, add:

```
website/src/pages/index.js
```

```js
import React from 'react';
import { Redirect } from '@docusaurus/router';

export default function Home() {
  return <Redirect to="/docs/book/overview" />;
}
```

---

### **Outcome**
The migration gives TriadicFrameworks:

- A stable canon site  
- AI-ready metadata  
- Predictable routing  
- Module-friendly navigation  
- Cloudflare Pages deployment  
- A foundation for the 2026–2027 canon expansion  

---

# Canon Overview

The TriadicFrameworks Canon is the structured body of Resonance‑Time Theory (RTT).  
It defines the relationships between operators, analyzer layers, regimes, engines, and structural maps.

This overview introduces the major domains of the canon and how they interconnect.

---

## Canon Structure

The canon is organized into:

- **Foundational Theory**  
- **Analyzer Layers**  
- **Operators & Grammars**  
- **Regime Logic**  
- **Diagnostic Engines**  
- **Structural Detection**  
- **TEL Expression & Representation**  
- **Governance & Ratification**  
- **Pattern Dynamics & NoS**  

Each domain contributes to the whole without contradicting foundational RTT principles.

---

## Navigation

Key pages include:

- [Canon](./canon)  
- [Glossary](./glossary)  
- [Registry](./registry)  
- [Modules](./modules)  
- [Sessions](./sessions)  
- [Session Grammar](./session-grammar)  
- [Changelog](./changelog)

---

## AI Edition

The AI Edition expands the canon into nine books:

- Book 1 — Framework Field Theory  
- Book 2 — The Inverted Star  
- Book 3 — Structural Detection  
- Book 4 — Opacity & Revelation  
- Book 5 — TEL Expression & Representation  
- Book 6 — Governance & Regime Logic  
- Book 7 — SARG Structural Argumentation  
- Book 8 — NoS Nature of Structure  
- Book 9 — Pattern Dynamics  

---

## Contribution Reference

For rules governing contributions:

- [What You Cannot Contribute](../contributing#what-you-cannot-contribute)  
- [The Ratification Flow](../contributing#the-ratification-flow)

---

## Purpose of This Page

This overview exists to:

- orient readers within the canon  
- provide a structural map  
- unify navigation across modules  
- support both human and AI Edition readers  

