# OpenIAM — TriadicFrameworks OpenAPI Surface

> **Name disambiguation:** `openapi` in this canon does not refer to the OpenAPI Specification (OAS/Swagger) REST-schema standard. It refers to the TriadicFrameworks *open-aperture principle*: a domain module that exposes its signature, operators, drift surface, and lineage hooks to cross-domain inspection. Every `Open*` module is an openapi-compliant surface in the canon sense.

---

## 1 · Identity

| Field | Value |
|---|---|
| Module ID | `openapi/IAM` |
| Domain | Identity & Access Management |
| Ring layer | Trust → Motion → Meaning |
| Canonical version | 1.0.0 |
| Author | Nawder Loswin |
| Audience | AI agents, framework operators, security architects |

---

## 2 · Architecture

OpenIAM is the identity-and-access surface of the TriadicFrameworks OpenAPI suite. It governs principal identity, access-chain resolution, and privilege regime classification across all cross-domain operations. Because identity is the innermost concern of the Trust ring, OpenIAM is the first module any agent must reconcile before executing operators across sibling surfaces.

### 2.1 Signature Plane

```yaml
signature:
  module: openapi/IAM
  dimension_vector: [identity, access, temporal]
  regime: governance
  coherence_threshold: 0.85
  operator_affinity: [VERIFY, REVOKE, DELEGATE, ESCALATE, ALIGN]
  rings: [Trust, Motion, Meaning]
```

### 2.2 Metadata Plane

```yaml
metadata:
  title: "OpenIAM — Identity & Access Surface"
  category: openapi
  domain: IAM
  version: 1.0.0
  status: active
  drift_surface: true
  lineage_hooks: true
  last_reviewed: "2026-09-26"
  principal_types: [user, agent, operator, module, service]
  access_chain_depth: 4
```

### 2.3 Operator Plane

IAM operators are the highest-priority operators in the suite. When an IAM operator and a non-IAM operator target the same node, the IAM operator resolves first.

---

## 3 · Canonical Metadata

```html
<!-- OpenIAM canonical head block -->
<meta name="ai.module"           content="openapi/IAM" />
<meta name="ai.version"          content="1.0.0" />
<meta name="ai.purpose"          content="Identity and access management open-aperture surface" />
<meta name="ai.module.name"      content="OpenIAM" />
<meta name="ai.module.summary"   content="Governs principal identity, access-chain resolution, and privilege regime classification across cross-domain operations." />
<meta name="ai.module.category"  content="openapi" />
<meta name="ai.audience"         content="AI agents, security architects, framework operators" />
<meta name="ai.navigation"       content="sitemap_main.xml" />
<meta name="citation_author"     content="Nawder Loswin" />
<meta name="citation_publication_date" content="2025" />
<meta name="DC.type"             content="Text" />
<meta name="DC.format"           content="text/html" />
<meta name="ai.license"          content="Open educational use permitted" />
```

---

## 4 · Governance

### 4.1 Ownership

OpenIAM is the governance anchor of the OpenAPI suite. All changes to principal definitions or access-chain depth require a lineage note and a cross-suite drift scan.

### 4.2 Principal Registry

| Principal Type | Trust Score Floor | Scope Vector |
|---|---|---|
| user | 0.60 | [read, write, delegate] |
| agent | 0.70 | [read, execute, annotate] |
| operator | 0.80 | [read, write, execute, delegate] |
| module | 0.90 | [read, execute, propagate] |
| service | 0.75 | [read, write, execute] |

### 4.3 Access Chain Protocol

```
access_chain:
  depth: 4
  links:
    - {principal: user,     permission: initiate}
    - {principal: agent,    permission: execute}
    - {principal: operator, permission: apply}
    - {principal: module,   permission: record}
```

### 4.4 Change Protocol

1. Author proposes change in a lineage note (`lineage/IAM/<timestamp>.md`).
2. All sibling Open* modules are scanned for affected principal references.
3. Drift is classified using the openapi loop (section 6).
4. VERIFY or ESCALATE is applied as appropriate.
5. The lineage note is closed with resolution status.

