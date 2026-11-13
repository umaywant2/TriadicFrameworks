# **LMA_boundary.md**

## *Structural Assisted Intelligence — Language Model Atlas Boundary*
### *SAI/0.1 · TriadicFrameworks Research Substrate*

---

## **Purpose**

The Language Model Atlas (LMA) is a surrounding map of language and knowledge resources.

It translates between human language and SAI structure.  
It does not become the intelligence substrate.  
It does not write structural truth back into SAI.

This document defines the only permitted crossing points.

---

## **Direction of Authority**

```
Human / Application
        ↓
       LMA          (translation & resource map)
        ↓
       SAI          (structural authority)
        ↓
   RTT Grammar
```

SAI remains the sole authority on:

- observation content and provenance  
- relations and coherence  
- status (including UNKNOWN, CONFLICT, UNRESOLVED)  
- operation history  

LMA may read these. It may not overwrite them.

---

## **What SAI Emits (LMA may consume)**

SAI may expose, in structured form only:

- Observation records (`id`, `content`, `source`, `status`, `provenance`)  
- Relation records (`id`, `from`, `to`, `type`, `coherence`, `provenance`)  
- Operation records (`id`, `operator`, `target`, `result_status`, `order`)  
- Current status enum value  
- Provenance paths (ordered list of operation ids)

Emission is read-only. No natural-language generation is required from SAI.

---

## **What LMA May Return to SAI**

LMA may submit only:

1. **New observations**  
   Via the OBSERVE operator.  
   Must include explicit `source` (e.g. `lma:model-x` or `lma:dictionary`).  
   Content is treated as asserted input, never as inferred truth.

2. **Relation suggestions**  
   Via the RELATE operator.  
   Marked as proposed; SAI decides whether the relation is recorded and what coherence it receives.

3. **Recall requests**  
   Via the RECALL operator.  
   Pure reads.

LMA may not:

- Call ALIGN, DIFFERENTIATE, RESOLVE, or STABILIZE directly  
- Modify existing observation content  
- Delete or rewrite operation history  
- Set status values  
- Inject provenance that claims to originate inside SAI  

---

## **Translation Contract**

| Direction       | LMA Responsibility                          | SAI Responsibility                     |
|-----------------|---------------------------------------------|----------------------------------------|
| Inbound         | Map natural language → observation or relate proposal | Accept or reject via operator rules   |
| Outbound        | Map SAI status + provenance path → optional natural language | Emit only structured records          |
| Uncertainty     | Preserve UNKNOWN / UNRESOLVED / CONFLICT    | Never fabricate to satisfy LMA        |

If LMA cannot produce a valid OBSERVE or RELATE payload, it must surface the SAI status unchanged.

---

## **Invariants at the Boundary**

1. Every LMA-originated observation carries an LMA source tag.  
2. SAI may ignore or reject any LMA proposal without explanation beyond status.  
3. LMA-generated language is never stored as SAI content unless it first passes through OBSERVE.  
4. Provenance walks always show the LMA source when present; they never hide it.  
5. The boundary is one-way for structural authority.

---

## **Minimal Example**

```
LMA → SAI:  OBSERVE content="sky cloudy" source="lma:user"
SAI → LMA:  obs-0001 status=OBSERVED

LMA → SAI:  RELATE obs-0001 obs-0002 type=suggests
SAI → LMA:  rel-0001 coherence=aligned status=RELATED

LMA → SAI:  (requests natural-language summary)
SAI → LMA:  status=ALIGNED path=[op-0004, op-0003, op-0002, op-0001]
LMA:        (optionally renders the path in language; does not write back)
```

---

**Canonical session header**

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```
