# Logbuch · AVADAM Webseite

Hier steht, was wann an der Seite geändert wurde. Neuste Einträge zuoberst.

So führen wir es:

- Jede Änderung bekommt einen Eintrag, auch eine kleine. Lieber einen Satz zu viel als einen zu wenig.
- Pro Eintrag: was geändert wurde und wer es gemacht hat. Die Kurznummer des Commits dazuschreiben, sobald sie bekannt ist. Beim Eintrag, der mit der Änderung selbst mitkommt, steht sie noch nicht fest, dann bleibt sie weg oder wird nachgetragen.
- „Claude“ heisst, die Änderung ist in einer Claude-Sitzung entstanden, im Auftrag von Adi oder Dani.
- Geschrieben wird so, dass man es in einem halben Jahr noch versteht. Keine Abkürzungen, keine Fachbegriffe ohne Erklärung.
- Offene Punkte gehören nicht hierhin, die stehen in `AUFGABEN.md`.

## 8. November 2026

**„Neu“ bei den Interaktiven Spots entfernt** · Claude für Dani
Die Überschrift über den Spots heisst jetzt nur noch „Interaktive Spots“, ohne „Neu:“ davor. Wir bieten es an und fertig. In allen vier Sprachen geändert, geprüft hell und dunkel auf allen Breiten.

**Links ins FAQ, GuardOpS mit 27 Jahren** · Claude für Dani · `7f379f8`
Die Absätze zu CI und Social-Media-Management haben neu einen zweiten Link „Fragen dazu im FAQ“, der direkt zur passenden Frage springt und sie gleich aufklappt (`#faq-ci`, `#faq-social-media`). Dafür können Fragen in `faq_items` jetzt eine eigene ID haben, ein kleines Skript öffnet die Antwort beim Sprung. Ohne JavaScript landet man trotzdem bei der Frage. Beim Bereich Software und Tools stand, GuardOpS sei aus 22 Jahren Erfahrung entstanden. Richtig sind die gemeinsamen 27 Jahre von Adi und Dani, korrigiert in allen vier Sprachen. Geprüft in allen vier Sprachen, hell und dunkel, auf 320, 390, 768 und 1280 Pixel, ohne Fehler in der Konsole.

**CI und Social-Media-Management in den Bereichen, mit internen Links** · Claude für Dani · `2bdc6a3`
Keine eigene Sparte, sondern in die bestehenden Bereiche eingebaut, in allen vier Sprachen. Bei Webseiten steht neu ein Absatz zum kompletten CI (Logo, Farben, Schriften, Visitenkarten, Logo für Arbeitskleidung, Banner für die Social-Media-Kanäle), Anker `#ci`. Bei Motion-Videos ein Absatz zum Social-Media-Management, Anker `#social-media`. Die beiden Absätze verlinken sich gegenseitig, dazu ein kurzer Satz mit Link bei den Interaktiven Karten. Springt man auf einen Anker, leuchtet der Absatz kurz auf. Im FAQ zwei neue Fragen zu CI und Social Media. Technisch können die Bereiche in `_build/content.py` jetzt optional Zusatzabsätze mit Anker und Link haben (`extra` in `_build/build.py`), Stil in `assets/style.css`. Auch `llms.txt` nimmt die neuen Texte mit. Geprüft in allen vier Sprachen, hell und dunkel, auf 320, 390, 768 und 1280 Pixel, ohne Fehler in der Konsole.

## 7. November 2026

**Neuer Bereich „Interaktive Spots“ auf der Webseite, zweites Beispiel umbenannt** · Claude für Dani · `07cf81b`
Auf der Startseite gibt es nach den Motion-Videos einen neuen Abschnitt „Neu: Interaktive Spots“ (`#spots`) in allen vier Sprachen. Zwei Karten mit Vorschaubild und Link zum Ausprobieren: „Der Spot“ für neue Kunden und „Der Spot mit Termin“ für die Webseite eines Kunden. Dazu eine neue FAQ-Frage „Was ist ein interaktiver Spot?“. Texte in `_build/content.py` (`spots_…` und `faq_items`), Vorlage in `_build/build.py`, Stil in `assets/style.css`, Bilder `media/spot-1.jpg` und `media/spot-2.jpg`. Das zweite Beispiel heisst neu „Muster Kosmetik“ mit Sarah statt makellos und Dayana und liegt unter `spot/kosmetik/`. Alle echten Angaben (Name, Telefon, Mail, WhatsApp, Hinweise auf die offizielle Seite) sind raus, Adresse und Nummer sind erfunden.

