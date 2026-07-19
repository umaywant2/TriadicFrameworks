# 🎨 RTT Facilities — Figma Library Structure  
**Canonical Organization & Design System Integrity**

This document defines the **canonical Figma library structure** for the RTT Facilities design system.

Its purpose is to ensure that:
- Components are discoverable and semantically grouped  
- Governance concepts are reflected in structure  
- Contributors cannot accidentally fragment meaning  
- The library scales without reorganization  

Structure is treated as a **governance artifact**, not a convenience.

---

## 1. Library Philosophy

The Figma library is organized to reflect **Facilities meaning**, not UI patterns.

- Folders encode **domain and governance concepts**
- Components are grouped by **what they represent**, not how they look
- Naming and structure reinforce each other
- No component exists without a clear semantic home

---

## 2. Top‑Level Figma Files

Each major domain has its own canonical library file.

```
RTT Facilities — Core Library
RTT Facilities — Dashboards
RTT Facilities — City‑Facing
RTT Facilities — Domain Extensions (AGERI, etc.)
```

Cross‑domain reuse flows **from Core outward**, never inward.

---

## 3. Core Library File Structure

**RTT Facilities — Core Library**

```
📁 00 — Foundations
📁 01 — Systems
📁 02 — Corridors
📁 03 — Scores
📁 04 — Capital
📁 05 — Audit
📁 06 — Status
📁 07 — Navigation
📁 08 — Layout
📁 09 — Controls
📁 99 — Deprecated
```

Folder numbers are fixed and must not be reordered.

---

## 4. Foundations (00)

```
📁 00 — Foundations
  ├─ Color Tokens
  ├─ Typography
  ├─ Spacing & Grid
  ├─ Iconography
  ├─ Motion Guidelines
```

Foundations are **never duplicated** in other files.

---

## 5. Systems (01)

```
📁 01 — Systems
  ├─ SystemBadge
  ├─ DependencyIndicator
  ├─ SystemStatusFlag
```

Represents infrastructure systems (Electrical, Water, etc.).

---

## 6. Corridors (02)

```
📁 02 — Corridors
  ├─ CorridorBoundary
  ├─ CorridorClassBadge
  ├─ CorridorRiskIndicator
```

Corridor components are **first‑class governance artifacts**.

---

## 7. Scores (03)

```
📁 03 — Scores
  ├─ DriftTrend
  ├─ HarmonicsIndicator
  ├─ PropagationRiskBadge
```

Score components map directly to the Global Index Schema.

---

## 8. Capital (04)

```
📁 04 — Capital
  ├─ ModernizationCycleBadge
  ├─ CapitalPriorityIndicator
  ├─ DeferredRiskFlag
```

Capital components must support **decision explainability**.

---

## 9. Audit (05)

```
📁 05 — Audit
  ├─ AuditStatusFlag
  ├─ ReviewTriggerIndicator
  ├─ FollowUpRequiredBadge
```

Audit components make accountability visible.

---

## 10. Status (06)

```
📁 06 — Status
  ├─ OperationalStateIndicator
  ├─ InterventionActiveFlag
  ├─ PublicVisibilityBadge
```

Status components reflect **current governance state**, not alerts.

---

## 11. Navigation (07)

```
📁 07 — Navigation
  ├─ GlobalNav
  ├─ CorridorSelector
  ├─ SystemFilter
```

Navigation components are semantic, not decorative.

---

## 12. Layout (08)

```
📁 08 — Layout
  ├─ DashboardFrame
  ├─ PanelContainer
  ├─ SectionHeader
```

Layout components provide structure without meaning leakage.

---

## 13. Controls (09)

```
📁 09 — Controls
  ├─ Toggle
  ├─ Dropdown
  ├─ Button
```

Controls are generic and never encode Facilities meaning.

---

## 14. Deprecated (99)

```
📁 99 — Deprecated
```

Deprecated components:
- Are clearly marked
- Are not reused
- Remain for reference only

Deletion requires steward approval.

---

## 15. Domain Extension Libraries

Domain extensions (e.g., **RTT‑AGERI**) follow the same structure:

```
RTT Facilities — AGERI
  ├─ 00 — Foundations (references Core)
  ├─ 01 — Systems
  ├─ 02 — Exposure
  ├─ 03 — Climate Stress
```

Extensions **add meaning without redefining it**.

---

## 16. Enforcement Rules

- Components must live in exactly one folder  
- Folder hopping is prohibited  
- New folders require steward approval  
- Structure changes are governance events  

---

## 17. Canonical Status

This Figma library structure is **canonical**.

All RTT Facilities design work must conform to it.
