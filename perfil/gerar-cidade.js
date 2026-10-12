// Gera perfil/cidade.svg: a cidade dia e noite com os carros.
// Cada prédio é uma semana real de contribuições (dados do GitHub).
// Roda sozinho pelo GitHub Actions (.github/workflows/cidade.yml).
const fs = require("fs");
const path = require("path");

const USUARIO = process.env.USUARIO || "Paula-Thamyres";
const TOKEN = process.env.GITHUB_TOKEN;
const FONTE = "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";

async function buscarDados() {
  const query = `query($login: String!) { user(login: $login) { contributionsCollection { contributionCalendar { totalContributions weeks { contributionDays { contributionCount } } } } } }`;
  const r = await fetch("https://api.github.com/graphql", {
    method: "POST",
    headers: { Authorization: `bearer ${TOKEN}`, "Content-Type": "application/json", "User-Agent": "cidade-paula" },
    body: JSON.stringify({ query, variables: { login: USUARIO } })
  });
  const j = await r.json();
  if (!j.data || !j.data.user) throw new Error("Não consegui ler as contribuições: " + JSON.stringify(j));
  const cal = j.data.user.contributionsCollection.contributionCalendar;
  return { total: cal.totalContributions, semanas: cal.weeks.map(w => w.contributionDays.reduce((a, d) => a + d.contributionCount, 0)) };
}

