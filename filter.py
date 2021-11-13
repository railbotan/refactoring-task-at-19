from PIL import Image
import numpy as np


class pixelArtGenerator():

    def __init__(self, gradations= 6, pixel_step = 10):
        self.step = pixel_step
        self.gradation = 255 / gradations

    def get_pixel_color(self, img_array, i, j):
        return np.sum(img_array[i: i + self.step, j: j + self.step]) // (10 * self.step)

    def set_pixel_color(self, img_array, i, j, s):
        img_array[i: i + self.step, j: j + self.step] = int(s // self.gradation) * self.gradation / 3
        return img_array 

    def generate(self, img):
        img_array = np.array(img)
        h, w = len(img_array), len(img_array[1])
        for i in range(0, h, self.step):
            for j in range(0, w, self.step):
                color = self.get_pixel_color(img_array, i, j)
                img_array = self.set_pixel_color(img_array, i, j, color)
        return Image.fromarray(img_array)


img = Image.open("img2.jpg")
generator = pixelArtGenerator(gradations = 10, pixel_step=10)
res = generator.generate(img)
res.save('res.jpg')