# qCompute — Operator Catalog  
**File:** qc_Operators.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **complete operator catalog** for qCompute.

Operators are structural actions that pass through:

```
Validator → Router → Frame Manager → Drift Engine → Capture → Replay
```

qCompute computes **structure**, not amplitudes.

---

# 1. Operator Families

qCompute defines five operator families:

| Family | Tier | Examples | Notes |
|--------|------|----------|-------|
| **r1** (primitive) | r1 | `x`, `y`, `z`, `h`, `s`, `t` | low drift, local-sim |
| **r2** (composite) | r2 | `cx`, `cz`, `swap` | medium drift, hybrid-sim |
| **r3** (pulse) | r3 | `pulse` | high drift, hardware-qpu-2, token required |
| **measurement** | special | `measure` | tier decrease, new frame |
| **meta** | meta | `barrier`, `flush` | zero drift, new frame |

Each operator has:

- name  
- tier  
- parameter schema  
- drift characteristic  
- backend binding  
- environment legality  
- routing behavior  

---

# 2. r1 Operators (Primitive Tier)

r1 operators are **primitive structural actions**.

Backend: `local-sim`  
Environment: sandbox, production  
Drift: low  
Frame: may reuse frame  

### 2.1 Operator List

| Operator | Params | Description |
|----------|---------|-------------|
| `x` | `q: int` | Pauli‑X |
| `y` | `q: int` | Pauli‑Y |
| `z` | `q: int` | Pauli‑Z |
| `h` | `q: int` | Hadamard |
| `s` | `q: int` | Phase |
| `t` | `q: int` | T‑gate |

### 2.2 Schema

```
x(q=<int>)
y(q=<int>)
z(q=<int>)
h(q=<int>)
s(q=<int>)
t(q=<int>)
```

---

# 3. r2 Operators (Composite Tier)

r2 operators are **composite structural actions**.

Backend: `hybrid-sim`  
Environment: sandbox, production  
Drift: medium  
Frame: may reuse or open new frame (tier escalation, drift overflow)  

### 3.1 Operator List

| Operator | Params | Description |
|----------|---------|-------------|
| `cx` | `q1: int`, `q2: int` | Controlled‑X |
| `cz` | `q1: int`, `q2: int` | Controlled‑Z |
| `swap` | `q1: int`, `q2: int` | Swap |

### 3.2 Schema

```
cx(q1=<int>, q2=<int>)
cz(q1=<int>, q2=<int>)
swap(q1=<int>, q2=<int>)
```

---

# 4. r3 Operators (Pulse Tier)

r3 operators are **pulse‑level structural actions**.

Backend: `hardware-qpu-2`  
Environment: production only  
Drift: high  
Frame: always opens new frame  
Token: required  

### 4.1 Operator List

| Operator | Params | Description |
|----------|---------|-------------|
| `pulse` | `q: int`, `duration: float`, `amplitude: float` | Pulse operator |

### 4.2 Schema

```
pulse(q=<int>, duration=<float>, amplitude=<float>)
```

---

# 5. Measurement Operators

Measurement is a **tier‑decrease** operator.

Backend: `local-sim`  
Environment: sandbox, production  
Drift: reset  
Frame: always opens new frame  

### 5.1 Operator List

| Operator | Params | Description |
|----------|---------|-------------|
| `measure` | `q: int` | Structural measurement |

### 5.2 Schema

```
measure(q=<int>)
```

---

# 6. Meta Operators

Meta operators are **structural boundaries**.

Backend: same as current frame  
Environment: sandbox, production  
Drift: zero  
Frame: always opens new frame  

### 6.1 Operator List

| Operator | Params | Description |
|----------|---------|-------------|
| `barrier` | none | Frame boundary |
| `flush` | none | Frame boundary + drift reset |

### 6.2 Schema

```
barrier()
flush()
```

---

# 7. Operator Legality Summary

| Operator | Tier | Backend | Env | Token | Frame Action |
|----------|------|----------|------|--------|----------------|
| r1 | r1 | local-sim | sandbox, production | no | reuse |
| r2 | r2 | hybrid-sim | sandbox, production | no | reuse/new |
| r3 | r3 | hardware-qpu-2 | production | yes | new |
| measure | special | local-sim | sandbox, production | no | new |
| meta | meta | current | sandbox, production | no | new |

---

# 8. Routing Behavior

Routing reasons include:

- `"tier-binding"`  
- `"tier-escalation"`  
- `"tier-decrease"`  
- `"measurement"`  
- `"meta"`  
- `"r3-requires-new-frame"`  
- `"drift-overflow"`  
- `"environment-transition"`  
- `"token-required"`  

Operators always produce routing metadata.

---

# 9. Capture Metadata

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

# 10. Replay Verification

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
- hash chain integrity  

Replay must match capture exactly.

---

# 11. Invariants

1. r1 → local-sim  
2. r2 → hybrid-sim  
3. r3 → hardware-qpu-2  
4. r3 requires token  
5. r3 always opens new frame  
6. measurement always opens new frame  
7. meta always opens new frame  
8. tier must not decrease inside a frame  
9. drift must not exceed bound  
10. archive forbids all operators  

---

# 12. Summary

The Operator Catalog defines:

- operator families  
- tier assignments  
- backend binding  
- environment legality  
- drift characteristics  
- routing behavior  
- capture metadata  
- replay invariants  

Operators are the **structural actions** of qCompute.
