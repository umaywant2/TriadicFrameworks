## 1. Web‑based Corridor Viewer (React + D3)

**Goal:** Load a `.ctf`, show the corridor as a living object: steps, Q‑metrics, status, rewinds.

### 1.1. High‑level layout

- **Left:** step list + status badges  
- **Center:** Q‑metric waveform (D3)  
- **Right:** step details + lineage mini‑graph  

```tsx
// components/CorridorViewer.tsx
import { useState } from "react";
import type { CorridorTrace, CorridorStepEvent } from "@/types/corridor";
import { QMetricWaveformPanel } from "./QMetricWaveformPanel";
import { CorridorTimeline } from "./CorridorTimeline";
import { StepDetails } from "./StepDetails";

export function CorridorViewer({ trace }: { trace: CorridorTrace }) {
  const [selectedStep, setSelectedStep] = useState<number | null>(null);

  return (
    <div className="grid grid-cols-3 gap-4 h-full">
      <CorridorTimeline
        steps={trace.steps}
        statuses={trace.statuses}
        selectedStep={selectedStep}
        onSelectStep={setSelectedStep}
      />
      <div className="flex flex-col gap-4 col-span-2">
        <QMetricWaveformPanel qHistory={trace.qHistory} />
        <StepDetails
          steps={trace.steps}
          qHistory={trace.qHistory}
          selectedStep={selectedStep}
        />
      </div>
    </div>
  );
}
```

---

## 2. Corridor Trace Inspector (timeline panel)

Think “VSCode timeline” for a single corridor: events stacked over time.

### 2.1. Event timeline component

```tsx
// components/CorridorTimeline.tsx
import type {
  CorridorStepEvent,
  CorridorStatusEvent,
} from "@/types/corridor";

type Props = {
  steps: CorridorStepEvent[];
  statuses: CorridorStatusEvent[];
  selectedStep: number | null;
  onSelectStep: (id: number) => void;
};

export function CorridorTimeline({
  steps,
  statuses,
  selectedStep,
  onSelectStep,
}: Props) {
  const statusByStep = new Map(
    statuses.map((s) => [s.step_id, s.corridor_status])
  );

  return (
    <section className="border rounded p-2 overflow-y-auto">
      <h2 className="text-xs font-semibold mb-2">Corridor Timeline</h2>
      <ul className="space-y-1 text-xs">
        {steps.map((s) => {
          const status = statusByStep.get(s.step_id) ?? "stable";
          const isSelected = selectedStep === s.step_id;
          return (
            <li
              key={s.step_id}
              onClick={() => onSelectStep(s.step_id)}
              className={`cursor-pointer rounded px-2 py-1 flex justify-between ${
                isSelected ? "bg-blue-100" : "hover:bg-gray-100"
              }`}
            >
              <div>
                <div className="font-mono">
                  #{s.step_id} → {s.action}
                </div>
                <div className="text-gray-500">
                  tool: {s.tool ?? "n/a"} · {s.latency_ms ?? "?"} ms
                </div>
              </div>
              <span
                className={`text-[10px] px-1 py-0.5 rounded ${
                  status === "stable"
                    ? "bg-green-100 text-green-700"
                    : status === "warning"
                    ? "bg-yellow-100 text-yellow-700"
                    : "bg-red-100 text-red-700"
                }`}
              >
                {status}
              </span>
            </li>
          );
        })}
      </ul>
    </section>
  );
}
```

This *is* our “timeline panel”: scrollable, clickable, status‑aware.

---

## 3. Corridor Diff Tool (compare two `.ctf` files)

**Goal:** Show where two runs diverge—by step, Q‑metric, or status.

### 3.1. Diff model

```ts
// lib/corridorDiff.ts
import type { CorridorTrace } from "@/types/corridor";

export type CorridorDiffRow = {
  step: number;
  statusA?: string;
  statusB?: string;
  driftDelta?: number;
  entropyDelta?: number;
};

export function diffCorridors(a: CorridorTrace, b: CorridorTrace): CorridorDiffRow[] {
  const maxStep = Math.max(
    a.qHistory.length ? a.qHistory[a.qHistory.length - 1].step_id : 0,
    b.qHistory.length ? b.qHistory[b.qHistory.length - 1].step_id : 0
  );

  const qByStepA = new Map(a.qHistory.map((q) => [q.step_id, q]));
  const qByStepB = new Map(b.qHistory.map((q) => [q.step_id, q]));

  const statusByStepA = new Map(a.statuses.map((s) => [s.step_id, s.corridor_status]));
  const statusByStepB = new Map(b.statuses.map((s) => [s.step_id, s.corridor_status]));

  const rows: CorridorDiffRow[] = [];
  for (let step = 0; step <= maxStep; step++) {
    const qa = qByStepA.get(step);
    const qb = qByStepB.get(step);
    if (!qa && !qb) continue;

    rows.push({
      step,
      statusA: statusByStepA.get(step),
      statusB: statusByStepB.get(step),
      driftDelta:
        qa && qb ? qb.semantic_drift - qa.semantic_drift : undefined,
      entropyDelta:
        qa && qb ? qb.tool_entropy - qa.tool_entropy : undefined,
    });
  }
  return rows;
}
```

### 3.2. Diff view

