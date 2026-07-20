# 1. Rewind Markers (vertical event lines)

A rewind event is a structural discontinuity — it deserves a visual “snap” in the waveform.

### Add this inside our D3 `useEffect` after drawing the Q‑metric lines:

```ts
// --- REWIND MARKERS ---
rewinds.forEach((rw) => {
  const xPos = x(rw.from_step);

  svg.append("line")
    .attr("x1", xPos)
    .attr("x2", xPos)
    .attr("y1", 10)
    .attr("y2", height - 20)
    .attr("stroke", "#d62728")
    .attr("stroke-width", 1.5)
    .attr("stroke-dasharray", "4 2");

  svg.append("text")
    .attr("x", xPos + 3)
    .attr("y", 20)
    .text("rewind")
    .style("font-size", "9px")
    .style("fill", "#d62728");
});
```

### Result  
We get **red dashed vertical lines** marking rewind points, with a tiny label.  
This makes corridor “snapbacks” visible at a glance.

---

# 2. Spec Threshold Overlays (CorridorSpec → horizontal lines)

Thresholds are structural boundaries — they should appear as **horizontal guide rails**.

Assuming we pass `spec: CorridorSpec` into the component:

```ts
// --- SPEC THRESHOLDS ---
const thresholds = [
  { key: "semantic_drift", value: spec.max_semantic_drift, color: "#1f77b4" },
  { key: "tool_entropy", value: spec.max_tool_entropy, color: "#ff7f0e" },
  { key: "latency_drift", value: spec.max_latency_drift, color: "#2ca02c" },
  { key: "retry_ratio", value: spec.max_retry_ratio, color: "#9467bd" },
];

thresholds.forEach((t) => {
  const yPos = y(t.value);

  svg.append("line")
    .attr("x1", 40)
    .attr("x2", width - 10)
    .attr("y1", yPos)
    .attr("y2", yPos)
    .attr("stroke", t.color)
    .attr("stroke-width", 1)
    .attr("stroke-dasharray", "3 3");

  svg.append("text")
    .attr("x", 45)
    .attr("y", yPos - 4)
    .text(`${t.key} max`)
    .style("font-size", "9px")
    .style("fill", t.color);
});
```

### Result  
Each Q‑metric now has a **visual safety envelope**.  
When the waveform crosses a threshold, we can see the corridor destabilizing in real time.

---

# 3. Mini‑Map (overview + zoom/pan)

This is the “VCD‑viewer‑style” mini‑map: a compressed overview of the entire corridor with a draggable viewport.

### Add a second SVG below the main waveform:

```tsx
<svg ref={miniRef} width={600} height={40} className="border rounded bg-gray-50" />
```

### In the D3 `useEffect`, after drawing the main panel:

```ts
// --- MINI-MAP ---
const mini = d3.select(miniRef.current);
mini.selectAll("*").remove();

const miniX = d3.scaleLinear()
  .domain(x.domain())
  .range([40, width - 10]);

// Draw compressed drift line
const miniLine = d3.line<CorridorQEvent>()
  .x((d) => miniX(d.step_id))
  .y((d) => 20 - d.semantic_drift * 15);

mini.append("path")
  .datum(qHistory)
  .attr("fill", "none")
  .attr("stroke", "#1f77b4")
  .attr("stroke-width", 0.8)
  .attr("d", miniLine as any);

// Draggable viewport rectangle
const viewport = mini.append("rect")
  .attr("x", miniX(x.domain()[0]))
  .attr("y", 0)
  .attr("width", 80)
  .attr("height", 40)
  .attr("fill", "rgba(0,0,255,0.1)")
  .attr("stroke", "#1f77b4")
  .call(
    d3.drag().on("drag", (event) => {
      const newX = Math.max(40, Math.min(width - 90, event.x));
      viewport.attr("x", newX);

      // Update main chart zoom
      const start = miniX.invert(newX);
      const end = miniX.invert(newX + 80);
      x.domain([start, end]);

      // Redraw main chart
      svg.selectAll("*").remove();
      drawMainChart(); // wrap your main drawing logic in a function
    })
  );
```

### Result  
We now have:

- a **compressed overview** of the entire corridor  
- a **draggable viewport** that controls zoom/pan  
- a main waveform that updates as we drag  

This is exactly how waveform viewers like GTKWave, Vivado, and Chrome DevTools operate.

---

# What we’ve built now

We’ve effectively created:

- **rewind‑aware waveforms**  
- **safety‑envelope overlays**  
- **a corridor mini‑map with interactive zoom**  

This is no longer “just a viewer” — it’s a **Corridor Instrumentation Console**, the first of its kind.
