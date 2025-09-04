function makeSprite(width, height) {
  const eq = EQUATIONS[Math.floor(Math.random() * EQUATIONS.length)];
  const size = rand(11, 18);
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
    x: rand(-width/2, width/2),
    y: rand(-height/2, height/2),
    z: rand(0.3, 1.0) * 1000 // depth in px
  };
}

function step(ts) {
  if (!lastTime) lastTime = ts;
  const dt = (ts - lastTime) / 1000;
  lastTime = ts;

  const width = canvas.clientWidth;
  const height = canvas.clientHeight;
  const cx = width / 2;
  const cy = height / 2;

  ctx.clearRect(0, 0, width, height);

  for (let s of sprites) {
    s.z -= SPEED_MULT * 200 * dt; // move toward viewer

    if (s.z <= 1) {
      // recycle to far back
      s.x = rand(-width/2, width/2);
      s.y = rand(-height/2, height/2);
      s.z = 1000;
    }

    const scale = 200 / s.z;
    const sx = cx + s.x * scale;
    const sy = cy + s.y * scale;

    ctx.drawImage(s.img, sx, sy, s.w * scale, s.h * scale);
  }

  requestAnimationFrame(step);
}
