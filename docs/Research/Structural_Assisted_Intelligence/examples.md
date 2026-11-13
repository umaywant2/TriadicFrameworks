# **examples.md**

## *Structural Assisted Intelligence — Primitive Sessions*
### *SAI/0.1 · TriadicFrameworks Research Substrate*

---

## **Purpose**

These sessions demonstrate the kernel operating within its invariants.

No natural language is generated.  
Unknown is returned when appropriate.  
Every “why” is a provenance walk.

---

## **1. Clean Observe → Relate → Align**

```
SAI> observe sky cloudy
OBSERVED
id: obs-0001
content: "sky cloudy"
status: OBSERVED
provenance: op-0001

SAI> observe forecast rain
OBSERVED
id: obs-0002
content: "forecast rain"
status: OBSERVED
provenance: op-0002

SAI> relate obs-0001 obs-0002 type:suggests
RELATED
id: rel-0001
from: obs-0001
to: obs-0002
coherence: aligned
status: RELATED
provenance: op-0003

SAI> align rel-0001
ALIGNED
id: rel-0001
coherence: aligned
status: ALIGNED
provenance: op-0004
```

---

## **2. Path That Correctly Remains Unresolved**

```
SAI> observe temperature 22
OBSERVED
id: obs-0003
status: OBSERVED
provenance: op-0005

SAI> resolve obs-0003
UNRESOLVED
reason: insufficient supporting relations
status: UNRESOLVED
provenance: op-0006
```

No evidence was invented. The status remains unresolved.

---

## **3. Conflict Allowed to Persist**

```
SAI> observe road wet
OBSERVED
id: obs-0004
status: OBSERVED
provenance: op-0007

SAI> observe road dry
OBSERVED
id: obs-0005
status: OBSERVED
provenance: op-0008

SAI> relate obs-0004 obs-0005 type:conflicts
RELATED
id: rel-0002
coherence: conflicting
status: RELATED
provenance: op-0009

SAI> differentiate rel-0002
CONFLICT
id: rel-0002
coherence: conflicting
status: CONFLICT
provenance: op-0010
```

The conflict is recorded and left intact. No forced resolution occurs.

---

## **4. Provenance Walk (“why”)**

```
SAI> why rel-0001

PATH
op-0004 ALIGN     → status: ALIGNED
op-0003 RELATE    → rel-0001 created (obs-0001 ↔ obs-0002)
op-0002 OBSERVE   → obs-0002 created
op-0001 OBSERVE   → obs-0001 created

status: ALIGNED
```

The response contains only the actual structural path. No generated explanation is added.

---

## **5. Unknown as Successful Result**

```
SAI> observe 
UNKNOWN
reason: no content supplied
status: UNKNOWN
provenance: op-0011
```

The kernel refuses to manufacture an observation.

---

## **Notes**

- All sessions are reproducible from the operation log alone.  
- Statuses CONFLICT, DRIFT, UNRESOLVED, and UNKNOWN are stable and successful.  
- These transcripts are the acceptance criteria for any later implementation.

---

**Canonical session header**

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```
