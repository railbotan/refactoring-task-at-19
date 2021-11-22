from PIL import Image
import numpy as np


class GrayscaleFilter:
    def __init__(self, p_size, g_step):
        self.pixel_size = p_size
        self.grayscale = g_step
        self.img_arr = None

    def get_average_brightness(self, start_x, start_y):
        average = np.sum((self.img_arr[start_y: start_y + self.pixel_size, start_x: start_x + self.pixel_size])) / 3
        return int(average // (self.pixel_size * self.pixel_size))

    def set_gradation(self, start_x, start_y):
        average = self.get_average_brightness(start_x, start_y)
        gradation = int(average // self.grayscale) * self.grayscale
        self.img_arr[start_y: start_y + self.pixel_size, start_x: start_x + self.pixel_size] = gradation

    def img_convert(self, input_file_name, output_file_name):
        self.img_arr = np.array(Image.open(input_file_name))
        height = len(self.img_arr)
        width = len(self.img_arr[1])
        for y in range(0, height, self.pixel_size):
            for x in range(0, width, self.pixel_size):
                self.set_gradation(x, y)
        res = Image.fromarray(self.img_arr)
        res.save(output_file_name)


input_file_name = input("Введите имя исходного изображения: ")
output_file_name = input("Введите имя нового изображения: ")
pixel_size = int(input("Введите размер пикселей: "))
grayscale_step = int(input("Введите шаг градации серого: "))

grayscale_filter = GrayscaleFilter(pixel_size, grayscale_step)
grayscale_filter.img_convert(input_file_name, output_file_name)
