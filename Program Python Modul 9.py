import time
import os
from termcolor import colored, cprint

teks = " Happy Eid "
lebar = 20
lapisan = " " * lebar
pergeseran = lapisan + teks + lapisan

for i in range(len(pergeseran) - lebar + 1):
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    tampilan = pergeseran[i:i + lebar]  
    cprint(tampilan, 'green')
    time.sleep(0.2)  