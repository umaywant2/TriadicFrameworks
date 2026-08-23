# Invariant Arc Example (Internet2 RTT/Inside)

## Purpose
Demonstrate how RTT‑Inside detects, evaluates, and stabilizes an **invariant arc**
within an Internet2‑class dimensional substrate. This example shows the full
regime‑aware chain: DSRSP scan → harmonic signature → invariant evaluation →
tier classification → lineage stitching.

---

# Scenario
A long‑haul flow crosses two timing regimes and one optical regime. During the
transition, a stable pattern emerges — a candidate **invariant arc**. RTT‑Inside
evaluates the arc, checks its stability, and determines whether it belongs in
the clear substrate or the Tier‑2 sandbox.

---

# Operator Chain

```
intent      = INTENT_I2(path_policy)
signal      = TIF_I2(telemetry)
mgmt        = MAN_I2(controller_action)
flow        = FFF_I2(flow_record)

signature   = DSRSP_AWARE_I2(path, sensors)
harmonic    = HARMONIC_SCAN_I2(flow, signature)
tier        = SUBSTRATE_CLASSIFY(harmonic, invariants)

decision    = INVARIANT_REGISTRY_I2(candidate_arc, evidence)
health      = SUBSTRATE_HEALTH_I2(regime_profiles, tier_distribution)

resolved    = CRE_I2(intent, signal, mgmt)
lineage     = CSL_I2([resolved, decision])
time        = CET_I2(lineage)

output      = RTT_I2(time)
```

---

# Interpretation (Student‑Readable)

### **1. Regime Scan**
`DSRSP_AWARE_I2` detects a stable signature across multiple regimes — a sign that
an invariant arc *might* be forming.

### **2. Harmonic Analysis**
`HARMONIC_SCAN_I2` confirms that the pattern is not a resonance burst or
regime‑crossing distortion.

### **3. Tier Classification**
`SUBSTRATE_CLASSIFY` assigns the flow to:

- **Tier‑0** if the arc is stable  
- **Tier‑1** if the arc is regime‑shifted but safe  
- **Tier‑2** if the arc is unstable and must be sandboxed  

### **4. Invariant Registry**
`INVARIANT_REGISTRY_I2` evaluates the candidate arc:

- **accepted** → added to the clear substrate  
- **sandboxed** → placed in the Resonance Chamber  
- **rejected** → discarded  

### **5. Substrate Health**
`SUBSTRATE_HEALTH_I2` ensures the substrate remains stable across regimes.

### **6. Causal Stitching**
RTT stitches:

- declared intent  
- telemetry  
- management actions  
- invariant evaluation  
- tier classification  

into a single causal lineage.

---

# Result
RTT produces a dimensional causal object describing:

- how the invariant arc emerged  
- how it was evaluated  
- whether it was accepted or sandboxed  
- how it affected substrate health  
- how it fits into the overall lineage  

This is the **canonical Internet2 invariant‑arc example** used for teaching
dimensional reasoning and regime‑aware causality.
