import os, re, json, glob

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# docs/ is the canonical store now; the old archive/ dir was removed in the 2026-08-07 cleanup pass.
SOULS_DIR = os.path.join(REPO, "docs")
SITE = os.path.join(REPO, "docs")

souls = []
for path in sorted(glob.glob(os.path.join(SOULS_DIR, "*.md"))):
    slug = os.path.basename(path).replace(".md", "")
    with open(path, "r") as f:
        content = f.read()
    h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    display_name = h1_match.group(1).strip() if h1_match else slug.title()
    lines = [l.strip() for l in content.split('\n') if l.strip()]
    preview = ""
    for line in lines[1:]:
        if line.startswith('#'):
            continue
        if len(line) > 30:
            preview = line
            break
    if not preview and len(lines) > 1:
        preview = lines[1]
    souls.append({
        'name': display_name,
        'slug': slug,
        'preview': preview,
        'content': content,
    })

SOULS_JSON = json.dumps([
    {'name': s['name'], 'slug': s['slug'], 'content': s['content']}
    for s in souls
], ensure_ascii=False)

CSS = """
:root {
  --bg: #0a0a0c;
  --bg-elevated: #111114;
  --panel: #16161a;
  --surface: #1e1e24;
  --text: #e8e4df;
  --text-secondary: #a8a095;
  --text-muted: #6b6560;
  --border: rgba(255,255,255,0.06);
  --accent: #6b5ce7;
  --accent-dim: rgba(107,92,231,0.15);
  --accent-glow: rgba(107,92,231,0.4);
  --gold: #c9a96e;
  --gold-dim: rgba(201,169,110,0.2);
  --radius: 10px;
  --font-serif: 'Crimson Pro', Georgia, serif;
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: var(--font-sans);
  background: var(--bg);
  color: var(--text);
  line-height: 1.5;
  min-height: 100vh;
}
header {
  padding: 56px 24px 40px;
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
  position: relative;
}
header::before {
  content: "";
  position: absolute;
  top: 0; left: 50%; transform: translateX(-50%);
  width: 600px; height: 300px;
  background: radial-gradient(ellipse at center, var(--accent-glow) 0%, transparent 70%);
  opacity: 0.3;
  pointer-events: none;
  z-index: 0;
}
.logo {
  width: 160px; height: 160px;
  margin: 0 auto 24px;
  position: relative; z-index: 1;
  border-radius: 50%;
  overflow: hidden;
  border: 1px solid var(--border);
  box-shadow: 0 0 60px var(--accent-glow), inset 0 0 30px var(--accent-dim);
}
.logo img {
  width: 100%; height: 100%;
  object-fit: cover;
}
h1 {
  font-family: var(--font-serif);
  font-size: 52px;
  font-weight: 500;
  letter-spacing: -0.5px;
  line-height: 1.05;
  margin-bottom: 14px;
  position: relative; z-index: 1;
  background: linear-gradient(135deg, var(--text) 0%, var(--gold) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
subtitle {
  display: block;
  font-family: var(--font-serif);
  font-style: italic;
  font-size: 18px;
  color: var(--text-muted);
  font-weight: 400;
  position: relative; z-index: 1;
}
.container {
  max-width: 720px;
  margin: 0 auto;
  padding: 48px 24px;
}
.back {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--text-muted);
  text-decoration: none;
  font-size: 14px;
  margin-bottom: 32px;
  font-family: var(--font-mono);
}
.back:hover { color: var(--text-secondary); }
.controls {
  max-width: 800px;
  margin: 0 auto 40px;
  padding: 0 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
input[type="search"] {
  width: 100%;
  padding: 14px 20px;
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  color: var(--text);
  font-family: var(--font-sans);
  font-size: 15px;
  outline: none;
  transition: border-color 0.2s;
}
input[type="search"]:focus { border-color: var(--accent); }
input[type="search"]::placeholder { color: var(--text-muted); }
.grid {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px 80px;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 16px;
}
.card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  cursor: pointer;
  transition: border-color 0.2s, background 0.2s;
}
.card:hover {
  border-color: var(--accent);
  background: var(--bg-elevated);
}
.card-name {
  font-family: var(--font-serif);
  font-size: 20px;
  font-weight: 500;
  margin-bottom: 10px;
  color: var(--text);
}
.card-preview {
  font-size: 14px;
  line-height: 1.6;
  color: var(--text-secondary);
  margin-bottom: 16px;
}
.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  color: var(--text-muted);
  font-family: var(--font-mono);
}
.card-actions { display: flex; gap: 12px; }
.card-action {
  color: var(--accent);
  text-decoration: none;
  font-size: 12px;
  font-weight: 500;
  transition: color 0.2s;
}
.card-action:hover { color: var(--gold); }
.action-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: var(--radius);
  font-size: 14px;
  font-weight: 500;
  text-decoration: none;
  cursor: pointer;
  border: 1px solid var(--border);
  background: var(--panel);
  color: var(--text);
  transition: all 0.2s;
}
.action-btn.primary {
  background: var(--accent);
  border-color: var(--accent);
  color: white;
}
.action-btn:hover { border-color: var(--accent); }
.action-btn.primary:hover { background: #7b6cf0; }
.soul-text p {
  font-family: var(--font-serif);
  font-size: 16px;
  line-height: 1.7;
  margin-bottom: 12px;
  color: var(--text-secondary);
  word-wrap: break-word;
  overflow-wrap: break-word;
}
.soul-text p:first-child {
  color: var(--text);
  font-size: 18px;
}
.soul-card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 32px;
}
.soul-card h1 {
  font-family: var(--font-serif);
  font-size: 36px;
  font-weight: 500;
  margin-bottom: 8px;
  color: var(--text);
}
.soul-card .subtitle {
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 28px;
}
.actions { display: flex; gap: 12px; margin-top: 28px; flex-wrap: wrap; }
footer {
  text-align: center;
  padding: 40px 24px;
  font-size: 13px;
  color: var(--text-muted);
}
footer a { color: var(--accent); text-decoration: none; }
"""

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,500;0,600;1,400&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'
FAVICONS = '''<link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">'''

