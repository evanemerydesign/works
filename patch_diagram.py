import os
S = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(S, "build_site.py"); t = open(p, encoding="utf-8").read()

def rep(a, b):
    global t
    assert a in t, a[:70]
    t = t.replace(a, b, 1)

DIAGRAM = r'''
DIAGRAM = """<svg class="dia" viewBox="0 0 1200 660" role="img" aria-labelledby="diaT diaD">
<title id="diaT">Thesis and concepts</title>
<desc id="diaD">Pure form held against applied overlay; code writes the mathematics that acts on the body; the result is pressed into cyanotype, plotted ink and pigment.</desc>
<defs>
  <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="12" cy="12" r="0.9" fill="#161616" opacity=".28"/></pattern>
  <pattern id="dz" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(-35)"><rect width="7" height="14" fill="#161616"/></pattern>
  <marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#161616"/></marker>
</defs>
<rect width="1200" height="660" fill="#f4f0ea"/><rect width="1200" height="660" fill="url(#dots)"/>

<!-- tier labels -->
<g class="lab"><text x="24" y="60">01 · Thesis</text><text x="24" y="300">02 · System</text><text x="24" y="510">03 · Output</text></g>

<!-- ROW 1: form vs overlay -->
<g class="box"><rect x="150" y="40" width="390" height="160"/>
  <text class="h" x="170" y="72">PURE FORM</text><text class="s" x="170" y="94">head · cube · sphere</text>
  <g stroke="#161616" stroke-width="2" fill="none">
    <ellipse cx="215" cy="150" rx="22" ry="28"/><path d="M215 178 v14 M204 192 h22"/>
    <path d="M300 128 l30 -17 l30 17 v34 l-30 17 l-30 -17 z M300 128 l30 17 l30 -17 M330 145 v51"/>
    <circle cx="430" cy="150" r="28"/><path d="M402 150 a28 12 0 0 0 56 0" stroke-dasharray="3 3"/>
  </g></g>
<g class="box"><rect x="660" y="40" width="390" height="160"/>
  <text class="h" x="680" y="72">APPLIED OVERLAY</text><text class="s" x="680" y="94">dazzle camouflage · pattern that dissolves readable shape</text>
  <g stroke="#161616" stroke-width="2"><rect x="700" y="118" width="70" height="70" fill="url(#dz)"/><circle cx="850" cy="153" r="36" fill="url(#dz)"/><ellipse cx="970" cy="153" rx="24" ry="32" fill="url(#dz)"/></g></g>
<path d="M545 120 H655" stroke="#161616" stroke-width="2" marker-start="url(#ah)" marker-end="url(#ah)"/>
<text class="s" x="600" y="108" text-anchor="middle">held in opposition</text>
<text class="cap" x="600" y="232" text-anchor="middle">Form and surface held in opposition. Surface prevails.</text>

<!-- authorship arrow -->
<path d="M855 200 V270" stroke="#161616" stroke-width="2" marker-end="url(#ah)"/>
<text class="s" x="870" y="240">authorship of the overlay: drawn → written</text>

<!-- ROW 2: code -> mathematics -> body -->
<g class="box"><rect x="150" y="280" width="250" height="140"/>
  <text class="h" x="170" y="312">CODE</text><text class="s" x="170" y="334">Rhino · Grasshopper · Blender</text><text class="s" x="170" y="352">I write the system that finds the pattern.</text></g>
<path d="M405 350 H470" stroke="#161616" stroke-width="2" marker-end="url(#ah)"/>
<g class="box"><rect x="475" y="280" width="290" height="140"/>
  <text class="h" x="495" y="312">MATHEMATICS</text><text class="s" x="495" y="334">fractal · vector field · recursive displacement</text><text class="s" x="495" y="352">height field · voxel · survey annotation</text><text class="s" x="495" y="378">Behaves according to its own nature.</text></g>
<path d="M770 350 H835" stroke="#161616" stroke-width="2" marker-end="url(#ah)"/>
<text class="s" x="802" y="340" text-anchor="middle">acts on</text>
<g class="box dark"><rect x="840" y="280" width="250" height="140"/>
  <text class="h" x="860" y="312">THE BODY</text><text class="s" x="860" y="334">head · figure · torso</text><text class="s" x="860" y="352">The surface the logic acts upon.</text><text class="s" x="860" y="378">A person and a proof at once.</text></g>

<!-- to output -->
<path d="M965 420 V450 H300 V488" stroke="#161616" stroke-width="2" fill="none"/>
<path d="M965 450 V488 M632 450 V488" stroke="#161616" stroke-width="2" marker-end="url(#ah)"/>
<path d="M300 486 V488" stroke="#161616" stroke-width="2" marker-end="url(#ah)"/>
<text class="s" x="632" y="442" text-anchor="middle">pressed into cotton rag</text>

<!-- ROW 3: outputs -->
<g class="box"><rect x="150" y="490" width="300" height="120"/>
  <text class="h" x="170" y="522">CYANOTYPE</text><text class="s" x="170" y="544">the blueprint's own chemistry</text><text class="s" x="170" y="562">geometry that was never photographed</text></g>
<g class="box"><rect x="482" y="490" width="300" height="120"/>
  <text class="h" x="502" y="522">PEN PLOTTER</text><text class="s" x="502" y="544">white ink · one stroke at a time</text><text class="s" x="502" y="562">CNC plotter · AxiDraw</text></g>
<g class="box"><rect x="815" y="490" width="300" height="120"/>
  <text class="h" x="835" y="522">PIGMENT</text><text class="s" x="835" y="544">archival inkjet · spray paint</text><text class="s" x="835" y="562">on fine art paper</text></g>
<text class="cap" x="632" y="644" text-anchor="middle">The digital carries no weight until it is pressed into paper.</text>
</svg>"""
'''
rep("rel = \"../\" if BARE else \"\"", DIAGRAM + "\nrel = \"../\" if BARE else \"\"")

