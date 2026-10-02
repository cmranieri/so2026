#include <stdio.h>
#include <unistd.h>

/* O filho se comunica com o pai usando o pipe.
* pipe() retorna um vetor com descritores para dois arquivos:
* fd[0]: arquivo é somente leitura (receberá a saída do pipe)
* fd[1]: arquivo é somente escrita (envia entrada para o pipe) 
* Pai e filho mantêm seu próprio fd */

int main() {
    int fd[2], child;
    pipe(fd);
    child = fork();

    if (child) { // Este é o pai; leitor
        char buf[1024];
        close(fd[1]); // Fecha seu arquivo de escrita
        read(fd[0], buf, 1024); // Bloqueia esperando filho
        printf("-->%s\n", buf);
        close(fd[0]);
    } else { // Este é o filho; escritor
        close(fd[0]); // Fecha seu arquivo de leitura
        write(fd[1], "hello", 5);
        close(fd[1]);
    }
    return 0;
}
