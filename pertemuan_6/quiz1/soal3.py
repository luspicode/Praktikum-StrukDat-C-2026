# NAMA : LUTHFI KRISHNA HARYADI
# NIM : 25071103865
# KELAS : TI-C

katalog = [ {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok': 
2}, {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5} ] 

def update_stok(katalog, sn_target, jumlah_tambah):
  for i in katalog:
    if sn_target == i['sn']:
      i['stok'] += jumlah_tambah
      print(f'berhasil menambahkan {i['tipe']}, stok sekarang {i['stok']}')
      return i['merk']

daftar_merk = set()

for i in range(1): 
  sn_target = input('masukkan sn : ')
  jumlah_tambah = int(input('masukkan jumlah tambahan stok : '))
  daftar_merk.add(update_stok(katalog, sn_target, jumlah_tambah))
  
print(daftar_merk)
