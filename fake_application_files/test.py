from PIL import Image, ImageDraw, ImageFont

image = Image.open("origin.png")  # 把Image对象实例为image，传入原始图片
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font="苹方.ttf", size=48)

draw.text((55, 40), "10:02", font=font, fill="green")
image.show()
