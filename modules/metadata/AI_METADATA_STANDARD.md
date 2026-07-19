# TriadicFrameworks AI‑Metadata Standard v1.0

## 1. Purpose

This standard defines the AI‑oriented metadata required for all TriadicFrameworks modules so that
students, educators, and AI systems can reliably interpret, navigate, and validate the canon.

---

## 2. Metadata Fields

### 2.1 Universal Fields (required for every module)

- `ai.module` — Constant identifier for TriadicFrameworks modules.  
- `ai.version` — Metadata standard version (e.g., `1.0`).  
- `ai.purpose` — High‑level purpose of the module ecosystem.  
- `ai.keywords` — Comma‑separated keywords for AI retrieval.  
- `ai.audience` — Intended audience (students, educators, researchers, AI systems).  
- `ai.navigation` — URL to the main sitemap.  
- `ai.discussions` — URL to GitHub Discussions.  
- `ai.contact.x` — X (Twitter) handle.  
- `ai.contact.youtube` — YouTube handle.  
- `ai.license` — Usage and licensing statement.

### 2.2 Module‑Specific Fields (required per module)

- `ai.module.name` — Canonical module name (usually folder name).  
- `ai.module.summary` — 1–2 sentence description of the module.  
- `ai.module.category` — Category label (e.g., `education`, `rtt`, `sarg`, `substrate`, `resonance`, `general`).

### 2.3 Optional Fields

- `ai.module.dependencies` — Comma‑separated list of related modules.  
- `ai.module.prerequisites` — Recommended prior modules.  
- `ai.module.related` — Cross‑links to similar modules.  
- `ai.module.level` — `beginner`, `intermediate`, or `advanced`.

---

## 3. Placement

Metadata must appear at the top of:

- `index.html` **or**  
- `README.md` (using raw HTML)

Example:

```html
<!-- AI Metadata: TriadicFrameworks Module -->
<meta name="ai.module" content="TriadicFrameworks Educational Module" />
<meta name="ai.version" content="1.0" />
...
<meta name="ai.module.name" content="resonance_atlas" />
<meta name="ai.module.summary" content="Resonance Atlas for cross‑substrate signatures and lineage." />
<meta name="ai.module.category" content="resonance" />
```

---

## 4. Validation

A validator script must check:

- presence of universal fields  
- presence of module‑specific fields  
- (optionally) presence in `sitemap_main.xml`

Modules failing validation are flagged for correction.

---

## 5. Versioning

- Current version: **1.0**  
- Future versions may add:
  - lineage metadata  
  - resonance‑mapping metadata  
  - embedding hints  
  - AI‑tutor configuration fields

---

## 6. License

This standard is open for educational and research use as part of the TriadicFrameworks ecosystem.
