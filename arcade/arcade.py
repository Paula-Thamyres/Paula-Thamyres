"""
Arcade da Paula — três jogos no README do GitHub: Quiz de JavaScript, Memória Dev e Xadrez Candy.

Como funciona:
  - Cada jogada é uma issue com título no formato  arcade|<jogo>|<jogada>
  - O GitHub Actions roda  python arcade/arcade.py play  com os dados da issue
  - O script atualiza o estado (arcade/estado.json), gera as imagens e reescreve o README
    entre os marcadores <!-- ARCADE:... -->

Comandos:
  python arcade/arcade.py init   -> gera as imagens fixas, zera o estado e monta as seções do README
  python arcade/arcade.py play   -> processa a issue (variáveis ISSUE_TITLE, ISSUE_USER, ISSUE_NUMBER)
"""
import html
import json
import os
import random
import re
import sys
from urllib.parse import quote

import chess

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA = os.path.join(RAIZ, "arcade")
IMG = os.path.join(PASTA, "img")
OUT = os.path.join(PASTA, "out")
ESTADO = os.path.join(PASTA, "estado.json")
PERGUNTAS = os.path.join(PASTA, "perguntas.json")
README = os.path.join(RAIZ, "README.md")
REPO = os.environ.get("GITHUB_REPOSITORY", "Paula-Thamyres/Paula-Thamyres")

PONTOS = {"quiz": 2, "par": 1, "xadrez": 1, "mate": 5}
SIMBOLOS = ["{ }", "</>", "=>", "[ ]", "&&", "( )", "===", "#"]
NOMES_PECA = {chess.PAWN: "Peão", chess.KNIGHT: "Cavalo", chess.BISHOP: "Bispo",
              chess.ROOK: "Torre", chess.QUEEN: "Dama", chess.KING: "Rei"}

# Paleta do perfil
ROXO, ROXO_ESC, LILAS, ROSA, ROSA_CLARO, CIANO = "#8b5cf6", "#4c1d95", "#c4b5fd", "#f472b6", "#fbcfe8", "#22d3ee"
FONTE = "Segoe UI, Helvetica, Arial, sans-serif"
MONO = "Consolas, Menlo, 'DejaVu Sans Mono', monospace"


# ----------------------------------------------------------------------------- utilidades
def esc(texto):
    return html.escape(str(texto), quote=True)


def salvar(caminho, conteudo):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)


def link_issue(titulo, corpo=None):
    corpo = corpo or ("Só clicar em **Create** (ou **Submit new issue**) aqui embaixo. "
                      "Em uns 30 segundos o robô faz a jogada, atualiza o perfil e fecha esta issue. 💜")
    return f"https://github.com/{REPO}/issues/new?title={quote(titulo)}&body={quote(corpo)}"


def carregar_estado():
    with open(ESTADO, encoding="utf-8") as f:
        return json.load(f)


def salvar_estado(estado):
    salvar(ESTADO, json.dumps(estado, ensure_ascii=False, indent=2))


def pontuar(estado, usuario, jogo, pontos):
    r = estado["ranking"].setdefault(usuario, {"pontos": 0, "quiz": 0, "memoria": 0, "xadrez": 0})
    r["pontos"] += pontos
    r[jogo] += 1


# ----------------------------------------------------------------------------- imagens fixas
def svg_banner():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="150" viewBox="0 0 900 150">
<defs>
  <linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1a1033"/><stop offset="1" stop-color="#3b1a63"/></linearGradient>
  <filter id="brilho" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <pattern id="p" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" fill="#ffffff" opacity="0.08"/></pattern>
</defs>
<rect width="900" height="150" rx="18" fill="url(#g)"/>
<rect width="900" height="150" rx="18" fill="url(#p)"/>
<text x="40" y="74" font-family="{FONTE}" font-size="42" font-weight="800" letter-spacing="3" fill="#ffffff" filter="url(#brilho)">ARCADE <tspan fill="{ROSA}">DA PAULA</tspan></text>
<text x="42" y="108" font-family="{MONO}" font-size="16" fill="{LILAS}">3 jogos · clique, envie a issue e o robô joga com você</text>
<g transform="translate(620 32)">
  <rect width="78" height="86" rx="14" fill="{ROSA}"/><text x="39" y="60" text-anchor="middle" font-family="{FONTE}" font-size="44" font-weight="800" fill="#3b0a2a">?</text>
  <text x="39" y="104" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{ROSA_CLARO}">QUIZ</text>
