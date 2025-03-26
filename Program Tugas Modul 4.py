#inputkan jumlah baris (n), minimal n=4
#cetak pola grid ukuran n x n
#Jika n ganjil maka cetak nilai pada suku tengah yaitu 'HORE'

import os
os.system('cls')
n = int(input('Inputkan jumlah baris: '))
if n < 4:
    print("Jumlah baris minimal 4")
else:
    total_boom = 0
    tengah = n//2
    for i in range(n):
        for k in range(n):
            if i == k == tengah :
                if n % 2 == 1 and i == k == n // 2:
                    print('HORE', end=' ')
                else:
                    print(1, end=' ')
            elif i + k == n - 1:
                print(2, end=' ')
            else:
                print('BOOM', end=' ')
                total_boom += 1
        print()

    print(f"Total BOOM yang muncul sebanyak = {total_boom}")