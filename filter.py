from PIL import Image
import numpy as np


def get_average(x, y, pixel_size):
    average = np.sum((img_arr[y: y + pixel_size, x: x + pixel_size])) / 3
    return int(average // (pixel_size * pixel_size))


def make_gray(x, y, pixel_size, grayscale):
    average = get_average(x, y, pixel_size)
    img_arr[y: y + pixel_size, x: x + pixel_size] = int(average // grayscale) * grayscale


def convert(pixel_size, grayscale):
    height, width = len(img_arr), len(img_arr[1])
    for y in range(0, height, pixel_size):
        for x in range(0, width, pixel_size):
            make_gray(x, y, pixel_size, grayscale)
    res = Image.fromarray(img_arr)
    res.save('res.jpg')


img = Image.open("img2.jpg")
img_arr = np.array(img)
convert(10, 50)
