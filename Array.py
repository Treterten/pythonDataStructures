class Array():
  def __init__(self, dataType, size):
    self.storage = {}
    self.length = 0
    self.size = size
    if (dataType != int and dataType != str and dataType != bool and dataType != object and dataType != float):
      raise TypeError('Invalid DataType')
    self.dataType = dataType
  def setAt(self, index, item):
    if (self.size == self.length):
      raise ValueError('Array is at max capacity.')
    if (type(item) != self.dataType):
      raise TypeError('Invalid Type for Array')
    self.storage[index] = item
  def get(self, index):
    return self.storage[index]


def testArray():
  myArr = Array(str, '4')
  myArr.setAt(0, '2')

testArray()