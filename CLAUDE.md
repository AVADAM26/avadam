# AVA-DAM Webseite · Projektbeschreibung für Claude

Diese Datei lesen, bevor am Projekt gearbeitet wird. Sie gilt für alle, die hier mitarbeiten, Mensch oder Claude.

## Worum es geht

AVA-DAM ist die gemeinsame Marke von **Adrian von Arb** (Adi) und **Daniel Muccio** (Dani). Wir bauen Webseiten, Software und Tools, Motion-Videos und interaktive Karten. Die Ideen kommen von uns, umgesetzt wird mit KI.

Der Name setzt sich aus unseren Namen zusammen (**A**drian **v**on **A**rb, **D**aniel **M**uccio) und wird wie „Adam“ ausgesprochen. Adam steht für den ersten Menschen. Von dort hat alles angefangen, auch die Ära der KI. AVA-DAM soll daran erinnern, woher wir kommen. Slogan: **Human + Technology. Together.**

Standorte: Schweiz, 4632 Trimbach. Grossbritannien, Grantown-on-Spey PH26 3JN.

Diese Seite ist der erste Auftritt von AVA-DAM. Später kommen Tools und weitere Bereiche dazu.

- Vorschau: https://dmuccios24-oss.github.io/avadam/
- Sprachen: Deutsch (Hauptordner), Englisch `/en/`, Italienisch `/it/`, Französisch `/fr/`

## Aufbau

```
_build/content.py   alle Texte in vier Sprachen  ← hier Texte ändern
_build/build.py     erzeugt die Seiten, Sitemap, robots.txt, llms.txt
assets/             style.css, Logos, Favicon, Schriften, Vorschaubild
media/              Videos, Posterbilder, Screenshots
index.html, en/, it/, fr/   werden erzeugt, nie von Hand bearbeiten
AUFGABEN.md         offene Punkte
```

Nach jeder Änderung an Texten oder an `build.py` im Projektordner ausführen:

```
python3 _build/build.py
```

Die erzeugten HTML-Dateien werden mit committed, weil GitHub Pages sie direkt ausliefert.

## Regeln, die immer gelten

**Vier Sprachen.** Jede inhaltliche Änderung in allen vier Sprachen nachziehen. Keine Sprache vergessen.

**Nichts erfinden.** Keine Zahlen, Kunden, Zitate, Auszeichnungen oder Fakten, die Adi oder Dani nicht genannt haben. Fehlt etwas, Platzhalter setzen und nachfragen.

**Schreibstil.** Schweizer Schreibweise, immer „ss“, nie „ß“. Direkt, unkompliziert, freundlich, persönlich, eher gesprochen als akademisch. Kein Marketing-Deutsch, keine Superlative, keine KI-Floskeln. Wenige Gedankenstriche und Doppelpunkte, lieber Fliesstext als Aufzählungen. Englisch: britisch, natürlich, nicht steif. „Guest/Guests“ wird im Englischen bewusst gross geschrieben.

**Corporate Identity.** Nicht verändern ohne Absprache.
- Dunkelblau `#101B35`, Blau `#3C82D9`, Weiss
- Schrift Montserrat, lokal eingebunden unter `assets/fonts/` (kein Google-Fonts-Link, wegen Datenschutz)
- Logo nur aus den Dateien verwenden: `assets/avadam-logo.svg` (hell) und `assets/avadam-logo-dark.svg` (dunkel). Die Wortmarke ist gezeichnet und keine Schrift, nie abtippen oder nachbauen.

**Pflicht auf jeder unserer Webseiten**
- Hell/Dunkel-Modus: richtet sich zuerst nach dem Gerät, der Schalter merkt sich die Wahl.
- Back-to-Top-Button als Daniels Markenzeichen. Hier drei Motive, die bei jedem Laden zufällig wechseln: Apfel (Human, Adams Apfel), Roboter (Technology), Stecker wie im Logo (Together). Jedes hat eine kleine Animation vor dem Hochfliegen.
- Auf dem Handy ein Klappmenü.

**SEO und KI-Tauglichkeit**
- Aller Inhalt steht direkt im HTML, lesbar ohne JavaScript.
- Pro Sprache eine eigene Seite mit `hreflang`, `canonical`, Meta-Beschreibung, Open-Graph-Daten.
- Strukturierte Daten (JSON-LD) für Organisation, Webseite, Projekte und Videos.
- `sitemap.xml`, `robots.txt` (alle Crawler erlaubt) und `llms.txt` werden vom Build erzeugt.
- FAQ-Bereich ist vorbereitet. Das FAQPage-Schema erst einfügen, wenn echte Fragen und Antworten feststehen.
- Jedes Bild mit sinnvollem Alt-Text, Überschriften in logischer Reihenfolge.
- Bei eigener Domain nur `BASE` in `_build/build.py` anpassen und neu bauen.

**Kein Tracking, keine Cookies** ohne ausdrückliches Okay von Adi und Dani.

## Prüfen vor jedem Commit

- Seite lokal ansehen (`python3 -m http.server` im Projektordner).
- Breiten 320, 390, 768 und 1280 Pixel: nichts darf seitlich überstehen.
- Hell und dunkel ansehen, alle vier Sprachen.
- Keine Fehler in der Browser-Konsole.

## Zusammenarbeit

- Vor dem Arbeiten immer zuerst den neusten Stand holen (`git pull`).
- Kurz absprechen, wer woran arbeitet. Nicht gleichzeitig an derselben Datei.
- Kleine, verständliche Commits mit deutscher Beschreibung.
- Offene Punkte stehen in `AUFGABEN.md`. Erledigtes dort abhaken.
