### 1. Types for the Corridor Trace

```ts
// types/corridor.ts
export type CorridorHeader = {
  type: "header";
  task_id: string;
  timestamp: number;
  corridor_spec: Record<string, any>;
};

export type CorridorStepEvent = {
  type: "step";
  step_id: number;
  parent_step_id: number | null;
  timestamp: number;
  action: string;
  observation: string;
  tool?: string;
  latency_ms?: number;
};

export type CorridorQEvent = {
  type: "q";
  step_id: number;
  semantic_drift: number;
  tool_entropy: number;
  latency_drift: number;
  branching_pressure: number;
  retry_ratio: number;
};

export type CorridorStatusEvent = {
  type: "status";
  step_id: number;
  corridor_status: "stable" | "warning" | "halted";
  violations: string[];
};

export type CorridorRewindEvent = {
  type: "rewind";
  from_step: number;
  to_step: number;
  timestamp: number;
};

export type CorridorFooter = {
  type: "footer";
  timestamp: number;
  final_status: string;
};

export type CorridorEvent =
  | CorridorHeader
  | CorridorStepEvent
  | CorridorQEvent
  | CorridorStatusEvent
  | CorridorRewindEvent
  | CorridorFooter;

export type CorridorTrace = {
  header: CorridorHeader;
  steps: CorridorStepEvent[];
  qHistory: CorridorQEvent[];
  statuses: CorridorStatusEvent[];
  rewinds: CorridorRewindEvent[];
  footer?: CorridorFooter;
};
```

---

### 2. API route that returns a parsed CTF

We can wire this later to disk or object storage.

```ts
// app/api/corridor/[id]/route.ts
import { NextResponse } from "next/server";
import type { CorridorTrace, CorridorEvent } from "@/types/corridor";

export async function GET(
  _req: Request,
  { params }: { params: { id: string } }
) {
  const id = params.id;

  // TODO: load from storage; for now, mock
  const raw = await fetch(`https://example.com/traces/${id}.ctf`).then(r =>
    r.text()
  );

  const events: CorridorEvent[] = raw
    .trim()
    .split("\n")
    .map((line) => JSON.parse(line));

  const trace: CorridorTrace = {
    header: events.find((e) => e.type === "header") as any,
    steps: events.filter((e) => e.type === "step") as any,
    qHistory: events.filter((e) => e.type === "q") as any,
    statuses: events.filter((e) => e.type === "status") as any,
    rewinds: events.filter((e) => e.type === "rewind") as any,
    footer: events.find((e) => e.type === "footer") as any,
  };

  return NextResponse.json(trace);
}
```

---

### 3. Next.js Corridor Viewer page

```tsx
// app/corridor/[id]/page.tsx
"use client";

import { useEffect, useState } from "react";
import type { CorridorTrace, CorridorStepEvent } from "@/types/corridor";
import { QMetricWaveformPanel } from "@/components/QMetricWaveformPanel";

export default function CorridorPage({ params }: { params: { id: string } }) {
  const { id } = params;
  const [trace, setTrace] = useState<CorridorTrace | null>(null);
  const [selectedStep, setSelectedStep] = useState<number | null>(null);

  useEffect(() => {
    fetch(`/api/corridor/${id}`)
      .then((r) => r.json())
      .then(setTrace)
      .catch(console.error);
  }, [id]);

  if (!trace) return <div>Loading corridor {id}…</div>;

  const { header, steps, qHistory, statuses } = trace;

  const statusByStep = new Map(
    statuses.map((s) => [s.step_id, s.corridor_status])
  );

  const onSelectStep = (s: CorridorStepEvent) => {
    setSelectedStep(s.step_id);
  };

  return (
    <div className="flex flex-col gap-4 p-4">
      <header className="border-b pb-2">
        <h1 className="text-xl font-semibold">
          Corridor: {header.task_id} ({id})
        </h1>
        <p className="text-sm text-gray-500">
          Max steps: {header.corridor_spec.max_steps} ·
          max drift: {header.corridor_spec.max_semantic_drift}
        </p>
      </header>

      <main className="grid grid-cols-3 gap-4">
        {/* Left: step timeline */}
        <section className="col-span-1 border rounded p-2 overflow-y-auto max-h-[70vh]">
          <h2 className="font-semibold mb-2 text-sm">Steps</h2>
          <ul className="space-y-1 text-xs">
            {steps.map((s) => {
              const status = statusByStep.get(s.step_id) ?? "stable";
              const isSelected = selectedStep === s.step_id;
              return (
                <li
                  key={s.step_id}
                  onClick={() => onSelectStep(s)}
                  className={`cursor-pointer rounded px-2 py-1 flex justify-between items-center ${
                    isSelected ? "bg-blue-100" : "hover:bg-gray-100"
                  }`}
                >
                  <div>
                    <div className="font-mono">
                      #{s.step_id} → {s.action}
                    </div>
                    <div className="text-gray-500">
                      tool: {s.tool ?? "n/a"} · latency:{" "}
                      {s.latency_ms ?? "?"} ms
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

        {/* Right: Q-metrics + details */}
        <section className="col-span-2 flex flex-col gap-4">
          <div className="border rounded p-2">
            <h2 className="font-semibold mb-2 text-sm">Q‑Metrics</h2>
            <QMetricWaveformPanel qHistory={qHistory} />
          </div>

          <div className="border rounded p-2">
            <h2 className="font-semibold mb-2 text-sm">Step Details</h2>
            {selectedStep == null ? (
              <p className="text-xs text-gray-500">
                Select a step from the left timeline.
              </p>
            ) : (
              (() => {
                const step = steps.find((s) => s.step_id === selectedStep);
                const q = qHistory.find((q) => q.step_id === selectedStep);
                if (!step) return null;
                return (
                  <div className="text-xs space-y-1">
                    <div className="font-mono">
                      #{step.step_id} (parent {step.parent_step_id ?? "∅"})
                    </div>
                    <div>Action: {step.action}</div>
                    <div>Observation: {step.observation}</div>
                    <div>Tool: {step.tool ?? "n/a"}</div>
                    <div>Latency: {step.latency_ms ?? "?"} ms</div>
                    {q && (
                      <div className="mt-2">
                        <div className="font-semibold">Q‑metrics</div>
                        <pre className="bg-gray-50 p-2 rounded">
                          {JSON.stringify(q, null, 2)}
                        </pre>
                      </div>
                    )}
                  </div>
                );
              })()
            )}
          </div>
        </section>
      </main>
    </div>
  );
}
```
