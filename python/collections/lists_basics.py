def create_list():
    '''Создание списка'''
    return [1, 2, 3, 4, 5]

# 2. Добавление элемента в конец
def append_element(lst, item):
    lst.append(item)
    return lst

# 3. Вставка элемента по индексу
def insert_element(lst, index, item):
    lst.insert(index, item)
    return lst

# 4. Удаление элемента по значению
def remove_element(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# 5. Удаление элемента по индексу
def pop_element(lst, index=-1):
    return lst.pop(index)

# 6. Получение длины списка
def get_length(lst):
    return len(lst)

# 7. Проверка наличия элемента
def contains_element(lst, item):
    return item in lst

# 8. Получение индекса элемента
def get_index(lst, item):
    return lst.index(item) if item in lst else -1

# 9. Подсчёт количества вхождений
def count_element(lst, item):
    return lst.count(item)

# 10. Сортировка списка
def sort_list(lst: list[int]):
    lst.sort(key=lambda x: -x)
    return lst

# 11. Разворот списка
def reverse_list(lst):
    lst.reverse()
    return lst

# 12. Копирование списка
def copy_list(lst):
    return lst.copy()

# 13. Объединение списков
def extend_list(lst1, lst2):
    lst1.extend(lst2)
    return lst1

# 14. Срез списка
def slice_list(lst, start=0, end=None):
    return lst[start:end]


# 15. Итерация по списку
def iterate_list(lst):
    for item in lst:
        print(item)


# Пример использования всех функций
if __name__ == "__main__":
    my_list = create_list()
    print("Исходный список:", my_list)

    my_list = append_element(my_list, 6)
    print("После добавления 6:", my_list)

    my_list = insert_element(my_list, 0, 0)
    print("После вставки 0 в начало:", my_list)

    my_list = remove_element(my_list, 3)
    print("После удаления 3:", my_list)

    popped = pop_element(my_list, 1)
    print(f"Удалён элемент по индексу 1: {popped}, список: {my_list}")

    print("Длина списка:", get_length(my_list))
    print("Содержит ли 5:", contains_element(my_list, 5))
    print("Индекс 5:", get_index(my_list, 5))
    print("Количество 2:", count_element(my_list, 2))

    sorted_list = sort_list(my_list.copy())
    print("Отсортированный список:", sorted_list)

    reversed_list = reverse_list(my_list.copy())
    print("Развёрнутый список:", reversed_list)

    copied = copy_list(my_list)
    print("Копия списка:", copied)

    extended = extend_list(my_list.copy(), [7, 8])
    print("Расширенный список:", extended)

    sliced = slice_list(my_list, 1, 4)
    print("Срез [1:4]:", sliced)

    print("Элементы списка по одному:")
    iterate_list([10, 20, 30])
