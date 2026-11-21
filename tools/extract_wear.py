"""Kleidungs-Ebene aus einem "angezogenen" Friedrich-Bild herauslösen.

Aufruf:
  python3 extract_wear.py --base <grundbild.png|webp> --dressed <angezogen.png> --out friedrich_<stufe>_wear-<teil>.png

  --base     das freigegebene Grundbild der Stufe, z. B. adult/3quarter (2048 PNG oder 1024 WebP)
  --dressed  dasselbe Bild, in dem NUR das Kleidungsstück ergänzt wurde (gleicher Ausschnitt, gleiche Größe)
  --out      die fertige Ebene: nur das Kleidungsstück auf transparentem Hintergrund, gleiche Leinwand

Prüfungen (Abbruch mit Hinweis, wenn etwas nicht stimmt):
  - gleiche Bildgröße und Seitenverhältnis
  - die Figur darf sich außerhalb des Kleidungsstücks kaum verändert haben (sonst passt die Ebene nicht)
  - das Kleidungsstück muss eine zusammenhängende, sinnvolle Fläche sein

Die Ebene wird danach wie jedes andere Bild mit import_friedrich.py übernommen
(Manifest-Schlüssel <stufe>/wear-<teil>, Datei <stufe>/wear-<teil>.webp).
"""
import sys, argparse
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

def load(p, size=None):
    im = Image.open(p).convert("RGBA")
    if size and im.size != size: im = im.resize(size, Image.LANCZOS)
    return im

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True); ap.add_argument("--dressed", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--threshold", type=float, default=34, help="Mindestunterschied pro Pixel (0–255)")
    ap.add_argument("--min-area", type=float, default=0.002, help="kleinste Fläche des Teils, Anteil am Bild")
    ap.add_argument("--max-drift", type=float, default=7.0, help="erlaubte mittlere Abweichung der übrigen Figur")
    a = ap.parse_args()

    dressed = Image.open(a.dressed).convert("RGBA")
    base = load(a.base)
    if abs(base.size[0]/base.size[1] - dressed.size[0]/dressed.size[1]) > 0.002:
        sys.exit(f"ABGELEHNT: Seitenverhältnis unterschiedlich ({base.size} gegen {dressed.size})")
    base = load(a.base, dressed.size)
    B = np.asarray(base).astype(np.int16); D = np.asarray(dressed).astype(np.int16)
    h, w = B.shape[:2]

    # Unterschied: Farbe (nur wo etwas sichtbar ist) und Deckkraft
    vis = (np.maximum(B[..., 3], D[..., 3]) > 24)
    dc = np.abs(B[..., :3] - D[..., :3]).max(axis=2) * vis
    da = np.abs(B[..., 3] - D[..., 3])
    diff = np.maximum(dc, da)
    mask = diff > a.threshold
    # Rauschen weg, Lücken schließen, nur zusammenhängende größere Flächen behalten
    mask = ndimage.binary_opening(mask, iterations=2)
    mask = ndimage.binary_closing(mask, iterations=4)
    lab, n = ndimage.label(mask)
    fig0 = B[..., 3] > 24
    if not n:
        d0 = float(dc[fig0].mean()) if fig0.any() else 0.0
        if d0 > a.max_drift: sys.exit(f"ABGELEHNT: Die ganze Figur ist verändert (Abweichung {d0:.1f}). Bitte nur das Kleidungsstück ergänzen und alles andere unverändert lassen.")
        sys.exit("ABGELEHNT: kein Kleidungsstück gefunden (Bilder sind praktisch gleich)")
    sizes = ndimage.sum(mask, lab, range(1, n + 1))
    keep = [i + 1 for i, s in enumerate(sizes) if s >= max(sizes.max() * 0.08, h * w * 0.0004)]
    mask = np.isin(lab, keep)
    mask = ndimage.binary_fill_holes(mask)
    area = mask.sum() / (h * w)
    if area < a.min_area: sys.exit(f"ABGELEHNT: Kleidungsstück zu klein ({area*100:.2f} % des Bildes)")

    # Hat sich die übrige Figur verändert? Dann passt die Ebene nicht auf das freigegebene Grundbild.
    ring = ndimage.binary_dilation(mask, iterations=int(min(h, w) * 0.02))
    fig = (B[..., 3] > 24) & ~ring
    drift = float(dc[fig].mean()) if fig.any() else 0.0
    ys, xs = np.nonzero(mask)
    print(f"Teil gefunden: {area*100:.2f} % der Fläche, Bereich x {xs.min()/w*100:.0f}–{xs.max()/w*100:.0f} %, y {ys.min()/h*100:.0f}–{ys.max()/h*100:.0f} %")
    print(f"Abweichung der übrigen Figur: {drift:.1f} (erlaubt bis {a.max_drift})")
    if drift > a.max_drift:
        sys.exit("ABGELEHNT: Die Figur wurde beim Anziehen mitverändert. Bitte nur das Kleidungsstück ergänzen und alles andere unverändert lassen.")

    # Ebene: angezogene Pixel im Bereich, weicher Rand (2 px)
    soft = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.2))
    alpha = (np.asarray(soft).astype(np.float32) / 255.0) * (D[..., 3] / 255.0)
    out = np.dstack([D[..., :3], (alpha * 255).round()]).astype(np.uint8)
    Image.fromarray(out, "RGBA").save(a.out)
    # Kontrolle: Grundbild + Ebene muss wieder wie das angezogene Bild aussehen
    comp = base.copy(); comp.alpha_composite(Image.fromarray(out, "RGBA"))
    res = np.abs(np.asarray(comp).astype(np.int16)[..., :3] - D[..., :3]).max(axis=2)[vis].mean()
    print(f"Kontrolle Grundbild + Ebene gegen angezogenes Bild: mittlere Abweichung {res:.1f}")
    print(f"Gespeichert: {a.out}")

if __name__ == "__main__":
    main()
