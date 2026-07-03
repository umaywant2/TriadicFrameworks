# qCompute — Environment Transition Engine  
**File:** qc_Transitions.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The Transition Engine governs movement between qCompute environments:

```
sandbox → production → archive
```

Transitions are **deterministic**, **token‑gated**, and **replay‑verifiable**.

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

The Transition Engine:

- validates environment transitions  
- enforces token requirements  
- closes the current frame  
- opens a new frame  
- updates drift bounds  
- updates backend legality  
- updates lineage  
- emits transition metadata for capture  
- verifies transitions during replay  

Transitions are structural governance events.

---

# 2. Environments

qCompute defines three environments:

| Environment | Description |
|-------------|-------------|
| **sandbox** | relaxed drift, r1/r2 allowed |
| **production** | strict drift, r1/r2/r3 allowed |
| **archive** | terminal, no operators allowed |

---

# 3. Legal Transitions

Only two transitions are legal:

```
sandbox → production
production → archive
```

All other transitions are illegal:

```
sandbox → archive      (forbidden)
production → sandbox   (forbidden)
archive → anything     (forbidden)
```

If illegal:

```
allowed: false
reason: "illegal transition"
```

---

# 4. Token Requirements

Transitions require tokens:

| Transition | Token Required |
|------------|----------------|
| sandbox → production | yes |
| production → archive | yes |
| archive → * | forbidden |

If token missing:

```
allowed: false
reason: "token required"
```

---

# 5. Transition Effects

A transition performs:

1. **close current frame**  
2. **update environment**  
3. **reset drift**  
4. **recompute backend legality**  
5. **open new frame**  
6. **append lineage entry**  
7. **emit transition metadata**  

Transitions always open a new frame.

---

# 6. Transition Metadata (Capture)

Each transition produces:

```
transition:
  from: "<env>"
  to: "<env>"
  token_used: "<token-id>"
  timestamp: "<iso8601>"
  hash_prev: "<sha256>"
  hash_self: "<sha256>"
```

All fields are required.

---

# 7. Routing Interaction

Router treats transitions as **strongest‑priority triggers**:

- always opens new frame  
- always resets drift  
- always rechecks backend legality  
- always updates environment  

Routing reason:

```
"environment-transition"
```

---

# 8. Drift Interaction

Transitions reset drift:

```
drift_total = 0
```

New drift bound is determined by the new environment:

| Environment | Drift Bound |
|-------------|-------------|
| sandbox | relaxed |
| production | strict |
| archive | immutable |

---

# 9. Backend Interaction

After transition:

- backend legality is rechecked  
- r3 becomes legal only in production  
- all backends become illegal in archive  

If backend becomes illegal:

- frame closes  
- new frame opens with legal backend  

---

# 10. Replay Verification

Replay reconstructs transitions by:

1. reading transition entries  
2. verifying legality  
3. verifying token usage  
4. verifying environment sequence  
5. verifying frame boundaries  
6. verifying drift resets  
7. verifying backend legality  
8. verifying hash chain integrity  

Replay must confirm:

- transitions match canonical rules  
- no illegal transitions occur  
- archive is terminal  

Replay is deterministic and read‑only.

---

# 11. Invariants

1. only sandbox → production → archive is legal  
2. transitions require tokens  
3. transitions always open new frames  
4. transitions reset drift  
5. transitions update backend legality  
6. transitions update environment  
7. archive forbids all operators  
8. archive is terminal  
9. hash chain must remain valid  

---

# 12. Summary

The Transition Engine provides:

- deterministic environment changes  
- token‑gated governance  
- drift resets  
- backend legality enforcement  
- frame segmentation  
- replay‑verifiable lineage  

Transitions are the **governance backbone** of qCompute.
