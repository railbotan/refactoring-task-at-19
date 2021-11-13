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
        color_sum = np.sum((self.arr[i: i + self.size, j: j + self.size]) / 3)
        average = int(color_sum // (self.size*self.size))
        self.arr[i: i + self.size, j: j + self.size] = int(average // self.step) * self.step
        j = j + self.size
      i = i + self.size
    return self.arr

newPicture = Grey(step, height, width, size, arr)
res = Image.fromarray(newPicture.getGrey())
res.save('res.jpg')
