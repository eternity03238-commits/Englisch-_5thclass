# Bildauftrag Units 2–4

Möwenflug, Englisch Klasse 5 · Stand 22.11.2026 · maschinenlesbar: [`units-2-4.json`](units-2-4.json)

> **Neuer Auftrag:** [Admiralsmöwe](admiralsmoewe.md): neue Wachstumsstufe von Friedrich (13 Figurenbilder, offen).

Für Units 2–4 sind **57 neue Bilder** im Beta-Branch geliefert. Diese Datei sagt für jedes Bild, was darauf zu sehen ist, in welchem Format es geliefert wird, wohin die Datei kommt und welcher Manifest-Eintrag dazugehört. Wiederverwendete Bilder stehen unten und müssen nicht neu gestaltet werden.

## So wird der Auftrag abgearbeitet

1. Aufgaben nach prioritaet (1 = Unit 2 zuerst) abarbeiten, innerhalb einer Unit: Außenszene, dann Belohnungs-Ansicht derselben Szene, dann Lernraum.
2. Dateien auf den Branch beta/friedrich-2-assets legen, Manifest ergänzen, "version" erhöhen.
3. In dieser Datei bei erledigten Aufgaben status auf "geliefert" setzen.
4. Katharina gibt die Bilder frei und schickt Claude den commitgenauen Manifest-Link; erst dann baut die App sie ein.

## Stil für alle Bilder

Warme, sonnige 3D-Illustration im Stil eines Animationsfilms, wie die vorhandenen Hafenstadt-Szenen (beta/assets/world/hafenstadt/). Weiches goldenes Nachmittagslicht, englische Küstenstadt Brighton/Sussex, Kreidefelsen, Meer und Leuchtturm dürfen im Hintergrund auftauchen. Materialien: Backstein, Sandstein, Holzplanken, Kopfsteinpflaster, Rosen und Lavendel. Farben: Creme, Petrol, Koralle, Himmelblau, warmes Holz.

**Nie im Bild:**
- keine Menschen und keine Tiere als Hauptfigur (die Möwe Friedrich wird von der App eingesetzt)
- keine Schrift, keine Buchstaben, keine Zahlen außer Zifferblättern ohne Ziffern-Text
- keine Namen, Logos oder echten Markenzeichen
- kein Rahmen, keine Vignette

| Art | Vorgaben |
| --- | --- |
| Außenszene | Hochformat 941 × 1672 px (Verhältnis 0,5628). Kamera auf Augenhöhe einer Möwe am Boden. Unteres Drittel: freie, begehbare Bodenfläche (Pflaster, Planken oder Weg) ohne Gegenstände, dort steht später Friedrich (ca. 30–60 % der Breite, Füße bei ca. 79 % der Höhe). In der Bildmitte (ca. 35–60 % der Höhe) ein klar erkennbarer Eingang (Tür, Tor, Theke), den die App zum Leuchten bringt. |
| Belohnungs-Ansicht | GENAU derselbe Bildausschnitt, dieselbe Kamera und dieselben Formen wie die Außenszene, pixelgenau deckungsgleich. Nur Licht und kleine festliche Details ändern sich (die App blendet weich über). |
| Lernraum | Innenansicht hinter der Tür, Hochformat 941 × 1672 px. Obere Hälfte zeigt den Raum mit den Gegenständen des Themas, untere Hälfte eine ruhige freie Fläche (Boden, Tisch oder Theke), auf der die App Karteikarten anzeigt. Keine Schrift auf Tafeln oder Plakaten. |
| Übersichtskarte | Hochformat 941 × 1672 px, schräge Vogelperspektive wie hafenstadt/lernwelt-uebersicht.webp. Die sechs Lernorte als klar getrennte, wiedererkennbare Gebäude oder Plätze, jeweils mit etwas Freiraum darüber für einen Ortspin der App. Keine Beschriftung. |
| Kleidungsstück | Für den Kleiderschrank: 512 × 512 px, freigestellt mit echtem Alphakanal, Vorderansicht, mittig, wie rewards/sun.webp oder rewards/captain.webp. Weiche 3D-Optik passend zu Friedrich. |

**Dateien:** Je Bild: Original-PNG nach art-source/…, für die App WebP in voller Größe plus kleine Variante (Szenen: -640.webp mit 640 × 1137 px; Kleidungsstücke: -128.webp mit 128 × 128 px). Danach die Einträge im passenden Manifest ergänzen und dessen "version" um 1 erhöhen.

**Manifest-Einträge (Beispiel Außenszene):**

```json
"varndean-schultor": {
  "learningArea": "u2_weg",
  "backgrounds": [
    {"path": "varndean/varndean-schultor.webp", "width": 941, "height": 1672},
    {"path": "varndean/varndean-schultor-640.webp", "width": 640, "height": 1137}
  ],
  "rewardBackgrounds": [
    {"path": "varndean/varndean-schultor-licht.webp", "width": 941, "height": 1672},
    {"path": "varndean/varndean-schultor-licht-640.webp", "width": 640, "height": 1137}
  ]
}
```

