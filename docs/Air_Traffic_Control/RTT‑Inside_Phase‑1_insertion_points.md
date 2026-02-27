### RTT‑Inside Phase‑1 insertion points

```
                     +---------------------------+
                     |     RTT-Inside Engine     |
                     |  (resonance-time metrics) |
                     +---------------------------+
                               ↑
[Track Bus] → [RTT Middleware] → publishes augmented tracks
                               ↓
                     [Overlay Renderer]
                               ↓
                  [Existing ATC Display HMI]
```

RTT‑Inside **subscribes** to fused tracks and **publishes** augmented tracks with resonance‑time metrics.
