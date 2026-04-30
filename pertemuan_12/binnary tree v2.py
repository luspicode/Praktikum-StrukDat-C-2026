class TreeNode:
  def __init__(self, data):
    self.data = data
    self.kanan = None
    self.kiri = None
    self.prev = None
    

root = TreeNode('A')
root.kiri = TreeNode('B')
root.kiri.prev = root
root.kiri.kiri = TreeNode('D')
root.kiri.kiri.prev = root.kiri
root.kiri.kanan = TreeNode('E')
root.kiri.kanan.prev = root.kiri
root.kanan = TreeNode('C')
root.kanan.prev = root
root.kanan.kanan = TreeNode('F')
root.kanan.kanan.prev = root.kanan


def preOrderTraversal(root):
  if root is None:
    return
  print(root.data, end=", ")
  preOrderTraversal(root.kiri)
  preOrderTraversal(root.kanan)

def inOrderTraversal(root):
  if root is None:
    return
  inOrderTraversal(root.kiri)
  print(root.data, end=", ")
  inOrderTraversal(root.kanan)

def postOrderTraversal(root):
  if root is None:
    return
  postOrderTraversal(root.kiri)
  postOrderTraversal(root.kanan)
  print(root.data, end=", ")

def leaf(root):
  if root is None:
    return
  if root.kiri is None and root.kanan is None:
    print(root.data)
  leaf(root.kanan)
  leaf(root.kiri)

leaf(root)
# print('root :', root.data)
# print('anak kiri dari A :', root.kiri.data)
# print('anak kanan dari A :', root.kanan.data)
# print('anak kiri dari B :', root.kiri.kiri.data)
# print('anak kanan dari B :', root.kiri.kanan.data)
# print('anak kanan dari C :', root.kanan.kanan.data)


print('preOrderTranversalRoot ', end=': ')
preOrderTraversal(root)
print()
print('inOrderTranversalRoot ', end=': ')
inOrderTraversal(root)
print()
print('postOrderTranversalRoot ', end=': ')
postOrderTraversal(root)
print()

