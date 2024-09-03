#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int FLAG[37] = {99,116,102,103,114,102,50,52,123,121,97,121,121,102,111,114,114,101,97,100,105,110,103,95,109,101,33,33,95,50,57,99,102,120,55,125,10}; 

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

