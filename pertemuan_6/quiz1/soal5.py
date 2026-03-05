# NAMA : LUTHFI KRISHNA HARYADI
# NIM : 25071103865
# KELAS : TI-C

stok_gadget = [ 
{'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000}, 
{'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000}, 
{'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000}, 
{'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}, 
] 

katalog = [ {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 
2}, {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5} ] 

skema_komisi = ( 
(100000000, 10), # Penjualan >= 100jt -> Komisi 10% 
(50000000,  5),  # Penjualan >= 50jt  -> Komisi 5% 
(20000000,  2),  # Penjualan >= 20jt  -> Komisi 2% 
(0,         0)   # Di bawah 20jt      
)

def filter_harga(data, min_harga, max_harga):
  memenuhi = []
  for i in stok_gadget:
    if i['harga'] > min_harga and i['harga'] < max_harga:
      memenuhi.append(i)
  return memenuhi

def registrasi_gadget(merk, tipe, harga, sn):
  if harga >= 1000000:
    if len(sn) >= 5:
      return {'merk' : merk, 'tipe' : tipe, 'harga' : harga, 'sn' : sn, 'status' : 'Tersedia' }


def update_stok(katalog, sn_target, jumlah_tambah):
  for i in katalog:
    if sn_target == i['sn']:
      i['stok'] += jumlah_tambah
  return



def hitung_komisi(total_penjualan, skema, index=0):
  if total_penjualan > skema[index][0]:
    return skema[index][1]
  return hitung_komisi(total_penjualan, skema, index + 1)
  
inventaris = []

while True:
  print('=== PyGadget Hub ===')
  print('1. Tambah Gadget')
  print('2. Daftar Inventaris')
  print('3. Update Stok')
  print('4. Cek Komisi')
  print('5. Keluar')
  pilihan = input("pilih operasi 1/2/3/4/5 : ")
  
  if pilihan == '1':
    merk = input('masukkan merk : ')
    tipe = input('masukkan tipe barang : ')
    harga = float(input('masukkan harga barang : '))
    sn = input('masukkan serial number : ')
    inventaris.append(registrasi_gadget(merk, tipe, harga, sn))
    
  elif pilihan == '2':
    print('Daftar Inventaris')
    for i in inventaris:
      print(i)
      
  elif pilihan == '3':
    sn_target = input('masukkan sn : ')
    jumlah_tambah = int(input('masukkan jumlah tambahan stok : '))
    update_stok(katalog, sn_target, jumlah_tambah)
    
  elif pilihan == '4':
    nama_sales = input('masukkan nama sales : ')
    total_penjualan = int(input('masukkan total harga : '))
    persen = hitung_komisi(total_penjualan, skema_komisi)
    print(f'nama sales : {nama_sales}')
    print(f'persen komisi : {persen}%')
    print(f'nilai komisi : Rp{total_penjualan*persen/100 :,.0f}')
    
  elif pilihan =='5':
    print('Terima Kasih telah menggunakan aplikasi kami :)')
    break