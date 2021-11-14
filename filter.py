from PIL import Image
import numpy as np
class Filter():
    def __init__(self, img, mosaic_size, grayscale):
        self.arr = np.array(img)
        self.mosaic_size = mosaic_size
        self.grayscale = grayscale
        
    def __GetAverage(self, y, x):
        average = np.sum((self.arr[y: y + self.mosaic_size, x: x + self.mosaic_size]))/3
        return int(average // (self.mosaic_size*self.mosaic_size))
    
    def __DoGray(self, y, x):
        average = self.__GetAverage(y, x)
        self.arr[y: y + self.mosaic_size, x: x + self.mosaic_size] = int(average // self.grayscale) * self.grayscale

    def __SaveResult(self):
        res = Image.fromarray(self.arr)
        res.save('res.jpg')
                
    def StartFilter(self):
        height, width = len(self.arr), len(self.arr[1])
        for y in range(0, height, self.mosaic_size):
            for x in range(0, width, self.mosaic_size):
                self.__DoGray(y, x)
                
        self.__SaveResult()

img = Image.open("img2.jpg")
filtr = Filter(img, 10, 50)
filtr.StartFilter()
