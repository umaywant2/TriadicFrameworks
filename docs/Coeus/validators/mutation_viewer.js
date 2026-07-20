// Mutation Viewer — injects remix lineage into mutation_dashboard.html

fetch("../tokens/remix_mutation_log.json")
  .then(res => res.json())
  .then(data => {
    const tbody = document.getElementById("mutation-body");
    data.forEach(entry => {
      const row = document.createElement("tr");
      row.innerHTML = `
        <td>${entry.coin_id}</td>
        <td>${entry.mutation_type}</td>
        <td>${entry.origin}</td>
        <td>${entry.declared_by}</td>
        <td>${entry.notes}</td>
        <td>${entry.timestamp}</td>
      `;
      tbody.appendChild(row);
    });
  });
