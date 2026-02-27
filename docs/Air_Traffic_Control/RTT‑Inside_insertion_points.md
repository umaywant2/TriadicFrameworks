## 3. RTT‑Inside insertion points (Space Force)

Same pattern as ATC:

1. **Track bus tap**  
   - Subscribe to **orbital track stream** (state vectors, covariances, IDs, object class).  
   - Subscribe to **launch/re‑entry corridor definitions** (volumes, timelines).

2. **RTT‑Inside engine (space variant)**  
   - Compute resonance‑time metrics for:
     - Orbital stability  
     - Conjunction resonance  
     - Corridor coherence (launch/re‑entry vs orbital traffic)  

3. **Overlay renderer**  
   - Add resonance‑aware overlays to existing SDA/launch displays.
