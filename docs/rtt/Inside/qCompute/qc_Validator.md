# qCompute — Validator Engine  
**File:** qc_Validator.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The Validator is the **legality gate** of qCompute.

Every operator, transition, and structural action must pass through the Validator before routing, framing, drift, or capture.

The Validator enforces:

- grammar correctness  
- argument correctness  
- environment legality  
- tier legality  
- backend legality  
- token requirements  
- archive terminality  
- transition legality  

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

The Validator ensures that all structural actions are:

- legal  
- deterministic  
- governed  
- replay‑verifiable  

If an operator is illegal, it is **captured but not executed**.

---

# 2. Validation Inputs

Validator receives:

```
operator:
  name
  tier
  params

session:
  environment
  tokens
  current_frame

backend_profiles:
  tier_binding
  environment_legal
```

All fields are required.

---

# 3. Validation Output

Validator returns:

```
allowed: true | false
reason: "<canonical-reason>"
```

Canonical reasons:

- "invalid grammar"
- "invalid arguments"
- "illegal in environment"
- "backend mismatch"
- "backend illegal in environment"
- "tier decrease inside frame"
- "token required"
- "archive terminal"
- "illegal transition"

No other strings are permitted.

---

# 4. Grammar Validation

Validator checks:

- operator name exists  
- operator belongs to a valid family  
- arguments match canonical schema  
- argument types are correct  

If invalid:

```
allowed: false
reason: "invalid grammar"
```

---

# 5. Argument Validation

Validator checks:

- required parameters present  
- parameter types correct  
- parameter ranges valid  

If invalid:

```
allowed: false
reason: "invalid arguments"
```

---

# 6. Environment Validation

Environment legality:

| Environment | Allowed Tiers |
|-------------|---------------|
| sandbox | r1, r2 |
| production | r1, r2, r3 |
| archive | none |

If operator is illegal in environment:

```
allowed: false
reason: "illegal in environment"
```

Archive always returns:

```
allowed: false
reason: "archive terminal"
```

---

# 7. Tier Validation

Validator checks:

- tier legality in environment  
- tier monotonicity inside frame  

Tier decrease inside a frame is illegal unless operator is measurement.

If illegal:

```
allowed: false
reason: "tier decrease inside frame"
```

---

# 8. Backend Validation

Backend is determined by tier:

| Tier | Backend |
|------|----------|
| r1 | local-sim |
| r2 | hybrid-sim |
| r3 | hardware-qpu-2 |

Validator checks:

- backend exists  
- backend legal in environment  

If illegal:

```
allowed: false
reason: "backend illegal in environment"
```

---

# 9. Token Validation

Tokens required for:

- r3 operators  
- sandbox → production transition  
- production → archive transition  

If missing:

```
allowed: false
reason: "token required"
```

---

# 10. Transition Validation

Legal transitions:

```
sandbox → production
production → archive
```

All others are illegal:

```
allowed: false
reason: "illegal transition"
```

Archive is terminal:

```
allowed: false
reason: "archive terminal"
```

---

# 11. Measurement Validation

Measurement forces:

- tier decrease  
- new frame  

Measurement is always legal unless environment is archive.

---

# 12. Meta Operator Validation

Meta operators (`barrier`, `flush`) are always legal unless environment is archive.

Meta operators always:

- open new frame  
- reset drift  

---

# 13. Drift Validation (Pre‑Routing)

Validator does **not** compute drift, but it checks:

- drift metadata exists  
- drift values are numeric  
- drift does not exceed impossible bounds  

Drift overflow is handled by Router + Frame Manager.

---

# 14. Capture Integration

Validator emits:

```
validation:
  allowed: true|false
  reason: "<canonical-reason>"
```

This metadata is required for every operator.

---

# 15. Replay Verification

Replay re‑validates:

- grammar  
- arguments  
- environment legality  
- tier legality  
- backend legality  
- token requirements  
- transition legality  
- archive terminality  

Replay must confirm:

- Validator decisions match canonical rules  
- no illegal operators were executed  
- illegal operators were captured correctly  

Replay is deterministic and read‑only.

---

# 16. Invariants

1. grammar must be valid  
2. arguments must be valid  
3. environment must allow tier  
4. backend must be legal  
5. r3 requires token  
6. transitions require token  
7. archive forbids all operators  
8. tier must not decrease inside a frame  
9. measurement is the only legal tier decrease  
10. meta operators always legal (except archive)  
11. illegal operators are captured but not executed  

---

# 17. Summary

The Validator ensures:

- structural legality  
- deterministic governance  
- environment correctness  
- backend correctness  
- tier correctness  
- token correctness  
- transition correctness  

Validator is the **first and strictest gate** of qCompute.