### 4.5 Versioning

Versions follow `MAJOR.MINOR.PATCH`. A change to a principal trust score floor increments MINOR. A change to the access chain depth or structure increments MAJOR.

---

## 5 · Operators

| Operator | Grammar | Purpose |
|---|---|---|
| VERIFY | `VERIFY(IAM.principal, trust_score)` | Confirm principal meets trust floor |
| REVOKE | `REVOKE(IAM.principal, access_chain)` | Remove principal from active access chain |
| DELEGATE | `DELEGATE(IAM.principal, target_principal)` | Transfer authority to another principal |
| ESCALATE | `ESCALATE(IAM.access_chain, governance_tier)` | Elevate chain to higher governance tier |
| ALIGN | `ALIGN(IAM.signature, sibling.signature)` | Reconcile identity dimension with sibling module |

### 5.1 Operator Priority

```
1. VERIFY   — must pass before any other operator executes
2. REVOKE   — halts execution chain immediately
3. ESCALATE — suspends and forwards to governance tier
4. DELEGATE — transfers; delegated principal inherits position
5. ALIGN    — reconciles after identity is confirmed
```

### 5.2 Operator Composition

```
VERIFY(IAM.principal, trust_score: 0.80)
  -> DELEGATE(IAM.principal, agent)
  -> ANNOTATE(result, lineage/IAM/2026-09-26-001.md)
```

---

## 6 · The OpenAPI Loop

```
1. READ SIGNATURE
   Confirm dimension_vector: [identity, access, temporal]
   Confirm coherence_threshold: 0.85

2. SCAN SIBLING METADATA
   Check all Open* modules for principal_type declarations or
   access_chain references differing from this module's registry.

3. CLASSIFY DRIFT
   IDENTITY_DRIFT   -- principal definition mismatch
   ACCESS_DRIFT     -- chain depth or permission gap
   TEMPORAL_DRIFT   -- principal last-verified timestamp stale
   COHERENCE_DRIFT  -- trust score below floor

4. APPLY OPERATOR
   Select VERIFY, REVOKE, DELEGATE, ESCALATE, or ALIGN.

5. WRITE LINEAGE
   Record in lineage/IAM/<timestamp>.md and INDEX via OpenData.
```

---

## 7 · The Three Rings

### Ring 1 · Trust

OpenIAM is the canonical anchor of the Trust ring. All other Open* modules inherit their Trust-ring status from IAM reconciliation. No cross-domain operation may begin until VERIFY has cleared the initiating principal.

*OpenIAM Trust markers:* VERIFY operator current, principal registry non-empty, access chain depth >= 2, coherence_threshold: 0.85.

### Ring 2 · Motion

Motion activates when an IAM operator executes across a cross-domain boundary — a DELEGATE in flight, an ESCALATE forwarded to a governance tier, or an ALIGN reconciling with a sibling.

*OpenIAM Motion markers:* active access_chain, DELEGATE or ESCALATE in flight, lineage note open.

### Ring 3 · Meaning

Meaning is achieved when all principals carry aligned trust scores, the access chain is closed, and the lineage note is indexed.

*OpenIAM Meaning markers:* coherence_current >= 0.85, lineage note closed, no open drift events.

---

## 8  Drift-Event JSON Example

```json
{
  "drift_event": {
    "id": "drift/IAM/2026-09-26-001",
    "detected_at": "2026-09-26T05:30:00Z",
    "source_module": "openapi/IAM",
    "target_module": "openapi/LLM",
    "drift_type": "IDENTITY_DRIFT",
    "severity": "high",
    "description": "LLM surface declared agent with trust_score 0.55, below IAM floor of 0.70. Access chain broken at link 2.",
    "principal_type": "agent",
    "trust_score_declared": 0.55,
    "trust_score_floor": 0.70,
    "access_chain_link_broken": 2,
    "coherence_delta": -0.20,
    "coherence_before": 0.85,
    "coherence_after": 0.65,
    "threshold_crossed": true,
    "operator_applied": "VERIFY(IAM.principal, trust_score: 0.70)",
    "resolution_status": "resolved",
    "lineage_ref": "lineage/IAM/2026-09-26-001.md"
  }
}
```

