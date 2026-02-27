## 3.2 Compute RTT‑Inside Metrics

The RTT‑Inside engine computes:

- **Corridor Stability Score** (0–1)  
- **Drift Risk Index** (0–1)  
- **Conflict Resonance Index** (0–1)  
- **Predictive Ghost Positions**  
- **Advisory Level** (NORMAL / WATCH / ALERT)

### Example RTT‑Inside engine call

```ts
const rtt = rttEngine.computeMetrics(track, neighbors);
return { ...track, rtt };
```

This produces an **AugmentedTrack** object.
