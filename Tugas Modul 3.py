#inputkan nilai pertama 
#inputkan nilai kedua
#tampilkan pilihan operasi
#pilih salah satu operasi yang akan diproses
#tampilkan hasil operasi
#inputkan pilihan pengulangan
#tampilkan hasil pengulangan
#selesai

import os
os.system('cls')
while True:
    a = float(input("masukkan angka pertama = "))
    b = float(input("masukkan angka kedua = "))

    print("pilih operasi: ")
    print(f"1. penjumlahan")
    print(f"2. pengurangan")
    print(f"3. perkalian")
    print(f"4. pembagian")
    pilihan_operasi = input("pilihan operasi: ")

    if pilihan_operasi == "penjumlahan":
        hasil = a + b
    elif pilihan_operasi == "pengurangan":
        hasil = a - b
    elif pilihan_operasi== "perkalian":
        hasil = a * b
    elif pilihan_operasi == "pembagian":
        hasil = a / b
    else:
        hasil = "pilihan operasi tidak valid"


    print(f"hasil = {hasil}")

    perintah = input("perintah : ")
    if perintah == "berhenti":
        break
    elif perintah == "lanjut":
        pass