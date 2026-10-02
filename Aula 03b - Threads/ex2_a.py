# Ler 3 sensores periodicamente
# sensor_1: atualiza a cada 100ms
# sensor_2: atualiza a cada 250ms
# sensor_3: atualiza a cada 400ms

import time

t_0 = time.time()

def read_sensor(sensor_name,t):
    print(sensor_name, 't:', t, 'time:', (time.time()-t_0)*1000)
if __name__=='__main__':
    for t in range(2000):
        if not t % 100:
            read_sensor('sensor_1',t)
        if not t % 250:
            read_sensor('sensor_2',t)
        if not t % 400:
            read_sensor('sensor_3',t)
        time.sleep(1e-3)



