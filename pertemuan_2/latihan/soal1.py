stok = [15, 50, 30, 25, 40]

#1. tambahkan stok baru (100)
stok.append(100)

#2. sisipkan angka 75 pada indeks 2
stok.insert(2, 75)

#3. urutkan list terbaru dari besar ke kecil
stok.sort(reverse=True)

#4. hitung rata ratanya
jumlah = 0
banyak = 1
ratarata = 0
for x in stok:
  jumlah+=x
  banyak+=1
ratarata = jumlah/banyak

#5. tampilkan semua isi list setelah semua perubahan
print (stok)