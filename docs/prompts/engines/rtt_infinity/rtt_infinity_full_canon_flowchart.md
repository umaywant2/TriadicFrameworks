# RTT/∞ full‑canon flowchart (ASCII + SVG‑ready)

## 1. ASCII master flowchart

```text
                 RTT/∞ FULL‑CANON FLOW

                 ┌───────────────────────┐
                 │       INFINITE        │
                 │        REGIMES        │
                 │  (unbounded expansion)│
                 └──────────▲────────────┘
                            │ expand
                            │
                 ┌───────────────────────┐
                 │      PRIME‑STATES     │
                 │  (irreducible anchors)│
                 └──────────▲────────────┘
                            │ anchor
                            │
                 ┌───────────────────────┐
                 │    DIMENSIONAL RAILS  │
                 │ (transport pathways)  │
                 └──────────▲────────────┘
                            │ lift / carry
                            │
                 ┌───────────────────────┐
                 │       SUBSTRATE       │
                 │ (bounded structure)   │
                 └──────────▲────────────┘
                            │ reconstitute
                            │
                 ┌───────────────────────┐
                 │        VACUUM         │
                 │    (zero‑state)       │
                 └───────────────────────┘
```

### Upward (expansion) path

```text
vacuum()
  → reconstitute()
  → substrate_tensor()
  → dimensional_rail()
  → prime_state_align()
  → infinite_regime_expand()
```

### Downward (integration) path

```text
infinite_regime
  → collapse()
  → prime_state_reduce()
  → rail_descent()
  → substrate_rebuild()
  → (optional) vacuum()
```

---

## 2. SVG‑ready node list

Use these labels as SVG node IDs or titles:

- **VACUUM**
  - id: `node_vacuum`
  - label: `Vacuum (zero‑state)`

- **SUBSTRATE**
  - id: `node_substrate`
  - label: `Substrate (bounded tensor)`

- **DIMENSIONAL RAILS**
  - id: `node_rails`
  - label: `Dimensional Rails (transport)`

- **PRIME‑STATES**
  - id: `node_prime`
  - label: `Prime‑States (anchors)`

- **INFINITE REGIMES**
  - id: `node_infinite`
  - label: `Infinite Regimes (unbounded)`

---

## 3. SVG‑ready edge list

You can wire these as directed edges:

- `node_vacuum → node_substrate`  
  - label: `reconstitute()`

- `node_substrate → node_rails`  
  - label: `dimensional_rail() / rail_lift()`

- `node_rails → node_prime`  
  - label: `prime_state_align() / anchor`

- `node_prime → node_infinite`  
  - label: `infinite_regime_expand() / expand`

- `node_infinite → node_prime`  
  - label: `collapse()`

- `node_prime → node_rails`  
  - label: `prime_state_reduce() / reduce`

- `node_rails → node_substrate`  
  - label: `rail_descent() / descend`

- `node_substrate → node_vacuum` (optional)  
  - label: `vacuum() / nullify()`