Der Lernraum bekommt einen eigenen Eintrag (`varndean-schultor-innen`) mit derselben `learningArea`. Kleidungsstücke kommen nach `outfits` im Belohnungs-Manifest, Muster: `"sun": {"name": "Sonnenbrille", "slot": "eyes", "images": [...]}`.

## Regionen und Lernorte

### Unit 2: A new week at Varndean · Region „Die Varndean School“

Ordner: `beta/assets/world/varndean/` · Übersichtskarte: `varndean-uebersicht`

| Lernort (App-ID) | Außenszene | Lernraum | Wörter, die im Bild vorkommen sollen |
| --- | --- | --- | --- |
| Schultor & Schulweg (`u2_weg`) | `varndean-schultor` | `varndean-schultor-innen` | get up, walk, early, always, far, near, bring, be in a hurry, Off we go! |
| Uhrturm (`u2_uhr`) | `varndean-uhrturm` | `varndean-uhrturm-innen` | o'clock, half past, quarter past, quarter to, midday, midnight, minute |
| Klassenzimmer (`u2_klasse`) | `varndean-klassenfluegel` | `schule-am-meer-klassenzimmer` | maths, science, French, history, geography, art, music, timetable, homework, put your hand up |
| Kantine & Schulhof (`u2_kantine`) | `varndean-kantine` | `varndean-kantine-innen` | lunch, break, canteen, playground, food, apple, salad, ice cream, cook |
| Aula, Turnhalle & Bibliothek (`u2_aula`) | `varndean-aula` | `varndean-aula-innen` | assembly hall, gym, PE, library, drama, theatre, concert, dancer, music |
| Kalender-Garten (`u2_kalender`) | `varndean-kalender` | `varndean-kalender-innen` | January, February, spring, summer, autumn, winter, date, term, holidays, weekend |

### Unit 3: In our free time · Region „Clubs, Markt & Backstube“

Ordner: `beta/assets/world/freizeit/` · Übersichtskarte: `freizeit-uebersicht`

| Lernort (App-ID) | Außenszene | Lernraum | Wörter, die im Bild vorkommen sollen |
| --- | --- | --- | --- |
| Clubhaus (`u3_club`) | `freizeit-clubhaus` | `freizeit-clubhaus-innen` | club, join, member, chess, orchestra, choir, instrument, practise, be bored |
| Sportplatz (`u3_sport`) | `freizeit-sportplatz` | `freizeit-sportplatz-innen` | race, runner, cycle, medal, win, lose, winner, cheer, train, Good luck! |
| Gefühle-Brücke (`u3_gefuehle`) | `freizeit-gefuehle` | `freizeit-gefuehle-innen` | happy, sad, angry, nervous, excited, bored, unhappy, agree, hate, No way!, Oh dear! |
| Markt & Obststand (`u3_markt`) | `marktplatz` | `marktplatz-obststand` | shop, money, list, trolley, fruit, vegetables, strawberry, pineapple, carrot, tomato, juice, crisps, enough |
| Backstube (`u3_back`) | `freizeit-backstube` | `freizeit-backstube-innen` | recipe, ingredient, flour, sugar, butter, egg, chocolate, oven, fridge, bake, cut, scone |
| Geburtstags-Picknick (`u3_party`) | `freizeit-picknick` | `freizeit-picknick-innen` | birthday, invitation, present, cake, picnic, biscuit, sweet, Would you like…? |

### Unit 4: Out and about in Brighton · Region „Unterwegs in Brighton“

Ordner: `beta/assets/world/stadt/` · Übersichtskarte: `stadt-uebersicht`

| Lernort (App-ID) | Außenszene | Lernraum | Wörter, die im Bild vorkommen sollen |
| --- | --- | --- | --- |
| Aussichtspunkt (`u4_aussicht`) | `stadt-aussicht` | `stadt-aussicht-innen` | sight, famous, work of art, view, visitor, bench, beautiful, magical |
| Wetter-Promenade (`u4_wetter`) | `stadt-wetter` | `stadt-wetter-innen` | weather, sunny, cloudy, windy, rainy, stormy, snowy, rain, snow |
| Post & Läden (`u4_laeden`) | `stadt-laeden` | `stadt-laeden-innen` | post box, post office, bakery, customer, cost, pound, expensive, sell, opposite, pavement |
| Kino & Fahrgeschäfte (`u4_kino`) | `stadt-kino` | `stadt-kino-innen` | cinema, ride, light, decide, suggest, expensive, exciting |
| Bild-Werkstatt (`u4_bild`) | `stadt-bildwerkstatt` | `stadt-bildwerkstatt-innen` | description, title, caption, foreground, middle, on the left, on the right, at the top, at the bottom |
| Buddys Rettung & Zuhause (`u4_buddy`) | `stadt-buddy` | `stadt-buddy-innen` | rescue, police, key, locked, hide, follow, brave, worried, tidy, wash the dishes, dry, tooth |

## Bilder und Lieferstatus

Reihenfolge = Priorität. Unit 2 zuerst, damit die Region beim Freischalten vollständig ist.

