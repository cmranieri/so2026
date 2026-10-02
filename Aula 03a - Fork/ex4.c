#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int pid = fork();

    if (pid == 0) {
        printf("Filho (zumbi): PID = %d\n", getpid());
        return 0; // termina imediatamente
    } else {
        printf("Pai: dormindo 10 segundos (verifique com `ps`)\n");
        sleep(10);
        wait(NULL);
    }
    return 0;
}
