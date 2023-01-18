from PIL import Image
from PIL import ImageDraw


def pixelate(image, pixel_size=9, draw_margin=True):
    margin_color = (0, 0, 0)

    image = image.resize((image.size[0] // pixel_size, image.size[1] // pixel_size), Image.NEAREST)
    image = image.resize((image.size[0] * pixel_size, image.size[1] * pixel_size), Image.NEAREST)
    pixel = image.load()

    color_dict = {}
    # Draw black margin between pixels
    if draw_margin:
        for i in range(0, image.size[0], pixel_size):
            for j in range(0, image.size[1], pixel_size):
                for r in range(pixel_size):
                    pixel[i+r, j] = margin_color
                    pixel[i, j+r] = margin_color

    return image

path = r'/images_colors/image_thrashold0.png'

image = Image.open(path).convert('RGB')

image_pixelate = pixelate(image, pixel_size=20)
image_pixelate.save('output.jpg')

#for size in (8, 16, 32, 48):
 #   image_pixelate = pixelate(image, pixel_size=size)
  #  image_pixelate.save('image/output_{}.jpg'.format(size))

