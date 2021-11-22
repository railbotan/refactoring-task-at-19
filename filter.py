from PIL import Image
import numpy as np


class MosaicGenerator:
    def __init__(self, gradation=6, step=10):
        self.gradation = 255 / gradation
        self.step = 10

    def get_pixel_color(self, pixel_arr, i, j):
        colors_sum = 0
        for n in range(i, i + self.step):
            for m in range(j, j + self.step):
                r = pixel_arr[n][m][0]
                g = pixel_arr[n][m][1]
                b = pixel_arr[n][m][2]
                M = int(r) + int(g) + int(b)
                colors_sum += M
        return colors_sum // (10 * self.step)

    def set_pixel_color(self, pixel_arr, i, j, color_sum):
        for n in range(i, i + self.step):
            for m in range(j, j + self.step):
                pixel_arr[n][m][0] = int(color_sum // self.gradation) * self.gradation / 3
                pixel_arr[n][m][1] = int(color_sum // self.gradation) * self.gradation / 3
                pixel_arr[n][m][2] = int(color_sum // self.gradation) * self.gradation / 3
        return pixel_arr

    def generate_mosaic(self, img):
        pixel_arr = np.array(img)
        h, w = len(pixel_arr), len(pixel_arr[1])
        for i in range(0, h, self.step):
            for j in range(0, w, self.step):
                color_sum = self.get_pixel_color(pixel_arr, i, j)
                pixel_arr = self.set_pixel_color(pixel_arr, i, j, color_sum)
        return Image.fromarray(pixel_arr)


img = Image.open("img2.jpg")
generator = MosaicGenerator(gradation = 4)
res = generator.generate_mosaic(img)
res.save('res.jpg')