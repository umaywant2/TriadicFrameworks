# **operators.md**

## *Structural Assisted Intelligence — Operator Contracts*
### *SAI/0.1 · TriadicFrameworks Research Substrate*

---

## **Purpose**

These are the canonical operators of the SAI kernel.

Each operator may examine or transform structure.  
None may invent evidence.  
All effects must be traceable to prior observations or prior structure.

Unknown remains a valid, stable result.

---

## **OBSERVE**

**Role**  
Register an observation with full provenance.

**May see**  
Raw input, source identifier, timestamp/order.

**May change**  
Create a new observation record.  
Set initial status to OBSERVED (unresolved).

**Must never change**  
Existing relations, prior observations, or inferred content.

**Status transitions**  
`UNKNOWN → OBSERVED`

**Example**
```
OBSERVE sky cloudy
→ obs-0001 created
  content: "sky cloudy"
  provenance: user
  status: OBSERVED (unresolved)
```

---

## **RELATE**

**Role**  
Declare or detect a connection between two existing observations or states.

**May see**  
Two observation/state identifiers and an optional relation type.

**May change**  
Create a relation record linking the two.  
Update local coherence notes.

**Must never change**  
The content or provenance of the observations themselves.

**Status transitions**  
`OBSERVED → RELATED`  
`RELATED → RELATED` (additional links)

**Example**
```
RELATE obs-0001 obs-0002 type:suggests
→ relation-0001 created
  coherence: aligned
  status: RELATED
```

---

## **ALIGN**

**Role**  
Evaluate or increase structural alignment between related items.

**May see**  
Existing relations and their current coherence notes.

**May change**  
Update coherence annotation on a relation.  
Move status toward ALIGNED when alignment holds.

**Must never change**  
Observation content or invent supporting evidence.

**Status transitions**  
`RELATED → ALIGNED`  
`ALIGNED → ALIGNED` (reinforced)

**Example**
```
ALIGN relation-0001
→ coherence: aligned
  status: ALIGNED
```

---

## **DIFFERENTIATE**

**Role**  
Surface distinction or counterstate without erasing either side.

**May see**  
Two related observations or a single observation and a new counter-observation.

**May change**  
Create or annotate a counterstate.  
Set status to CONFLICT or DRIFT when distinction is material.

**Must never change**  
Erase either side of the distinction.

**Status transitions**  
`RELATED → CONFLICT`  
`RELATED → DRIFT`  
`ALIGNED → CONFLICT` (if new differentiation appears)

**Example**
```
DIFFERENTIATE obs-0001 vs obs-0003
→ counterstate recorded
  status: CONFLICT
```

---

## **RESOLVE**

**Role**  
Attempt resolution of an unresolved or conflicting structure.

**May see**  
Current relations, counterstates, and provenance paths.

**May change**  
Annotate a resolution path if one is fully supported by existing structure.  
Move status to STABLE or leave as UNRESOLVED.

**Must never change**  
Invent missing evidence to force a resolution.

**Status transitions**  
`CONFLICT → STABLE` (only if path is fully supported)  
`UNRESOLVED → STABLE`  
`* → UNRESOLVED` (if support is insufficient)

**Example**
```
RESOLVE relation-0001
→ insufficient supporting path
  status: UNRESOLVED
```

---

## **STABILIZE**

**Role**  
Dampen or lock a coherent state so it resists casual drift.

**May see**  
Current status and recent operation history.

**May change**  
Mark a state or relation as stabilized.  
Record the stabilizing operation in provenance.

**Must never change**  
Override an active CONFLICT or invent stability.

**Status transitions**  
`ALIGNED → STABLE`  
`STABLE → STABLE`

**Example**
```
STABILIZE relation-0001
→ status: STABLE
  provenance: stabilized by operator
```

---

## **RECALL**

**Role**  
Retrieve a prior observation, relation, or provenance path.

**May see**  
Any stored identifier or partial match.

**May change**  
Nothing. Read-only.

**Must never change**  
State, relations, or memory contents.

**Status transitions**  
None (status-preserving)

**Example**
```
RECALL obs-0001
→ returns full observation record + path
  status unchanged
```

---

## **Global Constraints**

- Every operator writes its own entry into the provenance log.  
- No operator may create an observation without an OBSERVE step.  
- No operator may delete history.  
- If an operator cannot act without inventing evidence, it returns the current status unchanged (or UNKNOWN / INSUFFICIENT).

---

**Canonical session header**

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```