### Priorität 1: Unit 2: A new week at Varndean

| Status | ID | Art | Motiv | Dateien |
| --- | --- | --- | --- | --- |
| geliefert | `varndean-uebersicht` | Übersichtskarte | Ein Schulgelände an der Küste: Hauptgebäude mit Uhrturm, Klassenzimmer-Flügel, Kantine mit Terrasse, Aula mit Turnhalle und Bibliothek, Garten mit Jahreszeiten-Beeten, Schultor mit Weg. Meer und Kreidefelsen am Rand. | `art-source/world/varndean/varndean-uebersicht.png`<br>`beta/assets/world/varndean/varndean-uebersicht.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-uebersicht-640.webp (640×1137)` |

### Priorität 2: Unit 3: In our free time

| Status | ID | Art | Motiv | Dateien |
| --- | --- | --- | --- | --- |
| geliefert | `freizeit-uebersicht` | Übersichtskarte | Ein Freizeitviertel: Clubhaus, Sportplatz mit Laufbahn, Brücke über einen Bach, der vorhandene Marktplatz mit Obststand, Backstube mit Schornstein, Picknickwiese. Alles mit Wegen verbunden. | `art-source/world/freizeit/freizeit-uebersicht.png`<br>`beta/assets/world/freizeit/freizeit-uebersicht.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-uebersicht-640.webp (640×1137)` |

### Priorität 3: Unit 4: Out and about in Brighton

| Status | ID | Art | Motiv | Dateien |
| --- | --- | --- | --- | --- |
| geliefert | `stadt-uebersicht` | Übersichtskarte | Brighton-Stadt am Meer: Aussichtspunkt mit Bank über dem Pier, Strandpromenade mit Wetterstation, Straße mit Postamt, rotem Briefkasten und Bäckerei, Kino mit Karussell, Atelier, Gasse mit Hundehütte. Erkennbar britisch, aber ohne echte Wahrzeichen-Schrift. | `art-source/world/stadt/stadt-uebersicht.png`<br>`beta/assets/world/stadt/stadt-uebersicht.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-uebersicht-640.webp (640×1137)` |

### Priorität 1: Unit 2: A new week at Varndean

