"""Baut die statischen Seiten von AVA-DAM (DE im Stamm, EN/IT/FR in Unterordnern).

Aufruf aus dem Projektordner:  python3 _build/build.py
Bei eigener Domain nur BASE anpassen und neu bauen.
"""
import json, os, html
from content import T, LANGS, LANG_NAMES, LOCALE, PROJECT_URLS

BASE = "https://avadam26.github.io/avadam/"
TODAY = "2026-10-21"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)

def path_of(lang):            # relativer Pfad der Sprachseite
    return "" if lang == "de" else f"{lang}/"

def url_of(lang):
    return BASE + path_of(lang)

def e(s):
    return html.escape(s, quote=True)


MOON = '<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
SUN = '<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'

# Drei Motive: Apfel (Human, Adams Apfel), Roboter (Technology), Stecker (Together)
TOTOP = (
 '<svg class="m-apfel" viewBox="0 0 64 64" aria-hidden="true">'
 '<path d="M32 19C24 12 9 14 9 32c0 16 10 27 18 27 3 0 3.5-2 5-2s2 2 5 2c8 0 18-11 18-27 0-18-15-20-23-13z" fill="#D93A3A"/>'
 '<path d="M32 19C24 12 9 14 9 32c0 16 10 27 18 27 3 0 3.5-2 5-2" fill="none" stroke="#A82525" stroke-width="1.5" opacity=".5"/>'
 '<ellipse cx="19" cy="31" rx="3" ry="7" fill="#fff" opacity=".45" transform="rotate(15 19 31)"/>'
 '<path d="M32 19c0-6 2-10 5-13" fill="none" stroke="#6B4423" stroke-width="3" stroke-linecap="round"/>'
 '<path d="M35 12c4-8 13-8 16-5-4 7-12 8-16 5z" fill="#3FA34D"/>'
 '<g class="bite" style="fill:var(--bg)"><circle cx="56" cy="29" r="6.5"/><circle cx="55" cy="39" r="6"/></g>'
 '</svg>'
 '<svg class="m-roboter" viewBox="0 0 64 64" aria-hidden="true">'
 '<g class="flame"><path d="M22 58q3.5 16 7 0z" fill="#FF9F1C"/><path d="M35 58q3.5 16 7 0z" fill="#FF9F1C"/><path d="M23.5 58q2 9 4 0z" fill="#FFE066"/><path d="M36.5 58q2 9 4 0z" fill="#FFE066"/></g>'
 '<line x1="32" y1="5" x2="32" y2="12" stroke="#101B35" stroke-width="2.5"/><circle cx="32" cy="5" r="3.5" fill="#3C82D9"/>'
 '<rect x="13" y="12" width="38" height="25" rx="9" fill="#3C82D9" stroke="#FFFFFF" stroke-width="1.5"/>'
 '<rect x="18.5" y="17" width="27" height="14" rx="6" fill="#101B35"/>'
 '<circle cx="26" cy="24" r="3.2" fill="#7FE3FF"/><circle cx="38" cy="24" r="3.2" fill="#7FE3FF"/>'
 '<rect x="11" y="40" width="6" height="11" rx="3" fill="#3C82D9" stroke="#FFFFFF" stroke-width="1.2"/><rect x="47" y="40" width="6" height="11" rx="3" fill="#3C82D9" stroke="#FFFFFF" stroke-width="1.2"/>'
 '<rect x="19" y="38" width="26" height="17" rx="6" fill="#101B35" stroke="#FFFFFF" stroke-width="1.5"/>'
 '<circle cx="32" cy="46.5" r="3.2" fill="#3C82D9"/>'
 '<rect x="21.5" y="54" width="8" height="5" rx="2" fill="#101B35" stroke="#FFFFFF" stroke-width="1.2"/><rect x="34.5" y="54" width="8" height="5" rx="2" fill="#101B35" stroke="#FFFFFF" stroke-width="1.2"/>'
 '</svg>'
 '<svg class="m-stecker" viewBox="0 0 64 64" aria-hidden="true">'
 '<g class="spark" stroke="#FFC233" stroke-width="2.5" stroke-linecap="round"><path d="M20 4l-4-4"/><path d="M44 4l4-4"/><path d="M32 1v-5"/></g>'
 '<rect x="23" y="3" width="5" height="13" rx="1.5" fill="#C9D2E3" stroke="#8A95AB" stroke-width="1"/><rect x="36" y="3" width="5" height="13" rx="1.5" fill="#C9D2E3" stroke="#8A95AB" stroke-width="1"/>'
 '<rect x="15" y="14" width="34" height="23" rx="7" fill="#3C82D9" stroke="#FFFFFF" stroke-width="1.5"/>'
 '<path d="M22 22h20M22 28h20" stroke="#2A6CC0" stroke-width="2.5" stroke-linecap="round"/>'
 '<path d="M24 37h16l-4 9h-8z" fill="#101B35" stroke="#FFFFFF" stroke-width="1.2" stroke-linejoin="round"/>'
 '<path d="M32 46c0 7-7 8-7 13 0 3 3 5 7 7" fill="none" stroke="#FFFFFF" stroke-width="8.5" stroke-linecap="round"/>'
 '<path d="M32 46c0 7-7 8-7 13 0 3 3 5 7 7" fill="none" stroke="#101B35" stroke-width="6" stroke-linecap="round"/>'
 '</svg>')

