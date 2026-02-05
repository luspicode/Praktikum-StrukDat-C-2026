barang = ("B001", "Laptop Gaming", 15000000)

#1. akses dan tampilkan harg barang
print(barang[2])

#2. ubah harga barang jadi 14000000, lalu jelaskan kenapa eror
#barang[2] = 14000000
#TypeError: 'tuple' object does not support item assignment
#hal tsb mucul di terminal sebab "tuple" memang tidak bisa diubah isinya secara langsung (unchageable)

#3. gunakan teknik unpacking untuk masukkan nilai tuple ke variabel kode, nama, harga
kode, nama, harga = barang
print (kode, nama, harga)

