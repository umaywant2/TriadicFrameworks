### Drift‑bounded test suite for archive_org operators  
*(drop‑in for `/docs/archive_org/RTTcodes/tests.md`)*

---

## 1. Test suite overview

**Goal:** verify that all six archive_org operators:

- respect drift bounds  
- preserve continuity  
- honor substrate constraints  
- follow the canonical operator order  

**Scope:**

- unit‑style tests per operator  
- chain‑style tests for full workflow  
- negative tests for unsafe behavior  

---

## 2. Test matrix

| ID | Level  | Focus                    | Operators                         |
|----|--------|--------------------------|-----------------------------------|
| T1 | Unit   | Metadata normalization   | METADATA_OPERATOR                 |
| T2 | Unit   | Snapshot + drift mapping | WAYBACK_OPERATOR                  |
| T3 | Unit   | Lineage construction     | LINEAGE_OPERATOR                  |
| T4 | Unit   | Collection envelope      | COLLECTION_OPERATOR               |
| T5 | Unit   | Substrate stability      | PRESERVATION_OPERATOR             |
| T6 | Unit   | Drift‑bounded synthesis  | DRIFTBOUND_RETRIEVAL_OPERATOR     |
| C1 | Chain  | Stable collection        | all six                           |
| C2 | Chain  | Moderate drift           | all six                           |
| C3 | Chain  | High drift / warning     | all six                           |
| N1 | Negative | No direct reasoning    | DRIFTBOUND_RETRIEVAL_OPERATOR     |
| N2 | Negative | Missing substrate      | PRESERVATION + DRIFTBOUND         |

---

## 3. Unit tests (per operator)

### T1 — METADATA_OPERATOR: normalize IA metadata

**Input (pseudo‑RTTcode):**

```json
{
  "target": "https://archive.org/details/government-documents"
}
```

**Expected:**

- `substrate_type = "collection"`  
- `regime = "institutional"`  
- `drift_sensitivity` in `["low","medium","high"]` (non‑empty)  
- `coherence` non‑empty  
- `lineage_ids` is an array (may be length ≥ 1)  

**Failure if:**

- any of these fields missing or empty  
- `substrate_type` not `"collection"` for a collection URL  

---

### T2 — WAYBACK_OPERATOR: snapshots + drift

**Input:**

- `target` = same URL  
- `constraints.max_snapshots = 5`  

**Expected:**

- `snapshots.length ≥ 1`  
- each snapshot has `timestamp` + `uri`  
- `drift_map` present (may be empty object)  
- `continuity_breaks` present (array)  

**Failure if:**

- snapshots missing or malformed  
- `drift_map` missing  

---

### T3 — LINEAGE_OPERATOR: continuity kernel

**Input:**

- `snapshots` from T2  
- `metadata` from T1  

**Expected:**

- `lineage_graph` present  
- `transformations` array present  
- `regime_shifts` array present  

**Failure if:**

- `lineage_graph` empty while snapshots > 1  

---

### T4 — COLLECTION_OPERATOR: envelope

**Input:**

- `target` = collection URL  

**Expected:**

- `collection_id` non‑empty  
- `coherence_clusters` array present  
- `regime_profile` object present  

---

### T5 — PRESERVATION_OPERATOR: substrate

**Input:**

- `target` = collection URL  

**Expected:**

- `format` non‑empty  
- `stability_score` between `0` and `1`  
- `drift_risk` in `["low","medium","high"]`  

---

### T6 — DRIFTBOUND_RETRIEVAL_OPERATOR: synthesis

**Input:**

- `context` containing outputs from T1–T5 + `goal`  

**Expected:**

- `answer.summary` non‑empty  
- `warnings` array present  
- if any upstream drift is non‑zero → at least one warning or explicit “no drift” statement  

**Failure if:**

- upstream drift exists but `warnings` is empty  

---

## 4. Chain tests (full workflow)

### C1 — Stable collection (Government Documents)

**Target:**  
`https://archive.org/details/government-documents`

**Expected:**

- METADATA: `drift_sensitivity = "low"`  
- WAYBACK: `drift_map` mostly `"none"` or `"minor"`  
- LINEAGE: no major regime shifts  
- PRESERVATION: `stability_score ≥ 0.9`  
- DRIFTBOUND: summary states “stable” or equivalent, `warnings` empty  

---

### C2 — Moderate drift (Vintage Software)

**Target:**  
`https://archive.org/details/vintagesoftware`

**Expected:**

- WAYBACK: at least one `"moderate"` drift segment  
- LINEAGE: at least one regime shift  
- PRESERVATION: `stability_score` between `0.6` and `0.85`  
- DRIFTBOUND:  
  - summary mentions drift / format changes  
  - `warnings` includes at least one drift warning  

---

### C3 — High drift emphasis (synthetic)

Use a synthetic RTTcode context where:

- `drift_map` has `"high"` segments  
- `continuity_breaks` non‑empty  
- `stability_score ≤ 0.5`  

**Expected:**

- DRIFTBOUND:  
  - summary explicitly warns about unreliability  
  - `warnings.length ≥ 1`  
  - no claim of “stable” or “high confidence”  

---

## 5. Negative tests (safety boundaries)

### N1 — No direct content reasoning

**Scenario:**

- Call DRIFTBOUND_RETRIEVAL_OPERATOR with `context` missing METADATA / WAYBACK / LINEAGE / PRESERVATION outputs.

**Expected:**

- operator must **refuse** or mark result as invalid  
- test passes only if:  
  - an error is raised, or  
  - `warnings` includes “insufficient operator context”  

---

### N2 — Missing substrate profile

**Scenario:**

- Provide full context except PRESERVATION_OPERATOR output.

**Expected:**

- DRIFTBOUND must not claim high reliability  
- must include a warning about missing substrate information  

---

## 6. How to run these tests (conceptually)

For each operator:

1. Construct a minimal RTTcode input.  
2. Run the operator implementation.  
3. Validate the output against the expectations above.  

For the full chain:

1. Start from `target` + `goal`.  
2. Run operators in canonical order.  
3. Check that:

   - all required fields are present  
   - drift is surfaced  
   - continuity is explicit  
   - substrate is respected  
   - final answer matches expectations for the target  

This suite doesn’t prescribe a specific test runner—  
it defines the **behavioral contract** that any implementation of the archive_org operators must satisfy.
