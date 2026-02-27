### 5.2 HMI overlay: color & icon logic

Assume the existing display already draws tracks; we add a **thin overlay layer**.

```ts
// overlayViewModel.ts
import { AugmentedTrack } from "./types";

export interface OverlayStyle {
  pathColor: string;
  labelBadge?: "NORMAL" | "WATCH" | "ALERT";
  ghostPositions: { lat: number; lon: number }[];
}

export function buildOverlayStyle(track: AugmentedTrack): OverlayStyle {
  const { corridor_stability, advisory_level } = track.rtt;

  const pathColor =
    advisory_level === "ALERT"
      ? "#ff4d4f" // red
      : advisory_level === "WATCH"
      ? "#faad14" // amber
      : corridor_stability > 0.9
      ? "#52c41a" // bright green
      : "#1890ff"; // default blue

  // For phase 1, ghost positions can be simple extrapolations
  const ghostPositions = extrapolateGhosts(track);

  return {
    pathColor,
    labelBadge: advisory_level,
    ghostPositions
  };
}

function extrapolateGhosts(track: AugmentedTrack) {
  // Simple forward projection; real RTT-Inside uses resonance-time predictions.
  const ghosts = [];
  const stepSec = 60;
  for (let t = stepSec; t <= track.rtt.time_horizon_sec; t += stepSec) {
    ghosts.push({
      lat: track.position.lat, // stub
      lon: track.position.lon  // stub
    });
  }
  return ghosts;
}
```

Then, in the existing HMI rendering loop:

```ts
// hmiOverlayRenderer.ts
import { AugmentedTrack } from "./types";
import { buildOverlayStyle } from "./overlayViewModel";

export function renderOverlay(ctx: CanvasRenderingContext2D, tracks: AugmentedTrack[]) {
  tracks.forEach(track => {
    const style = buildOverlayStyle(track);

    // 1. Draw path with RTT color
    drawTrackPath(ctx, track, style.pathColor);

    // 2. Draw label badge (NORMAL/WATCH/ALERT)
    drawLabelBadge(ctx, track, style.labelBadge);

    // 3. Draw ghost positions (subtle dots or contours)
    drawGhosts(ctx, style.ghostPositions);
  });
}
```

This is **non‑intrusive**: if RTT
