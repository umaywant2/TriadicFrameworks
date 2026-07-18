## 3. Phase‑2: Automation integration kit

Now we let automation consume RTT metrics.

### 3.1 Predictions + coherence outputs

```ts
// phase2/predictions.ts
import { AugmentedOrbitalTrack } from "../phase1/types";

export interface RttPrediction {
  objectId: string;
  predictedStates: {
    epoch: string;
    position_km: [number, number, number];
    velocity_km_s: [number, number, number];
  }[];
  drift_risk: number;
  conjunction_resonance: Record<string, number>;
}

export interface SystemCoherence {
  global_index: number; // 0–1
  shell_indices: Record<string, number>; // e.g. "LEO", "MEO", "GEO"
}
```

### 3.2 Phase‑2 engine wrapper

```ts
// phase2/rttAutomationAdapter.ts
import { AugmentedOrbitalTrack } from "../phase1/types";
import { RttPrediction, SystemCoherence } from "./predictions";

export class RttAutomationAdapter {
  predict(tracks: AugmentedOrbitalTrack[]): RttPrediction[] {
    // Stub: real impl uses RTK-like propagation
    return tracks.map(t => ({
      objectId: t.objectId,
      predictedStates: [],
      drift_risk: t.rtt.corridor_conflict_risk,
      conjunction_resonance: {}
    }));
  }

  systemCoherence(tracks: AugmentedOrbitalTrack[]): SystemCoherence {
    const avg = tracks.length
      ? tracks.reduce((s, t) => s + t.rtt.orbital_stability, 0) / tracks.length
      : 1;
    return { global_index: avg, shell_indices: {} };
  }
}
```

### 3.3 Automation integration loop

```ts
// phase2/automationLoop.ts
import { AugmentedOrbitalTrack } from "../phase1/types";
import { RttAutomationAdapter } from "./rttAutomationAdapter";

export class SpaceAutomation {
  private rtt = new RttAutomationAdapter();

  constructor(
    private subscribeAugmentedTracks: (cb: (tracks: AugmentedOrbitalTrack[]) => void) => void,
    private updateConjunctionEngine: (predictions) => void,
    private updateLaunchPlanner: (coherence) => void
  ) {}

  start() {
    this.subscribeAugmentedTracks((tracks) => {
      const predictions = this.rtt.predict(tracks);
      const coherence = this.rtt.systemCoherence(tracks);

      this.updateConjunctionEngine(predictions);
      this.updateLaunchPlanner(coherence);
    });
  }
}
```

**Outcome:** existing conjunction tools and launch planners get richer, resonance‑aware inputs without being rewritten.
