from PIL import Image
import numpy as np


def make_gray_picture(img_arr, mosaic_size, grayscale):
    height = len(img_arr)
    width = len(img_arr[0])
    gradation_step = 255 / (grayscale - 1)
    y = 0
    while y <= height - mosaic_size:
        x = 0
        while x <= width - mosaic_size:
            sum_bright = np.sum((img_arr[y: y + mosaic_size, x: x + mosaic_size]) / 3)
            aver_bright = int(sum_bright // (mosaic_size * mosaic_size))
            img_arr[y: y + mosaic_size, x: x + mosaic_size] = int(aver_bright // gradation_step) * gradation_step
            x += mosaic_size
        y += mosaic_size
    return img_arr


print("Enter the full name of the image")
img = Image.open(input())
print("Enter the full name of the result image")
res_name = input()
img_array = np.array(img)
make_gray_picture(img_array, 1, 10)
res = Image.fromarray(img_array)
res.save(res_name)
