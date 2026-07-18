// Forces: central sphere + three orbital bands with rotating equation chips.
// Each orbit uses its own color and radius; runs purely in CSS transforms.

(function () {
  const CONFIG = {
    TEST_MODE: window.FFF_CONFIG?.TEST_MODE ?? true,
    ORBITS: [
      { radius: 90,  chips: 12, speedSec: 18, cls: 'o0' },
      { radius: 130, chips: 16, speedSec: 26, cls: 'o1' },
      { radius: 170, chips: 20, speedSec: 34, cls: 'o2' },
    ],
  };

  function makeOrbitRing(r) {
    const ring = document.createElement('div');
    ring.className = 'orbit-ring';
    const d = r * 2;
    ring.style.width = `${d}px`;
    ring.style.height = `${d}px`;
    ring.style.marginLeft = `${-r}px`;
    ring.style.marginTop = `${-r}px`;
    return ring;
  }

  function makeOrbitTrack(radius, speedSec, chips, cls) {
    const track = document.createElement('div');
    track.className = 'orbit-track';
    track.style.setProperty('--radius', `${radius}px`);
    track.style.animationDuration = `${speedSec}s`;

    // Place chips around the orbit; CSS rotation spins the track
    for (let i = 0; i < chips; i++) {
      const theta = (i / chips) * 2 * Math.PI;
      const chip = document.createElement('span');
      chip.className = `eq-orbit-chip ${cls}`;
      const n = i + 1;
      const eq = String.raw`\mathcal{F}(${n})=\frac{GmM}{r^2}+${n}`;
      try {
        chip.innerHTML = window.katex
          ? window.katex.renderToString(eq, { throwOnError: false })
          : eq;
      } catch {
        chip.textContent = eq;
      }
      // Static pre-offset to distribute visually (rotation anim handles movement)
      chip.style.transform = `translate(-50%, -50%) rotate(${(theta * 180) / Math.PI}deg)`;
      track.appendChild(chip);
    }
    return track;
  }

  function buildStage(container) {
    const stage = document.createElement('div');
    stage.className = 'forces-stage';

    const sphere = document.createElement('div');
    sphere.className = 'gravity-sphere';
    stage.appendChild(sphere);

    CONFIG.ORBITS.forEach((o) => {
      stage.appendChild(makeOrbitRing(o.radius));
      const track = makeOrbitTrack(o.radius, o.speedSec, o.chips, o.cls);
      stage.appendChild(track);
    });

    return stage;
  }

  function mount(container) {
    const root = document.createElement('div');
    root.className = 'overlay-layer overlay-forces';
    root.appendChild(buildStage(container));
    container.appendChild(root);
    return root;
  }

  function initForces() {
    const targets = [];
    if (CONFIG.TEST_MODE) {
      document.querySelectorAll('.forces-animation').forEach(el => targets.push(el));
    } else {
      const lattice = document.getElementById('lattice-container');
      if (lattice) targets.push(lattice);
    }
    targets.forEach(mount);
    console.log('[FFF] Forces initialized', { test: CONFIG.TEST_MODE });
  }

  window.initForces = initForces;
})();
