from PIL import Image
import numpy as np
from numpy import ndarray


class ImageProcessor:
    def __init__(self, image_data: ndarray, size: int, level: int):
        self.data = image_data
        self.size = size
        self.step = int(255 / level)

    def process_image(self):
        height = len(self.data)
        width = len(self.data[1])
        for i in range(0, height, 10):
            for j in range(0, width, 10):
                color_sum = self._get_average_color(i, j)
                self._set_gradation(color_sum, i, j)
        return Image.fromarray(self.data)

    def _get_average_color(self, start_x, start_y):
        color_sum = 0
        for x in range(start_x, start_x + self.size):
            for y in range(start_y, start_y + self.size):
                pixel = self.data[x][y]
                average_color = pixel.sum() / 3
                color_sum += average_color
        color_sum = int(color_sum // self.size ** 2)
        return color_sum

    def _set_gradation(self, color_sum, i, j):
        for x in range(i, i + self.size):
            for y in range(j, j + self.size):
                self.data[x][y][0] = int(color_sum // self.step) * self.step
                self.data[x][y][1] = int(color_sum // self.step) * self.step
                self.data[x][y][2] = int(color_sum // self.step) * self.step


img = Image.open("img2.jpg")
image = np.array(img)

result = ImageProcessor(image, 10, 5).process_image()
result.save('res.jpg')
