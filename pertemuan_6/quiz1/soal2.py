# NAMA : LUTHFI KRISHNA HARYADI
# NIM : 25071103865
# KELAS : TI-C

stok_gadget = [ 
{'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000}, 
{'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000}, 
{'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000}, 
{'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000}, 
] 


def filter_harga(data, min_harga, max_harga):
  memenuhi = []
  for i in stok_gadget:
    if i['harga'] > min_harga and i['harga'] < max_harga:
      memenuhi.append(i)
  print('Tidak ada gadget dalam rentang harga tersebut.')
  return memenuhi

  

batas_atas = int(input('masukkan batas atas harga : '))
batas_bawah = int(input('masukkan batas bawah harga : '))

sesuai = filter_harga(stok_gadget, batas_bawah, batas_atas)

for i in sesuai:
  print(i)