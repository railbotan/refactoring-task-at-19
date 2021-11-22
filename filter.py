from PIL import Image
import numpy as np


class MosaicGenerator:
    def __init__(self, gradation=6, step=10):
        self.gradation = 255 / gradation
        self.step = 10

    def get_pixel_color(self, pixel_arr, i, j):
        return np.sum(pixel_arr[i: i + self.step, j: j + self.step]) // (10 * self.step)

    def set_pixel_color(self, pixel_arr, i, j, color_sum):
        pixel_arr[i: i + self.step, j: j + self.step] = int(color_sum // self.gradation) * self.gradation / 3
        return pixel_arr

    def generate_mosaic(self, img):
        pixel_arr = np.array(img)
        h, w = len(pixel_arr), len(pixel_arr[1])
        for i in range(0, h, self.step):
            for j in range(0, w, self.step):
                color_sum = self.get_pixel_color(pixel_arr, i, j)
                pixel_arr = self.set_pixel_color(pixel_arr, i, j, color_sum)
        return Image.fromarray(pixel_arr)


print("Введите название файла, который вы хотите преобразовать")
inp_path = input()
print("Введите название для выходного файла")
output_path = input()
img = Image.open(inp_path)
generator = MosaicGenerator(gradation=4)
res = generator.generate_mosaic(img)
res.save(output_path)
