from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
finImage = np.array(img)
height = len(finImage)
width = len(finImage[1])
i = 0
while i < height:
    j = 0
    while j < width:
        s = 0
        for n in range(i, i + 10):
            for m in range(j, j + 10):
                color1 = finImage[n][m][0]
                color2 = finImage[n][m][1]
                color3 = finImage[n][m][2]
                color = (int(color1) + int(color2) + int(color3)) / 3
                s += color
        s = int(s // 100)
        for n in range(i, i + 10):
            for m in range(j, j + 10):
                finImage[n][m][0] = int(s // 50) * 50
                finImage[n][m][1] = int(s // 50) * 50
                finImage[n][m][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(finImage)
res.save('res.jpg')
