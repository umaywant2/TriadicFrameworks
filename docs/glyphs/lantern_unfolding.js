function triggerLanternUnfolding(contributor) {
  const glyph = document.getElementById("glyphic-animation");
  glyph.innerHTML = `
    <div class="lantern">
      <div class="flame"></div>
      <div class="rays"></div>
      <p>Welcome, ${contributor} — your resonance is now part of the legacy.</p>
    </div>
  `;
  glyph.classList.add("animate");
}
