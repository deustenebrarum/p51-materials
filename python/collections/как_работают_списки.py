a = [1, 2, 3, 4, 6]
# i = 0
# while i < len(a):
#     print(a[i], end=' ')
#     i += 1
# for i in range(len(a)):
#     print(a[i], end=' ')

# для каждого такого номера i из диапазона от 0 до размера массива
# прибавить к общей сумме элемент массива под номером i
sum_ = 0
for i in range(len(a)):
    sum_ += a[i]

sum_ = 0
for item in a:
    sum_ += item

sum_ = 0
for i, item in enumerate(a):
    sum_ += item

print(sum_)

def max_length_item(strings):
    '''Пример решения задач из домашнего задания'''
    max_string = strings[0]
    for item in strings:
        if len(item) > len(max_string):
            max_string = item
    return max_string

