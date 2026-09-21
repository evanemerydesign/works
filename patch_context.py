import os
S = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(S, "build_site.py"); t = open(p, encoding="utf-8").read()

def rep(a, b, count=1):
    global t
    assert a in t, a[:70]
    t = t.replace(a, b, count)

# ---- context images: prepare + data ----
rep('''PHOTO = {"dazzle-mass", "disassembly"}''', '''PHOTO = {"dazzle-mass", "disassembly"}
G = "G:/My Drive/Personal/Abstract_Drawing_Experiments/Art_Brand/All_Work_Promo/GrabMe"
CONTEXT = {  # work id -> (source photo, caption)
  "duality": ("17904020-b4e7-11f0-aad9-5914333ed914~2.jpg", "Duality, framed"),
  "deep-blue": ("b0e279c0-e852-11f0-afdc-ed254b3f6072.jpg", "Deep Blue, framed"),
  "distant-blues": ("7ba04180-bdd1-11f0-8bbd-fdd8513e2933.jpg", "Distant Blues, framed"),
  "dazzle-dim": ("Dazzle_Dim_25x31.jpg", "Dazzle Dim, framed"),
  "fracture-head": ("Fraxture_Head_25x31.jpg", "Fracture Head, framed"),
}
if not BARE:
    from PIL import Image
    os.makedirs(os.path.join(S, "works", "img"), exist_ok=True)
    for k, (f, _) in CONTEXT.items():
        dst = os.path.join(S, "works", "img", "ctx-" + k + ".jpg")
        if not os.path.exists(dst):
            im = Image.open(os.path.join(G, f)).convert("RGB"); im.thumbnail((1800, 1800)); im.save(dst, quality=86)''')
rep('''     "wide": wide, "photo": k in PHOTO, "description": "" if BARE else strip(d)}''',
    '''     "wide": wide, "photo": k in PHOTO, "description": "" if BARE else strip(d),
     "context": ("img/ctx-" + k + ".jpg") if k in CONTEXT else "", "context_caption": CONTEXT[k][1] if k in CONTEXT else ""}''')
rep('''  "works_label": "Nine works · 2024 — 2025 · all available",''',
    '''  "works_label": "Nine works · 2024 — 2025 · all available",
  "insitu_label": "Framed and on the wall",
  "toggle_art": "Artwork",
  "toggle_ctx": "In situ",''')

# ---- CSS: arrows off the art, toggle, in-situ grid ----
rep('''.lb .stage {{ position:relative; display:flex; align-items:center; justify-content:center; padding:40px 24px; min-height:100vh; }}''',
    '''.lb .stage {{ position:relative; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:18px; padding:40px 24px 100px; min-height:100vh; }}
.lb .view {{ display:flex; gap:8px; }}
.lb .view button {{ background:var(--paper); border:2px solid var(--ink); box-shadow:3px 3px 0 #cfccc3; padding:8px 14px; cursor:pointer; font-family:'Space Mono', monospace; font-size:10px; letter-spacing:.14em; text-transform:uppercase; }}
.lb .view button[aria-pressed="true"] {{ background:var(--ink); color:var(--paper); }}
.lb .view button:focus-visible {{ outline:2px solid var(--blue); outline-offset:3px; }}''')
rep('''.lb .frame img {{ display:block; max-height:calc(100vh - 110px); max-width:100%; width:auto; height:auto; }}''',
    '''.lb .frame img {{ display:block; max-height:calc(100vh - 190px); max-width:100%; width:auto; height:auto; }}''')
rep('''.lb .arrow {{ position:fixed; top:50%; transform:translateY(-50%); z-index:2; }}
.lb .arrow.prev {{ left:356px; }} .lb .arrow.next {{ right:16px; }}''',
    '''.lb .arrow {{ position:fixed; bottom:calc(24px + env(safe-area-inset-bottom,0px)); z-index:2; }}
.lb .arrow.prev {{ right:74px; }} .lb .arrow.next {{ right:24px; }}''')
rep('''  .lb .arrow.prev {{ left:16px; }} .lb .arrow {{ top:auto; bottom:calc(16px + env(safe-area-inset-bottom,0px)); transform:none; }}''',
    '''  .lb .stage {{ padding-bottom:24px; }}
  .lb .arrow.prev {{ right:66px; }} .lb .arrow.next {{ right:16px; }}''')
