import threading
import time
import monitor

prob = 0.9
max_t = 3
max_len = 10

requests = []
generating = True
processing = True

monitor = monitor.MonitorBuffer(max_len)


def generate_requests():
    t=0
    while generating:
        t += 1
        monitor.inserir(t%5)
        print(f'{t} generated request, queue={monitor.buffer}, len={len(monitor.buffer)}')


def process_requests():
    while processing:
        x = monitor.remover()
        print(f'processing request, queue={monitor.buffer}, len={len(monitor.buffer)}')
        


gen_thread  = threading.Thread(target=generate_requests)
proc_thread = threading.Thread(target=process_requests)

gen_thread.start()
proc_thread.start()

time.sleep(1)
generating = False
processing = False

gen_thread.join()
proc_thread.join()
