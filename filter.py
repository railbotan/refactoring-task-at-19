from PIL import Image
import numpy as np

class pixelArtGenerator():

    def __init__(self, gradations= 6, pixel_step = 10):
        self.step = pixel_step
        self.gradation = 255 / gradations

    def get_pixel_color(self, arr, i, j):
        color_sum = 0
        for n in range(i, i + self.step):
                for m in range(j, j + self.step):
                    R = arr[n][m][0]
                    G = arr[n][m][1]
                    B = arr[n][m][2]
                    color_sum += int(R) + int(G) + int(B)
        return color_sum

    def set_pixel_color(self, arr, i, j, s):
        for n in range(i, i + self.step):
                for m in range(j, j + self.step):
                    arr[n][m][0] = int(s // self.gradation) * self.gradation / 3
                    arr[n][m][1] = int(s // self.gradation) * self.gradation / 3
                    arr[n][m][2] = int(s // self.gradation) * self.gradation / 3
        return arr

    def generate(self, img):
        arr = np.array(img)
        h, w = len(arr), len(arr[1])
        for i in range(0, h, self.step):
            for j in range(0, w, self.step):
                color_sum = self.get_pixel_color(arr, i, j) // (10 * self.step)
                arr = self.set_pixel_color(arr, i, j, color_sum)
        return Image.fromarray(arr)



img = Image.open("img2.jpg")
generator = pixelArtGenerator(gradations = 4)
res = generator.generate(img)
res.save('res.jpg')