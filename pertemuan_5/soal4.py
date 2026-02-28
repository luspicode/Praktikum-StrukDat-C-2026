gudang_pc = [ 
{"item": "Monitor", "harga": 1500000, "stok": 5}, 
{"item": "Keyboard", "harga": 400000, "stok": 12}, 
{"item": "Mouse", "harga": 250000, "stok": 20} 
] 

#1. 
tambah_dict = {"kategori" : "Aksesoris"}
gudang_pc[1].update(tambah_dict)

#2. 
gudang_pc.append({"item" : "Headset", "harga" : 35000, "stok" : 8})
print(gudang_pc)

#3. 
for duit in gudang_pc:
  aset = duit["harga"] * duit["stok"]
  print(f"Item: {duit["item"]} | total aset: {aset}")