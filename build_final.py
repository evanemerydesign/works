import os, re, subprocess, html
S = os.path.dirname(os.path.abspath(__file__))
md = open(r"C:\Users\evane\Downloads\b-art-submission-2026-10.md", encoding="utf-8").read()

def sec(t):
    return re.search(r"^## " + t + r".*?$\n(.*?)(?=^---$|\Z)", md, re.M | re.S).group(1).strip()
def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)
    return t
def paras(t):
    return "".join(f"<p>{inline(' '.join(p.split()))}</p>" for p in re.split(r"\n\s*\n", t) if p.strip())

bio = paras(sec("2\\.")); statement = paras(sec("3\\."))
tbl = sec("4\\.")
rows = [[c.strip() for c in r.strip("|").split("|")] for r in tbl.splitlines() if r.startswith("|") and not r.startswith("|---")]
total = inline([l for l in tbl.splitlines() if l.startswith("**Total")][0])
blocks = re.split(r"^### ", sec("5\\."), flags=re.M)[1:]
descs = [paras("\n".join(b.strip().splitlines()[3:])) for b in blocks]
info = {m.group(1): m.group(2) for m in re.finditer(r"^\*\*(.+?):\*\* (.+)$", sec("1\\."), re.M)}

works = [
 ("duality","Duality","2025","White ink on mat board","30 × 40 in","$1,800","Rhino · Grasshopper","CNC pen plotter",True),
 ("survey-figure","Survey Figure","2025","White ink on black archival paper","18 × 40 in","$1,000","Rhino · Grasshopper","AxiDraw",False),
 ("deep-blue","Deep Blue","2025","Cyanotype print on watercolor paper","25 × 31 in","$1,000","Octane Render · Vectron · C4D","Cyanotype",False),
 ("distant-blues","Distant Blues","2025","Cyanotype print on watercolor paper","25 × 31 in","$1,000","Octane Render · Vectron · C4D","Cyanotype",False),
 ("fractal-blues","Fractal Blues","2025","Cyanotype print on watercolor paper","25 × 31 in","$1,000","Octane Render · Vectron · C4D","Cyanotype",False),
 ("falling","Falling","2025","Cyanotype print on watercolor paper","25 × 31 in","$1,000","Octane Render · Vectron · C4D","Cyanotype",False),
 ("disassembly","Disassembly","2025","Ink on graph paper","18 × 22 in","$1,000","Rhino · Grasshopper · DrawingBot v3","CNC pen plotter",False),
 ("dazzle-mass","Dazzle Mass","2025","Archival pigment on fine art paper","18 × 22 in","$1,000","Rhino · Grasshopper · Blender","Archival inkjet",False),
 ("dazzle-dim","Dazzle Dim","2024","Archival pigment on fine art paper","25 × 31 in","$1,000","Rhino · Grasshopper","CNC pen plotter",False),
 ("fracture-head","Fracture Head","2024","Mixed media on fine art paper","25 × 31 in","$1,000","Rhino · Grasshopper · Blender · DrawingBot v3","Spray paint · CNC pen plotter",False),
]

works=[w for w in works if w[0]!="survey-figure"]
rows=[r for r in rows if r[1]!="Survey Figure"]
descs=[d for d,b in zip(descs,blocks) if "Survey Figure" not in b.splitlines()[0]]
total="Total retail: $9,800"

ORDER=["duality","deep-blue","distant-blues","fractal-blues","falling","dazzle-dim","fracture-head","disassembly","dazzle-mass"]
_dmap={b.splitlines()[0].split(". ",1)[-1].strip(): paras(chr(10).join(b.strip().splitlines()[3:])) for b in blocks}
works=sorted(works,key=lambda w: ORDER.index(w[0]))
descs=[_dmap[w[1]] for w in works]
_rmap={r[1]:r for r in rows[1:]}
rows=[rows[0]]+[[str(i)]+_rmap[w[1]][1:] for i,w in enumerate(works,1)]

COPY = dict(
 lede="My work applies the instruments of architecture to the human body.",
 brief=["Height fields, isometric projection, voxel decomposition, point clouds, the surveyor\u2019s annotation: the conventions by which we describe buildings and terrain, turned toward a face. What returns is a body read as site.",
        "I no longer draw the pattern; I write the system that finds it. Fractal geometry, vector fields, recursive displacement: mathematics behaving according to its own nature, with the human body as the surface it acts upon."],
 about_lede="The digital carries no weight until it is pressed into cotton rag.",
 about=["Every result lands in something physical and slow. Cyanotype, the chemistry of the blueprint, receives geometry that was never photographed. A pen plotter lays white ink onto mat board one stroke at a time.",
        "Evan Emery is a Phoenix-based artist, fabricator and educator. He directs The Guild, the fabrication division of 180 Degrees Design Build, and a six-axis robotics lab at The Design School at Arizona State University. His work is generated in code and resolved in cyanotype, pigment and plotted ink."],
 process_lede="Written in code. Drawn by machine.",
 process=["Geometry is generated in Rhino and Grasshopper, then handed to a plotter that lays white ink one stroke at a time. This clip follows Duality from the digital model to the plotter bed: two heads, 1,904 nodes."],
)
P = lambda xs: "".join("<p>"+x+"</p>" for x in xs)
_dims={w[1]:w[4] for w in works}
rows=[rows[0]]+[[r[0],r[1],r[2],r[3],_dims.get(r[1],r[4]),r[5]] for r in rows[1:]]

