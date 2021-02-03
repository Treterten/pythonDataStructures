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
  def removeFromHead(self):
    self.head = self.head.next
  def get(self, value):
    node = self.head
    while (node != None):
      if (node.value == value):
        return node
      node = node.next
    return None
  def getIndex(self, value):
    node = self.head
    index = 0
    while (node != None):
      if (node.value == value):
        return index
      index += 1
      node = node.next
    return index

  def printList(self):
    node = self.head
    string = ''
    while (node != None):
      string += node.value + '->'
      node = node.next
    return string

class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

if __name__ == '__main__':
  myList = LinkedList()
  myList.addToTail('hi')
  myList.addToTail('never')
  myList.addToTail('laughing')
  myList.addToHead('newHeadHaha')
  print(myList.printList())
  myList.removeFromHead()
  print(myList.getIndex('hi'))
  print(myList.get('laughing'))
  print(myList.get('not in the list'))