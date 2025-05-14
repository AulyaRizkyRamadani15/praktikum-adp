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
