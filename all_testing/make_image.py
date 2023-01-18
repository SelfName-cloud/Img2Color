from PIL import Image, ImageDraw, ImageFont
import sys


def pixelate(image, pixel_size=9, draw_margin=True):
    margin_color = (0, 0, 0)

    image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
    image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)
    pixel = image.load()


    # Draw black margin between pixels
    if draw_margin:
        for i in range(0, image.size[0], pixel_size):
            for j in range(0, image.size[1], pixel_size):
                for r in range(pixel_size):
                    pixel[i+r, j] = margin_color
                    pixel[i, j+r] = margin_color

    return image


path = r'/images_colors/output.jpg'

image = Image.open(path)

new_image = Image.new('RGB', image.size, (255, 255, 255))

img_pixelate = pixelate(new_image, pixel_size=20)

draw = ImageDraw.Draw(img_pixelate)
text = '11'
font = ImageFont.truetype("arial.ttf", size=18)
#draw.text((200, 200), text, font=font, fill='black')

pixel_size = 20
for i in range(0, image.size[0], pixel_size):
    for j in range(0, image.size[1], pixel_size):
        draw.text((i, j), text, font=font, fill='black')


img_pixelate.save('img_pixelate_number.jpg')

