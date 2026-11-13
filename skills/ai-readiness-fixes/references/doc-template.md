# Branded document template

Use for documents and deliverable packs (policies, context files, structures, release notes, fix packs). Same design family as the report template.

## Header block (always, in any format)

Start every document with this block, translated into the document language:

```
[Plugin name] ✦
# [Document title]
[Organisation / subject] · Version [x.y] · [YYYY-MM-DD] · Owner: [role] · Status: Draft | Current
```

Then a 2–3 line summary, then the content. Keep headings consistent: numbered H2 sections, tables for structured content, code blocks for anything to paste.

## HTML version (when the environment can render HTML artifacts or files)

Copy the HTML below, fill every `{{PLACEHOLDER}}`, put the document content in the body sections, keep colours and layout. Static HTML and CSS only — no scripts.

```html
<!DOCTYPE html>
<html lang="{{LANG}}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}}</title>
<style>
  :root{--navy:#1C1E4E;--teal:#0E7480;--gold:#FFC448;--ink:#14162F;--muted:#5B6275;--bg:#F6F7FB;--card:#FFFFFF;--line:#E3E6EF}
  *{box-sizing:border-box}
  body{margin:0;font-family:Inter,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink);line-height:1.55}
  .hero{background:linear-gradient(160deg,var(--navy),var(--teal));color:#fff;padding:32px 28px 28px}
  .hero .brand{font-size:12px;letter-spacing:.12em;text-transform:uppercase;opacity:.8}
  .hero h1{margin:6px 0 8px;font-size:26px}
  .meta{display:flex;flex-wrap:wrap;gap:8px}
  .meta span{background:rgba(255,255,255,.14);border-radius:999px;padding:3px 10px;font-size:12.5px}
  .wrap{max-width:900px;margin:-18px auto 40px;padding:0 16px}
  .card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px 24px;margin-bottom:16px}
  .summary{border-left:4px solid var(--gold)}
  h2{font-size:17px;color:var(--navy);margin:0 0 10px}
  table{width:100%;border-collapse:collapse;font-size:14px}
  th{text-align:left;color:var(--muted);border-bottom:2px solid var(--line);padding:8px 6px}
  td{border-bottom:1px solid var(--line);padding:8px 6px;vertical-align:top}
  pre{background:#0F1230;color:#E8ECF7;border-radius:10px;padding:14px;overflow:auto;font-size:12.5px}
  .foot{color:var(--muted);font-size:12px;text-align:center;margin-top:20px}
  .accent{color:var(--gold)}
</style>
</head>
<body>
  <header class="hero">
    <div class="brand">{{PLUGIN_NAME}} <span class="accent">✦</span></div>
    <h1>{{TITLE}}</h1>
    <div class="meta"><span>{{SUBJECT}}</span><span>v{{VERSION}}</span><span>{{DATE}}</span><span>{{OWNER}}</span><span>{{STATUS}}</span></div>
  </header>
  <main class="wrap">
    <section class="card summary">{{SUMMARY}}</section>
    <!-- repeat: one card per numbered section -->
    <section class="card"><h2>{{N}}. {{SECTION_TITLE}}</h2>{{SECTION_CONTENT}}</section>
    <div class="foot">{{PLUGIN_NAME}} · {{FOOTER_NOTE}}</div>
  </main>
</body>
</html>
```