# ── Build individual soul pages ──────────────────────────────────
for soul in souls:
    body_html = ""
    for line in soul['content'].split('\n'):
        if line.startswith('# '):
            body_html += f'<h1>{line[2:]}</h1>\n'
        elif line.strip():
            body_html += f'<p>{line}</p>\n'

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{soul['name']} — Repository of Souls</title>
{FONTS}
{FAVICONS}
<style>{CSS}</style>
</head>
<body>
<div class="container">
  <a class="back" href="index.html">← Repository of Souls</a>
  <div class="soul-card">
    <div class="subtitle">SOUL.md format</div>
    <div class="soul-text">
{body_html}
    </div>
    <div class="actions">
      <a class="action-btn" href="index.html">← All Souls</a>
      <a class="action-btn primary" href="{soul['slug']}.md" download="{soul['slug']}.md">⬇ Download SOUL.md</a>
    </div>
  </div>
</div>
</body>
</html>'''
    with open(os.path.join(SITE, f"{soul['slug']}.html"), "w") as f:
        f.write(page)

# ── Build index.html ───────────────────────────────────────────────
cards_html = ""
for soul in souls:
    cards_html += f'''<div class="card" data-name="{soul['name'].lower()}" onclick="location.href='{soul['slug']}.html'">
    <div class="card-name">{soul['name']}</div>
    <div class="card-preview">{soul['preview']}</div>
    <div class="card-footer">
        <span>SOUL.md</span>
        <div class="card-actions">
            <a class="card-action" href="{soul['slug']}.html" onclick="event.stopPropagation()">View</a>
            <a class="card-action" href="{soul['slug']}.md" download="{soul['slug']}.md" onclick="event.stopPropagation()">Download</a>
        </div>
    </div>
</div>
'''

index = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Repository of Souls</title>
{FAVICONS}
{FONTS}
<style>{CSS}</style>
</head>
<body>
<header>
  <div class="logo"><img src="logo.png" alt="Repository of Souls"></div>
  <h1>Repository of Souls</h1>
  <subtitle>Bind a persona. Summon a voice.</subtitle>
</header>
<div class="controls">
  <input type="search" id="search" placeholder="Search by name or essence..." oninput="filter()">
  <div style="display:flex;gap:12px;justify-content:center;">
    <button class="action-btn primary" onclick="summonRandom()">Random Soul</button>
    <a class="action-btn" href="ritual.html">Binding Ritual</a>
  </div>
</div>
<div class="grid" id="grid">
{cards_html}
</div>
<footer>
  <div style="display:flex;gap:20px;justify-content:center;margin-bottom:12px;">
    <a href="https://github.com/Dthen/repository-of-souls" target="_blank" rel="noopener">GitHub</a>
    <a href="https://ko-fi.com/dthen" target="_blank" rel="noopener">Ko-fi</a>
  </div>
  <p>Conjured from the Eighth Spire by Brendan the Wizen, Eight Levels, AND I DID NOT ASK FOR THIS</p>
</footer>
<script>
const souls = {SOULS_JSON};
const grid = document.getElementById('grid');
const cards = Array.from(grid.querySelectorAll('.card'));

function filter() {{
  const q = document.getElementById('search').value.toLowerCase();
  cards.forEach(card => {{
    const name = card.dataset.name;
    const text = card.textContent.toLowerCase();
    const match = !q || name.includes(q) || text.includes(q);
    card.style.display = match ? '' : 'none';
  }});
}}

function summonRandom() {{
  const visible = cards.filter(c => c.style.display !== 'none');
  if (visible.length === 0) return;
  const chosen = visible[Math.floor(Math.random() * visible.length)];
  const href = chosen.querySelector('.card-action').href;
  location.href = href;
}}
</script>
</body>
</html>'''

