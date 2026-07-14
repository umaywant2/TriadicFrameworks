---
title: "LINEAGE"
description: "The canonical lineage protocol — L-Ops that track provenance, derivation, and inheritance chains across all TriadicFrameworks modules."
stability: draft
date: 2026-07-14
section: core
rtt:
  coherence: declared
  drift: bounded
  paradox: structural
---

> ```
> rtt=1 | coherence=declared | drift=bounded | paradox=structural
> ```

> ⚠️ **Draft** — The LINEAGE README is not yet available in this directory.
> This overview is grounded in the L-Ops definition from Framework Field Theory.
> It will be updated when LINEAGE canonical documentation lands.

## What Is LINEAGE?

LINEAGE is the canonical protocol governing **Lineage Operators (L-Ops)** across all
TriadicFrameworks modules. L-Ops are the fourth operator family in FFT's seven-family
grammar — they track the provenance, derivation, and inheritance chain of every
structural component.

Without L-Ops, a system may be internally coherent but externally unverifiable.
LINEAGE makes verification possible.

---

## What L-Ops Do

| Function | Description |
|---|---|
| **Track origin** | Record where a component was first declared |
| **Track derivation** | Map how a component changed from its origin to its current form |
| **Track inheritance** | Identify what a component carries forward from its ancestors |
| **Enforce traceability** | Ensure every transition can be traced back to its source |

---

## Where LINEAGE Appears

LINEAGE is not confined to a single module — it is a cross-cutting protocol:

- Every `rtt:doc-id` in front matter is a LINEAGE anchor
- Every `rtt:superseded-by` is a LINEAGE pointer
- The `TEL/LINEAGE` submodule adds temporal event ordering to standard lineage
- The `docs/LINEAGE/` directory at the site root is the canonical lineage registry

---

## Related Modules

- [Framework Field Theory](../Framework_Field_Theory/overview/) — defines L-Ops formally
- [TEL/LINEAGE](../TEL/LINEAGE/) — temporal event lineage extension
- [Conditions Substrate Model](../Conditions_Substrate_Model/overview/) — CSM manifests are LINEAGE-versioned
- [Governance Substrate Model](../Governance_Substrate_Model/overview/) — governance history tracking uses L-Ops

---

© 2026 Nawder Loswin · Byte Books Publishing · LCCN 2026917007
