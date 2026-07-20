// Fluids: three slow-moving wave “streams” using a lightweight sine pass.
// Renders equation chips along sine paths updated via requestAnimationFrame.

(function () {
  const CONFIG = {
    TEST_MODE: window.FFF_CONFIG?.TEST_MODE ?? true,
    WAVES: 3,
    CHIPS_PER_WAVE: 28,
    AMPLITUDES: [16, 22, 28], // px
    SPEEDS: [0.6, 0.45, 0.33], // radians/sec
    PHASE_OFFSETS: [0, Math.PI / 3, Math.PI * 0.66],
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

    const amplitude = CONFIG.AMPLITUDES[idx % CONFIG.AMPLITUDES.length];
    const speed = CONFIG.SPEEDS[idx % CONFIG.SPEEDS.length];
    const phase0 = CONFIG.PHASE_OFFSETS[idx % CONFIG.PHASE_OFFSETS.length];

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
    return root;
  }

  function initFluids() {
    const targets = [];
    if (CONFIG.TEST_MODE) {
      document.querySelectorAll('.fluids-animation').forEach(el => targets.push(el));
    } else {
      const lattice = document.getElementById('lattice-container');
      if (lattice) targets.push(lattice);
    }
    targets.forEach(mount);
    console.log('[FFF] Fluids initialized', { test: CONFIG.TEST_MODE });
  }

  window.initFluids = initFluids;
})();
