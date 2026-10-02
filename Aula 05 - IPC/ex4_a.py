import threading
import time

max_len = 10

requests = []
running = True

full_sem = threading.Semaphore(0)
empty_sem = threading.Semaphore(max_len)

def dispatcher():
    t=0
    while running:
        t += 1
        empty_sem.acquire()
        requests.append(t%5)
        print(f'{t} generated request, queue={requests}, len={len(requests)}')
        full_sem.release()

def worker():
    while running:
        full_sem.acquire()
        x = requests.pop(0)
        print(f'processing request {x}, queue={requests}, len={len(requests)}')
        empty_sem.release()

dispatcher_thread  = threading.Thread(target=dispatcher)
worker_thread_1 = threading.Thread(target=worker)
worker_thread_2 = threading.Thread(target=worker)
dispatcher_thread.start()
worker_thread_1.start()
worker_thread_2.start()
time.sleep(1)
running = False
dispatcher_thread.join()
worker_thread_1.join()
worker_thread_2.join()
