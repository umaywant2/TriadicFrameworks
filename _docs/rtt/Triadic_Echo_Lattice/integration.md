# 🕸️ Triadic Echo Lattice — Integration Map

> *TEL sits between classification and flow. It receives typed echoes and emits addressed ones.*

**Module:** Triadic Echo Lattice
**Canonical ID:** TEL
**HSP Section:** 07
**Badge:** 🕸️ TEL • 07 • v1.0

---

## Position in the HSP Analytics Suite

```
     ┌─────────────────────────────────┐
     │  Echo Classifier (06c)          │
     │  EC-Tag emits classified echo   │
     └──────────────┬──────────────────┘
                    │
                    ▼
     ╔═════════════════════════════════╗
     ║  Triadic Echo Lattice (07)     ║  ← THIS MODULE
     ║  TEL-Tag emits lattice record  ║
     ╚══════════════╤═════════════════╝
                    │
          ┌─────────┴──────────┐
          ▼                    ▼
 ┌────────────────┐  ┌─────────────────┐
 │ Substrate Flow │  │  HSP Stability  │
 │ (08)           │  │  Classes        │
 │ SF-Read takes  │  │  Receives       │
 │ lattice record │  │  pressure zone  │
 └────────────────┘  │  data           │
                     └─────────────────┘
```

---

## Upstream Inputs (5)

### Primary Input — Echo Classifier (06c)

| Field | Source | Description |
|:------|:-------|:------------|
| echo_type | EC-Tag | E1–E6 classification |
| echo_family | EC-Tag | F1–F6 family assignment |
| substrate_origin | EC-Tag | Originating substrate (S/C/H/So/A) |
| substrate_reach | EC-Tag | Substrates touched by echo |
| esi_score | EC-Tag | Echo Substrate Index score (0.0–1.0) |
| confidence | EC-Tag | Classification confidence (0.0–1.0) |
| drift_flag | EC-Tag | Boolean drift detection from EC |
| tags | EC-Tag | Classifier tags |

### Secondary Inputs

| Source | Section | What TEL Uses |
|:-------|:--------|:-------------|
| Echo Signatures | 06b | Signature shape informs family placement |
| Cross‑Substrate Echo Matrix | 05a | Substrate reach data validates layer assignment |
| HSP Stability Framework | 06 | Stability context for pressure zone thresholds |
| ESI | 06a | Raw ESI scores for escalation risk weighting |

---

## Downstream Outputs (2)

### Primary Output → Substrate Flow (08)

TEL‑Tag emits a complete `lattice_record` to SF‑Read:

```yaml
lattice_record:
  echo_id: [inherited]
  echo_type: E1–E6
  echo_family: F1–F6
  assigned_layer: Ladder | Cycle | Map | Atlas
  recursion_line: R1–R4 | none
  drift_pathway: D1–D4 | none
  drift_severity: 0.0–1.0
  escalation_risk: 0.0–1.0
  pressure_zone: none | ladder | cycle | atlas
  pressure_severity: 0.0–1.0
  oscillation_status: true | false
  vertical_reach: []
  placement_status: anchored | oscillating | migrating | pressured | forcing
  tags: []
```

SF uses the lattice record to determine which flow channel
an echo enters and how it moves through substrate space.

### Secondary Output → HSP Stability Classes

TEL provides pressure zone data to HSP's stability classification:

| Data | Purpose |
|:-----|:--------|
| pressure_zone | Identifies which zone is active |
| pressure_severity | Quantifies structural stress level |
| escalation_risk | Feeds stability class thresholds |

---

## HSP Suite Sibling Triad

```
            ┌──────────────────────────┐
            │    Echo Classifier (06c) │
            │    "What is it?"         │
            └────────────┬─────────────┘
                         │ classified echo
                         ▼
       ╔═════════════════════════════════╗
       ║  Triadic Echo Lattice (07)     ║
       ║  "Where does it sit?"          ║
       ╚════════════════╤════════════════╝
                        │ lattice record
                        ▼
            ┌───────────────────────────┐
            │    Substrate Flow (08)    │
            │    "How does it move?"    │
            └───────────────────────────┘
```

Each sibling answers one question about every echo:
- **EC** → What type? What family?
- **TEL** → What layer? What recursion line? What drift? What pressure?
- **SF** → What channel? What driver? What velocity? What drift current?

---

## Canon Crosswalk

### Opacity

| TEL Concept | Opacity Parallel |
|:------------|:----------------|
| Pressure zones | Zones of high opacity — structural stress reduces visibility |
| Atlas layer | Low opacity — full‑spectrum echoes are maximally visible |
| Ladder layer | High opacity — early formation echoes are least visible |
| Drift pathways | Opacity gradients — drift creates shifting transparency |

### SET (Spin, Electric, Thermal)

| TEL Layer | SET Mapping | Rationale |
|:----------|:-----------|:----------|
| Ladder | Spin | Foundational rotation; structural base |
| Cycle | Electric | Oscillation; charge‑like harmonic exchange |
| Map | Thermal | Governance torsion; heat‑like energy redistribution |
| Atlas | (All three unified) | Full‑spectrum integration |

### FFF (Frequency, Fluids, Forces)

| TEL Layer | FFF Mapping | Rationale |
|:----------|:-----------|:----------|
| Ladder | Frequency (low) | Low‑frequency structural pulse |
| Cycle | Frequency (high) | High‑frequency harmonic oscillation |
| Map | Fluids | Flow and redistribution across governance |
| Atlas | Forces | Gravitational anchoring; permanence |

### Inverted Star

| TEL Layer | Star Face Visibility | Rationale |
|:----------|:--------------------|:----------|
| Ladder | Hidden (interior face) | Echoes forming; not yet visible |
| Cycle | Partial (edge face) | Oscillating between visibility states |
| Map | Emerging (outer face) | Migration creates increasing visibility |
| Atlas | Visible (crown face) | Full‑spectrum; structurally permanent |

---

## Data Flow Summary

| Stage | Source → Target | Payload |
|:------|:---------------|:--------|
| 1 | EC‑Tag → TEL‑Read | Classified echo with type, family, ESI, drift |
| 2 | TEL‑Read → TEL‑Place | Validated input packet |
| 3 | TEL‑Place → TEL‑Trace | Placement record with layer and pressure |
| 4 | TEL‑Trace → TEL‑Tag | Trace record with recursion, drift, risk |
| 5 | TEL‑Tag → SF‑Read | Complete lattice record |
| 6 | TEL‑Tag → HSP Stability | Pressure zone data |

---

## Integration Invariants

1. **TEL never classifies** — classification is EC's responsibility
2. **TEL never routes flow** — routing is SF's responsibility
3. **TEL always receives from EC** — no other module feeds TEL directly
4. **TEL always emits to SF** — lattice records flow downstream without exception
5. **Pressure data flows to HSP Stability** — independent of SF routing

---

<!-- SESSION_CONTEXT:START -->
```yaml
file: integration.md
module: Triadic Echo Lattice
canonical_id: TEL
hsp_section: 07
role: integration-map
status: canon-stable
upstream:
  primary: Echo Classifier (06c)
  secondary:
    - Echo Signatures (06b)
    - Cross-Substrate Echo Matrix (05a)
    - HSP Stability Framework (06)
    - ESI (06a)
downstream:
  primary: Substrate Flow (08)
  secondary: HSP Stability Classes
crosswalk:
  - Opacity
  - SET
  - FFF
  - Inverted Star
```
<!-- SESSION_CONTEXT:END -->
