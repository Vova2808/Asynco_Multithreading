import asyncio
import time
#pip install colorama
from colorama import init
init()
from colorama import Fore, Back, Style


print(f"{Fore.GREEN}-------------Асинхронные функции-------------{Style.RESET_ALL}")

async def fun1(x):
    print(f"{x} возвести во вторую степень = {x**2}")
    await asyncio.sleep(3)
    print(f'{Fore.YELLOW}fun1 завершена{Style.RESET_ALL}')


async def fun2(x):
    print(f"{x} возвести в 0.5 степень = {x**0.5}")
    await asyncio.sleep(3)
    print(f'{Fore.YELLOW}fun2 завершена{Style.RESET_ALL}')


print(f"{Fore.RED}Начало {time.strftime('%X')}{Style.RESET_ALL}")

loop = asyncio.get_event_loop()
task1 = loop.create_task(fun1(4))
task2 = loop.create_task(fun2(4))
loop.run_until_complete(asyncio.wait([task1, task2]))

print(f"{Fore.RED}Конец {time.strftime('%X')}{Style.RESET_ALL}")

print("")
print(f"{Fore.GREEN}-------------Обычные функции-------------{Style.RESET_ALL}")
time.sleep(2)


##############################################################
def fun1(x):
    print(f"{x} возвести во вторую степень = {x**2}")
    time.sleep(3)
    print(f'{Fore.YELLOW}fun1 завершена{Style.RESET_ALL}')


def fun2(x):
    print(f"{x} возвести в 0.5 степень = {x**0.5}")
    time.sleep(3)
    print(f'{Fore.YELLOW}fun2 завершена{Style.RESET_ALL}')


def main():
    fun1(4)
    fun2(4)

print(f"{Fore.RED}Начало {time.strftime('%X')}{Style.RESET_ALL}")
main()

print(f"{Fore.RED}Конец {time.strftime('%X')}{Style.RESET_ALL}")
