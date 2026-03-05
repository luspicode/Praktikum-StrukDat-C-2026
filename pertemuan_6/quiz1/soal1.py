# NAMA : LUTHFI KRISHNA HARYADI
# NIM : 25071103865
# KELAS : TI-C
def registrasi_gadget(merk, tipe, harga, sn):
  if harga >= 1000000:
    if len(sn) >= 5:
      return {'merk' : merk, 'tipe' : tipe, 'harga' : harga, 'sn' : sn, 'status' : 'Tersedia' }
    else:
      print('sn tidak sampai 5 karakter')
      return None
  else: 
    print('harga tidak sampai 1 juta')
    return None


inventaris = []
for i in range(3):
  merk = input('masukkan merk barang : ')
  tipe = input('masukkan tipe barang : ')
  harga = float(input('masukkan harga barang : '))
  sn = input('masukkan serial number : ')
  inventaris.append(registrasi_gadget(merk, tipe, harga, sn))


for i in inventaris:
  print(i)