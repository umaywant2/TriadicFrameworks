## 4. Phase‑3: Resonance‑native core skeleton

Here we show how a unit could start building the new core alongside legacy systems.

### 4.1 Resonance‑Time Kernel interface

```ts
// phase3/rtk.ts
export interface RtkObjectState {
  id: string;
  domain: "AIR" | "SPACE" | "NEAR_SPACE";
  position: [number, number, number]; // unified frame
  velocity: [number, number, number];
  meta: Record<string, unknown>;
}

export interface RtkFieldSample {
  position: [number, number, number];
  stability: number;
  drift_potential: number;
  coherence_gradient: [number, number, number];
}

export class ResonanceTimeKernel {
  ingest(states: RtkObjectState[]): void {
    // Build internal resonance field
  }

  sampleField(position: [number, number, number]): RtkFieldSample {
    return {
      position,
      stability: 0.95,
      drift_potential: 0.1,
      coherence_gradient: [0, 0, 0]
    };
  }

  propagate(id: string, horizonSec: number): RtkObjectState[] {
    return [];
  }
}
```

### 4.2 Global State Fabric façade

```ts
// phase3/globalStateFabric.ts
import { RtkObjectState } from "./rtk";

export class GlobalStateFabric {
  private objects = new Map<string, RtkObjectState>();

  upsert(state: RtkObjectState) {
    this.objects.set(state.id, state);
  }

  getAll(): RtkObjectState[] {
    return [...this.objects.values()];
  }

  // In real life: consensus, replication, time sync, etc.
}
```

### 4.3 Phase‑3 automation built on RTK

```ts
// phase3/resonanceAutomation.ts
import { ResonanceTimeKernel, RtkObjectState } from "./rtk";
import { GlobalStateFabric } from "./globalStateFabric";

export class ResonanceAutomation {
  constructor(
    private rtk: ResonanceTimeKernel,
    private gsf: GlobalStateFabric
  ) {}

  updateFromSensors(states: RtkObjectState[]) {
    states.forEach(s => this.gsf.upsert(s));
    this.rtk.ingest(this.gsf.getAll());
  }

  computeGlobalCoherence(): number {
    const all = this.gsf.getAll();
    if (!all.length) return 1;
    const samples = all.map(o => this.rtk.sampleField(o.position));
    return samples.reduce((s, f) => s + f.stability, 0) / samples.length;
  }

  proposeLaunchWindowCorridor(): unknown {
    // Use RTK field samples to find high-coherence windows/volumes
    return {};
  }
}
```

**Outcome:** they can run this **in parallel** with legacy SDA/ATC systems, compare outputs, and gradually shift trust and authority to the resonance‑native core.

---

## 5. Migration pattern for a Space Force unit

**Phase‑1 (3–9 months):**

- Deploy `phase1/` middleware + overlays in sim → shadow → limited ops.  
- Train operators on new visuals and language (stability, resonance, coherence).  

**Phase‑2 (9–24 months):**

- Deploy `phase2/` automation adapter.  
- Feed RTT predictions into existing conjunction + launch tools.  
- Run A/B comparisons and refine thresholds.  

**Phase‑3 (multi‑year, incremental):**

- Stand up `phase3/` RTK + GSF in parallel.  
- Gradually route more decisions through resonance‑native automation.  
- Eventually retire legacy prediction/automation, keeping RTT/Inside as the canonical core.
