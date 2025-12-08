import sqlite3
import os
from python.databases.sql_basics_calc import create_table, save_calculation, show_history


def test_calculator():
    # Удаляем старую базу данных, если она существует
    if os.path.exists('calculator.db'):
        os.remove('calculator.db')
    
    print("Тестируем создание таблицы...")
    create_table()
    print("Таблица создана успешно!")
    
    print("\nТестируем сохранение вычислений...")
    save_calculation(10, 5, '+', 15)
    save_calculation(10, 5, '-', 5)
    save_calculation(10, 5, '*', 50)
    save_calculation(10, 5, '/', 2)
    print("Вычисления сохранены успешно!")
    
    print("\nПроверяем содержимое базы данных:")
    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM calculations ORDER BY id')
    records = cursor.fetchall()
    for record in records:
        print(f"ID: {record[0]}, {record[1]} {record[2]} {record[3]} = "
              f"{record[4]} (время: {record[5]})")
    conn.close()
    
    print("\nТестируем отображение истории...")
    show_history()
    
    print("\nВсе тесты пройдены успешно!")


if __name__ == "__main__":
    test_calculator()