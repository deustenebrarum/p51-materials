number = int(input())

middle = number % 10_000 // 100

digit6 = number % 10
number //= 10
digit5 = number % 10
number //= 1000
digit2 = number % 10
number //= 10
digit1 = number % 10

result = (
    digit6 * 100_000 + digit5 * 10_000 +
    middle * 100 + digit2 * 10 + digit1
)

print(result)
