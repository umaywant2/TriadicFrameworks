(function () {
  const CONFIG = {
    WAVES: 3,
    CHIPS_PER_WAVE: 28,
    AMPLITUDES: [16, 22, 28],
    SPEEDS: [0.6, 0.45, 0.33],
    PHASE_OFFSETS: [0, Math.PI / 3, Math.PI * 0.66]
  };

  function makeChip(label, cls) {
    const span = document.createElement('span');
    span.className = `wave-chip ${cls}`;
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

  function buildWave(idx, width, height) {
    const holder = document.createElement('div');
    holder.className = `fluid-wave wave-${idx}`;
    holder.style.top = `${(idx + 0.5) * (height / CONFIG.WAVES)}px`;

    const chips = [];
    for (let i = 0; i < CONFIG.CHIPS_PER_WAVE; i++) {
      const n = i + 1;
      const eq = String.raw`\Psi_${idx+1}(x,t)=A\sin(kx-\omega t)+\frac{${n}}{${idx+1}}`;
      const chip = makeChip(eq, `w${idx}`);
      holder.appendChild(chip);
      chips.push(chip);
    }

    const amplitude = CONFIG.AMPLITUDES[idx];
    const speed = CONFIG.SPEEDS[idx];
    const phase0 = CONFIG.PHASE_OFFSETS[idx];

    function layout(t) {
      const tsec = t / 1000;
      for (let i = 0; i < chips.length; i++) {
        const frac = i / chips.length;
        const x = 24 + frac * (width - 48);
        const y = amplitude * Math.sin(2 * Math.PI * frac + phase0 - speed * tsec);
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
    root.className = 'overlay-layer overlay-fluids';
    const canvas = document.createElement('div');
    canvas.className = 'fluid-canvas';
    root.appendChild(canvas);

    const width = container.clientWidth || 1200;
    const height = canvas.clientHeight || 180;

    for (let w = 0; w < CONFIG.WAVES; w++) {
      canvas.appendChild(buildWave(w, width, height));
    }
    container.appendChild(root);
  }

  function initFluidsTest() {
    const container = document.querySelector('.fluids-test-zone');
    if (container) mount(container);
    console.log('[TFT] Fluids test initialized');
  }

  window.initFluidsTest = initFluidsTest;
  window.addEventListener('load', initFluidsTest);
})();
