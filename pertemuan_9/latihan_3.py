class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class CircularLinkedList:
  def __init__(self):
    self.head = None

  def tambah_petugas(self, nama):
    baru = Node(nama)

    if not self.head:
      self.head = baru
      baru.next = self.head

    else:
      temp = self.head
      while temp.next != self.head:
        temp = temp.next
            
      temp.next = baru
      baru.next = self.head

  def giliran_berikutnya(self, n):
    if not self.head:
      print("Tidak ada petugas")
      return

    current = self.head
        
    for i in range(1, n+1):
      print(f"Giliran {i}: {current.data}")
      current = current.next
      

daftar = CircularLinkedList()
daftar.tambah_petugas("Andi")
daftar.tambah_petugas("Budi")
daftar.tambah_petugas("Citra")
daftar.tambah_petugas("Dewi")

daftar.giliran_berikutnya(6)