JS = ("(function(){var b=document.getElementById('totop'),M=['apfel','roboter','stecker'];"
 "b.setAttribute('data-motif',M[Math.floor(Math.random()*M.length)]);var busy=false;"
 "function f(){if(busy)return;b.classList.toggle('show',window.scrollY>500)}"
 "addEventListener('scroll',f,{passive:true});f();"
 "b.addEventListener('click',function(){if(busy)return;"
 "if(matchMedia('(prefers-reduced-motion: reduce)').matches){scrollTo(0,0);return}"
 "busy=true;b.classList.add('go');"
 "setTimeout(function(){scrollTo({top:0,behavior:'smooth'})},650);"
 "setTimeout(function(){b.classList.remove('go','show');busy=false},2400)});"
 "var g=document.getElementById('burger'),P=document.getElementById('mmenu');function sm(o){P.hidden=!o;g.setAttribute('aria-expanded',o?'true':'false')}g.addEventListener('click',function(){sm(P.hidden)});P.addEventListener('click',function(e){if(e.target.closest('a'))sm(false)});addEventListener('keydown',function(e){if(e.key==='Escape'&&!P.hidden){sm(false);g.focus()}});addEventListener('resize',function(){if(innerWidth>860)sm(false)});var t=document.getElementById('theme');t.addEventListener('click',function(){var r=document.documentElement;"
 "var c=r.getAttribute('data-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');"
 "var n=c==='dark'?'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem('avadam-theme',n)}catch(e){}})})();")

ANCHORS = ["bereiche", "projekte", "geschichte", "kontakt"]

def jsonld(lang, t, r):
    org = {
        "@type": "Organization", "@id": BASE + "#org",
        "name": "AVA-DAM", "alternateName": ["AVADAM", "AVA DAM"],
        "url": BASE, "logo": BASE + "assets/avadam-logo.svg", "image": BASE + "assets/og-image.png",
        "slogan": "Human + Technology. Together.",
        "description": T["en"]["desc"],
        "founder": [{"@type": "Person", "name": "Adrian von Arb"}, {"@type": "Person", "name": "Daniel Muccio"}],
        "address": [
            {"@type": "PostalAddress", "postalCode": "4632", "addressLocality": "Trimbach", "addressCountry": "CH"},
            {"@type": "PostalAddress", "postalCode": "PH26 3JN", "addressLocality": "Grantown-on-Spey", "addressRegion": "Scotland", "addressCountry": "GB"},
        ],
        "knowsAbout": ["Web design", "Websites", "Software development", "Motion design", "Interactive maps", "Artificial intelligence", "SEO"],
        "knowsLanguage": ["de", "en", "it", "fr"],
    }
    site = {"@type": "WebSite", "@id": BASE + "#website", "url": BASE, "name": "AVA-DAM",
            "inLanguage": LANGS, "publisher": {"@id": BASE + "#org"}}
    page = {"@type": "WebPage", "@id": url_of(lang) + "#page", "url": url_of(lang), "name": t["title"],
            "description": t["desc"], "inLanguage": lang, "isPartOf": {"@id": BASE + "#website"},
            "about": {"@id": BASE + "#org"}, "primaryImageOfPage": BASE + "assets/og-image.png"}
    works = {"@type": "ItemList", "name": t["proj_h2"], "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "item": {
            "@type": "SoftwareApplication" if key == "guardops" else "CreativeWork",
            **({"applicationCategory": "BusinessApplication", "operatingSystem": "Web"} if key == "guardops" else {}),
            "name": name, "description": desc, "url": PROJECT_URLS[key], "creator": {"@id": BASE + "#org"}}}
        for i, (key, name, tags, desc) in enumerate(t["projects"])]}
    vids = [{"@type": "VideoObject", "name": f"{title} · Garden Park Guest House", "description": cap,
             "thumbnailUrl": BASE + f"media/{key}-poster.jpg", "contentUrl": BASE + f"media/{key}.mp4",
             "uploadDate": TODAY, "inLanguage": "de", "creator": {"@id": BASE + "#org"}}
            for key, title, cap in t["videos"]]
    # FAQPage-Schema erst einfügen, wenn echte Fragen und Antworten feststehen.
    return json.dumps({"@context": "https://schema.org", "@graph": [org, site, page, works] + vids},
                      ensure_ascii=False, indent=1)

