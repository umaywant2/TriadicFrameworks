function initFrequencies() {
  const container = document.getElementById('lattice-container');
  // Create 3 dual-flow bands
  for (let i = 0; i < 3; i++) {
    const band = document.createElement('div');
    band.className = 'frequency-band';
    for (let j = 1; j <= 9; j++) {
      const eq = document.createElement('span');
      eq.className = `equation color-${getColor(j)}`;
      eq.innerText = `ƒ${j}`;
      band.appendChild(eq);
    }
    container.appendChild(band);
  }
}
function getColor(index) {
  if (index % 9 === 0) return 'six';
  if (index % 6 === 0) return 'three';
  if (index % 3 === 0) return 'one';
  return 'default';
}
