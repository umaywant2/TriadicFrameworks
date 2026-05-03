### 4. D3.js Q‑metric waveform panel

A small, focused component that plots multiple Q‑metrics over step index.

```tsx
// components/QMetricWaveformPanel.tsx
"use client";

import * as d3 from "d3";
import { useEffect, useRef } from "react";
import type { CorridorQEvent } from "@/types/corridor";

type Props = {
  qHistory: CorridorQEvent[];
};

const METRICS = [
  "semantic_drift",
  "tool_entropy",
  "latency_drift",
  "branching_pressure",
  "retry_ratio",
] as const;

export function QMetricWaveformPanel({ qHistory }: Props) {
  const ref = useRef<SVGSVGElement | null>(null);

  useEffect(() => {
    if (!ref.current || qHistory.length === 0) return;

    const svg = d3.select(ref.current);
    const width = Number(svg.attr("width")) || 600;
    const height = Number(svg.attr("height")) || 200;
    svg.selectAll("*").remove();

    const steps = qHistory.map((q) => q.step_id);
    const x = d3
      .scaleLinear()
      .domain(d3.extent(steps) as [number, number])
      .range([40, width - 10]);

    const y = d3.scaleLinear().domain([0, 1]).range([height - 20, 10]);

    const color = d3
      .scaleOrdinal<string>()
      .domain(METRICS as any)
      .range(d3.schemeCategory10);

    // axes
    const xAxis = d3.axisBottom(x).ticks(6).tickFormat((d) => `#${d}`);
    const yAxis = d3.axisLeft(y).ticks(4);

    svg
      .append("g")
      .attr("transform", `translate(0,${height - 20})`)
      .call(xAxis as any)
      .selectAll("text")
      .style("font-size", "9px");

    svg
      .append("g")
      .attr("transform", `translate(40,0)`)
      .call(yAxis as any)
      .selectAll("text")
      .style("font-size", "9px");

    // lines
    METRICS.forEach((metric) => {
      const line = d3
        .line<CorridorQEvent>()
        .x((d) => x(d.step_id))
        .y((d) => y((d as any)[metric] ?? 0))
        .curve(d3.curveMonotoneX);

      svg
        .append("path")
        .datum(qHistory)
        .attr("fill", "none")
        .attr("stroke", color(metric) as string)
        .attr("stroke-width", 1.5)
        .attr("d", line as any);
    });

    // legend
    const legend = svg
      .append("g")
      .attr("transform", `translate(50, 10)`)
      .selectAll("g")
      .data(METRICS)
      .enter()
      .append("g")
      .attr("transform", (_d, i) => `translate(${i * 110}, 0)`);

    legend
      .append("rect")
      .attr("width", 10)
      .attr("height", 10)
      .attr("fill", (d) => color(d) as string);

    legend
      .append("text")
      .attr("x", 14)
      .attr("y", 9)
      .text((d) => d)
      .style("font-size", "9px");
  }, [qHistory]);

  return (
    <svg
      ref={ref}
      width={600}
      height={220}
      className="border rounded bg-white"
    />
  );
}
```

This gives us:

- X‑axis: step index  
- Y‑axis: normalized Q‑metric value (0–1; we can rescale per metric later)  
- Multiple colored lines (one per Q‑metric)  
- A tiny legend  

---

We now have:

- A **Next.js corridor viewer** that feels like a logic analyzer for agents  
- A **D3 waveform panel** that shows the “health” of reasoning over time  
- A clean path to plug in our `.ctf` files and watch RTT‑Inside corridors breathe
