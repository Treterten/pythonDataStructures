class Array():
  def __init__(self, dataType, size):
    self.storage = {}
    self.length = 0
    self.size = size
    if (dataType != int or dataType != str or dataType != bool or dataType != object or dataType != float):
      raise TypeError('Invalid DataType')
    self.dataType = dataType
  def setAt(self, index, item):
    if (self.size == self.length):
      raise ValueError('Array is at max capacity.')
    if (type(item) != self.dataType):
      raise TypeError('Invalid Type for Array<' + str(self.dataType) + '>')
    self.storage[index] = item
  def get(self, index):
    return self.storage[index]


def testArray():
  myArr = Array(str, 4)
  myArr.setAt(0, 2)

testArray()