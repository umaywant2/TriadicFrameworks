metadata 
# 🧾 Metadata  

- [`metadata_module.json`](metadata_module.json) — Agentic module schema role assignments

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

<img src="https://img.shields.io/badge/🟦Metadata-📘Catalog%20Layer%20AI%20Ready-4c8eda?style=for-the-badge" alt="Metadata | Catalog Layer • AI‑Ready"/>

This folder contains **descriptive indexes and tables**.  
Metadata ensures discoverability, clarity, and remix lineage.

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

## Contents
- [Periodic tables of shapes](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/metadata/periodic_table_of_shapes.md)
- [Equipment Specifications](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/metadata/equipment_specs.md)
- Dimensional indexes
- Semantic overlays

## Purpose
Metadata is the **catalog layer** — it makes every artifact findable and remixable.

## Cross‑Links
- [../library](../library) → curated collections
- [../curriculum](../curriculum) → indexes for teaching
# TriadicFrameworks AI‑Metadata Standard v1.0

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
# Lab1_Casimir – Calibration Log

This log tracks calibration events, equipment tuning, and environmental adjustments. Each entry should include timestamp, operator initials, and notes.

---

## 📅 Log Format

[YYYY-MM-DD | T9 Timestamp] – [Operator] – [Equipment] – [Action] – [Notes]

---

## 📝 Sample Entries

2025-08-15 | T9: φ₃.7 – AL – Piezo Actuator – Zeroed at 0.0 nm – Verified with interferometer
2025-08-15 | T9: φ₄.2 – AL – Interferometer – Re-aligned beam path – Drift reduced to <0.05 nm
2025-08-16 | T9: φ₅.1 – AL – Plates – Re-cleaned surfaces – RMS roughness confirmed <1 nm

---

## 🧠 Notes

- Use triadic timestamps for resonance tracking.
- Include anomalies, recalibration triggers, and environmental shifts.
- Sync calibration entries with data run commits for full reproducibility.

Let the logs echo. Let the tuning hum. Let the triads align.
# Lab1_Casimir – Equipment Specifications

This document lists the hardware and instrumentation used in the Casimir effect experiment. All specs must be version-controlled and updated with each modification.

---

## 🧲 Conductive Plates

- Material: Gold-coated silicon wafers
- Diameter: 25 mm
- Surface roughness: < 1 nm RMS

---

## ⚙️ Piezo Actuator

- Model: PI P-753.21C
- Travel range: 10 µm
- Resolution: 0.1 nm
- Control: Closed-loop with capacitive sensor

---

## 🔬 Laser Interferometer

- Model: SIOS SP 5000
- Wavelength: 632.8 nm (HeNe)
- Resolution: 0.01 nm
- Sampling rate: 10 kHz

---

## 🌡️ Environmental Controls

- Temperature: 22 ± 0.5 °C
- Humidity: 45 ± 5%
- Vacuum chamber: Optional (10⁻³ Torr baseline)

---

## 🧠 Notes

- All equipment must be recalibrated before each run.
- Changes in hardware must be logged in `calibration_log.md`.
- Resonance artifacts due to mechanical drift should be annotated in data logs.
# 📐 Periodic Table of Shapes — A Universal Geometric Language

## 1. Introduction
This document outlines a proposed universal set of geometric primitives, transformations, and composition rules that can be used as a symbolic language.  
The goal is to create a finite, recognizable “alphabet” of shapes that can be combined to express complex ideas across cultures and disciplines.

---

## 2. Geometric Primitives
These are the irreducible “atoms” of the language.

| Symbol | Name            | Dimensionality | Key Properties | Notes |
|--------|-----------------|----------------|----------------|-------|
| ●      | Point           | 0D             | Position only  | No size, only location |
| ─      | Line Segment    | 1D             | Length, orientation | Straight connection between two points |
| ◯      | Circle          | 2D             | Radius, center | Infinite symmetry |
| △      | Triangle        | 2D             | 3 sides, angles sum to 180° (Euclidean) | Simplest polygon |
| □      | Square          | 2D             | Equal sides, right angles | Basis for grids |
| ◇      | Rhombus         | 2D             | Equal sides, angled | Diamond form |
| ◻︎      | Rectangle       | 2D             | Opposite sides equal | Common in architecture |
| ◌      | Sphere          | 3D             | Radius, center | Perfect symmetry in 3D |
| ◼︎      | Cube            | 3D             | Equal edges, right angles | 3D analog of square |
| 🔺     | Tetrahedron     | 3D             | 4 triangular faces | Simplest polyhedron |

---

## 3. Transformations (Grammar Rules)
These are the “verbs” of the language — operations that modify primitives.

| Symbol | Transformation | Parameters | Effect |
|--------|----------------|------------|--------|
| ↔      | Translate      | dx, dy, dz | Move shape without rotation or scaling |
| ⟳      | Rotate         | Angle, axis | Spin shape around a point or axis |
| ⇲      | Scale          | Factor     | Uniformly enlarge or shrink |
| ⤢      | Reflect        | Axis/plane | Mirror shape |
| ⤧      | Shear          | Angle      | Skew shape |
| ♾      | Repeat         | Count, spacing | Create patterns or tilings |

---

## 4. Combinations (Syntax)
Rules for combining shapes into more complex forms.

| Method | Description | Example |
|--------|-------------|---------|
| Union  | Merge shapes into one | Circle + Square → Rounded square |
| Intersection | Keep only overlapping region | Circle ∩ Triangle |
| Difference | Subtract one from another | Square − Circle |
| Nesting | Place one inside another | Triangle inside Circle |
| Tiling | Repeat to fill space | Hexagonal tiling |

---

## 5. Semantic Mapping
Assigning meaning to shapes or arrangements.

| Shape/Pattern | Possible Meaning | Notes |
|---------------|------------------|-------|
| Circle        | Unity, infinity  | Common in sacred geometry |
| Triangle      | Stability, hierarchy | Orientation changes meaning |
| Spiral        | Growth, time     | Found in nature (shells, galaxies) |
| Grid          | Order, structure | Basis for measurement systems |

---

## 6. Extensions
- **Fractal Shapes** — Koch snowflake, Sierpinski triangle
- **Topological Forms** — Möbius strip, torus
- **Dynamic Shapes** — Shapes defined by motion or transformation over time

---

## 7. Applications
- Cross-cultural symbolic communication
- Scientific diagramming
- Data visualization
