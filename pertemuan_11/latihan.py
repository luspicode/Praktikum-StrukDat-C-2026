class Node:
  def __init__(self, nama, keluhan):
    self.nama = nama
    self.keluhan = keluhan
    self.next = None

class AntrianPasien:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def enqueue(self, nama, keluhan):
    new_node = Node(nama, keluhan)
    if self.tail is None:
      self.head = self.tail = new_node
      self.length += 1
      return
    self.tail.next = new_node
    self.tail = new_node
    self.length += 1

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty"
    temp = self.head
    self.head = temp.next
    self.length -= 1
    if self.head is None:
      self.tail = None
    return temp.nama

  def peek(self):
    if self.isEmpty():
      return "Queue is empty"
    return self.head.nama

  def isEmpty(self):
    return self.length == 0

  def size(self):
    return self.length

  def printQueue(self):
    temp = self.head
    while temp:
      print(temp.nama, end=" -> ")
      temp = temp.next
    print()
    
  def clear(self):
    self.head = None
    
pasien = AntrianPasien()

print('=========================================')
print('SISTEM ANTRIAN POLI UMUM RS Sehat Bersama')
print('=========================================')

print("Apakah antrian kosong?: ", pasien.isEmpty())

pasien.enqueue('Budi', 'demam tinggi')
pasien.enqueue('Ani', 'batuk pilek')
pasien.enqueue('Citra', 'sakit kepala')

print("Jumlah Antrian Pasien : ", pasien.size())

print("Pasien Berikutnya : ", pasien.peek())

print("Memanggil Pasien Pertama... ", pasien.dequeue())

pasien.enqueue('Dodi', 'nyeri perut')

print("Daftar Pasien (Antrian) : ", end="")
pasien.printQueue()

print("Memanggil Pasien Berikutnya... ", pasien.dequeue())

print("Daftar Pasien (Antrian) : ", end="")
pasien.printQueue()

print('Sesi Habis, Mengosongkan Antrian...')
pasien.clear()

print("Daftar Pasien (Antrian) : ", end="")
pasien.printQueue()