# **SAI-DESIGN.md**

## *Structural Assisted Intelligence — Canonical Design*
### *SAI/0.1 · TriadicFrameworks Research Substrate*

---

## **Purpose**

SAI is a minimal, model-independent structural reasoning kernel.

It implements Resonance-Time Theory as executable grammar and exists to test whether useful reasoning can arise from structure, operators, observation, and provenance before any trained model is introduced.

SAI is kernel-like. It supplies primitive machinery. Higher layers (applications, Language Model Atlas adapters, domain schemas) may be built above it without altering its invariants.

---

## **Absolute Rules**

1. **Unknown is a successful result.**  
   The system is never forced to manufacture an answer.

2. **Operators may transform structure. They may not invent evidence.**  
   All state changes must be traceable to observations or prior structure.

3. **Explanation is provenance.**  
   “Why” is answered by walking the actual path of observations, relations, and operators—not by generating an explanation after the fact.

4. **No model dependency for core function.**  
   SAI must operate fully without an LLM, embeddings, or statistical generation.

5. **Design under scarcity.**  
   Kilobytes before megabytes. Deterministic operations before generation. Explicit state before probabilities.

---

## **Six Components**

### 1. Observation
Everything enters as an observation, not as truth.

- Identity  
- Content / value  
- Source / provenance  
- Timestamp / order  
- Status / confidence  
- Relationships  

**Invariant:** Observed ≠ inferred ≠ unknown.

### 2. Structural State
Minimal internal representation.

Preferred form:  
`Entity → Relation → Entity` + RTT state variables.

SAI does not require linguistic understanding of the content. It requires that three structural objects have been asserted and that their provenance is known.

### 3. RTT Operator Kernel
Canonical operators (v0.1):

- **OBSERVE** — register an observation with provenance  
- **RELATE** — declare or detect a connection  
- **ALIGN** — evaluate or increase structural alignment  
- **DIFFERENTIATE** — surface distinction or counterstate  
- **RESOLVE** — attempt resolution of an unresolved structure  
- **STABILIZE** — dampen or lock a coherent state  
- **RECALL** — retrieve prior observation, relation, or path  

Operators transform or examine structure. They do not create evidence.

### 4. Triadic Observer
Maintains:

- claim  
- counterstate  
- observer  

Permitted structural statuses include:

- coherent  
- conflicting  
- unresolved  
- insufficient  
- drifting  

Paradox is allowed to persist rather than being erased.

### 5. Tiny Persistent Memory
Stores:

`observations → relations → operations → resulting states`

Memory is explicit and walkable. The reasoning history itself is the explanation.

### 6. Minimal Interface
Primitive, non-linguistic by default.

Example exchange:

```
SAI> observe sky cloudy
OBSERVED
id: obs-0001
state: unresolved

SAI> relate
RELATION DETECTED
obs-0001 <-> obs-0002
coherence: aligned
```

Natural language is deferred to the Language Model Atlas (LMA) layer.

---

## **Permitted State Transitions (v0.1)**

```
UNKNOWN
  ↓ OBSERVE
OBSERVED (unresolved)
  ↓ RELATE
RELATED
  ↓ ALIGN / DIFFERENTIATE
ALIGNED | CONFLICT | DRIFT
  ↓ RESOLVE / STABILIZE
STABLE | UNRESOLVED | INSUFFICIENT
```

- Any state may return to UNKNOWN if evidence is withdrawn or found insufficient.  
- CONFLICT and DRIFT are stable states, not errors.  
- STABLE does not imply truth; it implies structural coherence under current observations.

---

## **Architectural Separation**

```
Application
    ↓
   LMA          Language Model Atlas
    ↓
   SAI          Structural reasoning kernel
    ↓
RTT Structural Grammar
```

- SAI is the authority on state, relations, coherence, provenance, and uncertainty.  
- LMA is a surrounding map of language and knowledge resources. It translates between human language and SAI structure. It does not become the intelligence substrate.

---

## **Success Criteria for v0.1**

- The entire machine is explainable on one page.  
- All reasoning paths are inspectable.  
- Unknown is returned without fabrication.  
- Core function requires no model, GPU, or network.  
- Failure is informative.

---

## **Philosophy**

Small enough to understand.  
Structured enough to reason.  
Open enough to build upon.  
Old enough to run almost anywhere.

SAI/0: let structure earn the word intelligence.

---

**Canonical session header**

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```
