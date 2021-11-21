from PIL import Image
import numpy as np


# img = Image.open("img2.jpg")
# finImage = np.array(img)
# height = len(finImage)
# width = len(finImage[1])
# i = 0
# while i < height:
#     j = 0
#     while j < width:
#         s = 0
#         for n in range(i, i + 10):
#             for m in range(j, j + 10):
#                 color1 = finImage[n][m][0]
#                 color2 = finImage[n][m][1]
#                 color3 = finImage[n][m][2]
#                 color = (int(color1) + int(color2) + int(color3)) / 3
#                 s += color
#         s = int(s // 100)
#         for n in range(i, i + 10):
#             for m in range(j, j + 10):
#                 finImage[n][m][0] = int(s // 50) * 50
#                 finImage[n][m][1] = int(s // 50) * 50
#                 finImage[n][m][2] = int(s // 50) * 50
#         j = j + 10
#     i = i + 10
# res = Image.fromarray(finImage)
# res.save('res.jpg')


class PixelArt:
    def imgToNpArr(path):
        img = Image.open(path)
        return np.array(img)

    def saveImg(img, name):
        res = Image.fromarray(img)
        res.save(name)

    def avg(img, size, x, y):
        height = len(img)
        width = len(img[1])
        color = 0
        for i in range(x, min(x + size, width)):
            for j in range(y, min(y + size, height)):
                color += sum(int(color) for color in img[i][j]) // 3
        color = color // (size ** 2)
        return color

    def createPixel(img, size, grayscale):
        height = len(img)
        width = len(img[1])
        for y in range(0, height, size):
            for x in range(0, width, size):
                color = PixelArt.avg(img, size, x, y)
                for x1 in range(x, min(x + size, width)):
                    for y1 in range(y, min(y + size, height)):
                        img[x1][y1][0] = img[x1][y1][1] = img[x1][y1][2] = color - color % grayscale

        return img


img = PixelArt.imgToNpArr("img2.jpg")
PixelArt.saveImg(PixelArt.createPixel(img, 10, 50), 'final.jpg')
