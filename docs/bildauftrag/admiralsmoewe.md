# Bildauftrag: Admiralsmöwe

Möwenflug, Englisch Klasse 5 · Stand 22.11.2026 · maschinenlesbar: [`admiralsmoewe.json`](admiralsmoewe.json)

Friedrich bekommt eine neue Wachstumsstufe zwischen Kapitänsmöwe und Königsmöwe. Mit vier Units im Schuljahr waren die alten Stufen zu schnell erreicht. Die neue Reihenfolge:

| Stufe | Schlüssel | ab Fischen | Kopfbedeckung (fest im Bild) |
| --- | --- | --- | --- |
| Ei | `egg` | 0 | – |
| Küken | `chick` | 0 | – |
| Jungmöwe | `young` | 60 | – |
| Möwe | `adult` | 180 | – |
| Kapitänsmöwe | `captain` | 450 | dunkelblaue Kapitänsmütze mit Anker |
| **Admiralsmöwe** | **`admiral`** | **1100** | **Admirals-Zweispitz (neu)** |
| Königsmöwe | `king` | 2000 | goldene Krone |

Die App ist schon fertig umgebaut. Solange die Bilder fehlen, zeigt sie für die Admiralsmöwe die Kapitänsmöwe. Sobald die Bilder im Manifest stehen, erscheinen sie automatisch.

## So wird der Auftrag abgearbeitet

1. Die Bilder unten der Reihe nach erzeugen (zuerst `3quarter`, alle anderen richten sich danach).
2. PNGs mit den Dateinamen aus der Tabelle in einen Ordner legen und im Repo ausführen:
   `python3 tools/import_friedrich.py <ordner> --repo .`
   Das Skript prüft die Bilder, legt die Originale unter `art-source/friedrich/admiral/` ab, erzeugt `beta/assets/friedrich/admiral/<pose>.webp` und `<pose>-512.webp` und trägt sie in `beta/assets/friedrich/manifest.json` ein.
   Die Manifest-Version erhöht das Skript selbst.
3. Alles auf den Branch `beta/friedrich-2-assets` committen und in `admiralsmoewe.json` bei erledigten Bildern `status` auf `"geliefert"` setzen.
4. Katharina gibt die Bilder frei und schickt Claude den commitgenauen Manifest-Link. Erst dann baut die App sie fest ein und Claude justiert die Kleidungs-Anker im Prüfstand (`beta/friedrich.html`).

## Die Figur

**Es ist dieselbe Möwe wie bisher.** Körper, Gefieder, Gesicht, Augen, Schnabel, Beine und Proportionen bleiben exakt wie bei der Kapitänsmöwe. Nur die Kopfbedeckung ist neu.

Vorlagen (bitte genau ansehen):

- `art-source/friedrich/captain/<pose>.png`: gleiche Haltung, gleiche Größe, gleiche Position im Bild
- `art-source/friedrich/king/<pose>.png`: so festlich soll die höchste Stufe wirken, die Admiralsmöwe liegt knapp darunter

**Die neue Kopfbedeckung: ein Admirals-Zweispitz**

- Dunkler Marineblau-Filz wie die Kapitänsmütze, aber als Zweispitz quer auf dem Kopf (Spitzen nach links und rechts, in der Dreiviertelansicht leicht perspektivisch).
- Breite goldene Borte am Rand, vorne eine runde goldene Kokarde mit kleinem Anker.
- Oben am Hut eine kleine weiße Feder als Schmuck.
- Sitzt fest und gerade auf dem Kopf, etwas größer und edler als die Kapitänsmütze, aber nicht so hoch wie die Krone. Der Hut darf die Augen nicht verdecken.
- Weiche 3D-Optik wie Mütze und Krone, gleiche Lichtrichtung.