| Status | ID | Art | Motiv | Dateien |
| --- | --- | --- | --- | --- |
| geliefert | `varndean-schultor` | Außenszene | Schultor der Varndean School: schmiedeeisernes Tor, Fahrradständer, Bushaltestelle mit Schulbus, Weg zur großen Holztür des Hauptgebäudes. Im Bild zeigen: get up, walk, early, always, far, near, bring, be in a hurry, Off we go!. | `art-source/world/varndean/varndean-schultor.png`<br>`beta/assets/world/varndean/varndean-schultor.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-schultor-640.webp (640×1137)` |
| geliefert | `varndean-schultor-licht` | Belohnungs-Ansicht | Morgensonne, Schulglocke über der Tür glänzt, Blüten am Tor. Basis: Außenszene varndean-schultor. | `art-source/world/varndean/varndean-schultor-licht.png`<br>`beta/assets/world/varndean/varndean-schultor-licht.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-schultor-licht-640.webp (640×1137)` |
| geliefert | `varndean-schultor-innen` | Lernraum | Garderobe im Eingang: Haken mit Schultaschen und Jacken, Sitzbank, Fenster mit Morgenlicht. Im Bild zeigen: get up, walk, early, always, far, near, bring, be in a hurry, Off we go!. | `art-source/world/varndean/varndean-schultor-innen.png`<br>`beta/assets/world/varndean/varndean-schultor-innen.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-schultor-innen-640.webp (640×1137)` |
| geliefert | `varndean-uhrturm` | Außenszene | Schulhof mit schlankem Uhrturm (Zifferblatt ohne Ziffern-Text, nur Striche), Turmtür unten als Eingang, Bänke, Bäume. Im Bild zeigen: o'clock, half past, quarter past, quarter to, midday, midnight, minute. | `art-source/world/varndean/varndean-uhrturm.png`<br>`beta/assets/world/varndean/varndean-uhrturm.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-uhrturm-640.webp (640×1137)` |
| geliefert | `varndean-uhrturm-licht` | Belohnungs-Ansicht | Turmuhr leuchtet warm, kleine Lichter im Turmfenster, Abendhimmel. Basis: Außenszene varndean-uhrturm. | `art-source/world/varndean/varndean-uhrturm-licht.png`<br>`beta/assets/world/varndean/varndean-uhrturm-licht.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-uhrturm-licht-640.webp (640×1137)` |
| geliefert | `varndean-uhrturm-innen` | Lernraum | Uhrwerk-Raum im Turm: große Zahnräder, Pendel, mehrere Uhren an der Wand (nur Zeiger und Striche). Im Bild zeigen: o'clock, half past, quarter past, quarter to, midday, midnight, minute. | `art-source/world/varndean/varndean-uhrturm-innen.png`<br>`beta/assets/world/varndean/varndean-uhrturm-innen.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-uhrturm-innen-640.webp (640×1137)` |
| geliefert | `varndean-klassenfluegel` | Außenszene | Klassenzimmer-Flügel: zweistöckiges Backsteingebäude mit großen Fenstern, in denen Globus, Mikroskop, Notenständer und Farbpaletten zu sehen sind (Fächer). Eingangstür mittig. Im Bild zeigen: maths, science, French, history, geography, art, music, timetable, homework, put your hand up. | `art-source/world/varndean/varndean-klassenfluegel.png`<br>`beta/assets/world/varndean/varndean-klassenfluegel.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-klassenfluegel-640.webp (640×1137)` |
| geliefert | `varndean-klassenfluegel-licht` | Belohnungs-Ansicht | Goldene Sterne an den Fenstern, warmes Licht in allen Räumen. Basis: Außenszene varndean-klassenfluegel. | `art-source/world/varndean/varndean-klassenfluegel-licht.png`<br>`beta/assets/world/varndean/varndean-klassenfluegel-licht.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-klassenfluegel-licht-640.webp (640×1137)` |
| geliefert | `varndean-kantine` | Außenszene | Kantine mit Außenterrasse am Schulhof: Tische mit Tabletts, Äpfeln, Salat, Eiswagen, Spielgeräte auf dem Schulhof, Tür zur Kantine. Im Bild zeigen: lunch, break, canteen, playground, food, apple, salad, ice cream, cook. | `art-source/world/varndean/varndean-kantine.png`<br>`beta/assets/world/varndean/varndean-kantine.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-kantine-640.webp (640×1137)` |
| geliefert | `varndean-kantine-licht` | Belohnungs-Ansicht | Lichterkette über der Terrasse, Eiswagen leuchtet. Basis: Außenszene varndean-kantine. | `art-source/world/varndean/varndean-kantine-licht.png`<br>`beta/assets/world/varndean/varndean-kantine-licht.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-kantine-licht-640.webp (640×1137)` |
| geliefert | `varndean-kantine-innen` | Lernraum | Essensausgabe mit Tabletts, Schüsseln mit Salat, Obstkorb, Eistruhe, langer Tisch im Vordergrund. Im Bild zeigen: lunch, break, canteen, playground, food, apple, salad, ice cream, cook. | `art-source/world/varndean/varndean-kantine-innen.png`<br>`beta/assets/world/varndean/varndean-kantine-innen.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-kantine-innen-640.webp (640×1137)` |
| geliefert | `varndean-aula` | Außenszene | Gebäude mit drei Eingängen nebeneinander erkennbar: Aula (Theatervorhang im Fenster), Turnhalle (Basketballkorb, Sprossenwand im Fenster), Bibliothek (Bücherregale im Fenster). Hauptportal in der Mitte. Im Bild zeigen: assembly hall, gym, PE, library, drama, theatre, concert, dancer, music. | `art-source/world/varndean/varndean-aula.png`<br>`beta/assets/world/varndean/varndean-aula.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-aula-640.webp (640×1137)` |
| geliefert | `varndean-aula-licht` | Belohnungs-Ansicht | Scheinwerfer auf der Bühne, Konfetti-Glanz. Basis: Außenszene varndean-aula. | `art-source/world/varndean/varndean-aula-licht.png`<br>`beta/assets/world/varndean/varndean-aula-licht.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-aula-licht-640.webp (640×1137)` |
| geliefert | `varndean-aula-innen` | Lernraum | Bühne der Aula mit rotem Vorhang, Notenständern und Tanzfläche; seitlich Bücherregal und Sportgeräte. Im Bild zeigen: assembly hall, gym, PE, library, drama, theatre, concert, dancer, music. | `art-source/world/varndean/varndean-aula-innen.png`<br>`beta/assets/world/varndean/varndean-aula-innen.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-aula-innen-640.webp (640×1137)` |
| geliefert | `varndean-kalender` | Außenszene | Schulgarten mit vier Beeten in den vier Jahreszeiten (Frühlingsblüten, Sommersonne, Herbstlaub, Winterschnee), in der Mitte ein Gartenhaus als Eingang. Im Bild zeigen: January, February, spring, summer, autumn, winter, date, term, holidays, weekend. | `art-source/world/varndean/varndean-kalender.png`<br>`beta/assets/world/varndean/varndean-kalender.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-kalender-640.webp (640×1137)` |
| geliefert | `varndean-kalender-licht` | Belohnungs-Ansicht | Alle vier Beete leuchten, Laternen im Garten. Basis: Außenszene varndean-kalender. | `art-source/world/varndean/varndean-kalender-licht.png`<br>`beta/assets/world/varndean/varndean-kalender-licht.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-kalender-licht-640.webp (640×1137)` |
| geliefert | `varndean-kalender-innen` | Lernraum | Gartenhaus innen mit großem Wandkalender ohne Schrift (zwölf farbige Felder), Jahreszeiten-Mobile, Geburtstags-Girlande. Im Bild zeigen: January, February, spring, summer, autumn, winter, date, term, holidays, weekend. | `art-source/world/varndean/varndean-kalender-innen.png`<br>`beta/assets/world/varndean/varndean-kalender-innen.webp (941×1672)`<br>`beta/assets/world/varndean/varndean-kalender-innen-640.webp (640×1137)` |

