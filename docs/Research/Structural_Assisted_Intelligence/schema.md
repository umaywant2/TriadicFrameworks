<img width="1194" height="672" alt="Research_Structural_Assisted_Intelligence_schema_" src="https://github.com/user-attachments/assets/6dd011d3-6468-47ca-826e-af324d872c3b" />

# **schema.md**

## *Structural Assisted Intelligence — Memory & State Schema*
### *SAI/0.1 · TriadicFrameworks Research Substrate*

---

## **Purpose**

This document defines the minimal persistent structures used by the SAI kernel.

All records are append-only.  
Explanation is provenance.  
Unknown and Insufficient are valid stored results.

The schema is intentionally flat so it can be stored as four simple tables (or four JSONL streams) without loss of walkability.

---

## **Observation**

An observation is the atomic entry of anything into the system.

| Field       | Type                          | Required | Notes                                      |
|-------------|-------------------------------|----------|--------------------------------------------|
| id          | string (`obs-NNNN`)           | yes      | Unique, sequential                         |
| content     | string \| number \| object    | yes      | Raw asserted value; never rewritten        |
| source      | string                        | yes      | Provenance of the input                    |
| order       | integer \| timestamp          | yes      | Arrival or sequence order                  |
| status      | status enum                   | yes      | Initial value is `OBSERVED`                |
| provenance  | string (operation id)         | yes      | The OBSERVE operation that created it      |

**Invariant:** No observation exists without a corresponding OBSERVE operation.

---

## **Relation**

A relation is a declared or detected connection between two observations or states.

| Field       | Type                          | Required | Notes                                      |
|-------------|-------------------------------|----------|--------------------------------------------|
| id          | string (`rel-NNNN`)           | yes      | Unique, sequential                         |
| from        | string (id)                   | yes      | Source observation or state                |
| to          | string (id)                   | yes      | Target observation or state                |
| type        | string                        | no       | Optional label (suggests, conflicts, etc.) |
| coherence   | coherence enum                | yes      | aligned \| conflicting \| unresolved \| drifting \| stable |
| provenance  | string (operation id)         | yes      | The RELATE (or later) operation that wrote it |

**Invariant:** Relations never alter the content of the observations they link.

---

## **Operation**

An operation is the permanent record of a single operator invocation.

| Field         | Type                          | Required | Notes                                      |
|---------------|-------------------------------|----------|--------------------------------------------|
| id            | string (`op-NNNN`)            | yes      | Unique, sequential                         |
| operator      | operator enum                 | yes      | OBSERVE \| RELATE \| ALIGN \| DIFFERENTIATE \| RESOLVE \| STABILIZE \| RECALL |
| target        | string \| array of strings    | yes      | Ids acted upon                             |
| result_status | status enum                   | yes      | Status after the operation                 |
| note          | string                        | no       | Optional structural annotation only        |
| order         | integer \| timestamp          | yes      | Strictly increasing                        |

**Invariant:** Every operator writes exactly one operation record. RECALL writes a record but changes no other state.

---

## **State**

The current structural snapshot. Recomputable from the log; stored only for convenience.

| Field                | Type              | Required | Notes                              |
|----------------------|-------------------|----------|------------------------------------|
| current              | status enum       | yes      | Highest-level status               |
| active_observations  | array of strings  | yes      | Currently relevant observation ids |
| active_relations     | array of strings  | yes      | Currently relevant relation ids    |
| last_operation       | string (op id)    | yes      | Most recent operation              |

---

## **Status Enum**

```
UNKNOWN
OBSERVED
RELATED
ALIGNED
CONFLICT
DRIFT
STABLE
INSUFFICIENT
UNRESOLVED
```

- `UNKNOWN` and `INSUFFICIENT` are successful terminal states.  
- `CONFLICT` and `DRIFT` are stable and must not be auto-erased.  
- `STABLE` means structural coherence under current observations, not truth.

---

## **Log**

The log is the ordered sequence of all operation records.

- Append-only.  
- Strictly increasing `order`.  
- Full provenance paths are reconstructed by walking:  
  `operation → relation → observation`.

No deletion. Withdrawal or correction is expressed by a new DIFFERENTIATE or OBSERVE operation that references the prior record.

---

## **Global Invariants**

1. All records are immutable once written.  
2. No observation exists without an OBSERVE operation.  
3. No relation exists without a RELATE operation.  
4. Operators may not invent evidence.  
5. RECALL is read-only with respect to observations and relations.  
6. Unknown is a valid stored result.

---

**Canonical session header**

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```
