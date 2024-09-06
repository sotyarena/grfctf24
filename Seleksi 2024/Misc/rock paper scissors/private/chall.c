#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <time.h>

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


int rng() {
        srand(time(0));
        int num = rand() % 3;
        return num;
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

int main() {

        char confirmation[16];
	int maxPoint = 10;
        int turn = 0;
        int robot = 0;
        int player = 0;
        char *rps[] = {"rock", "paper", "scissors"};

	ignore_me_init_signal();

        printf("%s", "Hello Player!, welcome to my game :3\n");
        sleep(1);
        printf("%s", "We are gonna play Rock/Paper/Scissors, and I will reward you a flag if you manage to get 10 points :3\n");
        sleep(1);

        while (1) {
                printf("%s", "Do you wanna compete against the robot?\n[yes/no]\n");
                scanf("%s", confirmation);
                if (strcmp(confirmation, "no") == 0) {
                printf("%s", "GAME CLOSED.. Exitting..\n");
                return 0;
                } else if (strcmp(confirmation, "yes") == 0) {
                        break;
                } else {
                        continue;
                }
        }

        printf("%s", "\nGAME HAS STARTED\n");
	sleep(1);
	printf("%s", "This game is not rigged, I promise\n\n");
	sleep(1.3);
        while(turn < 25) {
            printf("==== SCORES ====\nRobot: %d\nYou  : %d\n==== ====== ====\n",robot,player);
            if (player == maxPoint) {
                    printf("You have won, but at what cost?\n");
		    sleep(3);
		    puts("shell ;)");
		    system("/bin/rbash");
                    return 0;
            } else if (robot == maxPoint) {
		    printf("*sad trombone* You lose!, but you can still try again!\n");
		    return 0;
	    }
            char battle[16] = "";
            printf("%s", "[rock/paper/scissors]\n");
            scanf("%s", battle);
                    if (strcmp(battle, "rock") == 0) {
                            if(strcmp(rps[rng()], "scissors") == 0) {
                                    printf("rock vs scissors\nRock wins!\n\n");
                                    player++;
                            } else if (strcmp(rps[rng()], "paper") == 0) {
                                    printf("rock vs paper\nPaper wins!\n\n");
                                    robot++;
                            } else {
                                    printf("rock vs rock\nDraw!\n\n");
                            }


                    } else if (strcmp(battle,"paper") == 0) {
                            if (strcmp(rps[rng()], "rock") == 0) {
                                    printf("paper vs rock\nRock wins!\n\n");
                                    player++;
                            } else if (strcmp(rps[rng()], "scissors") == 0) {
                                    printf("paper vs scissors\nScissors wins!\n\n");
                                    robot++;
                            } else {
                                    printf("paper vs paper\nDraw!\n\n");
                            }


                    } else if (strcmp(battle,"scissors") == 0) {
                            if (strcmp(rps[rng()],"rock") == 0) {
                                    printf("scissors vs rock\nRock wins!\n\n");
                                    robot++;
                            } else if (strcmp(rps[rng()],"paper") == 0) {
                                    printf("scissors vs paper\nScissors wins!\n\n");
                                    player++;
                            } else {
                                    printf("scissors vs scissors\nDraw!\n\n");
                           }
                    turn++;
		    } else {
                            printf("Invalid opt!!\n");
                    }
	}
}
