// Mint Viewer — injects mint attempts into mint_audit_dashboard.html

fetch("../tokens/mint_audit_log.json")
  .then(res => res.json())
  .then(data => {
    const tbody = document.getElementById("mint-body");
    data.forEach(entry => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${entry.coin_id}</td>
        <td>${entry.status}</td>
        <td>${entry.attempted_by}</td>
        <td>${entry.notes}</td>
        <td>${entry.timestamp}</td>
      `;
      tbody.appendChild(row);
    });
  });
