a = (1, 'a', True)
lst = [9, -5, 3]
dct = {'a': 1}
st = {1, 2, 3} | {2, 3, 6}


for pair in enumerate(lst):
    print(hash(pair) % 3)
