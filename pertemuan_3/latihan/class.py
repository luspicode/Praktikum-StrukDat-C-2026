class Tas:
  def __init__(self, merk, bahan, harga, kapasitas):
    self.merk = merk
    self.bahan = bahan
    self.harga = harga
    self.kapasitas = kapasitas
    
  def promosi_barang (self):
    print(f"halo guys, tas {self.barang} harganya {self.harga} dengan bahan {self.bahan}")

  def kegunaan_barang (self):
    print (f"tas westpack memiliki merk terkenal, namun hanya dapat menagngkat berat {self.kapasitas} ")
    print (f"tas lenovo memiliki kapasitas lebih besar, dan merk {self.merk} yang terkenal")
    print (f"tas Asus memiliki harga termmurah dengan kapasitas tertinggi yaitu {self.kapasitas}")
    
  def ganti_kapasitas (self, kapasitas_baru):
    self.kapasitas = kapasitas_baru
    
tas1 = Tas("Westpack", "katun", 100000, 5)
tas2 = Tas("Lenovo", "polyester", 200000, 7)
tas3 = Tas("Asus", "Latex", 150000, 8)

tas3.ganti_kapasitas(20)
print (tas3.kapasitas)