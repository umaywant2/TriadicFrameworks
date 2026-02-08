// Emitter Overlay — renders glyph overlays and rail highlights

function highlightRails(coin) {
  const glyph = coin.glyph || "—";
  const railBand = coin.rail_band || "—";
  const cell = document.querySelector(`td:contains('${glyph}')`);
  if (cell) {
    cell.style.backgroundColor = "#f0f8ff";
    cell.title = `Rail Band: ${railBand}`;
  }
}
