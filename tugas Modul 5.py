import os
os.system("cls")
#Mulai
#Buatkan array nilai x dari angka -7 sampai 7
#Buatkan tempat kosong untuk menyimpan hasil f(x)
#Lakukan perulangan untuk setiap nilai x
#Cetak nilai x dan f(x)
#Selesai

nilai_x = list(range(-7, 8))
f_x = []
for x in nilai_x:
    if x > 0:
        fx = x**3 - x
    elif x < 0:
        fx = 1 / (x**2)
    else:
        fx = 1
    f_x.append(fx)
    
print(f"|  x  |     f(x)     |")
for i in range(len(nilai_x)):
    print(f"| {nilai_x[i]:3} | {f_x[i]:12f} |")
