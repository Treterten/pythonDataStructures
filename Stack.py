class Stack():
  def __init__(self):
    self.storage = []
  def add(self, value):
    self.storage.append(value)
  def pop(self):
    return self.storage.pop()

