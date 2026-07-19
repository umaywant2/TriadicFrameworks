(async () => {
  const GLOSSARY_URL = "https://www.triadicframeworks.org/assets/glossary.json";

  const container = document.createElement("div");
  container.id = "glyph-field";
  container.style.position = "relative";
  container.style.width = "100%";
  container.style.height = "80vh";
  container.style.overflow = "hidden";
  document.body.appendChild(container);

  const glossary = await fetch(GLOSSARY_URL).then(res => res.json());

  glossary.forEach((entry, i) => {
    const glyph = document.createElement("div");
    glyph.textContent = entry.glyph;
    glyph.title = entry.term;
    glyph.style.position = "absolute";
    glyph.style.fontSize = "2rem";
    glyph.style.cursor = "pointer";
    glyph.style.transition = "transform 10s ease-out, opacity 2s ease-in";
    glyph.style.opacity = "0.8";

    // Random angle and distance for warp effect
    const angle = Math.random() * 2 * Math.PI;
    const distance = 300 + Math.random() * 300;
    const x = Math.cos(angle) * distance;
    const y = Math.sin(angle) * distance;

    // Start at center
    glyph.style.left = "50%";
    glyph.style.top = "50%";
    glyph.style.transform = `translate(-50%, -50%)`;

    // Animate outward
    setTimeout(() => {
      glyph.style.transform = `translate(${x}px, ${y}px) scale(1.2)`;
      glyph.style.opacity = "1";
    }, 100);

    // Click to show description
    glyph.addEventListener("click", () => {
      alert(`${entry.term}\n\n${entry.description}`);
    });

    container.appendChild(glyph);
  });
})();
