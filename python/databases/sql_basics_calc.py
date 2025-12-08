import os
import sqlite3


def create_table():
    """Создает таблицу для хранения результатов вычислений"""
    conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'calculator.db'))
    cursor = conn.cursor()

    # Создание таблицы, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num1 REAL,
            num2 REAL,
            operation TEXT,
            result REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()


def save_calculation(num1, num2, operation, result):
    """Сохраняет результат вычисления в базу данных"""
    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO calculations (num1, num2, operation, result)
        VALUES (?, ?, ?, ?)
    ''', (num1, num2, operation, result))

    conn.commit()
    conn.close()


def show_history():
    """Показывает историю вычислений"""
    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()

    query = '''SELECT num1, num2, operation, result, timestamp
               FROM calculations ORDER BY timestamp DESC LIMIT 10'''
    cursor.execute(query)
    records = cursor.fetchall()

    print("\nИстория вычислений (последние 10):")
    print("-" * 50)
    for record in records:
        print(f"{record[0]} {record[2]} {record[1]} = {record[3]} "
              f"(время: {record[4]})")

    conn.close()


def make_calculation():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    print("Доступные операции:")
    print("+ - сложение")
    print("- - вычитание")
    print("* - умножение")
    print("/ - деление")

    operation = input("Введите операцию: ")

    result = num1 + num2
    if operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ошибка: деление на ноль!")
            return
    else:
        print("Неверная операция!")
        return

    print(f"Результат: {num1} {operation} {num2} = {result}")

    # Сохраняем результат в базу данных
    save_calculation(num1, num2, operation, result)


def calculator():
    """Основная функция калькулятора"""
    print("Простейший калькулятор с сохранением в базу данных")

    # Создаем таблицу при запуске
    create_table()

    while True:
        print("\nМеню:")
        print("1. Выполнить вычисление")
        print("2. Показать историю")
        print("3. Выйти")

        choice = input("Выберите действие (1-3): ")

        if choice == '1':
            try:
                make_calculation()
            except ValueError:
                print("Ошибка: введите корректные числа!")
            except Exception:
                print("Произошла непредвиденная ошибка!")
        elif choice == '2':
            show_history()
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    calculator()
