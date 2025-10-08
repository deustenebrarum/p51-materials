# Конвертировать введённое число,
# представляющее собой количество рублей,
# в перечисленные валюты(USD, CYN) на выбор
# с помощью ввода пользователя.
# Повторять это действие,
# пока пользователь не выберет выйти.
import requests
import os
import json
import datetime

path = os.path.dirname(__file__)

with open(path + '/ruble_rates.json', 'r+') as file:
    text = file.read()
# Заготовленные курсы валют
with open(path + '/ruble_rates.json', 'w+') as file:
    if text != '' and text[0] == '{':
        data: dict = json.loads(text)
    else:
        data = {}
    current_date = datetime.datetime.now()
    last_save_date_string = data.get('last_save_date')
    if last_save_date_string is None:
        last_save_date_string = 'Jun 1 2005  1:33PM'
    last_save_date = datetime.datetime.strptime(
        last_save_date_string,
        '%b %d %Y %I:%M%p'
    )
    time_diff = current_date - last_save_date
    if time_diff.days > 0:
        rub_rate_info = requests.get('https://open.er-api.com/v6/latest/RUB')
        rub_rate_info = rub_rate_info.json()['rates']
        rub_rate_info['last_save_date'] = current_date.strftime(
            "%b %d %Y %I:%M%p"
        )
    else:
        rub_rate_info = data
    json.dump(rub_rate_info, file)
RUB_TO_USD = rub_rate_info['USD']
RUB_TO_CNY = rub_rate_info['CNY']

# Повторять постоянно:
while True:
    # Получить ввод от пользователя
    # и конвертировать в int, полученное значение должно
    # представлять количество рублей.
    rubles = int(input())
    # Вывести варианты валют для перевода: USD, CYN,
    print(
        'Варианты конвертации:\n' +
        '1) USD - доллары\n' +
        '2) CNY - юань'
    )
    # получить ввод от пользователя в виде выбранного варианта.
    choice = input()
    # Используя заготовленные курсы USD и  CYN,
    # умножить количество рублей на выбранный вариант курса,
    converted_value = rubles
    if choice == '1':
        converted_value *= RUB_TO_USD
    elif choice == '2':
        converted_value *= RUB_TO_CNY
    # вывести его пользователю.
    print(f"{converted_value:.2f}")
    # Спросить, хочет ли пользователь продолжить,
    print("Хотите продолжить?")
    # получить ввод от пользователя, если он ввёл 'да'
    # вне зависимости от регистра и лишних пробелов,
    # иначе заканчиваем повторения.
    if input().strip().lower() != 'да':
        break
