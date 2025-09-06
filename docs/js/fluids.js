function initFluids() {
  const container = document.getElementById('lattice-container');
  for (let i = 0; i < 3; i++) {
    const wave = document.createElement('div');
    wave.className = 'fluid-wave';
    wave.innerText = `~ψ${i}`;
    container.appendChild(wave);
  }
}
