## 3.4 Render Overlays on Existing Displays

The overlay module reads augmented tracks and draws:

- Stability‑colored paths  
- Advisory badges  
- Predictive ghost positions  
- Drift contours  

### Example overlay logic

```ts
const style = buildOverlayStyle(augmentedTrack);

drawTrackPath(ctx, track, style.pathColor);
drawLabelBadge(ctx, track, style.labelBadge);
drawGhosts(ctx, style.ghostPositions);
```

This is **non‑intrusive**: if RTT‑Inside is offline, the overlay simply doesn’t draw.
