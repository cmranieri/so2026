#include<stdio.h>
#include<signal.h>
#include<unistd.h>

void sig_handler(int signo)
{
    printf("\nreceived SIGINT\n");
}

int main(void)
{
    signal(SIGINT, sig_handler);
    while(1) 
        sleep(1);
    return 0;
}
