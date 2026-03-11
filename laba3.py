r = float(input("радиус: "))
pi = 3.14159
s = pi * r ** 2
print("площадь: ", s)

#--------------------------------------

a = float(input("введите а (не равен 0): "))
b = float(input("введите b: "))
if a != 0:
    x = -b / a
    print("корень: ", x)
else:
    print("a не равно 0")

#---------------------------------

c = float(input("введите цельсия: "))
f = 9 / 5 * c + 32
print(f"фаренгейт {f}")
a = float(input("введите число: "))
b = float(input("введите число: "))
c = float(input("введите число: "))
avg = (a + b + c) / 3
print("среднее: ", avg)

#------------------------------

one = 5 + 2 * 3 - 4 // 2
two = (3 + 5) * (2 + 4) // 2
th = -3 + 6 // 2 * 4
ff = 5 + 4 * 5 ** 2 + 7
print(one)
print(th)
print(two)
print(ff)

