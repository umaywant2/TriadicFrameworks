(function(){
  function initFrequencies(container) {
    const canvas = document.createElement("canvas");
    container.appendChild(canvas);
    const ctx = canvas.getContext("2d");

    function resize(){
      canvas.width = container.clientWidth;
      canvas.height = container.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    function drawEquation(eq, x, y, size){
      const span = document.createElement("span");
      katex.render(eq, span, { throwOnError: false });
      ctx.font = `${size}px Segoe UI, sans-serif`;
      ctx.fillStyle = "#ADFF2F";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(span.textContent, x, y);
    }

    function animate(time){
      ctx.clearRect(0,0,canvas.width,canvas.height);
      const cx = canvas.width/2;
      const cy = canvas.height/2;
      const eqCount = window.TFT_EQUATIONS.length;

      for(let i=0;i<eqCount*4;i++){
        const eq = window.TFT_EQUATIONS[i % eqCount];
        const angle = (i/eqCount) * Math.PI*2 + time*0.001;
        const radius = 40 + Math.sin(time*0.002 + i) * 20;
        const x = cx + Math.cos(angle) * radius;
        const y = cy + Math.sin(angle) * radius;
        drawEquation(eq, x, y, 10);
      }
      requestAnimationFrame(animate);
    }
    requestAnimationFrame(animate);
  }

  document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".frequencies-animation").forEach(initFrequencies);
  });
})();
