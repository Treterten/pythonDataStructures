class Queue():
  def __init__(self):
    self.storage = []
  def enqueue(self, value):
    self.storage.append(value)
  def isEmpty(self):
    if (len(self.storage) == 0):
      return True
    else:
      return False
  def dequeue(self):
    if (not self.isEmpty()):
      return self.storage.pop(0)
    else:
      return 'Empty'
  def getSize(self):
    return len(self.storage)