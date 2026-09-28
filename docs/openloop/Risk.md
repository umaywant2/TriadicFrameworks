# OpenRisk — TriadicFrameworks Open Loop Surface

> **Name disambiguation (first 80 words):** `openloop` refers to the TriadicFrameworks five-step operational loop: read signature → scan sibling metadata → classify drift → apply operator → write lineage. It is not a reference to open-loop control systems in engineering. The prefix `Open` in `OpenRisk` signals aperture — the module exposes its signature, operators, drift surface, and lineage hooks to cross-domain inspection. OpenRisk is the classification layer that gates all cross-domain operations when coherence falls below any module's declared floor.

---

## 1 · Identity

| Field | Value |
|---|---|
| Module ID | `openloop/Risk` |
| Domain | Risk Regime Classification |
| Ring layer | Trust → Meaning → Motion |
| Canonical version | 1.0.0 |
| Coherence floor | 0.80 — declared operational floor; the module will not accept a cross-domain payload without a GATE or ESCALATE from OpenRisk itself if coherence falls below this value |
| Primary verb | CLASSIFY |
| Author | Nawder Loswin |
| Audience | AI agents, framework operators, risk stewards, integration architects |

---

## 2 · Architecture

OpenRisk is the risk classification surface. It sits in the pipeline after OpenIAM (Trust cleared) and before OpenGeo/OpenLLM (Motion begins). Its job is to CLASSIFY the risk envelope of any cross-domain operation and issue a GATE decision.

### 2.1 Signature Plane

```yaml
signature:
  module: openloop/Risk
  dimension_vector: [regime, severity, temporal]
  regime: classification
  coherence_threshold: 0.80
  operator_affinity: [CLASSIFY, GATE, ESCALATE, ABSORB, PROPAGATE]
  rings: [Trust, Meaning, Motion]
```

### 2.2 Metadata Plane

```yaml
metadata:
  title: "OpenRisk — Risk Regime Classification Surface"
  category: openloop
  domain: Risk
  version: 1.0.0
  status: active
  drift_surface: true
  lineage_hooks: true
  last_reviewed: "2026-09-27"
  canonical_url: "https://www.triadicframeworks.org/docs/openloop/Risk"
```

### 2.3 Risk Tier Definitions

| Tier | Label | Severity Range | Gate Action |
|---|---|---|---|
| T0 | Low | coherence ≥ 0.90 | PASS — no gate |
| T1 | Moderate | 0.80 ≤ coherence < 0.90 | ANNOTATE and proceed |
| T2 | High | 0.70 ≤ coherence < 0.80 | GATE — operator required |
| T3 | Critical | coherence < 0.70 | ESCALATE — steward required |

### 2.4 Severity Formula

```
severity_score = 1.0 - coherence_current
gate_tier      = T0 if severity_score < 0.10
               = T1 if 0.10 ≤ severity_score < 0.20
               = T2 if 0.20 ≤ severity_score < 0.30
               = T3 if severity_score ≥ 0.30
```

---

## 3 · Canonical Metadata

```html
<!-- OpenRisk canonical head block -->
<meta name="ai.module"           content="openloop/Risk" />
<meta name="ai.version"          content="1.0.0" />
<meta name="ai.purpose"          content="Risk regime classification open-aperture surface" />
<meta name="ai.module.name"      content="OpenRisk" />
<meta name="ai.module.summary"   content="Classifies risk tier and severity for all cross-domain operations. Issues GATE or ESCALATE decisions before Motion operators execute." />
<meta name="ai.module.category"  content="openloop" />
<meta name="ai.audience"         content="AI agents, framework operators, risk stewards" />
<meta name="ai.canonical_url"    content="https://www.triadicframeworks.org/docs/openloop/Risk" />
<meta name="citation_author"     content="Nawder Loswin" />
<meta name="citation_publication_date" content="2025" />
<meta name="DC.type"             content="Text" />
<meta name="DC.format"           content="text/html" />
<meta name="ai.license"          content="Open educational use permitted" />
```

---

## 4 · Governance

### 4.1 Ownership
OpenRisk is governed by the TriadicFrameworks canon steward. Risk tier thresholds are declared floors, not empirically measured values. Changes to tier boundaries require a MAJOR version increment and a lineage note.

### 4.2 Change Protocol
1. Author proposes threshold change in a lineage note.
2. All sibling modules are re-evaluated against the new tier boundaries.
3. Any module whose coherence falls into a new gate tier receives a GATE event.
4. OpenData indexes the lineage note. Change takes effect.

