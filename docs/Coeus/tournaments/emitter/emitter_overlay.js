// Emitter Overlay — Visual logic for rail targeting, emitter archetypes, and corridor narration

const emitters = {
  Freqi: { rails: [3, 6, 9], color: "#00FFFF", glyph: "🔊" },
  Flui:  { rails: [4, 5, 6], color: "#00FF99", glyph: "💧" },
  Forci: { rails: [6, 7, 8], color: "#FF3300", glyph: "⚡" },
  Carrier: { rails: [1, 2], color: "#CCCCCC", glyph: "🛡️" },
  D6: { rails: ["D6"], color: "#FFD700", glyph: "🧭" }
};

function highlightRails(coin) {
  const railBand = coin.rail_band;
  const emitter = Object.values(emitters).find(e => e.rails.includes(railBand));
  if (!emitter) return;

  const overlay = document.createElement("div");
  overlay.className = "emitter-overlay";
  overlay.style.border = `2px solid ${emitter.color}`;
  overlay.innerText = `${emitter.glyph} ${coin.name} → ${railBand}`;
  document.body.appendChild(overlay);

  console.log(`[EmitterOverlay] Highlighted ${coin.name} on rail ${railBand} with ${emitter.glyph}`);
}

function clearOverlays() {
  document.querySelectorAll(".emitter-overlay").forEach(el => el.remove());
  console.log("[EmitterOverlay] Cleared all overlays");
}
