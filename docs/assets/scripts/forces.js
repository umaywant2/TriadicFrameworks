(function(){
  const COLORS = ["#FF4136", "#0074D9", "#B10DC9"];
  const DPR = Math.max(1, window.devicePixelRatio || 1);

  const glyphCache = new Map();
  function glyphKey(eq, color, size){ return `${eq}|${color}|${size}`; }
  function getGlyph(eq, color, size){
    const key = glyphKey(eq, color, size);
    if (glyphCache.has(key)) return glyphCache.get(key);
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
    container.appendChild(canvas);
    const ctx = canvas.getContext("2d");

    function resize(){
      const w = container.clientWidth;
      const h = container.clientHeight;
      canvas.width = w * DPR;
      canvas.height = h * DPR;
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      const maxRadius = Math.min(w, h) / 2 - 15;
      orbits[0].radius = maxRadius * 0.4;
      orbits[1].radius = maxRadius * 0.65;
      orbits[2].radius = maxRadius * 0.9;
    }
    window.addEventListener("resize", resize);

    const orbits = [
      { eq: window.TFT_EQUATIONS[1], radius: 0, angle: 0.0, speed: 0.020, color: COLORS[0] },
      { eq: window.TFT_EQUATIONS[2], radius: 0, angle: 1.3, speed: 0.017, color: COLORS[1] },
      { eq: window.TFT_EQUATIONS[3], radius: 0, angle: 2.2, speed: 0.015, color: COLORS[2] }
    ];

    function animate(){
      const w = canvas.clientWidth;
      const h = canvas.clientHeight;
      const cx = w/2;
      const cy = h/2;
      ctx.clearRect(0,0,w,h);

      // Sun (no static equation)
      const sunR = Math.min(w,h) * 0.08;
      ctx.beginPath();
      ctx.arc(cx, cy, sunR, 0, Math.PI*2);
      ctx.fillStyle = COLORS[0];
      ctx.shadowColor = "rgba(255,65,54,0.5)";
      ctx.shadowBlur = 8;
      ctx.fill();

      // Orbits
      ctx.shadowColor = "transparent";
      orbits.forEach(o=>{
        o.angle += o.speed;
        const ox = cx + Math.cos(o.angle) * o.radius;
        const oy = cy + Math.sin(o.angle) * o.radius;
        const g = getGlyph(o.eq, o.color, Math.max(10, sunR*0.8));
        ctx.drawImage(g, ox - g.width/(2*DPR), oy - g.height/(2*DPR));
      });

      requestAnimationFrame(animate);
    }

    resize();
    requestAnimationFrame(animate);
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".forces-animation").forEach(initForces);
  });
})();
