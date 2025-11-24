import asyncio

lock_ = asyncio.Lock()
async def coroutine1():
    print("1")
    await asyncio.sleep(0)
    print("2")
async def coroutine2():
    print("3")
    await asyncio.sleep(0)
    async with lock_:
        print("4")
        await coroutine3()
        print("5")
async def coroutine3():
    print("6")
    print("7")
async def coroutine5():
    print("8")
    await asyncio.sleep(0)
    print("9")
async def coroutine4():
    print("10")
    async with lock_:
        await coroutine5()
        print("11")
async def main():
    tasks = [
        asyncio.create_task(coroutine1()),
        asyncio.create_task(coroutine2()),
        asyncio.create_task(coroutine4())
    ]
    tasks[2].add_done_callback(
        lambda f: print("12")
    )
    await asyncio.wait(tasks)

asyncio.run(main())
