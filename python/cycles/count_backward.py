start = int(input())
count = int(input())

if count % 2 == 0:
    count -= 1

while start <= count:
    print(count)
    count -= 2
