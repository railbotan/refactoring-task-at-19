from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
h, w = len(arr), len(arr[1])
i = 0
while i < h:
    j = 0
    while j < w:
        s = 0
        for n in range(i, i + 10):
            for m in range(j, j + 10):
                r = arr[n][m][0]
                g = arr[n][m][1]
                b = arr[n][m][2]
                M = int(r) + int(g) + int(b)
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for m in range(j, j + 10):
                arr[n][m][0] = int(s // 50) * 50 / 3
                arr[n][m][1] = int(s // 50) * 50 / 3
                arr[n][m][2] = int(s // 50) * 50 / 3
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
