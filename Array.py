class Array():
  def __init__(self, length, dataType):
    self.storage = {}
    self.length = length
    if (dataType != int or dataType != str or dataType != bool or dataType != object or dataType != float):
      raise TypeError('Invalid DataType')
    self.dataType = dataType
  def add(self, index, item):
    if (type(item) != self.dataType):
      raise TypeError('Invalid Type for Array<' + str(self.dataType) + '>')
    self.storage[index] = item

