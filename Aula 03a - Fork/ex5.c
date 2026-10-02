#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int pid = fork();

    if (pid == 0) {
        printf("Filho: PID = %d\n", getpid());
        sleep(10); // Filho vive após a morte do pai
        printf("Filho órfão: meu novo pai é %d\n", getppid());
    } else {
        printf("Pai: morrendo agora\n");
        return 0; // termina imediatamente
    }
    return 0;
}
