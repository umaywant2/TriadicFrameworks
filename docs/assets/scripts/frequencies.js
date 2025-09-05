(function(){
  const DPR = Math.max(1, window.devicePixelRatio || 1);
  const BASE = "#ADFF2F", RED = "#FF4136", BLUE = "#0074D9", PURP = "#B10DC9";

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

  function buildColorStream(total) {
    const stream = [];
    let i = 1;
    while (stream.length < total) {
      if (i % 9 === 0) { for (let k=0;k<6 && stream.length<total;k++) stream.push(PURP); i++; continue; }
      if (i % 6 === 0) { for (let k=0;k<3 && stream.length<total;k++) stream.push(BLUE); i++; continue; }
      if (i % 3 === 0) { stream.push(RED); i++; continue; }
      stream.push(BASE); i++;
    }
    return stream;
  }

  function initFrequencies(container) {
    const canvas = document.createElement("canvas");
    container.appendChild(canvas);
    const ctx = canvas.getContext("2d");

    const size = 10;
    const spacing = 80;
    const speed = 60; // px/s
    const waveAmp = 20; // vertical amplitude of sine wave
    const waveLength = 200; // horizontal wavelength

    let waves = [];

    function resize(){
      const w = container.clientWidth;
      const h = container.clientHeight;
      canvas.style.width = w + "px";
      canvas.style.height = h + "px";
      canvas.width = Math.max(1, Math.floor(w * DPR));
      canvas.height = Math.max(1, Math.floor(h * DPR));
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      rebuild();
    }
    window.addEventListener("resize", resize);

    function rebuild(){
      const w = canvas.clientWidth;
      const eqs = (window.TFT_EQUATIONS && window.TFT_EQUATIONS.length) ? window.TFT_EQUATIONS : ["\\Psi","\\Phi","\\tau","E"];
      const count = Math.max(12, Math.floor(w / (spacing * 0.8)));
      const colors = buildColorStream(count);

      waves = [
        { dir: 1, phase: 0,     sprites: [] }, // L->R
        { dir: -1, phase: Math.PI/2, sprites: [] }, // R->L
        { dir: 1, phase: Math.PI, sprites: [] } // L->R again
      ];

      waves.forEach((wave, wi) => {
        for (let i=0;i<count;i++){
          wave.sprites.push({
            eq: eqs[i % eqs.length],
            color: colors[i],
            x: wave.dir === 1 ? -Math.random()*w : Math.random()*w
          });
        }
      });
    }

    function animate(time){
      const w = canvas.clientWidth;
      const h = canvas.clientHeight;
      const dt = 1/60;
      ctx.clearRect(0,0,w,h);

      waves.forEach((wave, wi) => {
        const baseY = h/2; // centerline
        wave.sprites.forEach((s, si) => {
          s.x += wave.dir * speed * dt;
          if (wave.dir === 1 && s.x > w + spacing) s.x = -spacing;
          if (wave.dir === -1 && s.x < -spacing) s.x = w + spacing;

          // sine wave vertical offset
          const y = baseY + Math.sin((s.x / waveLength) + wave.phase) * waveAmp;
          const g = getGlyph(s.eq, s.color, size);
          ctx.drawImage(g, Math.round(s.x - (wave.dir === -1 ? g.width/DPR : 0)), y - g.height/(2*DPR));
        });
      });

      requestAnimationFrame(animate);
    }

    resize();
    requestAnimationFrame(animate);
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".frequencies-animation").forEach(initFrequencies);
  });
})();
