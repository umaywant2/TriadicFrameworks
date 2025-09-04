// TFT Equation Starfield with Depth Parallax
(function () {
  const HERO_SELECTOR = ".hero";
  const DPR = Math.max(1, window.devicePixelRatio || 1);

  const EQUATIONS = [
    "F = -\\frac{\\pi^2 \\hbar c}{240 d^4}",
    "\\rho_0 = \\frac{\\hbar \\omega^2}{V}",
    "\\tau = \\frac{dR}{d\\phi}",
    "\\tau^{-1} = -\\frac{d\\phi}{dR}",
    "\\Psi(x,t) = A e^{i(kx - \\omega t)}",
    "\\Delta S = \\int_{t_0}^{t_1} (\\frac{d\\phi}{dt} \\cdot R(t))\\, dt",
    "T(\\lambda) = \\frac{I_{out}(\\lambda)}{I_{in}(\\lambda)}",
    "\\Phi = \\int_0^{\\infty} S(\\lambda) R(\\lambda)\\, d\\lambda",
    "L_r = \\sum_{j=1}^{m} V_j \\cdot \\theta_j",
    "G_k = \\sum_{i=1}^{n} \\alpha_i \\cdot \\phi_i",
    "E = m \\cdot R^2 \\cdot \\phi^2",
    "X(\\omega) = \\int_{-\\infty}^{\\infty} x(t) e^{-i\\omega t} dt"
  ];

  let WARP_FACTOR = 6;
  let BASE_MIN = 20;
  let BASE_MAX = 60;
  let DENSITY = 0.00045;
  let SPEED_MULT = 1;

  const prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (prefersReduced) {
    WARP_FACTOR = 2;
    BASE_MIN = 8;
    BASE_MAX = 20;
  }

  let hero, canvas, ctx, sprites = [];
  let lastTime = 0;

  function colors() {
    const dark = document.body.classList.contains("dark-mode");
    return {
      text: dark ? "#FFD966" : "#C18400",
      shadow: dark ? "rgba(255, 217, 102, 0.25)" : "rgba(193, 132, 0, 0.22)"
    };
  }

  function createCanvas() {
    canvas = document.createElement("canvas");
    canvas.className = "hero-warp";
    hero.appendChild(canvas);
    ctx = canvas.getContext("2d");
    resizeCanvas();
  }

  function resizeCanvas() {
    const rect = hero.getBoundingClientRect();
    canvas.style.width = rect.width + "px";
    canvas.style.height = rect.height + "px";
    canvas.width = Math.floor(rect.width * DPR);
    canvas.height = Math.floor(rect.height * DPR);
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    regenSprites();
  }

  function rand(min, max) {
    return Math.random() * (max - min) + min;
  }

  function measureText(font, text) {
    ctx.save();
    ctx.font = font;
    const metrics = ctx.measureText(text);
    ctx.restore();
    return { w: metrics.width, h: parseInt(font, 10) || 14 };
  }

  function makeSprite(width, height) {
    const eq = EQUATIONS[Math.floor(Math.random() * EQUATIONS.length)];
    const size = Math.round(rand(11, 18));
    const font = `${size}px Segoe UI, SegoeUI, 'Helvetica Neue', Arial, sans-serif`;

    const off = document.createElement("canvas");
    const octx = off.getContext("2d");
    const col = colors();

    const m = measureText(font, eq);
    off.width = Math.ceil(m.w + 12);
    off.height = Math.ceil(m.h + 12);

    octx.font = font;
    octx.textBaseline = "top";
    octx.fillStyle = col.text;
    octx.shadowColor = col.shadow;
    octx.shadowBlur = 8;
    octx.globalAlpha = rand(0.35, 0.75);
    octx.translate(6, 6);
    octx.fillText(eq, 0, 0);

    return {
      img: off,
      w: off.width,
      h: off.height,
      x: rand(0, width),
      y: rand(0, height),
      z: rand(0.3, 1.0), // depth: 0.3 = far, 1.0 = near
      speed: rand(BASE_MIN, BASE_MAX)
    };
  }

  function regenSprites() {
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    const targetCount = Math.max(16, Math.floor(width * height * DENSITY));
    sprites = [];
    for (let i = 0; i < targetCount; i++) {
      sprites.push(makeSprite(width, height));
    }
  }

  function step(ts) {
    if (!lastTime) lastTime = ts;
    const dt = Math.min(0.05, (ts - lastTime) / 1000);
    lastTime = ts;

    const width = canvas.clientWidth;
    const height = canvas.clientHeight;

    ctx.clearRect(0, 0, width, height);

    for (let s of sprites) {
      // Depth affects speed and scale
      const depthSpeed = s.speed * s.z;
      s.x -= depthSpeed * SPEED_MULT * dt;

      if (s.x < -s.w - 20) {
        s.x = width + rand(10, 80);
        s.y = rand(0, height - s.h);
        s.z = rand(0.3, 1.0);
        s.speed = rand(BASE_MIN, BASE_MAX);
      }

      const scale = 0.5 + s.z * 0.5;
      ctx.drawImage(s.img, Math.round(s.x), Math.round(s.y), s.w * scale, s.h * scale);
    }

    requestAnimationFrame(step);
  }

  function setImpulse() { SPEED_MULT = 1; }
  function setWarp() { SPEED_MULT = WARP_FACTOR; }

  function init() {
    hero = document.querySelector(HERO_SELECTOR);
    if (!hero) return;

    createCanvas();

    hero.addEventListener("pointerenter", setWarp);
    hero.addEventListener("pointerleave", setImpulse);
    hero.addEventListener("touchstart", () => {
      setWarp();
      setTimeout(setImpulse, 600);
    }, { passive: true });

    window.addEventListener("resize", () => requestAnimationFrame(resizeCanvas));

    document.addEventListener("theme:changed", regenSprites);

    requestAnimationFrame(step);
  }

  document.addEventListener("DOMContentLoaded", init);
})();
