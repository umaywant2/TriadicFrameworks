function getColorForIndex(i) {
  if (i % 9 === 0) return "#B10DC9"; // Purple burst
  if (i % 6 === 0) return "#0074D9"; // Blue triple
  if (i % 3 === 0) return "#FF4136"; // Red single
  return "#ADFF2F"; // Base
}

function animate(time) {
  ctx.clearRect(0,0,canvas.width,canvas.height);
  const eqCount = window.TFT_EQUATIONS.length;
  const spacing = 80;

  // Left to right
  for (let i=0; i<eqCount*3; i++) {
    const eq = window.TFT_EQUATIONS[i % eqCount];
    const x = (i*spacing + (time*0.05) % (spacing*eqCount)) % (canvas.width + spacing) - spacing;
    const y = canvas.height/3;
    drawEquation(eq, x, y, getColorForIndex(i), 10);
  }

  // Right to left
  for (let i=0; i<eqCount*3; i++) {
    const eq = window.TFT_EQUATIONS[i % eqCount];
    const x = canvas.width - ((i*spacing + (time*0.05) % (spacing*eqCount)) % (canvas.width + spacing));
    const y = (canvas.height/3)*2;
    drawEquation(eq, x, y, getColorForIndex(i), 10);
  }

  requestAnimationFrame(animate);
}