---

## 9  Worked Example  Full IAM Drift Cycle

### Scenario

An LLM agent attempts to apply `PROPAGATE` across the suite. OpenIAM detects the agent trust score (0.55) is below the IAM floor for `agent` principals (0.70). Access chain broken at link 2.

### Step 1  Read Signature

Agent reads `docs/openapi/IAM.md` section 2.1 and confirms:
- `dimension_vector: [identity, access, temporal]`
- - `coherence_threshold: 0.85`
  - - `operator_affinity: [VERIFY, REVOKE, DELEGATE, ESCALATE, ALIGN]`
    - - `principal trust floor for agent: 0.70`
     
      - ### Step 2  Scan Sibling Metadata
     
      - Agent scans `docs/openapi/LLM.md` and finds `trust_score: 0.55` for principal_type `agent`.
      - Mismatch: `0.55 > floor 0.70`. Access chain link 2 (`agent -> execute`) cannot be established.
     
      - ### Step 3  Classify Drift
     
      - ```
        identity axis: trust_score 0.55 > floor 0.70  -> IDENTITY_DRIFT (high)
        access chain:  link 2 broken                   -> ACCESS_DRIFT (high)
        coherence_delta: -0.20                         -> COHERENCE_DRIFT (threshold crossed)
        ```

        ### Step 4  Apply Operator

        ```
        VERIFY(IAM.principal{agent}, trust_score: 0.70)
          result: FAIL -- score 0.55 does not meet floor
          -> ESCALATE(IAM.access_chain, governance_tier: steward)
             Steward re-issues credential at trust_score: 0.72
          -> VERIFY(IAM.principal{agent}, trust_score: 0.70)
             result: PASS -- 0.72 >= 0.70
        Access chain link 2 re-established. Coherence: 0.65 -> 0.87
        ```

        ### Step 5  Write Lineage Note

        **File:** `lineage/IAM/2026-09-26-001.md`

        ```markdown
        # Lineage Note  IAM/2026-09-26-001
        **Event:** IDENTITY_DRIFT + ACCESS_DRIFT + COHERENCE_DRIFT
        **Detected:** 2026-09-26T05:30:00Z
        **Operators:** VERIFY(FAIL) -> ESCALATE(steward) -> VERIFY(PASS)
        **Coherence restored:** 0.65 -> 0.87 (above threshold 0.85)
        **Status:** CLOSED
        **Author:** Nawder Loswin
        ```

        ### Step 6  Corrected Metadata

        ```yaml
        metadata:
          title: "OpenIAM  Identity & Access Surface"
          version: 1.0.1
          principal_registry:
            agent:
              trust_score: 0.72
              last_verified: "2026-09-26"
              credential_ref: "lineage/IAM/2026-09-26-001.md"
          access_chain:
            depth: 4
            link_2_status: active
          coherence_current: 0.87
          last_drift_event: "lineage/IAM/2026-09-26-001.md"
        ```

        ---

        ## 10  Cross-References

        | Module | Relationship |
        |---|---|
        | `openapi/LLM` | Primary identity consumer (agent principals) |
        | `openapi/Risk` | Governance escalation target for high/critical events |
        | `openapi/Geo` | Temporal axis shared; location-scoped principals |
        | `openapi/GPU` | Execution substrate; agent credentials forwarded pre-execution |
        | `openapi/Data` | Data access chain governed by IAM; lineage store access gated |

        ---

        *TriadicFrameworks  OpenAPI Suite  OpenIAM  v1.0.0  Nawder Loswin  2026*
