# NAMA : LUTHFI KRISHNA HARYADI
# NIM : 25071103865
# KELAS : TI-C

skema_komisi = ( 
(100000000, 10), # Penjualan >= 100jt -> Komisi 10% 
(50000000,  5),  # Penjualan >= 50jt  -> Komisi 5% 
(20000000,  2),  # Penjualan >= 20jt  -> Komisi 2% 
(0,         0)   # Di bawah 20jt      
)

def hitung_komisi(total_penjualan, skema, index=0):
  if total_penjualan > skema[index][0]:
    return skema[index][1]
  return hitung_komisi(total_penjualan, skema, index + 1)
  
nama_sales = input('masukkan nama sales : ')
total_penjualan = int(input('masukkan total harga : '))
persen = hitung_komisi(total_penjualan, skema_komisi)

print(f'nama sales : {nama_sales}')
print(f'persen komisi : {persen}')
print(f'nilai komisi : Rp{total_penjualan*persen/100 :,.0f}')
