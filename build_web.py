import os, re, html, json, shutil
S = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(S, "build_final.py"), encoding="utf-8").read().split("CSS = ")[0])  # reuse parsing + works list


# ---- short copy + image overrides ----
from PIL import Image as _I
G="G:/My Drive/Personal/Abstract_Drawing_Experiments/Art_Brand/All_Work_Promo/GrabMe"
for k,src in {"dazzle-mass":G+"/Artwork_Framed-1.jpg","disassembly":G+"/Artwork_Framed-4.jpg"}.items():
    im=_I.open(src).convert("RGB"); im.thumbnail((1800,1800)); im.save(os.path.join(S,"img",k+".jpg"),quality=86)
works=[w for w in works if w[0]!="survey-figure"]

BARE = bool(os.environ.get("BARE"))
if BARE:
    COPY = dict(COPY, lede="I apply the machine as a means to express form.", brief=[], about_lede="", about=[], process_lede="", process=[])
    descs = ["" for _ in works]
W = os.path.join(S, "web_bare" if BARE else "web"); os.makedirs(os.path.join(W, "img"), exist_ok=True)
for w in works:
    shutil.copy(os.path.join(S, "img", w[0] + ".jpg"), os.path.join(W, "img", w[0] + ".jpg"))

PHOTO={"dazzle-mass","disassembly"}
data = [dict(id=k, title=t, year=y, medium=m, size=sz, price=pr, tools=tools, out=an, wide=wide, photo=(k in PHOTO), desc=d)
        for (k, t, y, m, sz, pr, tools, an, wide), d in zip(works, descs)]

cards = "\n".join(f'''<button class="card{' photo' if w['photo'] else ''}{' wide' if w['wide'] else ''}" data-i="{i}" aria-label="Open {html.escape(w['title'])}">
  <div class="box"><img src="img/{w['id']}.jpg" alt="{html.escape(w['title'])}" loading="{'eager' if i<5 else 'lazy'}"></div>
  <div class="cap"><span class="t">{html.escape(w['title'])}</span><span class="n">{i+1:02d}</span><span class="p">{w['price']}</span></div>
</button>''' for i, w in enumerate(data))

trows = "".join(f"<tr><td>{i+1}</td><td>{html.escape(w['title'])}</td><td>{w['year']}</td><td>{html.escape(w['medium'])}</td><td>{w['size']}</td><td>{w['price']}</td></tr>" for i, w in enumerate(data))
sp = re.findall(r"<p>.*?</p>", statement)

ABOUT = f'''<section class="s" id="about" style="background:var(--bg2)"><div class="wrap">
  <div class="hd"><h2 class="cp">About</h2><span class="lab">Evan Emery · Phoenix, Arizona</span></div>
  <div class="about"><p class="lede">{COPY["about_lede"]}</p><div class="body">{P(COPY["about"])}</div></div>
</div></section>'''

