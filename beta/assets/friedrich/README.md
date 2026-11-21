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

Nicht von Hand hier ablegen. Die Original-PNGs (2048 px) kommen nach `art-source/friedrich/` und werden mit
`python3 tools/import_friedrich.py <ordner>` geprüft, verkleinert und ins Manifest eingetragen.

Reihenfolge: zuerst nur die 5 Masteransichten der Königsmöwe. Weitere Bilder erst nach Freigabe.
