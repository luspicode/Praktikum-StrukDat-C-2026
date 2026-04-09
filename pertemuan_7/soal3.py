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

def sisipkan_vip(head, plat_baru, plat_target):
  plat_target = head
  
  plat_baru.next = plat_target.next
  plat_target.next = plat_baru
  return head


mobil1 = Node('b 123 aa')
mobil2 = Node('b 124 aa')
mobil3 = Node('b 125 aa')

mobil1.next = mobil2
mobil2.next = mobil3

print("Before sisipkan:")
traverseAndPrint(mobil1)

mobilvipbaru = Node('b 999 aa')
node1 = sisipkan_vip(mobil1, mobilvipbaru, mobil1)

print("after sisipkan:")
traverseAndPrint(mobil1)
