(function () {
  const CONFIG = {
    DIMENSIONS: 9,
    EQUATIONS_PER_DIM: 28,
    COLORS: ['c1', 'c3', 'c6', 'c9'],
    LOOP: [3, 1, 6, 3, 9, 6], // matches your harmonic packet logic
    SPEEDS: [0.6, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15],
    AMPLITUDES: [12, 14, 16, 18, 20, 22, 24, 26, 28]
  };

  function getColorClass(position) {
    let cycle = CONFIG.LOOP;
    let index = position % cycle.reduce((a, b) => a + b, 0);
    let sum = 0;
    for (let i = 0; i < cycle.length; i++) {
      sum += cycle[i];
      if (index < sum) return CONFIG.COLORS[i];
    }
    return CONFIG.COLORS[0];
  }

  function makeChip(label, cls) {
    const span = document.createElement('span');
    span.className = `tft-chip ${cls}`;
    try {
      if (window.katex) {
        span.innerHTML = window.katex.renderToString(label, { throwOnError: false });
      } else {
        span.textContent = label;
      }
    } catch {
      span.textContent = label;
    }
    return span;
  }

  function buildLane(dimIndex, width, height) {
    const holder = document.createElement('div');
    holder.className = `tft-lane dim-${dimIndex}`;
    holder.style.top = `${(dimIndex + 1) * 36}px`;

    const chips = [];
    for (let i = 0; i < CONFIG.EQUATIONS_PER_DIM; i++) {
      const label = String.raw`\mathcal{D}_{${dimIndex+1}}(t) = \sin(${i+1}t) + \frac{${i+1}}{${dimIndex+1}}`;
      const chip = makeChip(label, getColorClass(i));
      holder.appendChild(chip);
      chips.push(chip);
    }

    const amplitude = CONFIG.AMPLITUDES[dimIndex];
    const speed = CONFIG.SPEEDS[dimIndex];
    const phase = dimIndex * Math.PI / 4;

    function layout(t) {
      const tsec = t / 1000;
      for (let i = 0; i < chips.length; i++) {
        const frac = i / chips.length;
        const x = 24 + frac * (width - 48);
        const y = amplitude * Math.sin(2 * Math.PI * frac + phase - speed * tsec);
        const chip = chips[i];
        chip.style.left = `${x}px`;
        chip.style.top = `${y}px`;
      }
      requestAnimationFrame(layout);
    }
    requestAnimationFrame(layout);
    return holder;
  }

  function mount(container) {
    const root = document.createElement('div');
    root.className = 'tft-harmonics-overlay';
    const width = container.clientWidth || 1200;
    const height = 360;

    for (let d = 0; d < CONFIG.DIMENSIONS; d++) {
      root.appendChild(buildLane(d, width, height));
    }

    container.appendChild(root);
  }

  function initTFTHarmonics() {
    const container = document.querySelector('.tft-harmonics-test');
    if (container) mount(container);
    console.log('[TFT] Harmonics initialized');
  }

  window.initTFTHarmonics = initTFTHarmonics;
  window.addEventListener('load', initTFTHarmonics);
})();
