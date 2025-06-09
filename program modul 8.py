with open("data_praktikan.txt", "w") as f:
    f.write("2410431001,Rifqa,80,90,95\n")
    f.write("2410431002,Rosa,80,85,90\n")
    f.write("2410431003,Salma,90,95,100\n")
    f.write("2410431004,Zahra,75,80,85\n")
    f.write("2410431005,Aulya,90,95,100\n")
    f.write("2410431006,Lexa,100,95,100\n")
    f.write("2410431005,Aysi,90,95,80\n")
    f.write("2410431005,Sari,90,100,100\n")
    f.write("2410431005,Azizah,90,100,100\n")
    f.write("2410431005,Akbar,90,95,95\n")

file = open("data_praktikan.txt", "r")
data = file.readlines()
file.close()

nilai_akhir = []
nama_list = []

file2 = open("data_nilai_akhir.txt", "w")
for d in data:
    nim, nama, pretest, postest, tugas = d.strip().split(",")
    pretest = float(pretest)
    postest = float(postest)
    tugas = float(tugas)
    total = 0.35 * pretest + 0.35 * postest + 0.3 * tugas
    nilai_akhir.append(total)
    nama_list.append(nama)
    file2.write(f"{nim},{nama},{pretest},{postest},{tugas},{round(total,2)}\n")
file2.close()

rata2 = sum(nilai_akhir) / len(nilai_akhir)
tertinggi = max(nilai_akhir)
terendah = min(nilai_akhir)
bawah_rata2 = 0

for nilai in nilai_akhir:
    if nilai < rata2:
        bawah_rata2 += 1

print("\nHasil Analisis:")
print("Rata-rata nilai akhir:", round(rata2,2))
print("Nilai tertinggi:", round(tertinggi,2), "oleh", nama_list[nilai_akhir.index(tertinggi)])
print("Nilai terendah:", round(terendah,2), "oleh", nama_list[nilai_akhir.index(terendah)])
print("Jumlah yang di bawah rata-rata:", bawah_rata2)