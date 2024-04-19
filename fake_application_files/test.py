from PIL import ImageFont, ImageDraw, Image
import qrcode
'''
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=0,
                )
qr.add_data(f"https://jjfenggg.github.io/fake_application_files/QR/test.html")
qr.make(fit=True)
qrimg = qr.make_image(fill_color="black", back_color="white")
qrimg = qrimg.resize((390, 390))
'''
image = Image.open("test.png")
#image.paste(qrimg, (446, 1418))

font = ImageFont.truetype("苹方.ttf", 48)
draw = ImageDraw.Draw(image)
draw.text((403, 410), "徐梓郡", font=font, fill="green")
draw.text((403, 483), "2022", font=font, fill="green")
draw.text((403, 915), "2024", font=font, fill="green")
image.show()


