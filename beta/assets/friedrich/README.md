# Friedrich 2.0 – Grafikordner

Hier liegen nur fertige, freigegebene Bilder als WebP. Die App liest `manifest.json` und zeigt nur, was dort eingetragen ist. Alles andere erscheint als beschrifteter Platzhalter.

| Ordner | Stufe | ab Fischen |
|---|---|---|
| egg | Ei | Start |
| chick | Küken | 0 |
| young | Jungmöwe | 60 |
| adult | Möwe | 180 |
| captain | Kapitänsmöwe | 450 |
| king | Königsmöwe (mit Krone) | 900 |

Pro Stufe: `front, 3quarter, side, back, face` (Ansichten) und `blink, look_left, look_right, wave, celebrate, think, encourage` (Animations-Frames).
Jedes Bild als `<pose>.webp` (1024 px) und `<pose>-512.webp`.

## Freigegebene Grafiken (Ablauf ab jetzt)

Freigegebene Grafiken liegen **nicht** auf `main`, sondern auf dem Branch `beta/friedrich-2-assets` unter `beta/assets/friedrich/` samt `manifest.json`.
Der Prüfstand lädt sie nur über einen **commitgenauen** Link auf diese `manifest.json` (volle Commit-ID, kein Branch-Link):

    https://eternity03238-commits.github.io/Englisch-_5thclass/beta/friedrich.html?manifest=<Commit-Link>

Bilder werden über ihre IDs im Manifest zugeordnet (z. B. `friedrich_king_front`) und aus demselben Commit geladen, WebP bevorzugt, sonst PNG.
Die Beta-App und die Hauptanwendung zeigen weiter Platzhalter bzw. die bisherige Möwe. Eine Übernahme dorthin braucht eine eigene Freigabe.

## Alter Weg (lokal)

Nicht von Hand hier ablegen. Die Original-PNGs (2048 px) kommen nach `art-source/friedrich/` und werden mit
`python3 tools/import_friedrich.py <ordner>` geprüft, verkleinert und ins Manifest eingetragen.

Reihenfolge: zuerst nur die 5 Masteransichten der Königsmöwe. Weitere Bilder erst nach Freigabe.
