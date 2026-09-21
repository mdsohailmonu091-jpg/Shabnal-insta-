"""Instagram post designer (1080x1350, 4:5) - Shabnal gold/black theme. PIL only."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from common import IMAGES, GOLD, GOLD_LIGHT, CREAM, find_font, clean_for_image

W, H = 1080, 1350


def _font(serif, bold, size):
    path = find_font(bold=bold, serif=serif)
    try:
        if path:
            return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default(size=size)


def _cover(img, tw, th):
    """Resize + center-crop to fill tw x th."""
    w, h = img.size
    scale = max(tw / w, th / h)
    img = img.resize((int(w * scale) + 1, int(h * scale) + 1), Image.LANCZOS)
    x = (img.width - tw) // 2
    y = (img.height - th) // 2
    return img.crop((x, y, x + tw, y + th))


def _rounded(img, radius):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, img.width, img.height], radius=radius, fill=255)
    out = img.convert("RGBA")
    out.putalpha(mask)
    return out


def _gradient_bg():
    top = (10, 8, 5)
    mid = (32, 24, 10)
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / H
        if t < 0.5:
            k = t / 0.5
            c = tuple(int(top[i] + (mid[i] - top[i]) * k) for i in range(3))
        else:
            k = (t - 0.5) / 0.5
            c = tuple(int(mid[i] + (top[i] - mid[i]) * k) for i in range(3))
        for x in range(W):
            px[x, y] = c
    return img


def _center_text(draw, cx, y, text, font, fill, spacing=6):
    draw.text((cx, y), text, font=font, fill=fill, anchor="ma", spacing=spacing)


def _spaced(draw, cx, y, text, font, fill, gap=8):
    """Draw letterspaced text centered at cx."""
    widths = [draw.textlength(ch, font=font) for ch in text]
    total = sum(widths) + gap * (len(text) - 1)
    x = cx - total / 2
    for ch, wch in zip(text, widths):
        draw.text((x, y), ch, font=font, fill=fill, anchor="la")
        x += wch + gap


def _wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def build_post(product_key, hook, sub, cta_phone="DM / WhatsApp: 90263 99218",
               tagline="EXTRAIT DE PARFUM - LONG LASTING", out_path=None):
    hook = clean_for_image(hook)
    sub = clean_for_image(sub)

    base = _gradient_bg().convert("RGBA")

    # soft golden glow circle behind product
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W // 2 - 430, 160, W // 2 + 430, 1060], fill=(212, 164, 55, 38))
    glow = glow.filter(ImageFilter.GaussianBlur(60))
    base = Image.alpha_composite(base, glow)

    draw = ImageDraw.Draw(base)

    # double gold frame
    draw.rectangle([22, 22, W - 22, H - 22], outline=GOLD + (255,), width=5)
    draw.rectangle([40, 40, W - 40, H - 40], outline=GOLD + (140,), width=2)

    # brand header
    f_brand = _font(serif=True, bold=True, size=52)
    f_brand2 = _font(serif=False, bold=False, size=24)
    _spaced(draw, W // 2, 66, "SHABNAL", f_brand, GOLD_LIGHT + (255,), gap=14)
    _spaced(draw, W // 2, 132, "P E R F U M E S", f_brand2, (168, 156, 131, 255), gap=4)

    # diamond divider
    draw.line([W // 2 - 150, 178, W // 2 - 30, 178], fill=GOLD + (200,), width=2)
    draw.line([W // 2 + 30, 178, W // 2 + 150, 178], fill=GOLD + (200,), width=2)
    draw.polygon([(W // 2, 170), (W // 2 + 8, 178), (W // 2, 186), (W // 2 - 8, 178)], fill=GOLD + (255,))

    # product photo
    photo = Image.open(IMAGES[product_key]).convert("RGB")
    photo = _cover(photo, 880, 640)
    photo = _rounded(photo, 34)
    base.paste(photo, (100, 210), photo)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle([100, 210, 980, 850], radius=34, outline=GOLD + (255,), width=4)

    # hook + sub
    f_hook = _font(serif=True, bold=True, size=66)
    lines = _wrap(draw, hook, f_hook, 900)
    if len(lines) > 2:  # shrink if too long
        f_hook = _font(serif=True, bold=True, size=56)
        lines = _wrap(draw, hook, f_hook, 900)[:2]
    y = 878
    for ln in lines[:2]:
        _center_text(draw, W // 2, y, ln, f_hook, (255, 255, 255, 255))
        y += 76 if f_hook.size == 66 else 66

    f_sub = _font(serif=False, bold=False, size=33)
    for ln in _wrap(draw, sub, f_sub, 880)[:2]:
        _center_text(draw, W // 2, y + 2, ln, f_sub, GOLD_LIGHT + (255,))
        y += 44

    # CTA pill
    f_cta = _font(serif=False, bold=True, size=34)
    pill_w, pill_h = 700, 80
    px0, py0 = (W - pill_w) // 2, 1130
    draw.rounded_rectangle([px0, py0, px0 + pill_w, py0 + pill_h], radius=40, fill=GOLD + (255,))
    tw = draw.textlength(cta_phone, font=f_cta)
    draw.text((W // 2 - tw / 2, py0 + 20), cta_phone, font=f_cta, fill=(20, 14, 4, 255))

    # bottom tagline
    f_tag = _font(serif=False, bold=False, size=23)
    _spaced(draw, W // 2, 1236, tagline, f_tag, (168, 156, 131, 255), gap=3)

    out = base.convert("RGB")
    if out_path:
        os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
        out.save(out_path, "JPEG", quality=92)
    return out


if __name__ == "__main__":
    import sys
    key = sys.argv[1] if len(sys.argv) > 1 else "oud_rose"
    build_post(key, "OUD ROSE", "Eternal Romance - Extrait de Parfum",
               out_path="outbox/test_post.jpg")
    print("saved outbox/test_post.jpg")
