stok_barang = [15, 40, 30, 10, 25] 

#1. ganti nilai 10 ke 50
index = stok_barang.index(10)
stok_barang[index] = 50
print(stok_barang)

#2. tambah 5 ke akhir, urutkan daari besar ke kecil
stok_barang.append(5)
stok_barang.sort(reverse=True)

#3. tampilkan jumlah seluruh total elemen list
print(sum(stok_barang))

#4.
rata = sum(stok_barang)/len(stok_barang)
print(rata)
print("stok aman") if rata > 20 else print("waspada")

print(stok_barang)