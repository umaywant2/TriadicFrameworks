# RFC-002: Corridor Universes (Dev/Test/QA/Prod)

**Status:** Drafted
**Author(s):** Nawder Loswin, Copilot (assistant)  
**Created:** 2025-10-23  
**Lineage:** Follows RFC-001 (Triadic Validator Framework); Precedes RFC-003 (Attestation & Badges), RFC-004 (Entft Invariants)

---

## Abstract
This RFC defines the Corridor Universes model: a layered approach to virtual environments (Dev, Test, QA, Prod) that enforces safety, lineage, and attestation at each stage.  
Artifacts must pass triadic validation (causal, functional, cognitive) before promotion.  
Rollback and forensic capture are built into the corridor design.

---

## Motivation
Without structured corridors, experimentation risks contaminating production universes.  
The Corridor Universes model provides safe sandboxes for exploration while ensuring only validated artifacts reach production.  
This mirrors proven software lifecycles but extends them into universe‑scale simulations.

---

## Corridor Layers

- **Dev Universe**  
  - Purpose: rapid iteration, stochastic exploration.  
  - Constraints: minimal, exploratory.  
  - Validation: lightweight triadic checks.  

- **Test Universe**  
  - Purpose: deterministic replay, reproducibility.  
  - Constraints: seeded inputs, fixed entropy budgets.  
  - Validation: constraint coverage, lineage traceability.  

- **QA Universe**  
  - Purpose: edge‑case stress, chaos testing.  
  - Constraints: failure catalogs, rupture hygiene.  
  - Validation: resilience under adversarial conditions.  

- **Prod Universe**  
  - Purpose: narrow corridor, stable operation.  
  - Constraints: strict invariants, resonance budgets.  
  - Validation: full triadic proofs, attestation receipts required.  

---

## Promotion Gates
Artifacts may only advance if they satisfy corridor‑specific gates:

- **Dev → Test:** deterministic seed replay, lineage manifest present.  
- **Test → QA:** constraint coverage ≥ 95%, failure catalog updated.  
- **QA → Prod:** attestation receipt signed, rollback plan precomputed.  

---

## Rollback & Forensics
- **Rollback:** Each promotion stores a restore point; demotion is automatic on invariant breach.  
- **Forensics:** Failed promotions trigger capture of inputs, seeds, and diffs for curator review.  

---

## Specification

### Environment Manifests
- Define corridor constraints, entropy budgets, invariants.  
- Example: `/docs/schemas/corridor_env_manifest.json`

### Promotion Policy
```yaml
promotion:
  dev_to_test:
    requires: [lineage_manifest, deterministic_seed]
  test_to_qa:
    requires: [constraint_coverage: ">=95%", failure_catalog]
  qa_to_prod:
    requires: [attestation_receipt, rollback_plan]
```

### Validation Flow
```pseudo
for corridor in [Dev, Test, QA, Prod]:
    run triadic_validation(artifact, corridor.constraints)
    if pass:
        if promotion_gate_satisfied(corridor):
            promote(artifact, next_corridor)
        else:
            reject_with_diagnostics()
    else:
        demote_and_capture_forensics()
```

---

## Security Considerations
- Prevents unvalidated artifacts from contaminating production.  
- Ensures reproducibility via deterministic seeds.  
- Provides rollback and forensic capture for resilience.  
- Enforces resonance budgets and rupture hygiene at QA/Prod levels.  

---

## References
- RFC-000: Index and Lineage Map  
- RFC-001: Triadic Validator Framework  
- RFC-003: Attestation & Badge Suite (forthcoming)  
- RFC-004: Entft Invariants (forthcoming)