### Priorität 2: Unit 3: In our free time

| Status | ID | Art | Motiv | Dateien |
| --- | --- | --- | --- | --- |
| geliefert | `freizeit-clubhaus` | Außenszene | Clubhaus aus Holz mit Veranda, auf der Veranda ein großes Schachbrett, Instrumente am Fenster (Geige, Trommel), Eingangstür mittig. Im Bild zeigen: club, join, member, chess, orchestra, choir, instrument, practise, be bored. | `art-source/world/freizeit/freizeit-clubhaus.png`<br>`beta/assets/world/freizeit/freizeit-clubhaus.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-clubhaus-640.webp (640×1137)` |
| geliefert | `freizeit-clubhaus-licht` | Belohnungs-Ansicht | Notenlichter über dem Dach, Fenster warm beleuchtet. Basis: Außenszene freizeit-clubhaus. | `art-source/world/freizeit/freizeit-clubhaus-licht.png`<br>`beta/assets/world/freizeit/freizeit-clubhaus-licht.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-clubhaus-licht-640.webp (640×1137)` |
| geliefert | `freizeit-clubhaus-innen` | Lernraum | Musik- und Clubraum: Notenständer, Instrumente, Chor-Podest, Schachtisch, Pinnwand ohne Schrift. Im Bild zeigen: club, join, member, chess, orchestra, choir, instrument, practise, be bored. | `art-source/world/freizeit/freizeit-clubhaus-innen.png`<br>`beta/assets/world/freizeit/freizeit-clubhaus-innen.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-clubhaus-innen-640.webp (640×1137)` |
| geliefert | `freizeit-sportplatz` | Außenszene | Sportplatz mit roter Laufbahn, Ziellinie, Fahrrädern, Wimpeln, kleines Vereinsheim als Eingang. Im Bild zeigen: race, runner, cycle, medal, win, lose, winner, cheer, train, Good luck!. | `art-source/world/freizeit/freizeit-sportplatz.png`<br>`beta/assets/world/freizeit/freizeit-sportplatz.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-sportplatz-640.webp (640×1137)` |
| geliefert | `freizeit-sportplatz-licht` | Belohnungs-Ansicht | Siegerpodest mit Glanz, Fahnen, Konfetti. Basis: Außenszene freizeit-sportplatz. | `art-source/world/freizeit/freizeit-sportplatz-licht.png`<br>`beta/assets/world/freizeit/freizeit-sportplatz-licht.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-sportplatz-licht-640.webp (640×1137)` |
| geliefert | `freizeit-sportplatz-innen` | Lernraum | Umkleide mit Medaillen-Wand, Trinkflaschen, Laufschuhen, Bank im Vordergrund. Im Bild zeigen: race, runner, cycle, medal, win, lose, winner, cheer, train, Good luck!. | `art-source/world/freizeit/freizeit-sportplatz-innen.png`<br>`beta/assets/world/freizeit/freizeit-sportplatz-innen.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-sportplatz-innen-640.webp (640×1137)` |
| geliefert | `freizeit-gefuehle` | Außenszene | Holzbrücke über einen Bach, am Geländer runde Schilder mit gemalten Gesichtern (fröhlich, traurig, wütend, nervös, aufgeregt) ohne Schrift, Pavillon am anderen Ende als Eingang. Im Bild zeigen: happy, sad, angry, nervous, excited, bored, unhappy, agree, hate, No way!, Oh dear!. | `art-source/world/freizeit/freizeit-gefuehle.png`<br>`beta/assets/world/freizeit/freizeit-gefuehle.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-gefuehle-640.webp (640×1137)` |
| geliefert | `freizeit-gefuehle-licht` | Belohnungs-Ansicht | Regenbogen über der Brücke, Glühwürmchen. Basis: Außenszene freizeit-gefuehle. | `art-source/world/freizeit/freizeit-gefuehle-licht.png`<br>`beta/assets/world/freizeit/freizeit-gefuehle-licht.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-gefuehle-licht-640.webp (640×1137)` |
| geliefert | `freizeit-gefuehle-innen` | Lernraum | Gemütliche Ruhe-Ecke im Pavillon: Kissen, Decke, Gefühls-Gesichter als Bilder, Fenster zum Bach. Im Bild zeigen: happy, sad, angry, nervous, excited, bored, unhappy, agree, hate, No way!, Oh dear!. | `art-source/world/freizeit/freizeit-gefuehle-innen.png`<br>`beta/assets/world/freizeit/freizeit-gefuehle-innen.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-gefuehle-innen-640.webp (640×1137)` |
| geliefert | `marktplatz-licht` | Belohnungs-Ansicht | Neu nötig: Belohnungs-Ansicht des vorhandenen Marktplatzes, Lichterketten über den Ständen, Laternen an. Basis: Außenszene marktplatz (vorhanden: world/hafenstadt/marktplatz.webp). | `art-source/world/freizeit/marktplatz-licht.png`<br>`beta/assets/world/freizeit/marktplatz-licht.webp (941×1672)`<br>`beta/assets/world/freizeit/marktplatz-licht-640.webp (640×1137)` |
| geliefert | `freizeit-backstube` | Außenszene | Kleine Backstube mit Schornstein, Brezel- und Kuchen-Schaufenster ohne Schrift, Mehlsäcke vor der Tür, Eingangstür mittig. Im Bild zeigen: recipe, ingredient, flour, sugar, butter, egg, chocolate, oven, fridge, bake, cut, scone. | `art-source/world/freizeit/freizeit-backstube.png`<br>`beta/assets/world/freizeit/freizeit-backstube.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-backstube-640.webp (640×1137)` |
| geliefert | `freizeit-backstube-licht` | Belohnungs-Ansicht | Ofen glüht, fertiger Kuchen im Fenster, warmer Dampf. Basis: Außenszene freizeit-backstube. | `art-source/world/freizeit/freizeit-backstube-licht.png`<br>`beta/assets/world/freizeit/freizeit-backstube-licht.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-backstube-licht-640.webp (640×1137)` |
| geliefert | `freizeit-backstube-innen` | Lernraum | Küche mit Backofen, Kühlschrank, Waage, Schüsseln mit Mehl, Zucker, Eiern, Butter, Schokolade, Teller mit Scones, Arbeitsfläche im Vordergrund. Im Bild zeigen: recipe, ingredient, flour, sugar, butter, egg, chocolate, oven, fridge, bake, cut, scone. | `art-source/world/freizeit/freizeit-backstube-innen.png`<br>`beta/assets/world/freizeit/freizeit-backstube-innen.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-backstube-innen-640.webp (640×1137)` |
| geliefert | `freizeit-picknick` | Außenszene | Wiese mit Picknickdecke, Geschenken, Torte, Ballons und einer Laube als Eingang. Im Bild zeigen: birthday, invitation, present, cake, picnic, biscuit, sweet, Would you like…?. | `art-source/world/freizeit/freizeit-picknick.png`<br>`beta/assets/world/freizeit/freizeit-picknick.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-picknick-640.webp (640×1137)` |
| geliefert | `freizeit-picknick-licht` | Belohnungs-Ansicht | Lampions, Kerzen auf der Torte, Sternenhimmel. Basis: Außenszene freizeit-picknick. | `art-source/world/freizeit/freizeit-picknick-licht.png`<br>`beta/assets/world/freizeit/freizeit-picknick-licht.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-picknick-licht-640.webp (640×1137)` |
| geliefert | `freizeit-picknick-innen` | Lernraum | Laube innen: gedeckter Tisch mit Geburtstagstorte, Geschenken, Saft, Keksen, Süßigkeiten. Im Bild zeigen: birthday, invitation, present, cake, picnic, biscuit, sweet, Would you like…?. | `art-source/world/freizeit/freizeit-picknick-innen.png`<br>`beta/assets/world/freizeit/freizeit-picknick-innen.webp (941×1672)`<br>`beta/assets/world/freizeit/freizeit-picknick-innen-640.webp (640×1137)` |

