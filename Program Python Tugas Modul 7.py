def modulo():
    n = int(input("Masukkan n (1-10): "))
    while n <= 0 or n > 10:
        n = int(input("Masukkan lagi (1-10): "))
    print("Tabel Perkalian Modulo n")
    for i in range(n):
        for j in range(n):
            print((i*j) % n, end=" ")
        print()

def sigma():
    b = int(input("Batas bawah: "))
    a = int(input("Batas atas: "))
    while a < b:
        print("Batas atas harus ≥ batas bawah.")
        a = int(input("Batas atas: "))
    total = 0
    for i in range(b, a+1):
        total += i
    print("Σ x =", total)

def faktorial():
    n = int(input("n = "))
    while n < 0:
        n = int(input("Masukkan n ≥ 0: "))
    hasil = 1
    for i in range(1, n+1):
        hasil *= i
    print(f"{n}! =", hasil)

def rata_rata():
    n = int(input("Banyak data: "))
    while n <= 0:
        n = int(input("Masukkan lagi (n > 0): "))
    data = []
    for i in range(n):
        angka = float(input(f"Data ke-{i+1}: "))
        data.append(angka)
    total = sum(data)
    rata = total / n
    print("Total =", total)
    print("Rata-rata =", rata)

while True:
    print("Menu:")
    print("1. Tabel perkalian modulo n")
    print("2. Mencari nilai Σ x")
    print("3. Mencari nilai n!")
    print("4. Total dan rata-rata data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        modulo()
    elif pilihan == '2':
        sigma()
    elif pilihan == '3':
        faktorial()
    elif pilihan == '4':
        rata_rata()
    elif pilihan == '5':
        print("Program selesai.")
        break
    else:
        print("Silahkan Pilih angka 1-5 saja")