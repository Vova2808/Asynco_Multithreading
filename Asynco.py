# Импортируем все нужные библиотеки для асинхронности
import asyncio
import time

# Первая асинхронная функция
async def say_hello():
    print("Привет Мир!")

# Вторая асинхронная функция
async def say_goodbye(i):
    print("Пока Мир!")


# Запуск одновремменно
async def run_all_tasks():
    await asyncio.gather(
        say_hello(),
        say_goodbye()
    )

asyncio.run(run_all_tasks())
print("Все функции были выполненны одновременно")