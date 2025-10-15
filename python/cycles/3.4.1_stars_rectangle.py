rows_count = int(input())
cols_count = int(input())

for row in range(rows_count):
    # print('Работает первый(внешний) цикл')
    for col in range(cols_count):
        # print('Работает второй(внутренний) цикл')
        if (
            row == 0 or row == rows_count - 1 or
            col == 0 or col == cols_count - 1
        ):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
