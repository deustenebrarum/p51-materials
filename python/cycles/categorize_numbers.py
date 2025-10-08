while True:
    number = int(input())
    if number == 7:
        break
    if number == 5:
        continue
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

print("Good bye")
