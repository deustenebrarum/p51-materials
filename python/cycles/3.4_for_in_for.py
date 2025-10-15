# count_first = 0
# count_second = 0

# for row in range(10):
#     for col in range(10):
#         print(row + col, end=' ')
#         count_first += 1
#     print()
#     count_second += 1

# print('\n\n')
# print(count_first+count_second)
# for number in range(1, 26):
#     print(number, end=' ')
#     if number % 5 == 0:
#         print()
# exit()
count = 1
for row in range(5):
    # print('Работает первый(внешний) цикл')
    for col in range(5):
        # print('Работает второй(внутренний) цикл')
        print(count, end=' ')
        count += 1
    print()
