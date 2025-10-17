fetch("docs/_meta/site_manifest.json")
  .then(response => response.json())
  .then(data => {
    const { content, projects, podcasts } = data.site_manifest;

    const renderList = (items, targetId) => {
      const container = document.getElementById(targetId);
      items.forEach(item => {
        const li = document.createElement("li");
        li.innerHTML = `<a href="${item.path}">${item.title}</a>`;
        container.appendChild(li);
      });
    };

    renderList(content, "content-list");
    renderList(projects, "projects-list");
    renderList(podcasts, "podcasts-list");
  })
  .catch(error => console.error("Manifest load error:", error));
