import threading
import time

t_0 = time.time()

n_threads=2
buffer = str()
mutex = threading.Semaphore(1)

def hello():
    global buffer
    mutex.acquire()
    for x in 'hello world ':
        buffer += x
        time.sleep(1e-6)
    mutex.release()

def hello_loop():
    while time.time()-t_0 < 1:
        hello()


threads = []
for i in range(n_threads):
    thread = threading.Thread(target=hello_loop)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(buffer)
print(len(buffer))
