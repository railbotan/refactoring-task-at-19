from PIL import Image
import numpy as np


class GrayMosaicFilter:
    def apply_filter(self, image_name, mosaic_size, gradation):
        self.mosaic_size = mosaic_size
        self.gradation = 255 // gradation
        self.image_array = np.array(Image.open(image_name))

        height = len(self.image_array)
        width = len(self.image_array[1])
        for x in range(0, width, self.mosaic_size):
            for y in range(0, height, self.mosaic_size):
                brightness_average = self._get_brightness_average(x, y)
                self._set_pixel_color(x, y, brightness_average)
        return self.image_array

    def _get_brightness_average(self, x, y):
        return int(
            (self.image_array[x: x + self.mosaic_size, y: y + self.mosaic_size].sum()) / 3 // self.mosaic_size ** 2)

    def _set_pixel_color(self, x, y, average):
        self.image_array[x: x + self.mosaic_size, y: y + self.mosaic_size] = int(average // self.gradation) * \
                                                                             self.gradation


if __name__ == "__main__":
    filtered_array = GrayMosaicFilter().apply_filter("img2.jpg", 10, 5)
    result_image = Image.fromarray(filtered_array)
    result_image.save('res.jpg')
