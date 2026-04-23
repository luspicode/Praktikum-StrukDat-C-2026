class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Web:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self, value):
    new_node = Node(value)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self.size += 1

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    popped_node = self.head
    self.head = self.head.next
    self.size -= 1
    return popped_node.value

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.head.value

  def isEmpty(self):
    return self.size == 0

  def stackSize(self):
    return self.size

  def traverseAndPrint(self):
    currentNode = self.head
    while currentNode:
      print(currentNode.value, end=" -> ")
      currentNode = currentNode.next
    print()

web = Web()
web.push('youtube.com')
web.push('w3schools.com')
web.push('chatgpt.com')

print("LinkedList: ", end="")
web.traverseAndPrint()
print("Peek: ", web.peek())
print("Pop: ", web.pop())
print("LinkedList after Pop: ", end="")
web.traverseAndPrint()
print("isEmpty: ", web.isEmpty())
print("Size: ", web.stackSize())