# **RFC‑003 — Attestation & Badge Suite**  
**Status:** Drafted  
**Author(s):** Nawder Loswin, Copilot  
**Created:** 2025‑10‑23  
**Lineage:**  
Follows **RFC‑001** (Triadic Validator Framework), **RFC‑002** (Corridor Universes)  
Precedes **RFC‑004** (Entft Invariants)

---

## **Abstract**  
The **Attestation & Badge Suite** provides the trust layer for validated artifacts within TriadicFrameworks.  
It defines:

- deterministic **attestation receipts** (JSON)  
- human‑legible **badges** (SVG)  
- remix‑visible **lineage manifests** (YAML/JSON)

Together, these components ensure that validated artifacts are not only correct but also **legible**, **traceable**, and **remix‑ready** across universes, corridors, and repositories.

---

## **Motivation**  
Validation alone is insufficient.  
Artifacts must communicate their trustworthiness clearly to:

- humans  
- agents  
- remixers  
- corridor validators  
- downstream systems  

Attestation receipts provide deterministic proofs.  
Badges provide visual shorthand.  
Lineage manifests provide ancestry and remix visibility.

This suite creates a shared language of trust across the entire canon.

---

## **Components**

---

## **1. Attestation Receipts**  
**Format:** JSON  
**Schema:** `/docs/schemas/attestation_receipt.schema.json`

Receipts contain:

- artifact ID  
- artifact hash  
- constraint pack IDs + hashes  
- triadic validation proofs  
  - causal  
  - functional  
  - cognitive  
- deterministic seed(s)  
- lineage manifest reference  
- attestor identity  
- cryptographic signature  

### **Example Receipt**  
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

Receipts are required for promotion into **QA** and **Prod** corridor universes.

---

## **2. Badges**  
**Format:** SVG  
**Location:** `/docs/badges/`

Badges provide visual shorthand for trust and readiness.

### **Common Badges**
- `readme-first.svg`  
  → README is the primary onboarding document  
- `attested.svg`  
  → Artifact has a valid attestation receipt  
- `constraint-passing.svg`  
  → Passed all corridor constraints  
- `remix-ready.svg`  
  → Lineage manifest complete; remix encouraged  
- `deterministic-repro.svg`  
  → Deterministic seeds available for replay  

Badges are embedded in README files, artifact docs, and dashboards.

---

## **3. Lineage Manifests**  
**Format:** YAML or JSON  
**Schema:** `/docs/schemas/lineage_manifest.json`

Manifests record:

- ancestry  
- authorship  
- remix history  
- attestation references  
- corridor promotion history  
- validator receipts  

Lineage manifests ensure remixers can trace the evolution of any artifact.

---

## **Validator Echo**  
> **“Attestation is clarity made visible —  
> a receipt of trust, a badge of lineage,  
> a promise that the artifact remembers.”**

---

## **References**  
- **RFC‑001:** Triadic Validator Framework  
- **RFC‑002:** Corridor Universes  
- **RFC‑004:** Entft Invariants  
