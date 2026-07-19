# Schema Full UI design spec

# 1. product overview

**name:** triadicframeworks schema browser  
**purpose:** interactive explorer for the schema universe—helping creators, devs, and researchers:

- discover schemas by domain
- understand structure, fields, and dependencies
- navigate cross‑domain relationships
- launch validation and tooling flows

**primary data source:** `docs/schemas/schema-manifest.json` + schema files on disk/GitHub.

---

# 2. target users & core use cases

### 2.1 personas

- **creator / canon steward**
  - wants to see how new ideas fit into existing domains
  - checks lineage, domains, and structural gaps

- **developer / integrator**
  - needs to find the right schema quickly
  - wants field definitions, dependencies, and file paths
  - may copy paths into code or tooling

- **researcher / operator**
  - wants to understand what’s modeled (e.g., quantum, ATC, lab)
  - uses browser as documentation for RTT‑Inside systems

### 2.2 core use cases

1. **browse by domain**
   - expand “quantum”, see all quantum schemas, click one, inspect details.

2. **inspect a schema**
   - see description, fields, dependencies, used‑by, and file path.

3. **follow dependencies**
   - from `coeus_contract` → jump to `state_model`, `operator`, `resonance_constraints`.

4. **search**
   - type “drift” → see `ai_drift_vector`, `PlayerDriftProfile`, etc.

5. **launch tools**
   - click “Validate Universe” → run CLI or show status.
   - click “View JSON” → open raw schema.

---

# 3. information architecture

### 3.1 top‑level structure

- **global header**
  - app title, universe name, manifest version, quick actions.

- **left sidebar**
  - domain tree (from `domains` in manifest).
  - search box (filters schemas by name).

- **main content**
  - schema detail view (when a schema is selected).
  - empty state / welcome panel (when nothing selected).

### 3.2 navigation model

- **primary navigation:** domain → schema
- **secondary navigation:** dependency links inside schema detail
- **search navigation:** search → filtered list → schema

---

# 4. layout spec

### 4.1 global layout

- **header (top, full width)**
  - left: `TriadicFrameworks Schema Browser`
  - center: `Universe: Resonance‑Time`
  - right: `Manifest v1.0.0` + buttons:
    - `Validate Universe`
    - `View Manifest`
    - `Generate Graph`

- **body: two‑column**
  - left: fixed‑width sidebar (280–320px)
  - right: flexible main panel

### 4.2 sidebar

**elements:**

- **search input**
  - placeholder: `search schemas…`
  - filters schema list in real time.

- **domain list**
  - each domain:
    - icon (simple glyph per domain)
    - label (e.g., `quantum`, `finance`, `rtt-atc`)
    - expand/collapse arrow
  - expanded domain shows schemas as a flat list:
    - `quantum_state`
    - `quantum_substrate`
    - `quantum_energy_bank`

**behaviors:**

- clicking a schema:
  - highlights it in sidebar
  - loads its details in main panel.

---

# 5. schema detail view

### 5.1 header section

- **schema title:** humanized from filename (e.g., `Quantum State`)
- **domain:** badge (e.g., `quantum`)
- **file path:** `docs/schemas/quantum/quantum_state.schema.json`
- **actions:**
  - `View JSON` (opens raw file in new tab or modal)
  - `Copy Path` (copies repo path)
  - `Open in GitHub` (link to GitHub URL)

### 5.2 description block

- **description:** from manifest domain description + optional per‑schema metadata (future).
- **status (optional future):** `stable`, `experimental`, `draft`.

### 5.3 fields panel

- table layout:

| field name | type   | description (optional) |
|-----------|--------|------------------------|
| state_id  | string |                        |
| basis     | string |                        |
| amplitudes| object |                        |

- types inferred from schema `properties`.

### 5.4 dependencies panel

- **“Depends on” list**
  - e.g., `dimensional_layer`, `resonance_profile`
  - each item is a clickable chip → navigates to that schema.

- **“Used by” list**
  - reverse dependencies (computed from manifest or precomputed index).
  - each item clickable.

### 5.5 triadic context (optional but on‑brand)

- small panel showing if schema includes triadic fields:
  - `spin`, `charge`, `temperature` presence.
- simple indicator:
  - `Triadic Alignment: Full / Partial / None`

---

# 6. interactions & flows

### 6.1 search flow

1. user types `drift` in search.
2. sidebar filters to:
   - `ai_drift_vector`
   - `PlayerDriftProfile`
   - `GDDriftVector`
3. user clicks `ai_drift_vector` → detail view updates.

### 6.2 dependency navigation

1. user views `coeus_contract`.
2. in “Depends on”:
   - sees `state_model`, `operator`, `resonance_constraints`.
3. clicks `state_model` → sidebar auto‑expands `coeus` domain and selects `state_model`.

### 6.3 validate universe

- clicking `Validate Universe`:
  - either:
    - calls backend endpoint that wraps `rtt-schema validate`, or
    - shows instructions: `run: rtt-schema validate` in your terminal.
  - optional: show last validation result + timestamp.

---

# 7. visual style

### 7.1 theme

- **dark mode first**, aligned with triadicframeworks.org:
  - background: deep navy/space (`#050816` style)
  - text: light gray (`#e5e7eb`)
  - accents: triadic gradient or cyan/magenta highlights.

### 7.2 components

- **badges:** pill‑shaped, colored by domain (e.g., quantum = purple, finance = green).
- **chips:** for dependencies and used‑by.
- **monospace:** for file paths and field names.

---

# 8. technical notes

### 8.1 data loading

- load `schema-manifest.json` on app init.
- derive:
  - domain list
  - schema list per domain
  - reverse dependency map (schema → used‑by).

### 8.2 schema parsing

- when a schema is selected:
  - fetch JSON from `docs/schemas/<domain>/<file>`.
  - parse `properties` for fields.
  - optionally cache results.

### 8.3 routing (optional)

- URL pattern:
  - `/schemas/:domain/:schema`
- deep links:
  - shareable URLs for specific schema views.

---

# 9. deliverables you can drop into repo

you could add a design doc like:

- `docs/schemas/SCHEMA_BROWSER_SPEC.md`

containing:

- product overview
- IA
- layout
- interactions
- technical notes

