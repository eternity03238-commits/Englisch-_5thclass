"""Friedrich-Grafiken importieren.

Aufruf:  python3 import_friedrich.py <ordner-mit-pngs> [--repo /pfad/zum/repo]

Erwartete Dateinamen: friedrich_<stufe>_<pose>.png oder friedrich_<stufe>_wear-<teil>.png (Kleidungs-Ebene)
  stufe: egg, chick, young, adult, captain, king
  pose:  front, 3quarter, side, back, face, blink, look_left, look_right, wave, celebrate, think, encourage

Was passiert:
  1. Prüfung: echter Alphakanal, quadratisch, mindestens 1024 px, Figur nutzt etwa 80 % der Höhe.
  2. Original-PNG wird unverändert unter art-source/friedrich/<stufe>/ abgelegt (wird nie geladen).
  3. Gleichmäßig verkleinert (kein Zuschnitt, damit alle Ansichten gleich groß bleiben) auf
     1024 px und 512 px WebP unter beta/assets/friedrich/<stufe>/<pose>.webp und <pose>-512.webp.
  4. manifest.json wird aktualisiert, die App zeigt das Bild danach automatisch.
"""
import sys, os, re, json, shutil
from PIL import Image

STAGES = ["egg", "chick", "young", "adult", "captain", "king"]
POSES = ["front", "3quarter", "side", "back", "face", "blink", "look_left", "look_right", "wave", "celebrate", "think", "encourage"]
POSES += ["crack", "hatch", "fly"]
# Kleidungs-Ebenen: friedrich_<stufe>_wear-<teil>.png bzw. friedrich_<stufe>_wear-<teil>-<frame>.png
NAME = re.compile(r"^friedrich_(%s)_(%s|wear-[a-z0-9_]+(?:-(?:%s))?)\.png$" % ("|".join(STAGES), "|".join(POSES), "|".join(POSES)))

def check(im):
    notes, ok = [], True
    if im.mode != "RGBA" or im.getchannel("A").getextrema()[0] == 255:
        notes.append("FEHLER: kein transparenter Hintergrund"); ok = False
    w, h = im.size
    if w != h: notes.append(f"FEHLER: nicht quadratisch ({w}x{h})"); ok = False
    if min(w, h) < 1024: notes.append(f"FEHLER: zu klein ({w}x{h}), mindestens 1024 px"); ok = False
    if im.mode == "RGBA":
        bbox = im.getchannel("A").point(lambda a: 255 if a > 24 else 0).getbbox()
        if bbox:
            fh = (bbox[3] - bbox[1]) / h * 100
            cx = ((bbox[0] + bbox[2]) / 2) / w * 100
            notes.append(f"Figurhöhe {fh:.0f} % (Ziel 80 %), Mitte bei {cx:.0f} % (Ziel 50 %)")
            if not 72 <= fh <= 88: notes.append("HINWEIS: Figurhöhe weicht deutlich von 80 % ab")
            if not 44 <= cx <= 56: notes.append("HINWEIS: Figur nicht mittig")
            if bbox[1] < h * .04 or bbox[3] > h * .96: notes.append("HINWEIS: Figur zu nah am Bildrand")
    return ok, notes

def main():
    src = sys.argv[1]
    repo = sys.argv[sys.argv.index("--repo") + 1] if "--repo" in sys.argv else "."
    assets = os.path.join(repo, "beta", "assets", "friedrich")
    man_path = os.path.join(assets, "manifest.json")
    man = json.load(open(man_path)) if os.path.exists(man_path) else {"version": 1, "files": {}}
    done = 0
    for fn in sorted(os.listdir(src)):
        m = NAME.match(fn)
        if not m:
            if fn.lower().endswith(".png"): print(f"übersprungen (Name passt nicht): {fn}")
            continue
        stage, pose = m.groups()
        im = Image.open(os.path.join(src, fn)); im.load()
        if im.mode != "RGBA": im = im.convert("RGBA") if "A" in im.getbands() or im.mode == "P" else im
        ok, notes = check(im)
        if pose.startswith("wear-"):   # nur das Kleidungsstück: Höhe/Mitte der Figur nicht prüfen
            notes = [n for n in notes if n.startswith("FEHLER")]; ok = not notes
        print(f"{fn}: " + ("OK" if ok else "ABGELEHNT")); [print("   " + n) for n in notes]
        if not ok: continue
        os.makedirs(os.path.join(repo, "art-source", "friedrich", stage), exist_ok=True)
        shutil.copy(os.path.join(src, fn), os.path.join(repo, "art-source", "friedrich", stage, f"{pose}.png"))
        os.makedirs(os.path.join(assets, stage), exist_ok=True)
        for size, suffix in [(1024, ""), (512, "-512")]:
            im.resize((size, size), Image.LANCZOS).save(os.path.join(assets, stage, f"{pose}{suffix}.webp"), "WEBP", quality=88, method=6)
        man["files"][f"{stage}/{pose}"] = {"w": 1024, "h": 1024, "src": fn}
        done += 1
    if done:
        man["version"] = man.get("version", 1) + 1
        json.dump(man, open(man_path, "w"), indent=1, ensure_ascii=False)
    print(f"{done} Bild(er) übernommen, Manifest-Version {man['version']}")

if __name__ == "__main__":
    main()
