from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
height = len(arr)
width = len(arr[1])


def pixelate(image_array, gradation_number=5, pixel_size=10):
    grey_step = 256 // gradation_number
    for i in range(0, height, pixel_size):
        for j in range(0, width, pixel_size):
            summa = 0
            for di in range(i, min(i + pixel_size, height)):
                for dj in range(j, min(j + pixel_size, width)):
                    red = image_array[di][dj][0]
                    green = image_array[di][dj][1]
                    blue = image_array[di][dj][2]
                    mean_colour = (int(red) + green + blue) // 3
                    summa += mean_colour
            summa = int(summa // pixel_size // pixel_size)
            # print(s)
            for di in range(i, min(i + pixel_size, height)):
                for dj in range(j, min(j + pixel_size, width)):
                    image_array[di][dj][0] = int(summa // grey_step) * grey_step
                    image_array[di][dj][1] = int(summa // grey_step) * grey_step
                    image_array[di][dj][2] = int(summa // grey_step) * grey_step


pixelate(arr)

res = Image.fromarray(arr)
res.save('res.jpg')
