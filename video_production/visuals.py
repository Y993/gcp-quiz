"""
visuals.py — atmospheric background + telop renderer for the 『人間失格』 videos.
All visuals are generated programmatically (PIL + numpy); no external image APIs.
Motifs: cracked smiling mask / crowd silhouettes / smartphone glow / manuscript
paper / blurred mirror — matching the script in docs/youtube-example-ningen-shikkaku.md
"""
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_PATH = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"

# ---- low-level helpers -------------------------------------------------------

def _img(size, color=(8, 9, 14)):
    return Image.new("RGB", size, color)

def vertical_gradient(size, top, bottom):
    w, h = size
    t = np.array(top, dtype=np.float32)
    b = np.array(bottom, dtype=np.float32)
    ramp = np.linspace(0, 1, h, dtype=np.float32)[:, None]
    col = (t[None, :] * (1 - ramp) + b[None, :] * ramp)  # h x 3
    arr = np.repeat(col[:, None, :], w, axis=1).astype(np.uint8)
    return Image.fromarray(arr, "RGB")

def radial_glow(size, center, radius, color, strength=1.0):
    """Return an RGB image of a soft radial glow on black (for screen-blend)."""
    w, h = size
    cx, cy = center
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / max(radius, 1)
    falloff = np.clip(1 - d, 0, 1) ** 2
    falloff *= strength
    arr = (falloff[:, :, None] * np.array(color, dtype=np.float32)[None, None, :]).astype(np.uint8)
    return Image.fromarray(arr, "RGB")

def screen_blend(base, glow):
    a = np.asarray(base, dtype=np.float32) / 255
    b = np.asarray(glow, dtype=np.float32) / 255
    out = (1 - (1 - a) * (1 - b)) * 255
    return Image.fromarray(out.astype(np.uint8), "RGB")

def vignette(img, strength=0.85):
    w, h = img.size
    yy, xx = np.mgrid[0:h, 0:w]
    cx, cy = w / 2, h / 2
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    d = d / d.max()
    mask = 1 - (d ** 2) * strength
    arr = (np.asarray(img, dtype=np.float32) * mask[:, :, None]).clip(0, 255).astype(np.uint8)
    return Image.fromarray(arr, "RGB")

def add_grain(img, amount=6):
    arr = np.asarray(img, dtype=np.int16)
    noise = np.random.normal(0, amount, arr.shape[:2])[:, :, None]
    arr = (arr + noise).clip(0, 255).astype(np.uint8)
    return Image.fromarray(arr, "RGB")

def _font(px):
    return ImageFont.truetype(FONT_PATH, px)

# ---- motif: smiling mask with a crack ---------------------------------------

def _draw_mask(draw, cx, cy, scale, crack=0.0, face=(232, 226, 214)):
    """A pale theatrical smiling mask. crack 0..1 widens a vertical fracture."""
    rx, ry = int(110 * scale), int(150 * scale)
    shadow = (max(face[0] - 60, 0), max(face[1] - 60, 0), max(face[2] - 60, 0))
    draw.ellipse([cx - rx - 6, cy - ry - 6, cx + rx + 6, cy + ry + 6], fill=shadow)
    draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=face)
    eye_dy = int(ry * 0.18)
    ew = int(rx * 0.30)
    dark = (28, 24, 30)
    for sx in (-1, 1):
        ex = cx + sx * int(rx * 0.42)
        # closed/curved eyes
        draw.arc([ex - ew, cy - eye_dy - ew, ex + ew, cy - eye_dy + ew], 200, 340, fill=dark, width=max(3, int(6 * scale)))
    # wide smile
    sw = int(rx * 0.95)
    draw.arc([cx - sw, cy + int(ry * 0.05), cx + sw, cy + int(ry * 0.75)], 20, 160, fill=dark, width=max(4, int(8 * scale)))
    # brows
    for sx in (-1, 1):
        ex = cx + sx * int(rx * 0.42)
        draw.arc([ex - ew, cy - eye_dy - ew * 2, ex + ew, cy - eye_dy], 210, 330, fill=(150, 140, 132), width=max(2, int(3 * scale)))
    if crack > 0:
        # jagged vertical fracture, widening with `crack`
        pts = []
        n = 9
        amp = 10 * scale * crack
        for i in range(n + 1):
            t = i / n
            y = int(cy - ry + t * 2 * ry)
            x = int(cx + math.sin(t * 12) * amp + (random.random() - .5) * 6 * crack)
            pts.append((x, y))
        draw.line(pts, fill=(12, 12, 16), width=max(2, int(4 * scale * (0.6 + crack))))
        # split halves separate slightly
        if crack > 0.6:
            for (x, y) in pts:
                draw.line([(x - 2, y), (x + 2, y)], fill=(40, 38, 44), width=1)