**Zweites Beispiel: Spot mit Task für makellos Naturkosmetik** · Claude für Dani · `87de340`
Neue Seite `spot/makellos/`, ein Entwurf für die Webseite von Dayana Probst (makellos Naturkosmetik), mit Angebot, Über mich, Terminbuchung und Kontakt. Alle Angaben zu Behandlungen, Preisen, Öffnungszeiten und Kontakt stammen von makellos-naturkosmetik.ch. Mittendrin Dayanas Spot: sie stellt sich vor und stellt vier Fragen (Thema, je nach Thema eine eigene zweite Frage, Pflege heute, allein oder zu zweit). Danach gibt es eine Auswertung mit passender Behandlung, Dauer, Preis und Hinweisen, die man drucken, als PDF oder als Bild aufs Handy speichern kann. Am Schluss wählt man zwischen online buchen (Behandlung ist schon vorausgewählt, Zeiten richten sich nach den Öffnungszeiten), Rückruf oder vorbeikommen. Formulare verschicken nichts. Die Studio-Adresse fehlt noch, auf ihrer Seite steht einmal Olten und einmal Hünenberg (`ADDR` im Skript). Dayana ist gezeichnet, keine Fotos von ihrer Seite übernommen. DE, EN, IT, hell/dunkel, Klappmenü, Back-to-Top mit Nagellack oder Pipettenfläschchen. Vom ersten Spot aus oben verlinkt.

**Spot: Musik von Rocco drin, lebendigere Stimme, Sprecher-Skript** · Claude für Dani · `b30175b`
„Welcoming Morning“ von Rocco Brandonisio liegt als `media/spot-musik.mp3` im Repo (auf 128 kbit/s verkleinert, mit kurzem Ein- und Ausblenden für die Schleife) und läuft jetzt hörbar unter dem Spot, unter der Stimme etwas leiser. Die Browser-Stimme nimmt neu die natürlichste Stimme, die das Gerät hat, spricht Satz für Satz und je nach Moment schneller, langsamer, höher oder tiefer. Zwei Sätze enden neu mit Ausrufezeichen („Das wollen wir ändern!“, „Danke dir!“), in allen drei Sprachen. Für echte Gefühle ist aber eine Aufnahme nötig, darum kann der Spot jetzt eigene Sprachdateien abspielen. Das Skript mit Dateinamen und Audio Tags für ElevenLabs steht in `spot/STIMME.md`.

**Spot: Social Media, CI aus einer Hand, Musik vorbereitet** · Claude für Dani · `d4d3981`
Neue Frage 2 „Und Social Media? Soll sich jemand darum kümmern?“ mit eigener Szene, wenn man Ja sagt. Damit sind es jetzt vier Fragen, die Antwort steht auch in der Anfrage. Beim CI heisst es neu, dass von der Webseite über das Logo bis zur Visitenkarte alles aus einer Hand kommt. Dazu ein Musik-Player, der leise unter der Stimme läuft und am Schluss ausblendet, mit eigenem Knopf zum Abschalten und „Musik: Rocco Brandonisio“ im Fuss. Er sucht `media/spot-musik.mp3`. Solange die Datei fehlt, bleiben Knopf und Hinweis unsichtbar. Alles in DE, EN und IT.

