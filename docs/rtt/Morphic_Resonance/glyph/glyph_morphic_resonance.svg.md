```svg
<svg xmlns="http://www.w3.org/2000/svg"
     width="512" height="512"
     viewBox="0 0 512 512">

  <!-- Central hollow circle -->
  <circle cx="256" cy="256" r="42"
          fill="none" stroke="black" stroke-width="6"/>

  <!-- Three concentric rings -->
  <circle cx="256" cy="256" r="82"
          fill="none" stroke="black" stroke-width="4"/>
  <circle cx="256" cy="256" r="128"
          fill="none" stroke="black" stroke-width="3"/>
  <circle cx="256" cy="256" r="176"
          fill="none" stroke="black" stroke-width="2.5"/>

  <!-- Incoming filaments (left side) -->
  <path d="M 40 200 C 120 220, 180 240, 240 256"
        fill="none" stroke="black" stroke-width="4"/>
  <path d="M 40 256 C 120 260, 180 260, 240 256"
        fill="none" stroke="black" stroke-width="3"/>
  <path d="M 40 312 C 120 292, 180 272, 240 256"
        fill="none" stroke="black" stroke-width="4"/>

  <!-- Outgoing filament (right side) -->
  <path d="M 272 256 C 332 240, 392 220, 472 200"
        fill="none" stroke="black" stroke-width="4"/>

  <!-- Upward triangle (coherence) -->
  <polygon points="256,150 236,190 276,190"
           fill="none" stroke="black" stroke-width="4"/>

  <!-- Downward triangle (drift) -->
  <polygon points="256,362 236,322 276,322"
           fill="none" stroke="black" stroke-width="4"/>

</svg>
```
