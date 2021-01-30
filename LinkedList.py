class LinkedList():
  def __init__(self):
    self.storage = {}
    self.head = None
    self.tail = None
  def addToTail(self, value):
    newNode = Node(value)
    if (self.head == None):
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode





class Node():
  def __init__(self, value):
    self.value = value
    self.next = None
