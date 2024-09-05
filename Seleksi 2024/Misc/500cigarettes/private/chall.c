#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

// --------------------------------------------------- SETUP

void ignore_me_init_buffering() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

void kill_on_timeout(int sig) {
  if (sig == SIGALRM) {
  	printf("[!] Anti DoS Signal. Patch me out for testing.");
    _exit(0);
  }
}

void ignore_me_init_signal() {
	signal(SIGALRM, kill_on_timeout);
	alarm(60);
}

void readflag()
{
    char flag;
    FILE *fptr;

    fptr = fopen("flag.txt", "r");
    if (fptr == NULL)
    {
        puts("Create your own flag!");
        exit(0);
    }
    flag = fgetc(fptr);
    while (flag != EOF)
    {
        printf("%c", flag);
        flag = fgetc(fptr);
    }
    fclose(fptr);
}

int main()
{
    ignore_me_init_buffering();
    ignore_me_init_signal();
    
    char cigarettes[128];

    printf("%s", "https://youtu.be/yUnu_U2yKXY?t=104\n");
    printf("%s", "How many cigarettes Commander Bortus ordered?\n");
    gets(cigarettes);
    printf("%d\n", strlen(cigarettes));
    if (strlen(cigarettes) > 256) {
            readflag();
	    return 0;
    }
    if (strcmp(cigarettes, "500") == 0) {
        printf("%s", "Correct! but actually only 464 cigarettes appear in the machine\n");
    } else if (atoi(cigarettes) > 500) {
	    printf("%s", "Wow yeah, that's a lot of cigarettes!\nBut no..\n");
    } else {
	    printf("%s", "No, that's incorrect, try again!");
    }
    return 0;
}
