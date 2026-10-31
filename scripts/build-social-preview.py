from pathlib import Path
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets" / "aforaone-social-preview.svg"
TARGET = ROOT / "assets" / "aforaone-social-preview.png"

cairosvg.svg2png(
    url=str(SOURCE),
    write_to=str(TARGET),
    output_width=1200,
    output_height=630,
)

print(f"Generated {TARGET} (1200x630)")
