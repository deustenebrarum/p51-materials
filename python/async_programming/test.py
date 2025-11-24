def algo1(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(n):
            count += 1

    return count


print(algo1([1] * 10))
print(algo1([1] * 11))