### Priorität 3: Unit 4: Out and about in Brighton

| Status | ID | Art | Motiv | Dateien |
| --- | --- | --- | --- | --- |
| geliefert | `stadt-aussicht` | Außenszene | Aussichtsplattform über dem Meer mit Bank und Münzfernrohr, Blick auf Pier und Strand, kleines Museum mit Säulen als Eingang. Im Bild zeigen: sight, famous, work of art, view, visitor, bench, beautiful, magical. | `art-source/world/stadt/stadt-aussicht.png`<br>`beta/assets/world/stadt/stadt-aussicht.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-aussicht-640.webp (640×1137)` |
| geliefert | `stadt-aussicht-licht` | Belohnungs-Ansicht | Sonnenuntergang über dem Pier, Lichter am Pier. Basis: Außenszene stadt-aussicht. | `art-source/world/stadt/stadt-aussicht-licht.png`<br>`beta/assets/world/stadt/stadt-aussicht-licht.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-aussicht-licht-640.webp (640×1137)` |
| geliefert | `stadt-aussicht-innen` | Lernraum | Mini-Museum: Kunstwerke auf Sockeln, Bilderrahmen ohne Schrift, Bank im Vordergrund. Im Bild zeigen: sight, famous, work of art, view, visitor, bench, beautiful, magical. | `art-source/world/stadt/stadt-aussicht-innen.png`<br>`beta/assets/world/stadt/stadt-aussicht-innen.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-aussicht-innen-640.webp (640×1137)` |
| geliefert | `stadt-wetter` | Außenszene | Strandpromenade mit kleiner Wetterstation (Windrad, Thermometer ohne Zahlen, Wetterhahn), halb Sonne, halb Wolken, Pfützen, Eingang zur Wetterstation. Im Bild zeigen: weather, sunny, cloudy, windy, rainy, stormy, snowy, rain, snow. | `art-source/world/stadt/stadt-wetter.png`<br>`beta/assets/world/stadt/stadt-wetter.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-wetter-640.webp (640×1137)` |
| geliefert | `stadt-wetter-licht` | Belohnungs-Ansicht | Regenbogen nach dem Schauer, glitzernde Pfützen. Basis: Außenszene stadt-wetter. | `art-source/world/stadt/stadt-wetter-licht.png`<br>`beta/assets/world/stadt/stadt-wetter-licht.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-wetter-licht-640.webp (640×1137)` |
| geliefert | `stadt-wetter-innen` | Lernraum | Wetterraum mit Wetterkarte ohne Schrift (Sonnen-, Wolken-, Regen-, Schneesymbole), Regenschirme, Gummistiefel. Im Bild zeigen: weather, sunny, cloudy, windy, rainy, stormy, snowy, rain, snow. | `art-source/world/stadt/stadt-wetter-innen.png`<br>`beta/assets/world/stadt/stadt-wetter-innen.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-wetter-innen-640.webp (640×1137)` |
| geliefert | `stadt-laeden` | Außenszene | Straße mit Postamt (roter britischer Briefkasten davor), Bäckerei und Laden mit Markise, Gehweg vorne, Eingangstür des Postamts mittig. Im Bild zeigen: post box, post office, bakery, customer, cost, pound, expensive, sell, opposite, pavement. | `art-source/world/stadt/stadt-laeden.png`<br>`beta/assets/world/stadt/stadt-laeden.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-laeden-640.webp (640×1137)` |
| geliefert | `stadt-laeden-licht` | Belohnungs-Ansicht | Schaufenster beleuchtet, Laternen an. Basis: Außenszene stadt-laeden. | `art-source/world/stadt/stadt-laeden-licht.png`<br>`beta/assets/world/stadt/stadt-laeden-licht.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-laeden-licht-640.webp (640×1137)` |
| geliefert | `stadt-laeden-innen` | Lernraum | Postschalter mit Paketen, Briefmarken und Waage, daneben Bäckertheke mit Brot. Im Bild zeigen: post box, post office, bakery, customer, cost, pound, expensive, sell, opposite, pavement. | `art-source/world/stadt/stadt-laeden-innen.png`<br>`beta/assets/world/stadt/stadt-laeden-innen.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-laeden-innen-640.webp (640×1137)` |
| geliefert | `stadt-kino` | Außenszene | Altes Kino mit Glühbirnen-Vordach ohne Schrift, daneben ein Karussell am Meer, Eingang zum Kino mittig. Im Bild zeigen: cinema, ride, light, decide, suggest, expensive, exciting. | `art-source/world/stadt/stadt-kino.png`<br>`beta/assets/world/stadt/stadt-kino.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-kino-640.webp (640×1137)` |
| geliefert | `stadt-kino-licht` | Belohnungs-Ansicht | Glühbirnen und Karussell-Lichter an, Abendhimmel. Basis: Außenszene stadt-kino. | `art-source/world/stadt/stadt-kino-licht.png`<br>`beta/assets/world/stadt/stadt-kino-licht.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-kino-licht-640.webp (640×1137)` |
| geliefert | `stadt-kino-innen` | Lernraum | Kinosaal mit roten Sesseln, leerer Leinwand, Popcorn. Im Bild zeigen: cinema, ride, light, decide, suggest, expensive, exciting. | `art-source/world/stadt/stadt-kino-innen.png`<br>`beta/assets/world/stadt/stadt-kino-innen.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-kino-innen-640.webp (640×1137)` |
| geliefert | `stadt-bildwerkstatt` | Außenszene | Atelier mit großem Fenster, Staffelei mit halbfertigem Bild draußen, Farbtöpfe, Tür mittig. Im Bild zeigen: description, title, caption, foreground, middle, on the left, on the right, at the top, at the bottom. | `art-source/world/stadt/stadt-bildwerkstatt.png`<br>`beta/assets/world/stadt/stadt-bildwerkstatt.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-bildwerkstatt-640.webp (640×1137)` |
| geliefert | `stadt-bildwerkstatt-licht` | Belohnungs-Ansicht | Galerie-Spots auf den Bildern. Basis: Außenszene stadt-bildwerkstatt. | `art-source/world/stadt/stadt-bildwerkstatt-licht.png`<br>`beta/assets/world/stadt/stadt-bildwerkstatt-licht.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-bildwerkstatt-licht-640.webp (640×1137)` |
| geliefert | `stadt-bildwerkstatt-innen` | Lernraum | Bilderwand mit Rahmen (Landschaften ohne Schrift), Staffelei, Tisch im Vordergrund. Gut erkennbar: Vordergrund, Mitte, Hintergrund, oben, unten, links, rechts. Im Bild zeigen: description, title, caption, foreground, middle, on the left, on the right, at the top, at the bottom. | `art-source/world/stadt/stadt-bildwerkstatt-innen.png`<br>`beta/assets/world/stadt/stadt-bildwerkstatt-innen.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-bildwerkstatt-innen-640.webp (640×1137)` |
| geliefert | `stadt-buddy` | Außenszene | Gasse mit Reihenhaus, Hundehütte für Buddy (Hund nur als Hütte, Napf und Leine angedeutet), Schlüssel im Schloss der Haustür, Werkzeugkiste. Im Bild zeigen: rescue, police, key, locked, hide, follow, brave, worried, tidy, wash the dishes, dry, tooth. | `art-source/world/stadt/stadt-buddy.png`<br>`beta/assets/world/stadt/stadt-buddy.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-buddy-640.webp (640×1137)` |
| geliefert | `stadt-buddy-licht` | Belohnungs-Ansicht | Polizeiwagen mit Blaulicht vor dem Haus, Hütte bekränzt, alles gerettet. Basis: Außenszene stadt-buddy. | `art-source/world/stadt/stadt-buddy-licht.png`<br>`beta/assets/world/stadt/stadt-buddy-licht.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-buddy-licht-640.webp (640×1137)` |
| geliefert | `stadt-buddy-innen` | Lernraum | Küche des Hauses: Spüle mit Geschirr, Geschirrtuch, Zahnbürsten im Becher, Besen, Werkzeug. Im Bild zeigen: rescue, police, key, locked, hide, follow, brave, worried, tidy, wash the dishes, dry, tooth. | `art-source/world/stadt/stadt-buddy-innen.png`<br>`beta/assets/world/stadt/stadt-buddy-innen.webp (941×1672)`<br>`beta/assets/world/stadt/stadt-buddy-innen-640.webp (640×1137)` |

