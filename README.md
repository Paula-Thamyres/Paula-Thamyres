<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Paula Silva – Android Developer</title>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Sora:wght@300;400;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0d0d14;
    --card: #13131f;
    --card2: #1a1a2e;
    --border: #2a2a45;
    --purple: #9b6dff;
    --purple-light: #b98aff;
    --purple-dark: #6c3fff;
    --pink: #ff6eb4;
    --cyan: #56cfcf;
    --yellow: #ffd166;
    --green: #06d6a0;
    --text: #e8e8f0;
    --muted: #7a7a9a;
    --kotlin: #7f52ff;
    --java: #e76f00;
    --js: #f0db4f;
    --ts: #3178c6;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Sora', sans-serif;
    line-height: 1.6;
    overflow-x: hidden;
  }

  /* ── HERO ── */
  .hero {
    position: relative;
    width: 100%;
    height: 340px;
    overflow: hidden;
    background: linear-gradient(135deg, #0a0a18 0%, #1a0a2e 40%, #0d1a2e 100%);
  }

  .hero-scene {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: flex-end;
    justify-content: center;
  }

  /* Stars */
  .stars { position: absolute; inset: 0; }
  .star {
    position: absolute;
    background: #fff;
    border-radius: 50%;
    animation: twinkle 3s infinite alternate;
  }

  @keyframes twinkle {
    from { opacity: 0.2; transform: scale(1); }
    to   { opacity: 1;   transform: scale(1.3); }
  }

  /* Moon */
  .moon {
    position: absolute;
    top: 22px; right: 18%;
    width: 44px; height: 44px;
    background: linear-gradient(135deg, #ffffcc, #ffeeaa);
    border-radius: 50%;
    box-shadow: 0 0 20px 6px rgba(255,240,150,0.35);
    clip-path: polygon(30% 0%, 100% 0%, 100% 100%, 30% 100%, 0% 70%, 0% 30%);
    clip-path: ellipse(50% 50% at 60% 50%);
  }
  .moon::after {
    content:'';
    position:absolute;
    top:-4px; left:10px;
    width:44px; height:44px;
    background: #1a0a2e;
    border-radius: 50%;
  }

  /* City skyline */
  .skyline {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    display: flex;
    align-items: flex-end;
    gap: 3px;
    padding: 0 20px;
  }

  .building {
    background: linear-gradient(to top, #1a1a3a, #0d0d20);
    border-radius: 2px 2px 0 0;
    position: relative;
    flex-shrink: 0;
  }

  .building::after {
    content: '';
    position: absolute;
    inset: 0;
    background: repeating-linear-gradient(
      to right,
      transparent 0px,
      transparent 4px,
      rgba(150,100,255,0.08) 4px,
      rgba(150,100,255,0.08) 6px
    ),
    repeating-linear-gradient(
      to bottom,
      transparent 0px,
      transparent 8px,
      rgba(150,100,255,0.06) 8px,
      rgba(150,100,255,0.06) 10px
    );
  }

  /* Fairy lights */
  .fairy-lights {
    position: absolute;
    top: 30px; left: 0; right: 0;
    display: flex;
    justify-content: space-around;
    pointer-events: none;
  }

  .light-bulb {
    width: 6px; height: 8px;
    border-radius: 50% 50% 40% 40%;
    animation: glow 2s infinite alternate;
  }

  @keyframes glow {
    from { box-shadow: 0 0 4px 2px currentColor; opacity: 0.6; }
    to   { box-shadow: 0 0 10px 4px currentColor; opacity: 1; }
  }

  /* Developer illustration (CSS art) */
  .dev-scene {
    position: absolute;
    bottom: 0;
    left: 50%; transform: translateX(-50%);
    width: 520px; height: 280px;
  }

  /* Desk */
  .desk {
    position: absolute;
    bottom: 0; left: 30px; right: 30px;
    height: 18px;
    background: linear-gradient(to bottom, #3d2a1a, #2a1a0d);
    border-radius: 4px 4px 0 0;
    box-shadow: 0 -2px 20px rgba(155,109,255,0.2);
  }

  /* Monitors */
  .monitor-group {
    position: absolute;
    bottom: 18px;
    left: 50%; transform: translateX(-50%);
    display: flex;
    gap: 8px;
    align-items: flex-end;
  }

  .monitor {
    background: #0a0a12;
    border: 2px solid #2a2a50;
    border-radius: 4px;
    position: relative;
    overflow: hidden;
  }

  .monitor-screen {
    background: linear-gradient(135deg, #0d1a2e, #1a0d2e);
    width: 100%; height: 100%;
    padding: 4px;
    font-family: 'Fira Code', monospace;
    font-size: 3.5px;
    color: #56cfcf;
    overflow: hidden;
  }

  .monitor.main  { width: 160px; height: 100px; }
  .monitor.side  { width: 120px; height: 80px; }
  .monitor.small { width: 90px;  height: 65px; }

  .code-line { margin-bottom: 1.5px; white-space: nowrap; }
  .code-kw   { color: #b98aff; }
  .code-fn   { color: #56cfcf; }
  .code-str  { color: #ffd166; }
  .code-cm   { color: #4a4a6a; }

  /* Neon signs */
  .neon-keep-coding {
    position: absolute;
    top: 30px; left: 20px;
    font-family: 'Fira Code', monospace;
    font-size: 18px;
    font-weight: 600;
    color: #ff6eb4;
    text-shadow: 0 0 8px #ff6eb4, 0 0 20px #ff6eb4, 0 0 40px #ff6eb4;
    line-height: 1.3;
    animation: neon-flicker 4s infinite;
  }

  .neon-keep-coding .heart { font-size: 14px; display: block; }

  @keyframes neon-flicker {
    0%,95%,100% { opacity: 1; }
    96% { opacity: 0.7; }
    97% { opacity: 1; }
    98% { opacity: 0.5; }
  }

  /* React neon */
  .neon-react {
    position: absolute;
    top: 20px; right: 50px;
    width: 50px; height: 50px;
    color: #61dafb;
    text-shadow: 0 0 10px #61dafb;
    font-size: 44px;
    animation: spin-slow 8s linear infinite;
    display: flex; align-items: center; justify-content: center;
  }

  @keyframes spin-slow { to { transform: rotate(360deg); } }

  /* Post-its on right */
  .postits {
    position: absolute;
    top: 15px; right: 15px;
    display: flex; flex-direction: column; gap: 4px;
    background: rgba(13,13,30,0.85);
    border: 1px solid #2a2a45;
    border-radius: 6px;
    padding: 8px 12px;
    font-size: 9px;
    color: var(--muted);
  }

  .postit-item { display: flex; align-items: center; gap: 4px; }
  .postit-dot  { width: 6px; height: 6px; background: var(--purple); border-radius: 50%; }

  /* Cat decoration */
  .cat {
    position: absolute;
    bottom: 18px; left: 70px;
    width: 40px; height: 40px;
    font-size: 36px;
    filter: drop-shadow(0 0 8px rgba(155,109,255,0.6));
  }

  /* Kotlin mug */
  .mug {
    position: absolute;
    bottom: 20px; right: 100px;
    width: 28px; height: 32px;
  }
  .mug-body {
    width: 24px; height: 28px;
    background: linear-gradient(135deg, #2a1a0d, #3d2a1a);
    border-radius: 3px 3px 5px 5px;
    position: relative;
    margin: 0 auto;
  }
  .mug-body::after {
    content: 'KOTLIN\nPOWER';
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%,-50%);
    font-size: 3px;
    color: #7f52ff;
    text-align: center;
    white-space: pre;
    font-family: 'Fira Code';
    font-weight: 600;
  }
  .mug-handle {
    position: absolute;
    right: -6px; top: 6px;
    width: 8px; height: 14px;
    border: 2px solid #3d2a1a;
    border-radius: 0 6px 6px 0;
  }

  /* Candles */
  .candle {
    position: absolute;
    width: 10px;
  }
  .candle-body {
    height: 24px;
    background: linear-gradient(to right, #f5e6c8, #e8d5a8);
    border-radius: 2px;
    position: relative;
  }
  .candle-flame {
    width: 6px; height: 10px;
    background: radial-gradient(ellipse at center, #fff8dc 0%, #ffcc00 40%, #ff8800 80%, transparent 100%);
    border-radius: 50% 50% 20% 20%;
    position: absolute;
    top: -10px; left: 2px;
    animation: flicker 0.5s infinite alternate;
    box-shadow: 0 0 8px 3px rgba(255,180,0,0.6);
  }
  @keyframes flicker {
    from { transform: scaleX(1) scaleY(1) rotate(-2deg); }
    to   { transform: scaleX(0.85) scaleY(1.1) rotate(2deg); }
  }

  /* Developer person (CSS illustration) */
  .dev-person {
    position: absolute;
    bottom: 18px;
    right: 60px;
  }

  /* ── MAIN CONTENT ── */
  .container {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 20px 40px;
  }

  /* ── INTRO SECTION ── */
  .intro {
    padding: 36px 0 28px;
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 30px;
    align-items: start;
  }

  .intro-left h2 {
    font-size: 14px;
    color: var(--muted);
    font-weight: 400;
    margin-bottom: 6px;
    display: flex; align-items: center; gap: 8px;
  }

  .intro-left h1 {
    font-size: 52px;
    font-weight: 800;
    color: var(--purple);
    line-height: 1;
    margin-bottom: 20px;
    text-shadow: 0 0 40px rgba(155,109,255,0.3);
  }

  .intro-left p {
    color: var(--muted);
    font-size: 13.5px;
    margin-bottom: 10px;
    max-width: 400px;
  }

  .intro-right {
    display: flex; flex-direction: column; gap: 10px;
    min-width: 260px;
  }

  .intro-tag {
    display: flex; align-items: center; gap: 10px;
    font-size: 12.5px;
    color: var(--text);
  }

  .intro-tag .icon { font-size: 16px; }

  /* Terminal bar */
  .terminal-bar {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 20px;
    font-family: 'Fira Code', monospace;
    font-size: 13px;
    color: var(--muted);
    display: flex; align-items: center; justify-content: space-between;
    margin: 0 0 28px;
  }

  .terminal-bar .prompt { color: var(--purple); margin-right: 8px; }
  .terminal-bar .msg { color: var(--text); }
  .terminal-bar .tag { color: var(--muted); }

  .cursor {
    display: inline-block;
    width: 2px; height: 14px;
    background: var(--purple);
    animation: blink 1s step-end infinite;
    vertical-align: middle;
    margin-left: 2px;
  }

  @keyframes blink { 50% { opacity: 0; } }

  /* ── CARDS ── */
  .card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 22px;
    margin-bottom: 18px;
  }

  .card-title {
    display: flex; align-items: center; gap: 8px;
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text);
    margin-bottom: 18px;
  }

  /* ── TECH GRID ── */
  .tech-outer {
    display: grid;
    grid-template-columns: 1fr 260px;
    gap: 18px;
    margin-bottom: 18px;
  }

  .tech-categories {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0;
  }

  .tech-cat { padding: 0 10px; }
  .tech-cat:not(:last-child) { border-right: 1px solid var(--border); }

  .tech-cat-title {
    font-size: 11px;
    color: var(--muted);
    font-weight: 600;
    margin-bottom: 14px;
  }

  .tech-icons {
    display: flex; flex-wrap: wrap; gap: 12px;
  }

  .tech-icon {
    display: flex; flex-direction: column; align-items: center; gap: 5px;
    font-size: 10px; color: var(--muted);
    transition: transform 0.2s;
    cursor: default;
  }

  .tech-icon:hover { transform: translateY(-3px); color: var(--text); }

  .tech-icon .ico {
    width: 36px; height: 36px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 22px;
  }

  .ico-kotlin { background: linear-gradient(135deg, #7f52ff, #c33bde); }
  .ico-android { background: linear-gradient(135deg, #3ddc84, #0a7246); }
  .ico-jetpack { background: linear-gradient(135deg, #4285f4, #0f6dc5); }
  .ico-react { background: #1a2a3a; color: #61dafb; font-size: 24px; }
  .ico-js { background: #3a2f00; color: #f0db4f; font-weight: bold; font-size: 16px; font-family: 'Fira Code'; }
  .ico-html { background: #3a1500; color: #e34c26; font-size: 20px; }
  .ico-css { background: #001530; color: #2965f1; font-size: 20px; }
  .ico-as { background: linear-gradient(135deg, #3ddc84, #1a6640); }
  .ico-vscode { background: #001a30; color: #007acc; font-size: 20px; }
  .ico-git { background: #2a0a00; color: #f05030; font-size: 20px; }
  .ico-figma { background: #1a0a20; }

  /* Currently Studying card */
  .studying-list {
    display: flex; flex-direction: column; gap: 10px;
  }

  .studying-item {
    display: flex; align-items: center; gap: 8px;
    font-size: 13px;
  }

  .studying-dot {
    width: 8px; height: 8px;
    background: var(--purple);
    border-radius: 50%;
    flex-shrink: 0;
    box-shadow: 0 0 6px var(--purple);
  }

  /* ── GITHUB STATS ── */
  .github-grid {
    display: grid;
    grid-template-columns: 240px 1fr 220px;
    gap: 16px;
  }

  .grade-card {
    background: var(--card2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
    display: flex; flex-direction: column; gap: 8px;
  }

  .grade-name {
    font-size: 11px; color: var(--muted);
    display: flex; align-items: center; gap: 6px;
  }

  .grade-circle {
    display: flex; align-items: center; justify-content: center;
    margin: 8px auto;
    position: relative;
  }

  .grade-circle svg { transform: rotate(-90deg); }

  .grade-letter {
    position: absolute;
    font-size: 28px; font-weight: 800;
    color: var(--purple);
    text-shadow: 0 0 20px var(--purple);
  }

  .grade-stat {
    display: flex; align-items: center; justify-content: space-between;
    font-size: 11px; color: var(--muted);
  }

  .grade-stat .val { color: var(--text); font-weight: 600; }
  .grade-stat .icon { margin-right: 4px; }

  /* Big stats */
  .big-stats {
    background: var(--card2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
  }

  .big-stat-row {
    display: flex; gap: 20px;
    margin-bottom: 14px;
  }

  .big-stat {
    display: flex; flex-direction: column;
  }

  .big-stat .num {
    font-size: 28px; font-weight: 800;
    color: var(--purple);
  }

  .big-stat .lbl { font-size: 11px; color: var(--muted); }

  /* Sparkline */
  .sparkline-wrap {
    height: 50px;
    display: flex; align-items: flex-end; gap: 4px;
  }

  .spark-dot {
    width: 6px; height: 6px;
    background: var(--purple);
    border-radius: 50%;
    box-shadow: 0 0 6px var(--purple);
    align-self: flex-end;
  }

  .spark-line {
    flex: 1;
    height: 1px;
    background: var(--purple);
    opacity: 0.4;
    align-self: flex-end;
    margin-bottom: 2px;
  }

  /* Languages */
  .lang-card {
    background: var(--card2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
  }

  .lang-card-title { font-size: 11px; color: var(--muted); margin-bottom: 12px; }

  .lang-item {
    display: flex; align-items: center; gap: 8px;
    margin-bottom: 9px;
    font-size: 11px;
  }

  .lang-color {
    width: 12px; height: 12px;
    border-radius: 3px;
    flex-shrink: 0;
  }

  .lang-name { color: var(--text); flex: 1; }
  .lang-bar-wrap { width: 70px; height: 5px; background: #2a2a40; border-radius: 3px; }
  .lang-bar { height: 100%; border-radius: 3px; }
  .lang-pct { color: var(--muted); width: 32px; text-align: right; }

  /* ── PROJECTS ── */
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
  }

  .proj-card {
    background: var(--card2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px;
    display: flex; flex-direction: column; gap: 8px;
    transition: border-color 0.2s, transform 0.2s;
    cursor: default;
  }

  .proj-card:hover {
    border-color: var(--purple);
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(155,109,255,0.15);
  }

  .proj-header { display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 700; }
  .proj-icon { font-size: 16px; }
  .proj-desc { font-size: 11px; color: var(--muted); line-height: 1.5; flex: 1; }

  .proj-footer {
    display: flex; align-items: center; justify-content: space-between;
    font-size: 10px; color: var(--muted);
  }

  .proj-lang {
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 9.5px;
    font-weight: 600;
  }

  .lang-kotlin { background: rgba(127,82,255,0.2); color: #9b7fff; }
  .lang-js     { background: rgba(240,219,79,0.15); color: #f0db4f; }

  .proj-stars, .proj-forks {
    display: flex; align-items: center; gap: 3px;
  }

  /* ── CONNECT ── */
  .connect-grid {
    display: flex; gap: 12px; flex-wrap: wrap;
    margin-bottom: 10px;
  }

  .connect-btn {
    display: flex; align-items: center; gap: 10px;
    background: var(--card2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 12px 16px;
    flex: 1; min-width: 140px;
    cursor: pointer;
    transition: border-color 0.2s, transform 0.2s;
    text-decoration: none;
    color: inherit;
  }

  .connect-btn:hover {
    border-color: var(--purple);
    transform: translateY(-2px);
  }

  .connect-icon {
    width: 32px; height: 32px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
  }

  .ci-linkedin { background: #0a66c2; }
  .ci-gmail    { background: #ea4335; }
  .ci-insta    { background: linear-gradient(135deg, #f58529, #dd2a7b, #8134af); }
  .ci-portfolio { background: linear-gradient(135deg, var(--purple-dark), var(--pink)); }

  .connect-info { display: flex; flex-direction: column; }
  .connect-label { font-size: 13px; font-weight: 600; }
  .connect-sub   { font-size: 10px; color: var(--muted); }

  /* Cat bubble */
  .cat-bubble {
    position: relative;
    display: inline-flex; align-items: center; gap: 10px;
    float: right;
  }

  .bubble-text {
    background: rgba(155,109,255,0.15);
    border: 1px solid var(--purple);
    border-radius: 50%;
    width: 80px; height: 80px;
    display: flex; align-items: center; justify-content: center;
    text-align: center;
    font-size: 10px; font-weight: 700;
    color: var(--purple-light);
    line-height: 1.3;
  }

  /* Footer quote */
  .footer-quote {
    text-align: center;
    font-size: 13px;
    color: var(--muted);
    padding: 16px 0 4px;
    font-style: italic;
  }

  .footer-quote span { color: var(--purple); }

  /* ── SPARKLINE SVG ── */
  .sparkline-svg { width: 100%; height: 50px; }

  /* Dividers */
  .section-divider {
    height: 1px;
    background: var(--border);
    margin: 0 0 18px;
  }

  /* Animations */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .card { animation: fadeUp 0.5s ease both; }
  .card:nth-child(2) { animation-delay: 0.1s; }
  .card:nth-child(3) { animation-delay: 0.2s; }
  .card:nth-child(4) { animation-delay: 0.3s; }

  /* Progress ring */
  .ring-progress {
    stroke-dasharray: 251;
    stroke-dashoffset: 0;
    animation: ring-fill 1.5s ease both;
  }

  @keyframes ring-fill {
    from { stroke-dashoffset: 251; }
  }

  /* Scrollbar */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
</style>
</head>
<body>

<!-- ══════════════ HERO ══════════════ -->
<div class="hero">
  <div class="stars" id="stars"></div>

  <!-- Moon -->
  <div class="moon"></div>

  <!-- Neon signs -->
  <div class="neon-keep-coding">keep<br>coding<br><span class="heart">♥</span></div>

  <!-- React neon -->
  <div class="neon-react">⚛</div>

  <!-- Post-its top right -->
  <div class="postits">
    <div class="postit-item"><div class="postit-dot"></div> Clean Architecture</div>
    <div class="postit-item"><div class="postit-dot"></div> Android Development</div>
    <div class="postit-item"><div class="postit-dot"></div> Design Patterns</div>
  </div>

  <!-- City skyline -->
  <div class="skyline" id="skyline"></div>

  <!-- Dev scene -->
  <div class="dev-scene">
    <div class="desk"></div>

    <!-- Cat -->
    <div class="cat">🐱</div>

    <!-- Candle left -->
    <div class="candle" style="position:absolute;bottom:20px;left:130px;">
      <div class="candle-flame"></div>
      <div class="candle-body"></div>
    </div>

    <!-- Monitors -->
    <div class="monitor-group">
      <div class="monitor side">
        <div class="monitor-screen">
          <div class="code-line"><span class="code-cm">// Android App</span></div>
          <div class="code-line"><span class="code-kw">class</span> <span class="code-fn">MainActivity</span></div>
          <div class="code-line">  <span class="code-kw">: </span><span class="code-fn">AppCompatActivity</span>()</div>
          <div class="code-line">{</div>
          <div class="code-line">  <span class="code-kw">override fun</span></div>
          <div class="code-line">  <span class="code-fn">onCreate</span>(bundle)</div>
          <div class="code-line">  {</div>
          <div class="code-line">    <span class="code-fn">setContent</span> {</div>
          <div class="code-line">      <span class="code-fn">MyApp</span>()</div>
          <div class="code-line">    }</div>
          <div class="code-line">  }</div>
        </div>
      </div>
      <div class="monitor main">
        <div class="monitor-screen">
          <div class="code-line"><span class="code-kw">@Composable</span></div>
          <div class="code-line"><span class="code-kw">fun</span> <span class="code-fn">HomeScreen</span>() {</div>
          <div class="code-line">  <span class="code-fn">LazyColumn</span> {</div>
          <div class="code-line">    <span class="code-fn">item</span> {</div>
          <div class="code-line">      <span class="code-fn">Header</span>(</div>
          <div class="code-line">        title = <span class="code-str">"Paula"</span></div>
          <div class="code-line">      )</div>
          <div class="code-line">    }</div>
          <div class="code-line">    <span class="code-fn">items</span>(projects) {</div>
          <div class="code-line">      <span class="code-fn">ProjectCard</span>(it)</div>
          <div class="code-line">    }</div>
          <div class="code-line">  }</div>
          <div class="code-line">}</div>
        </div>
      </div>
      <div class="monitor small">
        <div class="monitor-screen">
          <div class="code-line"><span class="code-cm">// React.js</span></div>
          <div class="code-line"><span class="code-kw">const</span> App = () =></div>
          <div class="code-line">  &lt;<span class="code-fn">div</span>&gt;</div>
          <div class="code-line">    &lt;<span class="code-fn">Header</span> /&gt;</div>
          <div class="code-line">    &lt;<span class="code-fn">Main</span> /&gt;</div>
          <div class="code-line">  &lt;/<span class="code-fn">div</span>&gt;</div>
          <div class="code-line"><span class="code-kw">export default</span> App</div>
        </div>
      </div>
    </div>

    <!-- Mug -->
    <div class="mug" style="position:absolute;bottom:20px;right:80px;">
      <div class="mug-body"><div class="mug-handle"></div></div>
    </div>

    <!-- Candle right -->
    <div class="candle" style="position:absolute;bottom:22px;right:50px;">
      <div class="candle-flame"></div>
      <div class="candle-body" style="height:18px;background:linear-gradient(to right,#ffe8cc,#f5d8a0);"></div>
    </div>
  </div>

  <!-- Fairy lights -->
  <div class="fairy-lights" id="fairy"></div>
</div>

<!-- ══════════════ MAIN ══════════════ -->
<div class="container">

  <!-- INTRO -->
  <section class="intro">
    <div class="intro-left">
      <h2>👋 Olá, eu sou</h2>
      <h1>Paula Silva</h1>
      <p>Desenvolvedora Android apaixonada por tecnologia, interfaces modernas e experiências mobile intuitivas.</p>
      <p>Atualmente atuo com Kotlin e Jetpack Compose, criando aplicações Android com foco em arquitetura limpa, boas práticas e interfaces responsivas.</p>
      <p>Agora estou expandindo meus conhecimentos para o universo Front-end, estudando React.js para construir experiências cada vez mais completas entre mobile e web. 💜</p>
    </div>
    <div class="intro-right">
      <div class="intro-tag"><span class="icon">💻</span> Desenvolvedora Mobile Android</div>
      <div class="intro-tag"><span class="icon">📱</span> Experiência com Kotlin &amp; Jetpack Compose</div>
      <div class="intro-tag"><span class="icon">🎨</span> Interesse em UI/UX e interfaces modernas</div>
      <div class="intro-tag"><span class="icon">⚡</span> Explorando o ecossistema Front-end com React.js</div>
      <div class="intro-tag"><span class="icon">📚</span> Sempre aprendendo novas tecnologias</div>
    </div>
  </section>

  <!-- Terminal bar -->
  <div class="terminal-bar">
    <div><span class="prompt">&gt;</span> <span class="msg">Desenvolvendo soluções. Criando experiências. Evoluindo sempre.</span><span class="cursor"></span></div>
    <div class="tag">&lt;/&gt;</div>
  </div>

  <!-- TECH + STUDYING -->
  <div class="tech-outer">
    <div class="card" style="margin-bottom:0;">
      <div class="card-title">🚀 TECNOLOGIAS &amp; FERRAMENTAS</div>
      <div class="tech-categories">
        <!-- Mobile -->
        <div class="tech-cat">
          <div class="tech-cat-title">Mobile Development</div>
          <div class="tech-icons">
            <div class="tech-icon">
              <div class="ico ico-kotlin"><img src="https://upload.wikimedia.org/wikipedia/commons/7/74/Kotlin_Icon.png" width="24" onerror="this.outerHTML='K'" style="width:22px;height:22px;object-fit:contain;"></div>
              <span>Kotlin</span>
            </div>
            <div class="tech-icon">
              <div class="ico ico-android">🤖</div>
              <span>Android</span>
            </div>
            <div class="tech-icon">
              <div class="ico ico-jetpack" style="font-size:16px;color:#fff;">✦</div>
              <span style="text-align:center">Jetpack<br>Compose</span>
            </div>
          </div>
        </div>
        <!-- Front-end -->
        <div class="tech-cat">
          <div class="tech-cat-title">Front-end Journey</div>
          <div class="tech-icons">
            <div class="tech-icon">
              <div class="ico ico-react">⚛</div>
              <span>React</span>
            </div>
            <div class="tech-icon">
              <div class="ico ico-js">JS</div>
              <span>JavaScript</span>
            </div>
            <div class="tech-icon">
              <div class="ico ico-html">🔶</div>
              <span>HTML5</span>
            </div>
            <div class="tech-icon">
              <div class="ico ico-css">🔷</div>
              <span>CSS3</span>
            </div>
          </div>
        </div>
        <!-- Tools -->
        <div class="tech-cat">
          <div class="tech-cat-title">Tools</div>
          <div class="tech-icons">
            <div class="tech-icon">
              <div class="ico ico-as">🤖</div>
              <span style="text-align:center">Android<br>Studio</span>
            </div>
            <div class="tech-icon">
              <div class="ico ico-vscode" style="font-size:19px;">⬡</div>
              <span>VS Code</span>
            </div>
            <div class="tech-icon">
              <div class="ico ico-git">⬟</div>
              <span>Git<br>Figma</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Studying -->
    <div class="card" style="margin-bottom:0;">
      <div class="card-title">🌱 ATUALMENTE ESTUDANDO</div>
      <div class="studying-list">
        <div class="studying-item"><div class="studying-dot"></div>React.js</div>
        <div class="studying-item"><div class="studying-dot"></div>Componentização</div>
        <div class="studying-item"><div class="studying-dot"></div>Hooks</div>
        <div class="studying-item"><div class="studying-dot"></div>Consumo de APIs</div>
        <div class="studying-item"><div class="studying-dot"></div>Desenvolvimento Front-end moderno</div>
      </div>
    </div>
  </div>

  <!-- GITHUB STATS -->
  <div class="card">
    <div class="card-title">📊 GITHUB STATS</div>
    <div class="github-grid">

      <!-- Grade card -->
      <div class="grade-card">
        <div class="grade-name">🔗 Paula-Thamyres</div>
        <div class="grade-circle">
          <svg width="110" height="110" viewBox="0 0 110 110">
            <circle cx="55" cy="55" r="40" fill="none" stroke="#2a2a45" stroke-width="8"/>
            <circle cx="55" cy="55" r="40" fill="none" stroke="url(#ringGrad)" stroke-width="8"
              stroke-linecap="round" class="ring-progress"
              style="stroke-dasharray:251;stroke-dashoffset:20;"/>
            <defs>
              <linearGradient id="ringGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" stop-color="#9b6dff"/>
                <stop offset="100%" stop-color="#ff6eb4"/>
              </linearGradient>
            </defs>
          </svg>
          <div class="grade-letter">A+</div>
        </div>
        <div class="grade-stat"><span><span class="icon">↻</span>Commits</span><span class="val">1.2k</span></div>
        <div class="grade-stat"><span><span class="icon">⬜</span>Repositories</span><span class="val">42</span></div>
        <div class="grade-stat"><span><span class="icon">⇅</span>Pull Requests</span><span class="val">86</span></div>
        <div class="grade-stat"><span><span class="icon">◎</span>Issues</span><span class="val">15</span></div>
        <div class="grade-stat"><span><span class="icon">◇</span>Reviews</span><span class="val">120</span></div>
      </div>

      <!-- Big stats + sparkline -->
      <div class="big-stats">
        <div style="font-size:11px;color:var(--muted);margin-bottom:14px;">Estatísticas do GitHub</div>
        <div class="big-stat-row">
          <div class="big-stat"><div class="num">1.2k</div><div class="lbl">Commits</div></div>
          <div class="big-stat"><div class="num">42</div><div class="lbl">Repos</div></div>
          <div class="big-stat"><div class="num">286</div><div class="lbl">Contribuições</div></div>
        </div>
        <!-- Sparkline SVG -->
        <svg class="sparkline-svg" viewBox="0 0 220 50" preserveAspectRatio="none">
          <defs>
            <linearGradient id="spark" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stop-color="#9b6dff" stop-opacity="0.4"/>
              <stop offset="100%" stop-color="#9b6dff" stop-opacity="0"/>
            </linearGradient>
          </defs>
          <path d="M0,40 C20,35 30,20 50,25 C70,30 80,15 100,10 C120,5 130,18 150,12 C170,6 185,20 220,8"
            fill="none" stroke="#9b6dff" stroke-width="2" stroke-linecap="round"/>
          <path d="M0,40 C20,35 30,20 50,25 C70,30 80,15 100,10 C120,5 130,18 150,12 C170,6 185,20 220,8 L220,50 L0,50 Z"
            fill="url(#spark)"/>
          <!-- dots -->
          <circle cx="0"   cy="40" r="3" fill="#9b6dff"/>
          <circle cx="50"  cy="25" r="3" fill="#9b6dff"/>
          <circle cx="100" cy="10" r="3" fill="#9b6dff"/>
          <circle cx="150" cy="12" r="3" fill="#9b6dff"/>
          <circle cx="220" cy="8"  r="3" fill="#ff6eb4"/>
        </svg>
      </div>

      <!-- Languages -->
      <div class="lang-card">
        <div class="lang-card-title">Linguagens mais usadas</div>
        <div class="lang-item">
          <div class="lang-color" style="background:#7f52ff;"></div>
          <span class="lang-name">Kotlin</span>
          <div class="lang-bar-wrap"><div class="lang-bar" style="width:52.3%;background:#7f52ff;"></div></div>
          <span class="lang-pct">52.3%</span>
        </div>
        <div class="lang-item">
          <div class="lang-color" style="background:#e76f00;"></div>
          <span class="lang-name">Java</span>
          <div class="lang-bar-wrap"><div class="lang-bar" style="width:18.7%;background:#e76f00;"></div></div>
          <span class="lang-pct">18.7%</span>
        </div>
        <div class="lang-item">
          <div class="lang-color" style="background:#f0db4f;"></div>
          <span class="lang-name">JavaScript</span>
          <div class="lang-bar-wrap"><div class="lang-bar" style="width:12.8%;background:#f0db4f;"></div></div>
          <span class="lang-pct">12.8%</span>
        </div>
        <div class="lang-item">
          <div class="lang-color" style="background:#3178c6;"></div>
          <span class="lang-name">TypeScript</span>
          <div class="lang-bar-wrap"><div class="lang-bar" style="width:7.6%;background:#3178c6;"></div></div>
          <span class="lang-pct">7.6%</span>
        </div>
        <div class="lang-item">
          <div class="lang-color" style="background:#666;"></div>
          <span class="lang-name">Other</span>
          <div class="lang-bar-wrap"><div class="lang-bar" style="width:8.6%;background:#666;"></div></div>
          <span class="lang-pct">8.6%</span>
        </div>
      </div>

    </div>
  </div>

  <!-- PROJECTS -->
  <div class="card">
    <div class="card-title">✨ PROJETOS EM DESTAQUE</div>
    <div class="projects-grid">
      <div class="proj-card">
        <div class="proj-header"><span class="proj-icon">📱</span> MyTasks App</div>
        <div class="proj-desc">Aplicativo de tarefas com Jetpack Compose</div>
        <div class="proj-footer">
          <span class="proj-lang lang-kotlin">Kotlin</span>
          <span class="proj-stars">⭐ 128</span>
          <span class="proj-forks">🍴 34</span>
        </div>
      </div>
      <div class="proj-card">
        <div class="proj-header"><span class="proj-icon">🎬</span> Movie App</div>
        <div class="proj-desc">App de filmes com API, Compose e Clean Architecture</div>
        <div class="proj-footer">
          <span class="proj-lang lang-kotlin">Kotlin</span>
          <span class="proj-stars">⭐ 96</span>
          <span class="proj-forks">🍴 21</span>
        </div>
      </div>
      <div class="proj-card">
        <div class="proj-header"><span class="proj-icon">🌤️</span> Weather App</div>
        <div class="proj-desc">App de clima com integração de API e UI moderna</div>
        <div class="proj-footer">
          <span class="proj-lang lang-kotlin">Kotlin</span>
          <span class="proj-stars">⭐ 74</span>
          <span class="proj-forks">🍴 18</span>
        </div>
      </div>
      <div class="proj-card">
        <div class="proj-header"><span class="proj-icon">⚛️</span> Portfolio React</div>
        <div class="proj-desc">Meu portfólio pessoal feito com React.js</div>
        <div class="proj-footer">
          <span class="proj-lang lang-js">JavaScript</span>
          <span class="proj-stars">⭐ 53</span>
          <span class="proj-forks">🍴 12</span>
        </div>
      </div>
    </div>
  </div>

  <!-- CONNECT -->
  <div class="card">
    <div class="card-title">✉️ VAMOS NOS CONECTAR?</div>
    <div style="display:flex;align-items:flex-start;gap:20px;">
      <div class="connect-grid" style="flex:1;">
        <a class="connect-btn" href="#">
          <div class="connect-icon ci-linkedin">in</div>
          <div class="connect-info">
            <span class="connect-label">LinkedIn</span>
            <span class="connect-sub">/in/paulasilva</span>
          </div>
        </a>
        <a class="connect-btn" href="#">
          <div class="connect-icon ci-gmail">M</div>
          <div class="connect-info">
            <span class="connect-label">Gmail</span>
            <span class="connect-sub">paula.silva.dev@gmail.com</span>
          </div>
        </a>
        <a class="connect-btn" href="#">
          <div class="connect-icon ci-insta">📷</div>
          <div class="connect-info">
            <span class="connect-label">Instagram</span>
            <span class="connect-sub">@paula.dev</span>
          </div>
        </a>
        <a class="connect-btn" href="#">
          <div class="connect-icon ci-portfolio">✦</div>
          <div class="connect-info">
            <span class="connect-label">Portfólio</span>
            <span class="connect-sub">Em breve</span>
          </div>
        </a>
      </div>
      <div style="display:flex;flex-direction:column;align-items:center;gap:6px;flex-shrink:0;">
        <div style="font-size:40px;filter:drop-shadow(0 0 8px rgba(155,109,255,0.5));">🐱</div>
        <div class="bubble-text">Let's<br>build the<br>future!</div>
      </div>
    </div>
    <div class="footer-quote">✦ <span>"Transformando ideias em experiências digitais."</span> ✦</div>
  </div>

</div>

<script>
  // Generate stars
  const starsEl = document.getElementById('stars');
  for (let i = 0; i < 80; i++) {
    const s = document.createElement('div');
    s.className = 'star';
    const size = Math.random() * 2.5 + 0.5;
    s.style.cssText = `
      width:${size}px; height:${size}px;
      top:${Math.random()*100}%;
      left:${Math.random()*100}%;
      animation-delay:${Math.random()*3}s;
      animation-duration:${2+Math.random()*3}s;
    `;
    starsEl.appendChild(s);
  }

  // Generate city skyline
  const skylineEl = document.getElementById('skyline');
  const buildingCount = 28;
  const colors = ['#0d0d20','#13132a','#0a0a18','#1a1a35'];
  for (let i = 0; i < buildingCount; i++) {
    const b = document.createElement('div');
    b.className = 'building';
    const w = 18 + Math.random() * 40;
    const h = 40 + Math.random() * 160;
    b.style.cssText = `
      width:${w}px; height:${h}px;
      background: linear-gradient(to top, ${colors[Math.floor(Math.random()*colors.length)]}, #0a0a15);
      flex-shrink:0;
    `;
    skylineEl.appendChild(b);
  }

  // Fairy lights
  const fairyEl = document.getElementById('fairy');
  const lightColors = ['#ff6eb4','#9b6dff','#ffd166','#56cfcf','#ff8c42'];
  for (let i = 0; i < 30; i++) {
    const l = document.createElement('div');
    l.className = 'light-bulb';
    const c = lightColors[Math.floor(Math.random()*lightColors.length)];
    l.style.cssText = `
      background:${c}; color:${c};
      animation-delay:${Math.random()*2}s;
      animation-duration:${1.5+Math.random()*2}s;
    `;
    fairyEl.appendChild(l);
  }

  // Animate language bars on scroll
  const bars = document.querySelectorAll('.lang-bar');
  const widths = [];
  bars.forEach(b => {
    widths.push(b.style.width);
    b.style.width = '0';
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        bars.forEach((b, i) => {
          setTimeout(() => {
            b.style.transition = 'width 0.8s ease';
            b.style.width = widths[i];
          }, i * 120);
        });
        observer.disconnect();
      }
    });
  }, { threshold: 0.3 });

  const langCard = document.querySelector('.lang-card');
  if (langCard) observer.observe(langCard);
</script>
</body>
</html>
