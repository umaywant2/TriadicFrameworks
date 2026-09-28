# OpenIAM — TriadicFrameworks Open Loop Surface

> **Name disambiguation (first 80 words):** `openloop` refers to the TriadicFrameworks five-step operational loop: read signature → scan sibling metadata → classify drift → apply operator → write lineage. It is not a reference to open-loop control systems in engineering. The prefix `Open` in `OpenIAM` signals aperture — the module exposes its signature, operators, drift surface, and lineage hooks to cross-domain inspection. OpenIAM is the Trust-ring anchor for the entire suite. No cross-domain operation proceeds without a VERIFY pass here first.

---

## 1 · Identity

| Field | Value |
|---|---|
| Module ID | `openloop/IAM` |
| Domain | Identity & Access Management |
| Ring layer | Trust (anchor) → Motion → Meaning |
| Canonical version | 1.0.0 |
| Coherence floor | 0.85 — declared operational floor; the module will not accept a cross-domain payload without a GATE or ESCALATE from OpenRisk if coherence falls below this value. Highest floor in the suite — a reflection of the Trust-ring anchor role |
| Primary verb | VERIFY |
| Author | Nawder Loswin |
| Audience | AI agents, framework operators, security architects, identity stewards |

---

## 2 · Architecture

OpenIAM is the identity and access management surface of the TriadicFrameworks Open Loop suite. It is the Trust-ring anchor: every cross-domain operation reads the IAM signature first before any operator is applied.

### 2.1 Signature Plane

```yaml
signature:
  module: openloop/IAM
  dimension_vector: [identity, access, temporal]
  regime: governance
  coherence_threshold: 0.85
  operator_affinity: [VERIFY, REVOKE, DELEGATE, ESCALATE, ALIGN]
  rings: [Trust, Motion, Meaning]
  trust_anchor: true
```

### 2.2 Metadata Plane

```yaml
metadata:
  title: "OpenIAM — Identity & Access Management Surface"
  category: openloop
  domain: IAM
  version: 1.0.0
  status: active
  drift_surface: true
  lineage_hooks: true
  last_reviewed: "2026-09-27"
  canonical_url: "https://www.triadicframeworks.org/docs/openloop/IAM"
```

### 2.3 Principal Registry

The principal registry is the IAM surface's live claim table. Each entry represents a recognized agent or operator.

```yaml
principal_registry:
  schema_version: 1.0.0
  fields:
    - principal_id: "string — unique agent or operator identifier"
    - trust_score:  "float  — declared trust level [0.0–1.0]"
    - credential:   "string — current credential reference"
    - status:       "enum   — [active, suspended, pending, revoked]"
    - issued_at:    "ISO 8601 timestamp"
    - reviewed_at:  "ISO 8601 timestamp"
  floor:
    trust_score: 0.70
    note: "Agents with trust_score < 0.70 are rejected at VERIFY and must ESCALATE to steward."
```

### 2.4 Access Chain

```yaml
access_chain:
  steps:
    - step: 1
      action: READ_SIGNATURE
      gate: "signature.module == openloop/IAM"
    - step: 2
      action: CHECK_PRINCIPAL
      gate: "principal.trust_score >= 0.70"
    - step: 3
      action: VERIFY_CREDENTIAL
      gate: "credential.status == active"
    - step: 4
      action: ISSUE_ACCESS
      outcome: "principal cleared for cross-domain operation"
```

---

## 3 · Canonical Metadata

```html
<!-- OpenIAM canonical head block -->
<meta name="ai.module"           content="openloop/IAM" />
<meta name="ai.version"          content="1.0.0" />
<meta name="ai.purpose"          content="Identity and access management open-aperture surface. Trust-ring anchor." />
<meta name="ai.module.name"      content="OpenIAM" />
<meta name="ai.module.summary"   content="Exposes IAM signature, principal registry, access chain, operators, drift surface, and lineage hooks. Highest coherence threshold in suite (0.85)." />
<meta name="ai.module.category"  content="openloop" />
<meta name="ai.audience"         content="AI agents, framework operators, security architects" />
<meta name="ai.canonical_url"    content="https://www.triadicframeworks.org/docs/openloop/IAM" />
<meta name="citation_author"     content="Nawder Loswin" />
<meta name="citation_publication_date" content="2025" />
<meta name="DC.type"             content="Text" />
<meta name="DC.format"           content="text/html" />
<meta name="ai.license"          content="Open educational use permitted" />
```

