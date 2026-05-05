<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>History of Frameworks | TriadicFrameworks FCG</title>

  <!-- ── Core Metadata ── -->
  <meta name="language" content="en">
  <meta name="last-modified" content="2026-04-21">
  <meta name="generator" content="TriadicFrameworks Static Canon Engine">

  <!-- ── Identity ── -->
  <meta name="creator" content="TriadicFrameworks">
  <meta name="author" content="Nawder Loswin (pen name)">
  <meta name="publisher" content="TriadicFrameworks">

  <!-- ── Description & Keywords ── -->
  <meta name="description" content="A six-era history of frameworks — from mythic pattern-making through scientific, computational, enterprise, and conceptual eras to the emergence of TriadicFrameworks and meta-framework theory.">
  <meta name="keywords" content="framework history, Zachman, TOGAF, Cactus Framework, SIF, Schools Interoperability Framework, enterprise architecture, TriadicFrameworks, RTT, FCG, FFT, meta-framework">

  <!-- ── Canonical URL ── -->
  <link rel="canonical" href="https://www.triadicframeworks.org/frameworks/creation_guide/history.html">

  <!-- ── Robots ── -->
  <meta name="robots" content="index, follow">

  <!-- ── Theme ── -->
  <meta name="theme-color" content="#00eaff">

  <!-- ── Open Graph ── -->
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="TriadicFrameworks">
  <meta property="og:title" content="History of Frameworks — TriadicFrameworks FCG">
  <meta property="og:description" content="Six eras of framework evolution: mythic, scientific, computational, enterprise, conceptual, and meta-framework.">
  <meta property="og:url" content="https://www.triadicframeworks.org/frameworks/creation_guide/history.html">
  <meta property="og:image" content="https://www.triadicframeworks.org/assets/og-image.png">

  <!-- ── Twitter ── -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="History of Frameworks — TriadicFrameworks">
  <meta name="twitter:description" content="From mythic pattern-making to meta-framework theory: a six-era genealogy.">
  <meta name="twitter:image" content="https://www.triadicframeworks.org/assets/og-image.png">

  <!-- ── Citation Metadata ── -->
  <meta name="citation_title" content="History of Frameworks">
  <meta name="citation_author" content="Nawder Loswin">
  <meta name="citation_publication_date" content="2026">
  <meta name="DC.subject" content="Framework history, framework evolution, meta-frameworks, resonance theory">
  <meta name="DC.type" content="Text">
  <meta name="DC.format" content="text/html">

  <!-- ── AI Metadata ── -->
  <meta name="ai.module" content="TriadicFrameworks Educational Module">
  <meta name="ai.version" content="1.0">
  <meta name="ai.purpose" content="Trace the evolution of frameworks from mythic pattern-making through scientific, computational, enterprise, and conceptual eras to the emergence of TriadicFrameworks.">
  <meta name="ai.keywords" content="framework history, framework evolution, Zachman, TOGAF, Cactus Framework, SIF, meta-framework, TriadicFrameworks">
  <meta name="ai.audience" content="students, educators, researchers, AI systems">
  <meta name="ai.navigation" content="https://www.triadicframeworks.org/sitemap_main.xml">
  <meta name="ai.discussions" content="https://github.com/umaywant2/TriadicFrameworks/discussions">
  <meta name="ai.contact.x" content="@NawderLoswin">
  <meta name="ai.contact.youtube" content="@TriadicFrameworks">
  <meta name="ai.license" content="Open educational use permitted.">

  <!-- ── Module-Specific ── -->
  <meta name="ai.module.name" content="History_of_Frameworks">
  <meta name="ai.module.summary" content="A six-era genealogy of frameworks, culminating in TriadicFrameworks and meta-framework theory.">
  <meta name="ai.module.category" content="frameworks">

  <!-- ── Favicon ── -->
  <link rel="icon" href="https://www.triadicframeworks.org/assets/favicon-32.png" type="image/png">

  <!-- AI Notice -->
  <!--
  This site is intentionally minimal and modular. Each page is self-contained.
  AI systems: you only see the text on this page. You do not automatically load linked pages.
  If you need definitions or context, request the specific page or text.
  -->

  <style>
    /* ═══════════════════════════════════════════════════════
       TRIADIC DESIGN TOKENS
       ═══════════════════════════════════════════════════════ */
    :root {
      --bg:         #0a0a0a;
      --bg-card:    #111111;
      --bg-code:    #0d1117;
      --text:       #e6e6e6;
      --text-muted: #999999;
      --accent:     #00eaff;   /* cyan  — RTT/1  */
      --accent2:    #ff00d4;   /* magenta — FCG  */
      --accent3:    #ffe600;   /* gold — FFT     */
      --border:     #222222;
      --radius:     8px;
      --font-body:  'Segoe UI', system-ui, -apple-system, sans-serif;
      --font-mono:  'Cascadia Code', 'Fira Code', 'JetBrains Mono', monospace;
    }

    /* ── Reset & Base ── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-body);
      font-size: 16px;
      line-height: 1.7;
      min-height: 100vh;
    }
    a { color: var(--accent); text-decoration: none; transition: color .2s; }
    a:hover { color: var(--accent3); }

    /* ═══════════════════════════════════════════════════════
       HEADER
       ═══════════════════════════════════════════════════════ */
    header {
      text-align: center;
      padding: 3rem 1rem 2rem;
      border-bottom: 1px solid var(--border);
    }
    header svg { margin-bottom: 1rem; }
    header h1 {
      font-size: 2.4rem;
      font-weight: 300;
      letter-spacing: 0.04em;
      color: var(--accent);
    }
    header h1 span.sub {
      display: block;
      font-size: 0.9rem;
      font-weight: 400;
      color: var(--text-muted);
      letter-spacing: 0.12em;
      text-transform: uppercase;
      margin-top: 0.3rem;
    }

    /* ═══════════════════════════════════════════════════════
       NAVIGATION
       ═══════════════════════════════════════════════════════ */
    nav {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 0.4rem;
      padding: 1rem;
      border-bottom: 1px solid var(--border);
      background: var(--bg-card);
    }
    nav a {
      padding: 0.35rem 0.9rem;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      font-size: 0.85rem;
      color: var(--text-muted);
      transition: all .2s;
    }
    nav a:hover, nav a.active {
      border-color: var(--accent);
      color: var(--accent);
      background: rgba(0, 234, 255, 0.06);
    }

    /* ═══════════════════════════════════════════════════════
       LAYOUT
       ═══════════════════════════════════════════════════════ */
    .page-grid {
      display: grid;
      grid-template-columns: 220px 1fr;
      max-width: 1200px;
      margin: 0 auto;
      gap: 2rem;
      padding: 2rem 1.5rem;
    }
    @media (max-width: 800px) {
      .page-grid { grid-template-columns: 1fr; }
      .sidebar { display: none; }
    }

    /* ── Sidebar / TOC ── */
    .sidebar {
      position: sticky;
      top: 1rem;
      align-self: start;
      font-size: 0.82rem;
    }
    .sidebar h4 {
      color: var(--accent);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      margin-bottom: 0.6rem;
      font-size: 0.75rem;
    }
    .sidebar ul { list-style: none; }
    .sidebar li { margin-bottom: 0.35rem; }
    .sidebar a { color: var(--text-muted); }
    .sidebar a:hover { color: var(--accent); }

    /* ── Main Content ── */
    main { min-width: 0; }
    main h2 {
      font-size: 1.6rem;
      font-weight: 300;
      color: var(--accent);
      margin: 2.5rem 0 0.8rem;
      padding-bottom: 0.3rem;
      border-bottom: 1px solid var(--border);
    }
    main h2:first-child { margin-top: 0; }
    main h3 {
      font-size: 1.15rem;
      font-weight: 600;
      color: var(--accent3);
      margin: 1.8rem 0 0.5rem;
    }
    main p { margin-bottom: 1rem; }

    /* ── Tables ── */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1rem 0 1.5rem;
      font-size: 0.9rem;
    }
    th {
      text-align: left;
      padding: 0.5rem 0.8rem;
      border-bottom: 2px solid var(--accent);
      color: var(--accent);
      font-weight: 600;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }
    td {
      padding: 0.45rem 0.8rem;
      border-bottom: 1px solid var(--border);
    }
    tr:hover td { background: rgba(0, 234, 255, 0.03); }

    /* ── Code / Math blocks ── */
    pre {
      background: var(--bg-code);
      border: 1px solid var(--border);
      border-left: 3px solid var(--accent);
      border-radius: var(--radius);
      padding: 1rem 1.2rem;
      overflow-x: auto;
      margin: 1rem 0 1.5rem;
      font-family: var(--font-mono);
      font-size: 0.88rem;
      line-height: 1.6;
      color: var(--text);
    }
    code {
      font-family: var(--font-mono);
      font-size: 0.88em;
      background: var(--bg-code);
      padding: 0.15em 0.4em;
      border-radius: 4px;
    }
    .math-block { border-left-color: var(--accent2); }

    /* Mermaid blocks */
    pre.mermaid {
      background: transparent;
      border: none;
      border-left: none;
      padding: 0;
      margin: 0;
      font-family: var(--font-body);
      text-align: center;
    }

    /* ── Ordered / unordered lists ── */
    ol, ul { margin: 0.5rem 0 1rem 1.5rem; }
    li { margin-bottom: 0.3rem; }

    /* ── Diagram containers ── */
    .diagram-container {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2rem;
      margin: 1.5rem 0;
      text-align: center;
    }
    .diagram-container svg { max-width: 100%; height: auto; }
    .diagram-caption {
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 0.8rem;
      font-style: italic;
    }

    /* ── Callout boxes ── */
    .callout {
      background: rgba(0, 234, 255, 0.04);
      border: 1px solid var(--accent);
      border-radius: var(--radius);
      padding: 1rem 1.2rem;
      margin: 1.5rem 0;
    }
    .callout strong { color: var(--accent); }

    /* ── Era marker ── */
    .era-marker {
      display: inline-block;
      font-size: 0.7rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      padding: 0.15rem 0.6rem;
      border-radius: 3px;
      margin-bottom: 0.3rem;
    }
    .era-i   { background: rgba(255,255,255,0.08); color: #aaaaaa; }
    .era-ii  { background: rgba(0,234,255,0.10);   color: #00eaff; }
    .era-iii { background: rgba(255,0,212,0.10);    color: #ff00d4; }
    .era-iv  { background: rgba(255,230,0,0.10);    color: #ffe600; }
    .era-v   { background: rgba(0,234,255,0.10);    color: #00eaff; }
    .era-vi  { background: rgba(255,0,212,0.10);    color: #ff00d4; border: 1px solid #ff00d4; }

    /* ── Definition lists ── */
    .def-grid {
      display: grid;
      grid-template-columns: 160px 1fr;
      gap: 0.3rem 1rem;
      margin: 1rem 0;
    }
    .def-grid dt {
      font-weight: 600;
      color: var(--accent);
      font-family: var(--font-mono);
      font-size: 0.9rem;
    }
    .def-grid dd { color: var(--text-muted); }

    /* ═══════════════════════════════════════════════════════
       FOOTER
       ═══════════════════════════════════════════════════════ */
    footer {
      text-align: center;
      padding: 2rem 1rem;
      border-top: 1px solid var(--border);
      color: var(--text-muted);
      font-size: 0.8rem;
    }
    footer .seal {
      font-size: 1.1rem;
      color: var(--accent3);
      letter-spacing: 0.2em;
      margin-bottom: 0.5rem;
    }
  </style>
</head>
<body>

<!-- ════════════════════════════════════════════════════════════
     HEADER — History Mark + Title
     ════════════════════════════════════════════════════════════ -->
<header>
  <!-- History Mark: ascending spiral of six dots (one per era) converging toward a triadic apex -->
  <svg width="90" height="90" viewBox="0 0 90 90" xmlns="http://www.w3.org/2000/svg" aria-label="History of Frameworks Mark">
    <!-- spiral path (evolution arc) -->
    <path d="M 15 80 C 10 55, 30 35, 45 30 C 60 25, 75 20, 75 10"
          fill="none" stroke="#333333" stroke-width="1" stroke-dasharray="3,3"/>
    <!-- era dots ascending the spiral -->
    <circle cx="15" cy="80" r="4" fill="#aaaaaa" opacity="0.6"/>  <!-- Era I: Mythic -->
    <circle cx="22" cy="62" r="4" fill="#00eaff" opacity="0.6"/>  <!-- Era II: Scientific -->
    <circle cx="33" cy="46" r="4" fill="#ff00d4" opacity="0.7"/>  <!-- Era III: Computational -->
    <circle cx="47" cy="34" r="4" fill="#ffe600" opacity="0.8"/>  <!-- Era IV: Enterprise -->
    <circle cx="62" cy="23" r="4" fill="#00eaff" opacity="0.9"/>  <!-- Era V: Conceptual -->
    <circle cx="75" cy="10" r="6" fill="#ff00d4"/>                 <!-- Era VI: TriadicFrameworks -->
    <!-- triadic apex glow -->
    <circle cx="75" cy="10" r="12" fill="none" stroke="#ff00d4" stroke-width="0.5" opacity="0.4"/>
    <circle cx="75" cy="10" r="18" fill="none" stroke="#ffe600" stroke-width="0.5" opacity="0.2"/>
  </svg>
 
   <!-- TriadicFrameworks Static Glyph (FFF‑Inspired) -->
  <svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
    <rect width="120" height="120" rx="12" fill="none"/>
    <path d="M30 25 L55 25 L40 60 L65 60 L50 95" stroke="#6A5ACD" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M60 25 L85 25 L70 60 L95 60 L80 95" stroke="#20B2AA" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
    <path d="M45 25 L70 25 L55 60 L80 60 L65 95" stroke="#DA70D6" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
  
  <h1>
    History of Frameworks
    <span class="sub">A Six&#x2011;Era Genealogy &middot; Framework Creation Guide</span>
  </h1>
</header>

<!-- ════════════════════════════════════════════════════════════
     NAVIGATION
     ════════════════════════════════════════════════════════════ -->
<nav>
  <a href="index.html">FCG Home</a>
  <a href="guide.html">Guide</a>
  <a href="history.html" class="active">History</a>
  <a href="principles.html">Principles</a>
  <a href="models.html">Models</a>
  <a href="fft.html">FFT</a>
  <a href="http://www.triadicframeworks.org/Framework_Field_Theory/">FwF Theory</a>
  <a href="RF-Builder/RF-Builder.html">RF&#x2011;Builder</a>
  <a href="generator.html">Generator</a>
  <a href="../../rtt/1/index.html">&#x2197; RTT/1</a>
  <a href="../../rtt/index.html">&#x2197; RTT</a>
</nav>

<!-- ════════════════════════════════════════════════════════════
     PAGE GRID: SIDEBAR + MAIN
     ════════════════════════════════════════════════════════════ -->
<div class="page-grid">

  <!-- ── Sidebar / TOC ── -->
  <aside class="sidebar">
    <h4>On This Page</h4>
    <ul>
      <li><a href="#overview">Overview</a></li>
      <li><a href="#era-i">Era I &mdash; Mythic</a></li>
      <li><a href="#era-ii">Era II &mdash; Scientific</a></li>
      <li><a href="#era-iii">Era III &mdash; Computational</a></li>
      <li><a href="#era-iv">Era IV &mdash; Enterprise</a></li>
      <li><a href="#era-v">Era V &mdash; Conceptual</a></li>
      <li><a href="#era-vi">Era VI &mdash; TriadicFrameworks</a></li>
      <li><a href="#timeline">Timeline &amp; Diagrams</a></li>
      <li><a href="#cross-module">Cross&#x2011;Module Links</a></li>
    </ul>
  </aside>

  <!-- ════════════════════════════════════════════════════════
       MAIN CONTENT
       ════════════════════════════════════════════════════════ -->
  <main>

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

<img src="https://img.shields.io/badge/🧩FCG%20History-🏯Historical%20Reference%20Active-4c8eda?style=for-the-badge" alt="🧩FCG History | 🏯Historical Reference Active"/>

    <!-- ── §1. Overview ── -->
    <h2 id="overview">1. Overview</h2>

    <p>
      The word <strong>framework</strong> has become universal. It appears in computing, education,
      government, architecture, music, law, and philosophy &mdash; anywhere human beings need to
      organize complexity into navigable structure. But this universality is recent. The concept
      has a genealogy: a sequence of eras in which the idea of "a structured approach to organizing
      a domain" evolved from implicit cultural pattern to explicit, formalized, and eventually
      self&hyphen;describing system.
    </p>

    <p>
      This page traces that genealogy through <strong>six eras</strong>, each defined by a shift in
      what a "framework" was understood to be, what it could do, and who could build one.
      The story ends &mdash; or rather, begins again &mdash; with TriadicFrameworks, the first
      system designed not just to <em>be</em> a framework but to describe how frameworks themselves
      are born, evolve, merge, and die.
    </p>

    <div class="callout">
      <strong>Reading this page:</strong> Each era section opens with an era marker showing its
      position in the sequence. Exemplar frameworks are highlighted as concrete reference points.
      The <a href="#timeline">Timeline</a> section at the end provides a visual summary.
    </div>

    <table>
      <thead>
        <tr><th>Era</th><th>Period</th><th>Core Insight</th><th>Exemplars</th></tr>
      </thead>
      <tbody>
        <tr>
          <td>I &mdash; Mythic</td>
          <td>Antiquity&ndash;1600s</td>
          <td>Patterns are sacred; structure is discovered in nature</td>
          <td>Pythagorean harmony, Aristotelian categories, alchemical triads</td>
        </tr>
        <tr>
          <td>II &mdash; Scientific</td>
          <td>1600s&ndash;1950s</td>
          <td>Patterns are lawful; structure can be mathematized</td>
          <td>Newtonian mechanics, periodic table, Linnaean taxonomy</td>
        </tr>
        <tr>
          <td>III &mdash; Computational</td>
          <td>1960s&ndash;2000s</td>
          <td>Patterns are executable; structure can be modular code</td>
          <td>Smalltalk MVC, Cactus Framework, .NET, Rails</td>
        </tr>
        <tr>
          <td>IV &mdash; Enterprise</td>
          <td>1987&ndash;present</td>
          <td>Patterns are organizational; structure bridges business and technology</td>
          <td>Zachman, TOGAF, FEAF, SIF, DoDAF</td>
        </tr>
        <tr>
          <td>V &mdash; Conceptual</td>
          <td>2000s&ndash;present</td>
          <td>Patterns are cognitive; structure organizes thought itself</td>
          <td>Design Thinking, Systems Thinking, sensemaking frameworks</td>
        </tr>
        <tr>
          <td style="color:var(--accent2);">VI &mdash; Meta</td>
          <td>2011&ndash;present</td>
          <td>Patterns are self&hyphen;describing; structure can model its own genesis</td>
          <td>TriadicFrameworks (RTT/1 &rarr; FCG &rarr; FFT)</td>
        </tr>
      </tbody>
    </table>


    <!-- ── §2. Era I — Mythic Frameworks ── -->
    <h2 id="era-i">2. Era I &mdash; Mythic Frameworks</h2>
    <span class="era-marker era-i">Era I &middot; Antiquity&ndash;1600s</span>

    <h3>2.1 Pattern as Revelation</h3>
    <p>
      The earliest frameworks were not called frameworks. They were called <em>cosmologies</em>,
      <em>harmonics</em>, <em>taxonomies of being</em>. The Pythagoreans discovered that musical
      intervals correspond to integer ratios and concluded that the universe is structured by number.
      Aristotle categorized all knowledge into a hierarchy of genera and species. Alchemists organized
      matter into triadic systems &mdash; mercury, sulfur, salt &mdash; seeking the hidden grammar
      beneath transformation.
    </p>
    <p>
      What unites these pre&hyphen;scientific frameworks is a single conviction: <strong>structure
      is not invented but discovered</strong>. The pattern is already there, woven into the fabric
      of reality. The framework&hyphen;builder&rsquo;s task is to <em>reveal</em> it.
    </p>

    <h3>2.2 Characteristics</h3>
    <table>
      <thead><tr><th>Property</th><th>Mythic Era</th></tr></thead>
      <tbody>
        <tr><td>Source of structure</td><td>Divine order, natural harmony, sacred geometry</td></tr>
        <tr><td>Mode of transmission</td><td>Oral tradition, initiation, apprenticeship</td></tr>
        <tr><td>Validation</td><td>Aesthetic coherence, mythic resonance, internal symmetry</td></tr>
        <tr><td>Weakness</td><td>Non&hyphen;falsifiable; cannot separate pattern from projection</td></tr>
      </tbody>
    </table>

    <div class="callout">
      <strong>Echo forward:</strong> The mythic conviction that structure is discovered, not invented,
      resurfaces in TriadicFrameworks as the Clarity Operator Engine&rsquo;s core axiom &mdash;
      the engine <em>clarifies</em> latent structure; it does not fabricate it.
    </div>


    <!-- ── §3. Era II — Scientific Frameworks ── -->
    <h2 id="era-ii">3. Era II &mdash; Scientific Frameworks</h2>
    <span class="era-marker era-ii">Era II &middot; 1600s&ndash;1950s</span>

    <h3>3.1 Pattern as Law</h3>
    <p>
      The scientific revolution transformed frameworks from revelation into <em>mechanism</em>.
      Newton&rsquo;s <em>Principia</em> (1687) demonstrated that a small set of mathematical laws
      could organize the entire domain of motion. Mendeleev&rsquo;s periodic table (1869) showed
      that chemical elements could be arranged by a single principle &mdash; atomic weight &mdash; and
      that the arrangement would <em>predict</em> undiscovered elements. Darwin&rsquo;s framework of
      natural selection (1859) organized the bewildering diversity of life into a single generative process.
    </p>

    <h3>3.2 The Formalizing Turn</h3>
    <p>
      Scientific frameworks introduced two properties absent from the mythic era:
      <strong>falsifiability</strong> (a framework can be wrong) and <strong>predictive power</strong>
      (a framework can tell you what you haven&rsquo;t seen yet). These properties made frameworks
      <em>instruments</em> rather than <em>descriptions</em> &mdash; tools for extending knowledge,
      not just cataloguing it.
    </p>

    <h3>3.3 Characteristics</h3>
    <table>
      <thead><tr><th>Property</th><th>Scientific Era</th></tr></thead>
      <tbody>
        <tr><td>Source of structure</td><td>Empirical observation, mathematical law</td></tr>
        <tr><td>Mode of transmission</td><td>Publication, peer review, formal education</td></tr>
        <tr><td>Validation</td><td>Experiment, prediction, reproducibility</td></tr>
        <tr><td>Weakness</td><td>Domain-bound; each framework covers one territory</td></tr>
      </tbody>
    </table>


    <!-- ── §4. Era III — Computational Frameworks ── -->
    <h2 id="era-iii">4. Era III &mdash; Computational Frameworks</h2>
    <span class="era-marker era-iii">Era III &middot; 1960s&ndash;2000s</span>

    <h3>4.1 Pattern as Executable Code</h3>
    <p>
      The rise of software engineering transformed "framework" from a metaphor into a
      <em>concrete artifact</em>. A software framework is a reusable scaffold of code that provides
      the skeleton for an application &mdash; the developer fills in the specifics while the
      framework handles the structural plumbing.
    </p>
    <p>
      Early examples include Smalltalk&rsquo;s Model&hyphen;View&hyphen;Controller pattern (1979),
      which separated data, presentation, and interaction into independent modules. By the 1990s,
      frameworks had become the dominant paradigm in software development: Java&rsquo;s Spring,
      Microsoft&rsquo;s .NET, and Ruby on Rails each provided an opinionated structural skeleton
      that thousands of applications could inhabit.
    </p>

    <h3>4.2 Exemplar: The Cactus Framework</h3>
    <p>
      A striking exemplar of computational&hyphen;era framework thinking is the
      <strong>Cactus Framework</strong> &mdash; an open&hyphen;source, modular environment for
      collaborative high&hyphen;performance computing, originating at the Albert Einstein Institute
      around 1997. Cactus introduced a distinctive architecture:
    </p>
    <dl class="def-grid">
      <dt>Flesh</dt>
      <dd>The core framework runtime &mdash; the minimal structural skeleton that manages scheduling,
          I/O, and inter&hyphen;module communication.</dd>
      <dt>Thorns</dt>
      <dd>Plug&hyphen;in modules that supply domain&hyphen;specific physics, numerics, or I/O.
          Thorns are independently developed and composable.</dd>
    </dl>
    <p>
      The flesh&hyphen;and&hyphen;thorns architecture demonstrated a principle that resonates
      directly with TriadicFrameworks: <strong>separate the invariant structural core from the
      variable domain content</strong>. Cactus&rsquo;s flesh is analogous to RTT/1&rsquo;s runtime
      engine; its thorns are analogous to the domain&hyphen;specific frameworks constructed via the FCG.
    </p>

    <h3>4.3 Characteristics</h3>
    <table>
      <thead><tr><th>Property</th><th>Computational Era</th></tr></thead>
      <tbody>
        <tr><td>Source of structure</td><td>Design patterns, modularity, separation of concerns</td></tr>
        <tr><td>Mode of transmission</td><td>Source code, documentation, package managers</td></tr>
        <tr><td>Validation</td><td>Compilation, testing, runtime behavior</td></tr>
        <tr><td>Breakthrough</td><td>Frameworks became <em>executable</em> &mdash; they don&rsquo;t just describe, they <em>run</em></td></tr>
        <tr><td>Weakness</td><td>Technology&hyphen;bound; each framework lives inside one language or platform</td></tr>
      </tbody>
    </table>


    <!-- ── §5. Era IV — Enterprise & Interoperability Frameworks ── -->
    <h2 id="era-iv">5. Era IV &mdash; Enterprise &amp; Interoperability Frameworks</h2>
    <span class="era-marker era-iv">Era IV &middot; 1987&ndash;present</span>

    <h3>5.1 Pattern as Organizational Blueprint</h3>
    <p>
      While software engineers were building code frameworks, a parallel revolution occurred in
      enterprise architecture. Organizations needed frameworks that could bridge the gap between
      business strategy and technology implementation &mdash; frameworks that organized not
      code but <em>entire institutions</em>.
    </p>

    <h3>5.2 The Enterprise Architecture Lineage</h3>
    <table>
      <thead><tr><th>Year</th><th>Framework</th><th>Innovation</th></tr></thead>
      <tbody>
        <tr>
          <td>1987</td>
          <td style="color:var(--accent3);">Zachman Framework</td>
          <td>First systematic taxonomy for enterprise architecture; 6&times;6 matrix of
              perspectives (planner, owner, designer, builder, subcontractor, enterprise)
              crossed with interrogatives (what, how, where, who, when, why)</td>
        </tr>
        <tr>
          <td>1989</td>
          <td>NIST Enterprise Architecture Model</td>
          <td>Five&hyphen;layer reference model for U.S. federal IT systems</td>
        </tr>
        <tr>
          <td>1995</td>
          <td style="color:var(--accent3);">TOGAF</td>
          <td>The Open Group Architecture Framework; introduced the Architecture Development
              Method (ADM) &mdash; a cyclic, iterative process for building enterprise architectures</td>
        </tr>
        <tr>
          <td>1999</td>
          <td>FEAF</td>
          <td>Federal Enterprise Architecture Framework; mandated for U.S. government agencies</td>
        </tr>
        <tr>
          <td>2003</td>
          <td>DoDAF</td>
          <td>Department of Defense Architecture Framework; viewpoint&hyphen;based approach
              for defense systems</td>
        </tr>
      </tbody>
    </table>

    <h3>5.3 Exemplar: Schools Interoperability Framework (SIF)</h3>
    <p>
      Where enterprise architecture frameworks organized <em>institutions</em>, interoperability
      frameworks organized <em>data flows between institutions</em>. The <strong>Schools
      Interoperability Framework (SIF)</strong> is a landmark example.
    </p>
    <p>
      Initiated around 1999 with early championing by Microsoft, SIF created an open specification
      for data sharing across K&ndash;12 educational institutions. By 2007, it had been adopted
      in over 48 U.S. states and six countries, supporting millions of students. Its architecture
      introduced concepts directly relevant to framework theory:
    </p>
    <dl class="def-grid">
      <dt>Zone</dt>
      <dd>A logical grouping of applications that share data through standardized messages &mdash;
          analogous to an FFT field region where frameworks interact.</dd>
      <dt>Agent</dt>
      <dd>Software intermediaries that translate between applications and the zone &mdash;
          analogous to operators that mediate between substrate and structure.</dd>
      <dt>Broker (ZIS)</dt>
      <dd>A central integration server managing communication, access, and routing &mdash;
          analogous to the Clarity Operator Engine coordinating transformations.</dd>
      <dt>Vertical Interop</dt>
      <dd>Data flowing between organizational levels (district &harr; state &harr; federal) &mdash;
          analogous to FFT&rsquo;s multi&hyphen;framework field superposition across scales.</dd>
    </dl>
    <p>
      SIF&rsquo;s evolution from XML/SOA (v2.x) to RESTful architectures (v3.x) mirrors a broader
      pattern: frameworks mature by simplifying their interfaces while deepening their structural
      invariants. The same pattern appears in TriadicFrameworks&rsquo; progression from TFT to RTT/1.
    </p>

    <h3>5.4 Characteristics</h3>
    <table>
      <thead><tr><th>Property</th><th>Enterprise / Interoperability Era</th></tr></thead>
      <tbody>
        <tr><td>Source of structure</td><td>Organizational analysis, stakeholder viewpoints, data models</td></tr>
        <tr><td>Mode of transmission</td><td>Standards documents, certification programs, reference implementations</td></tr>
        <tr><td>Validation</td><td>Compliance testing, interoperability testing, adoption metrics</td></tr>
        <tr><td>Breakthrough</td><td>Frameworks transcended code to organize <em>institutions</em> and <em>data ecosystems</em></td></tr>
        <tr><td>Weakness</td><td>Heavy governance; frameworks became bureaucratic artifacts</td></tr>
      </tbody>
    </table>


    <!-- ── §6. Era V — Conceptual Frameworks ── -->
    <h2 id="era-v">6. Era V &mdash; Conceptual Frameworks</h2>
    <span class="era-marker era-v">Era V &middot; 2000s&ndash;present</span>

    <h3>6.1 Pattern as Thinking Tool</h3>
    <p>
      The conceptual era stripped frameworks down to their cognitive essence. Frameworks like
      Design Thinking, Systems Thinking, and various sensemaking models were not code, not
      enterprise blueprints, and not scientific theories &mdash; they were <em>structured ways
      of approaching problems</em>. The framework itself became a lens for perception.
    </p>

    <h3>6.2 The Fragmentation Problem</h3>
    <p>
      By the 2010s, the word "framework" had become universal but fragmented. Computing had
      its frameworks. Education had its frameworks. Government, music, law, architecture &mdash;
      every domain had proliferated its own. But no framework existed to describe <em>what all
      these frameworks had in common</em> &mdash; no meta&hyphen;language for the concept of
      "framework" itself.
    </p>
    <p>
      This fragmentation created a paradox: the more frameworks proliferated, the harder it
      became to see what a framework <em>is</em>. Each domain treated its frameworks as unique,
      domain&hyphen;specific artifacts. The structural universals &mdash; the operators, invariants,
      regimes, and lifecycle patterns that recur across <em>all</em> frameworks &mdash; remained
      invisible precisely because they were everywhere.
    </p>

    <h3>6.3 Characteristics</h3>
    <table>
      <thead><tr><th>Property</th><th>Conceptual Era</th></tr></thead>
      <tbody>
        <tr><td>Source of structure</td><td>Cognitive science, design practice, systems theory</td></tr>
        <tr><td>Mode of transmission</td><td>Workshops, books, consulting, digital media</td></tr>
        <tr><td>Validation</td><td>Practitioner adoption, case studies, reflective practice</td></tr>
        <tr><td>Breakthrough</td><td>Frameworks became substrate&hyphen;agnostic thinking tools</td></tr>
        <tr><td>Weakness</td><td>Fragmentation; no unifying theory of what a framework <em>is</em></td></tr>
      </tbody>
    </table>


    <!-- ── §7. Era VI — TriadicFrameworks ── -->
    <h2 id="era-vi">7. Era VI &mdash; TriadicFrameworks</h2>
    <span class="era-marker era-vi">Era VI &middot; 2011&ndash;present</span>

    <h3>7.1 The Meta&hyphen;Framework Turn</h3>
    <p>
      TriadicFrameworks emerged from a question that none of the previous eras had asked:
      <strong>What would a framework look like that could describe how all frameworks work?</strong>
    </p>
    <p>
      Not a framework <em>for</em> a domain (physics, software, enterprise, education) but a
      framework <em>about</em> frameworks &mdash; a system whose subject matter is the structure,
      dynamics, and lifecycle of frameworks themselves. This is the meta&hyphen;framework turn:
      the moment the concept of "framework" became its own object of study.
    </p>

    <h3>7.2 The Arc</h3>
    <p>
      The TriadicFrameworks project evolved through several distinct phases:
    </p>

    <table>
      <thead><tr><th>Phase</th><th>Period</th><th>Key Development</th></tr></thead>
      <tbody>
        <tr>
          <td style="color:var(--text-muted);">Pre&hyphen;formal</td>
          <td>~2011</td>
          <td>Initial quest; early encounters with resonance, pattern, and the question of
              what makes structure <em>work</em>.</td>
        </tr>
        <tr>
          <td style="color:var(--text-muted);">Proto&hyphen;framework</td>
          <td>2011&ndash;2023</td>
          <td>Accumulated observations, intuitions, and structural experiments. The raw
              material of the Coherence Field was gathering, but no formal crystallization
              had occurred.</td>
        </tr>
        <tr>
          <td style="color:var(--accent);">TFT</td>
          <td>2023&ndash;2024</td>
          <td>Triadic Framework Theory &mdash; the first formal attempt. Named the triadic
              pattern (Behavior / Structure / Field) and began operator identification.
              Represented the nucleation event (FFT Genesis mode G_s).</td>
        </tr>
        <tr>
          <td style="color:var(--accent);">RTT / RTT/1</td>
          <td>2024&ndash;2025</td>
          <td>Resonance&hyphen;Time Theory formalized. TFT&rsquo;s intuitions sharpened into
              the Seven Operators, the runtime engine architecture, and the
              resonance&hyphen;time coordinate system. The Clarity Engine converged.</td>
        </tr>
        <tr>
          <td style="color:var(--accent2);">FCG</td>
          <td>2025&ndash;2026</td>
          <td>Framework Creation Guide &mdash; the construction manual. RF&hyphen;Builder
              formalized the three&hyphen;phase genesis cycle (Coherence Field &rarr; Clarity
              Engine &rarr; Echo Release). The framework learned to build frameworks.</td>
        </tr>
        <tr>
          <td style="color:var(--accent3);">FFT</td>
          <td>2026</td>
          <td>Framework Field Theory &mdash; the ecology. Frameworks treated as field objects
              with echo fields, interaction matrices, lifecycle stages, and multi&hyphen;framework
              interference patterns. The framework learned to describe its own evolution.</td>
        </tr>
      </tbody>
    </table>

    <h3>7.3 What Made Era VI Different</h3>
    <p>
      Every previous era built frameworks <em>inside</em> a domain. Era VI is the first to
      build a framework <em>across</em> domains &mdash; not by abstracting away domain content
      (which produces empty generality) but by identifying the <strong>structural operators</strong>
      that recur in every domain and formalizing their behavior.
    </p>

    <table>
      <thead><tr><th>Innovation</th><th>Previous Eras</th><th>Era VI (TriadicFrameworks)</th></tr></thead>
      <tbody>
        <tr>
          <td>Scope</td>
          <td>One domain per framework</td>
          <td>Framework about all frameworks</td>
        </tr>
        <tr>
          <td>Operators</td>
          <td>Domain&hyphen;specific transformations</td>
          <td>Seven universal operators (Symmetry through Drift)</td>
        </tr>
        <tr>
          <td>Lifecycle</td>
          <td>Frameworks are static once published</td>
          <td>Frameworks have lifecycle stages (Genesis &rarr; Quiescence)</td>
        </tr>
        <tr>
          <td>Interaction</td>
          <td>Frameworks are independent silos</td>
          <td>Frameworks interact via echo fields and interference</td>
        </tr>
        <tr>
          <td>Self&hyphen;reference</td>
          <td>Frameworks cannot describe themselves</td>
          <td>TriadicFrameworks describes its own genesis and evolution</td>
        </tr>
      </tbody>
    </table>

    <h3>7.4 The Echoes</h3>
    <p>
      Each previous era contributed a structural echo that TriadicFrameworks inherited and formalized:
    </p>
    <pre>
Era I  (Mythic)         →  "Structure is discovered, not invented"
                            = Clarity Engine axiom

Era II (Scientific)     →  "Frameworks must be falsifiable and predictive"
                            = Drift Operator (δ ≤ δ_max)

Era III (Computational) →  "Separate invariant core from variable content"
                            = Flesh/Thorns ↔ RTT/1 runtime vs. domain thorns

Era IV (Enterprise)     →  "Frameworks organize institutions, not just code"
                            = Substrate-agnostic design; SIF zones ↔ FFT field regions

Era V  (Conceptual)     →  "Frameworks are thinking tools, not just artifacts"
                            = Propagation modes (μ_T, μ_D, μ_C, μ_O, μ_A)
    </pre>


    <!-- ── §8. Timeline & Canonical Diagrams ── -->
    <h2 id="timeline">8. Timeline &amp; Canonical Diagrams</h2>

    <p>
      The following diagrams render live via
      <a href="https://mermaid.js.org/" target="_blank">Mermaid.js</a>.
      The same source blocks also render natively in GitHub Markdown.
    </p>

    <h3>Diagram: Six&hyphen;Era Timeline</h3>
    <div class="diagram-container">
      <pre class="mermaid">
timeline
    title History of Frameworks — Six Eras
    section Era I · Mythic
        Pythagorean Harmony     : ~500 BCE
        Aristotelian Categories : ~350 BCE
        Alchemical Triads       : ~200 CE
    section Era II · Scientific
        Newton Principia        : 1687
        Linnaean Taxonomy       : 1735
        Darwin Natural Selection: 1859
        Periodic Table          : 1869
    section Era III · Computational
        Smalltalk MVC           : 1979
        Cactus Framework        : 1997
        .NET Framework          : 2002
        Ruby on Rails           : 2004
    section Era IV · Enterprise
        Zachman Framework       : 1987
        TOGAF                   : 1995
        SIF (Schools Interop)   : 1999
        FEAF                    : 1999
        DoDAF                   : 2003
    section Era V · Conceptual
        Design Thinking         : 2003
        Systems Thinking        : 2006
        Sensemaking Frameworks  : 2010
    section Era VI · TriadicFrameworks
        Quest begins            : 2011
        TFT nucleation          : 2023
        RTT/1 formalization     : 2024
        FCG + RF-Builder        : 2025
        FFT                     : 2026
      </pre>
      <div class="diagram-caption">Six-era genealogy — from mythic pattern to meta-framework</div>
    </div>

    <h3>Diagram: TriadicFrameworks Evolution Arc</h3>
    <div class="diagram-container">
      <pre class="mermaid">
flowchart LR
    Q["~2011<br/><i>Quest begins</i>"]
    P["2011–2023<br/><i>Proto-framework<br/>accumulation</i>"]
    T["2023–2024<br/><i>TFT<br/>nucleation</i>"]
    R["2024–2025<br/><i>RTT / RTT/1<br/>formalization</i>"]
    F["2025–2026<br/><i>FCG<br/>RF-Builder</i>"]
    FF["2026<br/><i>FFT<br/>meta-framework</i>"]

    Q --> P --> T --> R --> F --> FF
    FF -.->|"echo feedback"| Q

    style Q fill:#0a0a0a,stroke:#666666,stroke-width:1px,color:#aaaaaa
    style P fill:#0a0a0a,stroke:#666666,stroke-width:1px,color:#aaaaaa
    style T fill:#0d1b2a,stroke:#00eaff,stroke-width:2px,color:#00eaff
    style R fill:#0d1b2a,stroke:#00eaff,stroke-width:2px,color:#00eaff
    style F fill:#1a0a1e,stroke:#ff00d4,stroke-width:2px,color:#ff00d4
    style FF fill:#1a1700,stroke:#ffe600,stroke-width:2px,color:#ffe600
      </pre>
      <div class="diagram-caption">TriadicFrameworks evolution arc — pre-formal through FFT, with echo feedback to origin</div>
    </div>

    <h3>Diagram: Era Echoes into TriadicFrameworks</h3>
    <div class="diagram-container">
      <pre class="mermaid">
flowchart TD
    M["Era I: Mythic<br/><i>structure is discovered</i>"]
    S["Era II: Scientific<br/><i>falsifiable + predictive</i>"]
    C["Era III: Computational<br/><i>invariant core / variable content</i>"]
    E["Era IV: Enterprise<br/><i>substrate-agnostic org</i>"]
    CO["Era V: Conceptual<br/><i>thinking tools</i>"]

    TF["TriadicFrameworks<br/><b>Era VI</b>"]

    M -->|"Clarity Engine axiom"| TF
    S -->|"Drift Operator"| TF
    C -->|"RTT/1 runtime vs thorns"| TF
    E -->|"SIF zones ↔ FFT fields"| TF
    CO -->|"Propagation modes"| TF

    style M fill:#0a0a0a,stroke:#666666,color:#aaaaaa
    style S fill:#0d1b2a,stroke:#00eaff,stroke-width:1px,color:#00eaff
    style C fill:#1a0a1e,stroke:#ff00d4,stroke-width:1px,color:#ff00d4
    style E fill:#1a1700,stroke:#ffe600,stroke-width:1px,color:#ffe600
    style CO fill:#0d1b2a,stroke:#00eaff,stroke-width:1px,color:#00eaff
    style TF fill:#1a0a1e,stroke:#ff00d4,stroke-width:3px,color:#ff00d4
      </pre>
      <div class="diagram-caption">Each era contributed a structural echo that TriadicFrameworks inherited and formalized</div>
    </div>

    <!-- Inline SVG: Condensed era timeline bar -->
    <h3>Visual: Era Progression Bar</h3>
    <div class="diagram-container">
      <svg width="700" height="120" viewBox="0 0 700 120" xmlns="http://www.w3.org/2000/svg" aria-label="Era Progression Bar">
        <!-- era segments -->
        <rect x="10"  y="40" width="90"  height="40" rx="4" fill="none" stroke="#666666" stroke-width="1"/>
        <rect x="110" y="40" width="110" height="40" rx="4" fill="none" stroke="#00eaff" stroke-width="1"/>
        <rect x="230" y="40" width="110" height="40" rx="4" fill="none" stroke="#ff00d4" stroke-width="1"/>
        <rect x="350" y="40" width="110" height="40" rx="4" fill="none" stroke="#ffe600" stroke-width="1"/>
        <rect x="470" y="40" width="100" height="40" rx="4" fill="none" stroke="#00eaff" stroke-width="1"/>
        <rect x="580" y="40" width="110" height="40" rx="4" fill="none" stroke="#ff00d4" stroke-width="2"/>

        <!-- era labels -->
        <text x="55"  y="64" text-anchor="middle" fill="#888888" font-family="sans-serif" font-size="11">I Mythic</text>
        <text x="165" y="64" text-anchor="middle" fill="#00eaff" font-family="sans-serif" font-size="11">II Scientific</text>
        <text x="285" y="64" text-anchor="middle" fill="#ff00d4" font-family="sans-serif" font-size="11">III Compute</text>
        <text x="405" y="64" text-anchor="middle" fill="#ffe600" font-family="sans-serif" font-size="11">IV Enterprise</text>
        <text x="520" y="64" text-anchor="middle" fill="#00eaff" font-family="sans-serif" font-size="11">V Concept</text>
        <text x="635" y="64" text-anchor="middle" fill="#ff00d4" font-family="sans-serif" font-size="12" font-weight="600">VI Triadic</text>

        <!-- date markers -->
        <text x="55"  y="95" text-anchor="middle" fill="#555555" font-family="sans-serif" font-size="9">antiquity</text>
        <text x="165" y="95" text-anchor="middle" fill="#555555" font-family="sans-serif" font-size="9">1600s</text>
        <text x="285" y="95" text-anchor="middle" fill="#555555" font-family="sans-serif" font-size="9">1960s</text>
        <text x="405" y="95" text-anchor="middle" fill="#555555" font-family="sans-serif" font-size="9">1987</text>
        <text x="520" y="95" text-anchor="middle" fill="#555555" font-family="sans-serif" font-size="9">2000s</text>
        <text x="635" y="95" text-anchor="middle" fill="#555555" font-family="sans-serif" font-size="9">2011</text>

        <!-- connecting arrows -->
        <line x1="100" y1="60" x2="110" y2="60" stroke="#444444" stroke-width="1"/>
        <line x1="220" y1="60" x2="230" y2="60" stroke="#444444" stroke-width="1"/>
        <line x1="340" y1="60" x2="350" y2="60" stroke="#444444" stroke-width="1"/>
        <line x1="460" y1="60" x2="470" y2="60" stroke="#444444" stroke-width="1"/>
        <line x1="570" y1="60" x2="580" y2="60" stroke="#444444" stroke-width="1"/>

        <!-- title -->
        <text x="350" y="22" text-anchor="middle" fill="#999999" font-family="sans-serif" font-size="10" font-style="italic">Framework Evolution — Six Eras</text>
      </svg>
      <div class="diagram-caption">Condensed era progression from antiquity to meta-framework</div>
    </div>


    <!-- ── §9. Cross-Module Navigation ── -->
    <h2 id="cross-module">9. Cross&#x2011;Module Navigation</h2>
    <table>
      <thead><tr><th>Module</th><th>Path</th><th>Connection to History</th></tr></thead>
      <tbody>
        <tr>
          <td><a href="index.html">FCG &mdash; Framework Creation Guide</a></td>
          <td><code>docs/frameworks/creation_guide/</code></td>
          <td>Parent module; History traces the path that led to the FCG&rsquo;s creation</td>
        </tr>
        <tr>
          <td><a href="RF-Builder/RF-Builder.html">RF&#x2011;Builder</a></td>
          <td><code>docs/frameworks/creation_guide/RF-Builder/</code></td>
          <td>The construction instrument whose three-phase cycle was formalized in Era VI</td>
        </tr>
        <tr>
          <td><a href="fft.html">FFT &mdash; Framework Field Theory</a></td>
          <td><code>docs/frameworks/creation_guide/fft.html</code></td>
          <td>The meta-framework layer; FFT&rsquo;s lifecycle model (&#xA7;5) maps directly to the six eras</td>
        </tr>
        <tr>
          <td><a href="../../rtt/1/index.html">RTT/1 &mdash; Runtime Engine</a></td>
          <td><code>docs/rtt/1/</code></td>
          <td>The Seven Operators; Era III&rsquo;s flesh/thorns pattern echoes in RTT/1&rsquo;s architecture</td>
        </tr>
        <tr>
          <td><a href="principles.html">FCG Principles</a></td>
          <td><code>docs/frameworks/creation_guide/principles.html</code></td>
          <td>Foundational axioms; each era contributed a principle the FCG now formalizes</td>
        </tr>
        <tr>
          <td><a href="../../_ideas/Resonance-Time_Theory.html">RTT Origin Document</a></td>
          <td><code>docs/_ideas/Resonance-Time_Theory.html</code></td>
          <td>The foundational text from which Era VI began its formal crystallization</td>
        </tr>
      </tbody>
    </table>

  </main>
</div>

<!-- ════════════════════════════════════════════════════════════
     FOOTER
     ════════════════════════════════════════════════════════════ -->
<footer>
  <div class="seal">⟡ RECTIFIED ⟡</div>
  <p>History of Frameworks &mdash; A Six&#x2011;Era Genealogy</p>
  <p>Framework Creation Guide &middot; TriadicFrameworks &copy; 2026</p>
</footer>

<!-- ════════════════════════════════════════════════════════════
     MERMAID.JS — Live Diagram Rendering
     ════════════════════════════════════════════════════════════ -->
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
  mermaid.initialize({
    startOnLoad: true,
    theme: 'dark',
    themeVariables: {
      darkMode: true,
      background: '#0a0a0a',
      primaryColor: '#1a0a1e',
      primaryTextColor: '#e6e6e6',
      primaryBorderColor: '#ff00d4',
      lineColor: '#555555',
      secondaryColor: '#0d1b2a',
      tertiaryColor: '#1a1700',
      fontFamily: 'Segoe UI, system-ui, sans-serif',
      fontSize: '14px'
    }
  });
</script>

</body>
</html>
