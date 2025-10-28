# хешкарта или словарь(dict) в python
# - это тип данных, который хранит пары ключ-значение
# Пример:
opposites = {
    'left': 'right',
    'up': 'down',
    'right': 'left',
    'down': 'up'
}
# ^ - словарь, который хранит противоположные стороны
# по стороне слева, будет выдавать сторону справа, например
print(opposites['up'])
# ^ - выдаст right
# операции со словарями

# получение элемента
print(opposites['left'])
# изменение элемента
opposites['left'] = 'right'
print(opposites['left'])
# добавление элемента
opposites['top'] = 'bottom'
print(opposites)
# удаление элемента
opposites.pop('top')
# либо
# del opposites['top']
print(opposites)
# получение всех ключей для перебора
print()
for key in opposites:
    print(key)
print()
# получение всех значений для перебора
for value in opposites.values():
    print(value)
print()
# получение всех пар ключ-значение для перебора
for key, value in opposites.items():
    print(key, value)
print()
# получение ключа или значение по умолчанию
print


# так же существует другой вид хешкарт - множество(set)
# - это тип данных, который хранит уникальные значения
# с моментальным доступом по ключу, но не имеет значений
# Например:
unique_sides = {'left', 'right', 'up', 'down'}
unique_sides.add('left')
print(unique_sides)  # { 'right', 'left', 'down', 'up' }
# ^ только уникальные значения, не по порядку
# операции со множествами
# проверка наличия ключа
print('up' in unique_sides)
# удаление ключа
unique_sides.remove('up')
# установка ключа
unique_sides.add('up')

# проверка наличия элемента в некотором списке
# перебирается линейно
# даже если вы пишите такую проверку
unique_sides = ['left', 'right', 'up', 'down']
if 'up' in unique_sides:
    print('Вы выбрали верхнюю сторону и получили золотой остров')
# технически всё будет работать внутри как код ниже
is_found = False
for side in unique_sides:
    if side == 'top':
        is_found = True
        break
if is_found:
    print('Вы выбрали верхнюю сторону и получили золотой остров')
# а вот такая проверка будет работать практически моментально
unique_sides = {'left', 'right', 'up', 'down'}
if 'top' in unique_sides:
    print('Вы выбрали верхнюю сторону и получили золотой остров')
