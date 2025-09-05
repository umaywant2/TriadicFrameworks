(function(){
  // Lab colors: Force (red), Fluids (blue), Frequencies (purple)
  const COLORS = ["#FF4136", "#0074D9", "#B10DC9"];
  const DPR = Math.max(1, window.devicePixelRatio || 1);

  // Cache KaTeX→canvas glyphs for performance
  const glyphCache = new Map();
  function glyphKey(eq, color, size){ return `${eq}|${color}|${size}`; }

  function getGlyph(eq, color, size){
    const key = glyphKey(eq, color, size);
    if (glyphCache.has(key)) return glyphCache.get(key);

    // Render KaTeX into a temporary span, then draw its textContent
    const span = document.createElement("span");
    try { katex.render(eq, span, { throwOnError: false }); } catch(e){}
    const text = span.textContent || eq;

    const off = document.createElement("canvas");
    const ctx = off.getContext("2d");
    ctx.font = `${size}px Segoe UI, sans-serif`;
    const w = Math.ceil(ctx.measureText(text).width + 8);
    const h = Math.ceil(size + 8);
    off.width = Math.ceil(w * DPR);
    off.height = Math.ceil(h * DPR);
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    ctx.font = `${size}px Segoe UI, sans-serif`;
    ctx.textBaseline = "middle";
    ctx.fillStyle = color;
    ctx.shadowColor = "rgba(0,0,0,0.25)";
    ctx.shadowBlur = 4;
    ctx.fillText(text, 4, h/2);
    glyphCache.set(key, off);
    return off;
  }

  function initForces(container) {
    const canvas = document.createElement("canvas");
    canvas.style.display = "block";
    container.appendChild(canvas);
    const ctx = canvas.getContext("2d");

    function resize(){
      const w = container.clientWidth;
      const h = container.clientHeight;
      canvas.style.width = w + "px";
      canvas.style.height = h + "px";
      canvas.width = Math.max(1, Math.floor(w * DPR));
      canvas.height = Math.max(1, Math.floor(h * DPR));
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    }
    window.addEventListener("resize", resize);
    resize();

    // Fit nicely in 150x120 container
    const centerEq = (window.TFT_EQUATIONS && window.TFT_EQUATIONS[0]) || "F";
    const orbits = [
      { eq: (window.TFT_EQUATIONS && window.TFT_EQUATIONS[1]) || "\\rho_0", radius: 22, angle: 0.0, speed: 0.020, color: COLORS[0] }, // red
      { eq: (window.TFT_EQUATIONS && window.TFT_EQUATIONS[2]) || "\\tau",   radius: 34, angle: 1.3, speed: 0.017, color: COLORS[1] }, // blue
      { eq: (window.TFT_EQUATIONS && window.TFT_EQUATIONS[3]) || "\\Psi",   radius: 46, angle: 2.2, speed: 0.013, color: COLORS[2] }  // purple
    ];

    function animate(ts){
      const w = canvas.clientWidth;
      const h = canvas.clientHeight;
      const cx = w/2;
      const cy = h/2;

      ctx.clearRect(0,0,w,h);

      // Sun (small, top-left bias if container is at hero-left)
      const sunR = 12;
      ctx.beginPath();
      ctx.arc(cx, cy, sunR, 0, Math.PI*2);
      ctx.fillStyle = COLORS[0];
      ctx.shadowColor = "rgba(255,65,54,0.5)";
      ctx.shadowBlur = 8;
      ctx.fill();

      // Sun equation (white)
      const sunGlyph = getGlyph(centerEq, "#FFFFFF", 10);
      ctx.drawImage(sunGlyph, cx - sunGlyph.width/(2*DPR), cy - sunGlyph.height/(2*DPR));

      // Orbits (equation “particles”)
      ctx.shadowColor = "transparent";
      const maxRadius = Math.min(container.clientWidth, container.clientHeight) / 2 - 15;
      const orbits = [
      { eq: window.TFT_EQUATIONS[1], radius: maxRadius * 0.4, angle: 0.0, speed: 0.020, color: COLORS[0] }, // red
      { eq: window.TFT_EQUATIONS[2], radius: maxRadius * 0.65, angle: 1.3, speed: 0.017, color: COLORS[1] }, // blue
      { eq: window.TFT_EQUATIONS[3], radius: maxRadius * 0.9,  angle: 2.2, speed: 0.015, color: COLORS[2] }  // purple
      ];

      
      });

      requestAnimationFrame(animate);
    }
    requestAnimationFrame(animate);
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".forces-animation").forEach(initForces);
  });
})();
