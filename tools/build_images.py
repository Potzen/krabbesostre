#!/usr/bin/env python3
"""Klargør billeder til krabbesostre.dk — beskæring, skalering, WebP."""
import os
from PIL import Image, ImageEnhance, ImageFilter

HER = os.path.dirname(os.path.abspath(__file__))
ROD = os.path.dirname(HER)
SRC = os.path.join(ROD, "src")
OUT = os.path.join(ROD, "billeder")
os.makedirs(OUT, exist_ok=True)


def crop_to_ratio(im, ratio, anchor=0.5):
    """Beskær til ratio (b/h). anchor 0..1 = hvor i den lange akse vi bevarer."""
    w, h = im.size
    target = ratio
    cur = w / h
    if abs(cur - target) < 0.001:
        return im
    if cur > target:  # for bred -> skær i bredden
        new_w = int(round(h * target))
        x = int(round((w - new_w) * anchor))
        return im.crop((x, 0, x + new_w, h))
    new_h = int(round(w / target))
    y = int(round((h - new_h) * anchor))
    return im.crop((0, y, w, y + new_h))


def process(src_name, out_name, ratio=None, width=1600, anchor=0.5,
            quality=80, sharpen=True, warmth=1.0):
    im = Image.open(os.path.join(SRC, src_name)).convert("RGB")
    if ratio:
        im = crop_to_ratio(im, ratio, anchor)
    if im.width > width:
        h = int(round(width * im.height / im.width))
        im = im.resize((width, h), Image.LANCZOS)
    if warmth != 1.0:
        im = ImageEnhance.Color(im).enhance(warmth)
    if sharpen:
        im = im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=55, threshold=3))
    path = os.path.join(OUT, out_name)
    im.save(path, "WEBP", quality=quality, method=6)
    print(f"{out_name:26s} {im.width}x{im.height}  {os.path.getsize(path)/1024:7.1f} kB")
    return im


JOBS = [
    # navn i src,                             ud,                ratio, bredde, anchor
    ("61348347-Krabberiska_l.jpg",            "hero.webp",        16/9,  2000, 0.62, 82),
    ("61348347-Krabberiska_l.jpg",            "hero-mobil.webp",  3/4,   1000, 0.30, 82),
    ("a5f04f46-caption.jpg",                  "krabbeklor.webp",  1/1,   1100, 0.50, 82),
    ("b377ee17-rejerne.png",                  "rejer.webp",       1/1,    760, 0.50, 84),
    ("cbe18eb5-719159707_2641306216328112_6298869248937728670_n.jpg",
                                              "sild.webp",        3/4,   1100, 0.50, 82),
    ("509273f7-505898624_10162078209914017_7419643288261777260_n.jpg",
                                              "sostrene.webp",    3/4,   1200, 0.50, 82),
    ("1575cb5f-120625120625krabbesostrejejr23894.webp",
                                              "bojer.webp",      16/9,   2000, 0.50, 80),
    ("241f9241-Kurvkopi.jpg",                 "kurv.webp",        3/4,   1400, 0.50, 82),
    ("241f9241-Kurvkopi.jpg",                 "kurv-bred.webp",  21/9,   2000, 0.72, 80),
    ("b148c146-510442585_17875606284361414_3180545970556545440_n.jpg",
                                              "skilt.webp",       1/1,   1100, 0.50, 82),
    ("642bc82b-urreq4626wfe5m.jpg",           "maiken.webp",      3/4,   1200, 0.50, 82),
    ("7d5f277e-bordd_kning.jpeg",             "borddaekning.webp",4/3,   1500, 0.50, 82),
    # OG-billede til deling
    ("61348347-Krabberiska_l.jpg",            "og.webp",         1.91,   1200, 0.62, 80),
]

total = 0
for src, out, ratio, width, anchor, q in JOBS:
    process(src, out, ratio, width, anchor, quality=q)
    total += os.path.getsize(os.path.join(OUT, out))
print(f"\nI alt: {total/1024/1024:.2f} MB")
