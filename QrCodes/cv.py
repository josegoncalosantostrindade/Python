import qrcode
import os

pdf_path = input('Enter the local PDF file path: ').strip()
file_path = '/Users/jgtrindade/Desktop/Curriculo/Python/QrCodes/cv.png'

os.makedirs(os.path.dirname(file_path), exist_ok=True)

qr = qrcode.QRCode()
qr.add_data(pdf_path)

img = qr.make_image()
img.save(file_path)

print('QRCode for local PDF path was generated')