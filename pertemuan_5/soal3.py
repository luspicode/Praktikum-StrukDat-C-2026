ukm_coding = {"Andi", "Budi", "Caca", "Deni"}  
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"} 

#1. yg ada di coding aja
codingaja = ukm_coding - ukm_robotik

#2. gabungan
gabungan = ukm_robotik | ukm_coding
print(gabungan)
#3. 
ada = "Andi" in ukm_robotik
print(ada)