**Entwurf „Interaktiver Spot“ unter `/spot/`** · Claude für Dani · `68ce569`
Ein klickbarer Prototyp, damit Adi sieht, was Dani im Kopf hat. Die Idee ist von SPOT/TASK (Spot Interattivo) abgeschaut: ein kurzer Film, der unterwegs Fragen stellt, und darunter eine Seite mit passenden Referenzen und einem Anfrageformular. Am Beispiel eines Massagestudios („Studio Lena“, erfunden). Die erste Frage hat Dani vorgegeben (Erklärvideo, Webseite, Webseite und CI, kompletter Auftritt), dazu zwei weitere (wo stehst du heute, wann soll's losgehen). Je nach Antwort kommt eine andere Szene und andere Referenzen. Die Szenen sind gezeichnete, animierte Bilder, die Stimme kommt vorerst aus dem Browser, im fertigen Spot käme eine echte Sprecherstimme. Sprachen Deutsch, Englisch, Italienisch, im Spot umschaltbar. Das Formular verschickt nichts, es zeigt nur, wie die Anfrage samt Antworten bei uns ankäme. Die Seite ist `noindex`, nirgends verlinkt und steht nicht in der Sitemap. Hell/Dunkel und Back-to-Top wie auf der Hauptseite. Alles in einer Datei, `spot/index.html`.

## 31. Oktober 2026

**Interaktive Karte jetzt auf Englisch, Sprachhinweis bei den Videos** · Claude für Dani
Das Video zur interaktiven Karte ist jetzt die englische Fassung (gesprochen und Schrift auf Englisch), auf allen vier Sprachseiten. `media/karte.mp4` und das Posterbild `media/karte-poster.jpg` ersetzt, die deutsche Fassung liegt bei Dani auf der externen Platte. Unter „Highlands“ und der Karte steht neu ein kleiner Hinweis, in welcher Sprache gesprochen wird und dass es die andere Sprache auch gibt, in allen vier Sprachen (`video_notes` in `_build/content.py`, Stil `.reel figcaption .note`).

## 30. Oktober 2026

**Drittes Motion-Video „That's it from us“** · Claude für Dani · `1aaf1c8`
Neues Video zum Saisonende 2026 für das Garden Park Guest House, mit echten Fotos und Videos aus dem Haus (49 Sekunden, mit Ton). Steht als drittes Video neben „Highlands“ und der interaktiven Karte, in allen vier Sprachen. Der Einleitungstext sagt jetzt „Drei Beispiele“ statt „Zwei“. Video für die Webseite verkleinert auf 720 × 1280 (`media/saisonende.mp4`), Posterbild aus der ersten Szene (`media/saisonende-poster.jpg`).

## 23. Oktober 2026

**Neues Demo-Video für „Mein Tag“** · Claude für Dani
`media/meintag.mp4` ersetzt durch das neue Demo-Video (1:49) mit Danis Stimme und Rocco's Musik. Neu mit der Mail-Szene (Termin aus dem Büro per Mail) und dem Fussballer, der den Ball nach oben kickt. Ohne Untertitel.

**Neue Referenz „Mein Tag“ neben GuardOpS** · Claude für Dani · `af4329d`
Danis persönlicher Tagesplaner mit KI steht jetzt in der Zeile Software und Tools, gleich neben GuardOpS. Kategorie „Web-Software“ (englisch „Web tool“, italienisch „Strumento web“, französisch „Outil web“), Text in allen vier Sprachen. Das Bild ist das Schlussbild aus dem Demo-Video (`media/meintag.jpg`). „Ansehen“ öffnet das Demo-Video mit Musik (`media/meintag.mp4`), weil der Planer selbst privat ist.

**„Software“ heisst jetzt überall „Software und Tools“** · Claude für Dani · `1fbc55b`
Im Seitentitel, in der Beschreibung für Google, in der Zeile über der grossen Überschrift und im Einleitungstext steht jetzt „Software und Tools“ statt nur „Software“, in allen vier Sprachen (Software and tools, Software e strumenti, Logiciels et outils). So passen auch kleine Werkzeuge wie der Tagesplaner „Mein Tag“ dazu. Bei GuardOpS bleibt „Software“, das ist eine.

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
