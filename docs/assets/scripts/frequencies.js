(function(){
  const container = document.getElementById("frequencies-animation");
  if (!container) return;
  const canvas = document.createElement("canvas");
  container.appendChild(canvas);
  const ctx = canvas.getContext("2d");

  function resize(){
    canvas.width = container.clientWidth;
    canvas.height = container.clientHeight;
  }
  window.addEventListener("resize", resize);
  resize();

  function animate(time){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    const cx = canvas.width/2;
    const cy = canvas.height/2;
    const eqCount = TFT_EQUATIONS.length;
    for(let i=0;i<eqCount*4;i++){
      const eq = TFT_EQUATIONS[i % eqCount];
      const angle = (i/eqCount) * Math.PI*2 + time*0.001;
      const radius = 40 + Math.sin(time*0.002 + i) * 20;
      const x = cx + Math.cos(angle) * radius;
      const y = cy + Math.sin(angle) * radius;
      ctx.font = "10px Segoe UI, sans-serif";
      ctx.fillStyle = "#ADFF2F";
      ctx.fillText(eq, x, y);
    }
    requestAnimationFrame(animate);
  }
  requestAnimationFrame(animate);
})();
