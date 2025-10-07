// D3.js Remix Lineage Graph
const nodes = [
  { id: "Nawder", badge: "Legacy Architect" },
  { id: "umaywant2", badge: "Glyphstream Guardian" },
  { id: "EchoTesters", badge: "Resonance Initiate" }
];

const links = [
  { source: "umaywant2", target: "Nawder" },
  { source: "EchoTesters", target: "umaywant2" }
];

// Render with badge overlays, pulse trails, and hover tooltips
