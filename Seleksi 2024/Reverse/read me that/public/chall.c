#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int FLAG[37] = {flag nya bukan disnii :)}; 

int main()
{
	char inputs[48];
	int i;
	printf("I want you to give me the REAL INPUT!\n");
	fgets(inputs,48,stdin);
	for (i=0; i<37; i++) {
		if (inputs[i] != FLAG[i]) {
			printf("No, that is NOT the REAL INPUT!!\n");
			return 0;
		}
	}
	printf("That IS the REAL INPUT!!!\n");
	return 0;
}

