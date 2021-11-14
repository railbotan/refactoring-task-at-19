from PIL import Image
import numpy as np
class Filter():
    def __init__(self, img, mosaic_size, grayscale):
        self.arr = np.array(img)
        self.mosaic_size = mosaic_size
        self.grayscale = grayscale
        
    def __GetAverage(self, y, x):
        average = 0
        for n in range(y, y + self.mosaic_size):
            for m in range(x, x + self.mosaic_size):
                R = int(self.arr[n][m][0])
                G = int(self.arr[n][m][1])
                B = int(self.arr[n][m][2])
                median = R + G + B
                average += median
        return int(average // (self.mosaic_size*self.mosaic_size))
    
    def __DoGray(self, y, x, average):
        for n in range(y, y + self.mosaic_size):
            for m in range(x, x + self.mosaic_size):
                self.arr[n][m][0] = int(average // self.grayscale) * self.grayscale/3
                self.arr[n][m][1] = int(average // self.grayscale) * self.grayscale/3
                self.arr[n][m][2] = int(average // self.grayscale) * self.grayscale/3

    def __SaveResult(self):
        res = Image.fromarray(self.arr)
        res.save('res.jpg')
                
    def StartFilter(self):
        height, width = len(self.arr), len(self.arr[1])
        y = 0
        while y < height:
            x = 0
            while x < width:
                average = self.__GetAverage(y, x)
                self.__DoGray(y, x, average)
                x = x + self.mosaic_size
            y = y + self.mosaic_size
        self.__SaveResult()

img = Image.open("img2.jpg")
filtr = Filter(img, 10, 50)
filtr.StartFilter()
