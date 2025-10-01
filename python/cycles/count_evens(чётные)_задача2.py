count = int(input())
end = int(input())

if count % 2 != 0:
    count += 1

while count <= end:
    print(count)
    count += 2
