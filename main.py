r = int(input("введите радиус круга :"))
pi = 3.14159
s = r*r**pi
print(f'Площадь круга равна {s}')


a = float(input("Введите a: "))
b = float(input("введите  b: "))
if a != 0:
    x = -b / a
    print("x =, x")
elif b == 0:
    print("решений очень много")
else:
    print("решений нет")
