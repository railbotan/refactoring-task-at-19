from PIL import Image
import numpy as np


def get_average_brightness(start_x, start_y, pixel_size):
    average = np.sum((img_arr[start_y: start_y + pixel_size, start_x: start_x + pixel_size])) / 3
    return int(average // (pixel_size * pixel_size))


def set_gradation(start_x, start_y, pixel_size, grayscale):
    average = get_average_brightness(start_x, start_y, pixel_size)
    gradation = int(average // grayscale) * grayscale
    img_arr[start_y: start_y + pixel_size, start_x: start_x + pixel_size] = gradation


def img_convert(pixel_size, grayscale):
    height = len(img_arr)
    width = len(img_arr[1])
    for y in range(0, height, pixel_size):
        for x in range(0, width, pixel_size):
            set_gradation(x, y, pixel_size, grayscale)
    res = Image.fromarray(img_arr)
    res.save('res.jpg')


img = Image.open("img2.jpg")
img_arr = np.array(img)
img_convert(10, 50)
