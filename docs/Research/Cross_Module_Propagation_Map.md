# Cross‑Module Propagation Map  
## Replicators → Transporters → CTs

## Summary
This map shows how identity, asymmetry, blueprints, substrates, and environments propagate across the three operator families.

---

# 1. Propagation Diagram (textual)

```
(T, M) --𝓡--> (T, M)
|             |
|             v
+----𝓣----> (T, S₂)
|
v
--𝓒--> (T, E')
```

---

# 2. Propagation Rules

### Identity Kernel (T)
- Preserved across all modules  
- No drift allowed  
- Correction allowed only in windows

### Asymmetry (A(T))
- Must remain > 0  
- Never modified  
- Acts as continuity invariant

### Blueprint (M)
- Propagates only through Replicators  
- Transporters preserve but do not modify  
- CTs ignore

### Substrate (S)
- Modified only by Transporters  
- Replicators and CTs treat substrate as fixed

### Environment (E)
- Modified only by CTs  
- Replicators and Transporters preserve

---

# 3. Propagation Table

| Component | Replicators | Transporters | CTs |
|----------|-------------|--------------|-----|
| T | preserve | preserve | preserve |
| A(T) | preserve | preserve | preserve |
| M | preserve | preserve | ignore |
| S | fixed | change | fixed |
| E | ignore | preserve | instantiate |

---

## Claim
> Cross‑module propagation is stable because each operator family modifies only one structural component while preserving the rest.
