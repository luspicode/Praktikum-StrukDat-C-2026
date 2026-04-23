pengunjung_hari_ini = [ 
{"id": "M001", "nama": "Rina",   "usia": 20, "kategori": "Fiksi",   "kembali": False}, 
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",   "kembali": True}, 
{"id": "M003", "nama": "Siti",   "usia": 19, "kategori": "Fiksi",   "kembali": False}, 
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",   "kembali": True}, 
{"id": "M005", "nama": "Yuni",   "usia": 18, "kategori": "Sains",   "kembali": False}, 
{"id": "M006", "nama": "Bagas",  "usia": 22, "kategori": "Hukum",   "kembali": False}, 
]


def tampilkan_pengunjung(pengunjung_hari_ini):
  print('===== DATA PENGUNJUNG PERPUSTAKAAN ===== ')
  print('No | ID   | Nama   | Usia | Kategori | Status Kembali ')
  print('---+------+--------+------+----------+--------------- ')
  for i in range(len(pengunjung_hari_ini)):
    p = pengunjung_hari_ini[i]

    #karena masih boolean, ganti dulu ke string statusnya
    kembali = 'Sudah Kembali' if p['kembali'] else 'Belum Kembali' 
    print(f'{i+1}  | {p['id']} | {p['nama']:<6} | {p['usia']}   | {p['kategori']}    | {kembali} ')

def filter_belum_kembali(pengunjung_hari_ini):
  belum = []
  for i in range(len(pengunjung_hari_ini)):
    p = pengunjung_hari_ini[i]
    if p['kembali'] == False:
      belum.append(p['nama'])
  belum.sort()
  
  print('===== PENGUNJUNG BELUM KEMBALI ===== ')
  for i in range(len(belum)):
    print(f'{i+1}. {belum[i]}')
  print(f'Total belum kembali: {len(belum)} pengunjung ')


tampilkan_pengunjung(pengunjung_hari_ini)
filter_belum_kembali(pengunjung_hari_ini)
print()
print()


def info_perpustakaan():
  info = ('Perpustakaan Kampus Terpadu', 'Jl. Pendidikan No. 5, Pekanbaru ','0761-54321 ')
  return info

def rekap_kategori(pengunjung_hari_ini):
  
  #buat variabel rekap (set) untuk mengumpulkan kategori unik
  rekap = set([pengunjung_hari_ini[i]['kategori'] for i in range(len(pengunjung_hari_ini))])
  print(f'Kategori Buku Unik: {rekap}')
  print(f'Jumlah Kategori: {len(rekap)}')
  
  #buat dict untuk kategori sekaligus jumlahnya
  rkp_ktgr = dict()
  for i in range(len(pengunjung_hari_ini)):
    ktgr = pengunjung_hari_ini[i]['kategori']
    if (ktgr in rkp_ktgr) == False:
      rkp_ktgr[ktgr] = 1
    else:
      rkp_ktgr[ktgr] += 1
      
  print('Rekap per kategori: ')
  #akses item dari dict
  for i, j in rkp_ktgr.items():
    print(f'{i} : {j} pengunjung')

info = info_perpustakaan()
print('Info Perpustakaan: ')
print(f'Nama    : {info[0]}')
print(f'Alamat  : {info[1]}')
print(f'Telp    : {info[2]}')
print()

rekap_kategori(pengunjung_hari_ini)
print()
print()



class Pengunjung:
  #definisikan jumalah Pasien
  jumlah = 0
  def __init__(self, id, nama, kategori):
    self.__id = id
    self.__nama = nama
    self.__kategori = kategori
    #buat pengunjung tambah 1 disini karena setiap buat objek dengan class Pengunjung , pengunjung emang nambah 1
    Pengunjung.jumlah += 1
    
  def get_id(self):
    return self.__id
  
  def get_nama(self):
    return self.__nama
  
  def get_kategori(self):
    return self.__kategori
  
  def tampilkan_info(self):
    print(f'ID       : {self.__id} ')
    print(f'Nama     : {self.__nama} ')
    print(f'Kategori : {self.__kategori} ')
    
  @staticmethod
  def hitung_pengunjung():
    return Pengunjung.jumlah
  
  
class PengunjungPrioritas(Pengunjung):
  def __init__(self, id, nama, kategori, prioritas):
    super().__init__(id, nama, kategori)
    self.prioritas = prioritas
    
    
  def tampilkan_info(self):
    super().tampilkan_info()
    print(f'Prioritas: {self.prioritas}')
    if self.prioritas == 'Mendesak':
      print('** Layani segera! ** ')
      
p1 = Pengunjung('M001', 'Rina', 'Fiksi')
p2 = PengunjungPrioritas('M007', 'Gilang', 'Referensi', 'Mendesak')

p1.tampilkan_info()
print()
p2.tampilkan_info()

print(f'Total pengunjung terdaftar: {p1.hitung_pengunjung()}')
print()
print()



class Node: 
  def __init__(self, data):
    self.data = data
    self.next = None
    
class AntrianPeminjaman:
  def __init__(self, data):
    self.head = data
    
  def tambah(self, data):
    node_baru = Node(data)
    temp = self.head
    
    while temp.next:
      temp = temp.next
    temp.next = node_baru

  def tampilkan(self):
    print('===== ANTRIAN PEMINJAMAN ===== ')
    i =0
    temp = self.head
    while temp:
      p = temp.data
      print(f'[{i+1}] {p['id']} - {p['nama']} | {p['kategori']}')
      temp = temp.next
      i += 1
      
  def panggil_berikutnya(self):
    if not self.head:
      print('ga ada pengunjung')
      return None
    
    print('Memanggil pengunjung berikutnya... ')
    temp = self.head
    print(f'Silakan masuk: {temp.data['nama']} ({temp.data['id']}) - {temp.data['kategori']} ')
    temp = temp.next
    self.head = self.head.next
    
  def cari(self, nama):
    temp = self.head
    print(f'Mencari "{nama}"... ')
    i = 1
    while temp:
      if temp.data['nama'] == nama:
        print(f'Ditemukan: {temp.data["id"]} - {temp.data["nama"]} | {temp.data["kategori"]} (posisi ke- {i}) ')
      temp = temp.next
      i+=1
        
        
  def hapus_berdasarkan_id(self, id):
    if id == self.head.data[id]:
      self.head = self.head.next
      return None
    
    else:
      temp = self.head
      while temp:
        if id == self.head.data[id]:
          self.head = self.head.next
          return None
        temp = temp.next
    print('ID tidak ditemukan dalam antrian ')


  def hitung(self):
    temp = self.head
    i = 0
    while temp:
      temp = temp.next
      i += 1
    return i
antrian = AntrianPeminjaman(Node({"id": "M001", "nama": "Rina",   "kategori": "Fiksi"})) 
antrian.tambah({"id": "M002", "nama": "Hendra", "kategori": "Sains"}) 
antrian.tambah({"id": "M003", "nama": "Siti",   "kategori": "Fiksi"}) 
antrian.tambah({"id": "M004", "nama": "Taufik", "kategori": "Hukum"}) 
antrian.tampilkan() 
antrian.panggil_berikutnya() 
antrian.tampilkan() 

antrian.cari("Taufik") 
antrian.tampilkan() 
# hapusnya eror
# antrian.hapus_berdasarkan_id("M003") 
# antrian.tampilkan() 

print("Total antrian:", antrian.hitung())