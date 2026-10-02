import threading
import time

t_0 = time.time()

n_threads=2
buffer = str()

turn = 0

def hello(id):
    global buffer,turn
    while turn != id:
        time.sleep(0)
    for x in 'hello world ':
        buffer += x
        time.sleep(1e-6)
    turn = (id+1) % n_threads

def hello_loop(id):
    while time.time()-t_0 < 1:
        hello(id)


threads = []
for i in range(n_threads):
    thread = threading.Thread(target=hello_loop, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(buffer)
print(len(buffer))
