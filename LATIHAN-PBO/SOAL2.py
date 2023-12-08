# IF ELSE PADA FOR LOOP
print("Mengecek Bilangan Ganjil dan Genap dengan For Loop:")
for i in range(1, 7):
    if i % 2 == 0:
        print(f"{i} adalah bilangan genap")
    else:
        print(f"{i} adalah bilangan ganjil")



#CONTOH LAINNYA IF ELSE PADA FOR LOP

print("\nMengecek Bilangan Kelipatan 2 dan 3")
for number in range(2, 8):
    if number % 2 == 0 and number % 3 == 0:
        print(f"{number} adalah kelipatan 2 dan 3")
    elif number % 2 == 0:
        print(f"{number} adalah kelipatan 2")
    elif number % 3 == 0:
        print(f"{number} adalah kelipatan 3")
    else:
        print(number)
 
#IF ELSE PADA WHILE LOOP
# Menghitung jumlah angka genap dan ganjil dalam rentang tertentu menggunakan while loop dan if else
print("\nMenghitung jumlah bilangan ganjil dan genap")
rentang_awal = 1
rentang_akhir = 10

angka = rentang_awal
jumlah_genap = 0
jumlah_ganjil = 0

while angka <= rentang_akhir:
    if angka % 2 == 0:
        jumlah_genap += 1
    else:
        jumlah_ganjil += 1
    angka += 1

print(f"Jumlah angka genap dalam rentang {rentang_awal} sampai {rentang_akhir}: {jumlah_genap}")
print(f"Jumlah angka ganjil dalam rentang {rentang_awal} sampai {rentang_akhir}: {jumlah_ganjil}")



