from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
image_data = np.array(img)
height = len(image_data)
width = len(image_data[1])
i = 0
while i < height:
    j = 0
    while j < width:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                r = image_data[n][n1][0]
                g = image_data[n][n1][1]
                b = image_data[n][n1][2]
                average_color = (int(r) + int(g) + int(b)) / 3
                s += average_color
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                image_data[n][n1][0] = int(s // 50) * 50
                image_data[n][n1][1] = int(s // 50) * 50
                image_data[n][n1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(image_data)
res.save('res.jpg')
