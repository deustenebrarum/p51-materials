from time_consts import MINUTES_PER_HOUR, SECONDS_PER_MINUTE


size_gb = int(input("Введите размер в гигабайтах: "))
speed_bit = int(input("Введите скорость в битах в секунду: "))

BITS_PER_BYTE = 8

size_bit = size_gb * 1024 * 1024 * 1024 * BITS_PER_BYTE

seconds = size_bit // speed_bit
minutes = seconds // SECONDS_PER_MINUTE
hours = minutes // MINUTES_PER_HOUR

choice = input()

match choice:
    case '1':
        print(hours, 'часов')
    case '2':
        print(minutes, 'минут')
    case '3':
        print(seconds, 'секунд')
