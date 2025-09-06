function initForces() {
  const container = document.getElementById('lattice-container');
  const sphere = document.createElement('div');
  sphere.id = 'gravity-sphere';
  container.appendChild(sphere);

  for (let i = 0; i < 3; i++) {
    const orbit = document.createElement('div');
    orbit.className = `force-orbit color-${i}`;
    orbit.innerText = `∑${i}`;
    container.appendChild(orbit);
  }
}
