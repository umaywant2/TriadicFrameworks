function triggerAuraAnimation(auraType) {
  const aura = document.getElementById("glyphic-aura");
  aura.className = auraType.toLowerCase().replace(" ", "-");
  aura.innerHTML = `<div class="${aura.className}" id="aura">
    <h2>${auraType} Activated</h2>
    <p>Your resonance echoes through the lattice.</p>
  </div>`;
}