function desenhar({ total, semanas }) {
  let sd = 25;
  const rnd = () => (sd = (sd * 1103515245 + 12345) % 2147483648) / 2147483648;
  const R = (a, b) => a + rnd() * (b - a);
  const P = { sky: ["#05040f", "#140c2e", "#2a1450"], body: "#140e2a", edge: "#3b2a6b", back: "#1d1438", win: ["#f472b6", "#22d3ee", "#c4b5fd"], ground: "#0d0920", line: "#f472b6" };
  const H = 260, gy = H - 34, maxH = gy - 70;
  const anim = (vals) => `<animate attributeName="stop-color" values="${vals}" dur="16s" repeatCount="indefinite"/>`;
  let s = `<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">`
    + `<stop offset="0" stop-color="${P.sky[0]}">${anim(`${P.sky[0]};#3b2a6b;#7dd3fc;#3b2a6b;${P.sky[0]}`)}</stop>`
    + `<stop offset=".65" stop-color="${P.sky[1]}">${anim(`${P.sky[1]};#9d174d;#c4b5fd;#9d174d;${P.sky[1]}`)}</stop>`
    + `<stop offset="1" stop-color="${P.sky[2]}">${anim(`${P.sky[2]};#f472b6;#fde68a;#f472b6;${P.sky[2]}`)}</stop>`
    + `</linearGradient><clipPath id="borda"><rect width="760" height="${H}" rx="14"/></clipPath></defs><g clip-path="url(#borda)">`;
  s += `<rect width="760" height="${H}" fill="url(#sky)"/>`;
  // estrelas
  for (let i = 0; i < 60; i++) s += `<circle cx="${R(6, 754).toFixed(0)}" cy="${R(4, gy - 80).toFixed(0)}" r="${R(.4, 1.4).toFixed(1)}" fill="#fff" class="tw" style="animation-delay:${R(0, 3).toFixed(1)}s"/>`;
  // planeta com a lua girando
  const cx = 640, cy = 62, r = 26, d = r * 1.75;
  s += `<defs><radialGradient id="pl" cx=".35" cy=".35" r=".75"><stop offset="0" stop-color="#fbcfe8"/><stop offset=".55" stop-color="#f472b6"/><stop offset="1" stop-color="#9d174d"/></radialGradient></defs>`
    + `<circle cx="${cx}" cy="${cy}" r="${r}" fill="url(#pl)" style="filter:drop-shadow(0 0 ${r * .45}px #f472b6)"/>`
    + `<path d="M${cx - r * .9} ${cy - r * .2} Q${cx} ${cy - r * .05} ${cx + r * .9} ${cy - r * .25}" stroke="#fbcfe8" stroke-width="${r * .08}" fill="none" opacity=".4"/>`
    + `<path d="M${cx - r * .85} ${cy + r * .3} Q${cx} ${cy + r * .45} ${cx + r * .85} ${cy + r * .25}" stroke="#9d174d" stroke-width="${r * .1}" fill="none" opacity=".35"/>`
    + `<g><circle cx="${cx + d}" cy="${cy}" r="4.5" fill="#22d3ee" style="filter:drop-shadow(0 0 4px #22d3ee)"/><animateTransform attributeName="transform" type="rotate" from="0 ${cx} ${cy}" to="360 ${cx} ${cy}" dur="7s" repeatCount="indefinite"/></g>`;
  // prédios do fundo
  let back = "";
  for (let i = 0; i < 46; i++) { const h = R(30, maxH * .55), x = i * 17 - 6; back += `<rect x="${x.toFixed(0)}" y="${(gy - h).toFixed(0)}" width="16" height="${h.toFixed(0)}" fill="${P.back}"/>`; }
  // prédios da frente: um por semana
  const n = semanas.length, passo = 732 / n, w = passo * .876, max = Math.max(1, ...semanas);
  let front = "";
  semanas.forEach((v, i) => {
    const k = v / max, h = 26 + k * maxH, x = 14 + i * passo, y = gy - h, top = i % 6;
    front += `<rect x="${x.toFixed(1)}" y="${y.toFixed(1)}" width="${w.toFixed(1)}" height="${h.toFixed(1)}" fill="${P.body}" stroke="${P.edge}" stroke-width=".8"/>`;
    if (top === 1 && k > .25) front += `<line x1="${(x + w / 2).toFixed(1)}" y1="${y.toFixed(1)}" x2="${(x + w / 2).toFixed(1)}" y2="${(y - 14).toFixed(1)}" stroke="${P.edge}" stroke-width="1.2"/><circle cx="${(x + w / 2).toFixed(1)}" cy="${(y - 14).toFixed(1)}" r="1.8" fill="#f43f5e"><animate attributeName="opacity" values="1;.1;1" dur="1.6s" repeatCount="indefinite"/></circle>`;
    if (top === 3 && k > .2) front += `<rect x="${(x + 2.5).toFixed(1)}" y="${(y - 7).toFixed(1)}" width="${(w - 5).toFixed(1)}" height="7" fill="${P.body}" stroke="${P.edge}" stroke-width=".8"/>`;
    if (top === 5 && k > .35) front += `<path d="M${x.toFixed(1)} ${y.toFixed(1)} L${(x + w / 2).toFixed(1)} ${(y - 12).toFixed(1)} L${(x + w).toFixed(1)} ${y.toFixed(1)} Z" fill="${P.body}" stroke="${P.edge}" stroke-width=".8"/>`;
    for (let wy = y + 6; wy < gy - 6; wy += 8) for (let c = 0; c < 2; c++) if (rnd() < .12 + k * .72) {
      const col = P.win[Math.floor(rnd() * P.win.length)];
      front += `<rect x="${(x + w * .18 + c * w * .39).toFixed(1)}" y="${wy.toFixed(1)}" width="3" height="3.6" fill="${col}"${rnd() < .25 ? ` class="tw" style="animation-delay:${R(0, 3).toFixed(1)}s"` : ""}/>`;
    }
  });
  s += `<g opacity=".75">${back}</g>${front}`;
  // rua e carros
  s += `<rect y="${gy}" width="760" height="34" fill="${P.ground}"/><line x1="0" y1="${gy + .5}" x2="760" y2="${gy + .5}" stroke="${P.line}" stroke-width="1.5" opacity=".7" style="filter:drop-shadow(0 0 4px ${P.line})"/>`;
  ["#fde047", "#f472b6", "#22d3ee"].forEach((c, i) => {
    s += `<rect y="${gy + 18}" width="18" height="2.5" rx="1" fill="${c}" style="filter:drop-shadow(0 0 3px #fff)"><animate attributeName="x" from="${i % 2 ? 780 : -20}" to="${i % 2 ? -20 : 780}" dur="${4 + i}s" begin="${i}s" repeatCount="indefinite"/></rect>`;
  });
  s += `<text x="20" y="28" font-size="12.5" fill="#f5f3ff" font-family="JB, monospace">${total} contribuições no último ano · cada prédio é uma semana</text></g>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 ${H}" width="760" height="${H}" role="img" aria-label="${total} contribuições no último ano">
<style>
@font-face{font-family:"JB";src:url(data:font/woff;base64,${FONTE}) format("woff");}
@keyframes tw{0%,100%{opacity:.25}50%{opacity:1}}
.tw{animation:tw 2.8s ease-in-out infinite}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>
${s}
</svg>
`;
}

(async () => {
  const dados = process.env.DADOS_TESTE ? JSON.parse(fs.readFileSync(process.env.DADOS_TESTE, "utf8")) : await buscarDados();
  const destino = path.join(__dirname, "cidade.svg");
  fs.writeFileSync(destino, desenhar(dados));
  console.log(`Cidade gerada: ${dados.total} contribuições, ${dados.semanas.length} semanas -> ${destino}`);
})().catch(e => { console.error(e.message); process.exit(1); });