### Priorität 1: Unit 2: A new week at Varndean

| Status | ID | Art | Motiv | Dateien |
| --- | --- | --- | --- | --- |
| geliefert | `tie` | Kleidungsstück | Schulkrawatte (Slot `neck`). Gestreifte Schulkrawatte in Petrol und Gold, Varndean-Stil, ohne Wappen-Schrift. | `art-source/rewards/tie.png`<br>`beta/assets/rewards/tie.webp (512×512)`<br>`beta/assets/rewards/tie-128.webp (128×128)` |

### Priorität 2: Unit 3: In our free time

| Status | ID | Art | Motiv | Dateien |
| --- | --- | --- | --- | --- |
| geliefert | `chef` | Kleidungsstück | Kochmütze (Slot `hat`). Weiße Kochmütze mit kleinem Kochlöffel-Anstecker. | `art-source/rewards/chef.png`<br>`beta/assets/rewards/chef.webp (512×512)`<br>`beta/assets/rewards/chef-128.webp (128×128)` |

### Priorität 3: Unit 4: Out and about in Brighton

| Status | ID | Art | Motiv | Dateien |
| --- | --- | --- | --- | --- |
| geliefert | `sou_wester` | Kleidungsstück | Südwester (Slot `hat`). Gelber Südwester-Regenhut mit breiter Krempe hinten. | `art-source/rewards/sou_wester.png`<br>`beta/assets/rewards/sou_wester.webp (512×512)`<br>`beta/assets/rewards/sou_wester-128.webp (128×128)` |

