"""Shared helpers: asset paths, fonts, text sanitizing for PIL/ffmpeg."""
import glob
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "assets")
OUTBOX = os.path.join(BASE, "outbox")

PHONE_DISPLAY = "90263 99218"
WA_LINK = "https://wa.me/919026399218"

IMAGES = {
    "oud_rose":  os.path.join(ASSETS, "oud-rose.jpg"),
    "good_vibe": os.path.join(ASSETS, "good-vibe.jpg"),
    "all_mine":  os.path.join(ASSETS, "all-mine.jpg"),
    "combo":     os.path.join(ASSETS, "combo-poster.jpg"),
    "craft":     os.path.join(ASSETS, "craft.jpg"),
    "bg_rose":   os.path.join(ASSETS, "bg_rose.jpg"),
    "bg_smoke":  os.path.join(ASSETS, "bg_smoke.jpg"),
    "bg_festive": os.path.join(ASSETS, "bg_festive.jpg"),
}

GOLD = (212, 164, 55)
GOLD_LIGHT = (240, 212, 136)
CREAM = (247, 241, 229)
DARK = (12, 10, 7)


def find_font(bold=True, serif=True):
    """Find a usable TTF font, preferring DejaVu."""
    if serif and bold:
        cands = ["DejaVuSerif-Bold.ttf", "DejaVuSerifCondensed-Bold.ttf",
                 "DejaVuSans-Bold.ttf", "NotoSerif-Bold.ttf"]
    elif serif:
        cands = ["DejaVuSerif.ttf", "DejaVuSerifCondensed.ttf", "DejaVuSans.ttf"]
    elif bold:
        cands = ["DejaVuSans-Bold.ttf", "DejaVuSansCondensed-Bold.ttf", "DejaVuSerif-Bold.ttf"]
    else:
        cands = ["DejaVuSans.ttf", "DejaVuSansCondensed.ttf"]
    for c in cands:
        for p in glob.glob(f"/usr/share/fonts/**/{c}", recursive=True):
            return p
        for p in glob.glob(f"/usr/local/share/fonts/**/{c}", recursive=True):
            return p
    return None


def clean_for_image(text):
    """Strip emojis/symbols that PIL/ffmpeg fonts can't render."""
    text = (text or "").strip()
    # keep basic latin, numbers and common punctuation
    text = re.sub(r"[^\x20-\x7E]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def escape_drawtext(text):
    """Escape text for ffmpeg drawtext filter."""
    t = clean_for_image(text)
    t = t.replace("\\", "\\\\").replace("'", "\\'").replace(":", "\\:").replace("%", "%%")
    return t
