# Logbuch · AVADAM Webseite

Hier steht, was wann an der Seite geändert wurde. Neuste Einträge zuoberst.

So führen wir es:

- Jede Änderung bekommt einen Eintrag, auch eine kleine. Lieber einen Satz zu viel als einen zu wenig.
- Pro Eintrag: was geändert wurde und wer es gemacht hat. Die Kurznummer des Commits dazuschreiben, sobald sie bekannt ist. Beim Eintrag, der mit der Änderung selbst mitkommt, steht sie noch nicht fest, dann bleibt sie weg oder wird nachgetragen.
- „Claude“ heisst, die Änderung ist in einer Claude-Sitzung entstanden, im Auftrag von Adi oder Dani.
- Geschrieben wird so, dass man es in einem halben Jahr noch versteht. Keine Abkürzungen, keine Fachbegriffe ohne Erklärung.
- Offene Punkte gehören nicht hierhin, die stehen in `AUFGABEN.md`.

## 23. Oktober 2026

**Arbeit aus Cloud-Sitzungen kommt immer in main** · Claude für Dani
Neue Regel in `CLAUDE.md`. Sitzungen in der Cloud arbeiten auf einem eigenen Zweig `claude/…`. Am Ende jeder Sitzung wird die Arbeit jetzt in `main` übernommen, sonst kommt sie nie auf die Live-Seite. Bei der Gelegenheit Adis Zweig vom 22. Oktober (Logbuch, Leseseite, Videorahmen) in `main` übernommen. Die Korrektur der Videorahmen war in `main` schon drin, dort gilt die neuere Fassung.

**Adis GitHub-Konto für Commits eingetragen** · Claude für Dani · `c6a3b14`
In `CLAUDE.md` steht jetzt, mit welchem Namen und welcher Adresse Adis Commits laufen, damit auch er auf GitHub bei den Contributors erscheint.

**Commits im Namen der Person, die arbeitet** · Claude für Dani · `15a9bdf`
Bisher liefen alle Commits nur als „claude“, darum waren weder Adi noch Dani bei den Contributors sichtbar. Neu in `CLAUDE.md`: Commits immer mit dem GitHub-Konto von Adi oder Dani.

## 22. Oktober 2026

**Seite neu veröffentlicht** · Claude für Dani · `d1e23c4`
Leerer Commit, damit GitHub Pages die Seite sicher neu ausliefert.

**Link zu formateins.ch bei der Schweizer Niederlassung** · Claude für Dani · `941c0f3`
Bei der Adresse in der Schweiz verweist jetzt ein Link auf formateins.ch, in allen vier Sprachen.

**FAQ: drei Fragen zu KI und Datenschutz** · Claude für Dani · `946533a`
Drei weitere Fragen im FAQ, wie wir mit KI arbeiten und was mit Daten passiert, in allen vier Sprachen.

**FAQ „Was oft gefragt wird“** · Claude für Dani · `6423c2c`, `dae5b92`
Der vorbereitete FAQ-Bereich ist jetzt gefüllt, in allen vier Sprachen, mit FAQPage-Schema für die Suchmaschinen. Der Punkt ist in `AUFGABEN.md` abgehakt.

**Referenzen in Zeilen zu je drei** · Claude für Dani · `d75d1d2`
Die Referenzen stehen jetzt in drei Zeilen: Webseiten, Software, Interaktive Karten, je bis zu drei.

**Referenz Adrian von Arb Films** · Claude für Dani · `fef5d6f`
Adis Filmseite neu als Referenz, in allen Sprachen.

**Name überall AVADAM** · Claude für Dani · `cf6b425`
In allen Texten heisst es jetzt einheitlich AVADAM, ohne Bindestrich. Die Regel dazu steht in `CLAUDE.md`.

**Geschichte breiter, neues Vorschaubild Highlands** · Claude für Dani · `ddf0a9c`
Der Abschnitt zur Geschichte des Namens kommt ohne grosses Logo aus und ist breiter. Dazu ein neues Vorschaubild fürs Highlands-Video.

**Kartenvideo Version 3** · Claude für Dani · `4fe81fc`
Neues Video zur Grantown-Karte mit korrigierten Untertiteln, dazu das Foto vom Cottage und bessere Darstellung der Videos auf dem Handy.

**Adressen nach dem Umzug in die Organisation AVADAM26** · Claude für Dani · `b0e117a`, `ef60100`
Die Seite und das VKU-Projekt liegen neu bei der GitHub-Organisation AVADAM26. Alle Adressen, `sitemap.xml`, `robots.txt` und `llms.txt` angepasst.

**Logbuch als Leseseite für Adi** · Claude
Neu macht `_build/logbuch_seite.py` aus dieser Datei eine Seite, die man einfach anklicken und lesen kann, damit Adi den Verlauf auch ohne GitHub-Zugang sieht. Farben, Schrift und Logo kommen aus `assets/style.css`, also nichts doppelt gepflegt. Hell/Dunkel-Schalter und Back-to-Top sind drin, wie auf der Webseite. Die Seite liegt bewusst nicht auf der öffentlichen Webseite, sondern als Artifact zum Teilen. Nach jeder Änderung am Logbuch den Generator laufen lassen und das Artifact neu veröffentlichen.

**Motion-Videos waren zu hoch, korrigiert** · Claude
Die beiden Videorahmen im Motion-Bereich waren gut doppelt so hoch wie gedacht, 320 auf 1280 Pixel statt 320 auf 569. Grund war die Höhenangabe im HTML der Videos, die sich gegen das Seitenverhältnis aus dem CSS durchgesetzt hat. Dadurch wurden die Posterbilder stark beschnitten, auf dem ersten Video fehlte der obere Teil, auf dem zweiten war die Schrift angeschnitten. Mit `height:auto` in `assets/style.css` stimmen die Rahmen wieder und sehen aus wie zwei Handys nebeneinander. Geprüft in allen vier Sprachen, hell und dunkel, auf 320, 390, 768 und 1280 Pixel Breite. Die Bilder auf der Seite waren nicht betroffen.

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
