"""Build index.html from src/site.template.html. Run: python3 src/build.py"""
import pathlib
R = pathlib.Path(__file__).resolve().parent.parent
s = (R/'src/site.template.html').read_text().replace('BUDDHA_PATH', (R/'src/buddha-path.txt').read_text().strip())
s = s.replace("window.__open=open;window.__curtain=v=>{start=v};", "")  # test hooks only in template
head = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="robots" content="noindex,nofollow,noarchive"><meta property="og:title" content="Sanket & Hemangi">'
        '<meta property="og:description" content="You are invited to our wedding, 29 November 2026, Thane">'
        '<meta property="og:image" content="https://sanketwedshemangi.github.io/invite-1.png">'
        '<style>html,body{margin:0}:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}img{max-width:100%}[hidden]{display:none!important}</style></head><body>')
(R/'index.html').write_text(head + s + '</body></html>')
print('built index.html')