def bg_mask(size, crack=0.0, sub=0.0):
    base = vertical_gradient(size, (18, 14, 22), (6, 6, 10))
    g = radial_glow(size, (size[0] // 2, int(size[1] * 0.42)), size[1] * 0.5, (60, 48, 70), 0.5)
    base = screen_blend(base, g)
    d = ImageDraw.Draw(base)
    scale = size[1] / 1080 * 1.0
    _draw_mask(d, size[0] // 2, int(size[1] * 0.40), scale, crack=crack)
    base = vignette(base, 0.9)
    return add_grain(base)

# ---- motif: crowd silhouettes (one figure highlighted) ----------------------

def _person(draw, x, base_y, h, color):
    head_r = int(h * 0.12)
    cy = base_y - h + head_r
    draw.ellipse([x - head_r, cy - head_r, x + head_r, cy + head_r], fill=color)
    bw = int(h * 0.34)
    draw.polygon([(x - bw // 2, base_y), (x + bw // 2, base_y),
                  (x + int(bw * 0.30), cy + head_r), (x - int(bw * 0.30), cy + head_r)], fill=color)

def bg_crowd(size, highlight=True):
    base = vertical_gradient(size, (20, 22, 30), (8, 8, 12))
    d = ImageDraw.Draw(base)
    w, h = size
    random.seed(7)
    rows = [(0.78, 60, (26, 28, 38)), (0.86, 80, (18, 20, 28)), (0.96, 110, (10, 11, 16))]
    for (by, ph, col) in rows:
        y = int(h * by)
        ph2 = int(h * ph / 540)
        x = -20
        while x < w + 40:
            _person(d, x, y, ph2, col)
            x += int(ph2 * 0.55) + random.randint(-6, 10)
    if highlight:
        hx = int(w * 0.5)
        _person(d, hx, int(h * 0.94), int(h * 150 / 540), (150, 150, 158))
        g = radial_glow(size, (hx, int(h * 0.74)), h * 0.28, (40, 44, 60), 0.5)
        base = screen_blend(base, g)
    base = vignette(base, 0.85)
    return add_grain(base)

# ---- motif: smartphone glow + notifications ---------------------------------

def bg_phone(size, hearts=True):
    base = vertical_gradient(size, (10, 12, 20), (4, 4, 8))
    d = ImageDraw.Draw(base)
    w, h = size
    pw, ph = int(w * 0.16), int(h * 0.34)
    px, py = w // 2 - pw // 2, int(h * 0.40)
    glow = radial_glow(size, (w // 2, int(h * 0.57)), h * 0.5, (70, 110, 170), 0.85)
    base = screen_blend(base, glow)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=int(pw * 0.12), fill=(150, 180, 220))
    d.rounded_rectangle([px + 6, py + 6, px + pw - 6, py + ph - 6], radius=int(pw * 0.10), fill=(205, 225, 245))
    if hearts:
        random.seed(3)
        for _ in range(26):
            hx = random.randint(int(w * 0.18), int(w * 0.82))
            hy = random.randint(int(h * 0.10), int(h * 0.92))
            s = random.randint(int(h * 0.012), int(h * 0.03))
            c = random.choice([(235, 90, 110), (240, 120, 90), (235, 170, 80)])
            _heart(d, hx, hy, s, c)
    base = vignette(base, 0.8)
    return add_grain(base)

def _heart(draw, x, y, s, color):
    draw.pieslice([x - s, y - s, x, y], 0, 360, fill=color)
    draw.pieslice([x, y - s, x + s, y], 0, 360, fill=color)
    draw.polygon([(x - s, y - s // 4), (x + s, y - s // 4), (x, y + s)], fill=color)

# ---- motif: manuscript paper (原稿用紙) -------------------------------------

def bg_manuscript(size):
    base = vertical_gradient(size, (30, 26, 22), (14, 12, 10))
    d = ImageDraw.Draw(base)
    w, h = size
    paper = (212, 202, 180)
    line = (150, 80, 70)
    mx, my = int(w * 0.14), int(h * 0.12)
    pw, ph = w - mx * 2, h - my * 2
    d.rectangle([mx, my, mx + pw, my + ph], fill=paper)
    cols = 16
    cw = pw / cols
    for i in range(cols + 1):
        x = mx + i * cw
        d.line([(x, my), (x, my + ph)], fill=line, width=1)
    rows = 12
    rh = ph / rows
    for j in range(rows + 1):
        y = my + j * rh
        d.line([(mx, y), (mx + pw, y)], fill=line, width=1)
    # pen shadow diagonal
    sh = Image.new("RGB", size, (0, 0, 0))
    sd = ImageDraw.Draw(sh)
    sd.line([(int(w * 0.62), int(h * 0.20)), (int(w * 0.50), int(h * 0.85))], fill=(60, 60, 60), width=int(h * 0.02))
    sh = sh.filter(ImageFilter.GaussianBlur(18))
    base = Image.fromarray((np.asarray(base, np.float32) * 0.78 + np.asarray(sh, np.float32) * 0.5).clip(0, 255).astype(np.uint8))
    base = vignette(base, 0.7)
    return add_grain(base, 4)

# ---- motif: blurred face in a mirror ----------------------------------------

def bg_mirror(size):
    base = vertical_gradient(size, (16, 18, 24), (6, 7, 11))
    d = ImageDraw.Draw(base)
    w, h = size
    # mirror frame
    mx, my = int(w * 0.34), int(h * 0.14)
    mw, mh = int(w * 0.32), int(h * 0.66)
    d.rounded_rectangle([mx - 12, my - 12, mx + mw + 12, my + mh + 12], radius=20, fill=(40, 36, 44))
    inner = Image.new("RGB", (mw, mh), (24, 26, 34))
    idr = ImageDraw.Draw(inner)
    # vague face
    fcx, fcy = mw // 2, int(mh * 0.46)
    idr.ellipse([fcx - mw * 0.22, fcy - mh * 0.20, fcx + mw * 0.22, fcy + mh * 0.24], fill=(70, 68, 78))
    idr.ellipse([fcx - mw * 0.10, fcy - mh * 0.05, fcx - mw * 0.02, fcy + mh * 0.01], fill=(40, 40, 48))
    idr.ellipse([fcx + mw * 0.02, fcy - mh * 0.05, fcx + mw * 0.10, fcy + mh * 0.01], fill=(40, 40, 48))
    inner = inner.filter(ImageFilter.GaussianBlur(11))
    base.paste(inner, (mx, my))
    g = radial_glow(size, (mx + mw // 2, my + int(mh * 0.4)), h * 0.32, (40, 44, 58), 0.4)
    base = screen_blend(base, g)
    base = vignette(base, 0.85)
    return add_grain(base)

# ---- motif: plain atmospheric / title -------------------------------------

def bg_dark(size, tint=(30, 24, 36)):
    base = vertical_gradient(size, tint, (5, 5, 9))
    g = radial_glow(size, (size[0] // 2, int(size[1] * 0.5)), size[1] * 0.55, (40, 34, 50), 0.4)
    base = screen_blend(base, g)
    return add_grain(vignette(base, 0.8))

# ---- telop / text -----------------------------------------------------------

def _wrap(text, font, max_w, draw):
    # wrap by character (Japanese has no spaces); respect explicit \n
    out_lines = []
    for para in text.split("\n"):
        line = ""
        for ch in para:
            if draw.textlength(line + ch, font=font) <= max_w:
                line += ch
            else:
                out_lines.append(line)
                line = ch
        out_lines.append(line)
    return out_lines

def draw_text_block(img, text, *, pos="bottom", size_px=None, fill=(245, 245, 245),
                    stroke=(0, 0, 0), stroke_w=None, max_w_ratio=0.82, accent=None,
                    band=True):
    """Burn telop text onto img. pos: 'bottom'|'center'|'top'."""
    img = img.copy()
    d = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    if size_px is None:
        size_px = int(h * 0.058)
    if stroke_w is None:
        stroke_w = max(2, int(size_px * 0.10))
    font = _font(size_px)
    lines = _wrap(text, font, int(w * max_w_ratio), d)
    line_h = int(size_px * 1.34)
    block_h = line_h * len(lines)
    if pos == "bottom":
        y0 = int(h * 0.97) - block_h
    elif pos == "top":
        y0 = int(h * 0.06)
    else:
        y0 = (h - block_h) // 2
    if band:
        pad = int(size_px * 0.5)
        band_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        bd = ImageDraw.Draw(band_img)
        bd.rectangle([0, y0 - pad, w, y0 + block_h + pad], fill=(0, 0, 0, 120))
        band_img = band_img.filter(ImageFilter.GaussianBlur(6))
        img = Image.alpha_composite(img.convert("RGBA"), band_img).convert("RGB")
        d = ImageDraw.Draw(img, "RGBA")
    y = y0
    for ln in lines:
        tw = d.textlength(ln, font=font)
        x = (w - tw) // 2
        d.text((x, y), ln, font=font, fill=fill, stroke_width=stroke_w, stroke_fill=stroke)
        y += line_h
    if accent:
        # thin accent underline under the block
        d.rectangle([int(w * 0.5 - 60), y + 6, int(w * 0.5 + 60), y + 12], fill=accent)
    return img

def draw_title(img, main, sub=None, *, main_px=None, accent=(206, 60, 60)):
    img = img.copy()
    w, h = img.size
    d = ImageDraw.Draw(img, "RGBA")
    if main_px is None:
        main_px = int(h * 0.11)
    mf = _font(main_px)
    lines = _wrap(main, mf, int(w * 0.86), d)
    lh = int(main_px * 1.22)
    total = lh * len(lines)
    y = (h - total) // 2 - int(h * 0.04)
    for ln in lines:
        tw = d.textlength(ln, font=mf)
        x = (w - tw) // 2
        d.text((x, y), ln, font=mf, fill=(245, 242, 238), stroke_width=max(3, int(main_px * 0.06)), stroke_fill=(0, 0, 0))
        y += lh
    d.rectangle([w // 2 - int(w * 0.06), y + 10, w // 2 + int(w * 0.06), y + 10 + max(4, int(h * 0.006))], fill=accent)
    if sub:
        sf = _font(int(main_px * 0.42))
        tw = d.textlength(sub, font=sf)
        d.text(((w - tw) // 2, y + int(h * 0.05)), sub, font=sf, fill=(210, 205, 200),
               stroke_width=2, stroke_fill=(0, 0, 0))
    return img
