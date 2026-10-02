import threading
import time

n_philosophers = 5
running = True
status = ['pensando'] * n_philosophers
meals_eaten = [0] * n_philosophers

forks = [threading.Semaphore(1) for _ in range(n_philosophers)]
table_sem = threading.Lock()


def show_status():
    while running:
        print(status)
        time.sleep(0.1)

def philosopher(i):
    left = i
    right = (i + 1) % n_philosophers

    while running:
        status[i] = 'pensando'
        time.sleep(1e-3)

        status[i] = 'esperando garfos'
        table_sem.acquire()
        forks[left].acquire()
        forks[right].acquire()

        status[i] = 'comendo'
        time.sleep(1e-3)
        meals_eaten[i] += 1

        forks[right].release()
        forks[left].release()
        table_sem.release()


threads = [threading.Thread(target=philosopher, args=(i,))
           for i in range(n_philosophers)]
status_thread = threading.Thread(target=show_status)

status_thread.start()
for thread in threads:
    thread.start()

time.sleep(2)
running = False

status_thread.join()
for thread in threads:
    thread.join()

print(meals_eaten)
