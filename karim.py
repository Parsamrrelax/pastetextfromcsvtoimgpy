import csv

from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("w.ttf", size=55)


with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    i = 0
    for [message] in reader:
        i += 1
        img = Image.open('1.jpg')

        imgDraw = ImageDraw.Draw(img)

        textWidth, textHeight = imgDraw.textsize(message, font=font)
# change the value infront of imgdraw.text to move the text
        imgDraw.text((175,180), message, font=font, fill=(0, 0, 0))

        img.save(f'result{i}.png')
