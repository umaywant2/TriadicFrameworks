document.addEventListener("DOMContentLoaded", () => {
  const glyph = document.querySelector(".glyph");
  glyph.addEventListener("mouseover", () => {
    glyph.style.transform = "scale(1.05)";
  });
  glyph.addEventListener("mouseout", () => {
    glyph.style.transform = "scale(1)";
  });
});
