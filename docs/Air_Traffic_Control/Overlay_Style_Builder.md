## 6.2 Overlay Style Builder

```ts
export function buildOverlayStyle(track: AugmentedTrack) {
  const { corridor_stability, advisory_level } = track.rtt;

  const pathColor =
    advisory_level === "ALERT" ? "#ff4d4f" :
    advisory_level === "WATCH" ? "#faad14" :
    corridor_stability > 0.9 ? "#52c41a" :
    "#1890ff";

  return {
    pathColor,
    labelBadge: advisory_level,
    ghostPositions: extrapolateGhosts(track)
  };
}
```
