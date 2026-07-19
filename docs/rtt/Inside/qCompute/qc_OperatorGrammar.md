# qCompute — Operator Grammar  
**File:** qc_OperatorGrammar.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **formal grammar**, **argument rules**, and **legality semantics** for all qCompute operators.

The grammar is:

- minimal  
- deterministic  
- environment‑aware  
- backend‑aware  
- drift‑aware  
- replay‑safe  

qCompute computes **structure**, not amplitudes.

---

# 1. Operator Namespace

Operators belong to five families:

| Family | Tier | Examples |
|--------|------|----------|
| **r1** (primitive) | r1 | `x`, `y`, `z`, `h`, `s`, `t` |
| **r2** (composite) | r2 | `cx`, `cz`, `swap` |
| **r3** (pulse) | r3 | `pulse` |
| **measurement** | special | `measure` |
| **meta** | meta | `barrier`, `flush` |

Each operator has:

- name  
- tier  
- drift characteristic  
- backend requirement  
- environment legality  

---

# 2. Formal Grammar

### 2.1 Operator Invocation

```
<operator> "(" <args> ")"
```

### 2.2 Arguments

```
<args> ::= <arg> | <arg> "," <args>
<arg>  ::= <name> "=" <value>
```

### 2.3 Names

```
<name> ::= /[a-zA-Z_][a-zA-Z0-9_]*/
```

### 2.4 Values

```
<value> ::= <int> | <float> | <bool> | <string>
```

### 2.5 QuBits

```
q, q1, q2 ∈ ℕ
```

---

# 3. Operator Legality Rules

Each operator is validated against:

1. grammar  
2. argument correctness  
3. environment legality  
4. tier legality  
5. backend legality  
6. token requirements  
7. archive terminality  

If invalid:

```
allowed: false
reason: "<canonical reason>"
```

Canonical reasons:

- `"invalid grammar"`
- `"invalid arguments"`
- `"illegal in environment"`
- `"backend mismatch"`
- `"backend illegal in environment"`
- `"tier decrease inside frame"`
- `"token required"`
- `"archive terminal"`
- `"illegal transition"`

---

# 4. Tier Semantics

### r1 (primitive)

- allowed in sandbox + production  
- low drift  
- backend: `local-sim`  
- may reuse frame  

### r2 (composite)

- allowed in sandbox + production  
- medium drift  
- backend: `hybrid-sim`  
- **tier escalation** → new frame  

### r3 (pulse)

- **production only**  
- **token required**  
- high drift  
- backend: `hardware-qpu-2`  
- always opens new frame  

### measurement

- allowed in sandbox + production  
- forces **tier decrease**  
- forces **new frame**  

### meta

- allowed in sandbox + production  
- zero drift  
- always opens new frame  

---

# 5. Backend Legality

| Backend | Allowed Tiers | Environments |
|---------|---------------|--------------|
| `local-sim` | r1 | sandbox, production |
| `hybrid-sim` | r1, r2 | sandbox, production |
| `hardware-qpu-2` | r3 | production only |

Archive is **terminal** and forbids all operators.

---

# 6. Environment Legality

| Environment | Allowed Tiers | Notes |
|-------------|---------------|-------|
| sandbox | r1, r2 | relaxed drift |
| production | r1, r2, r3 | strict drift, tokens required for r3 |
| archive | none | terminal |

Transitions:

- sandbox → production (token required)  
- production → archive (token required)  
- archive → (forbidden)  

---

# 7. Drift Semantics

Each operator has a drift characteristic:

| Tier | Drift |
|------|--------|
| r1 | low |
| r2 | medium |
| r3 | high |
| measurement | reset |
| meta | zero |

Drift overflow:

- closes current frame  
- opens new frame  
- routes operator into new frame  

---

# 8. Frame Semantics

A frame is valid if:

- tier is monotonic (no decrease)  
- backend is consistent  
- drift ≤ drift bound  
- environment is legal  

Triggers for new frame:

- first operator  
- tier escalation  
- tier decrease  
- r3 operator  
- drift overflow  
- meta operator  
- environment transition  

---

# 9. Capture Semantics

Each operator produces:

```
operator:
  op_id: "<id>"
  name: "<operator>"
  params: {...}
  validation: {...}
  routing: {...}
  drift: {...}
  timestamp: "<iso8601>"
  hash_prev: "<sha256>"
  hash_self: "<sha256>"
```

All fields are required.

---

# 10. Replay Semantics

Replay verifies:

- grammar  
- tier monotonicity  
- backend legality  
- environment legality  
- drift bounds  
- transition legality  
- hash chain integrity  
- canonical field presence  

Replay is deterministic and read‑only.

---

# 11. Invariants

1. grammar must be valid  
2. arguments must be valid  
3. environment must allow tier  
4. backend must match tier  
5. r3 requires token  
6. measurement forces new frame  
7. meta forces new frame  
8. drift must not exceed bound  
9. archive is terminal  
10. hash chain must be valid  

---

# Summary

The Operator Grammar defines:

- operator namespace  
- formal grammar  
- argument rules  
- tier semantics  
- backend legality  
- environment legality  
- drift + frame semantics  
- capture + replay invariants  

This grammar is the **foundation** of qCompute.
