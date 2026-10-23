# AVADAM Webseite · Projektbeschreibung für Claude

Diese Datei lesen, bevor am Projekt gearbeitet wird. Sie gilt für alle, die hier mitarbeiten, Mensch oder Claude.

## Worum es geht

AVADAM ist die gemeinsame Marke von **Adrian von Arb** (Adi) und **Daniel Muccio** (Dani). Wir bauen Webseiten, Software und Tools, Motion-Videos und interaktive Karten. Die Ideen kommen von uns, umgesetzt wird mit KI.

Der Name setzt sich aus unseren Namen zusammen (**A**drian **v**on **A**rb, **D**aniel **M**uccio) und wird wie „Adam“ ausgesprochen. Adam steht für den ersten Menschen. Von dort hat alles angefangen, auch die Ära der KI. AVADAM soll daran erinnern, woher wir kommen. Slogan: **Human + Technology. Together.**

Standorte: Schweiz, 4632 Trimbach (eigene Seite: https://www.formateins.ch/). Grossbritannien, Grantown-on-Spey PH26 3JN (eigene Seite folgt). AVADAM ist das Dach für alles, die Seiten der Niederlassungen werden bei den Standorten verlinkt (`PLACE_URLS` in `_build/content.py`).

Diese Seite ist der erste Auftritt von AVADAM. Später kommen Tools und weitere Bereiche dazu.

- Vorschau: https://avadam26.github.io/avadam/
- Sprachen: Deutsch (Hauptordner), Englisch `/en/`, Italienisch `/it/`, Französisch `/fr/`

## Aufbau

```
_build/content.py   alle Texte in vier Sprachen  ← hier Texte ändern
_build/build.py     erzeugt die Seiten, Sitemap, robots.txt, llms.txt
assets/             style.css, Logos, Favicon, Schriften, Vorschaubild
media/              Videos, Posterbilder, Screenshots
index.html, en/, it/, fr/   werden erzeugt, nie von Hand bearbeiten
AUFGABEN.md         offene Punkte
LOGBUCH.md          was wann geändert wurde
_build/logbuch_seite.py   macht daraus die Leseseite fürs Artifact
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
- Name in Texten immer **AVADAM**: zusammen und alles gross, ohne Bindestrich. Gilt für alle Texte, Titel, Meta-Daten, Alt-Texte, Mails und Projektbeschreibungen. Nur im Logo verbindet der Strich das A mit dem D, das ist Gestaltung und kein Bindestrich. Nie „AVA-DAM“, „Ava-Dam“ oder „AvaDam“ schreiben.
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
- FAQ-Bereich „Was oft gefragt wird“ mit FAQPage-Schema. Fragen und Antworten in `faq_items` in `_build/content.py`, in allen vier Sprachen.
- Jedes Bild mit sinnvollem Alt-Text, Überschriften in logischer Reihenfolge.
- Bei eigener Domain nur `BASE` in `_build/build.py` anpassen und neu bauen.

**Referenzen.** Ziel sind 3 × 3 Referenzen: eine Zeile Webseiten, eine Zeile Software, eine Zeile Interaktive Karten, je bis zu drei. Reihenfolge in `PROJECT_ROWS` in `_build/content.py`.

**Kein Tracking, keine Cookies** ohne ausdrückliches Okay von Adi und Dani.

## Prüfen vor jedem Commit

- Seite lokal ansehen (`python3 -m http.server` im Projektordner).
- Breiten 320, 390, 768 und 1280 Pixel: nichts darf seitlich überstehen.
- Hell und dunkel ansehen, alle vier Sprachen.
- Keine Fehler in der Browser-Konsole.
- Eintrag im `LOGBUCH.md` geschrieben.

## Zusammenarbeit

- Vor dem Arbeiten immer zuerst den neusten Stand holen (`git pull`).
- Kurz absprechen, wer woran arbeitet. Nicht gleichzeitig an derselben Datei.
- Kleine, verständliche Commits mit deutscher Beschreibung.
- **Commits immer im Namen der Person, die gerade arbeitet**, nie nur als „claude“. Nur so erscheint sie auf GitHub bei den Contributors. Vor dem ersten Commit `git config user.name` und `git config user.email` im Repo entsprechend setzen. Ist unklar, wer arbeitet, kurz fragen.
  - Dani: `scotlandbydan` mit der Noreply-Adresse `317312833+dmuccios24-oss@users.noreply.github.com`, nie mit seiner Gmail-Adresse. Sonst blockt GitHub den Push.
  - Adi: `f5yct67kcv-source` mit der Noreply-Adresse `284693819+f5yct67kcv-source@users.noreply.github.com`, nicht mit seiner Apple-Relay-Adresse.
  - Gilt in allen Projekten.
- **Arbeit am Ende jeder Sitzung in `main` zurückführen.** Cloud-Sitzungen (claude.ai/code, Handy, Desktop „Cloud“) arbeiten auf einem eigenen Zweig `claude/…`. Bevor die Sitzung endet: `git pull origin main`, Konflikte lösen, dann in `main` übernehmen und hochladen. Sonst bleibt die Arbeit liegen und kommt nie auf die Live-Seite. Nur wenn Adi oder Dani ausdrücklich zuerst prüfen wollen, stattdessen einen Pull Request machen und Bescheid geben. Gilt in allen Projekten.
- Offene Punkte stehen in `AUFGABEN.md`. Erledigtes dort abhaken.
- Jede Änderung kommt ins `LOGBUCH.md`, zuoberst, mit Datum und wer es gemacht hat, die Kurznummer des Commits sobald sie bekannt ist. Auch kleine Änderungen. So sehen beide, was seit dem letzten Mal passiert ist, ohne die Git-Historie durchzugehen.
- Danach `python3 _build/logbuch_seite.py` laufen lassen und das Artifact neu veröffentlichen, damit Adi den neusten Stand sieht, auch ohne GitHub. Das Logbuch gehört nicht auf die öffentliche Webseite.
