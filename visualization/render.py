"""Render a rotating illustration of the manuscript's affine example."""
from math import cos, radians, sin
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
BACKGROUND = "#172736"
PALE = "#e5ecf3"
CYAN = "#78ead9"
GOLD = "#ffc883"
BIG = ImageFont.load_default(size=25)
NORMAL = ImageFont.load_default(size=18)
LABELS = ("z", "a", "b", "w")


def render(degrees):
    image = Image.new("RGB", (640, 522), BACKGROUND)
    draw = ImageDraw.Draw(image)
    angle = radians(degrees)
    c, s = cos(angle), sin(angle)

    def project(point, middle):
        x, y = point
        return 320 + 29 * (x * c - y * s), middle + 13.63 * (x * s + y * c)

    def panel(stretch, middle, prime):
        edge = max(2, stretch)
        grid = [(-edge, -1.6), (edge, -1.6), (edge, 1.6), (-edge, 1.6), (-edge, -1.6)]
        draw.line([project(point, middle) for point in grid], fill="#486074")
        z, a, b, w = [project(point, middle) for point in
                      [(0, 0), (stretch, 0), (0, 1), (-stretch, -1)]]
        draw.line([z, a, b], fill=CYAN, width=4, joint="curve")
        draw.line([z, w, b], fill=GOLD, width=4, joint="curve")
        for i in range(0, 10, 2):
            x0, y0 = (z[k] + i / 10 * (b[k] - z[k]) for k in range(2))
            x1, y1 = (z[k] + (i + 1) / 10 * (b[k] - z[k]) for k in range(2))
            draw.line([(x0, y0), (x1, y1)], fill=PALE, width=2)
        for i, ((x, y), label) in enumerate(zip([z, a, b, w], LABELS)):
            draw.ellipse((x-4, y-4, x+4, y+4), fill=PALE)
            offset = [(-13, 15), (8, 3), (8, -24), (-16, -25)][i]
            draw.text((x+offset[0], y+offset[1]), label + ("'" if prime else ""),
                      font=NORMAL, fill=PALE, stroke_width=1, stroke_fill=BACKGROUND)

    draw.text((22, 17), "Two arcs, one short chord", fill=PALE, font=BIG)
    draw.text((22, 63), "SOURCE   |a - z| = |b - z| = 1", fill=PALE, font=NORMAL)
    draw.text((22, 216), "IMAGE   Horizontal stretch: 8x", fill=PALE, font=NORMAL)
    draw.text((22, 488), "Chord length: 1   ·   Arc diameters: at least 8", fill=PALE, font=NORMAL)
    panel(1, 149, False)
    panel(8, 354, True)
    return image


frames = [render(degree) for degree in range(14, 374, 6)]
frames[0].save(ROOT / "construction.gif", save_all=True, append_images=frames[1:],
               duration=85, loop=0, optimize=True)
