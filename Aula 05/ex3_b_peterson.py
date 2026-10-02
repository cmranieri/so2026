import threading
import time

t_0 = time.time()

n_threads=2
buffer = str()

turn = 0
interested = [False, False]

def hello(id):
    global buffer,turn
    other = 1 - id
    interested[id] = True
    turn = other
    while interested[other] and turn == other:
        pass
    for x in 'hello world ':
        buffer += x
        time.sleep(1e-6)
    interested[id] = False

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
