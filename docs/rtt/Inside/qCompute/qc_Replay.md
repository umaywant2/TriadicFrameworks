# qCompute — Replay Engine  
**File:** qc_Replay.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The Replay Engine is the **final authority** of qCompute.

Replay reconstructs:

- session  
- frames  
- operators  
- transitions  
- drift  
- routing  
- backend legality  
- environment sequence  
- hash chain integrity  

Replay verifies that the `.qtrace` ledger is **complete**, **valid**, and **canonical**.

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

Replay:

- reads the `.qtrace` file  
- reconstructs the entire session deterministically  
- verifies all invariants  
- verifies all routing decisions  
- verifies all drift calculations  
- verifies all transitions  
- verifies all frame boundaries  
- verifies all backend legality  
- verifies all environment legality  
- verifies the hash chain  

Replay is **read‑only** and **authoritative**.

---

# 2. Replay Inputs

Replay receives:

```
.qtrace file:
  header
  operator entries
  frame summaries
  transitions
  footer
  hash chain root
```

All fields are required.

---

# 3. Replay Reconstruction Model

Replay reconstructs the session by:

1. reading operator stream  
2. applying Validator rules  
3. applying Router rules  
4. applying Frame Manager rules  
5. applying Drift Engine rules  
6. applying Transition Engine rules  
7. verifying capture metadata  
8. verifying hash chain integrity  

Replay must produce the **same structural session** that was originally executed.

---

# 4. Operator Reconstruction

For each operator:

Replay verifies:

- grammar  
- arguments  
- tier legality  
- backend legality  
- environment legality  
- token requirements  
- routing reason  
- frame action  
- drift metadata  
- timestamps  
- hash chain links  

Replay recomputes:

- backend  
- routing reason  
- frame action  
- drift predicted  
- drift measured  
- drift accumulated  

Replay must match capture exactly.

---

# 5. Frame Reconstruction

Replay reconstructs frames by:

- opening frames on routing triggers  
- closing frames on routing triggers  
- enforcing tier monotonicity  
- enforcing backend consistency  
- enforcing drift bounds  
- enforcing environment consistency  

Replay verifies:

- frame boundaries  
- frame drift summaries  
- frame backend summaries  
- frame timestamps  

Frames must match capture exactly.

---

# 6. Transition Reconstruction

Replay reconstructs transitions by:

- reading transition entries  
- verifying legality  
- verifying token usage  
- verifying environment sequence  
- verifying drift reset  
- verifying frame closure  
- verifying backend legality  

Replay must confirm:

- sandbox → production → archive  
- no illegal transitions  
- archive is terminal  

---

# 7. Drift Reconstruction

Replay recomputes drift:

```
drift_total = Σ drift_measured
```

Replay verifies:

- drift never exceeds bound  
- drift overflow events match capture  
- drift resets match frame boundaries  
- drift summaries match operator accumulation  

Drift must match capture exactly.

---

# 8. Backend Reconstruction

Replay verifies:

- backend legality  
- tier binding  
- environment legality  
- backend changes  
- backend summaries  

Backend must match capture exactly.

---

# 9. Hash Chain Verification

Each operator and transition includes:

```
hash_prev: "<sha256>"
hash_self: "<sha256>"
```

Replay verifies:

- hash_prev matches previous entry  
- hash_self matches recomputed hash  
- final hash matches footer root  

If hash chain invalid:

```
replay_valid: false
reason: "hash chain invalid"
```

---

# 10. Replay Metadata

Replay produces:

```
replay:
  valid: true|false
  reasons: [...]
  reconstructed_session: {...}
```

Reasons include:

- "illegal operator"
- "illegal transition"
- "tier violation"
- "backend violation"
- "environment violation"
- "drift violation"
- "hash chain invalid"
- "capture mismatch"

---

# 11. Invariants

Replay enforces:

1. grammar correctness  
2. argument correctness  
3. environment legality  
4. backend legality  
5. tier monotonicity  
6. drift bounds  
7. routing correctness  
8. transition correctness  
9. token requirements  
10. frame boundaries  
11. archive terminality  
12. hash chain integrity  

Replay is the **final arbiter** of structural truth.

---

# 12. Summary

The Replay Engine:

- reconstructs the entire session  
- verifies every structural decision  
- enforces all invariants  
- validates the hash chain  
- ensures the `.qtrace` file is canonical  

Replay is the **authoritative verifier** of qCompute.