CSS = """
@page { size: 1440px 810px; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { background: #f4f0ea; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'Space Mono', monospace; color: #161616; }
.page { width: 1440px; height: 810px; position: relative; overflow: hidden; page-break-after: always; break-after: page; }
.page:last-child { page-break-after: auto; break-after: auto; }
.cp { font-family: 'Chakra Petch', sans-serif; font-weight: 700; }
.sg { font-family: 'Space Grotesk', sans-serif; }
/* hero */
.hero { background: #0f1f3d; }
.hero img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: center 30%; }
.hero .shade { position: absolute; inset: 0; background: linear-gradient(to top, rgba(8,14,30,.97) 0%, rgba(8,14,30,.85) 32%, rgba(8,14,30,.3) 60%, rgba(8,14,30,0) 80%), linear-gradient(to bottom, rgba(8,14,30,.8) 0%, rgba(8,14,30,0) 16%); }
.hero .t { position: absolute; left: 56px; bottom: 52px; color: #f4f0ea; text-shadow: 0 2px 14px rgba(0,0,0,.9), 0 0 2px rgba(0,0,0,.8); }
.hero .t h1 { font-size: 64px; line-height: .95; letter-spacing: -.01em; }
.hero .t .sub { font-size: 12px; letter-spacing: .28em; text-transform: uppercase; margin-top: 18px; opacity: 1; }
.hero .r { position: absolute; right: 56px; bottom: 52px; color: #f4f0ea; text-align: right; font-size: 11px; line-height: 1.8; opacity: 1; letter-spacing: .06em; text-shadow: 0 2px 10px rgba(0,0,0,.9); }
.hero .tag { position: absolute; left: 56px; top: 44px; color: #f4f0ea; font-size: 11px; letter-spacing: .28em; text-transform: uppercase; opacity: .85; }
/* grid cover */
.cover { background: #f4f0ea; padding: 24px 40px; }
.cover .hd { display: flex; justify-content: space-between; align-items: flex-start; height: 44px; }
.cover .hd h1 { font-size: 21px; letter-spacing: -0.01em; line-height: 1; margin-top: 3px; }
.cover .hd .sub { font-size: 9px; letter-spacing: .22em; text-transform: uppercase; color: #6f6e6b; margin-top: 8px; }
.cover .hd .r { text-align: right; }
.cover .hd .r .sub { letter-spacing: .06em; text-transform: none; }
.grid { display: grid; grid-template-columns: repeat(5, 1fr); grid-template-rows: repeat(2, 1fr); gap: 24px 22px; margin-top: 20px; height: 660px; }
.card { display: flex; flex-direction: column; min-height: 0; }
.card .box { flex: 1; background: #f9f7f2; border: 2px solid #161616; box-shadow: 3px 3px 0 #d8d5cf; display: flex; align-items: center; justify-content: center; padding: 16px; min-height: 0; }
.card .box img { max-width: 100%; max-height: 100%; width: auto; height: auto; display: block; box-shadow: 0 1px 2px rgba(0,0,0,.18); }
.card.wide .box { padding: 0; overflow: hidden; }
.card.wide .box img { width: 100%; height: 100%; max-width: none; max-height: none; object-fit: cover; box-shadow: none; }
.card .cap { text-align: center; font-size: 9.5px; letter-spacing: .12em; text-transform: uppercase; margin-top: 12px; height: 14px; }
.card .cap span { color: #9a9894; margin-left: 6px; }
.cover .ft { position: absolute; left: 40px; bottom: 30px; font-size: 9px; letter-spacing: .22em; text-transform: uppercase; color: #6f6e6b; }
/* work pages */
.work { background: #efebe1; }
.work .bg { position: absolute; inset: 0;
  background-image: linear-gradient(to right, rgba(0,0,0,.055) 1px, transparent 1px), linear-gradient(to bottom, rgba(0,0,0,.055) 1px, transparent 1px),
                    linear-gradient(to right, rgba(0,0,0,.028) 1px, transparent 1px), linear-gradient(to bottom, rgba(0,0,0,.028) 1px, transparent 1px);
  background-size: 48px 48px, 48px 48px, 12px 12px, 12px 12px; }
.panel { position: absolute; left: 0; top: 0; width: 330px; height: 810px; background: #f5f2ec; padding: 44px 30px; }
.panel .num { font-size: 9.5px; letter-spacing: .12em; color: #5d5d5d; }
.panel h2 { font-size: 30px; line-height: 1; letter-spacing: -0.01em; text-transform: uppercase; margin-top: 36px; padding-bottom: 12px; border-bottom: 1px solid #7d7c79; }
.meta { margin-top: 18px; display: grid; grid-template-columns: 96px 1fr; row-gap: 8px; font-size: 9.5px; line-height: 1.5; }
.meta dt { color: #7b7b79; letter-spacing: .12em; text-transform: uppercase; }
.meta dd { color: #161616; }
.meta dd.price { font-weight: 700; }
.desc { margin-top: 24px; padding-top: 18px; border-top: 1px solid #d8d5cf; font-family: 'Space Grotesk', sans-serif; font-size: 12.5px; line-height: 1.5; color: #2a2a2a; }
.desc p { margin-bottom: 8px; }
.stage { position: absolute; left: 330px; top: 0; right: 0; height: 810px; display: flex; align-items: center; justify-content: center; }
.frame { background: #faf9f4; border: 2px solid #161616; padding: 14px; box-shadow: 6px 6px 0 #cfccc3; }
.frame img { display: block; height: 660px; width: auto; max-width: 900px; object-fit: contain; }
.frame.wide img { height: auto; width: 900px; }
.frame.raw { background: none; border: 0; padding: 0; }
/* text pages */
.txt { background: #f4f0ea; padding: 44px 56px; }
.txt .hd { display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 2px solid #161616; padding-bottom: 12px; }
.txt .hd h1 { font-size: 26px; line-height: 1; text-transform: uppercase; }
.txt .hd .sub { font-size: 9.5px; letter-spacing: .22em; text-transform: uppercase; color: #6f6e6b; }
.tag { font-family: 'Chakra Petch', sans-serif; font-weight: 700; font-size: 44px; line-height: 1.02; text-transform: uppercase; letter-spacing: -.01em; max-width: 1100px; margin-top: 34px; }
.tag2 { font-family: 'Chakra Petch', sans-serif; font-weight: 700; font-size: 22px; line-height: 1.1; text-transform: uppercase; margin-bottom: 14px; }
.cols2 { display: grid; grid-template-columns: 1fr 1fr; gap: 56px; margin-top: 30px; font-family: 'Space Grotesk', sans-serif; font-size: 15px; line-height: 1.55; }
.cols2 p { margin-bottom: 10px; }
.cols { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 40px; margin-top: 28px; font-family: 'Space Grotesk', sans-serif; font-size: 13.2px; line-height: 1.5; }
.cols h3 { font-family: 'Chakra Petch', sans-serif; font-weight: 700; font-size: 13px; letter-spacing: .06em; text-transform: uppercase; margin-bottom: 10px; }
.cols p { margin-bottom: 9px; }
.two { display: grid; grid-template-columns: 1.35fr 1fr; gap: 48px; margin-top: 28px; }
table { width: 100%; border-collapse: collapse; font-size: 11.5px; font-family: 'Space Grotesk', sans-serif; }
th, td { text-align: left; padding: 8px 8px; border-bottom: 1px solid #d8d5cf; vertical-align: top; }
th { font-family: 'Space Mono', monospace; font-size: 9px; letter-spacing: .12em; text-transform: uppercase; color: #6f6e6b; border-bottom: 1px solid #161616; }
td:last-child, th:last-child { text-align: right; white-space: nowrap; }
.total { font-size: 10.5px; margin-top: 14px; }
.contact { font-family: 'Space Grotesk', sans-serif; font-size: 13.5px; line-height: 1.7; }
.contact h3 { font-family: 'Chakra Petch', sans-serif; font-weight: 700; font-size: 13px; letter-spacing: .06em; text-transform: uppercase; margin-bottom: 10px; }
.contact .k { display: inline-block; width: 100px; color: #6f6e6b; font-family: 'Space Mono', monospace; font-size: 9.5px; letter-spacing: .12em; text-transform: uppercase; }
.mini { display: grid; grid-template-columns: repeat(10, 1fr); gap: 10px; margin-top: 30px; }
.mini img { width: 100%; height: 150px; object-fit: contain; background: #f9f7f2; border: 1px solid #d8d5cf; }
.txt .ft { position: absolute; left: 56px; right: 56px; bottom: 30px; display: flex; justify-content: space-between; font-size: 9px; letter-spacing: .22em; text-transform: uppercase; color: #6f6e6b; }
"""

