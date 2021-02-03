class Stack():
  def __init__(self):
    self.storage = []
  def add(self, value):
    self.storage.append(value)
  def pop(self):
    return self.storage.pop()
  def __str__(self):
    string = ''
    for element in self.storage:
      string += element + ' '
    return string

if __name__ == '__main__':
  myStack = Stack()
  myStack.add('hi')
  myStack.add('oh no')
  myStack.add('hehe')
  print(myStack)
  myStack.pop()
  print(myStack)
