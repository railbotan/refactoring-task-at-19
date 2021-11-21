from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
giv_image = np.array(img)
height = len(giv_image)
width = len(giv_image[1])
i = 0
while i < height:
    j = 0
    while j < width:
        s = 0
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                r = giv_image[n][n1][0]
                g = giv_image[n][n1][1]
                b = giv_image[n][n1][2]
                color = (int(r) + int(g) + int(b)) / 3
                s += color
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                giv_image[n][n1][0] = int(s // 50) * 50
                giv_image[n][n1][1] = int(s // 50) * 50
                giv_image[n][n1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(giv_image)
res.save('res.jpg')
