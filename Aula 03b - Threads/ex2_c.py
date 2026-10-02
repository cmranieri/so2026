import threading
import time
import random

t_0 = time.time()

def read_sensor(sensor_name):
    print(sensor_name, (time.time()-t_0)*1000)
    r = random.randint(10,50) / 1000
    time.sleep(r)


def read_sensor_loop(sensor_name, interval):
    for i in range(10):
        thread = threading.Thread(target=read_sensor,args=(sensor_name,))
        thread.start()
        time.sleep(interval)


threads = []

thread = threading.Thread(target=read_sensor_loop,args=("sensor_1",0.1))
threads.append(thread)
thread.start()

thread = threading.Thread(target=read_sensor_loop,args=("sensor_2",0.25))
threads.append(thread)
thread.start()

thread = threading.Thread(target=read_sensor_loop,args=("sensor_3",0.4))
threads.append(thread)
thread.start()

for thread in threads:
    thread.join()