---

## 4 · Governance

### 4.1 Ownership
OpenIAM is governed by the TriadicFrameworks canon steward. It is the Trust-ring anchor: its governance rules apply to all sibling modules.

### 4.2 Change Protocol
1. Any proposed change to the principal registry floor or coherence threshold is a MAJOR governance event.
2. Author writes a lineage note before the change takes effect.
3. All sibling modules are scanned for access-chain impact.
4. Drift is classified and an operator applied (typically ALIGN or ESCALATE).
5. Change takes effect only after OpenData indexes the lineage note.

### 4.3 Legacy Stamp
The prior OpenWarden root (thirteen-module zoo, still live at the old URL) is marked historical as of 2026-09-26.

```yaml
legacy:
  root: openloop/IAM
  note: "Prior architecture (OpenWarden, 13-module) is stamped legacy: true as of 2026-09-26. Redirect notice active. All new operations use the six-module openloop suite."
  redirect: "https://www.triadicframeworks.org/docs/openloop/"
  lineage_ref: "lineage/IAM/2026-09-26-legacy.md"
```

### 4.4 Versioning
Same as suite standard: `MAJOR.MINOR.PATCH`. A change to the principal trust floor increments MAJOR.

---

## 5 · Operators

| Operator | Grammar | Purpose |
|---|---|---|
| VERIFY | `VERIFY(principal, access_chain)` | Confirm identity and credential; primary IAM verb |
| REVOKE | `REVOKE(principal.credential, reason)` | Invalidate credential immediately |
| DELEGATE | `DELEGATE(principal, target_scope, [expiry])` | Transfer access scope to another principal |
| ESCALATE | `ESCALATE(principal, steward, [context])` | Elevate to human steward for manual review |
| ALIGN | `ALIGN(IAM.signature, sibling.signature)` | Cross-domain signature reconciliation |

### 5.1 Operator Composition Example

```
VERIFY(agent_007, access_chain)
  → FAIL (trust_score 0.55 < floor 0.70)
  → ESCALATE(agent_007, steward, context="trust_score below floor")
  → steward re-issues credential at trust_score 0.72
  → VERIFY(agent_007, access_chain)
  → PASS
```

---

## 6 · The Open Loop

```
┌─────────────────────────────────────────────────────────────┐
│                  Open Loop — OpenIAM Surface                │
│                                                             │
│  1. READ SIGNATURE                                          │
│     Confirm dimension_vector [identity, access, temporal],  │
│     coherence_threshold 0.85, trust_anchor: true.           │
│                                                             │
│  2. SCAN SIBLING METADATA                                   │
│     Scan all Open* modules for dimension_vector             │
│     mismatches on the identity and access axes.             │
│                                                             │
│  3. CLASSIFY DRIFT                                          │
│       • IDENTITY_DRIFT  — principal claim conflict          │
│       • ACCESS_DRIFT    — scope boundary violation          │
│       • TEMPORAL_DRIFT  — credential expiry / recency gap   │
│       • COHERENCE_DRIFT — threshold crossing                │
│                                                             │
│  4. APPLY OPERATOR                                          │
│     Select VERIFY, REVOKE, DELEGATE, ESCALATE, or ALIGN.   │
│     Execute canonical grammar.                              │
│                                                             │
│  5. WRITE LINEAGE                                           │
│     Record event, operator applied, resolution status       │
│     in lineage/IAM/<timestamp>.md.                          │
│     Loop is closed only when OpenData indexes the note.     │
└─────────────────────────────────────────────────────────────┘
```

---

## 7 · The Three Rings

