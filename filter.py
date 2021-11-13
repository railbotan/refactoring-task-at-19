from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
height = len(arr)
width = len(arr[1])
size = int(input("Enter size: "))
gradation = int(input("Enter gradation: "))
step = int(255 / gradation)

class Grey:
  def __init__(self, step, height, width, size, arr):
    self.step = step
    self.height = height
    self.width = width
    self.size = size
    self.arr = arr
  def getGrey(self):
    i = 0
    while i < self.height:
      j = 0
      while j < self.width:
        average = 0
        for n in range(i, i + self.size):
            for n1 in range(j, j + self.size):
                r = self.arr[n][n1][0]
                g = self.arr[n][n1][1]
                b = self.arr[n][n1][2]
                grey = (int(r) + int(g) + int(b)) / 3
                average += grey
        average = int(average // (self.size*self.size))
        for n in range(i, i + self.size):
            for n1 in range(j, j + self.size):
                self.arr[n][n1][0] = int(average // self.step) * self.step
                self.arr[n][n1][1] = int(average // self.step) * self.step
                self.arr[n][n1][2] = int(average // self.step) * self.step
            j = j + self.size
            i = i + self.size
        return self.arr

        newPicture = Grey(step, height, width, size, arr)
        res = Image.fromarray(newPicture.getGrey())
        res.save('res.jpg')
