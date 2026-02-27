## 3. Conceptual data model for RTT‑Inside overlay

### 🧱 Base track (from ATC system)

```json
{
  "trackId": "AB123",
  "callsign": "AB123",
  "position": { "lat": 42.21, "lon": -83.35, "alt_ft": 32000 },
  "velocity": { "groundspeed_kt": 450, "heading_deg": 270, "roc_fpm": 0 },
  "source": ["PSR", "SSR", "ADS-B"],
  "timestamp": "2026-01-08T12:00:00Z"
}
```

### 🌐 RTT‑Inside augmentation

```json
{
  "trackId": "AB123",
  "rtt": {
    "corridor_stability": 0.92,        // 0–1
    "drift_risk": 0.08,                // 0–1
    "conflict_resonance": 0.15,        // 0–1
    "time_horizon_sec": 600,           // prediction horizon
    "advisory_level": "NORMAL"         // NORMAL / WATCH / ALERT
  }
}
```

The overlay module merges these into a **view model** for the operator.
