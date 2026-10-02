import threading
import time

a = 1
b = 1

def soma():
    global a,b
    for i in range(5):
        aux = a
        a = a+b
        b = aux
        print('a = ', a, '; b = ', b)
        time.sleep(1)

def multiplica():
    global a,b
    for i in range(5):
        aux = a
        a = a*b
        b = aux
        print('a = ', a, '; b = ', b)
        time.sleep(1)

thread1 = threading.Thread(target=soma)
thread2 = threading.Thread(target=multiplica)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
