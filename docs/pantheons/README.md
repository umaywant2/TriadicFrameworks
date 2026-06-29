# Triadic Pantheon Canon

> **Canon Layer:** Structural Cosmology  
> **Scope:** Cross-tradition pantheon alignment  
> **Status:** Active Scaffold — v0.1.0  
> **Maintainer:** Nawder / Triadic Pantheon Canon Project

---

## Overview

The **Triadic Pantheon Canon (TPC)** is a comparative mythological framework that maps the divine figures and cosmological structures of distinct world pantheons onto a shared three-layer architecture. Rather than collapsing traditions into a single synthetic mythology, the TPC preserves each tradition's internal logic while surfacing structural homologies across them.

The canon operates on the premise that sovereign mythological systems independently articulate three irreducible ontological operators — **Genesis**, **Continuance**, and **Dissolution** — and that divine personas, cosmological hierarchies, and ritual mechanics can be read as expressions of these operators at varying scales and resolutions.

---

## Triadic Architecture

Every pantheon module within this canon is organized around three canonical layers:

| Layer | Operator | Function | Sanskrit Cognate | Greek Cognate |
|-------|----------|----------|------------------|---------------|
| **Layer I** | Genesis | Origination; the emergence of form from undifferentiated potential | *Srishti* | *Arkhē* |
| **Layer II** | Continuance | Sustaining order; the preservation of relational coherence across time | *Sthiti* | *Kosmos* |
| **Layer III** | Dissolution | Transformative undoing; return to potential; the liminal threshold | *Samhara* | *Khaos* / *Lethe* |

These layers are **not sequential phases** but co-present aspects of any cosmological moment. A deity, myth, or ritual event may embody a single operator dominantly while participating in the others implicitly.

---

## Canonical Operators

Each pantheon entry defines its triadic operators — the specific divine figures, forces, or principles that carry the Layer I–III functions within that tradition. Operators are tagged with:

- **Primary Operator (`op:primary`)** — the deity or force most fully expressing the layer's function
- **Secondary Operator (`op:secondary`)** — a deity whose role partially or contextually overlaps the layer
- **Liminal Operator (`op:liminal`)** — figures that traverse or mediate between layers (psychopomps, tricksters, threshold deities)

---

## Repository Structure

```
docs/
└── pantheons/
    ├── README.md                  ← This file (Canon overview)
    ├── OPERATORS.md               ← Operator tag definitions and usage guide
    ├── METADATA_SCHEMA.md         ← Canonical metadata schema for all modules
    │
    ├── greek/
    │   ├── README.md              ← Greek Triadic Profile
    │   └── capture.md             ← Greek deity capture file
    │
    └── hindu/
        ├── README.md              ← Hindu Triadic Profile (forthcoming)
        └── capture.md             ← Hindu deity capture file
```

---

## Pantheon Index

| Pantheon | Status | Primary Tradition | Layer I Op. | Layer II Op. | Layer III Op. |
|----------|--------|-------------------|-------------|--------------|---------------|
| [Greek](./greek/README.md) | ✅ Active | Hellenic Polytheism | Chaos / Eros | Zeus | Hades / Dionysus |
| Hindu | 🔄 In Progress | Vedic / Puranic | Brahma | Vishnu | Shiva |
| Norse | 🕐 Planned | Norse Polytheism | Ymir / Odin | Thor | Loki / Ragnarök |
| Egyptian | 🕐 Planned | Kemetic Religion | Atum | Ra / Ma'at | Osiris / Set |
| Mesopotamian | 🕐 Planned | Sumerian-Akkadian | Apsu / Tiamat | Enlil | Ereshkigal |

---

## Alignment Principles

The TPC adheres to the following interpretive principles:

1. **Emic Priority** — Each tradition is first understood on its own terms before cross-mapping is applied.
2. **Structural Homology, Not Synthesis** — Mapping reveals resonances; it does not create a super-tradition or flatten differences.
3. **Layered Operator Fluidity** — Deities may shift dominant operator across mythological epochs, texts, or ritual contexts. Assignments are contextual, not fixed.
4. **Metadata Integrity** — All canon entries carry versioned metadata to track interpretive decisions and sourcing lineage.
5. **Liminal Fidelity** — Threshold figures (tricksters, psychopomps, shapeshifters) are given their own operator tag and are never forcibly assigned to a single layer.

---

## Metadata Schema

All pantheon README modules conform to the following front-matter schema:

```yaml
canon: Triadic Pantheon Canon
module: <pantheon-name>
version: <semver>
layer_i_operator: <deity or force>
layer_ii_operator: <deity or force>
layer_iii_operator: <deity or force>
liminal_operators:
  - <deity>
primary_sources:
  - <text or tradition>
cross_references:
  - <related pantheon module>
status: draft | active | archived
last_updated: <ISO 8601 date>
```

---

## Contributing

When adding a new pantheon module:

1. Create a folder under `docs/pantheons/<tradition-name>/`
2. Add a `capture.md` with raw deity profiles and sourcing notes
3. Draft `README.md` using the Greek module as the canonical template
4. Register the pantheon in the **Pantheon Index** above
5. Ensure all metadata fields are populated before marking status `active`

---

*Triadic Pantheon Canon — structured for depth, built for alignment.*
