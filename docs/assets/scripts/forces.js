const colors = ["#FF4136", "#0074D9", "#B10DC9"]; // Red, Blue, Purple

function drawOrbitingEq(eq, x, y, color, size) {
  const span = document.createElement("span");
  katex.render(eq, span, { throwOnError: false });
  ctx.font = `${size}px Segoe UI, sans-serif`;
  ctx.fillStyle = color;
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(span.textContent, x, y);
}

function animate() {
  ctx.clearRect(0,0,canvas.width,canvas.height);
  const cx = canvas.width/2;
  const cy = canvas.height/2;

  // Sun
  ctx.beginPath();
  ctx.arc(cx, cy, 12, 0, Math.PI*2);
  ctx.fillStyle = "#FF4136";
  ctx.fill();
  drawOrbitingEq(window.TFT_EQUATIONS[0], cx, cy, "#fff", 10);

  // Orbiters
  orbits.forEach((o, idx) => {
    o.angle += o.speed;
    const ox = cx + Math.cos(o.angle) * o.radius;
    const oy = cy + Math.sin(o.angle) * o.radius;
    drawOrbitingEq(o.eq, ox, oy, colors[idx], 10);
  });

  requestAnimationFrame(animate);
}
