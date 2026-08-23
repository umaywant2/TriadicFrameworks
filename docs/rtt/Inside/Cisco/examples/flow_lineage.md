# Flow Lineage Example (Cisco RTT/Inside)

## Purpose
Demonstrate how RTT‑Inside reconstructs **causal lineage** for a flow traversing
Cisco‑class systems. This example uses the base Cisco operator grammar and shows
how telemetry, management actions, and forwarding behavior combine into a single
RTT causal object.

---

# Scenario
A flow enters a Cisco fabric, triggers a policy‑driven management action, is
forwarded across multiple devices, and emits telemetry at each hop. RTT‑Inside
stitches these signals into a coherent lineage chain.

---

# Operator Chain

```
intent      = INTENT_CISCO(device_policy)
signal      = TIF_CISCO(telemetry)
mgmt        = MAN_CISCO(controller_action)
flow        = FFF_CISCO(flow_record)

resolved    = CRE_CISCO(intent, signal, mgmt)
lineage     = CSL_CISCO([resolved])
time        = CET_CISCO(lineage)

output      = RTT_CISCO(time)
```

---

# Interpretation (Student‑Readable)

- **INTENT_CISCO** captures the declared network intent (policy, routing objective).
- **TIF_CISCO** interprets telemetry emitted by the device during flow handling.
- **MAN_CISCO** records any management‑plane actions (controller updates, config pushes).
- **FFF_CISCO** extracts flow‑level causality (forwarding decisions, path selection).
- **CRE_CISCO** resolves these into a unified causal event.
- **CSL_CISCO** stitches events into a lineage chain.
- **CET_CISCO** applies antitime ordering for temporal clarity.
- **RTT_CISCO** produces the final causal object.

---

# Result
RTT reconstructs a clear causal narrative:

- why the flow was forwarded  
- which policies influenced it  
- what telemetry was emitted  
- what management actions occurred  
- how the final state emerged  

This is the foundation for higher‑level reasoning in grid‑scale, DSRSP‑aware, and
Internet3‑class substrates.
