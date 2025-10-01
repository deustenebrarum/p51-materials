input = input().strip()

if input.isdigit() and input[0] != '-':
    hours = int(input) % 24
    if hours < 6:
        print('Good night')
    elif hours < 13:
        print('Good morning')
    elif hours < 17:
        print('Good day')
    else:
        print('Good evening')
else:
    print("Ошибка ввода")