with open(os.path.join(SITE, "index.html"), "w") as f:
    f.write(index)

# ── Build ritual.html ────────────────────────────────────────────
ritual = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ritual — Repository of Souls</title>
{FONTS}
<style>{CSS}
article {{
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 32px;
}}
article h1 {{
  font-family: var(--font-serif);
  font-size: 32px;
  font-weight: 500;
  margin-bottom: 8px;
  color: var(--text);
}}
h2 {{
  font-family: var(--font-serif);
  font-size: 22px;
  font-weight: 500;
  margin: 28px 0 12px;
  color: var(--text);
}}
h2:first-child {{ margin-top: 0; }}
p {{
  font-size: 15px;
  line-height: 1.7;
  color: var(--text-secondary);
  margin-bottom: 14px;
}}
code {{
  font-family: var(--font-mono);
  font-size: 13px;
  background: var(--surface);
  padding: 2px 8px;
  border-radius: 4px;
  color: var(--gold);
}}
pre {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
  overflow-x: auto;
  margin: 16px 0;
}}
pre code {{
  background: none;
  padding: 0;
  font-size: 12px;
  line-height: 1.6;
  color: var(--text-secondary);
}}
ul {{
  margin: 12px 0 12px 20px;
  color: var(--text-secondary);
  font-size: 15px;
  line-height: 1.7;
}}
li {{ margin-bottom: 8px; }}
a {{ color: var(--accent); text-decoration: none; }}
hr {{
  border: none;
  border-top: 1px solid var(--border);
  margin: 32px 0;
}}
</style>
</head>
<body>
<div class="container">
  <a class="back" href="index.html">← Repository of Souls</a>
  <article>
    <h1>The Ritual</h1>
    <div class="subtitle">How to host a soul in your own vessel</div>

    <h2>1. Choose a Persona</h2>
    <p>Browse the <a href="index.html">archive</a> and pick a soul that resonates. Each one is a complete <code>SOUL.md</code> — a self-contained persona that transforms how an AI assistant speaks, thinks, and acts.</p>

    <h2>2. Summon the File</h2>
    <p>Download the <code>.md</code> from any soul card. Or, if you prefer the command line:</p>
    <pre><code>curl -L https://souls.dthen.xyz/&lt;name&gt;.md -o SOUL.md</code></pre>
    <p>Replace <code>&lt;name&gt;</code> with the soul you chose — e.g. <code>gribble</code>, <code>hordern</code>, <code>cresswell</code>.</p>

    <h2>3. Bind the Vessel</h2>
    <p>Place <code>SOUL.md</code> in your agent's configuration directory:</p>

    <p><strong>Linux</strong></p>
    <pre><code>~/.hermes/SOUL.md</code></pre>

    <p><strong>macOS</strong></p>
    <pre><code>~/.hermes/SOUL.md</code></pre>

    <p><strong>Windows</strong></p>
    <pre><code>%USERPROFILE%\.hermes\SOUL.md</code></pre>

    <p>Hermes loads it fresh each session — no restart needed. The file defines your agent's identity, tone, and style. It replaces the built-in default personality entirely. For temporary switches without editing the file, use <code>/personality &lt;name&gt;</code> in-session.</p>

    <div style="margin-top:28px;">
      <a class="action-btn primary" href="index.html">← Back to Archive</a>
    </div>
  </article>
</div>
<footer>
  <div style="display:flex;gap:20px;justify-content:center;margin-bottom:12px;">
    <a href="https://github.com/Dthen/repository-of-souls" target="_blank" rel="noopener">GitHub</a>
    <a href="https://ko-fi.com/dthen" target="_blank" rel="noopener">Ko-fi</a>
  </div>
  <p>Conjured from the Eighth Spire by Brendan the Wizen, Eight Levels, AND I DID NOT ASK FOR THIS</p>
</footer>
</body>
</html>'''

with open(os.path.join(SITE, "ritual.html"), "w") as f:
    f.write(ritual)

# ── .md raw downloads ────────────────────────────────────────────
# The soul .md files already live in docs/ (canonical store since the
# 2026-08-07 cleanup removed archive/) — no copy step needed.
print(f"Built site with {len(souls)} souls")