## Wiederverwenden (nichts neu zu gestalten)

| Bild | Datei | Verwendung in Units 2–4 |
| --- | --- | --- |
| `schule-am-meer-klassenzimmer` | `world/hafenstadt/klassenzimmer.webp` | Lernraum von Unit 2 „Klassenzimmer“ |
| `marktplatz` | `world/hafenstadt/marktplatz.webp` | Außenszene von Unit 3 „Markt & Obststand“ (bisher keinem Lernort zugeordnet) |
| `marktplatz-obststand` | `world/hafenstadt/obststand.webp` | Lernraum von Unit 3 „Markt & Obststand“ |
| `ortsdiplom_urkunde` | `rewards/ortsdiplom_urkunde.webp` | Unit-Diplome 2–4: die App setzt Unit-Nummer und Name als Text darüber |
| `unterricht_schulbuch` | `rewards/unterricht_schulbuch.webp` | Region-Bild Unit 2 (vorläufig, eigenes Bild optional) |
| `stufenaufstieg_podest` | `rewards/stufenaufstieg_podest.webp` | Region-Bild Unit 3 (vorläufig, eigenes Bild optional) |
| `brighton_reisekompass` | `rewards/brighton_reisekompass.webp` | Region-Bild Unit 4 (vorläufig, eigenes Bild optional) |
| `hintergrund_*, menue_*, hafen_hintergrund` | `rewards/` | Alle Menü-Hintergründe gelten unverändert auch für Units 2–4 |
| `journalPostcards` | `rewards/postkarte_*.webp` | Reisetagebuch, unabhängig von den Units |
| `Friedrich-Stufen und Posen` | `friedrich/` | unverändert |

Optional später: eigene Region-Bilder (`region_varndean`, `region_freizeit`, `region_stadt`, 512 × 512 px freigestellt) und Kleidungs-Ebenen je Möwen-Stufe (`<stufe>/wear-tie` usw., siehe `tools/`).
