"""Macht aus LOGBUCH.md eine lesbare Seite für Adi und Dani.

Aufruf aus dem Projektordner:  python3 _build/logbuch_seite.py

Ergebnis ist _build/logbuch.html. Die Datei wird als Artifact veröffentlicht,
nicht auf die öffentliche Webseite gelegt, das Logbuch ist intern. Farben,
Schrift und Logo kommen aus assets/style.css, damit nichts doppelt gepflegt
werden muss. Nach jeder Änderung am Logbuch neu laufen lassen und das
Artifact neu veröffentlichen.
"""
import os, re, html
from build import TOTOP

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def e(s):
    return html.escape(s, quote=True)


def inline(s):
    """`Code` und **fett** in HTML umsetzen, alles andere maskieren."""
    out = e(s)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    return out


def lesen(pfad):
    """LOGBUCH.md in Titel, Vorspann, Regeln und Datumsabschnitte zerlegen."""
    zeilen = open(pfad, encoding="utf-8").read().split("\n")
    titel, vorspann, regeln, abschnitte = "", [], [], []
    i = 0
    while i < len(zeilen):
        z = zeilen[i].rstrip()
        if z.startswith("# "):
            titel = z[2:].strip()
        elif z.startswith("## "):
            abschnitte.append({"datum": z[3:].strip(), "eintraege": []})
        elif z.startswith("- "):
            regeln.append(z[2:].strip())
        elif z.startswith("**") and abschnitte:
            kopf = z.strip()
            m = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", kopf)
            name, rest = m.group(1), m.group(2)
            teile = [p.strip() for p in rest.split("·") if p.strip()]
            wer = teile[0] if teile else ""
            nummer = teile[1].strip("`") if len(teile) > 1 else ""
            text = []
            i += 1
            while i < len(zeilen) and zeilen[i].strip():
                text.append(zeilen[i].strip())
                i += 1
            abschnitte[-1]["eintraege"].append(
                {"name": name, "wer": wer, "nummer": nummer, "text": " ".join(text)})
            continue
        elif z and not abschnitte and not z.startswith("#"):
            vorspann.append(z)
        i += 1
    return titel, vorspann, regeln, abschnitte


