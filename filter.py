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
        for x in range(0, width, self.size):
            for y in range(0, height, self.size):
                average_color = self._get_average_color(x, y)
                self._set_gradation(average_color, x, y)
        return Image.fromarray(self.data)

    def _get_average_color(self, start_x, start_y):
        average_color_sum = self.data[start_x:start_x + self.size,
                                      start_y:start_y + self.size].sum() / 3
        average_color = int(average_color_sum // self.size ** 2)
        return average_color

    def _set_gradation(self, color, start_x, start_y):
        self.data[start_x:start_x + self.size,
                  start_y:start_y + self.size] = int(color // self.step) * self.step


img = Image.open("img2.jpg")
image = np.array(img)

result = ImageProcessor(image, 10, 5).process_image()
result.save('res.jpg')
