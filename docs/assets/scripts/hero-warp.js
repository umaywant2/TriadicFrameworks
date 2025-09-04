// === Equation Tornado Overlay ===
(function () {
  const HERO_SELECTOR = ".hero";
  const EQUATIONS = [
    "\\Psi(x,t) = A e^{i(kx - \\omega t)}",
    "\\Phi = \\int_0^{\\infty} S(\\lambda) R(\\lambda)\\, d\\lambda",
    "E = m R^2 \\phi^2",
    "\\tau = \\frac{dR}{d\\phi}",
    "X(\\omega) = \\int_{-\\infty}^{\\infty} x(t) e^{-i\\omega t} dt"
  ];

  let hero, canvas, ctx, particles = [];
  let angle = 0;

  function colors() {
    const dark = document.body.classList.contains("dark-mode");
    return dark ? "#FFD966" : "#C18400";
  }

  function makeParticle() {
    const eq = EQUATIONS[Math.floor(Math.random() * EQUATIONS.length)];
    const size = 14;
    const font = `${size}px Segoe UI, sans-serif`;

    const off = document.createElement("canvas");
    const octx = off.getContext("2d");
    octx.font = font;
    const m = octx.measureText(eq);
    off.width = m.width + 12;
    off.height = size + 12;

    octx.font = font;
    octx.textBaseline = "top";
    octx.fillStyle = colors();
    octx.globalAlpha = 0.8;
    octx.translate(6, 6);
    octx.fillText(eq, 0, 0);

    return {
      img: off,
      radius: Math.random() * 40 + 40, // distance from center
      height: Math.random() * 60 - 30, // vertical offset
      speed: Math.random() * 0.02 + 0.01,
      angle: Math.random() * Math.PI * 2
    };
  }

  function initParticles(count) {
    particles = [];
    for (let i = 0; i < count; i++) {
      particles.push(makeParticle());
    }
  }

  function step() {
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    const cx = width / 2;
    const cy = height / 2;

    ctx.clearRect(0, 0, width, height);

    particles.forEach(p => {
      p.angle += p.speed;
      const x = cx + Math.cos(p.angle) * p.radius;
      const y = cy + Math.sin(p.angle) * p.radius + p.height;
      ctx.drawImage(p.img, x, y);
    });

    requestAnimationFrame(step);
  }

  function init() {
    hero = document.querySelector(HERO_SELECTOR);
    if (!hero) return;

    canvas = document.createElement("canvas");
    canvas.className = "hero-tornado";
    hero.appendChild(canvas);
    ctx = canvas.getContext("2d");

    function resize() {
      const rect = hero.getBoundingClientRect();
      canvas.width = rect.width;
      canvas.height = rect.height;
      initParticles(12); // number of equations in tornado
    }
    window.addEventListener("resize", resize);
    resize();

    requestAnimationFrame(step);
  }

  document.addEventListener("DOMContentLoaded", init);
})();
