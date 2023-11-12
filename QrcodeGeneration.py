import qrcode
link = input('Link for QrCode:') 
data = qrcode.make(link)
data.save('Qrcode.png')

