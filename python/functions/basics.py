def название_функции(параметр1, параметр2):
    # тело функции
    pass

# функция суммы


def my_sum(number1, number2):
    return number1 + number2

# s = sum(1, 3)
# with open('test', 'w') as f:
#     f.write(s)
# print(s)
# http.send(s)

# функция возведения в квадрат


def square(number):
    return number * number


# функция нахождения площади окружности по радиусу
def get_circle_area(radius):
    import math
    return math.pi * square(radius)


# функция нахождения наибольшего из двух чисел
def my_max(number1, number2):
    if number1 > number2:
        return number1
    return number2


# функция проверки числа на положительность
def is_positive(number):
    return number > 0


# функция, проверяющая, находится ли число в переданных
#    границах диапазона
def is_in_range(number, start, end):
    return number >= start and number <= end


# функция нахождения модуля числа(делающая его положительным)
def absolute(number):
    if is_positive(number):
        return number
    return -number


# функция проверки на високосный год
def is_leap(year):
    return (
        year % 400 == 0 or
        year % 4 == 0 and year % 100 != 0
    )


def test_is_leap():
    from datetime import datetime
    birthday = datetime(2021, 1, 1)
    if is_leap(birthday.year):
        print('Вы родились в високосный год')
    else:
        print('В году вашего рождения 365 дней')


# функция нахождения наибольшего из 3х чисел
def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    if b > c:
        return b
    return c


def test_max_of_three():
    a = int(input())
    b = int(input())
    c = int(input())

    print(f"Наибольшее число: {max_of_three(a, b, c)}")


# функция, выводящая на экран все целые числа в переданном
#    диапазоне(передаётся два числа - начало и конец)
def print_numbers_in_range(start, end):
    for number in range(start, end):
        print(number)
    # print(*range(start, end))


# функция, считающая сумму всех целых чисел в диапазоне
def sum_range(start, end):
    sum_ = 0
    for number in range(start, end):
        sum_ += number
    return sum_
    # return sum(range(start, end))


# функция, выводящая меню с выбором цвета и выдающая
#    выбор пользователя
RED = "#ff0000"
GREEN = "#00ff00"
BLUE = "#0000ff"


def choose_color_by_menu():
    print(
        "Выберите цвет:"
        "1) Красный" +
        "2) Зелёный" +
        "3) Синий"
    )
    choice = input()
    match choice:
        case '1':
            return RED
        case '2':
            return GREEN
        case '3':
            return BLUE
    return None


def test_choose_color():
    import os
    color = choose_color_by_menu()
    if color == RED:
        os.system("color 40")
    if color == GREEN:
        os.system("color 23")
    if color == BLUE:
        os.system("color 1F")
    print("Цвет изменён успешно")


# функция сортировки двух чисел minmax - возвращает
#    оба числа в порядке возрастания
def minmax(a, b):
    return (a, b) if a < b else (b, a)


def test_sum_range():
    first_border = int(input(
        "Введите первую границу диапазона: "))
    second_border = int(input(
        "Введите левую границу диапазона: "))

    print(sum_range(*minmax(
        first_border, second_border
    )))
