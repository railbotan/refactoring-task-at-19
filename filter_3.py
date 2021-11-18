from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)


def pixelate(image_array, gradation_number=5, pixel_size=10):
    height = len(image_array)
    width = len(image_array[0])
    grey_step = 256 // gradation_number
    for i in range(0, height, pixel_size):
        for j in range(0, width, pixel_size):
            summa = np.sum(image_array[i:i + pixel_size, j:j + pixel_size])
            summa = int(summa // 3 // pixel_size // pixel_size) // grey_step * grey_step

            image_array[i:i + pixel_size, j:j + pixel_size] = summa


pixelate(arr, 2, 12)

res = Image.fromarray(arr)
res.save('res.jpg')
