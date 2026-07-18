# 🌀 Loophole Overlay (RTT Minimal Edition)

The Loophole Overlay is a diagnostic layer applied on top of the Resonance Atlas to reveal:
- corridor discontinuities  
- drift pockets  
- unbounded ranges  
- regime mismatches  
- missing substrate declarations  

It is used during harvesting, validation, and scanner visualization.

---

## 🔍 What Counts as a Loophole?

A loophole is any region where:
- the declared frequency range exceeds its RTT corridor  
- the substrate is undefined or ambiguous  
- the phase cannot be mapped  
- the resonance budget is violated  
- drift accumulates faster than correction  

---

## 🧩 Overlay Structure

Each loophole is represented as:

```json
{
  "id": "loophole_x",
  "phase": "III",
  "type": "corridor_gap",
  "description": "Frequency range extends beyond ecological corridor.",
  "severity": "medium",
  "suggested_fix": "Re-evaluate substrate or split into sub-corridors."
}
