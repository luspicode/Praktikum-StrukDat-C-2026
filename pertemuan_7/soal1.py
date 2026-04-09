daftar_plat = ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
genap = []
ganjil = []

for i in daftar_plat:
  plat = i.split()
  if int(plat[1]) % 2 == 0:
    genap.append(i)
  else :
    ganjil.append(i)
    
    
for i in daftar_plat:
  if int(plat[-5]) % 2 == 0:
    genap.append(i)
  else :
    ganjil.append(i)
print(genap, ganjil)

