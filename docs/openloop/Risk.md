# OpenRisk — TriadicFrameworks OpenAPI Surface

Name disambiguation: `openapi` in this canon does not refer to the OpenAPI Specification (OAS/Swagger) REST-schema standard. It refers to the TriadicFrameworks **open-aperture principle**: a domain module that exposes its signature, operators, drift surface, and lineage hooks to cross-domain inspection. Every `Open*` module is an openapi-compliant surface in the canon sense.

---

## 1 · Identity

| Field | Value |
|---|---|
| Module ID | `openapi/Risk` |
| Domain | Risk Regime Classification |
| Ring layer | Trust → Meaning → Motion |
| Canonical version | 1.0.0 |
| Author | Nawder Loswin |
| Audience | AI agents, framework operators, risk architects, governance stewards |

---

## 2 · Architecture

OpenRisk is the risk-classification surface of the TriadicFrameworks OpenAPI suite. It reads the severity of any detected drift event, assigns it to a risk tier, and either gates further execution or propagates a risk envelope to sibling modules. Because risk classification gates Trust-ring operations, OpenRisk runs immediately after OpenIAM verifies the initiating principal.

### 2.1 Signature Plane

```yaml
signature:
  module_id: openapi/Risk
  version: 1.0.0
  dimension_vector: [regime, severity, temporal]
  coherence_threshold: 0.80
  regime: classification
  ring_primary: Trust
  operator_affinity: [CLASSIFY, GATE, ESCALATE, ABSORB, PROPAGATE]
  drift_surface: true
  lineage_hooks: true
  canonical_url: https://triadicframeworks.com/docs/openapi/Risk
```

### 2.2 Metadata Plane

```yaml
metadata:
  title: "OpenRisk — Risk Regime Classification Surface"
  version: 1.0.0
  risk_tiers: [low, moderate, high, critical]
  risk_gate_threshold: 0.75
  severity_formula: "severity = (drift_magnitude * weight_regime) + (temporal_decay * weight_time)"
  coherence_current: 0.80
  last_drift_event: null
  lineage_store: lineage/Risk/
```

### 2.3 Operator Plane

OpenRisk operators execute in severity-descending order. A GATE blocks all downstream operators until a human or governance-tier agent resolves the condition. CLASSIFY must always precede GATE or ESCALATE in any operator chain.

---

## 3 · Canonical Metadata

```html
<meta name="ai.module"          content="openapi/Risk" />
<meta name="ai.version"         content="1.0.0" />
<meta name="ai.domain"          content="Risk Regime Classification" />
<meta name="ai.ring"            content="Trust" />
<meta name="ai.regime"          content="classification" />
<meta name="ai.coherence"       content="0.80" />
<meta name="ai.operators"       content="CLASSIFY,GATE,ESCALATE,ABSORB,PROPAGATE" />
<meta name="ai.dimension_vector" content="regime,severity,temporal" />
<meta name="ai.risk_tiers"      content="low,moderate,high,critical" />
<meta name="ai.risk_gate_threshold" content="0.75" />
<meta name="ai.drift_surface"   content="true" />
<meta name="ai.lineage_hooks"   content="true" />
<meta name="ai.suite"           content="openapi" />
<meta name="ai.canonical_url"   content="https://triadicframeworks.com/docs/openapi/Risk" />
<meta name="ai.disambiguation"  content="openapi = TriadicFrameworks open-aperture principle. NOT OAS/Swagger." />
<meta name="citation_author"    content="Nawder Loswin" />
<meta name="citation_title"     content="OpenRisk — TriadicFrameworks OpenAPI Surface" />
<meta name="citation_date"      content="2025" />
```

---

## 4 · Governance

### 4.1 Ownership

OpenRisk is the classification authority for the OpenAPI suite. No operator across any sibling module may produce an output whose severity exceeds `high` without first receiving a GATE or ESCALATE resolution from OpenRisk.

### 4.2 Risk Tier Definitions

| Tier | Severity Range | Gate Required | Auto-Escalate |
|---|---|---|---|
| `low` | 0.00 - 0.25 | No | No |
| `moderate` | 0.26 - 0.50 | No | No |
| `high` | 0.51 - 0.75 | Yes | No |
| `critical` | 0.76 - 1.00 | Yes | Yes -> OpenIAM |

### 4.3 Severity Formula

```
severity = (drift_magnitude x weight_regime) + (temporal_decay x weight_time)
```

Default weights: `weight_regime = 0.65`, `weight_time = 0.35`. Weights may be overridden per-module via the module's `risk_weight_override` signature field.

### 4.4 Gate Protocol

A GATE is a hard stop. When GATE fires:
1. The current operator chain is suspended.
2. A drift event is opened in `lineage/Risk/<timestamp>.md`.
3. Sibling modules are notified via PROPAGATE (risk envelope only - no data payload).
4. Resolution requires either: (a) a human governance actor closes the event, or (b) OpenIAM issues a DELEGATE to a governance-tier principal who then closes it.
5. Once resolved, GATE lifts and the suspended chain resumes from the point of interruption.

### 4.5 Change Protocol

1. Author proposes change to tier boundaries or severity formula in a lineage note (`lineage/Risk/<timestamp>.md`).
2. All sibling Open* modules are scanned for affected risk references.
3. Drift is classified using the openapi loop (section 6).
4. CLASSIFY is applied; if severity >= `high`, ESCALATE fires to OpenIAM.
5. The lineage note is closed with resolution status.

### 4.6 Versioning

