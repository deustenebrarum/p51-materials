import math

diameter = int(input("Диаметр: "))

print(
    "Что посчитать?\n" +
    "1) Площадь\n" +
    "2) Периметр\n"
)

choice = input()

if choice == '1':
    print(math.pi * (diameter/2)**2)
elif choice == '2':
    print(math.pi * diameter)
else:
    print("Нет такого варианта")
