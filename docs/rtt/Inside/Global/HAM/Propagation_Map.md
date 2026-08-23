# 📡 **RTT/Inside: Resonance‑Aware Propagation Map (Mockup)**  
*Field Display — HF / VHF / UHF Stability + Drift Forecast*

```
*
┌──────────────────────────────────────────────────────────────────────────────┐
│                     RESONANCE‑AWARE PROPAGATION MAP (RTT/Inside)             │
│                           Region: Upper Midwest / Great Lakes                │
│                           Timestamp: 2026‑01‑08 13:00Z                       │
└──────────────────────────────────────────────────────────────────────────────┘

  Stability Legend:   🟢 Stable   🟡 Watch   🟠 Degrading   🔴 Unstable
  Drift Vectors:      → low drift   ⇢ moderate drift   ⇢⇢ high drift

────────────────────────────────────────────────────────────────────────────────

MAP OVERLAY (HF + VHF + TERRAIN COHERENCE)
────────────────────────────────────────────────────────────────────────────────

                 (NORTH)
                     ↑
        ┌─────────────────────────────────────────────────┐
        │   🟢 40m NVIS Corridor (Stable)                │
        │   Light drift: →                                │
        │                                                 │
        │   🟡 20m Skip Zone Forming                      │
        │   Drift vectors: ⇢⇢ toward SE                  │
        │                                                 │
        │   Terrain Shadow (VHF):                         │
        │      Region: Huron Ridge                        │
        │      Status: 🟠 Degrading                       │
        │      Note: Move 30m east for LOS recovery       │
        │                                                 │
        │   UHF Repeater Nodes:                           │
        │      RPT‑12: 🟢 Stable                         │
        │      RPT‑07: 🟡 Load rising                    │
        │      RPT‑03: 🔴 Unstable (drift interference)  │
        └─────────────────────────────────────────────────┘
                     ↓
                 (SOUTH)

────────────────────────────────────────────────────────────────────────────────

BAND‑BY‑BAND RESONANCE STATUS
────────────────────────────────────────────────────────────────────────────────

 HF Bands:
   • 80m: 🟢 Stable — local SAR ideal, NVIS strong
   • 40m: 🟢 Stable — best for regional comms (2–6 hr window)
   • 20m: 🟡 Watch — solar drift increasing, skip zone expanding
   • 10m: 🔴 Unstable — sporadic‑E only, avoid for ops

 VHF/UHF:
   • 2m simplex: 🟢 Stable east of ridge, 🟠 west side degrading
   • 70cm: 🟡 Watch — temperature inversion causing ducting
   • Airband (AM): 🟢 Stable — clear path to ATC sector 12

────────────────────────────────────────────────────────────────────────────────

CROSS‑DOMAIN COHERENCE (AIR ↔ HAM ↔ SAR)
────────────────────────────────────────────────────────────────────────────────

   • ATC Sector 12 → SAR Team Bravo:
       Path: 🟢 Stable  
       Drift forecast: minimal for 90 min

   • SAR Team Bravo → Command Post:
       Path: 🟠 Degrading  
       Recommendation: shift 15m north to regain VHF LOS

   • HF Relay (HAM) → State EOC:
       Path: 🟢 Stable  
       Best band: 40m  
       Expected SNR: +12 dB

   • Satellite Relay (LEO‑01) → Ground Teams:
       Path: 🟡 Watch  
       Drift vectors: ⇢ toward SW due to ionospheric resonance

────────────────────────────────────────────────────────────────────────────────

RTT/Inside RECOMMENDATIONS
────────────────────────────────────────────────────────────────────────────────

   ✔ Primary Ops Channel: 146.52 (VHF simplex) — stable corridor east  
   ✔ Secondary: 40m HF — high coherence, strong NVIS  
   ✔ Avoid: 20m for next 45 min (skip zone drift)  
   ✔ Move Team Bravo 20–30m north to restore VHF clarity  
   ✔ Use RPT‑12 for repeater ops; avoid RPT‑03 (unstable)  

────────────────────────────────────────────────────────────────────────────────

NOTES
────────────────────────────────────────────────────────────────────────────────

   • Drift vectors updated every 30 seconds  
   • HF coherence recalculated every 5 minutes  
   • Terrain resonance model active (RTT/Inside v1.3)  
   • Cross‑domain sync: ATC / SAR / HAM / Space Relay aligned  

────────────────────────────────────────────────────────────────────────────────
```

---

## 🧭 What this mockup demonstrates

- **HF propagation stability** (NVIS, skip zones, solar drift)  
- **VHF/UHF terrain‑aware coherence**  
- **Repeater stability scoring**  
- **Cross‑domain alignment** (ATC ↔ SAR ↔ HAM ↔ satellite)  
- **Drift vectors** showing where signals will degrade  
- **RTT/Inside recommendations** for best channels and movement  

It’s exactly the kind of tactical map a HAM operator, SAR team, or ATC liaison could use in the field.
