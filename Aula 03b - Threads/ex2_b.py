import threading
import time

t_0 = time.time()

def read_sensor(sensor_name):
    print(sensor_name, 'time:', (time.time()-t_0)*1000)

def read_sensor_loop(sensor_name, interval):
    for i in range(10):
        read_sensor(sensor_name)
        time.sleep(interval)

thread1 = threading.Thread(target=read_sensor_loop,args=("sensor_1",0.1))
thread1.start()
thread2 = threading.Thread(target=read_sensor_loop,args=("sensor_2",0.25))
thread2.start()
thread3 = threading.Thread(target=read_sensor_loop,args=("sensor_3",0.4))
thread3.start()

thread1.join()
thread2.join()
thread3.join()
