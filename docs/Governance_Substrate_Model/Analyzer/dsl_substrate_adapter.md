# DSL Substrate Adapter  
*A bridge between domain‑specific languages and the Governance Substrate Model (GSM)*

The DSL Substrate Adapter enables external policy DSLs, modeling languages, and structured rule systems to interface with the Governance Substrate Model. It translates domain‑specific constructs into GSM‑compatible structural artifacts such as vectors, invariant flags, drift signals, and basin classifications. This allows governance‑aware applications to integrate GSM reasoning without rewriting their internal logic.

---

### Purpose of the Adapter

The adapter provides a consistent way for any DSL to:

- express governance structures in substrate‑level terms  
- map DSL constructs to the five‑axis structural vector  
- evaluate invariants and physics rules  
- detect drift and structural tension  
- integrate Analyzer outputs into external tools  
- maintain coherence across domains  

It acts as a structural “interpreter” that ensures DSLs remain compatible with the GSM.

---

### Supported Input Types

The adapter accepts DSL constructs such as:

- rule blocks  
- policy definitions  
- institutional schemas  
- procedural flows  
- governance constraints  
- structural declarations  

Each construct is normalized and mapped into GSM‑compatible structures.

---

### Mapping Model

The adapter uses a three‑stage mapping process:

1. **DSL → Structural Claims**  
   Extracts governance‑relevant meaning from DSL syntax.

2. **Structural Claims → Axis Assignments**  
   Maps claims to the five axes:  
   - Centralization  
   - Method  
   - Oversight  
   - Access  
   - Timing  

3. **Axis Assignments → Structural Vector**  
   Produces a GSM‑compatible vector `[C, M, O, A, T]`.

Mapping rules are defined in `statement_mapping_rules.yaml` and extended here for DSL‑specific constructs.

---

### Example Mapping (Conceptual)

```
dsl_rule: "selection_method = preferential"
→ claim: "method: preferential"
→ axis: M = 1.0
```

```
dsl_rule: "oversight = independent_commission"
→ claim: "oversight: independent"
→ axis: O = 0.0
```

```
dsl_rule: "term_length = fixed"
→ claim: "timing: fixed"
→ axis: T = 0.0
```

These examples illustrate how DSL semantics become structural vectors.

---

### Integration with the Analyzer

Once the adapter produces a structural vector, it flows through the Analyzer pipeline:

- invariant evaluation  
- physics application  
- basin classification  
- drift detection  
- transition pathway analysis  
- narrative generation  

The adapter ensures that DSL‑originating structures behave identically to native GSM artifacts.

---

### Error Handling and Structural Validation

The adapter performs structural validation:

- missing axis assignments  
- contradictory rules  
- unsupported constructs  
- incoherent timing or oversight declarations  
- invalid combinations of method and access  

Errors are returned as structural diagnostics, not syntax errors.

---

### Extensibility

Developers can extend the adapter by adding:

- new DSL keywords  
- new mapping rules  
- domain‑specific structural constraints  
- custom invariant checks  
- adapters for multiple DSLs  

Extensions must preserve GSM coherence and avoid embedding ideology or policy preferences.

---

### Output Schema

The adapter returns:

- structural_vector  
- mapping_trace  
- invariant_flags  
- physics_forces  
- basin_classification  
- drift_signals  
- structural_narrative  

These outputs can be consumed by dashboards, simulators, or external DSL engines.

---

### Developer Notes

- Keep mapping rules transparent and explainable.  
- Avoid embedding political or normative assumptions.  
- Maintain compatibility with the Analyzer pipeline.  
- Document all DSL‑specific extensions.  
