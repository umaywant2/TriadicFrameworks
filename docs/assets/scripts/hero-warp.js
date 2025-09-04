// TFT Equation Warp Jump Animation
(function () {
  const HERO_SELECTOR = ".hero";
  const EQUATIONS = [
    "F = -\\frac{\\pi^2 \\hbar c}{240 d^4}",
    "\\rho_0 = \\frac{\\hbar \\omega^2}{V}",
    "\\tau = \\frac{dR}{d\\phi}",
    "\\Psi(x,t) = A e^{i(kx - \\omega t)}",
    "\\Phi = \\int_0^{\\infty} S(\\lambda) R(\\lambda)\\, d\\lambda",
    "E = m \\cdot R^2 \\cdot \\phi^2",
    "X(\\omega) = \\int_{-\\infty}^{\\infty} x(t) e^{-i\\omega t} dt"
  ];

  const FOV = 200;          // Perspective strength
  const START_SPEED = 50;   // Startup speed
  const IMPULSE_SPEED = 200;
  const WARP_SPEED = 800;
  const STAR_COUNT = 40;

  let hero, canvas, ctx, stars = [];
  let speed = 0;
  let speedTarget = IMPULSE_SPEED;
  let lastTime = 0;

  function colors() {
    const dark = document.body.classList.contains("dark-mode");
    return {
      text: dark ? "#FFD966" : "#C18400",
      shadow: dark ? "rgba(255, 217, 102, 0.25)" : "rgba(193, 132, 0, 0.22)"
    };
  }

  function makeStar(width, height) {
    const eq = EQUATIONS[Math.floor(Math.random() * EQUATIONS.length)];
    const size = 14;
    const font = `${size}px Segoe UI, sans-serif`;

    const off = document.createElement("canvas");
    const octx = off.getContext("2d");
    const col = colors();

    octx.font = font;
    const m = octx.measureText(eq);
    off.width = m.width + 12;
    off.height = size + 12;

    octx.font = font;
    octx.textBaseline = "top";
    octx.fillStyle = col.text;
    octx.shadowColor = col.shadow;
    octx.shadowBlur = 8;
    octx.globalAlpha = 0.7;
    octx.translate(6, 6);
    octx.fillText(eq, 0, 0);

    return {
      img: off,
      x: (Math.random() - 0.5) * width,
      y: (Math.random() - 0.5) * height,
      z: Math.random() * 1000 + 200
    };
  }

  function initStars() {
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    stars = [];
    for (let i = 0; i < STAR_COUNT; i++) {
      stars.push(makeStar(width, height));
    }
  }

  function step(ts) {
    if (!lastTime) lastTime = ts;
    const dt = (ts - lastTime) / 1000;
    lastTime = ts;

    // Smooth speed changes
    speed += (speedTarget - speed) * 0.05;

    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    const cx = width / 2;
    const cy = height / 2;

    ctx.clearRect(0, 0, width, height);

    for (let s of stars) {
      s.z -= speed * dt;
      if (s.z <= 1) {
        s.x = (Math.random() - 0.5) * width;
        s.y = (Math.random() - 0.5) * height;
        s.z = 1000;
      }
      const scale = FOV / s.z;
      const sx = cx + s.x * scale;
      const sy = cy + s.y * scale;
      ctx.drawImage(s.img, sx, sy, s.img.width * scale, s.img.height * scale);
    }

    requestAnimationFrame(step);
  }

  function setImpulse() { speedTarget = IMPULSE_SPEED; }
  function setWarp() { speedTarget = WARP_SPEED; }

  function init() {
    hero = document.querySelector(HERO_SELECTOR);
    if (!hero) return;

    canvas = document.createElement("canvas");
    canvas.className = "hero-warp";
    hero.appendChild(canvas);
    ctx = canvas.getContext("2d");

    function resize() {
      const rect = hero.getBoundingClientRect();
      canvas.width = rect.width;
      canvas.height = rect.height;
      initStars();
    }
    window.addEventListener("resize", resize);
    resize();

    hero.addEventListener("pointerenter", setWarp);
    hero.addEventListener("pointerleave", setImpulse);

    speed = START_SPEED;
    requestAnimationFrame(step);
  }

  document.addEventListener("DOMContentLoaded", init);
})();
