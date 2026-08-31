metrology 
# TCT Protocol

**Status:** REDIRECT STUB
**Document ID:** metrology-redirect-001
**Canonical Path:** `docs/metrology/TCT_Protocol.md`
**Resolves To:** `docs/post-ASML_era/TCT_Protocol.md`

---

## Redirect Notice

> **This path is a registered alias.** The content you are looking for has been published at its canonical location:
>
> **`docs/post-ASML_era/TCT_Protocol.md`**

This file exists to preserve inbound links from tools, scripts, and documentation that reference the metrology-scoped path `docs/metrology/TCT_Protocol.md`. No content is maintained here.

---

## Why This Alias Exists

During the initial documentation architecture, the Temporal Contrast Test protocol was anticipated to reside under `docs/metrology/` alongside other metrology standards. The document was subsequently placed in `docs/post-ASML_era/` as part of the core post-ASML era canon, because TCT results drive SC class assignment and feed directly into fab qualification gates that span beyond metrology scope.

The alias `docs/metrology/TCT_Protocol.md` is retained as a stable redirect for tools and external references that predate the canonical path assignment.

---

## Canonical Document Summary

The **TCT Protocol** (`docs/post-ASML_era/TCT_Protocol.md`) is the normative protocol for the Temporal Contrast Test. It defines:

- Physical basis of temporal contrast as a measurable quantity
- TAIS/ARS/CEC instrument system requirements and configuration
- Test coupon specification and handling
- FSCP (Full-Surface Coherence Probe) address pattern with spacings S1–S7
- Complete test sequence with step-level normative requirements
- AER (Anomalous Event Rate) computation including time-since-injection correction
- Contrast curve fitting using logistic sigmoid parameterization
- SC Rating derivation at reference interval Δτ_ref = 1/256
- SC class assignment from SC Rating (thresholds: SC-I >0.92, SC-II 0.75–0.92, SC-III <0.75)
- Spatial uniformity analysis using 5×5 subregion decomposition
- Calibration chain: RLSS → FTRC → session calibration
- Measurement uncertainty budget
- TCT Report format and required fields
- Integration with downstream protocols (TRS Qualification, PDK certification)

---

## Navigation

| | |
|---|---|
| **Canonical document** | `docs/post-ASML_era/TCT_Protocol.md` |
| **SC class authority** | `docs/materials/SC_Classification.md` |
| **Metrology standard** | `docs/post-ASML_era/The_TGI_Metrology_Standard.md` |
| **Data exchange format** | `docs/data-formats/TCT_DEF_Schema.md` |
| **Module index** | `docs/post-ASML_era/README.md` |
| **Module metadata** | `docs/post-ASML_era/module.json` |

---

*This redirect stub is maintained by the TriadicFrameworks documentation graph. Do not add content to this file — update the canonical document instead.*
