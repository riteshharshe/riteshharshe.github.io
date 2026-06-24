import io

import qrcode
import qrcode.image.svg
import cairosvg

url = "https://riteshharshe.github.io/contact.html"

# Generate QR as SVG in memory
factory = qrcode.image.svg.SvgPathImage
img = qrcode.make(url, image_factory=factory)

svg_buffer = io.BytesIO()
img.save(svg_buffer)
svg_bytes = svg_buffer.getvalue()

# Convert SVG bytes directly to PDF
cairosvg.svg2pdf(
    bytestring=svg_bytes,
    write_to="qr_contact.pdf",
)