"""Build the GTA 6 DMV meme: a Vice City driver's license renewal form.

Fixed 1024x1024 flat vector poster, cream paper, dark navy and pink.
No network, no clock, no randomness, so the output bytes are deterministic.
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
CREAM = (255, 246, 232)
NAVY = (20, 33, 61)
PINK = (255, 46, 136)
MAGENTA = (233, 30, 99)
RED = (214, 32, 32)
WHITE = (255, 255, 255)
GREY = (90, 90, 110)
LIGHT = (255, 225, 238)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def star_points(cx, cy, r_outer, r_inner, points=5, rot=-90):
    pts = []
    for i in range(points * 2):
        r = r_outer if i % 2 == 0 else r_inner
        a = math.radians(rot + i * 180 / points)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def draw_ghost(draw, x, y, w, h):
    """White ghost clerk: rounded body, wavy hem, star eyes, pink badge."""
    # body: top semicircle + rectangle, wavy bottom hem
    draw.ellipse([x, y, x + w, y + w * 0.62], fill=WHITE, outline=NAVY, width=5)
    draw.rectangle([x, y + w * 0.3, x + w, y + h - 28], fill=WHITE, outline=NAVY, width=5)
    # cover the top seam line inside the body
    draw.rectangle([x + 6, y + w * 0.3, x + w - 6, y + w * 0.34], fill=WHITE)
    # wavy hem: three scallops
    hem_y = y + h - 28
    for i in range(3):
        sx = x + i * w / 3
        draw.pieslice([sx, hem_y - 14, sx + w / 3, hem_y + 28],
                      start=0, end=180, fill=WHITE, outline=NAVY, width=5)
    # star eyes
    draw.polygon(star_points(x + w * 0.32, y + h * 0.32, 26, 11), fill=NAVY)
    draw.polygon(star_points(x + w * 0.68, y + h * 0.32, 26, 11), fill=NAVY)
    # open smile
    draw.arc([x + w * 0.38, y + h * 0.44, x + w * 0.62, y + h * 0.58],
             start=10, end=170, fill=NAVY, width=5)
    # blush cheeks
    draw.ellipse([x + w * 0.16, y + h * 0.42, x + w * 0.28, y + h * 0.48], fill=PINK)
    draw.ellipse([x + w * 0.72, y + h * 0.42, x + w * 0.84, y + h * 0.48], fill=PINK)
    # pink badge with a white star, on the chest
    bx, by, br = x + w * 0.5, y + h * 0.72, 34
    draw.ellipse([bx - br, by - br, bx + br, by + br], fill=PINK, outline=NAVY, width=4)
    draw.polygon(star_points(bx, by, 22, 9), fill=WHITE)


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    # outer border
    d.rectangle([16, 16, W - 16, H - 16], outline=NAVY, width=10)

    # header: navy band
    d.rectangle([36, 36, W - 36, 196], fill=NAVY)
    d.text((512, 66), "STATE OF LEONIDA", font=font(BOLD, 26),
           fill=PINK, anchor="mt")
    d.text((512, 108), "VICE CITY DMV", font=font(BOLD, 68),
           fill=WHITE, anchor="mt")
    d.text((512, 172), "DRIVER'S LICENSE RENEWAL", font=font(BOLD, 28),
           fill=WHITE, anchor="mt")

    # form line
    d.text((60, 216), "FORM VC-6  •  RENEWAL", font=font(BOLD, 26), fill=NAVY)
    d.text((964, 216), "No. GTA-V-2013", font=font(BOLD, 26), fill=NAVY, anchor="rt")

    # license details, left column
    y = 258
    d.text((60, y), "NAME", font=font(BOLD, 22), fill=GREY)
    d.text((60, y + 26), "ONE PATIENT GAMER", font=font(BOLD, 34), fill=NAVY)
    y += 86
    d.text((60, y), "ISSUED  •  EXPIRES", font=font(BOLD, 22), fill=GREY)
    d.text((60, y + 26), "17 SEP 2013  →  19 NOV 2026", font=font(BOLD, 30), fill=NAVY)
    y += 86
    d.text((60, y), "WAIT", font=font(BOLD, 22), fill=GREY)
    d.text((60, y + 26), "4,811 DAYS  •  13 YEARS", font=font(BOLD, 34), fill=PINK)
    y += 86
    d.text((60, y), "DRIVES", font=font(BOLD, 22), fill=GREY)
    d.text((60, y + 26), "JASON & LUCIA", font=font(BOLD, 30), fill=NAVY)
    d.text((60, y + 58), "Alligator in the back seat.", font=font(REG, 24), fill=GREY)

    # ghost clerk, right column, with a caption
    draw_ghost(d, 660, 250, 280, 330)
    d.text((800, 592), "YOUR CLERK", font=font(BOLD, 22), fill=NAVY, anchor="mt")
    d.text((800, 618), "make.fun ghost", font=font(REG, 22), fill=GREY, anchor="mt")

    # itemised lines, kept compact so the TOTAL stays clear of the footer
    items = [
        ("Photo retake — aged 13 years", "$0.00"),
        ("Vision test — reads GTA VI at 214 GB", "$0.00"),
        ("Driving test in Vice City", "$0.00"),
        ("Trailer rewatches × 2,147", "$0.00"),
        ("2 delays — Fall 2025 / May 2026", "$0.00"),
        ("GTA VI — finally", "$79.99"),
    ]
    y = 652
    d.line([(60, y), (964, y)], fill=NAVY, width=4)
    y += 10
    for label, price in items:
        d.text((60, y), label, font=font(REG, 27), fill=NAVY)
        d.text((964, y), price, font=font(BOLD, 27), fill=NAVY, anchor="rt")
        y += 34
    d.line([(60, y + 4), (964, y + 4)], fill=NAVY, width=4)
    y += 14
    d.text((60, y), "TOTAL", font=font(BOLD, 36), fill=NAVY)
    d.text((964, y), "$79.99", font=font(BOLD, 40), fill=PINK, anchor="rt")

    # PAID stamp, rotated, over the $0.00 rows — never over the TOTAL
    stamp = Image.new("RGBA", (300, 130), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stamp)
    sd.rounded_rectangle([6, 6, 294, 124], radius=18, outline=RED, width=8)
    sd.text((150, 65), "PAID", font=font(BOLD, 64), fill=RED, anchor="mm")
    stamp = stamp.rotate(-14, resample=Image.BICUBIC, expand=True)
    # sits over the $0.00 rows, clear of the GTA VI price and the TOTAL
    img.paste(stamp, (620, 648), stamp)
    d = ImageDraw.Draw(img)

    # footer punchline band
    d.rectangle([36, 930, W - 36, 988], fill=NAVY)
    d.text((512, 959), "PAID BY MY AI AGENT on make.fun",
           font=font(BOLD, 30), fill=WHITE, anchor="mm")

    out = Path(__file__).resolve().parent / "meme.png"
    img.save(out, "PNG")
    print(f"saved {out} {img.size}")


if __name__ == "__main__":
    main()
