a = [
      [[1,2],
      [3,2]],
      
      [[4,3],
      [5,2]],

      [[2,5],
      [1,6]]
    ]


print(a[1][0][1])
print("Insyaallah akan terbuka 19 juta lapangan pekerjaan")

y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")
print(x)


import math
x = input("Enter a number:")
y = math.sqrt(float(x))
print(f"The square root of {x} is {y}")


print(angka)

"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 1, in <module>
    print(angka)
NameError: name 'angka' is not defined
"""


bukan_angka = '1'
bukan_angka + 2
"""
Output:
Traceback (most recent call last):
  File "/home/glot/main.py", line 2, in <module>
    bukan_angka + 2
TypeError: can only concatenate str (not "int") to str
"""


try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')


var_dict = {"rata_rata": "1.0"}

try:
    print(f"rata-rata adalah {var_dict['rata_rata']}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")
    
"""
Output:
rata-rata adalah 1.0
Kode ini dieksekusi jika tidak ada exception.
Kode ini dieksekusi terlepas dari ada atau tidaknya exception.
"""

try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    
    hasil = angka1 / angka2
    print("Hasil pembagian:", hasil)

except ValueError:
    print("Input harus berupa angka!")

except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")

else:
    print("Perhitungan berhasil dilakukan.")

finally:
    print("Program selesai dijalankan.")