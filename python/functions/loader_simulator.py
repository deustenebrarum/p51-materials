import time


def print_loader():
    print('[', end='')
    for _ in range(10):
        print('==='*100, end='')
        time.sleep(1)
    print(']')


if __name__ == "__main__":
    print_loader()
