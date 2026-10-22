# Logbuch · AVA-DAM Webseite

Hier steht, was wann an der Seite geändert wurde. Neuste Einträge zuoberst.

So führen wir es:

- Jede Änderung bekommt einen Eintrag, auch eine kleine. Lieber einen Satz zu viel als einen zu wenig.
- Pro Eintrag: was geändert wurde und wer es gemacht hat. Die Kurznummer des Commits dazuschreiben, sobald sie bekannt ist. Beim Eintrag, der mit der Änderung selbst mitkommt, steht sie noch nicht fest, dann bleibt sie weg oder wird nachgetragen.
- „Claude“ heisst, die Änderung ist in einer Claude-Sitzung entstanden, im Auftrag von Adi oder Dani.
- Geschrieben wird so, dass man es in einem halben Jahr noch versteht. Keine Abkürzungen, keine Fachbegriffe ohne Erklärung.
- Offene Punkte gehören nicht hierhin, die stehen in `AUFGABEN.md`.

## 22. Oktober 2026

**Logbuch angelegt** · Claude
Diese Datei. Rückwirkend gefüllt mit allem, was seit dem Start passiert ist, damit Adi und Dani den Verlauf an einem Ort lesen können, ohne die Git-Historie durchzugehen. Die Regel dazu steht neu in `CLAUDE.md`, ein Hinweis darauf im `README.md`.

**Datum in den offenen Aufgaben korrigiert** · Claude · `4d85e66`
Kleine Korrektur in `AUFGABEN.md`, das Stand-Datum stimmte nicht.

**Abschnitt „Zu uns zwei“ in allen vier Sprachen** · Claude · `817ab64`
Neuer Abschnitt über Adi und Dani, mit Erfahrung aus HR, Marketing, Verkauf, Sicherheit und Geschäftsführung, dazu Adis Fotografie und Danis Betriebe in Schottland. Text in `_build/content.py` auf Deutsch, Englisch, Italienisch und Französisch, dazu etwas CSS für die beiden Namenskarten. Der Punkt ist in `AUFGABEN.md` abgehakt.

## 21. Oktober 2026

**Projektbeschreibung und Liste der offenen Aufgaben** · Claude · `41457d5`
`CLAUDE.md` mit allem, was man über das Projekt wissen muss, bevor man daran arbeitet: Aufbau, Regeln, Corporate Identity, Schreibstil, was vor jedem Commit geprüft wird. Dazu `AUFGABEN.md` mit dem, was noch offen ist, getrennt nach „von Adi und Dani“ und „von Claude“.

**Klappmenü auf dem Handy** · Claude · `ca5d6d6`
Auf schmalen Bildschirmen klappt die Navigation jetzt auf und zu, statt gedrängt in einer Zeile zu stehen.

**Hell/Dunkel-Modus, Back-to-Top-Knopf, Ton in den Videos** · Claude · `f881ac1`
Die Seite richtet sich zuerst nach der Einstellung des Geräts, der Schalter oben rechts merkt sich danach die eigene Wahl. Der Back-to-Top-Knopf zeigt bei jedem Laden zufällig eines von drei Motiven, Apfel für Human, Roboter für Technology und Stecker wie im Logo für Together, jedes mit einer kleinen Animation, bevor es hochfliegt. Die beiden Motion-Videos laufen neu mit Ton. Dazu kam das helle Logo für den Dunkelmodus (`assets/avadam-logo-dark.svg`).

**Erste Version der Seite in vier Sprachen** · Claude · `d218bf8`
Der Start. Eine Startseite auf Deutsch, Englisch, Italienisch und Französisch, erzeugt aus `_build/content.py` und `_build/build.py`. Mit Hero, den vier Bereichen, den vier Projekten (VKU Oberbaselbiet, Butterfly Cottage, Grantown-Karte, GuardOpS), den zwei Motion-Videos, der Geschichte zum Namen, einem vorbereiteten FAQ-Bereich und dem Kontaktteil. Dazu die Grundlagen fürs Gefundenwerden: `hreflang`, `canonical`, Meta-Beschreibungen, Open-Graph-Daten, strukturierte Daten, `sitemap.xml`, `robots.txt` und `llms.txt`. Schriften liegen lokal unter `assets/fonts/`, kein Google-Fonts-Link, kein Tracking, keine Cookies.