**Sonst nichts anziehen.** Keine Jacke, keine Schulterklappen, keine Orden, nichts am Hals oder am Rücken. Die App setzt dort Kleidungsstücke aus dem Kleiderschrank auf (Fliege, Krawatte, Rucksack, Sonnenbrille, Kopfhörer). Die passen nur, wenn Hals, Brust, Flügel und Augen genau dort liegen wie bei der Kapitänsmöwe.

## Technische Vorgaben (für jedes Bild)

- PNG, quadratisch, mindestens 1024 × 1024 px, besser 2048 × 2048 px
- echter transparenter Hintergrund (Alphakanal), kein Schatten auf dem Boden, keine Bodenfläche
- Figur füllt etwa 80 % der Bildhöhe, steht mittig (Mitte bei 50 % der Breite), Füße auf derselben Höhe wie bei der Kapitänsmöwe
- Hutspitze und Feder mit mindestens 4 % Abstand zum oberen Bildrand
- keine Schrift, keine Zahlen, kein Rahmen
- alle Frames deckungsgleich zu `admiral/3quarter`: Körper, Füße und Kopf liegen pixelgenau an derselben Stelle, nur die beschriebenen Teile (Augen, Flügel, Blick) ändern sich. Die App blendet die Frames über die Grundansicht.

## Die Bilder

| # | Datei | Pose | Motiv | Pflicht |
| --- | --- | --- | --- | --- |
| 1 | `friedrich_admiral_3quarter.png` | Dreiviertelansicht | Grundansicht wie `captain/3quarter`: steht, Blick nach rechts, freundlich und stolz | ja |
| 2 | `friedrich_admiral_front.png` | Vorderansicht | wie `captain/front`, Blick zum Betrachter | ja |
| 3 | `friedrich_admiral_side.png` | Seitenansicht | wie `captain/side`, Profil nach rechts | ja |
| 4 | `friedrich_admiral_back.png` | Rückenansicht | wie `captain/back`, Zweispitz von hinten mit Feder | ja |
| 5 | `friedrich_admiral_face.png` | Kopf-Porträt | wie `captain/face`: nur Kopf mit Hut, groß, für das runde Profilbild | ja |
| 6 | `friedrich_admiral_blink.png` | Frame: Blinzeln | wie 3quarter, beide Augen geschlossen (entspannt, nicht schlafend) | ja |
| 7 | `friedrich_admiral_look_left.png` | Frame: Blick links | wie 3quarter, Augen und Kopf leicht nach links gedreht | ja |
| 8 | `friedrich_admiral_look_right.png` | Frame: Blick rechts | wie 3quarter, Augen und Kopf leicht nach rechts gedreht | ja |
| 9 | `friedrich_admiral_wave.png` | Frame: Winken | wie 3quarter, vorderer Flügel zum Gruß erhoben | ja |
| 10 | `friedrich_admiral_celebrate.png` | Frame: Jubeln | wie 3quarter, beide Flügel hoch, Augen fröhlich, Schnabel offen | ja |
| 11 | `friedrich_admiral_think.png` | Frame: Nachdenken | wie 3quarter, Flügelspitze am Schnabel, Blick nach oben | ja |
| 12 | `friedrich_admiral_encourage.png` | Frame: Mutmachen | wie 3quarter, Flügel nach vorn gestreckt wie ein „Daumen hoch“, aufmunternder Blick | ja |
| 13 | `friedrich_admiral_fly.png` | Fliegen | wie `king/fly`: im Gleitflug, Flügel ausgebreitet, Hut sitzt fest | optional |

## Manifest-Einträge (macht das Import-Skript)

```json
"admiral/3quarter": {"w": 1024, "h": 1024, "src": "friedrich_admiral_3quarter.png"},
"admiral/front":    {"w": 1024, "h": 1024, "src": "friedrich_admiral_front.png"}
```

…und so weiter für jede Pose, Schlüssel immer `admiral/<pose>`. Die App erkennt die Stufe an `admiral/3quarter`. Fehlt diese Ansicht, zeigt sie weiter die Kapitänsmöwe.
