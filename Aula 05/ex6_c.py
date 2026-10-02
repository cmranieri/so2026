import threading
import time

n_readers = 10
n_writers = 2
running = True
reader_count = 0

mutex = threading.Lock()  # Protege reader_count
resource_sem = threading.Semaphore(1)
entry_sem = threading.Semaphore(1)  # Controla a entrada de leitores e escritores.

reader_status = ['descansando'] * n_readers
writer_status = ['descansando'] * n_writers
reads = [0] * n_readers
writes = [0] * n_writers


def show_status():
    while running:
        print('Leitores:  ', reader_status)
        print('Escritores:', writer_status)
        time.sleep(0.5)


def reader(i):
    global reader_count

    while running:
        reader_status[i] = 'esperando'
        with entry_sem:
            with mutex:
                reader_count += 1
                if reader_count == 1:
                    resource_sem.acquire()  # Primeiro leitor bloqueia escritores.

        reader_status[i] = 'lendo'
        time.sleep(0.02)
        reads[i] += 1

        with mutex:
            reader_count -= 1
            if reader_count == 0:
                resource_sem.release()  # Último leitor libera o recurso.

        reader_status[i] = 'descansando'
        time.sleep(1e-3)


def writer(i):
    while running:
        writer_status[i] = 'esperando'
        # Fecha a entrada e espera os leitores atuais terminarem.
        entry_sem.acquire()

        resource_sem.acquire()
        writer_status[i] = 'escrevendo'
        time.sleep(0.02)
        writes[i] += 1
        resource_sem.release()

        entry_sem.release()  # Reabre a entrada após escrever.
        writer_status[i] = 'descansando'
        time.sleep(0.01)


reader_threads = [threading.Thread(target=reader, args=(i,))
                  for i in range(n_readers)]
writer_threads = [threading.Thread(target=writer, args=(i,))
                  for i in range(n_writers)]
status_thread = threading.Thread(target=show_status)


for thread in reader_threads:
    thread.start()
for thread in writer_threads:
    thread.start()
status_thread.start()

time.sleep(3)
running = False

# As operações pendentes terminam; sem novas leituras, escritores podem avançar.
for thread in reader_threads + writer_threads:
    thread.join()
status_thread.join()

print('Leituras por leitor:', reads)
print('Escritas por escritor:', writes)
