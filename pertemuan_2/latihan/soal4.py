nilai_siswa = {
"S01": {"nama": "Dina", "tugas": 80, "uts": 75,
"uas": 85},
"S02": {"nama": "Abdul Harris", "tugas": 90, "uts":
88, "uas": 92},
"S03": {"nama": "Sheila", "tugas": 70, "uts": 65,
"uas": 70}
}

#1. tambahkan s04, fafa, t85, uts80, uas90
nilai_siswa["S04"] = {
  "nama": "Fafa",
  "tugas": 85,
  "uts": 80,
  "uas":90
  }

#2. hitung nilai akhir tugas 20%, uts 30, uas 50
for x in nilai_siswa.values():
  final = (x["tugas"]*0.2 + x["uts"]*0.3 + x["uas"]*0.5)

#3. print yang nilai diatas 80
  if final >80:
    print (f"{x["nama"]} = {final}")


print (nilai_siswa["S01"]["nama "])