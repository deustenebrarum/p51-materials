def sum_and_count_digits(number):
    sum_ = 0
    count = 0
    while number != 0:
        sum_ += number % 10
        number //= 10
        count += 1
    return sum_, count


def get_result_by_menu(sum_, count):
    print(
        '1) Количество\n' +
        '2) Сумма\n' +
        '3) Среднее арифметическое\n'
    )
    choice = input()
    match choice:
        case '1':
            return count
        case '2':
            return sum_
        case '3':
            return sum_ / count
        case _:
            print("Нет такого варианта")
    return None


def main():
    while True:
        number = int(input())
        digits_sum, digits_count = sum_and_count_digits(number)

        result = get_result_by_menu(digits_sum, digits_count)
        if result is not None:
            print(result)
        to_exit = input("Продолжить?(Y/n): ") == 'n'
        if to_exit:
            break


if __name__ == "__main__":
    main()
