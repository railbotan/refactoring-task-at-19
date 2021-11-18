from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a:
    j = 0
    while j < a1:
        s = 0
        for n in range(i, min(i + 10, a - 1)):
            for d1 in range(j, j + 10):
                n1 = arr[n][d1][0]
                n2 = arr[n][d1][1]
                n3 = arr[n][d1][2]
                M = int(n1)
                M = (M + n2 + n3) // 3
                s += M
        s = int(s // 100)
        # print(s)
        for n in range(i, min(i + 10, a - 1)):
            for d1 in range(j, j + 10):
                arr[n][d1][0] = int(s // 50) * 50
                arr[n][d1][1] = int(s // 50) * 50
                arr[n][d1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
