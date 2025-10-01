number = int(input())
power = int(input())

result = 1

if power < 0 or power > 7:
    print("Ошибка ввода")
else:
    if power > 0:
        result *= number
    if power > 1:
        result *= number
    if power > 2:
        result *= number
    if power > 3:
        result *= number
    if power > 4:
        result *= number
    if power > 5:
        result *= number
    if power > 6:
        result *= number
    if power > 7:
        result *= number

    print(result)