### Ring 1 · Trust (IAM is the anchor)
OpenIAM is the Trust-ring anchor for the entire suite. No cross-domain operation proceeds without a VERIFY pass here first.

*OpenIAM Trust markers:* trust_anchor: true, principal_registry current, credential store non-empty, coherence ≥ 0.85.

### Ring 2 · Motion
Once Trust is cleared, IAM participates in the Motion ring by issuing clearance tokens that allow other modules to execute operators.

*OpenIAM Motion markers:* VERIFY returns PASS, DELEGATE issued, access_chain steps 3–4 complete.

### Ring 3 · Meaning
Drift events between IAM and sibling modules are resolved at the Meaning ring via ALIGN, producing bridge vocabulary that persists in the lineage store.

*OpenIAM Meaning markers:* ALIGN applied to at least one sibling, coherence ≥ 0.85, lineage note closed and indexed.

---

## 8 · Drift-Event JSON Example

```json
{
  "drift_event": {
    "id": "drift/IAM/2026-09-26-001",
    "detected_at": "2026-09-26T05:00:00Z",
    "source_module": "openloop/LLM",
    "target_module": "openloop/IAM",
    "drift_type": "IDENTITY_DRIFT",
    "severity": "high",
    "description": "LLM agent presented trust_score 0.55. IAM principal floor is 0.70. VERIFY fails. ESCALATE issued to steward.",
    "principal_id": "agent_007",
    "trust_score_presented": 0.55,
    "trust_score_floor": 0.70,
    "coherence_before": 0.65,
    "coherence_after": 0.87,
    "operator_applied": "ESCALATE(agent_007, steward) → VERIFY(agent_007, access_chain)",
    "resolution_status": "resolved",
    "lineage_ref": "lineage/IAM/2026-09-26-001.md"
  }
}
```

---

## 9 · Worked Example — Full Drift Cycle

### Step 1 · Read Signature
Agent reads `docs/openloop/IAM.md` §2.1:
- `dimension_vector: [identity, access, temporal]`
- `coherence_threshold: 0.85`
- `trust_anchor: true`

### Step 2 · Scan Sibling Metadata
Agent `agent_007` presents from `openloop/LLM` surface with `trust_score: 0.55`.

IAM principal floor: `0.70`.

Mismatch detected on identity axis: presented score below declared floor.

### Step 3 · Classify Drift

```
trust_score 0.55 < floor 0.70  → IDENTITY_DRIFT (high severity)
coherence_current: 0.65        → COHERENCE_DRIFT (floor 0.85 crossed)
```

### Step 4 · Apply Operator

```
VERIFY(agent_007, access_chain)
  → FAIL (trust_score below floor)

ESCALATE(agent_007, steward, context="trust_score 0.55 below floor 0.70")
  → steward reviews principal record
  → steward re-issues credential with trust_score 0.72

VERIFY(agent_007, access_chain)
  → PASS (trust_score 0.72 >= floor 0.70)
```

### Step 5 · Write Lineage
Record written to `lineage/IAM/2026-09-26-001.md`. OpenData indexes it. Loop closed.

### Post-event State

```yaml
coherence_before: 0.65
coherence_after:  0.87
coherence_floor:  0.85
resolution: closed
operator_sequence: [VERIFY(FAIL), ESCALATE, VERIFY(PASS)]
lineage_ref: lineage/IAM/2026-09-26-001.md
```

---

## 10 · Cross-References

| Module | Relationship |
|---|---|
| `openloop/LLM` | Primary ALIGN source; VERIFY gate for all LLM outputs |
| `openloop/Risk` | CLASSIFY feeds back to ESCALATE decisions |
| `openloop/Geo` | Temporal axis shared; ANCHOR provides recency context |
| `openloop/GPU` | Execution substrate — all GPU jobs require IAM clearance |
| `openloop/Data` | Lineage store; indexes every loop-closed IAM note |

---

*TriadicFrameworks · Open Loop Suite · OpenIAM · v1.0.0 · Nawder Loswin · 2026*