</g>
<g transform="translate(712 32)">
  <rect x="8" y="-4" width="62" height="86" rx="12" fill="{ROXO_ESC}" transform="rotate(8 39 43)"/>
  <rect width="78" height="86" rx="14" fill="{ROXO}"/><text x="39" y="56" text-anchor="middle" font-family="{MONO}" font-size="24" font-weight="700" fill="#ffffff">&lt;/&gt;</text>
  <text x="39" y="104" text-anchor="middle" font-family="{MONO}" font-size="11" fill="{LILAS}">MEMÓRIA</text>
</g>
<g transform="translate(804 32)">
  <rect width="78" height="86" rx="14" fill="{CIANO}"/>
  <circle cx="39" cy="28" r="10" fill="#0e4a57"/><path d="M27 66 Q29 46 39 42 Q49 46 51 66 Z" fill="#0e4a57"/><rect x="23" y="64" width="32" height="8" rx="4" fill="#0e4a57"/>
  <text x="39" y="104" text-anchor="middle" font-family="{MONO}" font-size="11" fill="#a5f3fc">XADREZ</text>
</g>
</svg>'''


def svg_opcao(letra, texto):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="380" height="60" viewBox="0 0 380 60">
<rect x="1" y="1" width="378" height="58" rx="14" fill="#1f1633" stroke="{ROXO}" stroke-width="2"/>
<circle cx="32" cy="30" r="17" fill="{ROSA}"/>
<text x="32" y="36" text-anchor="middle" font-family="{FONTE}" font-size="17" font-weight="800" fill="#3b0a2a">{letra}</text>
<text x="62" y="37" font-family="{MONO}" font-size="18" font-weight="600" fill="#f5f3ff">{esc(texto)}</text>
</svg>'''


def svg_pergunta(num, total, p):
    linhas = p.get("codigo", [])
    h = 112 + len(linhas) * 26 + (22 if linhas else 0)
    codigo = ""
    if linhas:
        codigo = f'<rect x="32" y="96" width="696" height="{len(linhas) * 26 + 18}" rx="10" fill="#0b0f17"/>'
        for i, linha in enumerate(linhas):
            codigo += f'<text x="50" y="{122 + i * 26}" font-family="{MONO}" font-size="17" fill="{CIANO}">{esc(linha)}</text>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{h}" viewBox="0 0 760 {h}">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1c1236"/><stop offset="1" stop-color="#2a1450"/></linearGradient></defs>
<rect width="760" height="{h}" rx="18" fill="url(#g)"/>
<text x="32" y="40" font-family="{MONO}" font-size="13" font-weight="700" letter-spacing="2" fill="{ROSA}">PERGUNTA {num:02d} DE {total:02d} · JAVASCRIPT</text>
<text x="32" y="76" font-family="{FONTE}" font-size="25" font-weight="700" fill="#ffffff">{esc(p["pergunta"])}</text>
{codigo}
</svg>'''


def svg_carta(tipo, simbolo=""):
    """tipo: verso | aberta | par"""
    if tipo == "verso":
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="84" height="108" viewBox="0 0 84 108">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{ROXO}"/><stop offset="1" stop-color="{ROXO_ESC}"/></linearGradient></defs>
<rect x="3" y="3" width="78" height="102" rx="12" fill="url(#g)" stroke="{LILAS}" stroke-width="2"/>
<rect x="10" y="10" width="64" height="88" rx="8" fill="none" stroke="#ffffff" stroke-opacity="0.25" stroke-dasharray="3 4"/>
<text x="42" y="66" text-anchor="middle" font-family="{FONTE}" font-size="36" font-weight="800" fill="#ffffff">?</text>
</svg>'''
    par = tipo == "par"
    fundo, borda, cor = (ROSA, "#ffffff", "#3b0a2a") if par else ("#ede9fe", ROSA, ROXO_ESC)
    tam = 26 if len(simbolo) <= 2 else 22
    selo = f'<circle cx="68" cy="16" r="10" fill="#ffffff"/><path d="M63 16 l4 4 l7 -8" stroke="{ROSA}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/>' if par else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="84" height="108" viewBox="0 0 84 108">
