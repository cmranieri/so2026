#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int pid = fork();

    if (pid < 0) {
        return 1;
    }
    if (pid == 0) {
        // Filho
        printf("Filho: meu PID é %d\n", getpid());
    } else {
        // Pai
        printf("Pai: meu PID é %d\n", getpid());
        printf("Pai: o PID do meu filho é %d\n", pid);
        wait(NULL); // espera o filho terminar
    }
    return 0;
}
