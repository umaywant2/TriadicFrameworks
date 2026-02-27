## 2. Logical entry point for RTT‑Inside (phase‑1 overlay)

We want **maximum leverage with minimal intrusion**. That means:

- Don’t touch raw radar/ADS‑B hardware.  
- Don’t rewrite the fusion engine (yet).  
- **Attach at the “track bus” and the HMI.**

### 🎯 Ideal insertion points

1. **Track stream tap (middleware):**
   - Subscribe to fused track updates (position, velocity, altitude, intent, quality).
   - Compute **RTT‑Inside resonance metrics**:
     - Corridor stability score  
     - Drift risk index  
     - Conflict resonance index (pairwise/group)  
   - Publish **augmented tracks** back onto a side‑channel or enriched topic.

2. **HMI overlay module:**
   - Read augmented tracks.  
   - Render:
     - Color‑coded stability  
     - Predictive “ghost” positions  
     - Subtle icons/contours for resonance drift  
   - No change to core display engine—just an overlay layer.

This gives us a **Phase‑1 RTT‑Inside variant** that:
- Uses existing data  
- Adds no new safety‑critical dependencies  
- Can be toggled on/off for trials  
- Is easy to A/B test in sim and replay
