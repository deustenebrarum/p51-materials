number = int(input())

is_fizz = number % 3 == 0
is_buzz = number % 5 == 0
if 1 > number or number > 100:
    print("Ошибка ввода")
elif is_fizz and is_buzz:
    print("FizzBuzz")
elif is_fizz:
    print("Fizz")
elif is_buzz:
    print("Buzz")
else:
    print(number)
