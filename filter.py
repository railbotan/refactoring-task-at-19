from PIL import Image
import numpy as np


def get_average(x, y, pixel_size):
    average = 0
    for n in range(y, y + pixel_size):
        for m in range(x, x + pixel_size):
            r = img_arr[n][m][0]
            g = img_arr[n][m][1]
            b = img_arr[n][m][2]
            brightness_mid = (int(r) + int(g) + int(b)) / 3
            average += brightness_mid
    return int(average // (pixel_size * pixel_size))


def make_gray(x, y, pixel_size, grayscale):
    average = get_average(x, y, pixel_size)
    for n in range(y, y + pixel_size):
        for m in range(x, x + pixel_size):
            img_arr[n][m][0] = int(average // grayscale) * grayscale
            img_arr[n][m][1] = int(average // grayscale) * grayscale
            img_arr[n][m][2] = int(average // grayscale) * grayscale


def convert(arr, pixel_size, grayscale):
    height = len(arr)
    width = len(arr[1])
    y = 0
    while y < height:
        x = 0
        while x < width:
            make_gray(x, y, pixel_size, grayscale)
            x = x + 10
        y = y + 10
        res = Image.fromarray(arr)
        res.save('res.jpg')


img = Image.open("img2.jpg")
img_arr = np.array(img)
convert(img_arr, 10, 50)
