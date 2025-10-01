number = int(input())

hundreds_k_count = number // 100_000
if hundreds_k_count < 1 or hundreds_k_count > 9:
    print("Так низя")
else:
    digit6 = number % 10
    number //= 10
    digit5 = number % 10
    number //= 10
    digit4 = number % 10
    number //= 10
    digit3 = number % 10
    number //= 10
    digit2 = number % 10
    number //= 10
    digit1 = number % 10
    
    digit6, digit1 = digit1, digit6

    left_sum = digit1 + digit2 + digit3
    right_sum = digit4 + digit5 + digit6

    print("Счастливое" if left_sum == right_sum else "Не счастливое")
