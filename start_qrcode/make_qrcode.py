import hashlib
import sys
import time

import qrcode


def generate_qr_code(url, file_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(file_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python make_qrcode.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    timestamp = str(time.time()).encode("utf-8")
    file_name = hashlib.md5(timestamp).hexdigest() + ".png"
    generate_qr_code(url, file_name)
    print(f"QR code saved as {file_name}")
