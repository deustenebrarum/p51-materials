# a = 50
# print(a % 7 == 0)
# if a % 7 == 0:
#     print("a делится")
# else:
#     print("a не делится")
# a = ...

# print((a > 7 and a < 5) == False)
# print(a == a)
# print(a or a)
# print(a and a)
# print(not (not (a)))

# if a == 4:
#     print("a равно 4")
# else:
#     print("a не равно 4")

# age = int(input())
# print("Passed" if age >= 18 else "Blocked")

# if age >= 18:
#     print("Passed")
# else:
#     print("Blocked")

# pass_text = "Blocked"
# if age >= 18:
#     pass_text = "Passed"

# print(pass_text)

# number = int(input())

# if number % 7 == 0:
#     print("Number is dividable by 7")
# else:
#     print("Number is not dividable by 7")


# a, b = int(input()), int(input())

# if a > b:
#     print(f"Большее число: {a}")
# elif b > a:
#     print(f"Большее число: {b}")
# else:
#     print("Числа равны")

# if a != b:
#     print(f"Большее число: {a if a > b else b}")
# else:
#     print("Числа равны")
# print(
#     f"Большее число {a}" if a > b
#     else f"Большее число {b}" if b > a
#     else "Числа равны"
# )

# print(
#     "Числа равны" if a == b
#     else f"Большее число {a if a > b else b}"
# )

a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))

print(
    '1. Sum\n' +
    '2. Difference\n' +
    '3. Mean\n' +
    '4. Product'
)

choice = input()

# if choice == '1':
#     print(a + b)
# elif choice == '2':
#     print(a - b)
# elif choice == '3':
#     print((a + b) / 2)
# elif choice == '4':
#     print(a * b)
# else:
#     print("No such variant")

match choice:
    case '1':
        print(a + b)
    case '2':
        print(a - b)
    case '3':
        print((a + b) / 2)
    case '4':
        print(a * b)
    case _:
        print("No such variant")