def seite():
    titel, vorspann, regeln, abschnitte = lesen(os.path.join(ROOT, "LOGBUCH.md"))
    anzahl = sum(len(a["eintraege"]) for a in abschnitte)
    neuste = abschnitte[0]["datum"] if abschnitte else ""
    einleitung = " ".join(v for v in vorspann if not v.endswith(":"))

    gruppen = []
    for a in abschnitte:
        eintraege = []
        for x in a["eintraege"]:
            marke = (f'<span class="lb-nummer" title="Commit in Git">{e(x["nummer"])}</span>'
                     if x["nummer"] else
                     '<span class="lb-nummer offen" title="Commit-Nummer wird nachgetragen">noch offen</span>')
            eintraege.append(
                f'<article class="lb-eintrag">'
                f'<h3>{inline(x["name"])}</h3>'
                f'<p class="lb-meta"><span class="lb-wer">{e(x["wer"])}</span>{marke}</p>'
                f'<p class="lb-text">{inline(x["text"])}</p>'
                f'</article>')
        gruppen.append(
            f'<section class="lb-tag"><h2>{e(a["datum"])}</h2>'
            f'<div class="lb-eintraege">{"".join(eintraege)}</div></section>')

    regelliste = "".join(f"<li>{inline(r)}</li>" for r in regeln)

    return f"""<title>AVA-DAM Logbuch</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="assets/style.css">
<style>
/* Leseseite: eine Spalte, Einträge an einer Zeitachse, Farben und Schrift aus der CI */
body{{font-family:"Montserrat",system-ui,sans-serif}}
.lb-blatt{{max-width:760px;margin:0 auto;
  padding-left:max(16px,env(safe-area-inset-left,0px));
  padding-right:max(16px,env(safe-area-inset-right,0px));
  padding-block:48px 96px}}
.lb-kopf{{display:flex;flex-wrap:wrap;align-items:center;gap:16px;justify-content:space-between;margin-bottom:40px}}
.lb-kopf img{{height:30px;width:auto}}
.lb-schalter{{width:44px;height:44px;border-radius:999px;border:1px solid var(--line);background:transparent;
  color:var(--ink);cursor:pointer;display:grid;place-items:center;flex:none}}
.lb-schalter svg{{width:20px;height:20px}}
.lb-schalter .sun{{display:none}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]) .lb-schalter .moon{{display:none}}
  :root:not([data-theme="light"]) .lb-schalter .sun{{display:block}}}}
:root[data-theme="dark"] .lb-schalter .moon{{display:none}}
:root[data-theme="dark"] .lb-schalter .sun{{display:block}}
h1{{font-size:clamp(32px,6vw,46px);line-height:1.1;letter-spacing:-.02em;color:var(--ink);margin:0 0 16px;text-wrap:balance}}
.lb-lead{{color:var(--text);font-size:18px;margin:0 0 12px;max-width:62ch}}
.lb-stand{{color:var(--muted);font-size:14px;margin:0 0 40px;font-variant-numeric:tabular-nums}}
.lb-regeln{{background:var(--soft);border:1px solid var(--line);border-radius:var(--r);padding:28px 28px 24px;margin-bottom:56px}}
.lb-regeln h2{{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 16px}}
.lb-regeln ul{{margin:0;padding-left:20px;display:grid;gap:10px}}
.lb-regeln li{{color:var(--text);font-size:15px;line-height:1.6}}
.lb-tag{{position:relative;padding-left:28px;padding-bottom:44px}}
.lb-tag:last-of-type{{padding-bottom:0}}
.lb-tag::before{{content:"";position:absolute;left:5px;top:6px;bottom:0;width:2px;background:var(--line)}}
.lb-tag>h2{{font-size:14px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--blue-ink);
  margin:0 0 20px;position:relative;font-variant-numeric:tabular-nums}}
.lb-tag>h2::before{{content:"";position:absolute;left:-28px;top:3px;width:12px;height:12px;border-radius:999px;
  background:var(--blue);border:3px solid var(--bg);box-shadow:0 0 0 1px var(--line)}}
.lb-eintraege{{display:grid;gap:20px}}
.lb-eintrag{{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:24px 26px;min-width:0}}
.lb-eintrag h3{{margin:0 0 10px;font-size:19px;line-height:1.35;color:var(--ink);text-wrap:balance}}
.lb-meta{{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:0 0 14px}}
.lb-wer{{font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--blue-ink);
  background:var(--tagbg);border-radius:999px;padding:5px 12px}}
.lb-nummer{{font-family:ui-monospace,"SFMono-Regular",Menlo,Consolas,monospace;font-size:12px;color:var(--muted);
  border:1px solid var(--line);border-radius:999px;padding:4px 10px}}
.lb-nummer.offen{{font-family:inherit;font-style:italic}}
.lb-text{{margin:0;color:var(--text);font-size:16px;line-height:1.7}}
.lb-eintrag code,.lb-regeln code{{font-family:ui-monospace,"SFMono-Regular",Menlo,Consolas,monospace;font-size:.88em;
  background:var(--soft);border-radius:6px;padding:2px 6px}}
.lb-fuss{{border-top:1px solid var(--line);padding-top:24px;color:var(--muted);font-size:14px}}
@media (max-width:480px){{.lb-eintrag{{padding:20px}}.lb-regeln{{padding:22px 20px}}}}
</style>

<div class="lb-blatt">
<header class="lb-kopf">
  <img class="logo-light" src="assets/avadam-logo.svg" alt="AVA-DAM" width="668" height="126">
  <img class="logo-dark" src="assets/avadam-logo-dark.svg" alt="AVA-DAM" width="668" height="126">
  <button type="button" class="lb-schalter" id="theme" aria-label="Hell oder dunkel umschalten" title="Hell oder dunkel umschalten">
    <svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
    <svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
  </button>
</header>

<h1>{e(titel.split("·")[0].strip())}</h1>
<p class="lb-lead">{e(einleitung)}</p>
<p class="lb-stand">{anzahl} Einträge · neuster vom {e(neuste)}</p>

<div class="lb-regeln">
  <h2>So führen wir es</h2>
  <ul>{regelliste}</ul>
</div>

{"".join(gruppen)}

<p class="lb-fuss">Entsteht aus <code>LOGBUCH.md</code> im Repo. Wenn etwas fehlt, steht es dort noch nicht drin.</p>
</div>

<button type="button" class="totop" id="totop" aria-label="Nach oben" title="Nach oben">{TOTOP}</button>
<script>
(function(){{
  var t=document.getElementById('theme');
  try{{var g=localStorage.getItem('avadam-theme');if(g)document.documentElement.setAttribute('data-theme',g)}}catch(e){{}}
  t.addEventListener('click',function(){{
    var r=document.documentElement;
    var c=r.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
    var n=c==='dark'?'light':'dark';
    r.setAttribute('data-theme',n);
    try{{localStorage.setItem('avadam-theme',n)}}catch(e){{}}
  }});
  var b=document.getElementById('totop'),M=['apfel','roboter','stecker'],busy=false;
  b.setAttribute('data-motif',M[Math.floor(Math.random()*M.length)]);
  function f(){{if(busy)return;b.classList.toggle('show',window.scrollY>500)}}
  addEventListener('scroll',f,{{passive:true}});f();
  b.addEventListener('click',function(){{
    if(busy)return;
    if(matchMedia('(prefers-reduced-motion: reduce)').matches){{scrollTo(0,0);return}}
    busy=true;b.classList.add('go');
    setTimeout(function(){{scrollTo({{top:0,behavior:'smooth'}})}},650);
    setTimeout(function(){{b.classList.remove('go','show');busy=false}},2400);
  }});
}})();
</script>
"""


def main():
    ziel = os.path.join(HERE, "logbuch.html")
    open(ziel, "w", encoding="utf-8").write(seite())
    print("gebaut:", os.path.relpath(ziel, ROOT))


if __name__ == "__main__":
    main()
