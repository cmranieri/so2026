#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int pid = fork();

    if (pid == 0) {
        // Filho
        printf("Filho: meu PID é %d\n", getpid());
        execlp("ls", "ls", "-l", NULL);
    } else {
        // Pai
        wait(NULL);
        printf("Pai: meu PID é %d\n", getpid());
        printf("Pai: o PID do meu filho é %d\n", pid);
    }
    return 0;
}
