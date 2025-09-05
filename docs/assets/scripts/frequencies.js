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
    container.appendChild(canvas
