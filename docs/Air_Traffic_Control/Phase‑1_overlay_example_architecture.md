## 4. Phase‑1 overlay: example architecture

```text

[PSR/SSR/ADS-B/MLAT] 
        ↓
 [Surveillance Processor / Tracker]
        ↓  (fused tracks)
   [Track Bus / Message Broker]  →  [Recorder/Replay]
        ↓
   [RTT-Inside Engine]  ← (subscribes)
        ↓
 (augmented tracks with resonance metrics)
        ↓
   [Overlay Adapter]  →  [ATC Display HMI]
```
