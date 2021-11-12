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
            aver_bright = 0
            for px_y in range(y, y + mosaic_size):
                for px_x in range(x, x + mosaic_size):
                    red = img_arr[px_y][px_x][0]
                    green = img_arr[px_y][px_x][1]
                    blue = img_arr[px_y][px_x][2]
                    px_median = (int(red) + int(green) + int(blue)) / 3
                    aver_bright += px_median
            aver_bright = int(aver_bright // (mosaic_size * mosaic_size))
            for px_y in range(y, y + mosaic_size):
                for px_x in range(x, x + mosaic_size):
                    img_arr[px_y][px_x][0] = int(aver_bright // gradation_step) * gradation_step
                    img_arr[px_y][px_x][1] = int(aver_bright // gradation_step) * gradation_step
                    img_arr[px_y][px_x][2] = int(aver_bright // gradation_step) * gradation_step
            x += mosaic_size
        y += mosaic_size
    return img_arr


img = Image.open("img2.jpg")
img_array = np.array(img)
make_gray_picture(img_array, 10, 5)
res = Image.fromarray(img_array)
res.save('res.jpg')
