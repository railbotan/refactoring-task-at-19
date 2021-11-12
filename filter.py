from PIL import Image
import numpy as np


class GrayMosaicFilter:
    def apply_filter(self, image_name, mosaic_size, gradation):
        self.mosaic_size = mosaic_size
        self.gradation = 255 // gradation
        self.image_array = np.array(Image.open(image_name))

        height = len(self.image_array)
        width = len(self.image_array[1])
        for image_y in range(0, height, self.mosaic_size):
            for image_x in range(0, width, self.mosaic_size):
                brightness_average = self._get_brightness_average(image_x, image_y)
                self._set_pixel_color(image_x, image_y, brightness_average)
        return self.image_array

    def _get_brightness_average(self, x, y):
        brightness_average = 0
        for area_y in range(y, y + self.mosaic_size):
            for area_x in range(x, x + self.mosaic_size):
                pixel_average = sum(list(map(int, self.image_array[area_y][area_x]))) / 3
                brightness_average += pixel_average
        return int(brightness_average // self.mosaic_size ** 2)

    def _set_pixel_color(self, x, y, average):
        for area_y in range(y, y + self.mosaic_size):
            for area_x in range(x, x + self.mosaic_size):
                self.image_array[area_y][area_x] = [int(average // self.gradation) * self.gradation] * 3


if __name__ == "__main__":
    filtered_array = GrayMosaicFilter().apply_filter("img2.jpg", 10, 5)
    result_image = Image.fromarray(filtered_array)
    result_image.save('res.jpg')
