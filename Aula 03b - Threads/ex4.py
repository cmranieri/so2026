import threading
import time

a = 1
b = 1

lock_s = True

def soma():
    global a,b,lock_s
    for i in range(5):
        while lock_s:
            pass
        aux = a
        a = a+b
        b = aux
        print('a = ', a, '; b = ', b)
        lock_s = True
        time.sleep(1)

def multiplica():
    global a,b,lock_s
    for i in range(5):
        while not lock_s:
            pass
        aux = a
        a = a*b
        b = aux
        print('a = ', a, '; b = ', b)
        lock_s = False
        time.sleep(1)

threads = []

thread = threading.Thread(target=soma)
threads.append(thread)
thread.start()

thread = threading.Thread(target=multiplica)
threads.append(thread)
thread.start()

for thread in threads:
    thread.join()
