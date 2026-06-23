import argparse
import io

import qrcode
import qrcode.image.svg
import cairosvg

parser = argparse.ArgumentParser()
parser.add_argument("--paper_name", type=str, required=True)
args = parser.parse_args()
paper_name = args.paper_name

url = "https://riteshharshe.github.io/papers/" + paper_name.lstrip("/") + ".pdf"

# Generate QR as SVG in memory
factory = qrcode.image.svg.SvgPathImage
img = qrcode.make(url, image_factory=factory)

svg_buffer = io.BytesIO()
img.save(svg_buffer)
svg_bytes = svg_buffer.getvalue()

# Convert SVG bytes directly to PDF
cairosvg.svg2pdf(
    bytestring=svg_bytes,
    write_to="qr_%s.pdf"%paper_name,
)