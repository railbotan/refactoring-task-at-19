from PIL import Image
import numpy as np
from numpy import ndarray

class CreateImage:
    def __init__(self, image_data: ndarray, size: int, level: int):
        self.data = image_data
        self.size = size
        self.step = int(255 / level)

    def get_color(self, start_x, start_y):
        summa_color = self.data[start_x:start_x + self.size, start_y:start_y + self.size].sum() / 3
        color = int(summa_color // self.size ** 2)
        return color

    def create_image(self):
        height = len(self.data)
        width = len(self.data[1])
        for x in range(0, width, self.size):
            for y in range(0, height, self.size):
                color = self.get_color(x, y)
                self.gradation(color, x, y)
        return Image.fromarray(self.data)

def gradation(self, color, start_x, start_y):
    self.data[start_x:start_x + self.size,
      start_y:start_y + self.size] = int(color // self.step) * self.step

img = Image.open("img2.jpg")
image = np.array(img)

results = CreateImage(image, 10, 5).create_image()
results.save('res.jpg')