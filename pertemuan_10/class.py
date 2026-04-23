class Web:
  def __init__(self):
    self.web = []

  def push(self, element):
    self.web.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.web.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.web[-1]

  def isEmpty(self):
    return len(self.web) == 0

  def size(self):
    return len(self.web)

web = Web()

web.push('youtube.com')
web.push('w3schools.com')
web.push('chatgpt.com')

print("Stack: ", web.web)
print("Pop: ", web.pop())
print("Stack after Pop: ", web.web)
print("Peek: ", web.peek())
print("isEmpty: ", web.isEmpty())
print("Size: ", web.size())