<rect x="3" y="3" width="78" height="102" rx="12" fill="{fundo}" stroke="{borda}" stroke-width="3"/>
<text x="42" y="64" text-anchor="middle" font-family="{MONO}" font-size="{tam}" font-weight="800" fill="{cor}">{esc(simbolo)}</text>
{selo}
</svg>'''


def gerar_imagens_fixas():
    salvar(os.path.join(IMG, "banner.svg"), svg_banner())
    salvar(os.path.join(IMG, "memoria", "verso.svg"), svg_carta("verso"))
    for i, s in enumerate(SIMBOLOS):
        salvar(os.path.join(IMG, "memoria", f"carta-{i}.svg"), svg_carta("aberta", s))
        salvar(os.path.join(IMG, "memoria", f"par-{i}.svg"), svg_carta("par", s))


# ----------------------------------------------------------------------------- xadrez candy
TIME = {chess.WHITE: {"corpo": "#ec4899", "luz": "#fdf2f8", "linha": "#831843"},
        chess.BLACK: {"corpo": "#7c3aed", "luz": "#ede9fe", "linha": "#2e1065"}}


def desenho_peca(tipo, cor):
    t = TIME[cor]
    a = f'fill="{t["corpo"]}" stroke="{t["linha"]}" stroke-width="2.2" stroke-linejoin="round"'
    base = f'<rect x="12" y="39" width="28" height="7" rx="3.5" {a}/>'
    brilho = f'fill="{t["luz"]}" opacity="0.55"'
    if tipo == chess.PAWN:
        corpo = f'<path d="M18 40 Q19 28 26 26 Q33 28 34 40 Z" {a}/><circle cx="26" cy="19" r="7.5" {a}/><circle cx="23.5" cy="16.5" r="2.4" {brilho}/>'
    elif tipo == chess.ROOK:
        corpo = (f'<rect x="17" y="21" width="18" height="19" rx="2" {a}/>'
                 f'<path d="M14 12 h6 v4 h3 v-4 h6 v4 h3 v-4 h6 v10 h-24 Z" {a}/><rect x="18" y="14" width="3" height="5" rx="1.5" {brilho}/>')
    elif tipo == chess.BISHOP:
        corpo = (f'<path d="M18 40 Q16 28 26 13 Q36 28 34 40 Z" {a}/><circle cx="26" cy="10" r="3.4" {a}/>'
                 f'<path d="M29 20 L23 28" stroke="{t["linha"]}" stroke-width="2.4" stroke-linecap="round"/><ellipse cx="22" cy="27" rx="2" ry="4" {brilho}/>')
    elif tipo == chess.KNIGHT:
        corpo = (f'<path d="M17 40 L18.5 31 Q15 25 20 18 L23 10 L27 15 Q37 16 37 27 L34 32 L28.5 29 L27.5 33.5 L34 40 Z" {a}/>'
                 f'<circle cx="25.5" cy="19.5" r="1.8" fill="{t["linha"]}"/><path d="M21 22 Q20 27 22 31" stroke="{t["luz"]}" stroke-width="2" fill="none" opacity="0.6" stroke-linecap="round"/>')
    elif tipo == chess.QUEEN:
        corpo = (f'<path d="M15 40 L16.5 21 L21 30 L26 17 L31 30 L35.5 21 L37 40 Z" {a}/>'
                 f'<circle cx="16.5" cy="18.5" r="3" {a}/><circle cx="26" cy="14.5" r="3" {a}/><circle cx="35.5" cy="18.5" r="3" {a}/>'
                 f'<circle cx="26" cy="31" r="2.6" fill="#fde047" stroke="{t["linha"]}" stroke-width="1.2"/>')
    else:  # rei
        corpo = (f'<path d="M17 40 Q16 26 26 22 Q36 26 35 40 Z" {a}/>'
                 f'<rect x="24" y="7" width="4" height="14" rx="1.5" fill="#fde047" stroke="{t["linha"]}" stroke-width="1.6"/>'
                 f'<rect x="20" y="10.5" width="12" height="4" rx="1.5" fill="#fde047" stroke="{t["linha"]}" stroke-width="1.6"/>'
                 f'<ellipse cx="22" cy="30" rx="2.2" ry="4.5" {brilho}/>')
    return base + corpo


def svg_tabuleiro(board, ultimo=None):
    S, M = 52, 34
    total = S * 8 + M * 2
    partes = [f'<rect width="{total}" height="{total}" rx="24" fill="{ROSA_CLARO}"/>',
              f'<rect x="{M - 6}" y="{M - 6}" width="{S * 8 + 12}" height="{S * 8 + 12}" rx="14" fill="#ffffff"/>']
    destaque = set()
    if ultimo:
        destaque = {ultimo.from_square, ultimo.to_square}
    rei_xeque = board.king(board.turn) if board.is_check() else None
    for linha in range(8):
        for col in range(8):
            casa = chess.square(col, 7 - linha)
            x, y = M + col * S, M + linha * S
            cor = "#e9d5ff" if (linha + col) % 2 else "#fff1f8"
            partes.append(f'<rect x="{x + 1.5}" y="{y + 1.5}" width="{S - 3}" height="{S - 3}" rx="9" fill="{cor}"/>')
            if casa in destaque:
                partes.append(f'<rect x="{x + 1.5}" y="{y + 1.5}" width="{S - 3}" height="{S - 3}" rx="9" fill="#fde047" opacity="0.55"/>')
            if casa == rei_xeque:
                partes.append(f'<rect x="{x + 1.5}" y="{y + 1.5}" width="{S - 3}" height="{S - 3}" rx="9" fill="none" stroke="#e11d48" stroke-width="3"/>')
            peca = board.piece_at(casa)
            if peca:
                partes.append(f'<g transform="translate({x} {y})">{desenho_peca(peca.piece_type, peca.color)}</g>')
    for i in range(8):
        letra, num = "ABCDEFGH"[i], str(8 - i)
        partes.append(f'<text x="{M + i * S + S / 2}" y="{total - 11}" text-anchor="middle" font-family="{FONTE}" font-size="14" font-weight="700" fill="#9d174d">{letra}</text>')
        partes.append(f'<text x="{M / 2}" y="{M + i * S + S / 2 + 5}" text-anchor="middle" font-family="{FONTE}" font-size="14" font-weight="700" fill="#9d174d">{num}</text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{total}" height="{total}" viewBox="0 0 {total} {total}">{"".join(partes)}</svg>'


# ----------------------------------------------------------------------------- ranking
def svg_ranking(ranking):
    top = sorted(ranking.items(), key=lambda kv: (-kv[1]["pontos"], kv[0].lower()))[:8]
    h = 112 + max(1, len(top)) * 46
    p = [f'<rect width="760" height="{h}" rx="18" fill="#1c1236"/>',
         f'<text x="32" y="46" font-family="{FONTE}" font-size="24" font-weight="800" letter-spacing="2" fill="#ffffff">RANKING DO <tspan fill="{ROSA}">ARCADE</tspan></text>',
         f'<text x="32" y="74" font-family="{MONO}" font-size="13" fill="{LILAS}">quiz certo +2 · par na memória +1 · jogada no xadrez +1 · xeque-mate +5</text>']
    if not top:
        p.append(f'<text x="32" y="124" font-family="{FONTE}" font-size="17" fill="#e9d5ff">Ninguém jogou ainda. Seja a primeira pessoa a pontuar!</text>')
    medalhas = ["#fde047", "#e5e7eb", "#fdba74"]
    for i, (nome, r) in enumerate(top):
        y = 96 + i * 46
        p.append(f'<rect x="24" y="{y}" width="712" height="38" rx="10" fill="{"#2e1a52" if i == 0 else "#241640"}"/>')
        cor = medalhas[i] if i < 3 else ROXO
        p.append(f'<circle cx="48" cy="{y + 19}" r="13" fill="{cor}"/><text x="48" y="{y + 24}" text-anchor="middle" font-family="{FONTE}" font-size="13" font-weight="800" fill="#1c1236">{i + 1}</text>')
        p.append(f'<text x="74" y="{y + 25}" font-family="{FONTE}" font-size="17" font-weight="600" fill="#ffffff">{esc(nome)}</text>')
        p.append(f'<text x="420" y="{y + 25}" font-family="{MONO}" font-size="13" fill="{LILAS}">quiz {r["quiz"]} · pares {r["memoria"]} · lances {r["xadrez"]}</text>')
        p.append(f'<text x="716" y="{y + 26}" text-anchor="end" font-family="{FONTE}" font-size="20" font-weight="800" fill="{ROSA}">{r["pontos"]} pts</text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{h}" viewBox="0 0 760 {h}">{"".join(p)}</svg>'


# ----------------------------------------------------------------------------- estado inicial
def novo_baralho(semente):
    cartas = list(range(len(SIMBOLOS))) * 2
    random.Random(semente).shuffle(cartas)
    return {"cartas": cartas, "pares": [], "abertas": [], "jogadas": 0, "ultimo": "", "concluidos": []}


def estado_inicial():
    return {
        "versao": 0,
        "quiz": {"atual": 0, "ultimo": "", "respondidas": 0},
        "memoria": novo_baralho(2026),
        "xadrez": {"fen": chess.STARTING_FEN, "lances": [], "ultimo": "", "partidas": 0},
        "ranking": {},
    }


# ----------------------------------------------------------------------------- jogadas
def jogar_quiz(estado, usuario, jogada):
    perguntas = json.load(open(PERGUNTAS, encoding="utf-8"))
    q = estado["quiz"]
    if jogada not in "ABCD" or len(jogada) != 1:
        return "Não entendi a resposta. Use os botões A, B, C ou D do perfil. 💜"
    p = perguntas[q["atual"]]
    escolha = "ABCD".index(jogada)
    if escolha == p["certa"]:
        pontuar(estado, usuario, "quiz", PONTOS["quiz"])
        q["ultimo"] = f"✅ <b>@{usuario}</b> acertou a pergunta {q['atual'] + 1}: <code>{esc(p['opcoes'][escolha])}</code>"
        q["atual"] = (q["atual"] + 1) % len(perguntas)
        q["respondidas"] += 1
        return f"✅ Acertou, @{usuario}! +{PONTOS['quiz']} pontos.\n\n💡 {p['explicacao']}\n\nJá tem uma pergunta nova esperando no perfil."
    q["ultimo"] = f"❌ <b>@{usuario}</b> tentou <b>{jogada}</b> na pergunta {q['atual'] + 1}. Quem acerta?"
    return f"❌ Não foi dessa vez, @{usuario}. A pergunta continua aberta: tente outra alternativa!"


def jogar_memoria(estado, usuario, jogada):
    m = estado["memoria"]
    if not jogada.isdigit() or not 0 <= int(jogada) < len(m["cartas"]):
        return "Não encontrei essa carta. Clique em uma carta virada para baixo no perfil."
    i = int(jogada)
    if len(m["abertas"]) == 2:  # par errado da jogada anterior: desvira antes
        m["abertas"] = []
    if i in m["pares"] or i in m["abertas"]:
        return "Essa carta já está virada. Escolha outra! 🃏"
    m["abertas"].append(i)
    simbolo = SIMBOLOS[m["cartas"][i]]
    if len(m["abertas"]) == 1:
        m["ultimo"] = f"🃏 <b>@{usuario}</b> virou <code>{esc(simbolo)}</code>. Qual é o par?"
        return f"Você virou `{simbolo}`. Agora vire outra carta para tentar formar o par!"
    m["jogadas"] += 1
    a, b = m["abertas"]
    if m["cartas"][a] == m["cartas"][b]:
        m["pares"] += [a, b]
        m["abertas"] = []
        pontuar(estado, usuario, "memoria", PONTOS["par"])
        if len(m["pares"]) == len(m["cartas"]):
            jogadas = m["jogadas"]
            concluidos = (m["concluidos"] + [jogadas])[-5:]
            estado["memoria"] = novo_baralho(int(os.environ.get("ISSUE_NUMBER", "0")) + jogadas)
            estado["memoria"]["concluidos"] = concluidos
            estado["memoria"]["ultimo"] = f"🏁 <b>@{usuario}</b> fechou o jogo em {jogadas} jogadas! Cartas embaralhadas de novo."
            return f"🎉 Par `{simbolo}` e fim de jogo! Vocês completaram em {jogadas} jogadas. Embaralhei tudo de novo."
        m["ultimo"] = f"✨ <b>@{usuario}</b> encontrou o par <code>{esc(simbolo)}</code>!"
        return f"✨ Par encontrado: `{simbolo}`! +{PONTOS['par']} ponto."
    m["ultimo"] = f"😅 <b>@{usuario}</b> virou <code>{esc(SIMBOLOS[m['cartas'][a]])}</code> e <code>{esc(simbolo)}</code>: não formam par. Elas desviram na próxima jogada."
    return "Quase! Essas duas não formam par. Elas ficam visíveis até a próxima jogada, então memorize. 😉"


def jogar_xadrez(estado, usuario, jogada):
    x = estado["xadrez"]
    board = chess.Board(x["fen"])
    if jogada == "NOVO":
        if not board.is_game_over():
            return "A partida ainda está rolando! Dá para reiniciar só quando ela terminar."
        x.update({"fen": chess.STARTING_FEN, "lances": [], "partidas": x["partidas"] + 1,
                  "ultimo": f"🆕 <b>@{usuario}</b> começou uma nova partida."})
        return "Nova partida começou! As rosas jogam primeiro. ♟️"
    if not re.fullmatch(r"[A-H][1-8][A-H][1-8]", jogada):
        return "Não entendi essa jogada. Use os links de jogada do perfil."
    lance = chess.Move.from_uci(jogada.lower())
    peca = board.piece_at(lance.from_square)
    if peca and peca.piece_type == chess.PAWN and chess.square_rank(lance.to_square) in (0, 7):
        lance = chess.Move(lance.from_square, lance.to_square, promotion=chess.QUEEN)
    if lance not in board.legal_moves:
        return "Essa jogada não é válida agora (talvez alguém tenha jogado antes de você). Confira o tabuleiro e tente de novo!"
    nome = NOMES_PECA[peca.piece_type]
    board.push(lance)
    x["fen"] = board.fen()
    x["lances"] = (x["lances"] + [[jogada[:2], jogada[2:], usuario]])[-5:]
    pontuar(estado, usuario, "xadrez", PONTOS["xadrez"])
    if board.is_checkmate():
        estado["ranking"][usuario]["pontos"] += PONTOS["mate"]
        x["ultimo"] = f"🏆 <b>@{usuario}</b> deu <b>xeque-mate</b> com {nome} {jogada[:2]} → {jogada[2:]}!"
        return f"🏆 XEQUE-MATE! Você venceu a partida, @{usuario}! +{PONTOS['xadrez'] + PONTOS['mate']} pontos."
    if board.is_game_over():
        x["ultimo"] = f"🤝 Empate depois do lance de <b>@{usuario}</b>."
        return "A partida terminou empatada! Qualquer pessoa pode começar outra pelo perfil."
    extra = " Xeque! ⚠️" if board.is_check() else ""
    x["ultimo"] = f"♟️ <b>@{usuario}</b> jogou {nome} {jogada[:2]} → {jogada[2:]}.{extra}"
    return f"Lance feito: {nome} {jogada[:2]} → {jogada[2:]}.{extra} +{PONTOS['xadrez']} ponto."


# ----------------------------------------------------------------------------- README
def bloco_quiz(estado):
    perguntas = json.load(open(PERGUNTAS, encoding="utf-8"))
    q = estado["quiz"]
    n = q["atual"]
    p = perguntas[n]
    botoes = []
    for k in range(4):
        letra = "ABCD"[k]
        botoes.append(f'<a href="{link_issue(f"arcade|quiz|{letra}")}"><img src="arcade/out/opcao-{letra}-{estado['versao']}.svg" width="49%" alt="{letra}) {esc(p["opcoes"][k])}"></a>')
    linhas = [
        f'<p align="center"><img src="arcade/out/pergunta-{estado['versao']}.svg" width="100%" alt="Pergunta {n + 1}: {esc(p["pergunta"])}"></p>',
        f'<p align="center">{botoes[0]} {botoes[1]}<br>{botoes[2]} {botoes[3]}</p>',
        "",
        f'<p align="center">{q["ultimo"] or "Clique na alternativa que você acha certa 👆"}<br><sub>{q["respondidas"]} perguntas já respondidas pela comunidade</sub></p>',
    ]
    return "\n".join(linhas)


def bloco_memoria(estado):
    m = estado["memoria"]
    linhas_cartas = []
    for linha in range(2):
        cartas = []
        for col in range(8):
            i = linha * 8 + col
            s = m["cartas"][i]
            if i in m["pares"]:
                cartas.append(f'<img src="arcade/img/memoria/par-{s}.svg" width="11%" alt="{esc(SIMBOLOS[s])}">')
            elif i in m["abertas"]:
                cartas.append(f'<img src="arcade/img/memoria/carta-{s}.svg" width="11%" alt="{esc(SIMBOLOS[s])}">')
            else:
                cartas.append(f'<a href="{link_issue(f"arcade|memoria|{i}")}"><img src="arcade/img/memoria/verso.svg" width="11%" alt="carta {i + 1}"></a>')
        linhas_cartas.append("".join(cartas))
    pares = len(m["pares"]) // 2
    recorde = f" · recorde: {min(m['concluidos'])} jogadas" if m["concluidos"] else ""
    return "\n".join([
        f'<p align="center">{"<br>".join(linhas_cartas)}</p>',
        "",
        f'<p align="center"><b>Pares:</b> {pares}/8 · <b>Jogadas:</b> {m["jogadas"]}{recorde}<br>{m["ultimo"] or "Vire duas cartas iguais para formar um par 🃏"}</p>',
    ])


def bloco_xadrez(estado):
    x = estado["xadrez"]
    board = chess.Board(x["fen"])
    nome_img = f"tabuleiro-{estado['versao']}.svg"
    vez = "🩷 <b>Vez das rosas</b>" if board.turn == chess.WHITE else "💜 <b>Vez das roxas</b>"
    partes = [f'<p align="center"><img src="arcade/out/{nome_img}" width="440" alt="Tabuleiro de xadrez"></p>', ""]
    if board.is_game_over():
        partes.append(f'<p align="center">{x["ultimo"]}<br><b><a href="{link_issue("arcade|xadrez|NOVO")}">♟️ Começar uma nova partida</a></b></p>')
        return "\n".join(partes)
    partes.append(f'<p align="center">{vez} · lance {board.fullmove_number}{" · <b>Xeque!</b>" if board.is_check() else ""}<br>{x["ultimo"] or "Qualquer pessoa pode jogar: escolha um lance abaixo 👇"}</p>')
    partes.append("")
    grupos = {}
    for lance in board.legal_moves:
        de = chess.square_name(lance.from_square).upper()
        para = chess.square_name(lance.to_square).upper()
        grupos.setdefault(de, set()).add(para)
    ordem = sorted(grupos, key=lambda c: (list(NOMES_PECA).index(board.piece_at(chess.parse_square(c.lower())).piece_type), c))
    linhas = ['<table align="center">', "<tr><th>Peça</th><th>De</th><th>Para (clique)</th></tr>"]
    for de in ordem:
        peca = board.piece_at(chess.parse_square(de.lower()))
        destinos = " · ".join(f'<a href="{link_issue(f"arcade|xadrez|{de}{p}")}">{p}</a>' for p in sorted(grupos[de]))
        linhas.append(f"<tr><td>{NOMES_PECA[peca.piece_type]}</td><td><b>{de}</b></td><td>{destinos}</td></tr>")
    linhas.append("</table>")
    partes.append("\n".join(linhas))
    if x["lances"]:
        partes += ["", '<p align="center"><sub>Últimos lances: ' + " · ".join(f"{a}→{b} por @{esc(u)}" for a, b, u in reversed(x["lances"])) + "</sub></p>"]
    return "\n".join(partes)


def bloco_ranking(estado):
    return f'<p align="center"><img src="arcade/out/ranking-{estado["versao"]}.svg" width="100%" alt="Ranking do Arcade"></p>'


def substituir(texto, chave, conteudo):
    ini, fim = f"<!-- ARCADE:{chave}:INICIO -->", f"<!-- ARCADE:{chave}:FIM -->"
    padrao = re.compile(re.escape(ini) + r".*?" + re.escape(fim), re.S)
    if not padrao.search(texto):
        raise SystemExit(f"Marcador {ini} não encontrado no README.md")
    return padrao.sub(lambda _: f"{ini}\n{conteudo}\n{fim}", texto)


def atualizar(estado):
    estado["versao"] += 1
    os.makedirs(OUT, exist_ok=True)
    for nome in os.listdir(OUT):  # remove imagens antigas (evita cache do GitHub)
        os.remove(os.path.join(OUT, nome))
    x = estado["xadrez"]
    board = chess.Board(x["fen"])
    ultimo = None
    if x["lances"]:
        a, b, _ = x["lances"][-1]
        ultimo = chess.Move(chess.parse_square(a.lower()), chess.parse_square(b.lower()))
    salvar(os.path.join(OUT, f"tabuleiro-{estado['versao']}.svg"), svg_tabuleiro(board, ultimo))
    salvar(os.path.join(OUT, f"ranking-{estado['versao']}.svg"), svg_ranking(estado["ranking"]))
    perguntas = json.load(open(PERGUNTAS, encoding="utf-8"))
    n = estado["quiz"]["atual"]
    salvar(os.path.join(OUT, f"pergunta-{estado['versao']}.svg"), svg_pergunta(n + 1, len(perguntas), perguntas[n]))
    for k, op in enumerate(perguntas[n]["opcoes"]):
        salvar(os.path.join(OUT, f"opcao-{'ABCD'[k]}-{estado['versao']}.svg"), svg_opcao("ABCD"[k], op))
    with open(README, encoding="utf-8") as f:
        texto = f.read()
    texto = substituir(texto, "QUIZ", bloco_quiz(estado))
    texto = substituir(texto, "MEMORIA", bloco_memoria(estado))
    texto = substituir(texto, "XADREZ", bloco_xadrez(estado))
    texto = substituir(texto, "RANKING", bloco_ranking(estado))
    salvar(README, texto)
    salvar_estado(estado)


def comentar(mensagem):
    destino = os.path.join(os.environ.get("RUNNER_TEMP", OUT), "comentario.md")
    rodape = f"\n\n---\n🎮 Volte ao perfil para ver a jogada: https://github.com/{REPO.split('/')[0]}"
    salvar(destino, mensagem + rodape)
    print(mensagem)


def main():
    comando = sys.argv[1] if len(sys.argv) > 1 else "play"
    if comando == "init":
        gerar_imagens_fixas()
        atualizar(estado_inicial())
        print("Arcade iniciado.")
        return
    titulo = os.environ.get("ISSUE_TITLE", "").strip()
    usuario = os.environ.get("ISSUE_USER", "visitante").strip()
    partes = titulo.split("|")
    if len(partes) != 3 or partes[0].strip().lower() != "arcade":
        comentar("Não reconheci essa jogada. Use os botões do Arcade no perfil. 💜")
        return
    jogo, jogada = partes[1].strip().lower(), partes[2].strip().upper()
    estado = carregar_estado()
    if jogo == "quiz":
        msg = jogar_quiz(estado, usuario, jogada)
    elif jogo == "memoria":
        msg = jogar_memoria(estado, usuario, jogada)
    elif jogo == "xadrez":
        msg = jogar_xadrez(estado, usuario, jogada)
    else:
        msg = "Esse jogo não existe no Arcade. Os jogos são: quiz, memoria e xadrez."
    atualizar(estado)
    comentar(msg)


if __name__ == "__main__":
    main()
