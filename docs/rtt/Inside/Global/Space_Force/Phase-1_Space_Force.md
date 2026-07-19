## 2. Phase‑1: Space Force RTT/Inside overlay kit

### 2.1 Core types

```ts
// phase1/types.ts
export interface OrbitalTrack {
  objectId: string;
  name: string;
  class: "ACTIVE" | "DEBRIS" | "ROCKET_BODY";
  state: {
    frame: "ECI" | "ECEF";
    position_km: [number, number, number];
    velocity_km_s: [number, number, number];
  };
  epoch: string;
}

export interface Corridor {
  corridorId: string;
  type: "LAUNCH" | "REENTRY";
  time_window: { start: string; end: string };
}

export interface RttSpaceMetrics {
  orbital_stability: number;
  conjunction_resonance: number;
  corridor_conflict_risk: number;
  time_horizon_sec: number;
  advisory_level: "NORMAL" | "WATCH" | "ALERT";
}

export interface AugmentedOrbitalTrack extends OrbitalTrack {
  rtt: RttSpaceMetrics;
}
```

### 2.2 Phase‑1 engine + middleware

```ts
// phase1/rttSpaceEngine.ts
import { OrbitalTrack, Corridor, RttSpaceMetrics } from "./types";

export class RttSpaceEngine {
  constructor(private horizonSec: number = 86400) {}

  computeMetrics(
    track: OrbitalTrack,
    neighbors: OrbitalTrack[],
    corridors: Corridor[]
  ): RttSpaceMetrics {
    const stability = this.estimateOrbitalStability(track);
    const conjRes = this.estimateConjunctionResonance(track, neighbors);
    const corridorRisk = this.estimateCorridorConflict(track, corridors);

    const advisory =
      corridorRisk > 0.7 || conjRes > 0.7 ? "ALERT" :
      corridorRisk > 0.4 || conjRes > 0.4 ? "WATCH" :
      "NORMAL";

    return {
      orbital_stability: stability,
      conjunction_resonance: conjRes,
      corridor_conflict_risk: corridorRisk,
      time_horizon_sec: this.horizonSec,
      advisory_level: advisory
    };
  }

  private estimateOrbitalStability(track: OrbitalTrack): number { return 0.9; }
  private estimateConjunctionResonance(t: OrbitalTrack, n: OrbitalTrack[]): number { return 0.2; }
  private estimateCorridorConflict(t: OrbitalTrack, c: Corridor[]): number { return 0.1; }
}
```

```ts
// phase1/middleware.ts
import {
  OrbitalTrack,
  Corridor,
  AugmentedOrbitalTrack
} from "./types";
import { RttSpaceEngine } from "./rttSpaceEngine";

export class RttSpaceMiddleware {
  private engine = new RttSpaceEngine();
  private corridors: Corridor[] = [];

  constructor(
    private subscribeTracks: (cb: (tracks: OrbitalTrack[]) => void) => void,
    private subscribeCorridors: (cb: (corridors: Corridor[]) => void) => void,
    private publishAugmented: (tracks: AugmentedOrbitalTrack[]) => void
  ) {}

  start() {
    this.subscribeCorridors(c => { this.corridors = c; });

    this.subscribeTracks((tracks) => {
      const augmented = tracks.map(t => {
        const neighbors = tracks.filter(n => n.objectId !== t.objectId);
        const rtt = this.engine.computeMetrics(t, neighbors, this.corridors);
        return { ...t, rtt };
      });
      this.publishAugmented(augmented);
    });
  }
}
```

### 2.3 Phase‑1 overlay hook

```ts
// phase1/overlay.ts
import { AugmentedOrbitalTrack } from "./types";

export interface OverlayStyle {
  trackColor: string;
  haloRadius: number;
  labelBadge: "NORMAL" | "WATCH" | "ALERT";
}

export function buildOverlayStyle(track: AugmentedOrbitalTrack): OverlayStyle {
  const { orbital_stability, advisory_level } = track.rtt;

  const trackColor =
    advisory_level === "ALERT" ? "#ff4d4f" :
    advisory_level === "WATCH" ? "#faad14" :
    orbital_stability > 0.9 ? "#52c41a" :
    "#1890ff";

  const haloRadius = 1 + (1 - orbital_stability) * 4;

  return { trackColor, haloRadius, labelBadge: advisory_level };
}
```

**Outcome:** Space Force unit gets overlays in their SDA/launch displays with zero impact on core tools.
