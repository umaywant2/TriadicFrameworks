# 🌍 **OpenGeo — canonical_metadata.md**  
**OpenWarden Suite — Geospatial Metadata Substrate**  
**Analyzer Layer:** dimensional  
**Regime:** open‑geo‑governance  
**Version:** 1.0  

---

## **1. Canonical Metadata Overview**

OpenGeo defines the **canonical metadata schema** for all geospatial objects across the OpenWarden suite.  
This metadata ensures:

- dimensional clarity  
- coordinate correctness  
- locality stability  
- coherence declaration  
- drift‑bounded geospatial behavior  
- lineage transparency  
- operator grammar compliance  

Every geospatial object must include the fields defined in this document.

---

## **2. Canonical Metadata Fields**

### **2.1 Dimensional & Locality Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.geo.dimension` | Dimensional category | `region:north-america` |
| `open.geo.locality` | Locality descriptor | `locality:midwest` |
| `open.geo.region` | Semantic region (optional) | `semantic:great-lakes` |

These fields define the dimensional identity and contextual locality.

---

### **2.2 Coordinate Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.geo.coordinates` | Canonical coordinate block | `lat:42.204;lon:-83.485` |
| `open.geo.boundary` | Boundary descriptor (optional) | `boundary:wayne-county` |

Coordinates must be canonical, bounded, and reversible.

---

### **2.3 Coherence & Drift Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.geo.coherence` | Coherence score (0–1) | `0.94` |
| `open.geo.drift` | Drift status | `bounded` |

These fields determine stability and drift behavior.

---

### **2.4 Lineage Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.geo.lineage` | Lineage ID | `geolineage:3f7a` |
| `open.geo.parent` | Parent lineage (optional) | `geolineage:3f79` |

Lineage ensures transparency and prevents geospatial manipulation.

---

### **2.5 Operator Grammar Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.geo.operator.extend` | Operator availability | `true` |
| `open.geo.operator.condense` | Operator availability | `true` |
| `open.geo.operator.refactor` | Operator availability | `true` |
| `open.geo.operator.capture` | Operator availability | `true` |
| `open.geo.operator.annotate` | Operator availability | `true` |
| `open.geo.operator.correct` | Operator availability | `true` |

Operators ensure safe, reversible geospatial evolution.

---

### **2.6 Module Identity Fields**

| Field | Description | Example |
|-------|-------------|---------|
| `open.geo.version` | Module version | `1.0` |
| `open.geo.module` | Module name | `OpenGeo` |
| `open.geo.signature` | Dimensional signature | `opengeo-substrate` |

These fields anchor the object to the OpenGeo substrate.

---

## **3. Canonical Metadata Block (Full Example)**

```html
<meta name="open.geo.dimension" content="region:north-america">
<meta name="open.geo.locality" content="locality:midwest">
<meta name="open.geo.region" content="semantic:great-lakes">

<meta name="open.geo.coordinates" content="lat:42.204;lon:-83.485">
<meta name="open.geo.boundary" content="boundary:wayne-county">

<meta name="open.geo.coherence" content="0.94">
<meta name="open.geo.drift" content="bounded">

<meta name="open.geo.lineage" content="geolineage:3f7a">
<meta name="open.geo.parent" content="geolineage:3f79">

<meta name="open.geo.operator.extend" content="true">
<meta name="open.geo.operator.condense" content="true">
<meta name="open.geo.operator.refactor" content="true">
<meta name="open.geo.operator.capture" content="true">
<meta name="open.geo.operator.annotate" content="true">
<meta name="open.geo.operator.correct" content="true">

<meta name="open.geo.version" content="1.0">
<meta name="open.geo.module" content="OpenGeo">
<meta name="open.geo.signature" content="opengeo-substrate">
```

---

## **4. Metadata Validation Rules**

OpenGeo enforces:

- **dimensional correctness**  
- **coordinate stability**  
- **locality coherence**  
- **lineage integrity**  
- **operator grammar compliance**  
- **drift‑bounded updates**  

Metadata violations trigger:

- drift flag  
- suppression  
- correction  
- lineage update  

---

## **5. Cross‑Module Metadata Alignment**

OpenGeo metadata aligns with:

- **OpenSEO** — semantic region metadata  
- **OpenSoN** — social locality overlays  
- **OpenStream** — geospatial recommendation coherence  
- **OpenCatalog** — location‑based product metadata  
- **OpenAdEngine** — contextual geospatial ad metadata  
- **OpenRisk** — anomaly detection  
- **OpenIAM** — identity‑safe geospatial rules  

All alignment is drift‑bounded and coherence‑declared.

---

## **6. Required Metadata Presence**

Every geospatial object must include:

- dimensional fields  
- coordinate fields  
- locality fields  
- coherence & drift fields  
- lineage fields  
- operator grammar fields  
- module identity fields  

Missing fields are treated as dimensional drift.
