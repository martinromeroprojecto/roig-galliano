#!/usr/bin/env python3
"""Genera og-image.jpg (1200x630) — diseño Roig · Gallano.
Fondo oscuro con glow esmeralda + headline + subtítulo + pill de precio."""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BASE = (10, 15, 13)
EMER = (0, 232, 154)
WHITE = (245, 247, 246)
GRAY = (139, 148, 145)
INK = (8, 13, 11)

FONT = "/Users/martinromero/Library/Fonts/Inter-VariableFont_opsz,wght.ttf"

def f(size, name="Bold"):
    ft = ImageFont.truetype(FONT, size)
    try:
        ft.set_variation_by_name(name)
    except Exception:
        pass
    return ft

# ---- fondo con glow esmeralda (radial elíptico, centro a la derecha) ----
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
cx, cy, rx, ry = 1060.0, 300.0, 760.0, 560.0
nx = (xx - cx) / rx
ny = (yy - cy) / ry
d = np.sqrt(nx * nx + ny * ny)
inten = np.clip(1.0 - d, 0.0, 1.0) ** 1.7
add = np.stack([
    inten * 6.0,    # R
    inten * 58.0,   # G
    inten * 43.0,   # B
], axis=-1)
img = np.array(BASE, dtype=np.float32)[None, None, :] + add
# segundo glow tenue arriba-derecha para profundidad
d2 = np.sqrt(((xx - 1120) / 520) ** 2 + ((yy - 120) / 360) ** 2)
inten2 = np.clip(1.0 - d2, 0.0, 1.0) ** 2.4
img[..., 1] += inten2 * 20.0
img[..., 2] += inten2 * 15.0
img = np.clip(img, 0, 255).astype(np.uint8)
im = Image.fromarray(img, "RGB")
dr = ImageDraw.Draw(im)

PADX = 64

# ---- kicker "ROIG · GALLANO" con tracking ----
kick = f(30, "Bold")
tracking = 6
x = PADX
ky = 64
for ch in "ROIG · GALLANO":
    dr.text((x, ky), ch, font=kick, fill=EMER)
    w = dr.textlength(ch, font=kick)
    x += w + tracking

# ---- headline 2 líneas ----
head = f(96, "Bold")
dr.text((PADX, 156), "Importá desde China", font=head, fill=WHITE)
dr.text((PADX, 266), "sin perder margen.", font=head, fill=WHITE)

# ---- subtítulo ----
sub = f(33, "Medium")
dr.text((PADX, 398), "90 minutos por Zoom en vivo · con Bauti (Miami) y Ema (Shanghai)",
        font=sub, fill=GRAY)

# ---- pill de precio ----
pill = f(30, "Bold")
ptxt = "ARS 97.000 · 3 cuotas sin interés"
tb = dr.textbbox((0, 0), ptxt, font=pill)
tw, th = tb[2] - tb[0], tb[3] - tb[1]
px0, py0 = PADX, 478
padh, padv = 28, 18
px1 = px0 + tw + padh * 2
py1 = py0 + th + padv * 2
dr.rounded_rectangle([px0, py0, px1, py1], radius=(py1 - py0) // 2, fill=EMER)
dr.text((px0 + padh - tb[0], py0 + padv - tb[1]), ptxt, font=pill, fill=INK)

out = sys.argv[1] if len(sys.argv) > 1 else "og-image.jpg"
im.save(out, "JPEG", quality=88, optimize=True)
print("escrito:", out, im.size)