# CSS for the diagram
rep("/* in situ */", """/* thesis diagram */
.dia {{ width:100%; height:auto; display:block; border:2px solid var(--ink); box-shadow:4px 4px 0 var(--rule); background:var(--bg); }}
.dia .lab text {{ font-family:'Space Mono', monospace; font-size:11px; letter-spacing:.22em; text-transform:uppercase; fill:#6f6e6b; }}
.dia .box rect {{ fill:#f9f7f2; stroke:#161616; stroke-width:2; }}
.dia .box.dark rect {{ fill:#12305e; }}
.dia .box.dark text {{ fill:#f4f0ea; }}
.dia .box.dark .s {{ fill:#c9d2e3; }}
.dia .h {{ font-family:'Chakra Petch', sans-serif; font-weight:700; font-size:20px; fill:#161616; }}
.dia .s {{ font-family:'Space Mono', monospace; font-size:11.5px; fill:#4a4a48; }}
.dia .cap {{ font-family:'Chakra Petch', sans-serif; font-weight:700; font-size:16px; text-transform:uppercase; letter-spacing:.04em; fill:#161616; }}
.dia-wrap {{ overflow-x:auto; }}
.dia-wrap svg {{ min-width:720px; }}
/* in situ */""")

# section: after statement, before works; hidden in bare
rep('''<section class="s" id="works"><div class="wrap">''', '''<section class="s" id="thesis" style="background:var(--bg2)"><div class="wrap">
  <div class="hd"><h2 class="cp">Thesis</h2><span class="lab">Form · surface · system · material</span></div>
  <div class="dia-wrap">{DIAGRAM}</div>
</div></section>

<section class="s" id="works"><div class="wrap">''')
rep('''<li id="navInsitu">''', '''<li id="navThesis"><a href="#thesis">Thesis</a></li><li id="navInsitu">''')
rep('''if (!ctxWorks.length) {{ $('insitu').hidden = true; $('navInsitu').hidden = true; }}''',
    '''if (!ctxWorks.length) {{ $('insitu').hidden = true; $('navInsitu').hidden = true; }}
if (C.hide_thesis) {{ $('thesis').hidden = true; $('navThesis').hidden = true; }}''')
rep('''  "insitu_label": "Framed and on the wall",''', '''  "insitu_label": "Framed and on the wall",
  "hide_thesis": BARE,''')
open(p, "w", encoding="utf-8").write(t); print("diagram patched")