def lang_links(lang, r, label):
    out = [f'<nav class="langs" aria-label="{e(label)}">']
    for l in LANGS:
        cur = ' aria-current="true"' if l == lang else ""
        out.append(f'<a href="{r}{path_of(l) or "./"}" hreflang="{l}" lang="{l}" title="{LANG_NAMES[l]}"{cur}>{l.upper()}</a>')
    out.append("</nav>")
    return "".join(out)

def page(lang):
    t = T[lang]; r = "" if lang == "de" else "../"
    A = r + "assets/"; M = r + "media/"
    alt = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{url_of(l)}">' for l in LANGS)
    alt += f'\n<link rel="alternate" hreflang="x-default" href="{url_of("de")}">'
    og_alt = "\n".join(f'<meta property="og:locale:alternate" content="{LOCALE[l]}">' for l in LANGS if l != lang)
    nav = "".join(f'<a href="#{a}">{e(n)}</a>' for a, n in zip(ANCHORS, t["nav"]))

    areas = "".join(f'<article class="card"><span class="num">0{i+1}</span><h3>{e(h)}</h3><p>{e(p)}</p></article>'
                    for i, (h, p) in enumerate(t["areas"]))

    def pic(key, name):
        if key == "vku":
            return f'<div class="pic"><img src="{M}vku.jpg" alt="{e(name)}" width="1280" height="800" loading="lazy"></div>'
        if key == "karte":
            return f'<div class="pic"><img src="{M}karte-poster.jpg" alt="{e(name)}" width="720" height="1280" loading="lazy" style="object-position:50% 40%"></div>'
        if key == "butterfly":
            return f'<div class="pic"><img src="{M}butterfly.jpg" alt="{e(name)}, Grantown-on-Spey" width="1280" height="800" loading="lazy" style="object-position:50% 60%"></div>'
        cls = "navy"
        sub = "Swiss security software"
        return f'<div class="pic type {cls}" aria-hidden="true"><span>{e(name)}<small>{e(sub)}</small></span></div>'

    projects = "".join(
        f'<a class="proj" href="{PROJECT_URLS[key]}" target="_blank" rel="noopener">{pic(key, name)}'
        f'<div class="body"><div class="tags">' +
        "".join(f'<span class="tag{" grey" if j else ""}">{e(tg)}</span>' for j, tg in enumerate(tags)) +
        f'</div><h3>{e(name)}</h3><p>{e(desc)}</p><span class="more">{e(t["proj_more"])} ↗</span></div></a>'
        for key, name, tags, desc in t["projects"])

    videos = "".join(
        f'<figure class="reel"><video controls playsinline preload="none" poster="{M}{key}-poster.jpg" width="720" height="1280" aria-label="{e(title)}">'
        f'<source src="{M}{key}.mp4" type="video/mp4">{e(t["video_fallback"])}</video>'
        f'<figcaption><strong>{e(title)}</strong>{e(cap)}</figcaption></figure>'
        for key, title, cap in t["videos"])

    story = "".join(f"<p>{p}</p>" for p in t["story"])
    places = "".join(f'<div class="card place"><span class="country">{e(c)}</span><h3 style="margin-top:12px">{e(n)}</h3>'
                     f'<address>{e(a)}<br>{e(c)}</address></div>' for c, n, a in t["places"])

    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="author" content="AVA-DAM · Adrian von Arb, Daniel Muccio">
