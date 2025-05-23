def jarak(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

titik = []
for i in range(3):
    x = float(input(f"Masukkan x({i+1}): "))
    y = float(input(f"Masukkan y({i+1}): "))
    titik.append([x, y])

a = jarak(titik[0], titik[1])
b = jarak(titik[1], titik[2])
c = jarak(titik[2], titik[0])

if a == b or b == c or c == a:
    print("Terbentuk segitiga sama kaki.")
else:
    print("Tidak berbentuk segitiga sama kaki.")