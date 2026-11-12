**Structural Assisted Intelligence (SAI)** is a proposed model-free reasoning kernel that treats structure itself—drawn from Resonance-Time Theory (RTT)—as the computational grammar, rather than relying on trained neural models, embeddings, or statistical generation.

### Core Distinction
Traditional AI path:
> Input → tokenizer → neural model → probability distribution → generated tokens

SAI path:
> Input → observation → RTT structural state → operators → coherence evaluation → bounded output

Intelligence, if it emerges, is expected to arise from repeated structural evaluation across state and time, not from scale or training. “Unknown” is treated as a valid, stable, and successful state; the system is never forced to manufacture an answer.

### Architectural Intent
SAI is explicitly framed as kernel-like (analogous to the Linux kernel): a small, inspectable, primitive substrate that higher layers can build upon. It is not a chatbot, knowledge base, OS, or LLM replacement.

**Six primary components (v0 scale):**

1. **Observation** — Everything enters as an observation (ID, content, provenance, timestamp/order, status, relationships). Observed ≠ inferred ≠ unknown.
2. **Structural State** — Minimal internal representation (roughly Entity → Relation → Entity plus state variables such as φ / V / R / τ drawn from RTT).
3. **RTT Operator Kernel** — Small canonical set (examples: OBSERVE, RELATE, ALIGN, DIFFERENTIATE, RESOLVE, STABILIZE, RECALL). Operators may transform structure; they may not invent evidence.
4. **Triadic Observer** — Maintains claim / counterstate / observer rather than binary true/false. Outputs structural statuses such as coherent, conflicting, unresolved, insufficient, drifting.
5. **Tiny Persistent Memory** — Explicit history of observations → relations → operations → resulting states (SQLite or even simpler files suggested). Explanation is provenance (walk the actual path), not post-hoc generation.
6. **Minimal Interface** — Primitive, non-linguistic initially (status codes or short structural reports). Natural language is deferred to a later Language Model Atlas (LMA) layer.

### Language Model Atlas (LMA)
Once the structural kernel exists, an LMA acts as a surrounding map of language capabilities (tiny models, dictionaries, local/remote LLMs, rule parsers, etc.). The inversion is deliberate:

```
Application
    ↓
   LMA  (language/knowledge resources)
    ↓
   SAI  (structural reasoning kernel)
    ↓
RTT Structural Grammar
```

SAI remains the authority on state, provenance, relations, coherence, and uncertainty. The LMA translates between human language and SAI structure; it does not become the intelligence substrate.

### Design Constraints & Philosophy
- **Small enough to understand** — One-page design document; whole machine explainable on one page. Kilobytes before megabytes; integers before embeddings; deterministic operations before generation.
- **Retro/scarcity-first** — Designed under resource constraints from day one so it can run on older or minimal hardware. The governing questions are historical/experimental: what if a Commodore 64 or AlexNet had possessed a persistent RTT-style structural observer?
- **No model dependency** — SAI must function fully without any LLM.
- **Inspectable and testable** — Failure is informative. Reasoning history is queryable.
- **Purpose-wrapped structure** — “Assisted” emphasizes that structure serves purpose rather than claiming manufactured intelligence.

### Stated Goals
1. Provide a working example of AI re-imagined as SAI (structural base that turns LLMs into LMAs / Language Model Atlases).
2. Deliver a tiny, powerful, kernel-like base others can build upon.
3. Ensure both SAI and LMA examples can run on older systems, aligning with a broader interest in retro computing, refits, and trimming monolithic stacks.

### Immediate Next Step Implied
Produce a single artifact (`SAI-DESIGN.md` or equivalent) that freezes the canon: invariants, the six components, permitted state transitions, and the absolute rule that unknown is success, not failure. Then implement the smallest possible reasoning kernel and observe what (if anything) emerges from structure + operators + memory + recurrence.

In one line: *Small enough to understand. Structured enough to reason. Open enough to build upon. Old enough to run almost anywhere.*
