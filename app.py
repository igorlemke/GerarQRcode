import qrcode

#item que estara embutido no qrcode
url = 'www.cwi.com.br'

#criar o objeto do qrcode
qr = qrcode.QRCode(
       version=1,
       box_size=4,
       border=5
)

qr.add_data(url)
qr.make(fit=True)

#criar a imagem com o qrcode
img = qr.make_image(fill='black', back_color='white')
img.show()