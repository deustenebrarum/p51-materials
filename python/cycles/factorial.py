# Пользователь вводит с клавиатуры число. Требуется
# посчитать факториал числа. Например, если введено 3,
# факториал числа 1*2*3 = 6.
# Формула для расчета факториала: n! = 1*2*3…*n,где
# n — число для расчета факториала.

number = 1
n = int(input())
factorial = 1
# Решение через while
while number <= n:
    factorial *= number
    number += 1
# Решение через for
factorial = 1
for number in range(2, n + 1):
    factorial *= number