<link rel="canonical" href="{url_of(lang)}">
{alt}
<meta property="og:type" content="website">
<meta property="og:site_name" content="AVA-DAM">
<meta property="og:title" content="{e(t["title"])}">
<meta property="og:description" content="{e(t["desc"])}">
<meta property="og:url" content="{url_of(lang)}">
<meta property="og:image" content="{BASE}assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(t["logo_alt"])}">
<meta property="og:locale" content="{LOCALE[lang]}">
{og_alt}
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0A1020" media="(prefers-color-scheme: dark)">
<script>try{{var m=localStorage.getItem("avadam-theme");if(m)document.documentElement.dataset.theme=m}}catch(e){{}}</script>
<link rel="icon" href="{r}favicon.ico" sizes="32x32">
<link rel="icon" href="{A}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{A}apple-touch-icon.png">
<link rel="preload" href="{A}fonts/montserrat-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{A}style.css">
<link rel="alternate" type="text/plain" href="{BASE}llms.txt" title="LLM summary">
<script type="application/ld+json">
{jsonld(lang, t, r)}
</script>
</head>
<body>
<a class="skip" href="#inhalt">{e(t["skip"])}</a>
<header class="top">
<div class="wrap">
<a class="brand" href="{r}{path_of(lang) or './'}" aria-label="AVA-DAM"><img class="logo-light" src="{A}avadam-logo.svg" alt="{e(t["logo_alt"])}" width="668" height="126"><img class="logo-dark" src="{A}avadam-logo-dark.svg" alt="" aria-hidden="true" width="668" height="126"></a>
<div class="nav"><nav class="links nav" aria-label="Menu">{nav}</nav><div class="right">{lang_links(lang, r, t["lang_label"])}<button type="button" class="theme" id="theme" aria-label="{e(t["theme_label"])}" title="{e(t["theme_label"])}">{MOON}{SUN}</button><button type="button" class="burger" id="burger" aria-expanded="false" aria-controls="mmenu" aria-label="{e(t["menu_label"])}"><span></span><span></span><span></span></button></div></div>
</div>
<div class="mpanel" id="mmenu" hidden><nav class="mlinks" aria-label="{e(t["menu_label"])}">{nav}</nav>{lang_links(lang, r, t["lang_label"])}</div>
</header>

<main id="inhalt">
<section class="hero" aria-labelledby="h1">
<div class="wrap">
<span class="eyebrow">{e(t["hero_eyebrow"])}</span>
<h1 id="h1">{t["h1"]}</h1>
<p class="lead">{e(t["hero_lead"])}</p>
<div class="btns"><a class="btn primary" href="#projekte">{e(t["btn_projects"])}</a><a class="btn ghost" href="#kontakt">{e(t["btn_contact"])}</a></div>
<div class="cable" aria-hidden="true"><span class="h">HUMAN</span><span class="wire"></span><span class="gap"></span><span class="socket"></span><span class="t">TECHNOLOGY.</span></div>
</div>
</section>

<section id="bereiche" class="areas" aria-labelledby="h-areas">
<div class="wrap">
<div class="head"><span class="eyebrow">{e(t["areas_eyebrow"])}</span><h2 id="h-areas">{e(t["areas_h2"])}</h2><p class="lead">{e(t["areas_lead"])}</p></div>
<div class="grid4">{areas}</div>
</div>
</section>

<section id="projekte" aria-labelledby="h-proj">
<div class="wrap">
<div class="head"><span class="eyebrow">{e(t["proj_eyebrow"])}</span><h2 id="h-proj">{e(t["proj_h2"])}</h2></div>
<div class="projects">{projects}</div>
</div>
</section>

<section id="motion" class="motion" aria-labelledby="h-motion">
<div class="wrap">
<div class="head"><span class="eyebrow">{e(t["motion_eyebrow"])}</span><h2 id="h-motion">{e(t["motion_h2"])}</h2><p class="lead" style="color:#C9D2E3">{e(t["motion_lead"])}</p></div>
<div class="reels">{videos}</div>
</div>
</section>

<section id="geschichte" aria-labelledby="h-story">
<div class="wrap story">
<div><span class="eyebrow">{e(t["story_eyebrow"])}</span><h2 id="h-story" style="margin-bottom:28px">{e(t["story_h2"]).replace("AVA-DAM", '<span style="white-space:nowrap">AVA-DAM</span>')}</h2>{story}<p class="big">{e(t["story_big"])}</p></div>
<div class="adam" aria-hidden="true"><div class="name">AVA<b>DAM</b></div><div class="say">{e(t["say"])}</div><div class="slogan">HUMAN <span>+ TECHNOLOGY.</span> TOGETHER.</div></div>
</div>
</section>

