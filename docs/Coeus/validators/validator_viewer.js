// Validator Viewer — injects scored coins into validator_dashboard.html

fetch("../score_trace.json")
  .then(res => res.json())
  .then(data => {
    const tbody = document.getElementById("validator-body");
    data.forEach(entry => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${entry.coin_id}</td>
        <td>${entry.score}</td>
        <td>${entry.ethics_passed ? "✅" : "❌"}</td>
        <td>${entry.realm_safe ? "D3/D4" : "⚠️"}</td>
        <td>${entry.emitter_sync ? "Synced" : "Unsynced"}</td>
        <td>${entry.glyph}</td>
        <td>${entry.remix_lineage.join(", ") || "—"}</td>
        <td>${entry.mutation_type || "—"}</td>
        <td>${entry.timestamp}</td>
      `;
      tbody.appendChild(row);
      highlightRails(entry);
    });
  });