page = f'''<title>Evan Emery Selected Works</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@700&family=Space+Grotesk:wght@400;500&family=Space+Mono:wght@400;700&display=swap">
<style>
:root {{ --bg:#f4f0ea; --bg2:#efebe1; --card:#f9f7f2; --ink:#161616; --mute:#6f6e6b; --rule:#d8d5cf; --blue:#12305e; --blue2:#0b1a36; --paper:#faf9f4; }}
* {{ box-sizing:border-box; }}
html {{ scroll-behavior:smooth; }}
body {{ margin:0; background:var(--bg); color:var(--ink); font-family:'Space Grotesk', system-ui, sans-serif; font-size:16px; line-height:1.5; }}
@media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior:auto; }} * {{ transition:none !important; animation:none !important; }} }}
.cp {{ font-family:'Chakra Petch', 'Arial Narrow', sans-serif; font-weight:700; }}
.mono {{ font-family:'Space Mono', ui-monospace, monospace; }}
.lab {{ font-family:'Space Mono', ui-monospace, monospace; font-size:10px; letter-spacing:.22em; text-transform:uppercase; color:var(--mute); }}
a {{ color:inherit; }}
button {{ font:inherit; color:inherit; }}
/* nav */
.nav {{ position:sticky; top:env(safe-area-inset-top,0px); z-index:20; background:rgba(244,240,234,.92); backdrop-filter:blur(8px); border-bottom:1px solid var(--rule); }}
.nav .in {{ max-width:1400px; margin:0 auto; padding:12px 24px; display:flex; justify-content:space-between; align-items:center; gap:16px; }}
.nav .brand {{ font-size:15px; letter-spacing:-.01em; }}
.nav ul {{ list-style:none; margin:0; padding:0; display:flex; gap:22px; }}
.nav a {{ text-decoration:none; font-family:'Space Mono', monospace; font-size:10px; letter-spacing:.18em; text-transform:uppercase; color:var(--mute); }}
.nav a:hover {{ color:var(--ink); }}
/* hero */
.hero {{ position:relative; background:var(--blue2); color:#f4f0ea; min-height:520px; height:72vh; max-height:820px; overflow:hidden; }}
.hero img {{ position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:center 30%; }}
.hero .shade {{ position:absolute; inset:0; background:linear-gradient(to top, rgba(8,14,30,.97) 0%, rgba(8,14,30,.85) 30%, rgba(8,14,30,.3) 60%, rgba(8,14,30,0) 80%); }}
.hero .in {{ position:absolute; left:0; right:0; bottom:0; max-width:1400px; margin:0 auto; padding:0 24px 40px; text-shadow:0 2px 12px rgba(0,0,0,.9), 0 0 2px rgba(0,0,0,.8); display:flex; justify-content:space-between; align-items:flex-end; gap:24px; flex-wrap:wrap; }}
.hero h1 {{ margin:0; font-size:clamp(38px, 6.5vw, 76px); line-height:.94; letter-spacing:-.01em; text-wrap:balance; }}
.hero .sub {{ margin-top:16px; font-family:'Space Mono', monospace; font-size:11px; letter-spacing:.26em; text-transform:uppercase; opacity:1; }}
.hero .tag {{ position:absolute; top:22px; left:24px; font-family:'Space Mono', monospace; font-size:10px; letter-spacing:.26em; text-transform:uppercase; opacity:.85; }}
.hero .r {{ font-family:'Space Mono', monospace; font-size:11px; line-height:1.9; letter-spacing:.06em; opacity:1; text-align:right; }}
.hero .r a {{ text-decoration:none; }}
/* brief */
.brief {{ padding-block:64px 56px; }}
.brief .in {{ max-width:1400px; margin:0 auto; padding:0 24px; display:grid; grid-template-columns:minmax(0, 1fr) minmax(0, 1.6fr); gap:48px; align-items:start; }}
@media (max-width:900px) {{ .brief .in {{ grid-template-columns:1fr; gap:20px; }} }}
.brief .lede {{ margin:0; font-family:'Chakra Petch', 'Arial Narrow', sans-serif; font-weight:700; font-size:clamp(26px, 3.2vw, 40px); line-height:1.05; text-transform:uppercase; text-wrap:balance; }}
.brief .body p {{ margin:0 0 14px; font-size:17px; line-height:1.55; max-width:62ch; }}
.brief .lab {{ margin-top:6px; }}
/* sections */
.wrap {{ max-width:1400px; margin:0 auto; padding:0 24px; }}
section.s {{ padding-block:56px; }}
.hd {{ display:flex; justify-content:space-between; align-items:flex-end; gap:16px; border-bottom:2px solid var(--ink); padding-bottom:12px; margin-bottom:28px; flex-wrap:wrap; }}
.hd h2 {{ margin:0; font-size:24px; line-height:1; text-transform:uppercase; }}
/* gallery */
.grid {{ display:grid; grid-template-columns:repeat(5, 1fr); gap:26px 22px; }}
@media (max-width:1100px) {{ .grid {{ grid-template-columns:repeat(3, 1fr); }} }}
@media (max-width:640px) {{ .grid {{ grid-template-columns:repeat(2, 1fr); gap:20px 14px; }} }}
.card {{ background:none; border:0; padding:0; text-align:left; cursor:pointer; display:flex; flex-direction:column; gap:10px; }}
.card .box {{ aspect-ratio:4/5; background:var(--card); border:2px solid var(--ink); box-shadow:3px 3px 0 var(--rule); display:flex; align-items:center; justify-content:center; padding:7%; transition:transform .18s ease, box-shadow .18s ease; }}
.card:hover .box, .card:focus-visible .box {{ transform:translate(-2px,-2px); box-shadow:6px 6px 0 var(--rule); }}
.card:focus-visible {{ outline:2px solid var(--blue); outline-offset:4px; }}
.card img {{ max-width:100%; max-height:100%; width:auto; height:auto; display:block; box-shadow:0 1px 3px rgba(0,0,0,.2); }}
.card .cap {{ display:flex; gap:8px; align-items:baseline; font-family:'Space Mono', monospace; font-size:10px; letter-spacing:.12em; text-transform:uppercase; }}
.card .cap .n {{ color:var(--mute); }} .card .cap .p {{ margin-left:auto; font-weight:700; }}
.card.photo .box, .card.wide .box {{ padding:0; overflow:hidden; }}
.card.photo img, .card.wide img {{ width:100%; height:100%; object-fit:cover; box-shadow:none; }}
.lb .frame.raw {{ background:none; border:0; padding:0; box-shadow:6px 6px 0 #cfccc3; }}
.hint {{ margin-top:18px; }}
.lb .desc:empty {{ display:none; }}
.brief.bare .in {{ grid-template-columns:1fr; }}
.brief.bare .lede {{ font-size:clamp(30px, 4.2vw, 56px); max-width:22ch; }}
/* lightbox */
.lb {{ position:fixed; inset:0; z-index:50; background:var(--bg2); display:grid; grid-template-columns:340px 1fr; overflow:auto; }}
.lb .bg {{ position:absolute; inset:0; pointer-events:none;
  background-image:linear-gradient(to right, rgba(0,0,0,.055) 1px, transparent 1px), linear-gradient(to bottom, rgba(0,0,0,.055) 1px, transparent 1px), linear-gradient(to right, rgba(0,0,0,.028) 1px, transparent 1px), linear-gradient(to bottom, rgba(0,0,0,.028) 1px, transparent 1px);
  background-size:48px 48px, 48px 48px, 12px 12px, 12px 12px; }}
.lb .panel {{ position:relative; background:#f5f2ec; padding:calc(40px + env(safe-area-inset-top,0px)) 30px 40px; min-height:100%; }}
.lb .num {{ font-family:'Space Mono', monospace; font-size:10px; letter-spacing:.12em; color:#5d5d5d; }}
.lb h3 {{ margin:28px 0 0; font-size:30px; line-height:1; text-transform:uppercase; padding-bottom:12px; border-bottom:1px solid #7d7c79; }}
.lb dl {{ margin:18px 0 0; display:grid; grid-template-columns:96px 1fr; row-gap:8px; font-family:'Space Mono', monospace; font-size:10.5px; line-height:1.5; }}
.lb dt {{ color:#7b7b79; letter-spacing:.12em; text-transform:uppercase; }} .lb dd {{ margin:0; }} .lb dd.price {{ font-weight:700; }}
.lb .desc {{ margin-top:22px; padding-top:18px; border-top:1px solid var(--rule); font-size:14.5px; line-height:1.55; color:#2a2a2a; }}
.lb .desc p {{ margin:0 0 8px; }}
.lb .stage {{ position:relative; display:flex; align-items:center; justify-content:center; padding:40px 24px; min-height:100vh; }}
.lb .frame {{ background:var(--paper); border:2px solid var(--ink); padding:14px; box-shadow:6px 6px 0 #cfccc3; max-width:100%; }}
.lb .frame img {{ display:block; max-height:calc(100vh - 110px); max-width:100%; width:auto; height:auto; }}
.lb .ctl {{ position:fixed; top:calc(14px + env(safe-area-inset-top,0px)); right:16px; display:flex; gap:8px; z-index:2; }}
.lb .ctl button, .lb .arrow {{ background:var(--paper); border:2px solid var(--ink); box-shadow:3px 3px 0 #cfccc3; width:42px; height:42px; cursor:pointer; font-family:'Space Mono', monospace; font-size:16px; display:flex; align-items:center; justify-content:center; }}
.lb .ctl button:hover, .lb .arrow:hover {{ transform:translate(-1px,-1px); box-shadow:4px 4px 0 #cfccc3; }}
.lb .ctl button:focus-visible, .lb .arrow:focus-visible {{ outline:2px solid var(--blue); outline-offset:3px; }}
.lb .arrow {{ position:fixed; top:50%; transform:translateY(-50%); z-index:2; }}
.lb .arrow.prev {{ left:356px; }} .lb .arrow.next {{ right:16px; }}
@media (max-width:900px) {{
  .lb {{ grid-template-columns:1fr; }}
  .lb .panel {{ order:2; min-height:0; padding-top:28px; }}
  .lb .stage {{ order:1; min-height:0; padding:calc(70px + env(safe-area-inset-top,0px)) 16px 24px; }}
  .lb .frame img {{ max-height:70vh; }}
  .lb .arrow.prev {{ left:16px; }} .lb .arrow {{ top:auto; bottom:calc(16px + env(safe-area-inset-bottom,0px)); transform:none; }}
}}
/* process */
.proc {{ display:grid; grid-template-columns:minmax(260px, 420px) 1fr; gap:48px; align-items:center; }}
@media (max-width:800px) {{ .proc {{ grid-template-columns:1fr; gap:28px; }} }}
.vid {{ background:#0b1a36; border:2px solid #f4f0ea; box-shadow:6px 6px 0 rgba(244,240,234,.25); aspect-ratio:3/4; max-width:100%; }}
.vid video {{ display:block; width:100%; height:100%; object-fit:cover; background:#000; }}
.ptxt {{ max-width:60ch; }}
.ptxt h3 {{ margin:0 0 14px; font-size:20px; text-transform:uppercase; letter-spacing:.02em; }}
.ptxt p {{ margin:0 0 12px; font-size:16px; line-height:1.55; color:#e6e3dc; }}
/* statement */
.cols {{ display:grid; grid-template-columns:repeat(3, 1fr); gap:40px; }}
@media (max-width:900px) {{ .cols {{ grid-template-columns:1fr; gap:8px; }} }}
.cols p {{ margin:0 0 12px; max-width:62ch; }}
.cols h3 {{ margin:22px 0 10px; font-size:13px; letter-spacing:.06em; text-transform:uppercase; }}
.about {{ display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1.6fr); gap:48px; align-items:start; }}
@media (max-width:900px) {{ .about {{ grid-template-columns:1fr; gap:20px; }} }}
.about .lede {{ margin:0; font-family:'Chakra Petch', 'Arial Narrow', sans-serif; font-weight:700; font-size:clamp(26px, 3.2vw, 40px); line-height:1.05; text-transform:uppercase; text-wrap:balance; }}
.about .body p {{ margin:0 0 14px; font-size:17px; line-height:1.55; max-width:62ch; }}
.ptxt h3 {{ font-size:clamp(24px, 2.6vw, 34px) !important; line-height:1.05 !important; }}
/* list */
.two {{ display:grid; grid-template-columns:1.4fr 1fr; gap:48px; align-items:start; }}
@media (max-width:900px) {{ .two {{ grid-template-columns:1fr; }} }}
.tw {{ overflow-x:auto; }}
table {{ width:100%; border-collapse:collapse; font-size:14px; min-width:560px; }}
th, td {{ text-align:left; padding:9px 8px; border-bottom:1px solid var(--rule); vertical-align:top; }}
th {{ font-family:'Space Mono', monospace; font-size:10px; letter-spacing:.12em; text-transform:uppercase; color:var(--mute); border-bottom:1px solid var(--ink); font-weight:400; }}
td:last-child, th:last-child, td:first-child {{ font-variant-numeric:tabular-nums; }}
td:last-child, th:last-child {{ text-align:right; white-space:nowrap; font-weight:500; }}
.total {{ margin-top:14px; font-family:'Space Mono', monospace; font-size:11px; }}
.contact div {{ display:flex; gap:12px; align-items:baseline; padding:6px 0; border-bottom:1px solid var(--rule); }}
.contact .k {{ flex:0 0 96px; }}
.contact a {{ text-decoration:none; }} .contact a:hover {{ text-decoration:underline; }}
.contact h3 {{ margin:0 0 6px; font-size:13px; letter-spacing:.06em; text-transform:uppercase; }}
footer {{ border-top:1px solid var(--rule); }}
footer .in {{ max-width:1400px; margin:0 auto; padding:22px 24px; display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; }}
</style>

<nav class="nav"><div class="in"><span class="brand cp">EVAN EMERY</span>
<ul><li><a href="#works">Works</a></li><li><a href="#process">Process</a></li>{'' if BARE else '<li><a href="#about">About</a></li>'}<li><a href="#list">Available works</a></li><li><a href="#list">Contact</a></li></ul></div></nav>

<header class="hero">
  <img src="img/deep-blue.jpg" alt="Deep Blue, cyanotype print, 2025"><div class="shade"></div>
  <div class="in">
    <div><h1 class="cp">EVAN EMERY<br>SELECTED WORKS</h1><div class="sub">Human &nbsp;×&nbsp; Machine &nbsp;·&nbsp; Nine works &nbsp;·&nbsp; 2024 — 2025</div></div>
    <div class="r">Phoenix, Arizona<br><a href="https://www.instagram.com/evanemerydesign/">@evanemerydesign</a></div>
  </div>
</header>

<section class="brief{" bare" if BARE else ""}" id="statement"><div class="in">
  <div><p class="lede">{COPY["lede"]}</p><div class="lab">Artist statement</div></div>
  {'' if BARE else '<div class="body">' + P(COPY["brief"]) + '</div>'}
</div></section>

<section class="s" id="works"><div class="wrap">
  <div class="hd"><h2 class="cp">Works submitted</h2><span class="lab">Nine works · 2024 — 2025 · all available</span></div>
  <div class="grid">
{cards}
  </div>
  <div class="hint lab">Select any work to view it large with its details</div>
</div></section>

<section class="s" id="process" style="background:var(--blue2); color:#f4f0ea"><div class="wrap">
  <div class="hd" style="border-color:#f4f0ea"><h2 class="cp">Process</h2><span class="lab" style="color:#b9bec9">From code to paper</span></div>
  <div class="proc">
    <div class="vid"><video id="btsVideo" src="bts.mp4" poster="img/bts-poster.jpg" controls playsinline preload="metadata"></video></div>
    <div class="ptxt">
      {'' if BARE else '<h3 class="cp">' + COPY["process_lede"] + '</h3>' + P(COPY["process"])}
      <p class="lab" style="color:#b9bec9; margin-top:18px">Press play · 90 seconds · sound on</p>
    </div>
  </div>
</div></section>

{"" if BARE else ABOUT}

<section class="s" id="list"><div class="wrap">
  <div class="hd"><h2 class="cp">Available works</h2><span class="lab">Retail prices · framed originals and prints</span></div>
  <div class="two">
    <div><div class="tw"><table><thead><tr><th>#</th><th>Title</th><th>Year</th><th>Medium</th><th>Dimensions</th><th>Retail</th></tr></thead><tbody>{trows}</tbody></table></div>
      </div>
    <div class="contact"><h3 class="cp">Contact</h3>
      <div><span class="k lab">Name</span><span>Evan Emery</span></div>
      <div><span class="k lab">Location</span><span>Phoenix, Arizona</span></div>
      <div><span class="k lab">Email</span><a href="mailto:evanemerydesign@gmail.com">evanemerydesign@gmail.com</a></div>
      <div><span class="k lab">Instagram</span><a href="https://www.instagram.com/evanemerydesign/">@evanemerydesign</a></div>
      <div><span class="k lab">LinkedIn</span><a href="https://www.linkedin.com/in/evan-emery-2021/">evan-emery-2021</a></div>
    </div>
  </div>
</div></section>

<footer><div class="in"><span class="lab">Evan Emery · Phoenix, Arizona</span><span class="lab">Selected works · 2024 — 2025</span></div></footer>

<div class="lb" id="lb" hidden role="dialog" aria-modal="true" aria-label="Work detail">
  <div class="bg"></div>
  <div class="panel"><div class="num" id="lbNum"></div><h3 class="cp" id="lbTitle"></h3>
    <dl><dt>Year</dt><dd id="lbYear"></dd><dt>Medium</dt><dd id="lbMedium"></dd><dt>Size</dt><dd id="lbSize"></dd><dt>Tools</dt><dd id="lbTools"></dd><dt>Output</dt><dd id="lbOut"></dd><dt>Retail</dt><dd class="price" id="lbPrice"></dd></dl>
    <div class="desc" id="lbDesc"></div></div>
  <div class="stage"><div class="frame"><img id="lbImg" src="" alt=""></div></div>
  <div class="ctl"><button type="button" id="lbClose" aria-label="Close">✕</button></div>
  <button type="button" class="arrow prev" id="lbPrev" aria-label="Previous work">←</button>
  <button type="button" class="arrow next" id="lbNext" aria-label="Next work">→</button>
</div>

<script>
const WORKS = {json.dumps(data)};
const lb = document.getElementById('lb'); let cur = 0, lastFocus = null;
const $ = id => document.getElementById(id);
function show(i) {{
  cur = (i + WORKS.length) % WORKS.length; const w = WORKS[cur];
  $('lbNum').textContent = String(cur+1).padStart(2,'0') + ' / ' + String(WORKS.length).padStart(2,'0');
  $('lbTitle').textContent = w.title; $('lbYear').textContent = w.year; $('lbMedium').textContent = w.medium;
  $('lbSize').textContent = w.size; $('lbTools').textContent = w.tools; $('lbOut').textContent = w.out; $('lbPrice').textContent = w.price;
  $('lbDesc').innerHTML = w.desc; const im = $('lbImg'); im.src = 'img/' + w.id + '.jpg'; im.alt = w.title; im.parentElement.classList.toggle('raw', !!w.photo);
  lb.scrollTop = 0;
}}
function open(i) {{ lastFocus = document.activeElement; show(i); lb.hidden = false; document.body.style.overflow = 'hidden'; $('lbClose').focus(); }}
function close() {{ lb.hidden = true; document.body.style.overflow = ''; if (lastFocus) lastFocus.focus(); }}
document.querySelectorAll('.card').forEach(c => c.addEventListener('click', () => open(+c.dataset.i)));
$('lbClose').addEventListener('click', close);
$('lbPrev').addEventListener('click', () => show(cur-1));
$('lbNext').addEventListener('click', () => show(cur+1));
document.addEventListener('keydown', e => {{ if (lb.hidden) return; if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(cur-1); if (e.key === 'ArrowRight') show(cur+1); }});
let tx = null; lb.addEventListener('touchstart', e => tx = e.touches[0].clientX, {{passive:true}});
lb.addEventListener('touchend', e => {{ if (tx === null) return; const dx = e.changedTouches[0].clientX - tx; if (Math.abs(dx) > 60) show(cur + (dx < 0 ? 1 : -1)); tx = null; }});
</script>
'''
open(os.path.join(W, "index.html"), "w", encoding="utf-8").write(page)
print("ok", sum(os.path.getsize(os.path.join(W, "img", f)) for f in os.listdir(os.path.join(W, "img")))//1024, "KB images")
