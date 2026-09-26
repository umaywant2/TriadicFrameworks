# OpenLLM — TriadicFrameworks OpenAPI Surface

> **Name disambiguation:** `openapi` in this canon does not refer to the OpenAPI Specification (OAS/Swagger) REST-schema standard. It refers to the TriadicFrameworks *open-aperture principle*: a domain module that exposes its signature, operators, drift surface, and lineage hooks to cross-domain inspection. Every `Open*` module is an openapi-compliant surface in the canon sense.

---

## 1 · Identity

| Field | Value |
|---|---|
| Module ID | `openapi/LLM` |
| Domain | Language Model infrastructure |
| Ring layer | Motion → Trust → Meaning |
| Canonical version | 1.0.0 |
| Author | Nawder Loswin |
| Audience | AI agents, framework operators, integration architects |

---

## 2 · Architecture

OpenLLM is the language-model surface of the TriadicFrameworks OpenAPI suite. It exposes three structural planes:

### 2.1 Signature Plane
The signature plane declares the module's identity contract: its dimension vector, regime tag, coherence threshold, and operator affinity list. Agents read the signature before any cross-domain operation.

```yaml
signature:
  module: openapi/LLM
  dimension_vector: [semantic, temporal, causal]
  regime: generative
  coherence_threshold: 0.78
  operator_affinity: [NORMALIZE, ALIGN, PROPAGATE, COLLAPSE]
  rings: [Motion, Trust, Meaning]
```

### 2.2 Metadata Plane
The metadata plane holds canonical fields that sibling modules scan when classifying drift.

```yaml
metadata:
  title: "OpenLLM — Language Model Surface"
  category: openapi
  domain: LLM
  version: 1.0.0
  status: active
  drift_surface: true
  lineage_hooks: true
  last_reviewed: "2026-09-26"
```

### 2.3 Operator Plane
The operator plane enumerates all operators that may act on this module's outputs. Operators follow the canonical grammar: `VERB(subject, target, [modifier])`.

---

## 3 · Canonical Metadata

```html
<!-- OpenLLM canonical head block -->
<meta name="ai.module"           content="openapi/LLM" />
<meta name="ai.version"          content="1.0.0" />
<meta name="ai.purpose"          content="Language model open-aperture surface" />
<meta name="ai.module.name"      content="OpenLLM" />
<meta name="ai.module.summary"   content="Exposes LLM signature, operators, drift surface, and lineage hooks to cross-domain inspection." />
<meta name="ai.module.category"  content="openapi" />
<meta name="ai.audience"         content="AI agents, framework operators" />
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
OpenLLM is governed by the TriadicFrameworks canon steward (Nawder Loswin). Changes to the signature plane require a lineage note. Changes to the operator plane require a governance review and a drift-event record.

### 4.2 Change Protocol
1. Author proposes change in a lineage note (`lineage/<module>/<timestamp>.md`).
2. Sibling modules are scanned for drift exposure.
3. Drift is classified using the openapi loop (section 6).
4. An operator is applied to resolve or absorb drift.
5. The lineage note is closed with resolution status.

### 4.3 Versioning
Versions follow `MAJOR.MINOR.PATCH`. A drift event that changes the coherence threshold increments MINOR. A signature-plane breaking change increments MAJOR.

---

## 5 · Operators

| Operator | Grammar | Purpose |
|---|---|---|
| NORMALIZE | `NORMALIZE(LLM.output, semantic_axis)` | Flatten register varian

---

## 6 · The OpenAPI Loop

The openapi loop is the canonical read-scan-classify-apply-write cycle. Every compliant `Open*` module must support this loop.

```
1. READ SIGNATURE
   Agent reads module.signature to confirm identity contract and operator affinity.

2. SCAN SIBLING METADATA
   Agent scans all sibling Open* modules in docs/openapi/ for metadata mismatches
   vs. this module's declared dimension_vector.

3. CLASSIFY DRIFT
   Each mismatch is classified:
     * SEMANTIC_DRIFT  -- meaning divergence
     * REGIME_DRIFT    -- operational mode mismatch
     * TEMPORAL_DRIFT  -- version / recency gap
     * COHERENCE_DRIFT -- threshold crossing

4. APPLY OPERATOR
   Select and apply the appropriate operator from the module's operator affinity list.

5. WRITE LINEAGE
   Record the drift event, applied operator, and resolution in
   lineage/<module>/<timestamp>.md
```

---

## 7 · The Three Rings

Every OpenAPI surface is layered across three rings that define its scope of concern and propagation direction.

### Ring 1 · Trust
The innermost ring. Governs identity verification, signature validity, and governance compliance. A module with a broken Trust ring cannot participate in cross-domain operations.

*OpenLLM Trust markers:* valid signature YAML, canonical metadata block, governance record current.

### Ring 2 · Motion
The middle ring. Governs operator application, drift propagation, and loop execution. A module in the Motion ring is actively processing or propagating.

*OpenLLM Motion markers:* operator affinity list non-empty, drift_surface: true, lineage_hooks: true.

### Ring 3 · Meaning
The outer ring. Governs semantic coherence, output interpretation, and cross-domain alignment. A module reaching the Meaning ring has produced interpretable, aligned output.

*OpenLLM Meaning markers:* coherence_threshold >= 0.78, ALIGN operator applied, lineage note closed.

---

## 8 · Drift-Event JSON Example

```json
{
  "drift_event": {
    "id": "drift/LLM/2026-09-26-001",
    "detected_at": "2026-09-26T05:30:00Z",
    "source_module": "openapi/LLM",
    "target_module": "openapi/IAM",
    "drift_type": "SEMANTIC_DRIFT",
    "severity": "moderate",
    "description": "LLM output used identity context to mean conversation history; IAM surface uses same term for access-control principal. Dimension vectors misaligned on semantic_axis.",
    "dimension_vector_source": ["semantic", "temporal", "causal"],
    "dimension_vector_target": ["identity", "access", "temporal"],
    "coherence_delta": -0.14,
    "coherence_before": 0.82,
    "coherence_after": 0.68,
    "threshold_crossed": true,
    "operator_applied": "ALIGN(LLM.signature, IAM.signature)",
    "resolution_status": "resolved",
    "lineage_ref": "lineage/LLM/2026-09-26-001.md"
  }
}
```ce across model outputs |
| ALIGN | `ALIGN(LLM.signature, IAM.signature)` | Cross-domain signature reconciliation |
| PROPAGATE | `PROPAGATE(LLM.drift, sibling_modules)` | Broadcast detected drift to downstream surfaces |
| COLLAPSE | `COLLAPSE(LLM.ambiguity, coherence_threshold)` | Force resolution below coherence floor |
| ANNOTATE | `ANNOTATE(LLM.output, lineage_ref)` | Attach lineage reference to an output node |
| REFRAME | `REFRAME(LLM.context, causal_axis)` | Shift causal framing without altering semantic content |

### 5.1 Operator Composition Example

```
NORMALIZE(LLM.output, semantic_axis)
  -> ALIGN(LLM.signature, Risk.signature)
  -> ANNOTATE(result, lineage/LLM/2026-09-26-001.md)
```
