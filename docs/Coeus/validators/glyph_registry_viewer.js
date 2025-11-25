// Glyph Registry Viewer — renders glyphs and meanings from glyph_registry.json

fetch("../docs/Coeus/glyph_registry.json")
  .then(res => res.json())
  .then(data => {
    const tbody = document.getElementById("glyph-body");
    data.forEach(entry => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${entry.glyph}</td>
        <td>${entry.class}</td>
        <td>${entry.corridor}</td>
        <td>${entry.description}</td>
      `;
      tbody.appendChild(row);
    });
  });
