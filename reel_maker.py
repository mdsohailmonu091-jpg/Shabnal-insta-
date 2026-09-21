"""Reel maker: 1080x1920 vertical video with slow zoom + styled text overlays.

Frames are rendered with PIL (brand-styled text, no ffmpeg drawtext needed),
then encoded to H.264 with ffmpeg (system or imageio-ffmpeg binary).
"""
import os
import shutil
import subprocess
import tempfile
from PIL import Image, ImageDraw, ImageFont
from common import IMAGES, GOLD_LIGHT, find_font, clean_for_image

W, H, FPS = 1080, 1920, 30


def find_ffmpeg():
    p = shutil.which("ffmpeg")
    if p:
        return p
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def _run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"ffmpeg failed:\nCMD: {' '.join(cmd)}\n{r.stderr[-2000:]}")
    return r


def _font(bold, size):
    path = find_font(bold=bold, serif=False)
    try:
        if path:
            return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default(size=size)


def _cover(img, tw, th):
    w, h = img.size
    scale = max(tw / w, th / h)
    img = img.resize((int(w * scale) + 1, int(h * scale) + 1), Image.BICUBIC)
    x = (img.width - tw) // 2
    y = (img.height - th) // 2
    return img.crop((x, y, x + tw, y + th))


def _fit_font(text, start_size, max_w, bold):
    size = start_size
    f = _font(bold, size)
    tmp = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    while size > 24 and tmp.textlength(text, font=f) > max_w:
        size -= 4
        f = _font(bold, size)
    return f


def _text_overlay(title, sub):
    """Pre-rendered centered text card (same for all frames of a scene)."""
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    fb = _fit_font(title, 62, 920, True)
    fr = _fit_font(sub, 40, 920, False)
    tw = max(d.textlength(title, font=fb), d.textlength(sub, font=fr))
    box_w = int(tw + 120)
    box_h = 210
    x0 = (W - box_w) // 2
    y0 = int(H * 0.60)
    d.rounded_rectangle([x0, y0, x0 + box_w, y0 + box_h], radius=28,
                        fill=(8, 6, 3, 165), outline=(212, 164, 55, 220), width=3)
    d.text((W / 2, y0 + 34), title, font=fb, fill=(255, 255, 255, 255), anchor="ma")
    d.text((W / 2, y0 + 118), sub, font=fr, fill=GOLD_LIGHT + (255,), anchor="ma")
    return ov


def _vignette():
    """Top + bottom cinematic darkening."""
    g = Image.new("L", (W, H), 0)
    gd = ImageDraw.Draw(g)
    for y in range(H):
        t = y / H
        if t < 0.35:
            a = int(110 * (1 - t / 0.35))
        elif t > 0.55:
            a = int(140 * ((t - 0.55) / 0.45))
        else:
            a = 0
        gd.line([(0, y), (W, y)], fill=a)
    black = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    black.putalpha(g)
    return black


def build_reel(scenes, out_path, dur_per_scene=5):
    """scenes: list of {img, text, sub}. Returns out_path."""
    ffmpeg = find_ffmpeg()
    if not ffmpeg:
        raise RuntimeError("ffmpeg not found. Install: pip install imageio-ffmpeg")

    tmp = tempfile.mkdtemp(prefix="reel_")
    vig = _vignette()
    per = dur_per_scene * FPS
    idx = 0
    for sc in scenes:
        src = Image.open(IMAGES.get(sc["img"], IMAGES["oud_rose"])).convert("RGB")
        base = _cover(src, 1350, 2400)
        bw, bh = base.size
        txt = _text_overlay(clean_for_image(sc.get("text", "")),
                            clean_for_image(sc.get("sub", "")))
        for f in range(per):
            z = 1.25 + 0.125 * (f / max(1, per - 1))  # slow zoom in
            ww, hh = int(bw / z), int(bh / z)
            x, y = (bw - ww) // 2, (bh - hh) // 2
            frame = base.crop((x, y, x + ww, y + hh)).resize((W, H), Image.BICUBIC)
            frame = frame.convert("RGBA")
            frame = Image.alpha_composite(frame, vig)
            frame = Image.alpha_composite(frame, txt)
            frame.convert("RGB").save(os.path.join(tmp, f"fr_{idx:04d}.jpg"), quality=87)
            idx += 1

    silent = os.path.join(tmp, "silent.mp4")
    _run([ffmpeg, "-y", "-framerate", str(FPS), "-i", os.path.join(tmp, "fr_%04d.jpg"),
          "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "veryfast", "-crf", "21",
          silent])

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    _run([ffmpeg, "-y", "-i", silent, "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
          "-shortest", "-c:v", "copy", "-c:a", "aac", "-movflags", "+faststart", out_path])

    shutil.rmtree(tmp, ignore_errors=True)
    return out_path


if __name__ == "__main__":
    build_reel([
        {"img": "oud_rose", "text": "OUD ROSE", "sub": "Eternal Romance"},
        {"img": "bg_rose", "text": "Shahi Oud + Gulab", "sub": "Royal blend"},
        {"img": "combo", "text": "DM to Order", "sub": "WhatsApp 90263 99218"},
    ], "outbox/test_reel.mp4")
    print("saved outbox/test_reel.mp4")
