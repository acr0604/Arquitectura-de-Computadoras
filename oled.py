from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time
i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)
disp.fill(0)
disp.show()
#image = Image.new('1', (128, 64))
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
#draw.rectangle((0,0,width,height), outline=0, fill=0)
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()
#raw.text((30, 16), 'Oskar Villa', font=font, fill=255)
draw.line((40, 10, 50, 10), fill=255)
draw.line((36, 11, 54, 11), fill=255)
draw.line((33, 12, 57, 12), fill=255)
draw.line((31, 13, 59, 13), fill=255)
draw.line((29, 14, 61, 14), fill=255)
draw.line((28, 15, 62, 15), fill=255)
draw.line((26, 16, 64, 16), fill=255)
draw.line((25, 17, 65, 17), fill=255)
draw.line((24, 18, 66, 18), fill=255)
draw.line((23, 19, 67, 19), fill=255)
draw.line((22, 20, 68, 20), fill=255)
draw.line((21, 21, 69, 21), fill=255, width=2)
draw.line((20, 22, 70, 22), fill=255)
draw.line((19, 24, 71, 24), fill=255, width=3)
draw.line((18, 26, 72, 26), fill=255, width=3)
draw.line((17, 29, 73, 29), fill=255, width=3)
draw.line((16, 35, 74, 35), fill=255, width=10)
draw.line((17, 41, 73, 41), fill=255, width=3)
draw.line((18, 44, 72, 44), fill=255, width=3)
draw.line((19, 47, 71, 47), fill=255, width=3)
draw.line((20, 49, 70, 49), fill=255)
draw.line((21, 50, 69, 50), fill=255, width=2)
draw.line((22, 51, 68, 51), fill=255)
draw.line((23, 52, 67, 52), fill=255)
draw.line((24, 53, 66, 53), fill=255)
draw.line((25, 54, 65, 54), fill=255)
draw.line((26, 55, 64, 55), fill=255)
draw.line((28, 56, 62, 56), fill=255)
draw.line((29, 57, 61, 57), fill=255)
draw.line((31, 58, 59, 58), fill=255)
draw.line((33, 59, 57, 59), fill=255)
draw.line((36, 60, 54, 60), fill=255)
draw.line((40, 61, 50, 61), fill=255)
draw.line((40, 61, 50, 61), fill=0, width=12)
draw.line((31, 55, 60, 55), fill=0)
draw.line((28, 54, 63, 54), fill=0)
draw.line((26, 53, 65, 53), fill=0,width=2)
draw.line((25, 51, 66, 51), fill=0,width=2)
draw.line((25, 49, 66, 49), fill=0,width=2)



draw.line((55, 46, 58, 46), fill=0,width=2)
draw.line((45, 46, 48, 46), fill=0,width=2)
draw.line((35, 46, 38, 46), fill=0,width=2)

draw.line((54, 44, 59, 44), fill=0,width=2)
draw.line((44, 44, 49, 44), fill=0,width=2)
draw.line((34, 44, 39, 44), fill=0,width=2)

draw.line((57, 42, 60, 42), fill=0,width=4)
draw.line((47, 42, 50, 42), fill=0,width=4)
draw.line((37, 42, 40, 42), fill=0,width=4)

draw.line((54, 38, 57, 38), fill=0,width=5)
draw.line((44, 38, 47, 38), fill=0,width=5)
draw.line((34, 38, 37, 38), fill=0,width=5)
draw.line((28, 38, 30, 38), fill=0,width=5)
draw.line((22, 38, 24, 38), fill=0,width=5)

draw.line((57, 33, 59, 33), fill=0,width=4)
draw.line((47, 33, 49, 33), fill=0,width=4)
draw.line((37, 33, 39, 33), fill=0,width=4)
draw.line((48, 31, 50, 31), fill=0,width=4)
draw.line((38, 31, 40, 31), fill=0,width=4)
draw.line((39, 29, 41, 29), fill=0,width=2)

draw.line((30, 33, 32, 33), fill=0,width=7)
draw.line((24, 33, 26, 33), fill=0,width=7)

draw.line((32, 28, 34, 28), fill=0,width=3)
draw.line((26, 28, 28, 28), fill=0,width=3)



draw.text((80, 20), 'Alberto', font=font, fill=255)
draw.text((80, 30), 'Chavez', font=font, fill=255)
draw.text((80, 40), 'Rojas', font=font, fill=255)
# Muestra Texto
disp.image(image)
disp.show()

