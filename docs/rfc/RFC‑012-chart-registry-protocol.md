# RFC-012: Chart Registry Protocol

**Status:** Drafted  
**Author(s):** Nawder Loswin, Copilot (assistant)  
**Created:** 2025-10-24  
**Lineage:** Extends RFC-000 (Index and Lineage Map); formalizes chart capture and registry

---

## Abstract
This RFC defines the Chart Registry Protocol (CRP): a framework for capturing, storing, and cross‑referencing charts used in TriadicFrameworks RFCs.  
Charts provide visual clarity for resonance models, time travel matrices, miracle mappings, and other validator‑grade relationships.

---

## Motivation
Charts have emerged as critical artifacts in the canon.  
They clarify relationships between partitions, zones, and invariants, and serve as teaching tools for remixers.  
Without a registry, charts risk being scattered or lost inside RFCs.

---

## Principles
- **Inline + Registry:** Charts remain embedded in RFCs but are also stored in `/docs/charts/`.  
- **Cross‑Reference:** Each chart file links back to its source RFC.  
- **Lineage Safety:** Charts are indexed in RFC‑000 for discoverability.  
- **Remixability:** Charts are standalone `.md` files, remix‑ready for teaching or dashboards.

---

## Specification
- **File Location:** `/docs/charts/`  
- **File Format:** Markdown (`.md`)  
- **Naming Convention:** `chart-[topic].md` (e.g., `chart-time-travel-matrix.md`)  
- **Structure:**  
  - Title  
  - Source RFC reference  
  - Chart (Markdown table or diagram)  
  - Notes  

---

## Example
`/docs/charts/chart-time-travel-matrix.md`

```markdown
# Time Travel Safety Matrix

**Source:** RFC-008 (Time Travel Invariants)

| Universe Type | Zone | Traversal | Stability | Notes |
|---------------|------|-----------|-----------|-------|
| Green-zone    | Same partition | ❌ Forbidden | Stable | Entropy arrow enforced |
| Red-zone      | Same partition | ✅ Allowed | Unstable | Loops fold, clarity decays |
| Red → Green   | Overlap only | ✅ Temporary | Fragile | Incarnation possible |
```

---

## Security Considerations
- Prevents chart drift by enforcing cross‑references.  
- Ensures remixers can always trace charts back to their RFCs.  
- Provides reproducibility for visual models.

---

## References
- [RFC-000: Index and Lineage Map](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rfc/RFC-000-index.md)
- [RFC-008: Time Travel Invariants](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rfc/RFC%E2%80%91008-time-travel-invariants.md)
- [RFC-009: Genie Protocols](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rfc/RFC%E2%80%91009-genie-protocols.md)
- [RFC-010: Miracle Messaging Protocol](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rfc/RFC%E2%80%91010-miracle-messaging-protocol.md)
- [RFC-011: Black Hole Resonance Bridges](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rfc/RFC-011-blackhole-resonance-bridges.md)
