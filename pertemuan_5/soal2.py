data_aktivitas = [("Diki", 88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)] 

for mhs, nilai in data_aktivitas:
  if nilai > 80:
    print (f"{mhs} mendapatkan predikat gold")
    
  elif nilai > 50:
    print (f"{mhs} mendapatkan predikat silver")
  
  else:
    print (f"{mhs} mendapatkan predikat silver")