Versions follow `MAJOR.MINOR.PATCH`. A change to tier boundaries increments MAJOR. A change to severity formula weights increments MINOR. A documentation correction increments PATCH.

---

## 5 · Operators

| Operator | Grammar | Purpose |
|---|---|---|
| CLASSIFY | `CLASSIFY(Risk.event, severity_formula)` | Assign a drift event to a risk tier |
| GATE | `GATE(Risk.tier, operator_chain)` | Suspend operator chain pending resolution |
| ESCALATE | `ESCALATE(Risk.tier, openapi/IAM)` | Forward critical event to IAM governance |
| ABSORB | `ABSORB(Risk.event, lineage_ref)` | Accept and close a resolved low/moderate event |
| PROPAGATE | `PROPAGATE(Risk.envelope, sibling_modules)` | Broadcast risk envelope to all sibling surfaces |

### 5.1 Operator Priority

```
GATE > ESCALATE > CLASSIFY > PROPAGATE > ABSORB
```

GATE is the highest-priority operator in this module. When GATE and any other operator target the same event, GATE resolves first.

### 5.2 Operator Composition

```
CLASSIFY(Risk.event, severity_formula)
  -> if tier == critical: ESCALATE(Risk.tier, openapi/IAM)
  -> if tier == high:     GATE(Risk.tier, operator_chain)
  -> if tier <= moderate: ABSORB(Risk.event, lineage_ref)
                           -> PROPAGATE(Risk.envelope, sibling_modules)
```

---

## 6  The OpenAPI Loop

OpenRisk's instantiation of the five-step read->scan->classify->apply->write cycle:

```
+----------------------------------------------------------+
|              OpenRisk -- OpenAPI Loop                    |
|                                                          |
|  Step 1  READ SIGNATURE                                |
|    Read docs/openapi/Risk.md section 2.1                |
|    Confirm: dimension_vector, coherence_threshold,       |
|    risk_tiers, risk_gate_threshold, severity_formula     |
|                         |                               |
|                         v                               |
|  Step 2  SCAN SIBLING METADATA                         |
|    Scan all Open* .md files for risk_weight_override     |
|    and any open drift events with severity fields        |
|                         |                               |
|                         v                               |
|  Step 3  CLASSIFY DRIFT                                |
|    Apply severity_formula to each detected event         |
|    Map result to risk tier (low/moderate/high/critical)  |
|                         |                               |
|                         v                               |
|  Step 4  APPLY OPERATOR                                |
|    tier == critical -> ESCALATE -> OpenIAM               |
|    tier == high     -> GATE                              |
|    tier >= moderate -> ABSORB -> PROPAGATE               |
|                         |                               |
|                         v                               |
|  Step 5  WRITE LINEAGE NOTE                            |
|    lineage/Risk/>timestamp>.md                          |
|    Fields: event_id, tier, severity, operator_applied,   |
|    resolved_by, resolution_timestamp                     |
+----------------------------------------------------------+
```

---

## 7  The Three Rings

### Ring 1  Trust

OpenRisk is a Trust-ring gating module. Its primary function is to prevent operators from executing when risk conditions exceed safe thresholds. No cross-domain operation may proceed past the Trust ring if OpenRisk has issued an unresolved GATE.

**OpenRisk Trust markers:** CLASSIFY has run on the current event, no unresolved GATE in effect, coherence_threshold: 0.80.

### Ring 2  Meaning

Meaning is engaged when classification produces a risk tier that is semantically actionable  i.e., the operator chain can look at the tier and make a clear next-step decision without ambiguity. A `moderate` classification with a clear ABSORB resolution is a Meaning-ring completion.

**OpenRisk Meaning markers:** risk tier assigned, severity score computed, operator_applied confirmed, lineage note open with event record.

### Ring 3  Motion

Motion activates when a resolved event propagates its envelope outward  PROPAGATE firing across sibling surfaces, risk envelope received by OpenLLM, OpenGeo, OpenGPU, OpenData.

**OpenRisk Motion markers:** PROPAGATE in flight, sibling modules receiving risk envelope, lineage note updated with propagation receipt timestamps.

---

## 8  Drift-Event JSON Example

```json
{
  "event_id": "risk-evt-2026-09-26-001",
  "module": "openapi/Risk",
  "timestamp": "2026-09-26T06:30:00-04:00",
  "drift_type": "severity_threshold_breach",
  "detected_by": "openapi_loop.step3",
  "source_module": "openapi/LLM",
  "severity_input": {
    "drift_magnitude": 0.82,
    "weight_regime": 0.65,
    "temporal_decay": 0.44,
    "weight_time": 0.35
  },
  "severity_computed": 0.688,
  "risk_tier": "high",
  "gate_required": true,
  "operator_applied": "GATE",
  "gate_status": "open",
  "escalated_to": null,
  "lineage_ref": "lineage/Risk/2026-09-26-001.md",
  "resolution": {
    "status": "pending",
    "resolved_by": null,
    "resolution_timestamp": null
  },
  "propagation": {
    "envelope_broadcast": false,
    "sibling_modules_notified": []
  }
}
```

---

## 9  Worked Example -- Full Risk Drift Cycle

### Scenario

OpenLLM generates an output with an anomalous semantic collapse. The collapse is flagged as a potential `regime` drift. OpenRisk receives the event and must classify, gate, and resolve.

### Step 1  Read Signature

Agent reads `docs/openapi/Risk.md` section 2.1 and confirms:
- `dimension_vector: [regime, severity, temporal]`
- - `coherence_threshold: 0.80`
  - - `risk_gate_threshold: 0.75`
    - - `se
