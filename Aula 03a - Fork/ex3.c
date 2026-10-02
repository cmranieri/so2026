#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int pid;
    for (int i = 0; i < 5; i++) {
        pid = fork();
        if (pid == 0) {
            printf("Filho %d: PID = %d\n", i + 1, getpid());
            return 0;
        }
    }
    // Pai espera todos os filhos
    for (int i = 0; i < 5; i++) {
        wait(NULL);
    }
    printf("Pai: meu PID é %d\n", getpid());
    printf("Pai: todos os filhos terminaram.\n");
    return 0;
}
