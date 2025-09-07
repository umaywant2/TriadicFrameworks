// Frequencies: three bands; each band has two counter-flowing lanes.
// Color cadence: 1 color every 3 eqs, 3 colors every 6, 6 colors every 9.
// Mounts to test area and/or lattice overlay.

(function () {
  const CONFIG = {
    TEST_MODE: window.FFF_CONFIG?.TEST_MODE ?? true, // true: mount in test areas; false: lattice overlay
    EQUATION_COUNT: 36,
    BANDS: 3,
    LANES_PER_BAND: 2,
    // Speeds per lane index
    SPEEDS: ['slow', 'medium', 'fast'],
  };

  function colorClass(index) {
    if (index >= 9) return 'c9';
    if (index >= 6) return 'c6';
    if (index >= 3) return 'c3';
    return 'c1'; // base color
}

  function makeEq(label, i) {
    const span = document.createElement('span');
    span.className = `eq-chip ${colorClass(i)}`;
    // Prefer KaTeX if present
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

  function buildLane(eqLabels, speedClass) {
    // Duplicate content 2x for seamless marquee
    const lane = document.createElement('div');
    lane.className = `freq-lane ${speedClass}`;
    const doubled = eqLabels.concat(eqLabels);
    doubled.forEach((lbl, i) => lane.appendChild(makeEq(lbl, i + 1)));
    return lane;
  }

  function buildBand(index, widthPx) {
    const band = document.createElement('div');
    band.className = 'freq-band';
    // Generate equation labels for this band
    // Dual-flow: alternate signs to feel like biorhythm waves
    const eqs = Array.from({ length: CONFIG.EQUATION_COUNT }, (_, i) => {
      const n = i + 1;
      const phase = index + 1;
      return String.raw`\sin(${phase}t) + \frac{${n}}{${phase}}`;
    });
    // Two lanes with different speeds and opposite direction (using dir via CSS override)
    const laneA = buildLane(eqs, CONFIG.SPEEDS[(index + 0) % CONFIG.SPEEDS.length]);
    const laneB = buildLane(eqs.slice().reverse(), CONFIG.SPEEDS[(index + 1) % CONFIG.SPEEDS.length]);
    laneB.style.animationDirection = 'reverse';

    // Balance width so scroll feels natural
    laneA.style.minWidth = widthPx ? Math.ceil(widthPx * 2.2) + 'px' : '';
    laneB.style.minWidth = widthPx ? Math.ceil(widthPx * 2.2) + 'px' : '';

    band.appendChild(laneA);
    band.appendChild(laneB);
    return band;
  }

  function mount(container) {
    const root = document.createElement('div');
    root.className = 'overlay-layer overlay-frequencies';
    // Build three bands
    const width = container.clientWidth || 1200;
    for (let b = 0; b < CONFIG.BANDS; b++) {
      root.appendChild(buildBand(b, width));
    }
    container.appendChild(root);
    return root;
  }

  function initFrequencies() {
    const targets = [];
    if (CONFIG.TEST_MODE) {
      document.querySelectorAll('.frequencies-animation').forEach(el => {
        targets.push(el);
      });
    } else {
      const lattice = document.getElementById('lattice-container');
      if (lattice) targets.push(lattice);
    }
    targets.forEach(mount);
    console.log('[FFF] Frequencies initialized', { test: CONFIG.TEST_MODE });
  }

  // Expose
  window.initFrequencies = initFrequencies;
})();
