def print_cell_line(cell_size, is_black):
    BLACK_SYMBOL = '*'
    WHITE_SYMBOL = '-'
    for _ in range(cell_size):
        print(
            BLACK_SYMBOL if is_black
            else WHITE_SYMBOL,
            end=' '
        )


def is_black_cell(row, column):
    return (row + column) % 2 == 0


def print_chessboard_row(row, row_length, cell_size):
    for row_line in range(cell_size):
        for column in range(row_length):
            print_cell_line(
                cell_size,
                is_black_cell(row, column)
            )
        print()


def print_chessboard(cell_size):
    BOARD_SIZE = 8

    for row in range(BOARD_SIZE):
        print_chessboard_row(row, BOARD_SIZE, cell_size)


if __name__ == "__main__":
    print_chessboard(int(input()))