### 4.3 Versioning
`MAJOR.MINOR.PATCH`. A change to any tier boundary is MAJOR.

---

## 5 · Operators

| Operator | Grammar | Purpose |
|---|---|---|
| CLASSIFY | `CLASSIFY(operation, risk_tier)` | Assign a T0–T3 risk tier to a cross-domain operation |
| GATE | `GATE(operation, tier, [required_operator])` | Block operation until required operator is applied |
| ESCALATE | `ESCALATE(operation, steward, [context])` | Elevate T3 events to human steward |
| ABSORB | `ABSORB(drift_event, risk_envelope)` | Contain a bounded drift event within the current tier |
| PROPAGATE | `PROPAGATE(risk_classification, sibling_modules)` | Broadcast tier assignment to downstream surfaces |

---

## 6 · The Open Loop

```
┌─────────────────────────────────────────────────────────────┐
│                 Open Loop — OpenRisk Surface                │
│                                                             │
│  1. READ SIGNATURE                                          │
│     Confirm dimension_vector [regime, severity, temporal],  │
│     coherence_threshold 0.80.                               │
│                                                             │
│  2. SCAN SIBLING METADATA                                   │
│     Read coherence_current from all sibling modules.        │
│     Compute severity_score for each.                        │
│                                                             │
│  3. CLASSIFY DRIFT                                          │
│       • REGIME_DRIFT    — regime mismatch cross-domain      │
│       • SEVERITY_DRIFT  — tier boundary crossed             │
│       • TEMPORAL_DRIFT  — classification stale              │
│                                                             │
│  4. APPLY OPERATOR                                          │
│     CLASSIFY → GATE (if T2) → ESCALATE (if T3)             │
│     ABSORB (if T1 and bounded) → PROPAGATE                  │
│                                                             │
│  5. WRITE LINEAGE                                           │
│     Record tier assignment, gate decision, and resolution   │
│     in lineage/Risk/<timestamp>.md.                         │
│     Loop closed only when OpenData indexes the note.        │
└─────────────────────────────────────────────────────────────┘
```

---

## 7 · The Three Rings

### Ring 1 · Trust
OpenRisk sits in the Trust ring as the classification gate. It validates that a cross-domain operation has an acceptable risk envelope before Motion begins.

*OpenRisk Trust markers:* coherence ≥ 0.80, tier assigned, GATE decision issued or waived.

### Ring 2 · Meaning
Risk classification produces a Meaning artifact: the tier label and severity score that sibling modules use to interpret their own drift events.

*OpenRisk Meaning markers:* PROPAGATE applied, sibling modules have current tier assignments.

### Ring 3 · Motion
OpenRisk enters the Motion ring only to propagate classifications — not to execute. Motion operators GATE and PROPAGATE carry risk context downstream.

*OpenRisk Motion markers:* PROPAGATE dispatched, lineage note written and indexed.

---

## 8 · Drift-Event JSON Example

```json
{
  "drift_event": {
    "id": "drift/Risk/2026-09-26-001",
    "detected_at": "2026-09-26T05:45:00Z",
    "source_module": "openloop/LLM",
    "target_module": "openloop/Risk",
    "drift_type": "REGIME_DRIFT",
    "severity": "high",
    "description": "LLM regime (generative) produced output with coherence 0.71, crossing Risk T2 gate threshold. CLASSIFY assigned T2. GATE issued.",
    "coherence_before": 0.82,
    "coherence_after": 0.71,
    "risk_tier": "T2",
    "severity_score": 0.29,
    "operator_applied": "CLASSIFY(LLM.output, T2) → GATE(LLM.output, T2, ALIGN)",
    "resolution_status": "gated — awaiting ALIGN operator",
    "lineage_ref": "lineage/Risk/2026-09-26-001.md"
  }
}
```

---

## 9 · Cross-References

| Module | Relationship |
|---|---|
| `openloop/IAM` | Receives VERIFY PASS before CLASSIFY runs; ESCALATE routes to IAM steward |
| `openloop/LLM` | Primary classification target; generative outputs most frequently reach T1–T2 |
| `openloop/Geo` | Temporal axis shared; ANCHOR provides recency context for severity scoring |
| `openloop/GPU` | Execution jobs gated at T2–T3 until risk cleared |
| `openloop/Data` | Lineage store; indexes every CLASSIFY and GATE event |

---

*TriadicFrameworks · Open Loop Suite · OpenRisk · v1.0.0 · Nawder Loswin · 2026*
