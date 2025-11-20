# 📜 RFC-003: Attestation & Badge Suite

**Status:** Drafted
**Author(s):** Nawder Loswin, Copilot (assistant)  
**Created:** 2025-10-23  
**Lineage:** Follows RFC-001 (Triadic Validator Framework), RFC-002 (Corridor Universes); Precedes RFC-004 (Entft Invariants)

---

## Abstract
This RFC defines the Attestation & Badge Suite: a trust layer for validated artifacts.  
It introduces JSON receipts for deterministic proofs, SVG badges for onboarding clarity, and lineage manifests for remix visibility.  
The suite ensures that artifacts are not only validated but also legible to humans and agents.

---

## Motivation
Validation without visibility limits adoption.  
Attestation receipts and badges provide proof of integrity, constraint coverage, and remix readiness.  
They also create a shared language for trust across repositories, universes, and remixers.

---

## Components

### Attestation Receipts
- **Format:** JSON schema (`/docs/schemas/attestation_receipt.schema.json`)  
- **Contents:**
  - Artifact ID and hash  
  - Constraint pack IDs and hashes  
  - Validation proofs (causal, functional, cognitive)  
  - Deterministic seed(s)  
  - Lineage manifest reference  
  - Attestor signature  

**Example:**
```json
{
  "artifact_id": "bubbleTheory_manifest.json",
  "hash": "sha256-abc123...",
  "constraints": ["constraint_pack_v1.2"],
  "proofs": {
    "causal": true,
    "functional": true,
    "cognitive": true
  },
  "seed": "42",
  "lineage_ref": "lineage_manifest.json",
  "attestor": "validator-node-7",
  "signature": "ed25519:xyz..."
}
```

---

### Badges
- **Purpose:** Visual shorthand for validation status and remix readiness.  
- **Format:** SVG icons in `/docs/badges/`.  
- **Examples:**
  - `readme-first.svg` → README is primary onboarding doc.  
  - `attested.svg` → Artifact has valid attestation receipt.  
  - `constraint-passing.svg` → Passed all corridor constraints.  
  - `remix-ready.svg` → Lineage manifest complete, remix encouraged.  
  - `deterministic-repro.svg` → Deterministic seeds available for replay.  

Badges are embedded in `README.md` or artifact docs to signal trust at a glance.

---

### Lineage Manifests
- **Format:** YAML/JSON (`/docs/schemas/lineage_manifest.json`)  
- **Contents:** ancestry, authorship, remix history, attestation references.  
- **Purpose:** Preserve remix lineage and ensure validator clarity.

---

## Specification

### Attestation Flow
```pseudo
on_validation_success(artifact):
    receipt = generate_receipt(artifact, proofs, lineage)
    sign(receipt, attestor_key)
    store(receipt, /receipts/)
    badge = assign_badges(receipt)
    update_readme(badge)
```

### Badge Assignment Rules
- **Attested:** if valid receipt exists.  
- **Constraint-Passing:** if all corridor constraints satisfied.  
- **Remix-Ready:** if lineage manifest complete.  
- **Deterministic-Repro:** if seeds provided and replayable.  

---

## Security Considerations
- Receipts are cryptographically signed to prevent forgery.  
- Badges are only assigned if receipts validate against schema.  
- Lineage manifests prevent “cleartext lineage” downgrades.  
- Deterministic seeds ensure reproducibility and auditability.  

---

## References
- [RFC-000: Index and Lineage Map](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rfc/RFC-000-index.md)
- [RFC-001: Triadic Validator Framework](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rfc/RFC-001-triadic-validator-framework.md)
- [RFC-002: Corridor Universes](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rfc/RFC-002-corridor-universes.md)
- [RFC-004: Entft Invariants](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rfc/RFC-004-entft-invariants.md)
