import os
import time
from termcolor import colored, cprint

def loading():
    for i in range(0, 101, 10):
      print("loading...")
      cprint(" " * (i//2), "white", "on_blue", end="")
      cprint(f' {i}%')
      time.sleep(1/2)
      os.system('cls')
loading()

passing_grade = {
    "kedokteran" : 800.0,
    "kedokteran gigi" : 720.13,
    "farmasi" : 769.88,
    "keperawatan" : 744.21,
    "hukum" : 755.24,
    "ekonomi dan bisnis" : 754.78,
    "pertanian" : 615.30,
    "teknologi pertanian" : 636.72,
    "peternakan" : 560.0,
    "ilmu budaya" : 640.26,
    "ilmu sosial dan ilmu politik" : 660.83,
    "mipa" : 620.41,
    "teknik" : 718.19,
    "kesehatan masyarakat": 740.34,
    "perikanan dan ilmu kelautan" : 550.0 
}

def loading_proses(teks="Memeriksa kelulusan"):
    for i in range(3):
        print(f"{teks}{'.' * (i + 1)}", end="\r")
        time.sleep(0.5)

def hitung_rata(nilai_tes):
    return sum(nilai_tes.values()) / len(nilai_tes)

def cek_kelulusan(rata_rata, fakultas):
    if fakultas in passing_grade:
        return rata_rata >= passing_grade[fakultas]

def simpan_hasil(nama, fakultas, nilai_tes, rata_rata, status):
    with open("hasil_kelulusan.txt", "a") as file:
        nilai_str = ', '.join([f"{k}: {v}" for k, v in nilai_tes.items()])
        file.write(f"{nama}, {fakultas}, {nilai_str}, Rata-rata: {rata_rata:.2f}, Status: {status}\n")

def tampilkan_ringkasan():
    print("\n=== DATA TERAKHIR TERSIMPAN ===") 

    print(f"\n| {'Nama':<20} | {'Fakultas':<35} | {'Rata-rata':<10} | {'Status':<13} |")
    print("-" * 85)

    with open("hasil_kelulusan.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            if len(parts) >= 5:
                nama = parts[0]
                fakultas = parts[1]
                rata_rata = parts[-2].split(": ")[1] if ": " in parts[-2] else "-"
                status = parts[-1].split(": ")[1] if ": " in parts[-1] else "-"
                print(f"| {nama:<20} | {fakultas:<35} | {rata_rata:<10} | {status:<13} |")


def main():
    print("=== SELAMAT DATANG DI SIMULASI KELULUSAN UTBK ===")
    data_siswa = []  


    while True:
        nama = input(f"\nMasukkan nama Anda: ")

        try:
            nilai_utbk = {
                "Penalaran Umum": int(input("Masukkan nilai Penalaran Umum : ")),
                "Pengetahuan Kuantitatif": int(input("Masukkan nilai Pengetahuan Kuantitatif : ")),
                "Pengetahuan dan pemahaman Umum": int(input("Masukkan nilai Pengetahuan dan pemahaman Umum : ")),
                "Kemampuan Membaca dan Menulis": int(input("Masukkan nilai Kemampuan Membaca dan Menulis : ")),
                "Literasi Bahasa Inggris": int(input("Masukkan nilai Literasi Bhs Inggris : ")),
                "Literasi Bahasa Indonesia": int(input("Masukkan nilai Literasi Bhs Indo : ")),
                "Penalaran Kuantitatif": int(input("Masukkan nilai Penalaran Kuantitatif : ")),
            }
        except ValueError:
            print("Input nilai harus berupa angka!")
            continue

        rata_rata = hitung_rata(nilai_utbk)

        print("\nPilih Fakultas:")
        for i, fakultas in enumerate(passing_grade.keys()):
            print(f"{i + 1}. {fakultas}")
        try:
            pilihan = int(input("Masukkan nomor Fakultas pilihan: "))
            if 1 <= pilihan <= len(passing_grade):
                fakultas_dipilih = list(passing_grade.keys())[pilihan - 1]
            else:
                print("Pilihan tidak valid.\n")
                continue
        except :
            print("Masukkan harus berupa angka!\n")
            continue

        loading_proses()

        hasil = cek_kelulusan(rata_rata, fakultas_dipilih)
        status = "LULUS" if hasil else "TIDAK LULUS"
        lolos = rata_rata >=  passing_grade[fakultas_dipilih]

        print("\n--- HASIL KELULUSAN ---")
        print(f"Nama       : {nama}")
        print(f"Prodi      : {fakultas_dipilih}")
        for k, v in nilai_utbk.items():
            print(f"{k:<26}: {v}")
        print(f"Rata-rata  : {rata_rata:.2f}")
        warna = ("blue", "on_cyan") if lolos else ("red", "on_yellow")
        cprint(f"[{nama}] STATUS: {status}", warna[0], warna[1])
        if status == "TIDAK LULUS":
         print(f"Maaf, Anda tidak mencapai passing grade untuk prodi {fakultas_dipilih} ({passing_grade[fakultas_dipilih]}).")

        data_siswa.append([nama, fakultas_dipilih, rata_rata, status])
        simpan_hasil(nama, fakultas_dipilih, nilai_utbk, rata_rata, status)

        perulang = input("\nIngin mengecek peserta lain? (y/n): ")
        if perulang != 'y':
            print("Terima kasih telah menggunakan program ini.")
            print("Program ini hanyalah simulasi sederhana dan tidak mencerminkan hasil UTBK sebenarnya.")
            print("Cek informasi resmi SNPMB untuk hasil yang valid.")
            tampilkan_ringkasan()
            print("\n=== DATA PESERTA ===")
            print(f"| {'Nama':<20} | {'Fakultas':<35} | {'Rata-rata':<10} | {'Status':<13} |")
            print("-" * 85)
            for baris in data_siswa:
                print(f"| {baris[0]:<20} | {baris[1]:<35} | {baris[2]:<10.2f} | {baris[3]:<13} |")

            break

main()