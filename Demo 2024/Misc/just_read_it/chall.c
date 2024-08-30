#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[])
{
    char flag[48] = "GRF24{FAKE_FLAG}";
    char input[64];

    puts("");
    puts("haiiiiii, tugas kamu hari ini adalah memberikan aku input");
    puts("kalau input nya tepat, nanti ada hadiah nya!\n");

    if (argv[1] != NULL)
    {
        strcpy(input, argv[1]);
        printf("Kamu telah memasukkan: %s\n", input);
        if (strcmp(flag, input) == 0)
        {
            puts("kok kamu tau sihh, kamu jagooo >w<");
            return 0;
        }
        else
        {
            puts("masih belum :(");
            return 1;
        }
    }
    else
    {
        puts("aku mau nya input kamu :(");
        puts("caranya:\n./chall [input kalian]");
        return 1;
    }
}