<section id="team" class="areas" aria-labelledby="h-team">
<div class="wrap">
<div class="head"><span class="eyebrow">{e(t["team_eyebrow"])}</span><h2 id="h-team">{e(t["team_h2"])}</h2></div>
<div class="about">{"".join(f"<p>{e(x)}</p>" for x in t["about"])}</div>
<div class="duo">
<div class="card person"><span class="mono" aria-hidden="true">AvA</span><h3>Adrian von Arb</h3></div>
<div class="card person"><span class="mono b" aria-hidden="true">DM</span><h3>Daniel Muccio</h3></div>
</div>
<div class="places">{places}</div>
</div>
</section>

<section id="faq" class="faq" aria-labelledby="h-faq">
<div class="wrap">
<div class="head"><span class="eyebrow">{e(t["faq_eyebrow"])}</span><h2 id="h-faq">{e(t["faq_h2"])}</h2></div>
<div class="faq-list">
<details><summary>{e(t["faq_q"])}</summary><p>{e(t["faq_a"])}</p></details>
</div>
<p class="note">{e(t["faq_note"])}</p>
</div>
</section>

<section id="kontakt" class="contact" aria-labelledby="h-contact">
<div class="wrap">
<div class="head"><span class="eyebrow">{e(t["contact_eyebrow"])}</span><h2 id="h-contact">{e(t["contact_h2"])}</h2><p class="lead" style="margin:18px auto 0">{e(t["contact_lead"])}</p></div>
<p class="mailbox">✉ {e(t["mail_soon"])}</p>
</div>
</section>
</main>

<footer>
<div class="wrap">
<span><img class="logo-light" src="{A}avadam-logo.svg" alt="AVA-DAM" width="668" height="126" loading="lazy"><img class="logo-dark" src="{A}avadam-logo-dark.svg" alt="" aria-hidden="true" width="668" height="126" loading="lazy"></span>
<span>{e(t["footer"])}</span>
{lang_links(lang, r, t["lang_label"])}
</div>
</footer>
<button type="button" class="totop" id="totop" aria-label="{e(t["top_label"])}" title="{e(t["top_label"])}">{TOTOP}</button>
<script>{JS}</script>
</body>
</html>
'''

def sitemap():
    urls = []
    for l in LANGS:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{a}" href="{url_of(a)}"/>' for a in LANGS)
        alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{url_of("de")}"/>'
        urls.append(f"<url><loc>{url_of(l)}</loc><lastmod>{TODAY}</lastmod>{alts}</url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")

def llms():
    t = T["en"]
    lines = [f"# AVA-DAM", "", f"> {t['desc']}", "",
             "AVA-DAM is the joint label of Adrian von Arb and Daniel Muccio. The name is pronounced like \"Adam\": "
             "a reminder of the first human being, where everything began, including the age of AI. "
             "Slogan: Human + Technology. Together.", "", "## About us", ""] + t["about"] + ["",
             "## What we do"] + [f"- {h}: {p}" for h, p in t["areas"]] + ["", "## Projects"] + \
            [f"- [{n}]({PROJECT_URLS[k]}): {d}" for k, n, _, d in t["projects"]] + \
            ["", "## Locations", "- Switzerland: 4632 Trimbach", "- United Kingdom: Grantown-on-Spey PH26 3JN, Scotland", "",
             "## Languages"] + [f"- [{LANG_NAMES[l]}]({url_of(l)})" for l in LANGS] + [""]
    return "\n".join(lines)

def main():
    for l in LANGS:
        d = os.path.join(OUT, path_of(l))
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(page(l))
    open(os.path.join(OUT, "sitemap.xml"), "w").write(sitemap())
    open(os.path.join(OUT, "llms.txt"), "w").write(llms())
    open(os.path.join(OUT, "robots.txt"), "w").write(
        "# Alle Suchmaschinen und KI-Crawler sind willkommen.\nUser-agent: *\nAllow: /\n\n"
        f"Sitemap: {BASE}sitemap.xml\n")
    print("gebaut:", ", ".join(LANGS))

if __name__ == "__main__":
    main()
