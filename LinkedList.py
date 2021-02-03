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
  def addToHead(self, value):
    newNode = Node(value)
    newNode.next = self.head
    self.head = newNode
  def insertAtIndex(self, index, value):
    #TODO: Implementation
    newNode = Node(value)
    targetNode = self.head
    for i in range(0, index - 1):
      tagetNode = targetNode.next
    newNode.next = targetNode.next
    targetNode.next = newNode

class Node():
  def __init__(self, value):
    self.value = value
    self.next = None
