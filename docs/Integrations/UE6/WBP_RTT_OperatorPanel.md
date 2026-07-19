# WBP_RTT_OperatorPanel — Runtime Operator Inspector  
**RTT / Integrations / UE6 / UI**

A runtime UMG widget that displays live RTT operator values for any actor with an `URTTComponent`.

---

## Widget Name
`WBP_RTT_OperatorPanel`

## Parent Class
`UserWidget`

---

## Hierarchy

```
CanvasPanel
    ├── Border_Header
    │       └── TextBlock_Title ("RTT Operator Panel")
    ├── VerticalBox_Values
    │       ├── HorizontalBox_Phi
    │       │       ├── TextBlock_Label ("φ (Phi)")
    │       │       └── TextBlock_Value (bound)
    │       ├── HorizontalBox_Variance
    │       ├── HorizontalBox_Resonance
    │       └── HorizontalBox_Entropy
    └── Border_Footer
            └── TextBlock_TargetActor (bound)
```

---

## Variables

| Name | Type | Purpose |
|------|------|---------|
| `TargetActor` | Actor | Actor being inspected |
| `PhiValue` | float | φ operator output |
| `VarianceValue` | float | variance operator output |
| `ResonanceValue` | float | resonance amplitude |
| `EntropyValue` | float | entropy intensity |

---

## Bindings

- `TextBlock_Value_Phi` → `PhiValue`  
- `TextBlock_Value_Variance` → `VarianceValue`  
- `TextBlock_Value_Resonance` → `ResonanceValue`  
- `TextBlock_Value_Entropy` → `EntropyValue`  
- `TextBlock_TargetActor` → `TargetActor.DisplayName`

---

## Graph Logic

### Event: `Tick`
- If `TargetActor` has `URTTComponent`:
  - Call:
    - `RTT_ProbeResonance`
    - `RTT_TraceEntropy`
  - Update bound variables
- Redraw values

---

## Status
Ready for implementation.  
Fully aligned with the 2026 RTT Integrations standard.