cards = "\n".join(f'<div class="card{" wide" if w[8] else ""}"><div class="box"><img src="img/{w[0]}.jpg"></div><div class="cap">{w[1]}<span>{i:02d}</span></div></div>'
                  for i, w in enumerate(works, 1))
n = len(works); pages = []
for i, ((k, t, y, m, sz, pr, tools, an, wide), d) in enumerate(zip(works, descs), 1):
    pages.append(f'''<section class="page work"><div class="bg"></div>
  <div class="panel"><div class="num">{i:02d} / {n:02d}</div><h2 class="cp">{t}</h2>
    <dl class="meta"><dt>Year</dt><dd>{y}</dd><dt>Medium</dt><dd>{m}</dd><dt>Size</dt><dd>{sz}</dd><dt>Tools</dt><dd>{tools}</dd><dt>Output</dt><dd>{an}</dd><dt>Retail</dt><dd class="price">{pr}</dd></dl>
    <div class="desc">{d}</div></div>
  <div class="stage"><div class="frame{" wide" if wide else ""}{" raw" if k in ("dazzle-mass","disassembly") else ""}"><img src="img/{k}.jpg"></div></div>
</section>''')

tbody = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
thead = "".join(f"<th>{c}</th>" for c in rows[0])
mini = "".join(f'<img src="img/{w[0]}.jpg">' for w in works)
ft = '<div class="ft"><span>Evan Emery · Phoenix, Arizona</span><span>Selected works · 2024 — 2025</span></div>'

