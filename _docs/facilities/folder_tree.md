# 📁 RTT Facilities — Folder Tree  
**Canonical Structure · Substrate‑Aligned**

This document defines the **authoritative folder structure** for the RTT Facilities domain.

It reflects the Facilities Playbook, the Facilities substrate specification, and all currently instantiated Facilities artifacts, including **RTT‑AGERI**.

---

```
docs/facilities/
│
├── README.md
├── spec.md
├── glossary.md
│
├── folder_tree.md
│
├── global-modernization-timeline.md
├── rtt-global-facilities-strategy-2050.md
├── timeline-visual-storyboard.md
│
├── modernization-cycle-matrix.md
├── intervention-playbook.md
├── propagation-model.md
├── harmonics-scoring-rubric.md
│
├── governance/
│   └── rtt-global-governance-constitution.md
│
├── design-system/
│   ├── component-creation-checklist.md
│   ├── component-naming-convention.md
│   ├── component-proposal-form.md
│   ├── design-governance-charter.md
│   ├── figma-library-structure.md
│   ├── governance-poster.md
│   ├── onboarding-guide.md
│   └── style-guide.md
│
├── city-facing/
│   ├── city-manager-briefing-packet.md
│   ├── city-manager-slide-deck.md
│   └── press-release-template.md
│
├── residents/
│   ├── neighborhood-meeting-deck.md
│   ├── storm-season-101.md
│   ├── storm-season-dos-and-donts.md
│   └── storm-season-faq.md
│
└── RTT-AGERI/
    ├── README.md
    ├── spec.md
    │
    ├── scoring/
    │   ├── drift-scoring-rubric.md
    │   ├── harmonics-scoring-rubric.md
    │   └── propagation-model.md
    │
    ├── standards/
    │   ├── corridor-classification-standard.md
    │   ├── modernization-cycle-matrix.md
    │   └── failure-mode-catalog.md
    │
    ├── governance/
    │   ├── GHQ-governance-charter-for-RTT-AGERI.md
    │   ├── audit-protocol.md
    │   └── escalation-pathways.md
    │
    ├── city-facing/
    │   ├── AGERI-implementation-guide.md
    │   ├── corridor-assessment-template.md
    │   └── modernization-rollout-checklist.md
    │
    ├── residents/
    │   ├── what-is-AGERI.md
    │   ├── safety-basics.md
    │   └── modernization-notice-template.md
    │
    ├── dashboards/
    │   ├── global-index-schema.md
    │   ├── corridor-dashboard-mockups.md
    │   └── data-ingestion-spec.md
    │
    └── glossary.md
```

---

## 🧭 Structural Notes

### **Facilities Root**
Contains **canonical, cross‑domain substrate artifacts**:
- lifecycle
- scoring
- propagation
- intervention
- modernization timing
- strategy
- glossary

These files are **referenced**, not duplicated, by domain extensions.

---

### **RTT‑AGERI/**
The first fully instantiated **Facilities domain extension**.

It:
- Inherits Facilities substrate definitions
- Extends scoring, standards, and governance
- Provides city‑ and resident‑facing materials
- Does not redefine shared Facilities concepts

Future Facilities domains will follow this same pattern.

---

## 🔒 Canonical Status

This folder tree is **canonical**.

Structural changes should be:
- Rare
- Intentional
- Coordinated with Facilities governance
