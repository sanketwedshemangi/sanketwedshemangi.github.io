"""Build index.html (and hemangi/index.html, the Dhumal side's copy with its own Haldi) from src/site.template.html. Run: python3 src/build.py"""
import pathlib, re
R = pathlib.Path(__file__).resolve().parent.parent
s = (R/'src/site.template.html').read_text().replace('BUDDHA_PATH', (R/'src/buddha-path.txt').read_text().strip())
s, n = re.subn(r"/\*hooks\*/.*?/\*/hooks\*/", "", s, flags=re.S)  # test hooks live only in the template
assert n == 1, 'test hook marker missing from template'
head = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="robots" content="noindex,nofollow,noarchive"><meta property="og:title" content="Sanket & Hemangi">'
        '<meta property="og:description" content="You are invited to our wedding, 29 November 2026, Thane">'
        '<meta property="og:image" content="https://sanketwedshemangi.github.io/invite-1.png">'
        '<link rel="preconnect" href="https://fonts.googleapis.com"><style>html,body{margin:0}:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}img{max-width:100%}[hidden]{display:none!important}</style></head><body>')
(R/'index.html').write_text(head + s + '</body></html>')
# Hemangi's side holds its own Haldi; everything else is the same invite.
HALDI = ('<div class="when">Friday, 27 November 2026<br>6:00 pm onwards</div>\n'
         '     <div class="where">A-02 Kamal, New Mandala, BARC Colony, Mumbai 400094</div>\n'
         '     <a class="btn" href="https://www.google.com/maps/search/?api=1&amp;query=19.0379186,72.9349162"')
assert s.count(HALDI) == 1, 'Haldi block changed; update the Hemangi copy'
h = s.replace(HALDI, '<div class="when">Friday, 27 November 2026<br>5:00 pm onwards</div>\n'
              '     <div class="where">Silverador Boutique Hotel, Hall on the 6th floor, Opp R-Mall, Ghodbunder Road, Manpada, Thane (W) 400607</div>\n'
              '     <a class="btn" href="https://www.google.com/maps/search/?api=1&amp;query=Silverador+Boutique+Hotel+Manpada+Thane"')
(R/'hemangi').mkdir(exist_ok=True)
(R/'hemangi/index.html').write_text(head + h + '</body></html>')
print('built index.html and hemangi/index.html')
