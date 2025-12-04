import qrcode

url = input('Enter the URL: ').strip()
file_path = '/Users/jgtrindade/Desktop/Curriculo/Python/QrCodes/linkedin.png'

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print('QRCode was generated')