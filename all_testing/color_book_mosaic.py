import numpy as np
import sys
import cv2 as cv

from PIL import Image, ImageEnhance
from PIL import ImageFilter


class ColorBookMosaic:
    def __init__(self, img_path):
        self.img_path = img_path
        self.image = Image.open(img_path)

        if (self.image.mode != 'RGB'):
            background = Image.new("RGB", self.image.size, (255, 255, 255))
            background.paste(self.image, mask=self.image.split()[3])  # 3 is the alpha channel
            self.image = background

    def get_image_thrashold(self):

        img = cv.imread(self.img_path, 0)
        img = cv.medianBlur(img, 5)

        self.image_th1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
        self.image_th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

        for index, item in enumerate([self.image_th1, self.image_th2]):
            im = Image.fromarray(item)
            im.save('images_colors\image_thrashold_color{}.png'.format(index))

    def get_image_brake_mosaic(self):
        pass

    def get_image_thrashold_brake_mosaic(self, path_brake_img):
        pic = Image.open(path_brake_img)
        pic_img = pic.filter(ImageFilter.FIND_EDGES)
        enhancer = ImageEnhance.Contrast(pic_img)
        factor = 2
        im_output = enhancer.enhance(factor)
        outline_full = im_output.point(lambda x: 255 if x < 100 else 0)
        outline_full.save(r'images_colors\trashold_brake_mosaic.png')


if __name__ == "__main__":
    color_book_mosaic = ColorBookMosaic(r"C:\Users\ryabu\Downloads\face_paint.jpg")
    color_book_mosaic.get_image_thrashold()
    #color_book_mosaic.get_image_thrashold_brake_mosaic(r'D:\projectImg2Color\images_colors\face_mosaic.jpg')




