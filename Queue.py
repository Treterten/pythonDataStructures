class Queue():
  def __init__(self):
    self.storage = []
  def enqueue(self, value):
    self.storage.append(value)
  def __str__(self):
    return ' '.join([str(i) for i in self.storage])
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

if __name__ == '__main__':
  myQueue = Queue()
  myQueue.enqueue(3213)
  myQueue.enqueue('Hi')
  myQueue.enqueue('Over 90009')
  print(myQueue)
  myQueue.dequeue()
  print(myQueue)
  print(myQueue.isEmpty())
  print(myQueue.getSize())
  myQueue.dequeue()
  myQueue.dequeue()
  print(myQueue.isEmpty())