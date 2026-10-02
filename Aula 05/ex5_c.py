import threading
import time

n_philosophers = 5
running = True
status = ['pensando'] * n_philosophers
meals_eaten = [0] * n_philosophers

mutex = threading.Lock()
philosopher_sems = [threading.Semaphore(0) for _ in range(n_philosophers)]


def show_status():
    while running:
        print(status)
        time.sleep(0.1)


def test(i):
    # Deve ser chamada com o mutex adquirido.
    left = (i - 1) % n_philosophers
    right = (i + 1) % n_philosophers

    if (status[i] == 'esperando garfos'
            and status[left] != 'comendo'
            and status[right] != 'comendo'):
        status[i] = 'comendo'
        philosopher_sems[i].release()


def take_forks(i):
    with mutex:
        status[i] = 'esperando garfos'
        test(i)
    # Espera fora do mutex, permitindo que outros devolvam os garfos.
    philosopher_sems[i].acquire()


def put_forks(i):
    with mutex:
        status[i] = 'pensando'
        test((i - 1) % n_philosophers)
        test((i + 1) % n_philosophers)


def philosopher(i):
    while running:
        time.sleep(1e-3)
        take_forks(i)

        time.sleep(1e-3)
        meals_eaten[i] += 1

        put_forks(i)


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
