# задача: написать программу, которая находит сумму всех чисел кратных 9,
# сумму всех четных чисел, сумму всех нечетных чисел, а также
# среднее арифметическое каждого из этих типов чисел
number = int(input())
end = int(input())

multiples_9_sum = 0
count_9_multiples = 0
evens_sum = 0
count_evens = 0
odds_sum = 0
count_odds = 0

while number <= end:
    if number % 9 == 0:
        multiples_9_sum += number
        count_9_multiples += 1
    if number % 2 == 0:
        evens_sum += number
        count_evens += 1
    else:
        odds_sum += number
        count_odds += 1
    number += 1

print(multiples_9_sum)
print(multiples_9_sum / count_9_multiples)
print(evens_sum)
print(evens_sum / count_evens)
print(odds_sum)
print(odds_sum / count_odds)
number = int(input())
end = int(input())

multiples_9_sum = 0
count_9_multiples = 0
evens_sum = 0
count_evens = 0
odds_sum = 0
count_odds = 0

while number <= end:
    if number % 9 == 0:
        multiples_9_sum += number
        count_9_multiples += 1
    if number % 2 == 0:
        evens_sum += number
        count_evens += 1
    else:
        odds_sum += number
        count_odds += 1
    number += 1

print(multiples_9_sum)
print(multiples_9_sum / count_9_multiples)
print(evens_sum)
print(evens_sum / count_evens)
print(odds_sum)
print(odds_sum / count_odds)