# split statement: first 4 paragraphs col 1-2, rest col 3
sp = re.findall(r"<p>.*?</p>", statement)
c1, c2, c3 = "".join(sp[:3]), "".join(sp[3:5]), "".join(sp[5:])

html_doc = f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Evan Emery — Selected Works — </title>
<link rel="stylesheet" href="fonts/fonts-local.css"><style>{CSS}</style></head><body>
<section class="page hero"><img src="img/deep-blue.jpg"><div class="shade"></div>
  <div class="tag">Call to Artists · Art, Architecture &amp; Interior Design · October 2026</div>
  <div class="t"><h1 class="cp">EVAN EMERY<br>SELECTED WORKS</h1><div class="sub">Human &nbsp;×&nbsp; Machine &nbsp;·&nbsp; Nine works &nbsp;·&nbsp; 2024 — 2025</div></div>
  <div class="r">Phoenix, Arizona<br>@evanemerydesign</div>
</section>
<section class="page cover">
  <div class="hd"><div><h1 class="cp">SELECTED WORKS</h1><div class="sub">Human &nbsp;×&nbsp; Machine</div></div>
    <div class="r"><h1 class="cp">EVAN EMERY</h1><div class="sub">Nine works · 2024 — 2025</div></div></div>
  <div class="grid">{cards}</div>
  <div class="ft">Exploring the duality of technology juxtaposed with the pure human form</div>
</section>
{chr(10).join(pages)}
<section class="page txt">
  <div class="hd"><h1 class="cp">Artist statement</h1><div class="sub">Evan Emery · Phoenix, Arizona</div></div>
  <div class="tag">{COPY["lede"]}</div>
  <div class="cols2"><div>{P(COPY["brief"])}</div><div><div class="tag2">{COPY["about_lede"]}</div>{P(COPY["about"])}</div></div>
  {ft}
</section>
<section class="page txt">
  <div class="hd"><h1 class="cp">Works submitted · 9 pieces</h1><div class="sub">All works available · retail prices at 50% consignment</div></div>
  <div class="two"><div><table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table></div>
    <div class="contact"><h3>Contact</h3>
      <div><span class="k">Name</span>{info.get("Name","")}</div>
      <div><span class="k">Location</span>{info.get("Location","")}</div>
      <div><span class="k">Email</span>{info.get("Email","")}</div>
      <div><span class="k">Instagram</span>@evanemerydesign</div>
      <div><span class="k">LinkedIn</span>linkedin.com/in/evan-emery-2021</div>
    </div></div>
  <div class="mini">{mini}</div>
  {ft}
</section>
</body></html>'''
hp = os.path.join(S, "EvanEmery_SelectedWorks.html")
open(hp, "w", encoding="utf-8").write(html_doc)
pdf = hp[:-5] + ".pdf"
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=12000",
                f"--print-to-pdf={pdf}", "file:///" + hp.replace("\\", "/")], capture_output=True, text=True, timeout=170)
import fitz
d = fitz.open(pdf); print("pages", len(d), os.path.getsize(pdf)//1024, "KB")
for i in (0,):
    d[i].get_pixmap(dpi=72).save(os.path.join(S, f"fin_p{i+1}.png"))
