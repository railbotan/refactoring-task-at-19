from PIL import Image
import numpy as np
from numpy import ndarray

class CreateImage:
    def __init__(self, image_data: ndarray, size: int, level: int):
        self.data = image_data
        self.size = size
        self.step = int(255 / level)

    def get_color(self, start_x, start_y):
        summa_color = 0
        for x in range(start_x, start_x + self.size):
            for y in range(start_y, start_y + self.size):
                pixel = self.data[x][y]
                color = pixel.sum() / 3
                summa_color += color
        summa_color = int(summa_color // self.size ** 2)
        return summa_color

    def create_image(self):
        height = len(self.data)
        width = len(self.data[1])
        for i in range(0, height, 10):
            for j in range(0, width, 10):
                summa_color = self.get_color(i, j)
                self.gradation(summa_color, i, j)
        return Image.fromarray(self.data)

    def gradation(self, summa_color, i, j):
        for x in range(i, i + self.size):
            for y in range(j, j + self.size):
                self.data[x][y][0] = int(summa_color // self.step) * self.step
                self.data[x][y][1] = int(summa_color // self.step) * self.step
                self.data[x][y][2] = int(summa_color // self.step) * self.step

img = Image.open("img2.jpg")
image = np.array(img)

results = CreateImage(image, 10, 5).create_image()
results.save('res.jpg')