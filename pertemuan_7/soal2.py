class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode: 
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def insertNodeAtPosition(head, plat, position):
  if position == 1:
    mobilBaru.next = head
    return mobilBaru

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  mobilBaru.next = currentNode.next
  currentNode.next = mobilBaru
  return head

def deleteSpecificNode(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head

mobil1 = Node('b 123 aa')
mobil2 = Node('b 124 aa')
mobil3 = Node('b 125 aa')

mobil1.next = mobil2
mobil2.next = mobil3

print("Before deletion:")
traverseAndPrint(mobil1)

# Delete node4
mobil11 = deleteSpecificNode(mobil1, mobil2)

print("\nAfter deletion:")
traverseAndPrint(mobil1)

mobilBaru = Node('b 999 aa')
node1 = insertNodeAtPosition(mobil1, mobilBaru, 3)

print("\nAfter insertiion:")
traverseAndPrint(mobil1)

