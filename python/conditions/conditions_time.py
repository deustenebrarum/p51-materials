import time_consts

if __name__ == '__main__':
    hours_post_midnight = int(input('Введите количество часов с полуночи: '))

    print(
        'Осталось до следующей полуночи: '
        '1) часов\n' +
        '2) минут\n' +
        '3) секунд'
    )

    choice = input()

    hours_pre_midnight = time_consts.HOURS_PER_DAY - hours_post_midnight
    minutes_pre_midnight = time_consts.MINUTES_PER_HOUR * hours_pre_midnight
    seconds_pre_midnight = (
        time_consts.SECONDS_PER_MINUTE * minutes_pre_midnight
    )

    match choice:
        case '1':
            print(hours_pre_midnight, ' часов')
        case '2':
            print(minutes_pre_midnight, ' минут')
        case '3':
            print(seconds_pre_midnight, ' секунд')

    if choice == '1':
        print(hours_pre_midnight, ' часов')
    elif choice == '2':
        print(minutes_pre_midnight, ' минут')
    elif choice == '3':
        print(seconds_pre_midnight, ' секунд')
