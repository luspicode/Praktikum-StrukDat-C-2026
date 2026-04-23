class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
    
class DoubleLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def tambah_kendaraan(self, plat):
    baru = Node(plat)
    if not self.head:
      self.head = baru
      self.tail = baru
      
    else:
      self.tail.next = baru
      baru.prev = self.tail
      self.tail = baru
    
  def hapus_kendaraan(self, plat):
    temp = self.head
    while temp and temp.data != plat:
      temp = temp.next
    
    if not temp:
      print("Kendaraan tidak ditemukan")
      return
    
    if temp == self.head:
      self.head = temp.next
      if self.head:
        self.head.prev = None
      else:
        self.tail = None
    
    elif temp == self.tail:
      self.tail = temp.prev
      self.tail.next = None

    else:
      temp.prev.next = temp.next
      temp.next.prev = temp.prev

  def tampilkan_maju(self):
    print('[Maju]')
    temp = self.head
    while temp:
      print(temp.data)
      temp = temp.next

  def tampilkan_mundur(self):
    print('[Mundur]')
    temp = self.tail
    while temp:
      print(temp.data)
      temp = temp.prev


daftar = DoubleLinkedList()
daftar.tambah_kendaraan("B 1111 AA") 
daftar.tambah_kendaraan("D 2222 BB") 
daftar.tambah_kendaraan("A 3333 CC") 
daftar.tambah_kendaraan("B 4444 DD") 
print("Sebelum:") 
daftar.tampilkan_maju() 
daftar.hapus_kendaraan("A 3333 CC") 
print("Sesudah:") 
daftar.tampilkan_maju() 