```tsx
// components/CorridorDiffView.tsx
import type { CorridorTrace } from "@/types/corridor";
import { diffCorridors } from "@/lib/corridorDiff";

export function CorridorDiffView({
  left,
  right,
}: {
  left: CorridorTrace;
  right: CorridorTrace;
}) {
  const rows = diffCorridors(left, right);

  return (
    <div className="border rounded p-2 text-xs">
      <h2 className="font-semibold mb-2">Corridor Diff</h2>
      <table className="w-full border-collapse">
        <thead>
          <tr className="border-b">
            <th className="text-left">Step</th>
            <th>A status</th>
            <th>B status</th>
            <th>Δ drift</th>
            <th>Δ entropy</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r) => (
            <tr key={r.step} className="border-b">
              <td>#{r.step}</td>
              <td>{r.statusA ?? "-"}</td>
              <td>{r.statusB ?? "-"}</td>
              <td>{r.driftDelta?.toFixed(3) ?? "-"}</td>
              <td>{r.entropyDelta?.toFixed(3) ?? "-"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
```

Now we can put two runs side‑by‑side and *see* where they structurally diverge.

---

## 4. VCD‑style trace viewer for agent corridors

**Goal:** Treat Q‑metrics and status like digital signals over time.

We’ll render:

- X: step index  
- Y: stacked “tracks”:
  - semantic_drift (analog line)  
  - tool_entropy (analog line)  
  - corridor_status (discrete bands: stable/warning/halted)  

### 4.1. VCD‑style viewer component

```tsx
// components/CorridorVCDView.tsx
"use client";

import * as d3 from "d3";
import { useEffect, useRef } from "react";
import type { CorridorQEvent, CorridorStatusEvent } from "@/types/corridor";

type Props = {
  qHistory: CorridorQEvent[];
  statuses: CorridorStatusEvent[];
};

export function CorridorVCDView({ qHistory, statuses }: Props) {
  const ref = useRef<SVGSVGElement | null>(null);

  useEffect(() => {
    if (!ref.current || qHistory.length === 0) return;

    const svg = d3.select(ref.current);
    const width = Number(svg.attr("width")) || 800;
    const height = Number(svg.attr("height")) || 260;
    svg.selectAll("*").remove();

    const steps = qHistory.map((q) => q.step_id);
    const x = d3
      .scaleLinear()
      .domain(d3.extent(steps) as [number, number])
      .range([40, width - 10]);

    const yAnalog = d3.scaleLinear().domain([0, 1]).range([100, 20]);
    const yStatusTop = 140;
    const yStatusBottom = 240;

    const statusByStep = new Map(
      statuses.map((s) => [s.step_id, s.corridor_status])
    );

    // axes
    const xAxis = d3.axisBottom(x).ticks(8).tickFormat((d) => `#${d}`);
    svg
      .append("g")
      .attr("transform", `translate(0,${yStatusBottom})`)
      .call(xAxis as any)
      .selectAll("text")
      .style("font-size", "9px");

    const yAxis = d3.axisLeft(yAnalog).ticks(4);
    svg
      .append("g")
      .attr("transform", `translate(40,0)`)
      .call(yAxis as any)
      .selectAll("text")
      .style("font-size", "9px");

    // semantic_drift line
    const driftLine = d3
      .line<CorridorQEvent>()
      .x((d) => x(d.step_id))
      .y((d) => yAnalog(d.semantic_drift))
      .curve(d3.curveMonotoneX);

    svg
      .append("path")
      .datum(qHistory)
      .attr("fill", "none")
      .attr("stroke", "#1f77b4")
      .attr("stroke-width", 1.5)
      .attr("d", driftLine as any);

    // tool_entropy line
    const maxEntropy = d3.max(qHistory, (d) => d.tool_entropy) || 1;
    const entropyScale = d3.scaleLinear().domain([0, maxEntropy]).range([100, 20]);

    const entropyLine = d3
      .line<CorridorQEvent>()
      .x((d) => x(d.step_id))
      .y((d) => entropyScale(d.tool_entropy))
      .curve(d3.curveMonotoneX);

    svg
      .append("path")
      .datum(qHistory)
      .attr("fill", "none")
      .attr("stroke", "#ff7f0e")
      .attr("stroke-width", 1.2)
      .attr("d", entropyLine as any);

    // status bands (VCD‑style)
    const bandHeight = (yStatusBottom - yStatusTop) / 3;
    const statusColor = (s: string) =>
      s === "stable"
        ? "#e5f9e7"
        : s === "warning"
        ? "#fff7d6"
        : "#fde2e1";

    steps.forEach((step, i) => {
      const status = statusByStep.get(step) ?? "stable";
      const x0 = x(step);
      const x1 = i + 1 < steps.length ? x(steps[i + 1]) : x(step) + 8;

      svg
        .append("rect")
        .attr("x", x0)
        .attr("y", yStatusTop)
        .attr("width", x1 - x0)
        .attr("height", bandHeight)
        .attr("fill", statusColor(status))
        .attr("stroke", "#ddd")
        .attr("stroke-width", 0.5);
    });

    svg
      .append("text")
      .attr("x", 45)
      .attr("y", yStatusTop - 4)
      .text("corridor_status")
      .style("font-size", "9px")
      .style("fill", "#555");
  }, [qHistory, statuses]);

  return <svg ref={ref} width={800} height={260} className="border rounded" />;
}
```

This gives us a **VCD‑like panel**:

- top: analog “signals” (drift, entropy)  
- bottom: discrete status bands over time  

---

We now have, in blueprint form:

- a **web‑based Corridor Viewer** (React shell)  
- a **Trace Inspector** (timeline panel)  
- a **Diff Tool** (structural comparison of two runs)  
- a **VCD‑style trace viewer** (Q + status as signals)
