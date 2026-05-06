class Node:
  def __init__(self, id_buku, judul):
    self.id_buku = id_buku
    self.judul = judul
    self.left = None
    self.right = None
    
class Katalog:
  def __init__(self):
    self.root = None
    
  def insert (self, id_buku, judul):
    new_node = Node(id_buku, judul)
    if self.root == None:
      self.root = Node(id_buku, judul)
      print(f"Berhasil memasukkan: ID {id_buku} - {judul}")

    else:
      self.__insertrec(self.root, new_node)
    
  def __insertrec(self, current, new_node):
    #dikasih "__" biar privat, gabisa dipake dari luar
    if new_node.id_buku < current.id_buku:
      if current.left is None:
        current.left = new_node
        print(f"Berhasil memasukkan: ID {new_node.id_buku} - {new_node.judul}")
      else:
        self.__insertrec(current.left, new_node)

    elif new_node.id_buku > current.id_buku:
      if current.right is None:
        current.right = new_node
        print(f"Berhasil memasukkan: ID {new_node.id_buku} - {new_node.judul}")
      else:
        self.__insertrec(current.right, new_node)

  def search(self, id_buku):
    return self.__searchrec(self.root, id_buku)
  
  def __searchrec(self, current, id_buku):
    #ini juga, dikasih "__" biar privat, gabisa dipake dari luar karena buat rekursi doang
    if current == None:
      return None

    elif id_buku == current.id_buku:
      return current

    elif id_buku < current.id_buku:
      return self.__searchrec(current.left, id_buku)
    else:
      return self.__searchrec(current.right, id_buku)

  def traversal_inorder(self):
    return self.__traversal_inorder_rec(self.root)

  def __traversal_inorder_rec(self, current):
    if current == None:
      return None
    self.__traversal_inorder_rec(current.left)
    print(current.judul, end=", ")
    self.__traversal_inorder_rec(current.right)

  def get_min(self):
    current = self.root
    while current.left:
      current = current.left
    print(f'Buku dengan ID terkecil : {current.id_buku} - {current.judul}')
    
  def get_max(self):
    current = self.root
    while current.right:
      current = current.right
    print(f'Buku dengan ID terbesar : {current.id_buku} - {current.judul}')
    
  def height(self):
    return self.__heightrec(self.root)

  def __heightrec(self, current):
    if current == None:
      return -1 #ini -1 karena daun node terujung (leaf) tingginya 0, liat rumus height dibaris berikutnya
    
    height_left = self.__heightrec(current.left)
    height_right = self.__heightrec(current.right)
    
    height = max(height_left, height_right) + 1
    return height

print("SISTEM KATALOG PERPUSTAKAAN 'ILMU TERANG'")
print("=========================================")

katalog = Katalog()

katalog.insert(50, "Dasar Pemrograman")
katalog.insert(30, "Struktur Data")
katalog.insert(70, "Kecerdasan Buatan")
katalog.insert(20, "Matematika Diskrit")
katalog.insert(40, "Basis Data")
katalog.insert(60, "Jaringan Komputer")
katalog.insert(80, "Sistem Operasi")

katalog.traversal_inorder()

cari1 = katalog.search(60)
if cari1:
  print()
  print(f"Mencari ID 60... Ditemukan! Judul: {cari1.judul}")
else:
  print()
  print("Mencari ID 60... Data tidak ditemukan.")

cari2 = katalog.search(100)
if cari2:
  print(f"Mencari ID 100... Ditemukan! Judul: {cari2.judul}")
else:
  print("Mencari ID 100... Data tidak ditemukan.")

katalog.get_min()
katalog.get_max()

print(f"Tinggi (Height) Tree: {katalog.height()}")
print("=========================================")
print("Simulasi Selesai!")