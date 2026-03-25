# -*- coding: utf-8 -*-
import hashlib
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Отключаем экранирование не-ASCII символов, чтобы русский язык отдавался в чистом UTF-8
app.json.ensure_ascii = False

# Списки для генерации имени
ADJECTIVES = [
    "Дерзкий",
    "Сонный",
    "Пухлый",
    "Внезапный",
    "Тревожный",
    "Бешеный",
    "Грустный",
    "Хитрый",
    "Квадратный",
    "Желейный",
    "Мохнатый",
    "Лысый",
    "Сутулый",
    "Эпичный",
    "Священный",
]

NOUNS = [
    "Енот",
    "Банан",
    "Пельмень",
    "Гусь",
    "Капибара",
    "Хомяк",
    "Огурец",
    "Голубь",
    "Таракан",
    "Утконос",
    "Барсук",
    "Шмель",
    "Чебурек",
    "Мандарин",
    "Динозавр",
]

messages = [
    {
        "id": 1,
        "text": "Добро пожаловать в анонимный зоопарк!",
        "author": "Система",
        "time": datetime.now().strftime("%H:%M:%S"),
    }
]
message_id_counter = 2


def generate_author_name(req):
    """
    Генерирует постоянное имя на основе данных клиента,
    которые не меняются при перезагрузке страницы.
    """
    # Собираем "слепок" клиента: IP-адрес + Браузер + Язык
    client_footprint = f"{req.remote_addr}-{req.headers.get('User-Agent', '')}-{req.headers.get('Accept-Language', '')}"

    # Делаем MD5-хеш от этой строки (он всегда будет одинаковым для одинаковой строки)
    # Используем hashlib, так как встроенная функция hash() в Python меняет результат при каждом перезапуске сервера
    hash_hex = hashlib.md5(client_footprint.encode("utf-8")).hexdigest()

    # Превращаем 16-ричный хеш в обычное целое число
    hash_int = int(hash_hex, 16)

    # Берем остаток от деления на длину списка — это даст нам безопасный индекс
    adj_idx = hash_int % len(ADJECTIVES)
    # Чтобы индекс существительного не совпадал жестко с прилагательным,
    # делим хеш на другое число перед взятием остатка
    noun_idx = (hash_int // 100) % len(NOUNS)

    return f"{ADJECTIVES[adj_idx]} {NOUNS[noun_idx]}"


@app.route("/api/v1/messages", methods=["GET", "POST"])
def handle_messages():
    global message_id_counter

    if request.method == "GET":
        last_n = request.args.get("last", default=30, type=int)
        recent_messages = messages[-last_n:] if last_n > 0 else messages
        return jsonify(recent_messages), 200

    if request.method == "POST":
        data = request.get_json()

        if not data or "text" not in data or not str(data["text"]).strip():
            return jsonify({"error": "Пустое сообщение"}), 400

        # Генерируем смешное имя на основе хеша заголовков текущего запроса
        author_name = data.get("author", generate_author_name(request))

        new_message = {
            "id": message_id_counter,
            "text": str(data["text"]).strip(),
            "author": author_name,
            "time": datetime.now().strftime("%H:%M:%S"),
        }

        messages.append(new_message)
        message_id_counter += 1

        return jsonify(new_message), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