rep('''/* process */''', '''/* in situ */
.ctx {{ display:grid; grid-template-columns:repeat(3, 1fr); gap:22px; }}
@media (max-width:900px) {{ .ctx {{ grid-template-columns:repeat(2, 1fr); gap:14px; }} }}
.ctx button {{ background:none; border:0; padding:0; text-align:left; cursor:pointer; display:flex; flex-direction:column; gap:10px; }}
.ctx .ph {{ aspect-ratio:4/3; overflow:hidden; border:2px solid var(--ink); box-shadow:3px 3px 0 var(--rule); transition:transform .18s ease, box-shadow .18s ease; }}
.ctx button:hover .ph, .ctx button:focus-visible .ph {{ transform:translate(-2px,-2px); box-shadow:6px 6px 0 var(--rule); }}
.ctx button:focus-visible {{ outline:2px solid var(--blue); outline-offset:4px; }}
.ctx img {{ width:100%; height:100%; object-fit:cover; display:block; }}
.ctx .cap {{ font-family:'Space Mono', monospace; font-size:10px; letter-spacing:.12em; text-transform:uppercase; }}
/* process */''')

# ---- HTML: in-situ section + toggle in lightbox ----
rep('''<section class="s" id="process" style="background:var(--blue2); color:#f4f0ea">''',
    '''<section class="s" id="insitu"><div class="wrap">
  <div class="hd"><h2 class="cp">In situ</h2><span class="lab" data-t="insitu_label"></span></div>
  <div class="ctx" id="ctx"></div>
</div></section>

<section class="s" id="process" style="background:var(--blue2); color:#f4f0ea">''')
rep('''<li><a href="#works">Works</a></li><li><a href="#process">Process</a></li>''',
    '''<li><a href="#works">Works</a></li><li id="navInsitu"><a href="#insitu">In situ</a></li><li><a href="#process">Process</a></li>''')
rep('''  <div class="stage"><div class="frame" id="lbFrame"><img id="lbImg" src="" alt=""></div></div>''',
    '''  <div class="stage"><div class="frame" id="lbFrame"><img id="lbImg" src="" alt=""></div>
    <div class="view" id="lbView" hidden><button type="button" id="vArt" aria-pressed="true"></button><button type="button" id="vCtx" aria-pressed="false"></button></div></div>''')

# ---- JS ----
rep('''const lb = $('lb'); let cur = 0, lastFocus = null;
function show(i) {{''',
    '''const ctxWorks = C.works.map((w, i) => [w, i]).filter(([w]) => w.context);
$('ctx').innerHTML = ctxWorks.map(([w, i]) => `<button type="button" data-i="${{i}}" aria-label="Open ${{esc(w.title)}} in situ"><div class="ph"><img src="${{rel}}${{w.context}}" alt="${{esc(w.context_caption)}}" loading="lazy"></div><div class="cap">${{esc(w.context_caption)}}</div></button>`).join('');
if (!ctxWorks.length) {{ $('insitu').hidden = true; $('navInsitu').hidden = true; }}
$('vArt').textContent = C.toggle_art; $('vCtx').textContent = C.toggle_ctx;
const lb = $('lb'); let cur = 0, lastFocus = null, mode = 'art';
function setMode(m) {{
  const w = C.works[cur]; mode = (m === 'ctx' && w.context) ? 'ctx' : 'art';
  const im = $('lbImg'); im.src = mode === 'ctx' ? rel + w.context : IMG + w.id + '.jpg'; im.alt = mode === 'ctx' ? w.context_caption : w.title;
  $('lbFrame').classList.toggle('raw', mode === 'ctx' || !!w.photo);
  $('vArt').setAttribute('aria-pressed', mode === 'art'); $('vCtx').setAttribute('aria-pressed', mode === 'ctx');
  $('lbView').hidden = !w.context;
}}
function show(i, m) {{''')
rep('''  const im = $('lbImg'); im.src = IMG + w.id + '.jpg'; im.alt = w.title; $('lbFrame').classList.toggle('raw', !!w.photo); lb.scrollTop = 0;
}}
function open(i) {{ lastFocus = document.activeElement; show(i); lb.hidden = false;''',
    '''  setMode(m || 'art'); lb.scrollTop = 0;
}}
function open(i, m) {{ lastFocus = document.activeElement; show(i, m); lb.hidden = false;''')
rep('''document.querySelectorAll('.card').forEach(c => c.addEventListener('click', () => open(+c.dataset.i)));''',
    '''document.querySelectorAll('.card').forEach(c => c.addEventListener('click', () => open(+c.dataset.i)));
document.querySelectorAll('#ctx button').forEach(c => c.addEventListener('click', () => open(+c.dataset.i, 'ctx')));
$('vArt').addEventListener('click', () => setMode('art')); $('vCtx').addEventListener('click', () => setMode('ctx'));''')
rep('''const C = window.CONTENT, IMG = '{rel}img/';''', '''const C = window.CONTENT, IMG = '{rel}img/', rel = '{rel}';''')
open(p, "w", encoding="utf-8").write(t); print("patched")
