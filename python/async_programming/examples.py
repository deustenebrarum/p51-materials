import asyncio
import time


def example_1():
    """
    Пример 1: Асинхронная функция ≠ обычная функция.

    Важно:
      - `async def` создаёт *корутину* (coroutine), а не исполняемый код.
      - Вызов `foo()` без `await` или `asyncio.run()` просто возвращает объект корутины — НИЧЕГО не делает.
    """
    async def hello():
        await asyncio.sleep(1)
        print("async-функция запущена")
        return "Hello, async!"

    # ❌ Это НЕ запускает функцию — лишь создаёт объект!
    coro = hello()
    print("Тип результата вызова async-функции:", type(coro))  # <class 'coroutine'>
    print("Сам объект:", coro)  # <coroutine object hello at 0x...>

    # ✅ Так — запустится
    result = asyncio.run(coro)
    print("Результат после запуска:", result)


def example_2():
    """
    Пример 2: await vs time.sleep() — как НЕ блокировать цикл событий.

    Ключевое:
      - `time.sleep()` — блокирует ВЕСЬ поток, включая event loop.
      - `await asyncio.sleep()` — отдаёт управление event loop'у на время.
    """
    # Mutex, Semaphore
    async def fake_io_task(name: str, delay: float):
        print(f"[{name}] начался (ожидание {delay}s)")
        await asyncio.sleep(delay)  # ← УПРАВЛЕНИЕ УШЛО ОБРАТНО В ЦИКЛ
        print(f"[{name}] завершён")
        return name

    async def main():
        start = time.time()

        # Запускаем 3 задачи ПАРАЛЛЕЛЬНО
        results = await asyncio.gather(
            fake_io_task("A", 1.0),
            fake_io_task("B", 1.2),
            fake_io_task("C", 1.0),
        )

        elapsed = time.time() - start
        print(f"\n→ Все задачи завершены за {elapsed:.2f} сек (должно быть ~1.0)")
        print("Результаты:", results)

    asyncio.run(main())


def example_3():
    """
    Пример 3: async/await ≠ многопоточность.

    Пояснение:
      - Весь async-код выполняется в ОДНОМ потоке.
      - Переключение происходит ТОЛЬКО в точках `await`.
      - CPU-bound задачи НЕ выигрывают от async — только I/O-bound.

    Здесь: две задачи делят один поток, но не мешают друг другу — потому что спят.
    """
    async def cpu_like_task(name: str, steps: int):
        print(f"[{name}] старт (эмуляция CPU-работы БЕЗ await)")
        total = 0
        for i in range(steps):
            total += i * i
            # ⚠️ НИКАКОГО `await` — event loop НЕ ПОЛУЧАЕТ УПРАВЛЕНИЕ!
        print(f"[{name}] завершён, результат = {total % 1000}")
        return total

    async def io_task(name: str):
        print(f"[{name}] ждёт ввод/вывод...")
        await asyncio.sleep(0.1)  # ← здесь управление уйдёт
        print(f"[{name}] продолжает")
        return "OK"

    async def main():
        # Запустим CPU-задачу и IO-задачу одновременно
        t1 = asyncio.create_task(cpu_like_task("CPU", 5_000_000))
        t2 = asyncio.create_task(io_task("IO"))

        # IO-задача НЕ начнётся, пока CPU-задача не закончится!
        await t2
        await t1

    print("Запуск CPU + IO задачи...")
    asyncio.run(main())
    print("\n→ IO-задача 'проснулась' ТОЛЬКО после завершения CPU-задачи.\n"
          "  Это показывает: без `await` — нет кооперативной многозадачности.")


def example_4():
    """
    Пример 4: create_task() vs gather() — управление жизненным циклом.

    Разница:
      - `asyncio.gather()` — ждёт ВСЕ задачи, возвращает результаты списком.
      - `asyncio.create_task()` — запускает задачу 'в фоне', но НЕ ожидает её сам.
        → Чтобы не потерять исключение или результат — надо `await task`.

    Здесь: задача запущена, но main() завершается ДО её окончания → ошибка.
    """
    async def long_task():
        print("→ Долгая задача запущена")
        await asyncio.sleep(1)
        print("→ Долгая задача завершена")
        return 42

    async def main():
        print("1. Запускаем задачу через create_task()")
        task = asyncio.create_task(long_task())

        print("2. Не дожидаясь, завершаем main()...")
        # ❌ task остаётся 'висеть' — и при выходе будет предупреждение:
        #    "Task was destroyed but it is pending!"

    asyncio.run(main())
    # В консоли: RuntimeWarning: coroutine 'long_task' was never awaited


def example_5():
    """
    Пример 5: Правильная обработка исключений в асинхронном коде.

    Важно:
      - Исключение в корутине НЕ всплывёт само — его нужно явно обработать.
      - `await task` или `await asyncio.gather(...)` пробрасывают исключения.
      - Без этого — `Task exception was never retrieved`.
    """
    async def faulty():
        await asyncio.sleep(0.1)
        raise RuntimeError("💥 Всё сломалось!")

    async def safe_gather():
        try:
            await asyncio.gather(faulty(), faulty())
        except RuntimeError as e:
            print("Исключение поймано в gather():", e)

    async def unsafe_task():
        asyncio.create_task(faulty())
        # ❌ Никакого await — исключение потеряется
        await asyncio.sleep(0.2)
        print("main() завершился, но задача упала...")

    print("→ Проверка безопасного gather()")
    asyncio.run(safe_gather())

    print("\n→ Проверка небезопасного create_task() (будет warning)")
    asyncio.run(unsafe_task())


def example_6():
    """
    Пример 6: async-генераторы и асинхронные контекстные менеджеры.

    Возможности Python ≥3.6:
      - `async def __aiter__`, `async for`
      - `async def __aenter__`, `async with`

    Здесь: имитация асинхронной итерации по 'стриму данных'.
    """
    class AsyncDataStream:
        def __init__(self, items):
            self.items = items
            self.index = 0

        def __aiter__(self):
            return self

        async def __anext__(self):
            if self.index >= len(self.items):
                raise StopAsyncIteration
            item = self.items[self.index]
            self.index += 1
            await asyncio.sleep(0.1)  # имитация задержки сети/диска
            return item

    async def async_context():
        print("Открываем асинхронное соединение...")
        await asyncio.sleep(0.05)
        return "CONN"

    class AsyncDB:
        async def __aenter__(self):
            self.conn = await async_context()
            return self.conn

        async def __aexit__(self, *exc):
            print("Закрываем соединение...")
            await asyncio.sleep(0.05)

    async def main():
        print("→ Асинхронная итерация:")
        async for chunk in AsyncDataStream(["A", "B", "C"]):
            print("Получен чанк:", chunk)

        print("\n→ Асинхронный контекстный менеджер:")
        async with AsyncDB() as conn:
            print("Работаем с:", conn)

    asyncio.run(main())


if __name__ == "__main__":
    example_3()
