# Импортируем все нужные библиотеки для многопоточности
import threading

def print_hello(name):
    print("Привет я", name, flush=True)

thread1 = threading.Thread(target=print_hello,kwargs=dict(name='Вася'))
thread2 = threading.Thread(target=print_hello, kwargs=dict(name='Ваня'))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Все функции выполненны одновременно")
