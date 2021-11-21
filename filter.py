from PIL import Image
import numpy as np
import click
from numpy import ndarray

class CreateImage:
    def __init__(self, image_data: ndarray, size: int, level: int):
        self.data = image_data
        self.size = CreateImage.check_size(size)
        self.step = int(255 / CreateImage.check_level(level))

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

@staticmethod
def check_level(level):
    if level <= 0 or level > 255:
        raise ValueError("Уровень должен быть больше 0 и меньше 255")
    else:
        return level

@staticmethod
def check_size(size):
    if size <= 0:
        raise ValueError("Размер должен быть больше нуля")
    else:
        return size

@click.command()
@click.option("-i", default="input.png", help="Введите имя исходного изображения:")
@click.option("-o", default="output.jpg", help="Закрыть изображение:")
@click.option("--size", default=10, help="Размер мозайки:")
@click.option("--level", default=5, help="Номер цвета:")

def main(i, o, size, level):
    img = Image.open(i)
    image = np.array(img)

    result = ImageProcessor(image, size, level).process_image()
    result.save(o)


if __name__ == '__main__':
    main()